Title: Inventory Work Queue Orders

URL Source: https://developer.intacct.com/api/inventory-control/inventory-work-queue-orders/

Markdown Content:
*   [Get Inventory Work Queue Orders Object Definition](https://developer.intacct.com/api/inventory-control/inventory-work-queue-orders/#get-inventory-work-queue-orders-object-definition)
*   [Query and List Inventory Work Queue Orders](https://developer.intacct.com/api/inventory-control/inventory-work-queue-orders/#query-and-list-inventory-work-queue-orders)
*   [Query and List Inventory Work Queue Order (legacy)](https://developer.intacct.com/api/inventory-control/inventory-work-queue-orders/#query-and-list-inventory-work-queue-order-legacy)
*   [Get an Inventory Work Queue Order](https://developer.intacct.com/api/inventory-control/inventory-work-queue-orders/#get-an-inventory-work-queue-order)
*   [Update an Inventory Work Queue Order](https://developer.intacct.com/api/inventory-control/inventory-work-queue-orders/#update-an-inventory-work-queue-order)

* * *

This entity represents the fulfillment-enhanced view of a Sales Order. Inventory Work Queue Orders API allows you to organize which orders get processed first, for example, based on date ordered, importance of customer, kinds of items being shipped, ability to fulfill the entire order as well as other parameters.

Get Inventory Work Queue Orders Object Definition
-------------------------------------------------

#### `lookup`

> List all the fields and relationships for the inventory work queue orders definition object:

```
<lookup>
    <object>InventoryWQOrder</object>
</lookup>
```

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYWQORDER` |

* * *

Query and List Inventory Work Queue Orders
------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> query

```
<query>
    <object>InventoryWQOrder</object>
    <select>
        <field>ICWQORDERID</field>
        <field>SHIPTOCONTACT</field>
        <field>CUSTOMERNAME</field>
        <field>ORDERHOLDPROGRESS</field>
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
| object | Required | string | Use `INVENTORYWQORDER` |
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

Query and List Inventory Work Queue Order (legacy)
--------------------------------------------------

#### `readByQuery`

> readByQuery

```
<readByQuery>
    <object>InventoryWQOrder</object>
    <fields>ICWQORDERID, STATUS, CUSTOMERID, PCTFULFILLABLE</fields>
    <query>DOCID = 'SYS-Fulfillment Order-SYS-F1-00000039-doc'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYWQORDER` |
| keys | Required | string | Comma-separated list of object `ID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get an Inventory Work Queue Order
---------------------------------

#### `read`

> read

```
<read>
    <object>InventoryWQOrder</object>
    <keys>418--1--317--RPI</keys>
    <fields>DOCID, STATUS, HOLDPROGRESS, CUSTOMERID, PCTFULFILLABLE</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVENTORYWQORDER` |
| keys | Required | string | Comma-separated list of object `ID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Update an Inventory Work Queue Order
------------------------------------

#### `update`

> update

```
<update>
    <InventoryWQOrder>
        <ICWQORDERID>418--1--317--RPI</ICWQORDERID>
        <STATUS>picked</STATUS>
    </InventoryWQOrder>
</update>
```

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| INVENTORYWQORDER | Required | object | Object type to update |

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | No | enum | Current status or state of the order. No default value. Valid values are: `open`, `ready to pick`, `picked`, `packed`, `ready to ship`, `shipped`, `ready to invoice`, `invoiced` |
| PICKCONTAINER | No | string | The container from which to pick the order. |
| PACKCONTAINER | No | string | The container into which to pack the order. |
| SHIPTRACKING | No | string | Shipping tracking number |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

