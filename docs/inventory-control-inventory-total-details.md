Title: Inventory Total Details

URL Source: https://developer.intacct.com/api/inventory-control/inventory-total-details/

Markdown Content:
*   [Get Inventory Total Detail Object Definition](https://developer.intacct.com/api/inventory-control/inventory-total-details/#get-inventory-total-detail-object-definition)
*   [Query and List Inventory Total Details](https://developer.intacct.com/api/inventory-control/inventory-total-details/#query-and-list-inventory-total-details)
*   [Query and List Inventory Total Details (Legacy)](https://developer.intacct.com/api/inventory-control/inventory-total-details/#query-and-list-inventory-total-details-legacy)
*   [Get Inventory Total Detail](https://developer.intacct.com/api/inventory-control/inventory-total-details/#get-inventory-total-detail)

* * *

Inventory total details provide visibility into all the inventory totals your organization uses, including onhand, onhold, onorder, damaged, requisitioned, scrap/spoilage, or custom totals.

* * *

Get Inventory Total Detail Object Definition
--------------------------------------------

#### `lookup`

> List all the fields and relationships for the inventory total detail object:

```
<lookup>
    <object>INVENTORYTOTALDETAIL</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYTOTALDETAIL` |

* * *

Query and List Inventory Total Details
--------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the item ID for each inventory total detail for scrap or damaged items:

```
<query>
    <object>INVENTORYTOTALDETAIL</object>
    <select>
        <field>ITEMID</field>
        <field>TOTALNAME</field>
    </select>
    <filter>
        <or>
            <equalto>
                <field>TOTALNAME</field>
                <value>SCRAP OR SPOILAGE</value>
            </equalto>
            <equalto>
                <field>TOTALNAME</field>
                <value>DAMAGED</value>
            </equalto>
        </or>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYTOTALDETAIL` |
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

Query and List Inventory Total Details (Legacy)
-----------------------------------------------

#### `readByQuery`

> List inventory total details:

```
<readByQuery>
    <object>INVENTORYTOTALDETAIL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List inventory total details for scrap or damaged items:

```
<readByQuery>
    <object>inventorytotaldetail</object>
    <query>TOTALNAME='SCRAP OR SPOILAGE' OR TOTALNAME='DAMAGED'</query>
    <fields>*</fields>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYTOTALDETAIL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

#### `Response`

`inventorytotaldetail`

> The above function returns data structured like this:

```
<inventorytotaldetail>
    <ID>12535</ID>
    <ITEMID>AT-008</ITEMID>
    <WAREHOUSEKEY>1</WAREHOUSEKEY>
    <DOCUMENTID>Inventory Damaged Goods-ADJ0003</DOCUMENTID>
    <TOTALKEY>55</TOTALKEY>
    <TOTALNAME>DAMAGED</TOTALNAME>
    <UNIT>Each</UNIT>
    <QUANTITY>1</QUANTITY>
    <LOCATIONKEY>1</LOCATIONKEY>
    <DEPTKEY></DEPTKEY>
    <WHENCREATED>10/01/2019</WHENCREATED>
    <EFFECTONINVENTORY>Quantity &amp; Value</EFFECTONINVENTORY>
</inventorytotaldetail>
```

* * *

Get Inventory Total Detail
--------------------------

#### `read`

```
<read>
    <object>INVENTORYTOTALDETAIL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYTOTALDETAIL` |
| keys | Required | string | Comma-separated list of object `ID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

