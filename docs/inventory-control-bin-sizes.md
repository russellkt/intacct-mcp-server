Title: Bin Sizes

URL Source: https://developer.intacct.com/api/inventory-control/bin-sizes/

Markdown Content:
*   [Get Bin Size Object Definition](https://developer.intacct.com/api/inventory-control/bin-sizes/#get-bin-size-object-definition)
*   [Query and List Bin Sizes](https://developer.intacct.com/api/inventory-control/bin-sizes/#query-and-list-bin-sizes)
*   [Query and List Bin Sizes (Legacy)](https://developer.intacct.com/api/inventory-control/bin-sizes/#query-and-list-bin-sizes-legacy)
*   [Get Bin Size](https://developer.intacct.com/api/inventory-control/bin-sizes/#get-bin-size)
*   [Get Bin by ID](https://developer.intacct.com/api/inventory-control/bin-sizes/#get-bin-by-id)
*   [Create Bin Size](https://developer.intacct.com/api/inventory-control/bin-sizes/#create-bin-size)
*   [Update Bin Size](https://developer.intacct.com/api/inventory-control/bin-sizes/#update-bin-size)
*   [Delete Bin Size](https://developer.intacct.com/api/inventory-control/bin-sizes/#delete-bin-size)

* * *

A bin size in an attribute you can assign to a bin to make it easier to decide whether the bin is suitable for putting away items.

* * *

Get Bin Size Object Definition
------------------------------

#### `lookup`

> List all the fields and relationships for the bin size object:

```
<lookup>
    <object>BINSIZE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINSIZE` |

* * *

Query and List Bin Sizes
------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the ID and description for each bin size:

```
<query>
    <object>BINSIZE</object>
    <select>
        <field>SIZEID</field>
        <field>SIZEDESC</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINSIZE` |
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

Query and List Bin Sizes (Legacy)
---------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>BINSIZE</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINSIZE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Bin Size
------------

#### `read`

```
<read>
    <object>BINSIZE</object>
    <keys>4</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINSIZE` |
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
    <object>BINSIZE</object>
    <keys>S</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINSIZE` |
| keys | Required | string | Comma-separated list of object `SIZEID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Bin Size
---------------

#### `create`

```
<create>
    <BINSIZE>
        <SIZEID>S</SIZEID>
        <SIZEDESC>4x4</SIZEDESC>
    </BINSIZE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BINSIZE | Required | object | Object to create |

`BINSIZE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SIZEID | Required | string | Unique identifier for the bin size. The size ID cannot be modified. |
| SIZEDESC | Optional | string | Description for the bin size |

* * *

Update Bin Size
---------------

#### `update`

```
<update>
    <BINSIZE>
        <RECORDNO>4</RECORDNO>
        <BINDESC>4x8</BINDESC>
    </BINSIZE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BINSIZE | Required | object | Object to create |

`BINSIZE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Bin size `RECORDNO` to update. Required if not supplying the size ID. |
| SIZEID | Optional | string | Unique identifier for the bin size. Required if not supplying the bin size record number. The size ID cannot be modified. |
| SIZEDESC | Optional | string | Description for the bin size |

* * *

Delete Bin Size
---------------

#### `delete`

```
<delete>
    <object>BINSIZE</object>
    <keys>4</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BINSIZE` |
| keys | Required | string | Comma-separated list of bin size `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

