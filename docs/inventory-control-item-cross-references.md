Title: Item Cross References

URL Source: https://developer.intacct.com/api/inventory-control/item-cross-references/

Markdown Content:
*   [Get Item Cross Reference Object Definition](https://developer.intacct.com/api/inventory-control/item-cross-references/#get-item-cross-reference-object-definition)
*   [Query and List Item Cross References](https://developer.intacct.com/api/inventory-control/item-cross-references/#query-and-list-item-cross-references)
*   [Query and List Item Cross References (Legacy)](https://developer.intacct.com/api/inventory-control/item-cross-references/#query-and-list-item-cross-references-legacy)
*   [Get Item Cross Reference](https://developer.intacct.com/api/inventory-control/item-cross-references/#get-item-cross-reference)
*   [Create Item Cross Reference](https://developer.intacct.com/api/inventory-control/item-cross-references/#create-item-cross-reference)
*   [Update Item Cross Reference](https://developer.intacct.com/api/inventory-control/item-cross-references/#update-item-cross-reference)
*   [Delete Item Cross Reference](https://developer.intacct.com/api/inventory-control/item-cross-references/#delete-item-cross-reference)

* * *

An item cross reference lets you associate one of your company’s inventory items with a specific customer or vendor, or with another inventory item.

When you associate an inventory item with a customer or vendor (known as an `external cross-reference`), your customer or vendor can provide their own identifiers for inventory items that can be used in transactions.

When you associate an inventory item with another inventory item (known as an `internal cross-reference`), you can provide alternate items to substitute, upgrade, downgrade, or complement items in Order Entry transactions in the Sage Intacct UI.

* * *

Get Item Cross Reference Object Definition
------------------------------------------

#### `lookup`

> List all the fields and relationships for the item cross reference object:

```
<lookup>
    <object>ITEMCROSSREF</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMCROSSREF` |

* * *

Query and List Item Cross References
------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the item ID and reference type for each cross reference:

```
<query>
    <object>ITEMCROSSREF</object>
    <select>
        <field>ITEMID</field>
        <field>REFTYPE</field>
    </select>
</query>
```

> List available alternatives, such as substitutes or upgrades, for the monitor item:

```
<query>
    <object>ITEMCROSSREF</object>
    <select>
        <field>RECORDNO</field>
        <field>ITEMID</field>
        <field>REFTYPE</field>
        <field>ALTERNATEITEMID</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>ITEMID</field>
                <value>Monitor</value>
            </equalto>
            <equalto>
                <field>REFTYPECONTEXT</field>
                <value>Internal</value>
            </equalto>
        </and>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMCROSSREF` |
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

Query and List Item Cross References (Legacy)
---------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ITEMCROSSREF</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMCROSSREF` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Item Cross Reference
------------------------

#### `read`

```
<read>
    <object>ITEMCROSSREF</object>
    <keys>101</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMCROSSREF` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Item Cross Reference
---------------------------

[History](https://developer.intacct.com/api/inventory-control/item-cross-references/#history-create-item-cross-reference)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added ALTERNATEITEMID, added Substitute, Upgrade, Downgrade, and Complement values for REFTYPE |

#### `create`

> Create a cross reference to associate inventory item L-12 with the Acme vendor and use their alias name, BL-01, for that item:

```
<create>
    <ITEMCROSSREF>
        <REFTYPE>Vendor</REFTYPE>
        <ITEMID>L-12</ITEMID>
        <VENDORID>Acme</VENDORID>
        <ITEMALIASID>BL-01</ITEMALIASID>
        <ITEMALIASDESC>Base laptop</ITEMALIASDESC>
    </ITEMCROSSREF>
</create>
```

> Create a cross reference to associate inventory item L-14 with a substitute inventory item, L-16:

```
<create>
    <ITEMCROSSREF>
        <REFTYPE>Substitute</REFTYPE>
        <ITEMID>L-14</ITEMID>
        <ALTERNATEITEMID>L-16</ALTERNATEITEMID>
    </ITEMCROSSREF>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEMCROSSREF | Required | object | Object to create |

`ITEMCROSSREF`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| REFTYPE | Required | string | Reference type. Use `Vendor` or `Customer` for an external cross reference, or use `Substitute`, `Upgrade`, `Downgrade`, or `Complement` for an internal cross reference. |
| ITEMID | Required | string | ID of the inventory item that will have the cross reference. |
| ALTERNATEITEMID | Optional | string | ID of an alternate item. Required when using an internal cross reference type, such as `Substitute` or `Upgrade`. |
| VENDORID | Optional | string | Vendor ID, which is required if using a `Vendor` reference type |
| CUSTOMERID | Optional | string | Customer ID, which is required if using a `Customer` reference type |
| ITEMALIASID | Optional | string | Required for external cross references. Identifier for the item as understood by the given vendor or customer. Must be unique for the combination of vendor/item or customer/item. |
| ITEMALIASDESC | Optional | string | Description of the cross reference |
| UNIT | Optional | string | Valid unit of measure for the item |

* * *

Update Item Cross Reference
---------------------------

[History](https://developer.intacct.com/api/inventory-control/item-cross-references/#history-update-item-cross-reference)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added ALTERNATEITEMID |

#### `update`

> Update the description for the item cross reference:

```
<update>
    <ITEMCROSSREF>
        <RECORDNO>101</RECORDNO>
        <ITEMALIASDESC>Base laptop 2</ITEMALIASDESC>
    </ITEMCROSSREF>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEMCROSSREF | Required | object | Object to update |

`ITEMCROSSREF`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the item cross reference |
| ALTERNATEITEMID | Optional | string | ID of an alternate item for an internal cross reference type, such as `Substitute` or `Upgrade`. |
| ITEMALIASID | Optional | string | Alias for the item as understood by the relevant vendor or customer. Must be unique for the combination of vendor/item or customer/item. |
| ITEMALIASDESC | Optional | string | Description of the cross reference |
| UNIT | Optional | string | Valid unit of measure for the item |

* * *

Delete Item Cross Reference
---------------------------

#### `delete`

```
<delete>
    <object>ITEMCROSSREF</object>
    <keys>101</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEMCROSSREF` |
| keys | Required | string | Comma-separated list of item cross reference `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

