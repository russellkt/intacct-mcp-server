Title: Bin Faces

URL Source: https://developer.intacct.com/api/inventory-control/bin-faces/

Markdown Content:
*   [Get Bin Face Object Definition](https://developer.intacct.com/api/inventory-control/bin-faces/#get-bin-face-object-definition)
*   [Query and List Bin Faces](https://developer.intacct.com/api/inventory-control/bin-faces/#query-and-list-bin-faces)
*   [Query and List Bin Faces (Legacy)](https://developer.intacct.com/api/inventory-control/bin-faces/#query-and-list-bin-faces-legacy)
*   [Get Bin Face](https://developer.intacct.com/api/inventory-control/bin-faces/#get-bin-face)
*   [Get Bin Face by ID](https://developer.intacct.com/api/inventory-control/bin-faces/#get-bin-face-by-id)
*   [Create Bin Face](https://developer.intacct.com/api/inventory-control/bin-faces/#create-bin-face)
*   [Update Bin Face](https://developer.intacct.com/api/inventory-control/bin-faces/#update-bin-face)
*   [Delete Bin Face](https://developer.intacct.com/api/inventory-control/bin-faces/#delete-bin-face)

* * *

A bin face is one of the four optional attributes (zone, aisle, row, and bin face) that you can assign to a bin to make it easier to find the location of the bin within the warehouse.

Typically, each section between pillars in an aisle is considered a bin face.

* * *

Get Bin Face Object Definition
------------------------------

#### `lookup`

> List all the fields and relationships for the bin face object:

```
<lookup>
    <object>BINFACE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINFACE` |

* * *

Query and List Bin Faces
------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the ID and description for each bin face:

```
<query>
    <object>BINFACE</object>
    <select>
        <field>FACEID</field>
        <field>FACEDESC</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINFACE` |
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

Query and List Bin Faces (Legacy)
---------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>BINFACE</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINFACE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Bin Face
------------

#### `read`

```
<read>
    <object>BINFACE</object>
    <keys>4</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINFACE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Bin Face by ID
------------------

#### `readByName`

```
<readByName>
    <object>BINFACE</object>
    <keys>F2</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINFACE` |
| keys | Required | string | Comma-separated list of object `FACEID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Bin Face
---------------

#### `create`

```
<create>
    <BINFACE>
        <FACEID>F2</FACEID>
        <FACEDESC>Bin Face 02</FACEDESC>
    </BINFACE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BINFACE | Required | object | Object to create |

`BINFACE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FACEID | Required | string | Unique identifier for the bin face. The face ID cannot be modified. |
| FACEDESC | Optional | string | Description for the bin face |

* * *

Update Bin Face
---------------

#### `update`

```
<update>
    <BINFACE>
        <FACEID>F2</FACEID>
        <FACEDESC>Bin Face 02-1</FACEDESC>
    </BINFACE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BINFACE | Required | object | Object to create |

`BINFACE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Bin face `RECORDNO` to update. Required if not supplying the face ID. |
| FACEID | Optional | string | Unique identifier for the bin face. Required if not supplying the bin face record number. The face ID cannot be modified. |
| FACEDESC | Optional | string | Description for the bin face |

* * *

Delete Bin Face
---------------

#### `delete`

```
<delete>
    <object>BINFACE</object>
    <keys>4</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINFACE` |
| keys | Required | string | Comma-separated list of bin face `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

