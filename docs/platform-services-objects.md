Title: Objects

URL Source: https://developer.intacct.com/api/platform-services/objects/

Markdown Content:
*   [Query and List Objects](https://developer.intacct.com/api/platform-services/objects/#query-and-list-objects)
*   [Get Object Definition](https://developer.intacct.com/api/platform-services/objects/#get-object-definition)
*   [Get Object Definition (Legacy)](https://developer.intacct.com/api/platform-services/objects/#get-object-definition-legacy)
*   [Query and List Object Audit Trail Logs](https://developer.intacct.com/api/platform-services/objects/#query-and-list-object-audit-trail-logs)
*   [Query and List Object Audit Trail Logs (Legacy)](https://developer.intacct.com/api/platform-services/objects/#query-and-list-object-audit-trail-logs-legacy)
*   [Get Object Audit Trail Log](https://developer.intacct.com/api/platform-services/objects/#get-object-audit-trail-log)

* * *

An object is either a Sage Intacct standard object, such as AP Bill, or a custom object.

* * *

Query and List Objects
----------------------

Lists all standard and custom objects in a company, regardless of your permissions or the company’s subscriptions.

#### `inspect`

```
<inspect>
    <object>*</object>
</inspect>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `*` to return all objects |

* * *

Get Object Definition
---------------------

The `lookup` function lists all fields and relationships for standard or custom objects. Information about owned objects is not provided.

#### `lookup`

> List fields and relationships for a custom object:

```
<lookup>
    <object>MCA_attendee</object>
</lookup>
```

> List fields and relationships for a standard object:

```
<lookup>
    <object>CUSTOMER</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Optional | string | Object integration name to get. Required if not using `name` |
| name | Optional | string | Object name to get. Required if not using `object`. |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Invoice`). |

#### `Response`

> For a field, the output provides the ID, label, description, and so forth. Valid values for enumerations are also provided.

```
<Field>
    <ID>priority</ID>
    <LABEL>Priority</LABEL>
    <DESCRIPTION>Task priority</DESCRIPTION>
    <REQUIRED>false</REQUIRED>
    <READONLY>false</READONLY>
    <DATATYPE>ENUM</DATATYPE>
    <VALIDVALUES>
        <VALIDVALUE>High</VALIDVALUE>
        <VALIDVALUE>Normal</VALIDVALUE>
        <VALIDVALUE>Low</VALIDVALUE>
    </VALIDVALUES>
</Field>
```

> For a relationship, the output provides the ID, label, description, and so forth:

```
<Relationship>
    <OBJECTPATH>PRIMARYCONTACT</OBJECTPATH>
    <OBJECTNAME>CONTACT</OBJECTNAME>
    <LABEL>Primary Contact</LABEL>
    <RELATIONSHIPTYPE>MANY2ONE</RELATIONSHIPTYPE>
    <RELATEDBY>CONTACTINFO.CONTACTNAME</RELATEDBY>
</Relationship>
<Relationship>
    <OBJECTPATH>ACCOUNTLABEL</OBJECTPATH>
    <OBJECTNAME>ARACCOUNTLABEL</OBJECTNAME>
    <LABEL></LABEL>
    <RELATIONSHIPTYPE>MANY2ONE</RELATIONSHIPTYPE>
    <RELATEDBY>ACCOUNTLABEL</RELATEDBY>
</Relationship>
```

> Here are the relationships for a custom object:

```
<Relationship>
    <OBJECTPATH>R_attendee_customer</OBJECTPATH>
    <OBJECTNAME>customer</OBJECTNAME>
    <LABEL>Customer</LABEL>
    <RELATIONSHIPTYPE>MANY2ONE</RELATIONSHIPTYPE>
    <RELATEDBY>RCUSTOMER</RELATEDBY>
</Relationship>
```

#### `Parameters`

#### Fields

| Name | Description |
| --- | --- |
| ID | Field ID |
| LABEL | Field label |
| DESCRIPTION | Field description |
| REQUIRED | `true` if the field is required, `false` othewise |
| READONLY | `true` if the field is read only, `false` othewise |
| DATATYPE | Data type such as integer, text, enum, and so forth |
| VALIDVALUE | Allowed values for enum fields |

#### Relationships

| Name | Description |
| --- | --- |
| OBJECTPATH | Nexus path to a related object. Can be used to query fields using dot operator, for example, `PROJECT.CUSTOMER`. (The dot operator lets you access the values of fields on a related object that has a many-to-one relationship to the object being queried.) Note that an object can have multiple references to the same object type. For example, CUSTOMER has four relationships to CONTACT objects identified by SHIPTOTCONTACT, BILLTOCONTACT, DISPLAYCONTACT, and PRIMARYCONTACT nexus paths. |
| OBJECTNAME | Type of the related object |
| LABEL | The Print As parameter for the relationship |
| RELATIONSHIPTYPE | Type of relationship between two objects. Only one-to-one and one-to-many are returned. |
| RELATEDBY | the field of the object mapped to the column in the database table specified as the foreign key to the related object. |

* * *

Get Object Definition (Legacy)
------------------------------

Returns the object definition and all field details for a specific standard or custom object.

#### `inspect`

> Get object definition by integration name:

```
<inspect detail="1">
    <object>DEPARTMENT</object>
</inspect>
```

> Get object definition by printable name:

```
<inspect detail="1">
    <name>Sales Order</name>
</inspect>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detail | Optional | integer | Use `1` to return details otherwise use `0` to return summary info |
| object | Optional | string | Object integration name to get. Required if not using `name` |
| name | Optional | string | Object name to get. Required if not using `object`. If you need to get objects that utilize transaction definitions (docparid), you should use inspect with the `name` element instead of the `object` element. |

* * *

Query and List Object Audit Trail Logs
--------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, object ID, and the ‘created-by’ user for each object audit trail log:

```
<query>
    <object>ACTIVITYLOG</object>
    <select>
        <field>RECORDNO</field>
        <field>OBJ_ID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACTIVITYLOG` |
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

* * *

Query and List Object Audit Trail Logs (Legacy)
-----------------------------------------------

#### `readByQuery`

> List changes made to all objects on April 19, 2012:

```
<readByQuery>
    <object>ACTIVITYLOG</object>
    <fields>*</fields>
    <query>OBJ_ID &lt; 0 AND CREATED_AT &gt;= '04/19/2012 12:00:00' AND CREATED_AT &lt; '04/20/2012 12:00:00'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List changes made to custom object ID 10006:

```
<readByQuery>
    <object>ACTIVITYLOG</object>
    <fields>*</fields>
    <query>OBJ_ID = -10006</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACTIVITYLOG` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| OBJ\_ID | Required | integer | Object system ID. Must be prefixed with a dash `-`. Look up this value in the object definition. |

#### `Response`

> The above function returns data structured like this:

```
<activitylog>
    <RECORDNO>11033</RECORDNO>
    <OBJ_ID>-10006</OBJ_ID>
    <TRAIL_TEXT>Validation script for field &quot;Estimated Fees&quot; has been updated.</TRAIL_TEXT>
    <EMAIL_TEXT></EMAIL_TEXT>
    <CREATED_BY>1</CREATED_BY>
    <CREATEDBYUSER>jsmith</CREATEDBYUSER>
    <CREATED_AT>04/19/2012 19:38:32</CREATED_AT>
</activitylog>
```

* * *

Get Object Audit Trail Log
--------------------------

#### `read`

```
<read>
    <object>ACTIVITYLOG</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACTIVITYLOG` |
| keys | Required | string | Comma-separated list of log `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

