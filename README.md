# Intacct MCP Server (stdio Transport)

A Model Context Protocol (MCP) server for authenticating with Sage Intacct and making XML API requests, using stdio transport.

## Features

- **MCP Protocol Support**: Implements the JSON-RPC based MCP protocol
- **stdio Transport**: Direct communication via stdin/stdout
- **Intacct Authentication**: Handles login and session-based authentication
- **XML Request Handling**: Wraps your XML content with proper authentication

## Setup with uv

### 1. Create a Virtual Environment

```bash
# Create a virtual environment with Python 3.11
uv venv --python=3.11

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install dependencies using uv
uv sync
```

### 3. Configure Credentials

Copy the example environment file and edit it with your Intacct credentials:

```bash
# Copy the example file
cp .env.example .env

# Edit the .env file with your actual credentials
```

The `.env` file should contain your Intacct credentials:

```
INTACCT_SENDER_ID=your_sender_id
INTACCT_SENDER_PASSWORD=your_sender_password
INTACCT_COMPANY_ID=your_company_id
INTACCT_USER_ID=your_user_id
INTACCT_USER_PASSWORD=your_user_password
```

**Security Note**: The `.env` file contains sensitive credentials and is excluded from version control via `.gitignore`. Never commit your actual `.env` file to source control.

### 4. Run the Server

The server is designed to be launched as a subprocess by an MCP client (like Claude Desktop). However, you can test it manually:

```bash
uv run intacct_mcp_stdio.py
```

Then, you can enter JSON-RPC requests on stdin, one per line. For example:

```json
{"jsonrpc": "2.0", "id": "1", "method": "get_info"}
```

## Available Methods

### get_info

Returns information about the MCP server.

Example request:
```json
{"jsonrpc": "2.0", "id": "1", "method": "get_info"}
```

### list_tools

Returns a list of available tools.

Example request:
```json
{"jsonrpc": "2.0", "id": "1", "method": "list_tools"}
```

### tools/post_xml_to_intacct

Posts XML content to Intacct with proper authentication.

Example request:
```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "tools/post_xml_to_intacct",
  "params": {
    "credentials": {
      "sender_id": "your_sender_id",
      "sender_password": "your_sender_password",
      "session_id": "your_session_id"
    },
    "xml_content": "<function controlid=\"query1\"><readByQuery><object>CUSTOMER</object><fields>*</fields><query></query></readByQuery></function>",
    "parse_response": true
  }
}
```

### tools/get_intacct_session

Gets a new session ID from Intacct.

Example request:
```json
{
  "jsonrpc": "2.0",
  "id": "1", 
  "method": "tools/get_intacct_session",
  "params": {
    "credentials": {
      "sender_id": "your_sender_id",
      "sender_password": "your_sender_password",
      "company_id": "your_company_id",
      "user_id": "your_user_id",
      "user_password": "your_user_password"
    }
  }
}
```

## Integration with Claude Desktop

To use this MCP server with Claude Desktop:

1. Make sure the `intacct_mcp_stdio.py` script is executable
2. Register the server in Claude Desktop as a local server
3. Use the `mcp_config.json` file when adding the server

### MCP Configuration File

The `simple_mcp_config.json` file describes the MCP server capabilities and how to run it:

```json
{
  "id": "intacct-mcp",
  "name": "Intacct MCP Server",
  "description": "MCP server for Intacct API integration",
  "transport": "stdio",
  "server": {
    "command": "uv",
    "args": ["--directory", "${__dirname}", "run", "intacct_mcp_stdio.py"]
  }
}
```

This file tells Claude Desktop how to launch the server and what capabilities it provides.

## Troubleshooting

- Check the `intacct_mcp.log` file for detailed error messages
- Make sure your Intacct credentials are correct
- Verify that your XML content is properly formatted
