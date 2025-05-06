Title: Consolidation Journals

URL Source: https://developer.intacct.com/api/consolidations/global-consolidation-journals/

Markdown Content:
*   [Get Global Consolidation Journal Object Definition](https://developer.intacct.com/api/consolidations/global-consolidation-journals/#get-global-consolidation-journal-object-definition)
*   [Query and List Global Consolidation Journals](https://developer.intacct.com/api/consolidations/global-consolidation-journals/#query-and-list-global-consolidation-journals)
*   [Query and List Global Consolidation Journals (Legacy)](https://developer.intacct.com/api/consolidations/global-consolidation-journals/#query-and-list-global-consolidation-journals-legacy)
*   [Get Global Consolidation Journal](https://developer.intacct.com/api/consolidations/global-consolidation-journals/#get-global-consolidation-journal)
*   [Create Global Consolidation Journal](https://developer.intacct.com/api/consolidations/global-consolidation-journals/#create-global-consolidation-journal)
*   [Update Global Consolidation Journal](https://developer.intacct.com/api/consolidations/global-consolidation-journals/#update-global-consolidation-journal)
*   [Delete Global Consolidation Journal](https://developer.intacct.com/api/consolidations/global-consolidation-journals/#delete-global-consolidation-journal)

* * *

When you create a consolidation book, you get a single journal for all the consolidation entries for all of the entities.

You can then add journals for GAAP, tax, and user-defined books. Note that once you’ve run a consolidation, journals can no longer be modified.

**Note:** Most consolidation object names start with `GC` and are called “Global Coonsolidation,” but you can use them for domestic or global consolidations.

* * *

Get Global Consolidation Journal Object Definition
--------------------------------------------------

#### `lookup`

> List all the fields and relationships for the Global Consolidation journal object:

```
<lookup>
    <object>GCBOOKADJJOURNAL</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKADJJOURNAL` |

* * *

Query and List Global Consolidation Journals
--------------------------------------------

#### `query`

> List the record number and book ID for each Global Consolidation journal :

```
<query>
    <object>GCBOOKADJJOURNAL</object>
    <select>
        <field>RECORDNO</field>
        <field>BOOKID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKADJJOURNAL` |
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

Query and List Global Consolidation Journals (Legacy)
-----------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>GCBOOKADJJOURNAL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKADJJOURNAL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKKEY | Optional | string | Consolidation book ID |

* * *

Get Global Consolidation Journal
--------------------------------

#### `read`

```
<read>
    <object>GCBOOKADJJOURNAL</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKADJJOURNAL` |
| keys | Required | string | Comma-separated list of global consolidation journal `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Global Consolidation Journal
-----------------------------------

#### `create`

```
<create>
    <GCBOOKADJJOURNAL>
        <BOOKID>gc_book</BOOKID>
        <BOOKTYPE>GAAPADJ</BOOKTYPE>
        <SYMBOL>GAAPADJ</SYMBOL>
        <TITLE>GAAP Journal</TITLE>
    </GCBOOKADJJOURNAL>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKADJJOURNAL | Required | object | Object to create |

`GCBOOKJOURNAL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKID | Required | string | Book ID of the consolidation book |
| BOOKTYPE | Required | string | Type of journal. Use `Consolidation` for a global consolidation journal, `GAAPADJ` for GAAP adjustment journal, or `USERADJ` for a user-defined journal. |
| USERADJBOOKID | Optional | string | User-defined book ID. Required for user-defined journals. |
| SYMBOL | Optional | string | GL journal symbol |
| TITLE | Optional | string | Journal title |

* * *

Update Global Consolidation Journal
-----------------------------------

#### `update`

```
<update>
    <GCBOOKADJJOURNAL>
        <RECORDNO>95</RECORDNO>
        <TITLE>My Journal</TITLE>
    </GCBOOKADJJOURNAL>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKADJJOURNAL | Required | object | Object to update |

`GCBOOKADJJOURNAL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the adjusting journal |
| TITLE | Optional | string | Journal title |

* * *

Delete Global Consolidation Journal
-----------------------------------

#### `delete`

```
<delete>
    <object>GCBOOKADJJOURNAL</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKADJJOURNAL | Required | object | Object to delete. |
| keys | Required | string | Comma-separated list of journal `RECORDNO` to delete |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

