Title: Applications

URL Source: https://developer.intacct.com/api/platform-services/applications/

Markdown Content:
*   [Get Platform Services Application Object Definition](https://developer.intacct.com/api/platform-services/applications/#get-platform-services-application-object-definition)
*   [Query and List Platform Services Applications](https://developer.intacct.com/api/platform-services/applications/#query-and-list-platform-services-applications)
*   [Query and List Platform Services Applications (Legacy)](https://developer.intacct.com/api/platform-services/applications/#query-and-list-platform-services-applications-legacy)
*   [Get Platform Services Application](https://developer.intacct.com/api/platform-services/applications/#get-platform-services-application)
*   [Get Platform Services Application by ID](https://developer.intacct.com/api/platform-services/applications/#get-platform-services-application-by-id)
*   [Install Platform Services Application](https://developer.intacct.com/api/platform-services/applications/#install-platform-services-application)

* * *

A Platform Services application is an XML wrapper around a group of objects, menus, and portals that work together to fulfill a function.

* * *

Get Platform Services Application Object Definition
---------------------------------------------------

#### `lookup`

> List all the fields and relationships for the Platform Services application object:

```
<lookup>
    <object>PTAPPLICATION</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PTAPPLICATION` |

* * *

Query and List Platform Services Applications
---------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and application name for each Platform Services application:

```
<query>
    <object>PTAPPLICATION</object>
    <select>
        <field>RECORDNO</field>
        <field>APPLICATIONNAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PTAPPLICATION` |
| filter | Optional | object | [Filter expression](https://developer.intacct.com/web-services/queries/#filter) to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, `VENDOR.CREDITLIMIT` on APBILL). |
| select | Required | sequence | The names of the fields that you want included in the response, and an optional [aggregate function](https://developer.intacct.com/web-services/queries/#aggregate-functions) such as `count` or `sum`. Returning all fields is not supported. |
| orderby | Optional | object | Provide an `order` element with a field name and choose an ascending or descending [sort order](https://developer.intacct.com/web-services/queries/#order-by), for example:  
```
<order>  
   <field>RECORDNO</field>   
   <descending/>   
</order>
``` |
| options | Optional | object | [Query options](https://developer.intacct.com/web-services/queries/#options):
*   Set the `caseinsensitive` element to `true` for a case-insensitive query  
     `<caseinsensitive>true</caseinsensitive>`
*   In a multi-entity company, set the `showprivate` element to `true` to query data in private entities:  
     `<showprivate>true</showprivate>`
*   Specify the `returnformat` for the response: `xml` (default), `json`, or `csv`  
     `<returnformat>json</returnformat>`

 |
| pagesize | Optional | integer | Maximum number of matching objects to return in the response, between `1` and `2000` items (Default: `100`) |
| offset | Optional | integer | Point at which to start indexing into records (Default: `0`) |

#### `Response`

`PTAPPLICATION`

> The above function returns data structured like this:

```
<PTAPPLICATION>
    <RECORDNO>10014</RECORDNO>
    <APPLICATIONNAME>T2 Additional features</APPLICATIONNAME>
</PTAPPLICATION>
<PTAPPLICATION>
    <RECORDNO>10016</RECORDNO>
    <APPLICATIONNAME>MCA My Conferencing App</APPLICATIONNAME>
</PTAPPLICATION>
```

* * *

Query and List Platform Services Applications (Legacy)
------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PTAPPLICATION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PTAPPLICATION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Platform Services Application
---------------------------------

#### `read`

```
<read>
    <object>PTAPPLICATION</object>
    <keys>10016</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PTAPPLICATION` |
| keys | Required | string | Comma-separated list of platform Services application `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

#### `Response`

`PTAPPLICATION`

> The above function returns data structured like this:

```
<PTAPPLICATION>
    <RECORDNO>10016</RECORDNO>
    <APPLICATIONNAME>MCA My Conferencing App</APPLICATIONNAME>
    <ORDERNO>6</ORDERNO>
    <PROPERTIES>
        <isDeployed>true</isDeployed>
        <isManaged>false</isManaged>
        <OBJECTS>
            <OBJECT>
                <ID>10056</ID>
                <Name>MCA_attendee</Name>
                <isCustom>true</isCustom>
            </OBJECT>
            <OBJECT>
                <ID>10057</ID>
                <Name>MCA_conference_level</Name>
                <isCustom>true</isCustom>
            </OBJECT>
            <OBJECT>
                <ID>10058</ID>
                <Name>MCA_presenter</Name>
                <isCustom>true</isCustom>
            </OBJECT>
        </OBJECTS>
    </PROPERTIES>
    <DESCRIPTION></DESCRIPTION>
    <VERSION>1.2</VERSION>
    <CREATEDBY>48</CREATEDBY>
    <WHENCREATED>2020-06-11T17:52:00Z</WHENCREATED>
    <MODIFIEDBY>48</MODIFIEDBY>
    <WHENMODIFIED>2020-06-11T17:52:00Z</WHENMODIFIED>
    <ORIGINALID>43254845@10013</ORIGINALID>
</PTAPPLICATION>
```

* * *

Get Platform Services Application by ID
---------------------------------------

#### `readByName`

```
<readByName>
    <object>PTAPPLICATION</object>
    <keys>MCA My Conferencing App</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PTAPPLICATION` |
| keys | Required | string | Comma-separated list of platform Services application name to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Install Platform Services Application
-------------------------------------

As you build and deploy Platform Services applications on client companies, the need to programmatically install updates eventually arises. Installing or updating an application involves first publishing the application from the Sage Intacct UI to create the XML definition, then using `installApp` to post that definition to the target company.

Applications with user-defined dimensions require authorization from a designated administrator before they can be installed. If you run `installApp` on such an application, a request for authorization will be added in the **Requests for authorization** section under **Platform Services \> Applications** in the UI. Alternatively, you can generate an email request for authorization by running the installation from **Platform Services \> Applications \> Install From XML**.

#### `installApp`

```
<installApp>
    <appxml>
        <![CDATA[<application id="10032" origId="100227@10006" orderNo="16" isSystem="F" version="1" companyNo="34466622" ></application>]]>
    </appxml>
</installApp>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| appxml | Required | CDATA | The published application XML must be placed inside of a CDATA tag. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

