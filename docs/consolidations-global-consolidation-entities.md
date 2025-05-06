Title: Consolidation Entities

URL Source: https://developer.intacct.com/api/consolidations/global-consolidation-entities/

Markdown Content:
*   [Get Global Consolidation Entity Object Definition](https://developer.intacct.com/api/consolidations/global-consolidation-entities/#get-global-consolidation-entity-object-definition)
*   [Query and List Global Consolidation Entities](https://developer.intacct.com/api/consolidations/global-consolidation-entities/#query-and-list-global-consolidation-entities)
*   [Query and List Global Consolidation Entities (Legacy)](https://developer.intacct.com/api/consolidations/global-consolidation-entities/#query-and-list-global-consolidation-entities-legacy)
*   [Get Global Consolidation Entity](https://developer.intacct.com/api/consolidations/global-consolidation-entities/#get-global-consolidation-entity)
*   [Create Global Consolidation Entity](https://developer.intacct.com/api/consolidations/global-consolidation-entities/#create-global-consolidation-entity)
*   [Delete Global Consolidation Entity](https://developer.intacct.com/api/consolidations/global-consolidation-entities/#delete-global-consolidation-entity)

* * *

Specifies the entities to be consolidated in the book (in addition to those selected from the entity setup).

**Note:** Most consolidation object names start with `GC` and are called “Global Coonsolidation,” but you can use them for domestic or global consolidations.

* * *

Get Global Consolidation Entity Object Definition
-------------------------------------------------

#### `lookup`

> List all the fields and relationships for the Global Consolidation entity object:

```
<lookup>
    <object>GCBOOKENTITY</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKENTITY` |

* * *

Query and List Global Consolidation Entities
--------------------------------------------

#### `query`

> List the record number and book ID for each Global Consolidation entity:

```
<query>
    <object>GCBOOKENTITY</object>
    <select>
        <field>RECORDNO</field>
        <field>BOOKID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKENTITY` |
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

Query and List Global Consolidation Entities (Legacy)
-----------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>GCBOOKENTITY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKENTITY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Global Consolidation Entity
-------------------------------

#### `read`

```
<read>
    <object>GCBOOKENTITY</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKENTITY` |
| keys | Required | string | Comma-separated list of global consolidation entity `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Global Consolidation Entity
----------------------------------

#### `create`

```
<create>
    <GCBOOKENTITY>
        <BOOKID>gc_book</BOOKID>
        <LOCATIONID>110-SJC</LOCATIONID>
    </GCBOOKENTITY>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKENTITY | Required | object | Object to create |

`GCBOOKENTITY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKID | Required | string | Book ID of the consolidation book in which to include this entity |
| LOCATIONID | Required | string | Location ID for the entity |

* * *

Delete Global Consolidation Entity
----------------------------------

#### `delete`

```
<delete>
    <object>GCBOOKENTITY</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKENTITY | Required | object | Object to delete |
| keys | Required | string | Comma-separated list of book entity `RECORDNO` to delete |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

