Title: Warehouses

URL Source: https://developer.intacct.com/api/inventory-control/warehouses/

Markdown Content:
*   [Get Warehouse Object Definition](https://developer.intacct.com/api/inventory-control/warehouses/#get-warehouse-object-definition)
*   [Query and List Warehouses](https://developer.intacct.com/api/inventory-control/warehouses/#query-and-list-warehouses)
*   [Query and List Warehouses (Legacy)](https://developer.intacct.com/api/inventory-control/warehouses/#query-and-list-warehouses-legacy)
*   [Get Warehouse](https://developer.intacct.com/api/inventory-control/warehouses/#get-warehouse)
*   [Get Warehouse by ID](https://developer.intacct.com/api/inventory-control/warehouses/#get-warehouse-by-id)
*   [Create Warehouse](https://developer.intacct.com/api/inventory-control/warehouses/#create-warehouse)
*   [Update Warehouse](https://developer.intacct.com/api/inventory-control/warehouses/#update-warehouse)
*   [Delete Warehouse](https://developer.intacct.com/api/inventory-control/warehouses/#delete-warehouse)

* * *

Warehouse is a dimension that can be defined by the company and set on transactions to expand report functionality and insight.

* * *

Get Warehouse Object Definition
-------------------------------

#### `lookup`

> List all the fields and relationships for the warehouse object:

```
<lookup>
    <object>WAREHOUSE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `WAREHOUSE` |

* * *

Query and List Warehouses
-------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and location ID for each warehouse:

```
<query>
    <object>WAREHOUSE</object>
    <select>
        <field>RECORDNO</field>
        <field>LOCATIONID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `WAREHOUSE` |
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

Query and List Warehouses (Legacy)
----------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>WAREHOUSE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `WAREHOUSE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active and `F` for Inactive. |

* * *

Get Warehouse
-------------

#### `read`

```
<read>
    <object>WAREHOUSE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `WAREHOUSE` |
| keys | Required | string | Comma-separated list of warehouse `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Warehouse by ID
-------------------

#### `readByName`

```
<readByName>
    <object>WAREHOUSE</object>
    <keys>9ADMIN</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `WAREHOUSE` |
| keys | Required | string | Comma-separated list of warehouse `WAREHOUSEID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Warehouse
----------------

[History](https://developer.intacct.com/api/inventory-control/warehouses/#history-create-warehouse)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added ENABLENEGATIVEINV |
| 2018 Release 4 | Added ENABLE\_REPLENISHMENT |

#### `create`

```
<create>
    <WAREHOUSE>
        <WAREHOUSEID>W1234</WAREHOUSEID>
        <NAME>hello world</NAME>
        <LOC>
            <LOCATIONID>L1234</LOCATIONID>
        </LOC>
    </WAREHOUSE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| WAREHOUSE | Required | object | Object to create |

`WAREHOUSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| WAREHOUSEID | Required | string | Warehouse ID to create |
| NAME | Required | string | Warehouse name |
| LOC | Required | object | Location |
| MANAGERID | Optional | string | Manager employee ID |
| PARENTID | Optional | string | Parent warehouse ID |
| CONTACTINFO | Optional | object | Primary contact |
| SHIPTO | Optional | object | Ship to contact |
| USEDINGL | Optional | boolean | Used in GL. Use `false` for No, `true` for Yes. (Default: `true`) |
| STATUS | Optional | string | Warehouse status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| ENABLE\_REPLENISHMENT | Optional | boolean | Enable replenishment. Use `true` to enable, otherwise use `false`. (Default: `true`) |
| ENABLENEGATIVEINV | Optional | boolean | Enable negative inventory for this warehouse. This option lets you enable negative inventory for a specific warehouse, assuming that the company is not already configured to allow negative inventory. Use `true` to enable negative inventory for this warehouse, otherwise use `false`. (Default: `false`) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`LOC`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATIONID | Required | string | Location ID of warehouse |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Primary contact name |

`SHIPTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Ship to contact name |

* * *

Update Warehouse
----------------

[History](https://developer.intacct.com/api/inventory-control/warehouses/#history-update-warehouse)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added ENABLENEGATIVEINV |
| 2018 Release 4 | Added ENABLE\_REPLENISHMENT |

#### `update`

```
<update>
    <WAREHOUSE>
        <RECORDNO>212</RECORDNO>
        <STATUS>active</STATUS>
    </WAREHOUSE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| WAREHOUSE | Required | object | Object to update |

`WAREHOUSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of warehouse to update. Required if not using `WAREHOUSEID`. |
| WAREHOUSEID | Optional | string | Warehouse ID. Required if not using `RECORDNO`. |
| NAME | Optional | string | Warehouse name |
| LOC | Optional | object | Location |
| MANAGERID | Optional | string | Manager employee ID |
| PARENTID | Optional | string | Parent warehouse ID |
| CONTACTINFO | Optional | object | Primary contact |
| SHIPTO | Optional | object | Ship to contact |
| USEDINGL | Optional | boolean | Used in GL. Use `false` for No, `true` for Yes. (Default: `true`) |
| STATUS | Optional | string | Warehouse status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| ENABLE\_REPLENISHMENT | Optional | boolean | Enable replenishment for this warehouse. Use `true` to enable, otherwise use `false`. (Default: `true`) |
| ENABLENEGATIVEINV | Optional | boolean | Enable negative inventory for this warehouse. This option lets you enable negative inventory for a specific warehouse, assuming that the company is not already configured to allow negative inventory. Use `true` to enable negative inventory for this warehouse, otherwise use `false`. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`LOC`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATIONID | Required | string | Location ID of warehouse |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Primary contact name |

`SHIPTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Ship to contact name |

* * *

Delete Warehouse
----------------

#### `delete`

```
<delete>
    <object>WAREHOUSE</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `WAREHOUSE` |
| keys | Required | string | Comma-separated list of warehouse `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

