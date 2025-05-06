Title: Tax Records

URL Source: https://developer.intacct.com/api/sales-tax-vat-gst/tax-records/

Markdown Content:
*   [Get Tax Record Object Definition](https://developer.intacct.com/api/sales-tax-vat-gst/tax-records/#get-tax-record-object-definition)
*   [Query and List Tax Records](https://developer.intacct.com/api/sales-tax-vat-gst/tax-records/#query-and-list-tax-records)
*   [Query and List Tax Records (Legacy)](https://developer.intacct.com/api/sales-tax-vat-gst/tax-records/#query-and-list-tax-records-legacy)
*   [Get Tax Record](https://developer.intacct.com/api/sales-tax-vat-gst/tax-records/#get-tax-record)
*   [Update Tax Record](https://developer.intacct.com/api/sales-tax-vat-gst/tax-records/#update-tax-record)

* * *

A tax record is an object used for creating reports about taxes, such as VAT or GST, for compliance purposes. (AU, GB, ZA only)

* * *

Get Tax Record Object Definition
--------------------------------

#### `lookup`

> List all the fields and relationships for the tax record object:

```
<lookup>
    <object>TAXRECORD</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXRECORD` |

* * *

Query and List Tax Records
--------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, description, and tax type for each tax record:

```
<query>
    <object>TAXRECORD</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
        <field>TAXTYPE</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXRECORD` |
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

Query and List Tax Records (Legacy)
-----------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>TAXRECORD</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXRECORD` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TAXTYPE | Optional | string | Tax type for the tax record. Use `I` for input tax or `O` for output tax. |
| STATE | Optional | string | State of the source transaction. Use `S` for submitted, `P` for posted, or `F` for filed. |

* * *

Get Tax Record
--------------

#### `read`

```
<read>
    <object>TAXRECORD</object>
    <keys>102</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXRECORD` |
| keys | Required | string | Comma-separated list of record number of the tax record |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Update Tax Record
-----------------

You can update custom fields on a tax record. Update of standard fields is not supported.

#### `update`

> Update the MCA\_NOTES custom field with the given text:

```
<update>
    <TAXRECORD>
        <RECORDNO>12</RECORDNO>
        <MCA_NOTES>my text</MCA_NOTES>
    </TAXRECORD>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TAXRECORD | Required | object | Object to update |

`TAXRECORD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Tax record `RECORDNO` to update |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

