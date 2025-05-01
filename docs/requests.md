Title: XML Requests

URL Source: https://developer.intacct.com/web-services/requests/

Markdown Content:
*   [control element](https://developer.intacct.com/web-services/requests/#control-element)
    *   [senderid and password elements (required)](https://developer.intacct.com/web-services/requests/#senderid-and-password-elements-required)
    *   [controlid element (required)](https://developer.intacct.com/web-services/requests/#controlid-element-required)
    *   [uniqueid element (optional)](https://developer.intacct.com/web-services/requests/#uniqueid-element-optional)
    *   [dtdversion element (required)](https://developer.intacct.com/web-services/requests/#dtdversion-element-required)
    *   [includewhitespace element (optional)](https://developer.intacct.com/web-services/requests/#includewhitespace-element-optional)
    *   [policyid element (optional)](https://developer.intacct.com/web-services/requests/#policyid-element-optional)
    *   [showadditionalerrorinfo element (optional)](https://developer.intacct.com/web-services/requests/#showadditionalerrorinfo-element-optional)
*   [operation element](https://developer.intacct.com/web-services/requests/#operation-element)
    *   [transaction attribute (optional)](https://developer.intacct.com/web-services/requests/#transaction-attribute-optional)
*   [authentication element](https://developer.intacct.com/web-services/requests/#authentication-element)
    *   [login element (optional)](https://developer.intacct.com/web-services/requests/#login-element-optional)
    *   [sessionid element (optional)](https://developer.intacct.com/web-services/requests/#sessionid-element-optional)
*   [content element](https://developer.intacct.com/web-services/requests/#content-element)
    *   [function element](https://developer.intacct.com/web-services/requests/#function-element)
    *   [Control ID for a request versus control ID attribute of a function](https://developer.intacct.com/web-services/requests/#control-id-for-a-request-versus-control-id-attribute-of-a-function)
*   [What’s next?](https://developer.intacct.com/web-services/requests/#whats-next)

* * *

An XML request document establishes various credentials and includes the API function calls to execute via the gateway.

The following example highlights the basic structure of a request.

*   The main element, `request`, organizes the functionality into child elements.
*   The first child is a `control` element that includes your Web Services credentials and applies to the entire request.
*   This is followed by an `operation` element that authenticates access to a Sage Intacct company and provides the API calls as the content.

![Image 1: example of an XML request](https://developer.intacct.com/images/web-services/xml_body.png)

* * *

control element
---------------

Supplies the Web Services credentials and provides information about the request as a whole. It includes the following child elements:

### senderid and password elements (required)

Permanent Web Services sender ID and corresponding password, for example:

```
<senderid>jsmith_user</senderid>  
<password>agfh!@34</password>
```

Note that both the sender ID and password are case sensitive.

**Important:** Your Web Services sender ID must be [authorized](https://developer.intacct.com/support/faq/#why-am-i-getting-an-error-about-an-invalid-web-services-authorization) for use in a given company.

### controlid element (required)

Identifier used by the client application to match a request to its response. Clients can use a GUID or other identification system, for example:

```
<controlid>7a4ce54d-63d4-4433-bf09-92fcb00bab8d</controlid>
```

**Important Notes**

*   The value of this element is not checked for uniqueness, which means that a request may be submitted twice without an error. Using a timestamp for this value is a good way to differentiate similar requests. If you want to provide a check for uniqueness, use `uniqueid` below.
    
*   The use of `controlid` is particularly important when using [asynchronous requests](https://developer.intacct.com/web-services/sync-vs-async/).
    
*   Do not confuse the `controlid` _element_ here with the `controlid` _attribute_ of a function—see [below](https://developer.intacct.com/web-services/requests/#control-id-for-a-request-versus-control-id-attribute-of-a-function) for more information.
    

### uniqueid element (optional)

Specifies whether a request can be submitted more than once without an error.

*   When set to `true`, which is the default, a request cannot be repeated. The `controlid` attribute of the `<function>` element will be checked to determine if the operation was previously executed and completed.
    
*   When set to `false`, the system allows the operation to execute any number of times.
    

```
<uniqueid>false</uniqueid> 
```

Many _read_ operations have no meaningful side effects on the state of the system. On the other hand, many financial transactions do cause a meaningful change in the state of the system. It is common to set `uniqueid` to `false` for operations that contain exclusively read operations and `true` for operations that contain create or update functions. While working in test mode, you can set `uniqueid` to `false` for expediency.

### dtdversion element (required)

Identifies the version of the API in use. The value of `3.0` (the current version) is strongly recommended as it provides access to both the generic functions and the object-specific functions.

```
<dtdversion>3.0</dtdversion>
```

### includewhitespace element (optional)

Specifies whether responses should be formatted with whitespace and carriage returns for readability or if these marks should be omitted to improve performance and reduce the response size. The formatting is not needed if the response will be loaded into an XML parser anyway.

*   When set to `true`, which is the default, responses are formatted for readability.
    
*   When set to `false`, responses do not include formatting.
    

```
<includewhitespace>false</includewhitespace> 
```

### policyid element (optional)

Chooses asynchronous communication with the gateway by designating an existing transport policy (agreed upon by the client and Sage Intacct). With asynchronous communication, the response is returned via a _new_ HTTP connection using the parameters indicated in the transport policy settings.

```
<policyid>myAsyncPolicy</policyid>
```

If you do not include a `policyid`, synchronous communication is used. With synchronous communication, the response is returned in the _same_ HTTP connection as the request.

**Note:** If you need to create a transport policy, open a [support case](https://developer.intacct.com/support/).

### showadditionalerrorinfo element (optional)

When set to `true`, error responses will include an `<additionalinfo>` section containing a unique error ID and other information:

*   `<errorid>` - Unique error ID.
*   `<category>` - The type of problem, such as “Invalid permission.”
*   `<target>` - Information regarding what caused the error. For example, object name, field name, module name, etc.
*   `<description>` - Possible additional information.
    *   `<messageid>` -
    *   `<category>` -
    *   `<target>` -
    *   `<placeholders>` -
*   `<cdescription>` - Possible additional information.
    *   `<messageid>` -
    *   `<target>` -
    *   `<placeholders>` -
*   `<correction>` - Possible additional information.
    *   `<messageid>` -
    *   `<category>` -
    *   `<target>` -
    *   `<placeholders>` -

`<target>` can be set at both error and message levels, and thus will be returned at both error level and message levels in error response

All optional elements will be returned with empty values if there is no information available.

| Default Error Response | Error Response with `showadditionalerrorinfo` set to true |
| --- | --- |
| 
```
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <control>
    <status>success</status>
    <senderid>partner1</senderid>
    <controlid>ControlIdHere</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
  </control>
  <operation>
    <authentication>
      <status>success</status>
      <userid>jjones</userid>
      <companyid>Zzyzz Delivery</companyid>
      <locationid></locationid>
      <sessiontimestamp>2023-04-25T00:50:25+00:00</sessiontimestamp>
      <sessiontimeout>2023-04-25T03:00:25+00:00</sessiontimeout>
    </authentication>
    <result>
      <status>failure</status>
      <function>create</function>
      <controlid>testFunctionId</controlid>
      <data listtype="objects" count="0"/>
      <errormessage>
        <error>
          <errorno>BL01001973</errorno>
          <description>Duplicate account number</description>
          <description2>The account number &#039;5000.11&#039; already exists [Support ID: EsppO%7EZEcj0DEGV_L5hm95Ec91twAAABA]</description2>
          <correction>Enter unique account number</correction>
        </error>
        <error>
          <errorno>BL01001973</errorno>
          <description></description>
          <description2>Could not create GL Account record.</description2>
          <correction></correction>
        </error>
      </errormessage>
    </result>
  </operation>
</response>
```



 | 

```
<?xml version="1.0" encoding="UTF-8"?>
<response>
  <control>
    <status>success</status>
    <senderid>partner1</senderid>
    <controlid>ControlIdHere</controlid>
    <uniqueid>false</uniqueid>
    <dtdversion>3.0</dtdversion>
  </control>
  <operation>
    <authentication>
      <status>success</status>
      <userid>jjones</userid>
      <companyid>Zzyzz Delivery</companyid>
      <locationid></locationid>
      <sessiontimestamp>2023-04-25T00:52:34+00:00</sessiontimestamp>
      <sessiontimeout>2023-04-25T03:02:34+00:00</sessiontimeout>
    </authentication>
    <result>
      <status>failure</status>
      <function>create</function>
      <controlid>testFunctionId</controlid>
      <data listtype="objects" count="0"/>
      <errormessage>
        <error>
          <errorno>BL01001973</errorno>
          <description>Duplicate account number</description>
          <description2>The account number &#039;5000.11&#039; already exists [Support ID: d3DJI%7EZEckUDEkV9t5KUU5mpPrrQAAAAk]</description2>
          <correction>Enter unique account number</correction>
          <additionalinfo>
            <errorid>GL-0493</errorid>
            <category>Duplication Prevention</category>
            <target domain="" requestinfo="d3DJI%7EZEckUDEkV9t5KUU5mpPrrQAAAAk" object="" field="" businessinfo=""/>
            <description>
              <messageid>IA.DUPLICATE_ACCOUNT_NUMBER</messageid>
              <target domain="" requestinfo="" object="" field="" businessInfo=""/>
              <placeholders></placeholders>
            </description>
            <cdescription>
                <messageid>IA.THE_ACCOUNT_NUMBER_ALREADY_EXISTS</messageid>
                <target domain="" requestinfo="[Support ID: d3DJI%7EZEckUDEkV9t5KUU5mpPrrQAAAAk]" object="" field="" businessInfo=""/>
                <placeholders>
                  <placeholder name="ACCOUNTNO" value="5000.11"/>
                </placeholders>
            </cdescription>
            <correction>
              <messageid>IA.ENTER_UNIQUE_ACCOUNT_NUMBER</messageid>
              <target domain="" requestinfo="" object="" field="" businessInfo=""/>
              <placeholders></placeholders>
            </correction>
          </additionalinfo>
        </error>
        <error>
          <errorno>BL01001973</errorno>
          <description></description>
          <description2>Could not create GL Account record.</description2>
          <correction></correction>
          <additionalinfo>
            <errorid>GL-0504</errorid>
            <category>Unable to create record.</category>
            <target domain="" requestinfo="d3DJI%7EZEckUDEkV9t5KUU5mpPrrQAAAAk" object="" field="" businessinfo=""/>
            <description>
              <messageid></messageid>
              <category></category>
              <target domain="" object="" field="" businessInfo=""/>
              <placeholders></placeholders>
            </description>
            <cdescription>
              <messageid>IA.COULD_NOT_CREATE_GL_ACCOUNT_RECORD</messageid>
              <target domain="" requestinfo="" object="" field="" businessInfo=""/>
              <placeholders></placeholders>
            </cdescription>
            <correction>
              <messageid></messageid>
              <category></category>
              <target domain="" object="" field="" businessInfo=""/>
              <placeholders></placeholders>
            </correction>
          </additionalinfo>
        </error>
      </errormessage>
    </result>
  </operation>
</response>
```



 |

* * *

operation element
-----------------

Supplies the user authentication for a particular shared or distributed company and provides the content for the request. The content includes one or more API function calls.

The `operation` element has an optional attribute for setting transaction integrity.

### transaction attribute (optional)

Specifies whether all the functions in the operation block represent a single transaction.

*   When set to `true`, all of the functions are treated as a single transaction. If one function fails, all previously executed functions within the operation are rolled back. This is useful for groups of functions that rely on each other to change information in the database.
    
*   When set to `false`, which is the default, functions execute independently. If one function fails, others still proceed.
    

```
<operation transaction="true">
```

* * *

authentication element
----------------------

Provides credentials for access to the target company. You can provide company login credentials or a valid session ID.

### login element (optional)

Chooses to authenticate the request using login credentials. How you provide login credentials varies depending on your company setup. Some examples are below.

**For a standalone company**

Provide a user ID, company ID, and password to log in to a standalone company. This is the same information you use when you log into the Sage Intacct UI.

```
<login>
  <userid>myUserId</userid>
  <companyid>myCompanyId</companyid>
  <password>myPassword</password>
</login>
```

**For a multi-entity shared company**

Add a location ID to log into a multi-entity shared company. Entities are typically different locations of a single company.

```
<login>
  <userid>myUserId</userid>
  <companyid>myParentCompanyId</companyid>
  <password>myPassword</password>
  <locationid>entityId</locationid>
</login>
```

**For console _slide in_**

You need a client ID to log into a distributed child company. The user ID and password in this scenario are for access to the console, not the target/client company itself.

```
<login>
  <userid>myExtUserId</userid>
  <companyid>myConsoleId</companyid>
  <password>myPassword</password>
  <clientid>clientCompanyId</clientid>
  <locationid>entityId</locationid>
</login>
```

Here’s an alternative way of providing the same credentials:

```
<login>
  <userid>myExtUserId</userid>
  <companyid>myConsoleId|clientCompanyId|entityId</companyid>
  <password>myPassword</password>
</login>
```

### sessionid element (optional)

Chooses to authenticate the request using a session ID, which is the preferred way to make repeated API requests. A session ID is always tied to a set of user credentials and a unique endpoint.

```
<sessionid>validSessionId</sessionid>
```

You can get a session ID and unique endpoint using [getAPISession](https://developer.intacct.com/api/company-console/api-sessions/).

For testing purposes, you can use the **Generate API Session** request that is included with the downloadable Sage Intacct API collection:

[Download](https://developer.intacct.com/downloads/Intacct_API_Postman_Collection.zip)

* * *

content element
---------------

Supplies one or more `function` elements to be executed.

### function element

Supplies one or more API calls.

**Note:** The XML API includes two categories of functions, generic and object-specific. For more information, see [About API Functions](https://developer.intacct.com/web-services/functions/).

#### controlid attribute

Identifier for the function that can be used to correlate the results from the gateway with your calls. To assure transaction idempotence, use unique values such as GUIDs or sequenced numbers.

```
<function controlid="x99876">
```

#### _function name_

The function name defines the operation to execute, and the sub-elements of the function provide the necessary input data.

The following example uses a generic `create` function to create two standard and one custom (`COUNTER`) object.

```
<function controlid="3G2DFC86-9899-4283-360X-C789142D2801">
  <create>
    <LOCATION>
      <LOCATIONID>23</LOCATIONID>
      <NAME>Bags and More</NAME>
    </LOCATION>
    <VENDOR>
      <VENDORID>Vend-201</VENDORID>
      <NAME>Style Messenger Bags</NAME>
      <DISPLAYCONTACT>
        <MAILADDRESS>
          <COUNTRYCODE>US</COUNTRYCODE>
        </MAILADDRESS>
      </DISPLAYCONTACT>
    </VENDOR>
    <COUNTER>
      <ID>2389</ID>
      <DESCRIPTION>Item count</DESCRIPTION>
    </COUNTER>
  </create>
</function>
```

### Control ID for a request versus control ID attribute of a function

Keep in mind that there are two places in a request where control IDs are used, and they serve different purposes.

The `<controlid>` _element_ in the `<control>` block is simply used by a client to match a request with a response. The `controlid` _attribute_ of a `<function>` element is required for uniquely identifying functions for recovery purposes.

![Image 2: control ID for the request versus control IDs for functions](https://developer.intacct.com/images/web-services/control-id-compares.png)

* * *

What’s next?
------------

*   Learn about [XML responses](https://developer.intacct.com/web-services/responses/).
*   Learn about [handling errors](https://developer.intacct.com/web-services/error-handling/).

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

