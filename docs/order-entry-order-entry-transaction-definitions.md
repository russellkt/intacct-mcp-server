Title: Order Entry Transaction Definitions

URL Source: https://developer.intacct.com/api/order-entry/order-entry-transaction-definitions/

Markdown Content:
*   [Get Order Entry Transaction Definition Object Definition](https://developer.intacct.com/api/order-entry/order-entry-transaction-definitions/#get-order-entry-transaction-definition-object-definition)
*   [Query and List Order Entry Transaction Definitions](https://developer.intacct.com/api/order-entry/order-entry-transaction-definitions/#query-and-list-order-entry-transaction-definitions)
*   [Query and List Order Entry Transaction Definitions (Legacy)](https://developer.intacct.com/api/order-entry/order-entry-transaction-definitions/#query-and-list-order-entry-transaction-definitions-legacy)
*   [Get Order Entry Transaction Definition](https://developer.intacct.com/api/order-entry/order-entry-transaction-definitions/#get-order-entry-transaction-definition)

* * *

An Order Entry transaction definition is the template for an Order Entry transaction.

* * *

Get Order Entry Transaction Definition Object Definition
--------------------------------------------------------

#### `lookup`

> List all the fields and relationships for the Order Entry transaction definition object:

```
<lookup>
    <object>SODOCUMENTPARAMS</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTPARAMS` |

* * *

Query and List Order Entry Transaction Definitions
--------------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, template name, and template type for each transaction definition:

```
<query>
    <object>SODOCUMENTPARAMS</object>
    <select>
        <field>RECORDNO</field>
        <field>DOCID</field>
        <field>DOCCLASS</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTPARAMS` |
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

Query and List Order Entry Transaction Definitions (Legacy)
-----------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>SODOCUMENTPARAMS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTPARAMS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Order Entry Transaction Definition
--------------------------------------

#### `read`

```
<read>
    <object>SODOCUMENTPARAMS</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTPARAMS` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

