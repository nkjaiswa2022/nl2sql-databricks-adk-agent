# NL2SQL Databricks ADK Agent

This project demonstrates an Agent Development Kit (ADK) agent that interacts with a Databricks. The interaction is facilitated by a Model Context Protocol (MCP) server that exposes tools to query databricks using natural language queries.

## Project Structure

```
adk-agent/
├── agent.py     # The ADK agent for the databricks
├── server.py    # The MCP server exposing databricks query tools       
├── __init__.py              
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

Set the environment variables. Create a `.env` file in the **root of the `adk-agent` folder** :

    ```env
    # .env
    GOOGLE_GENAI_USE_VERTEXAI=TRUE
    GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
    GOOGLE_CLOUD_LOCATION=<REGION>
    ```
    The `databricks_mcp_server.py` and `agent.py` will load this key.

### 5. Create the SQLite Database and Tables

The project includes a script to create and populate the SQLite database (`database.db`) with some initial tables (`users`, `todos`) and dummy data.

Navigate to the `local_mcp` directory and run the script:
```bash
cd local_mcp
python3 create_db.py
cd ..
```
This will create `local_mcp/database.db` if it doesn't already exist.

## Running the Agent and MCP Server


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

You should see log output from both the agent (if any) and the MCP server (in `local_mcp/mcp_server_activity.log`, and potentially to the console if you uncommented the stream handler in `server.py`).
