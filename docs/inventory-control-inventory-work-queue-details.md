Title: Inventory Work Queue Details

URL Source: https://developer.intacct.com/api/inventory-control/inventory-work-queue-details/

Markdown Content:
*   [Get Inventory Work Queue Details Object Definition](https://developer.intacct.com/api/inventory-control/inventory-work-queue-details/#get-inventory-work-queue-details-object-definition)
*   [Query and List Inventory Work Queue Details](https://developer.intacct.com/api/inventory-control/inventory-work-queue-details/#query-and-list-inventory-work-queue-details)
*   [Query and List Inventory Work Queue Details (legacy)](https://developer.intacct.com/api/inventory-control/inventory-work-queue-details/#query-and-list-inventory-work-queue-details-legacy)
*   [Get an Inventory Work Queue Details](https://developer.intacct.com/api/inventory-control/inventory-work-queue-details/#get-an-inventory-work-queue-details)
*   [Update an Inventory Work Queue Details](https://developer.intacct.com/api/inventory-control/inventory-work-queue-details/#update-an-inventory-work-queue-details)

* * *

This entity represents a “bundle” within fulfillment. A fulfillment can independently transition between states such as `ready-to-pick`, `picked`, assigned, or held (in other words, paused within the fulfillment workflow).

Get Inventory Work Queue Details Object Definition
--------------------------------------------------

#### `lookup`

> List all the fields and relationships for the inventory work queue order details object:

```
<lookup>
    <object>InventoryWQDetail</object>
</lookup>
```

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYWQDETAIL` |

* * *

Query and List Inventory Work Queue Details
-------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> query

```
<query>
    <object>InventoryWQDetail</object>
    <select>
        <field>RECORDNO</field>
        <field>ICWQORDERID</field>
        <field>HOLDPROGRESS</field>
        <field>DOCUMENTTYPE</field>
    </select>
    <filter>
        <equalto>
            <field>STATUS</field>
            <value>ready to pick</value>
        </equalto>
    </filter>
</query>
```

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYWQDETAIL` |
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

Query and List Inventory Work Queue Details (legacy)
----------------------------------------------------

#### `readByQuery`

> readByQuery

```
<readByQuery>
    <object>InventoryWQDetail</object>
    <fields>RECORDNO, ICWQORDERID, DOCID, HOLDPROGRESS</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYWQDETAIL` |
| keys | Required | string | Comma-separated list of object `ID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

#### `read`

> read

```
<read>
    <object>InventoryWQDetail</object>
    <keys>66162</keys>
    <fields>RECORDNO, ICWQORDERID, DOCID, STATUS, HOLDPROGRESS</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYWQDETAIL` |
| keys | Required | string | Comma-separated list of object `ID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Update an Inventory Work Queue Details
--------------------------------------

#### `update`

> update

```
<update>
    <InventoryWQDetail>
        <RECORDNO>66162</RECORDNO>
        <HOLDPROGRESS>true</HOLDPROGRESS>
        <STATUS>open</STATUS>
    </InventoryWQDetail>
</update>
```

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| INVENTORYWQDETAIL | Required | object | Object type to update |

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | No | enum | Current status or state of the order. No default value. Valid values are: `open`, `ready to pick`, `picked`, `packed`, `ready to ship`, `shipped`, `ready to invoice`, `invoiced` |
| PICKCONTAINER | No | string | The container from which to pick the order. |
| PACKCONTAINER | No | string | The container into which to pack the order. |
| SHIPTRACKING | No | string | Shipping tracking number |
| HOLDPROGRESS | No | boolean | Whether or not the product is paused within the fulfillment workflow. The valid values for this field are `true` or `false`. Note that this field has no impoact on either the customer or the order. |
| QUANTITYPICKED | No | decimal | The amount of the product to be picked for an order. |
| QUANTITYPACKED | No | decimal | The amount of the product to be packed for an order. |
| ASSIGNED | No | string | The picker assigned to pick a product for the order. |
| NOTES | No | string | Free-form note field for any extra information about an order. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

