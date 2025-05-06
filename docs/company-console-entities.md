Title: Entities

URL Source: https://developer.intacct.com/api/company-console/entities/

Markdown Content:
*   [Get Entity Object Definition](https://developer.intacct.com/api/company-console/entities/#get-entity-object-definition)
*   [Query and List Entities](https://developer.intacct.com/api/company-console/entities/#query-and-list-entities)
*   [Query and List Entities (Legacy)](https://developer.intacct.com/api/company-console/entities/#query-and-list-entities-legacy)
*   [Get Entity](https://developer.intacct.com/api/company-console/entities/#get-entity)
*   [Get Entity by ID](https://developer.intacct.com/api/company-console/entities/#get-entity-by-id)
*   [List Entity Details](https://developer.intacct.com/api/company-console/entities/#list-entity-details)

* * *

Entity is a type of location (a dimension) that is available in multi-entity shared companies only.

An entity can represent a business unit, company, division, legal entity, offices, and so forth.

* * *

Get Entity Object Definition
----------------------------

#### `lookup`

> List all the fields and relationships for the entity object:

```
<lookup>
    <object>LOCATIONENTITY</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATIONENTITY` |

* * *

Query and List Entities
-----------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the Location ID, record number, and name for each entity:

```
<query>
    <object>LOCATIONENTITY</object>
    <select>
        <field>LOCATIONID</field>
        <field>NAME</field>
        <field>RECORDNO</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATIONENTITY` |
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

Query and List Entities (Legacy)
--------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>LOCATIONENTITY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATIONENTITY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active and `F` for Inactive. |

* * *

Get Entity
----------

#### `read`

```
<read>
    <object>LOCATIONENTITY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATIONENTITY` |
| keys | Required | string | Comma-separated list of department `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Entity by ID
----------------

#### `readByName`

```
<readByName>
    <object>LOCATIONENTITY</object>
    <keys>100-US</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATIONENTITY` |
| keys | Required | string | Comma-separated list of department `DEPARTMENTID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

List Entity Details
-------------------

#### `readEntityDetails`

Provides information about the entities that the current user can access.

```
<readEntityDetails/>
```

#### Parameters

No parameters

#### `Response`

> The above function returns data structured like this:

```
<entity>
    <id>Corporate</id>
    <name>Corporate</name>
    <recordno>7</recordno>
    <currency>USD</currency>
    <firstfiscalmonth>10</firstfiscalmonth>
    <firstfiscaltaxmonth></firstfiscaltaxmonth>
    <weekstart></weekstart>
</entity>
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| id | string | Unique entity ID |
| name | string | Entity name |
| recordno | integer | Record number of the entity |
| currency | string | Base currency for the entity (or the top level base currency if no currency is set for the entity) |
| firstfiscalmonth | string | First fiscal month |
| firstfiscaltaxmonth | string | First tax month |
| weekstart | string | Week begins on |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

