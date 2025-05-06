Title: Zones

URL Source: https://developer.intacct.com/api/inventory-control/zones/

Markdown Content:
*   [Get Zone Object Definition](https://developer.intacct.com/api/inventory-control/zones/#get-zone-object-definition)
*   [Query and List Zones](https://developer.intacct.com/api/inventory-control/zones/#query-and-list-zones)
*   [Query and List Zones (Legacy)](https://developer.intacct.com/api/inventory-control/zones/#query-and-list-zones-legacy)
*   [Get Zone](https://developer.intacct.com/api/inventory-control/zones/#get-zone)
*   [Get Zone by ID](https://developer.intacct.com/api/inventory-control/zones/#get-zone-by-id)
*   [Create Zone](https://developer.intacct.com/api/inventory-control/zones/#create-zone)
*   [Update Zone](https://developer.intacct.com/api/inventory-control/zones/#update-zone)
*   [Delete Zone](https://developer.intacct.com/api/inventory-control/zones/#delete-zone)

* * *

A zone is one the four optional attributes (zone, aisle, row, and bin face) that you can assign to a bin to make it easier to find in the warehouse.

Typically, zones are used when you store your items in separate areas of the warehouse based on the characteristics of the items. For example, you might have zones for receiving, refrigeration, dry storage, security storage, and oversize storage.

* * *

Get Zone Object Definition
--------------------------

#### `lookup`

> List all the fields and relationships for the zone object:

```
<lookup>
    <object>ZONE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ZONE` |

* * *

Query and List Zones
--------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the zone ID and description for each zone:

```
<query>
    <object>ZONE</object>
    <select>
        <field>ZONEID</field>
        <field>ZONEDESC</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ZONE` |
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

Query and List Zones (Legacy)
-----------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ZONE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ZONE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Zone
--------

#### `read`

```
<read>
    <object>ZONE</object>
    <keys>9</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ZONE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Zone by ID
--------------

#### `readByName`

```
<readByName>
    <object>ZONE</object>
    <keys>Z2</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ZONE` |
| keys | Required | string | Comma-separated list of object `ZONEID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Zone
-----------

#### `create`

```
<create>
    <ZONE>
        <ZONEID>Z2</ZONEID>
        <ZONEDESC>Zone 02</ZONEDESC>
    </ZONE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ZONE | Required | object | Object to create |

`ZONE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ZONEID | Required | string | Unique identifier for the zone. The zone ID cannot be modified. |
| ZONEDESC | Optional | string | Description for the zone |

* * *

Update Zone
-----------

#### `update`

```
<update>
    <ZONE>
        <RECORDNO>9</RECORDNO>
        <ZONEDESC>Refrigeration zone 2</ZONEDESC>
    </ZONE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ZONE | Required | object | Object to create |

`ZONE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Zone `RECORDNO` to update. Required if not supplying the zone ID. |
| ZONEID | Optional | string | Unique identifier for the zone. Required if not supplying the zone record number. The zone ID cannot be modified. |
| ZONEDESC | Optional | string | Description for the zone |

* * *

Delete Zone
-----------

#### `delete`

```
<delete>
    <object>ZONE</object>
    <keys>9</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ZONE` |
| keys | Required | string | Comma-separated list of zone `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

