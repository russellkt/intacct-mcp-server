import json
import sys
import uuid
import logging
import requests
import os
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional, Union, TypedDict, List, Tuple
import datetime

# Import MCP SDK
from mcp.server.fastmcp import FastMCP, Context

# Configure logging
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/intacct_mcp.log"),
        logging.StreamHandler(sys.stderr)
    ]
)
logger = logging.getLogger("intacct-mcp-server")

# Configuration
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get configuration from environment variables with defaults
INTACCT_ENDPOINT = os.environ.get("INTACCT_ENDPOINT", "https://api.intacct.com/ia/xml/xmlgw.phtml")
DTD_VERSION = os.environ.get("INTACCT_DTD_VERSION", "3.0")

# Get credentials from environment variables
ENV_CREDENTIALS = {
    "sender_id": os.environ.get("INTACCT_SENDER_ID", ""),
    "sender_password": os.environ.get("INTACCT_SENDER_PASSWORD", ""),
    "company_id": os.environ.get("INTACCT_COMPANY_ID", ""),
    "user_id": os.environ.get("INTACCT_USER_ID", ""),
    "user_password": os.environ.get("INTACCT_USER_PASSWORD", ""),
    "endpoint": INTACCT_ENDPOINT
}

# Log configuration but not credentials
logger.info(f"Using Intacct endpoint: {INTACCT_ENDPOINT}")
logger.info(f"Using DTD version: {DTD_VERSION}")
logger.info(f"Environment credentials loaded: {bool(ENV_CREDENTIALS['sender_id'])}")

# Create an MCP server with a standard name the CLI will recognize
mcp = FastMCP(
    "Intacct MCP Server",
    description="MCP server for authenticating with Intacct and making XML API requests",
    version="1.0.0"
)

# Custom type definitions
class IntacctCredentials(TypedDict, total=False):
    sender_id: str
    sender_password: str
    company_id: Optional[str]
    user_id: Optional[str]
    user_password: Optional[str]
    session_id: Optional[str]
    endpoint: Optional[str]

# Session cache to avoid unnecessary API calls
SESSION_CACHE = {}

def get_cached_session(company_id, user_id):
    """Get a cached session if available and not expired"""
    cache_key = f"{company_id}:{user_id}"
    if cache_key in SESSION_CACHE:
        session_data = SESSION_CACHE[cache_key]
        # Check if session is less than 1 hour old
        if (datetime.datetime.now() - session_data["timestamp"]).total_seconds() < 3600:
            return session_data["session_id"]
    return None

def cache_session(company_id, user_id, session_id):
    """Cache a session ID with timestamp"""
    cache_key = f"{company_id}:{user_id}"
    SESSION_CACHE[cache_key] = {
        "session_id": session_id,
        "timestamp": datetime.datetime.now()
    }

# Helper functions
def send_to_intacct(xml_request: str, endpoint: str = INTACCT_ENDPOINT) -> str:
    """Send XML request to Intacct API endpoint"""
    headers = {
        "Content-Type": "application/xml",
        "Accept": "application/xml"
    }
    
    # Ensure the XML request has the XML declaration
    if not xml_request.strip().startswith('<?xml'):
        xml_request = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_request
    
    # Log minimal request info instead of full XML
    logger.info(f"Sending request to Intacct endpoint: {endpoint}")
    
    response = requests.post(
        endpoint,
        data=xml_request,
        headers=headers
    )
    
    # Parse response to check for errors
    try:
        root = ET.fromstring(response.text)
        control = root.find('.//control')
        status = control.find('status').text if control and control.find('status') is not None else "unknown"
        
        if status.lower() == "success":
            logger.info(f"Received successful response from Intacct")
        else:
            # Log the full redacted response on error
            redacted_response = redact_credentials(response.text)
            logger.error(f"Error response from Intacct:\n{redacted_response}")
    except Exception as e:
        # If we can't parse the XML, log the redacted response
        redacted_response = redact_credentials(response.text)
        logger.error(f"Failed to parse Intacct response: {str(e)}\n{redacted_response}")
    
    response.raise_for_status()
    return response.text

def redact_credentials(xml_string: str) -> str:
    """Redact sensitive information from XML for logging"""
    # Simple redaction of common credential fields
    redacted = xml_string
    patterns = [
        (r'<password>.*?</password>', '<password>REDACTED</password>'),
        (r'<senderid>.*?</senderid>', '<senderid>REDACTED</senderid>'),
        (r'<userid>.*?</userid>', '<userid>REDACTED</userid>'),
        (r'<sessionid>.*?</sessionid>', '<sessionid>REDACTED</sessionid>')
    ]
    
    for pattern, replacement in patterns:
        import re
        redacted = re.sub(pattern, replacement, redacted)
    
    return redacted

def xml_to_dict(xml_string: str) -> Dict[str, Any]:
    """Convert XML string to dictionary recursively"""
    try:
        root = ET.fromstring(xml_string)
        return element_to_dict(root)
    except Exception as e:
        raise Exception(f"Failed to parse XML: {str(e)}")

def element_to_dict(element: ET.Element) -> Union[Dict[str, Any], str, None]:
    """Convert XML element to dictionary recursively"""
    result = {}
    
    # Add attributes
    if element.attrib:
        result.update(element.attrib)
    
    # Add children
    for child in element:
        child_result = element_to_dict(child)
        
        if child.tag in result:
            # If tag already exists, convert to list
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_result)
        else:
            result[child.tag] = child_result
    
    # Add text content if this is a leaf node
    if not result and element.text and element.text.strip():
        return element.text.strip()
    elif not result:
        return None
    
    return result

def check_response_status(parsed_response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check status at different levels of the Intacct response.
    Returns dict with success flag and error details if any.
    """
    # Check control status
    control = parsed_response.get("control", {})
    if isinstance(control, dict) and control.get("status") != "success":
        return {
            "success": False,
            "level": "control",
            "error_no": None,
            "description": control.get("description", "Control status failure")
        }
    
    # Check operation status
    operation = parsed_response.get("operation", {})
    if isinstance(operation, dict) and operation.get("status") == "failure":
        return {
            "success": False,
            "level": "operation",
            "error_no": None,
            "description": operation.get("description", "Operation status failure")
        }
    
    # Check authentication status
    authentication = operation.get("authentication", {}) if isinstance(operation, dict) else {}
    if isinstance(authentication, dict) and authentication.get("status") != "success":
        return {
            "success": False,
            "level": "authentication",
            "error_no": None,
            "description": authentication.get("description", "Authentication status failure")
        }
    
    # Check for batch response with multiple 'result' elements
    if isinstance(operation, dict) and "result" in operation:
        if isinstance(operation["result"], list):
            # Multiple results in a list
            all_errors = []
            for idx, result in enumerate(operation["result"]):
                if result.get("status") != "success":
                    all_errors.append({
                        "index": idx,
                        "function": result.get("function", "unknown"),
                        "controlid": result.get("controlid", "unknown"),
                        "description": result.get("description", "Function status failure"),
                        "error_no": result.get("errorno")
                    })
            
            if all_errors:
                return {
                    "success": False,
                    "level": "batch_result",
                    "error_no": all_errors[0].get("error_no"),
                    "description": f"Batch function failure: {all_errors[0].get('description')}",
                    "all_errors": all_errors
                }
        elif isinstance(operation["result"], dict):
            # Single result as a dict
            result = operation["result"]
            if result.get("status") != "success":
                return {
                    "success": False,
                    "level": "batch_result",
                    "error_no": result.get("errorno"),
                    "description": result.get("description", "Function status failure")
                }
    
    # Check for batch response with 'r' elements (alternative format)
    if isinstance(operation, dict) and "r" in operation:
        if isinstance(operation["r"], list):
            # Multiple results in a list
            all_errors = []
            for idx, result in enumerate(operation["r"]):
                if result.get("status") != "success":
                    all_errors.append({
                        "index": idx,
                        "function": result.get("function", "unknown"),
                        "controlid": result.get("controlid", "unknown"),
                        "description": result.get("description", "Function status failure"),
                        "error_no": result.get("errorno")
                    })
            
            if all_errors:
                return {
                    "success": False,
                    "level": "batch_result",
                    "error_no": all_errors[0].get("error_no"),
                    "description": f"Batch function failure: {all_errors[0].get('description')}",
                    "all_errors": all_errors
                }
        elif isinstance(operation["r"], dict):
            # Single result as a dict
            result = operation["r"]
            if result.get("status") != "success":
                return {
                    "success": False,
                    "level": "batch_result",
                    "error_no": result.get("errorno"),
                    "description": result.get("description", "Function status failure")
                }
    
    # If we got here and there's no result or r element in a batch context, that's an error
    if isinstance(operation, dict) and "result" not in operation and "r" not in operation:
        # This might be a batch request but missing the expected result structure
        return {
            "success": False,
            "level": "result",
            "error_no": None,
            "description": "Missing result element in response"
        }
    
    # If we got here, all checks passed
    return {"success": True}

def safe_parse_response(response_text):
    """
    Safely parse XML response to dictionary with proper error handling
    Returns tuple of (success, result, error_message)
    """
    try:
        parsed_response = xml_to_dict(response_text)
        return True, parsed_response, None
    except Exception as e:
        error_msg = f"Failed to parse XML response: {str(e)}"
        logger.error(error_msg)
        return False, None, error_msg

def extract_batch_results(parsed_response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract results from a batch response
    Returns a list of result dictionaries, one for each function in the batch
    """
    results = []
    operation = parsed_response.get("operation", {})
    
    # Check for multiple result elements (standard format)
    if isinstance(operation, dict) and "result" in operation:
        if isinstance(operation["result"], list):
            # Multiple results in a list
            for result in operation["result"]:
                results.append({
                    "status": result.get("status"),
                    "function": result.get("function"),
                    "controlid": result.get("controlid"),
                    "data": result.get("data")
                })
        elif isinstance(operation["result"], dict):
            # Single result as a dict
            result = operation["result"]
            results.append({
                "status": result.get("status"),
                "function": result.get("function"),
                "controlid": result.get("controlid"),
                "data": result.get("data")
            })
    
    # Check for r elements (alternative format)
    elif isinstance(operation, dict) and "r" in operation:
        if isinstance(operation["r"], list):
            # Multiple results in a list
            for result in operation["r"]:
                results.append({
                    "status": result.get("status"),
                    "function": result.get("function"),
                    "controlid": result.get("controlid"),
                    "data": result.get("data")
                })
        elif isinstance(operation["r"], dict):
            # Single result as a dict
            result = operation["r"]
            results.append({
                "status": result.get("status"),
                "function": result.get("function"),
                "controlid": result.get("controlid"),
                "data": result.get("data")
            })
    
    return results

def build_xml_request(credentials: IntacctCredentials, xml_content: str, transaction: bool = False) -> str:
    """Build an XML request with authentication"""
    # Determine authentication method
    if credentials.get("session_id"):
        # Using session authentication
        auth_xml = f"""
        <authentication>
            <sessionid>{credentials["session_id"]}</sessionid>
        </authentication>
        """
    elif all(k in credentials for k in ["company_id", "user_id", "user_password"]):
        # Using login authentication
        auth_xml = f"""
        <authentication>
            <login>
                <userid>{credentials["user_id"]}</userid>
                <companyid>{credentials["company_id"]}</companyid>
                <password>{credentials["user_password"]}</password>
            </login>
        </authentication>
        """
    else:
        raise Exception("Authentication information is incomplete")
    
    # Create control ID for this request
    control_id = str(uuid.uuid4())
    
    # Add transaction attribute if specified
    transaction_attr = ' transaction="true"' if transaction else ''
    
    # Build the full XML request - matching the format in the debug script
    xml_request = f"""
    <request>
        <control>
            <senderid>{credentials["sender_id"]}</senderid>
            <password>{credentials["sender_password"]}</password>
            <controlid>{control_id}</controlid>
            <uniqueid>false</uniqueid>
            <dtdversion>{DTD_VERSION}</dtdversion>
        </control>
        <operation{transaction_attr}>
            {auth_xml}
            <content>
                {xml_content}
            </content>
        </operation>
    </request>
    """
    
    return xml_request

def merge_credentials(user_credentials: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Merge user-provided credentials with environment credentials.
    Environment values are used as defaults if not provided by the user.
    """
    if user_credentials is None:
        user_credentials = {}
    
    # Start with environment credentials
    merged = ENV_CREDENTIALS.copy()
    
    # Override with user-provided credentials
    for key, value in user_credentials.items():
        if value:  # Only override if the value is not empty
            merged[key] = value
    
    return merged

def handle_intacct_error(error, context="Intacct operation"):
    """Centralized error handling for Intacct operations"""
    error_msg = f"Error in {context}: {str(error)}"
    logger.error(error_msg)
    return {"status": "error", "message": error_msg}

# MCP tool implementations
@mcp.tool()
async def post_xml_to_intacct(
    xml_content: str, 
    credentials: Optional[dict] = None,
    parse_response: bool = False,
    ctx: Context = None
) -> Dict[str, Any]:
    """
    Posts XML content to Intacct with proper authentication
    
    Args:
        xml_content: ONLY the <function>...</function> element block. DO NOT include full XML request
                    with authentication elements. The server will automatically wrap your function
                    element with the proper authentication and request structure.
        credentials: Optional override for Intacct credentials (sender_id, sender_password, etc.).
                    If not provided, values from environment variables will be used.
        parse_response: Whether to parse the XML response into JSON
        ctx: MCP context object
    
    Returns:
        Dict containing the response from Intacct
    
    Example:
        Correct usage:
        ```xml
        <function controlid="query1">
          <readByQuery>
            <object>CUSTOMER</object>
            <fields>*</fields>
            <query></query>
          </readByQuery>
        </function>
        ```
    """
    try:
        # Merge credentials
        merged_credentials = merge_credentials(credentials)
        
        # Log progress (visible in MCP Inspector)
        if ctx:
            await ctx.info("Building XML request with authentication")
        
        # Validate XML content
        if not xml_content:
            raise Exception("Missing required parameter: xml_content")
        
        # Build and send request
        xml_request = build_xml_request(merged_credentials, xml_content)
        
        if ctx:
            await ctx.info("Sending request to Intacct API")
        
        response_text = send_to_intacct(
            xml_request, 
            merged_credentials.get("endpoint", INTACCT_ENDPOINT)
        )
        
        # Parse the XML response to a dictionary
        success, parsed_response, error_msg = safe_parse_response(response_text)
        if not success:
            return {"status": "error", "message": error_msg}
        
        # Check response status at various levels
        status_check = check_response_status(parsed_response)
        if not status_check["success"]:
            error_msg = f"API Error ({status_check['level']}): {status_check['description']}"
            if status_check['error_no']:
                error_msg += f" (Error code: {status_check['error_no']})"
            
            # Include all errors if available
            all_errors = status_check.get("all_errors", [])
            if all_errors and len(all_errors) > 1:
                error_details = []
                for i, err in enumerate(all_errors[:5]):  # Limit to first 5 errors
                    desc = err.get("description") or "Unknown error"
                    error_details.append(f"{i+1}. {desc}")
                
                if error_details:
                    error_msg += "\n\nAdditional errors:\n" + "\n".join(error_details)
            
            return {"status": "error", "message": error_msg, "raw_response": response_text}
        
        if ctx:
            await ctx.info("Received successful response from Intacct")
        
        # Return response based on parse_response flag
        if parse_response:
            if ctx:
                await ctx.info("Parsing XML response to dictionary")
            return {
                "status": "success",
                "parsed_response": parsed_response
            }
        else:
            return {"status": "success", "xml_response": response_text}
    
    except Exception as e:
        logger.error(f"Error posting to Intacct: {str(e)}")
        return {"status": "error", "message": f"Error posting to Intacct: {str(e)}"}

@mcp.tool()
async def get_intacct_session(
    credentials: Optional[dict] = None,
    ctx: Context = None,
    debug: bool = False
) -> Dict[str, Any]:
    """
    Gets a new session ID from Intacct
    
    Args:
        credentials: Optional override for Intacct credentials 
                    (sender_id, sender_password, company_id, user_id, user_password).
                    If not provided, values from environment variables will be used.
        ctx: MCP context object
        debug: If true, returns full response for debugging
    
    Returns:
        Dict containing session information
    """
    try:
        # Merge credentials
        merged_credentials = merge_credentials(credentials)
        
        # Log progress
        if ctx:
            ctx.info("Validating credentials")
        
        # Validate required fields
        required_fields = ["sender_id", "sender_password", "company_id", "user_id", "user_password"]
        missing_fields = [field for field in required_fields if not merged_credentials.get(field)]
        if missing_fields:
            error_msg = f"Missing required credentials: {', '.join(missing_fields)}"
            logger.error(error_msg)
            raise Exception(error_msg)
        
        # Create the getAPISession function XML - match the debug script version
        session_function = f"""
        <function controlid="getSession-{uuid.uuid4()}">
            <getAPISession/>
        </function>
        """
        
        if ctx:
            ctx.info("Requesting new session from Intacct")
        
        # Build and send request
        xml_request = build_xml_request(merged_credentials, session_function)
        response_text = send_to_intacct(
            xml_request, 
            merged_credentials.get("endpoint", INTACCT_ENDPOINT)
        )
        
        if ctx:
            ctx.info("Parsing session response")
        
        # Parse the XML response to a dictionary
        success, parsed_response, error_msg = safe_parse_response(response_text)
        if not success:
            return {"status": "error", "message": error_msg}
        
        # If debug mode is enabled, return the full response for debugging
        if debug:
            return {
                "xml_response": response_text,
                "parsed_response": parsed_response
            }
        
        # Check status at various levels
        status_check = check_response_status(parsed_response)
        if not status_check["success"]:
            error_msg = f"API Error ({status_check['level']}): {status_check['description']}"
            if status_check["error_no"]:
                error_msg += f" (Error code: {status_check['error_no']})"
            logger.error(error_msg)
            raise Exception(error_msg)
        
        # Extract session info
        try:
            operation = parsed_response.get("operation", {})
            result = operation.get("result", {})
            
            if not result:
                logger.error("Missing result element in response")
                raise Exception("Missing result element in response")
            
            data = result.get("data", {})
            api = data.get("api", {})
            
            if not api:
                logger.error("Missing api element in result data")
                raise Exception("Missing api element in result data")
            
            session_id = api.get("sessionid")
            if not session_id:
                logger.error("Session ID not found in API response")
                raise Exception("Session ID not found in API response")
            
            # Return the session information
            return {
                "session_id": session_id,
                "endpoint": api.get("endpoint", INTACCT_ENDPOINT),
                "user_id": data.get("userid"),
                "company_id": data.get("companyid")
            }
        except Exception as e:
            logger.error(f"Error extracting session information: {str(e)}")
            raise Exception(f"Error extracting session information: {str(e)}")
    
    except Exception as e:
        logger.error(f"Error getting session: {str(e)}")
        raise Exception(f"Error getting session: {str(e)}")

@mcp.tool()
def test_intacct_connection(credentials: Optional[dict] = None) -> Dict[str, Any]:
    """
    Test the connection to Intacct API with detailed diagnostics
    
    Args:
        credentials: Optional override for Intacct credentials.
                    If not provided, values from environment variables will be used.
    
    Returns:
        Dict containing connection test results
    """
    try:
        # Merge credentials
        merged_credentials = merge_credentials(credentials)
        
        # Simple inspect function to test connection
        test_function = f"""
        <function controlid="inspect-{uuid.uuid4()}">
            <inspect>
                <object>*</object>
            </inspect>
        </function>
        """
        
        # Build the XML request
        xml_request = build_xml_request(merged_credentials, test_function)
        
        # Send the request
        response_text = send_to_intacct(
            xml_request, 
            merged_credentials.get("endpoint", INTACCT_ENDPOINT)
        )
        
        # Parse the XML response
        success, parsed_response, error_msg = safe_parse_response(response_text)
        if not success:
            return {"status": "error", "message": error_msg}
        
        # Check response status
        status_check = check_response_status(parsed_response)
        if not status_check["success"]:
            error_msg = f"API Error ({status_check['level']}): {status_check['description']}"
            if status_check["error_no"]:
                error_msg += f" (Error code: {status_check['error_no']})"
            return {"status": "error", "message": error_msg}
        
        # Return success with basic info
        return {
            "status": "success",
            "message": "Successfully connected to Intacct API",
            "endpoint": merged_credentials.get("endpoint", INTACCT_ENDPOINT),
            "dtd_version": DTD_VERSION,
            "timestamp": datetime.datetime.now().isoformat()
        }
    
    except Exception as e:
        logger.error(f"Connection test failed: {str(e)}")
        return {
            "status": "error",
            "message": f"Connection test failed: {str(e)}",
            "endpoint": merged_credentials.get("endpoint", INTACCT_ENDPOINT),
            "dtd_version": DTD_VERSION,
            "timestamp": datetime.datetime.now().isoformat()
        }

# Add a tool to get environment credentials status
@mcp.tool()
def get_credentials_status() -> Dict[str, Any]:
    """
    Get the status of environment credentials without exposing sensitive values
    
    Returns:
        Dict with status of each credential field
    """
    return {
        "sender_id_loaded": bool(ENV_CREDENTIALS["sender_id"]),
        "sender_password_loaded": bool(ENV_CREDENTIALS["sender_password"]),
        "company_id_loaded": bool(ENV_CREDENTIALS["company_id"]),
        "user_id_loaded": bool(ENV_CREDENTIALS["user_id"]),
        "user_password_loaded": bool(ENV_CREDENTIALS["user_password"]),
        "endpoint": ENV_CREDENTIALS["endpoint"]
    }

# Add example resources for reference documentation
@mcp.resource("intacct://schema/functions")
def get_functions_schema() -> str:
    """
    Returns documentation about common Intacct API functions
    """
    return """
    # Common Intacct API Functions
    
    ## General Ledger Functions
    - `get_glaccount`: Get general ledger account details
    - `create_glaccount`: Create a new general ledger account
    - `update_glaccount`: Update an existing general ledger account
    - `delete_glaccount`: Delete a general ledger account
    
    ## Accounts Payable Functions
    - `get_bill`: Get bill details
    - `create_bill`: Create a new bill
    - `update_bill`: Update an existing bill
    - `delete_bill`: Delete a bill
    
    ## Accounts Receivable Functions
    - `get_invoice`: Get invoice details
    - `create_invoice`: Create a new invoice
    - `update_invoice`: Update an existing invoice
    - `delete_invoice`: Delete an invoice
    """

@mcp.resource("intacct://examples/session")
def get_session_example() -> str:
    """
    Returns example code for getting a session from Intacct
    """
    return """
    # Example: Getting a session from Intacct
    
    ```json
    {
      "credentials": {
        "sender_id": "YOUR_SENDER_ID",
        "sender_password": "YOUR_SENDER_PASSWORD",
        "company_id": "YOUR_COMPANY_ID",
        "user_id": "YOUR_USER_ID",
        "user_password": "YOUR_USER_PASSWORD"
      }
    }
    ```
    
    This will return a session ID that can be used for subsequent requests.
    You can also configure these values in your .env file to avoid entering them each time.
    """

@mcp.resource("intacct://examples/get_gl_accounts")
def get_gl_accounts_example() -> str:
    """
    Returns example XML for getting general ledger accounts
    """
    return """
    # Example: Get General Ledger Accounts
    
    ```xml
    <function controlid="getGLAccounts">
        <get_list object="glaccount">
            <filter>
                <greaterthanorequalto>
                    <field>whenmodified</field>
                    <value>2023-01-01</value>
                </greaterthanorequalto>
            </filter>
            <fields>ACCOUNTNO,TITLE,STATUS,NORMALBALANCE,ACCOUNTTYPE</fields>
        </get_list>
    </function>
    ```
    
    Use this with the `post_xml_to_intacct` tool to retrieve GL accounts.
    """

@mcp.resource("intacct://setup/environment")
def get_environment_setup() -> str:
    """
    Returns instructions for setting up environment variables
    """
    return """
    # Setting Up Environment Variables
    
    Create a `.env` file in your project directory with the following variables:
    
    ```
    INTACCT_SENDER_ID=your_sender_id
    INTACCT_SENDER_PASSWORD=your_sender_password
    INTACCT_COMPANY_ID=your_company_id
    INTACCT_USER_ID=your_user_id
    INTACCT_USER_PASSWORD=your_user_password
    INTACCT_ENDPOINT=https://api.intacct.com/ia/xml/xmlgw.phtml
    INTACCT_DTD_VERSION=3.0
    ```
    
    These environment variables will be used as defaults if you don't provide credentials explicitly.
    """

@mcp.resource("intacct://troubleshooting")
def get_troubleshooting() -> str:
    """
    Returns troubleshooting tips for common Intacct API issues
    """
    return """
    # Troubleshooting Intacct API Connectivity
    
    ## Common Issues
    
    1. **Authentication Failures**
       - Verify your sender credentials (sender ID and password)
       - Verify your user credentials (company ID, user ID, and password)
       - Check if your user account has API access permissions
    
    2. **Endpoint Issues**
       - Ensure you're using the correct endpoint URL
       - Check for any network restrictions (firewalls, proxies, etc.)
    
    3. **XML Formatting Issues**
       - Validate your XML content against Intacct's specifications
       - Ensure special characters are properly escaped
    
    ## Debugging Steps
    
    1. Use the `test_intacct_connection` tool to test basic connectivity
    2. Run the `get_intacct_session` tool with debug=true to see the full response
    3. Check the logs at logs/intacct_mcp.log for detailed error messages
    
    ## API Documentation
    
    For more information, refer to the Sage Intacct Web Services documentation:
    https://developer.intacct.com/web-services/
    """

@mcp.tool()
async def batch_xml_to_intacct(
    functions: List[str],
    credentials: Optional[dict] = None,
    parse_response: bool = False,
    transaction: bool = False,
    ctx: Context = None
) -> Dict[str, Any]:
    """
    Posts multiple XML functions to Intacct in a single batch request
    
    Args:
        functions: List of XML function strings to be executed in a batch
        credentials: Optional override for Intacct credentials
        parse_response: Whether to parse the XML response into JSON
        transaction: Whether to treat all functions as a single transaction (if one fails, all are rolled back)
        ctx: MCP context object
    
    Returns:
        Dict containing the response from Intacct
    """
    try:
        # Merge credentials
        merged_credentials = merge_credentials(credentials)
        
        # Combine functions into a single content block
        batch_content = "\n".join(functions)
        
        if ctx:
            await ctx.info(f"Sending batch request with {len(functions)} functions" + 
                          (", as a transaction" if transaction else ""))
        
        # Build and send request with transaction attribute if specified
        xml_request = build_xml_request(merged_credentials, batch_content, transaction)
        response_text = send_to_intacct(
            xml_request, 
            merged_credentials.get("endpoint", INTACCT_ENDPOINT)
        )
        
        # Parse the XML response to a dictionary
        success, parsed_response, error_msg = safe_parse_response(response_text)
        if not success:
            return {"status": "error", "message": error_msg}
        
        # Check response status at various levels
        status_check = check_response_status(parsed_response)
        if not status_check["success"]:
            error_msg = f"API Error ({status_check['level']}): {status_check['description']}"
            if status_check["error_no"]:
                error_msg += f" (Error code: {status_check['error_no']})"
            
            # Include all errors if available
            all_errors = status_check.get("all_errors", [])
            if all_errors and len(all_errors) > 1:
                error_details = []
                for i, err in enumerate(all_errors[:5]):  # Limit to first 5 errors
                    desc = err.get("description") or "Unknown error"
                    error_details.append(f"{i+1}. {desc}")
                
                if error_details:
                    error_msg += "\n\nAdditional errors:\n" + "\n".join(error_details)
            
            return {"status": "error", "message": error_msg, "raw_response": response_text}
        
        if ctx:
            await ctx.info("Received successful response from Intacct")
        
        # Return response based on parse_response flag
        if parse_response:
            if ctx:
                await ctx.info("Parsing batch XML response to dictionary")
            
            # Extract individual results from the batch response
            batch_results = extract_batch_results(parsed_response)
            
            return {
                "status": "success",
                "batch_results": batch_results
            }
        else:
            return {"status": "success", "xml_response": response_text}
    
    except Exception as e:
        logger.error(f"Error in batch request: {str(e)}")
        return {"status": "error", "message": f"Error in batch request: {str(e)}"}

# Run the server
if __name__ == "__main__":
    mcp.run()
