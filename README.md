# NL2SQL Databricks ADK Agent

This project demonstrates an Agent Development Kit (ADK) agent that interacts with a Databricks. The interaction is facilitated by a Model Context Protocol (MCP) server that exposes tools to query databricks using natural language queries.

## Project Structure

```
adk-agent/
├── databricks-agent/
│   ├── agent.py             # The ADK agent for the databricks
│   ├── databricks_mcp_server.py            # The MCP server exposing databricks tools
│   └── __init__.py             
├── .env                   # For Google PROJECT and Location 
├── requirements.txt       # Python dependencies
└── readme.md              # Instructions file
```

## Setup Instructions

### 1. Prerequisites
- Python 3.11 or newer
- Access to a terminal or command prompt

### 2. Create and Activate Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment (e.g., named .venv)
python3 -m venv .venv
```

Activate the virtual environment:

On macOS/Linux:
```bash
# Activate virtual environment
source .venv/bin/activate
```

On Windows:
```bash
# Activate virtual environment
.venv\Scripts\activate
```

### 3. Install Dependencies

Install all required Python packages using pip:

```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt
```

### 4. Set Up Gemini API Key (for the ADK Agent)

The ADK agent in this project uses a Gemini model. You'll need a Gemini API Access to you project.

Set the environment variables. Update an `nl2sql-databricks-adk-agent/adk-agent/databricks-agent/.env` [variable file](https://github.com/nkjaiswa2022/nl2sql-databricks-adk-agent/blob/main/adk-agent/databricks-agent/.env) with PROJECT_ID, REGION, DATABRICKS_ACCESS_TOKEN, DATABRICKS_HOST,DATABRICKS_HTTP_PATH

The `databricks_mcp_server.py` and `agent.py` will load these variables.

### 5. Create the databricks Tables and load data

We have pre-loaded the Databricks bakehouse_dataset sales tables into Databricks.

For details and documentation on the dataset, please refer to the `nl2sql-databricks-adk-agent/bakehouse_dataset/README.MD` [file](https://github.com/nkjaiswa2022/nl2sql-databricks-adk-agent/tree/main/bakehouse_dataset). 


### 6. Running the Agent and MCP Server


To run the agent:

1.  Ensure your virtual environment is active and you are in the root directory of the `adk-agent` project.
2.  Execute the using adk web:

    ```bash
    adk web
    ```

This will:
- Start the `agent.py` script.
- The agent, upon initializing the `MCPToolset`, will execute the `python3 databricks_server.py` command.
- The `databricks_mcp_sserver.py` (MCP server) will start and listen for tool calls from the agent via stdio.
- The agent will then be ready to process your instructions (which you would typically provide in a UI application).

You should see log output from both the agent (if any) and the MCP server (in `dataicks-agent/mcp_server_activity.log`, and potentially to the console if you uncommented the stream handler in `databricks-mcp-server.py`).
