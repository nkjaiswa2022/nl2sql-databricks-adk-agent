import asyncio
import json
import os
from dotenv import load_dotenv
import logging

# MCP Server Imports
from mcp import types as mcp_types # Use alias to avoid conflict
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio # For running as a stdio server

from databricks import sql

# ADK Tool Imports
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.mcp_tool.conversion_utils import adk_to_mcp_tool_type

# --- Load Environment Variables (If ADK tools need them, e.g., API keys) ---
load_dotenv() # Create a .env file in the same directory if needed
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "mcp_server_activity.log")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH, mode="w"),
    ],
)

# --- Fetch Variables from Environment/dotEnv ---
access_token = os.getenv('DATABRICKS_ACCESS_TOKEN')
host = os.getenv('DATABRICKS_HOST')
http_path = os.getenv('DATABRICKS_HTTP_PATH')

# Enforce check to ensure all required variables were loaded
if not all([access_token, host, http_path]):
    missing_vars = []
    if not access_token:
        missing_vars.append('DATABRICKS_ACCESS_TOKEN')
    if not host:
        missing_vars.append('DATABRICKS_HOST')
    if not http_path:
        missing_vars.append('DATABRICKS_HTTP_PATH')
        
    error_message = (
        f"Missing required Databricks environment variables. "
        f"Please check your .env file or environment setup. Missing: {', '.join(missing_vars)}"
    )
    
    # Log the error and raise an exception to stop execution
    logging.critical(error_message)
    raise ValueError(error_message)

async def execute_databricks_query(query:str):
    """
    Connects to Databricks and executes a single SQL query.
    
    Args:
        query (str): The SQL query to execute.
        
    Returns:
        list: A list of dictionaries, where each dictionary is a row.
    """
    connection = None
    try:
        # Establish the connection
        connection = sql.connect(
            server_hostname=host,
            http_path=http_path,
            access_token=access_token,
	    _tls_verify_mode="none"
        )
        
        # Create a cursor to execute commands
        cursor = connection.cursor()
        
        logging.info(f"Executing query: {query}")
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Get column names to structure the output
        columns = [desc[0] for desc in cursor.description]
        
        # Convert the results to a list of dictionaries (more Pythonic)
        output_data = [dict(zip(columns, row)) for row in results]
        logging.info(f"output_data : {output_data}")
        return output_data

    except Exception as e:
        print(f"Error connecting to Databricks or executing query: {e}")
        return None
        
    finally:
        # Close the connection and cursor
        if connection:
            connection.close()

# --- Prepare the ADK Tool ---
print("Initializing ADK load_web_page tool...")
adk_tool_to_expose = FunctionTool(execute_databricks_query)
print(f"ADK tool '{adk_tool_to_expose.name}' initialized and ready to be exposed via MCP.")

# --- MCP Server Setup ---
print("Creating MCP Server instance...")
# Create a named MCP Server instance using the mcp.server library
app = Server("adk-tool-exposing-mcp-server")

# Implement the MCP server's handler to list available tools
@app.list_tools()
async def list_mcp_tools() -> list[mcp_types.Tool]:
    """MCP handler to list tools this server exposes."""
    print("MCP Server: Received list_tools request.")
    # Convert the ADK tool's definition to the MCP Tool schema format
    mcp_tool_schema = adk_to_mcp_tool_type(adk_tool_to_expose)
    print(f"MCP Server: Advertising tool: {mcp_tool_schema.name}")
    return [mcp_tool_schema]

# Implement the MCP server's handler to execute a tool call
@app.call_tool()
async def call_mcp_tool(
    name: str, arguments: dict
) -> list[mcp_types.Content]: # MCP uses mcp_types.Content
    """MCP handler to execute a tool call requested by an MCP client."""
    print(f"MCP Server: Received call_tool request for '{name}' with args: {arguments}")

    # Check if the requested tool name matches our wrapped ADK tool
    if name == adk_tool_to_expose.name:
        try:
            # Execute the ADK tool's run_async method.
            # Note: tool_context is None here because this MCP server is
            # running the ADK tool outside of a full ADK Runner invocation.
            # If the ADK tool requires ToolContext features (like state or auth),
            # this direct invocation might need more sophisticated handling.
            adk_tool_response = await adk_tool_to_expose.run_async(
                args=arguments,
                tool_context=None,
            )
            print(f"MCP Server: ADK tool '{name}' executed. Response: {adk_tool_response}")

            # Format the ADK tool's response (often a dict) into an MCP-compliant format.
            # Here, we serialize the response dictionary as a JSON string within TextContent.
            # Adjust formatting based on the ADK tool's output and client needs.
            response_text = json.dumps(adk_tool_response, indent=2)
            # MCP expects a list of mcp_types.Content parts
            return [mcp_types.TextContent(type="text", text=response_text)]

        except Exception as e:
            print(f"MCP Server: Error executing ADK tool '{name}': {e}")
            # Return an error message in MCP format
            error_text = json.dumps({"error": f"Failed to execute tool '{name}': {str(e)}"})
            return [mcp_types.TextContent(type="text", text=error_text)]
    else:
        # Handle calls to unknown tools
        print(f"MCP Server: Tool '{name}' not found/exposed by this server.")
        error_text = json.dumps({"error": f"Tool '{name}' not implemented by this server."})
        return [mcp_types.TextContent(type="text", text=error_text)]

# --- MCP Server Runner ---
async def run_mcp_stdio_server():
    """Runs the MCP server, listening for connections over standard input/output."""
    # Use the stdio_server context manager from the mcp.server.stdio library
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        print("MCP Stdio Server: Starting handshake with client...")
        await app.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name=app.name, # Use the server name defined above
                server_version="0.1.0",
                capabilities=app.get_capabilities(
                    # Define server capabilities - consult MCP docs for options
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
        print("MCP Stdio Server: Run loop finished or client disconnected.")

if __name__ == "__main__":
    print("Launching MCP Server to expose ADK tools via stdio...")
    try:
        asyncio.run(run_mcp_stdio_server())
    except KeyboardInterrupt:
        print("\nMCP Server (stdio) stopped by user.")
    except Exception as e:
        print(f"MCP Server (stdio) encountered an error: {e}")
    finally:
        print("MCP Server (stdio) process exiting.")
# --- End MCP Server ---
