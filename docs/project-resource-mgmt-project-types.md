Title: Project Types

URL Source: https://developer.intacct.com/api/project-resource-mgmt/project-types/

Markdown Content:
*   [Get Project Type Object Definition](https://developer.intacct.com/api/project-resource-mgmt/project-types/#get-project-type-object-definition)
*   [Query and List Project Types](https://developer.intacct.com/api/project-resource-mgmt/project-types/#query-and-list-project-types)
*   [Query and List Project Types (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/project-types/#query-and-list-project-types-legacy)
*   [Get Project Type](https://developer.intacct.com/api/project-resource-mgmt/project-types/#get-project-type)
*   [Get Project Type by ID](https://developer.intacct.com/api/project-resource-mgmt/project-types/#get-project-type-by-id)

* * *

Project types enable you to group projects into categories like Consulting, Internal, or Training.

* * *

Get Project Type Object Definition
----------------------------------

#### `lookup`

> List all the fields and relationships for the project type object:

```
<lookup>
    <object>PROJECTTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTTYPE` |

* * *

Query and List Project Types
----------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the name and status of each project type:

```
<query>
    <object>PROJECTTYPE</object>
    <select>
        <field>NAME</field>
        <field>STATUS</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTTYPE` |
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

Query and List Project Types (Legacy)
-------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PROJECTTYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Project Type
----------------

#### `read`

```
<read>
    <object>PROJECTTYPE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTTYPE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Project Type by ID
----------------------

#### `readByName`

```
<readByName>
    <object>PROJECTTYPE</object>
    <keys>Full Time</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTTYPE` |
| keys | Required | string | Comma-separated list of object `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

