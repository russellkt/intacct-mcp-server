Title: Time Types

URL Source: https://developer.intacct.com/api/project-resource-mgmt/time-types/

Markdown Content:
*   [Get Time Type Object Definition](https://developer.intacct.com/api/project-resource-mgmt/time-types/#get-time-type-object-definition)
*   [Query and List Time Types](https://developer.intacct.com/api/project-resource-mgmt/time-types/#query-and-list-time-types)
*   [Query and List Time Types (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/time-types/#query-and-list-time-types-legacy)
*   [Get Time Type](https://developer.intacct.com/api/project-resource-mgmt/time-types/#get-time-type)
*   [Get Time Type by ID](https://developer.intacct.com/api/project-resource-mgmt/time-types/#get-time-type-by-id)
*   [Create Time Type (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/time-types/#create-time-type-legacy)
*   [Update Time Type (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/time-types/#update-time-type-legacy)
*   [Delete Time Type (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/time-types/#delete-time-type-legacy)

* * *

Time types are exactly what they sound like – different categories of time, such as salary, contract hours, overtime, vacation, travel time, and so on.

* * *

Get Time Type Object Definition
-------------------------------

#### `lookup`

> List all the fields and relationships for the time type object:

```
<lookup>
    <object>TIMETYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMETYPE` |

* * *

Query and List Time Types
-------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and account number for each time type:

```
<query>
    <object>TIMETYPE</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCOUNTNO</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMETYPE` |
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

Query and List Time Types (Legacy)
----------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>TIMETYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMETYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Time Type
-------------

#### `read`

```
<read>
    <object>TIMETYPE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMETYPE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Time Type by ID
-------------------

#### `readByName`

```
<readByName>
    <object>TIMETYPE</object>
    <keys>Full Time</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMETYPE` |
| keys | Required | string | Comma-separated list of object `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Time Type (Legacy)
-------------------------

#### `create_timetype`

```
<create_timetype>
    <name>Regular staff time</name>
</create_timetype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Time type name to create |
| status | Optional | string | Time type status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| accountno | Optional | string | Account number |
| offsetaccountno | Optional | string | Offset account number |
| earningtypename | Optional | string | Earning type name |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Time Type (Legacy)
-------------------------

#### `update_timetype`

```
<update_timetype key="Regular staff time">
    <accountno>6500</accountno>
</update_timetype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Time type name to update |
| status | Optional | string | Time type status. Use `active` for Active otherwise use `inactive` for Inactive. |
| accountno | Optional | string | Account number |
| offsetaccountno | Optional | string | Offset account number |
| earningtypename | Optional | string | Earning type name |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Time Type (Legacy)
-------------------------

#### `delete_timetype`

```
<delete_timetype key="Regular staff time"></delete_timetype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Time type name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

