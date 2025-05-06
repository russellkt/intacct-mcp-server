Title: Bins

URL Source: https://developer.intacct.com/api/inventory-control/bins/

Markdown Content:
*   [Get Bin Object Definition](https://developer.intacct.com/api/inventory-control/bins/#get-bin-object-definition)
*   [Query and List Bins](https://developer.intacct.com/api/inventory-control/bins/#query-and-list-bins)
*   [Query and List Bins (Legacy)](https://developer.intacct.com/api/inventory-control/bins/#query-and-list-bins-legacy)
*   [Get Bin](https://developer.intacct.com/api/inventory-control/bins/#get-bin)
*   [Get Bin by ID](https://developer.intacct.com/api/inventory-control/bins/#get-bin-by-id)
*   [Create Bin](https://developer.intacct.com/api/inventory-control/bins/#create-bin)
*   [Update Bin](https://developer.intacct.com/api/inventory-control/bins/#update-bin)
*   [Delete Bin](https://developer.intacct.com/api/inventory-control/bins/#delete-bin)

* * *

A bin contains stocking information about items in a warehouse and identifies its location within the warehouse.

* * *

Get Bin Object Definition
-------------------------

#### `lookup`

> List all the fields and relationships for the bin object:

```
<lookup>
    <object>BIN</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BIN` |

* * *

Query and List Bins
-------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> For each bin in the given warehouse, list the bin ID and description:

```
<query>
    <object>BIN</object>
    <select>
        <field>BINID</field>
        <field>BINDESC</field>
    </select>
    <filter>
        <equalto>
            <field>WAREHOUSEID</field>
            <value>01</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BIN` |
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

Query and List Bins (Legacy)
----------------------------

#### `readByQuery`

```
<readByQuery>
    <object>BIN</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BIN` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Bin
-------

#### `read`

```
<read>
    <object>BIN</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BIN` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Bin by ID
-------------

#### `readByName`

```
<readByName>
    <object>BIN</object>
    <keys>Z2-A2a-R4-BF2-B2</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BIN` |
| keys | Required | string | Comma-separated list of object `BINID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Bin
----------

#### `create`

```
<create>
    <BIN>
        <BINID>Z2-A2a-R4-BF2-B2</BINID>
        <BINDESC>Bin 02</BINDESC>
        <WAREHOUSEID>01</WAREHOUSEID>
        <ZONEID>Z2</ZONEID>
        <AISLEID>A2a</AISLEID>
        <ROWID>R4</ROWID>
        <FACEID>F2</FACEID>
        <BINSIZEID>S</BINSIZEID>
    </BIN>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BIN | Required | object | Object to create |

`BIN`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BINID | Required | string | Unique identifier for the bin. Consider using an identifier that makes it easier to find the bin. For example, if bin 10 is in zone 4, aisle 2, row 3a, and bin face 2, you might use `Z4-A2-R3a-BF2-B10` for the ID. |
| BINDESC | Optional | string | Description for the bin |
| BINSIZEID | Optional | string | ID for the bin size |
| SEQUENCENO | Optional | numeric | Sequence number for the bin. Sequence numbering supports more efficient picking and packing, and cycle counts. |
| STATUS | Optional | string | Status of the bin. Use `active` or `inactive` (Default: `active`) |
| PORTABLE | Optional | boolean | Use `true` if the bin can be moved to another location, `false` otherwise (Default: `false`). |
| WAREHOUSEID | Optional | string | ID of the warehouse |
| ZONEID | Optional | string | ID of the zone |
| AISLEID | Optional | string | ID of the aisle |
| ROWID | Optional | string | ID of the row |
| FACEID | Optional | string | ID of the bin face |

* * *

Update Bin
----------

#### `update`

> Update the status of the bin with the given ID:

```
<update>
    <BIN>
        <BINID>Z2-A2a-R4-BF2-B2</BINID>
        <STATUS>inactive</STATUS>
    </BIN>
</update>
```

> Update the ID of the bin with the given record number:

```
<update>
    <BIN>
        <RECORDNO>7</RECORDNO>
        <BINID>Z2-A2a-R4-BF3-B3</BINID>
        <STATUS>active</STATUS>
    </BIN>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BIN | Required | object | Object to update |

`BIN`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BINID | Optional | string | ID of the bin. Required if not providing a record number. |
| RECORDNO | Optional | string | Record number of the bin. Required if not providing a bin ID. |
| BINDESC | Optional | string | Description for the bin |
| BINSIZEID | Optional | string | ID of the bin size |
| SEQUENCENO | Optional | numeric | Sequence number for the bin. Sequence numbering supports more efficient picking and packing, and cycle counts. |
| STATUS | Optional | string | Status of the bin. Use `active` or `inactive`. Bins should only be set to to `inactive` when empty. |
| PORTABLE | Optional | boolean | Use `true` if the bin can be moved to another location, `false` otherwise. Bins should only be set as portable when empty. |
| WAREHOUSEID | Optional | string | ID of the warehouse |
| ZONEID | Optional | string | ID of the zone |
| AISLEID | Optional | string | ID of the aisle |
| ROWID | Optional | string | ID of the row |
| FACEID | Optional | string | ID of the bin face |

* * *

Delete Bin
----------

#### `delete`

```
<delete>
    <object>BIN</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BIN` |
| keys | Required | string | Comma-separated list of bin `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

