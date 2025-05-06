Title: Order Entry Price Lists

URL Source: https://developer.intacct.com/api/order-entry/price-lists/

Markdown Content:
*   [Get Order Entry Price List Object Definition](https://developer.intacct.com/api/order-entry/price-lists/#get-order-entry-price-list-object-definition)
*   [Query and List Order Entry Price Lists](https://developer.intacct.com/api/order-entry/price-lists/#query-and-list-order-entry-price-lists)
*   [Query and List Order Entry Price Lists (Legacy)](https://developer.intacct.com/api/order-entry/price-lists/#query-and-list-order-entry-price-lists-legacy)
*   [Get Order Entry Price List](https://developer.intacct.com/api/order-entry/price-lists/#get-order-entry-price-list)
*   [Get Order Entry Price List by ID](https://developer.intacct.com/api/order-entry/price-lists/#get-order-entry-price-list-by-id)
*   [Create Order Entry Price List (Legacy)](https://developer.intacct.com/api/order-entry/price-lists/#create-order-entry-price-list-legacy)
*   [Update Order Entry Price List (Legacy)](https://developer.intacct.com/api/order-entry/price-lists/#update-order-entry-price-list-legacy)
*   [Delete Order Entry Price List (Legacy)](https://developer.intacct.com/api/order-entry/price-lists/#delete-order-entry-price-list-legacy)

* * *

An Order Entry price list contains the names of price lists in Order Entry.

* * *

Get Order Entry Price List Object Definition
--------------------------------------------

#### `lookup`

> List all the fields and relationships for the Order Entry price list object:

```
<lookup>
    <object>SOPRICELIST</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SOPRICELIST` |

* * *

Query and List Order Entry Price Lists
--------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each Order Entry price list:

```
<query>
    <object>SOPRICELIST</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SOPRICELIST` |
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

Query and List Order Entry Price Lists (Legacy)
-----------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>SOPRICELIST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SOPRICELIST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Order Entry Price List
--------------------------

#### `read`

```
<read>
    <object>SOPRICELIST</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SOPRICELIST` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Order Entry Price List by ID
--------------------------------

#### `readByName`

```
<readByName>
    <object>SOPRICELIST</object>
    <keys>Full Time</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SOPRICELIST` |
| keys | Required | string | Comma-separated list of object `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Order Entry Price List (Legacy)
--------------------------------------

#### `create_sopricelist`

```
<create_sopricelist>
    <name>Special Order Entry price list</name>
</create_sopricelist>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Price list name to create |
| datefrom | Optional | object | Date from |
| dateto | Optional | object | Date to |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

`datefrom`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`dateto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Update Order Entry Price List (Legacy)
--------------------------------------

#### `update_sopricelist`

```
<update_sopricelist name="Special Order Entry price list">
    <status>active</status>
</update_sopricelist>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Price list name to update |
| datefrom | Optional | object | Date from |
| dateto | Optional | object | Date to |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |

`datefrom`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`dateto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Delete Order Entry Price List (Legacy)
--------------------------------------

#### `delete_sopricelist`

```
<delete_sopricelist name="Special Order Entry price list"></delete_sopricelist>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Price list name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

