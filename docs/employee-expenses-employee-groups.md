Title: Employee Groups

URL Source: https://developer.intacct.com/api/employee-expenses/employee-groups/

Markdown Content:
*   [Get Employee Group Object Definition](https://developer.intacct.com/api/employee-expenses/employee-groups/#get-employee-group-object-definition)
*   [Query and List Employee Groups](https://developer.intacct.com/api/employee-expenses/employee-groups/#query-and-list-employee-groups)
*   [Query and List Employee Groups (Legacy)](https://developer.intacct.com/api/employee-expenses/employee-groups/#query-and-list-employee-groups-legacy)
*   [Get Employee Group](https://developer.intacct.com/api/employee-expenses/employee-groups/#get-employee-group)
*   [Get Employee Group by ID](https://developer.intacct.com/api/employee-expenses/employee-groups/#get-employee-group-by-id)

* * *

An employee group categories employee dimension records, mainly for the purpose of structuring financial reporting.

* * *

Get Employee Group Object Definition
------------------------------------

#### `lookup`

> List all the fields and relationships for the employee group object:

```
<lookup>
    <object>EMPLOYEEGROUP</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEGROUP` |

* * *

Query and List Employee Groups
------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, description, and ID for each employee group:

```
<query>
    <object>EMPLOYEEGROUP</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
        <field>ID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEGROUP` |
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

Query and List Employee Groups (Legacy)
---------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>EMPLOYEEGROUP</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEGROUP` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Employee Group
------------------

#### `read`

```
<read>
    <object>EMPLOYEEGROUP</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEGROUP` |
| keys | Required | string | Comma-separated list of group `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Employee Group by ID
------------------------

#### `readByName`

```
<readByName>
    <object>EMPLOYEEGROUP</object>
    <keys>TEST</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEGROUP` |
| keys | Required | string | Comma-separated list of group `ID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

