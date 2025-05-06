Title: Change Request Types

URL Source: https://developer.intacct.com/api/construction/change-request-types/

Markdown Content:
*   [Get Change Request Type Object Definition](https://developer.intacct.com/api/construction/change-request-types/#get-change-request-type-object-definition)
*   [Query and List Change Request Types](https://developer.intacct.com/api/construction/change-request-types/#query-and-list-change-request-types)
*   [Query and List Change Request Types (Legacy)](https://developer.intacct.com/api/construction/change-request-types/#query-and-list-change-request-types-legacy)
*   [Get Change Request Type](https://developer.intacct.com/api/construction/change-request-types/#get-change-request-type)
*   [Get Change Request Type by ID](https://developer.intacct.com/api/construction/change-request-types/#get-change-request-type-by-id)
*   [Create Change Request Type](https://developer.intacct.com/api/construction/change-request-types/#create-change-request-type)
*   [Update Change Request Type](https://developer.intacct.com/api/construction/change-request-types/#update-change-request-type)
*   [Delete Change Request Type](https://developer.intacct.com/api/construction/change-request-types/#delete-change-request-type)

* * *

Construction companies can create their own change request types for reporting purposes. For example, an `Internal` change request type might be used for a change request that specifies a cost to the contractor that should not be billed to the customer.

* * *

Get Change Request Type Object Definition
-----------------------------------------

#### `lookup`

> List all the fields and relationships for the change request type object:

```
<lookup>
    <object>CHANGEREQUESTTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTTYPE` |

* * *

Query and List Change Request Types
-----------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List information for change request types that are active:

```
<query>
    <object>CHANGEREQUESTTYPE</object>
    <select>
        <field>NAME</field>
        <field>STATUS</field>
        <field>RECORDNO</field>
    </select>
    <filter>
        <equalto>
            <field>STATUS</field>
            <value>active</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTTYPE` |
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

Query and List Change Request Types (Legacy)
--------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CHANGEREQUESTTYPE</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Change Request Type
-----------------------

#### `read`

```
<read>
    <object>CHANGEREQUESTTYPE</object>
    <keys>11</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTTYPE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the change request type to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Change Request Type by ID
-----------------------------

#### `readByName`

```
<readByName>
    <object>CHANGEREQUESTTYPE</object>
    <keys>Internal</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTTYPE` |
| keys | Required | string | Comma-separated list of change request type IDs to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Change Request Type
--------------------------

#### `create`

> Creates an active change request type named `Internal`:

```
<create>
    <CHANGEREQUESTTYPE>
        <NAME>Internal</NAME>
    </CHANGEREQUESTTYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUESTTYPE | Required | object | Object to create |

`CHANGEREQUESTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Unique name for the change request type. Use 80 or fewer characters. |
| STATUS | Optional | string | Status for the change request type. Use `active` or `inactive`. (Default: `active`) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Change Request Type
--------------------------

#### `update`

You can update the status of a change request type.

> Sets the status of a change request type to `inactive`:

```
<update>
    <CHANGEREQUESTTYPE>
        <RECORDNO>13</RECORDNO>
        <STATUS>inactive</STATUS>
    </CHANGEREQUESTTYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUESTTYPE | Required | object | Object to update |

`CHANGEREQUESTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | `RECORDNO` of the change request type to update. Required if not using `NAME`. |
| NAME | Optional | string | Unique name of the change request type to update. Required if not using `RECORDNO`. |
| STATUS | Optional | string | Status for the change request type. Use `active` or `inactive`. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Change Request Type
--------------------------

You can delete a change request type only if it is not in use by a change request.

#### `delete`

```
<delete>
    <object>CHANGEREQUESTTYPE</object>
    <keys>13</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTTYPE` |
| keys | Required | integer | `RECORDNO` of the change request type to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

