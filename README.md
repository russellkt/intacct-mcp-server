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

## Batch Operations and Transactions

The Intacct API supports sending multiple function elements in a single request, which can improve performance when you need to execute multiple operations.

### Basic Batch Operations

To send multiple operations in a single request, use the `batch_xml_to_intacct` tool with an array of function elements:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "tools/batch_xml_to_intacct",
  "params": {
    "functions": [
      "<function controlid=\"query1\"><query><object>VENDOR</object><select><field>VENDORID</field><field>NAME</field></select></query></function>",
      "<function controlid=\"query2\"><query><object>APBILL</object><select><field>RECORDNO</field><field>VENDORNAME</field></select></query></function>"
    ],
    "parse_response": true
  }
}
```

### Transaction Support

When creating or updating related records, you can ensure all operations succeed or fail together by using the `transaction` parameter:

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "tools/batch_xml_to_intacct",
  "params": {
    "functions": [
      "<function controlid=\"create1\"><create><VENDOR>...</VENDOR></create></function>",
      "<function controlid=\"create2\"><create><CONTACT>...</CONTACT></create></function>"
    ],
    "parse_response": true,
    "transaction": true
  }
}
```

When `transaction` is set to `true`, all functions are treated as a single transaction. If any function fails, all changes are rolled back, ensuring data consistency.

## Limitations

### Data Passing Between Functions

Intacct does not support passing data between functions in the same batch request. Each function in a batch is processed independently, and there's no way for one function to use the results of another function in the same request.

If you need to use the results from one operation to inform another operation, you must:
1. Send the first request
2. Process the response in your application
3. Use that data to construct a second request
4. Send the second request separately

### Query Pagination

For queries that return large result sets, Intacct uses pagination. The default page size is typically 100 records, but you can specify a different page size using the `pagesize` element in your query.

To retrieve additional pages, you'll need to use the `offset` parameter in subsequent queries or use the `readMore` function with the `resultId` from the previous response.

## Response Format

When using the MCP tools, you can control the response format using the `parse_response` parameter:

### XML Response (Default)

When `parse_response` is set to `false` (default), the response will contain only the raw XML:

```json
{
  "status": "success",
  "xml_response": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>..."
}
```

### JSON Response

When `parse_response` is set to `true`, the response will contain only the parsed JSON structure:

```json
{
  "status": "success",
  "parsed_response": {
    "control": {...},
    "operation": {...}
  }
}
```

For batch operations, the response will include an array of results:

```json
{
  "status": "success",
  "batch_results": [
    {
      "status": "success",
      "function": "query",
      "controlid": "query1",
      "data": {...}
    },
    {
      "status": "success",
      "function": "query",
      "controlid": "query2",
      "data": {...}
    }
  ]
}
```

### Error Responses

Error responses will include an error message and, for debugging purposes, may include the raw XML response:

```json
{
  "status": "error",
  "message": "API Error (authentication): Authentication failed",
  "raw_response": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>..."
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
"intacct-mcp": {
    "command": "uv",
    "args": [
      "--directory",
      "/ABSOLUTE/PATH/TO/DIRECTORY",
      "run",
      "intacct_mcp_stdio.py"
    ]
  }
```

This file tells Claude Desktop how to launch the server and what capabilities it provides.

## Troubleshooting

If you encounter issues with the MCP server or Intacct API:

1. Check the `logs/intacct_mcp.log` file for detailed error messages
2. Verify your Intacct credentials in the `.env` file
3. Ensure your XML content follows the correct format (only the `<function>` element)
4. For authentication issues, try getting a new session using `get_intacct_session`
5. Use the `test_intacct_connection` tool to diagnose connectivity problems

For more detailed troubleshooting information, use the `tools/get_troubleshooting` method.
