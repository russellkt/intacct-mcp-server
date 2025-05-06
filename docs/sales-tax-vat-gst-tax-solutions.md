Title: Tax Solutions

URL Source: https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/

Markdown Content:
*   [Get Tax Solution Object Definition](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/#get-tax-solution-object-definition)
*   [Query and List Tax Solutions](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/#query-and-list-tax-solutions)
*   [Query and List Tax Solutions (Legacy)](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/#query-and-list-tax-solutions-legacy)
*   [Get Tax Solution](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/#get-tax-solution)
*   [Get Tax Solution by ID](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/#get-tax-solution-by-id)

* * *

A tax solution provides the underlying mechanism (tax engine) for capturing and reporting taxes. (AU, GB, ZA only)

The tax solution also includes information about the GL accounts for input and output taxes as well as the start date of the first tax submission period.

* * *

Get Tax Solution Object Definition
----------------------------------

#### `lookup`

> List all the fields and relationships for the tax solution object:

```
<lookup>
    <object>TAXSOLUTION</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXSOLUTION` |

* * *

Query and List Tax Solutions
----------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, tax solution ID, and tax calculation method for each tax solution:

```
<query>
    <object>TAXSOLUTION</object>
    <select>
        <field>RECORDNO</field>
        <field>SOLUTIONID</field>
        <field>TAXMETHOD</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXSOLUTION` |
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

Query and List Tax Solutions (Legacy)
-------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>TAXSOLUTION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXSOLUTION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Tax Solution
----------------

#### `read`

```
<read>
    <object>TAXSOLUTION</object>
    <keys>2</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXSOLUTION` |
| keys | Required | string | Comma-separated list of record number of the tax solution |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Tax Solution by ID
----------------------

#### `readByName`

```
<readByName>
    <object>TAXSOLUTION</object>
    <keys>Australia - GST</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TAXSOLUTION` |
| keys | Required | string | Comma-separated list of tax solution name (`TAXSOLUTIONID`) |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

