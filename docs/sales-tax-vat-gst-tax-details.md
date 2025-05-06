Title: Tax Details

URL Source: https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/

Markdown Content:
*   [Get Tax Detail Object Definition](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/#get-tax-detail-object-definition)
*   [Query and List Tax Details](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/#query-and-list-tax-details)
*   [Query and List Tax Details (Legacy)](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/#query-and-list-tax-details-legacy)
*   [Get Tax Detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/#get-tax-detail)

* * *

A tax detail defines a specific type of tax that can be applied to a line item. (AU, GB, ZA only)

* * *

Get Tax Detail Object Definition
--------------------------------

#### `lookup`

> List all the fields and relationships for the tax detail object:

```
<lookup>
    <object>TAXDETAIL</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXDETAIL` |

* * *

Query and List Tax Details
--------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, tax type, and description for each tax detail:

```
<query>
    <object>TAXDETAIL</object>
    <select>
        <field>RECORDNO</field>
        <field>TAXTYPE</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXDETAIL` |
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

Query and List Tax Details (Legacy)
-----------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>TAXDETAIL</object>
    <fields></fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXDETAIL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TAXTYPE | Optional | string | Tax type for the detail. Use `S` for AR invoices and Order Entry transactions, or `P` for AP bills and Purchasing transactions. |

* * *

Get Tax Detail
--------------

#### `read`

```
<read>
    <object>TAXDETAIL</object>
    <keys>Purchases for Input Tax Sales</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXDETAIL` |
| keys | Required | string | Comma-separated list of tnique ID (`DETAILID`) of the tax detail |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

