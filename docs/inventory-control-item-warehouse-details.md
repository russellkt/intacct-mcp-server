Title: Item Warehouse Details

URL Source: https://developer.intacct.com/api/inventory-control/item-warehouse-details/

Markdown Content:
*   [Get Item Warehouse Detail Object Definition](https://developer.intacct.com/api/inventory-control/item-warehouse-details/#get-item-warehouse-detail-object-definition)
*   [Query and List Item Warehouse Details](https://developer.intacct.com/api/inventory-control/item-warehouse-details/#query-and-list-item-warehouse-details)
*   [Query and List Item Warehouse Details (Legacy)](https://developer.intacct.com/api/inventory-control/item-warehouse-details/#query-and-list-item-warehouse-details-legacy)
*   [Get Item Warehouse Detail](https://developer.intacct.com/api/inventory-control/item-warehouse-details/#get-item-warehouse-detail)

* * *

Item warehouse details are used with Inventory and Stockable Kit items.

Sage Intacct uses the information from these records in the Inventory Reorders report.

* * *

Get Item Warehouse Detail Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the item warehouse detail object:

```
<lookup>
    <object>ITEMWAREHOUSEINFO</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMWAREHOUSEINFO` |

* * *

Query and List Item Warehouse Details
-------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, item ID, and warehouse ID of each warehouse detail :

```
<query>
    <object>ITEMWAREHOUSEINFO</object>
    <select>
        <field>RECORDNO</field>
        <field>ITEMID</field>
        <field>WAREHOUSEID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMWAREHOUSEINFO` |
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

Query and List Item Warehouse Details (Legacy)
----------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ITEMWAREHOUSEINFO</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMWAREHOUSEINFO` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Item Warehouse Detail
-------------------------

#### `read`

```
<read>
    <object>ITEMWAREHOUSEINFO</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMWAREHOUSEINFO` |
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

