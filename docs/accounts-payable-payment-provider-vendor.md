Title: Payment Provider Vendor

URL Source: https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/

Markdown Content:
*   [Get Payment Provider Vendor Object Definition](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#get-payment-provider-vendor-object-definition)
*   [Query and List Payment Provider Vendors](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#query-and-list-payment-provider-vendors)
*   [Query and List Payment Provider Vendors (Legacy)](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#query-and-list-payment-provider-vendors-legacy)
*   [Get Payment Provider Vendor](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#get-payment-provider-vendor)
*   [Create Payment Provider Vendor](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#create-payment-provider-vendor)
*   [Update Payment Provider Vendor](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#update-payment-provider-vendor)

* * *

Payment provider services, like Vendor Payments powered by CSI, are only for US vendors accepting USD.

You can link a vendor with a given electronic payment provider as part of your setup for electronic payments.

Alternatively, you can create this linkage using the create and update functions on the [vendor](https://developer.intacct.com/api/accounts-payable/vendors/) object.

A subscription to Outbound Payment Services is required.

* * *

Get Payment Provider Vendor Object Definition
---------------------------------------------

#### `lookup`

> List all the fields and relationships for the payment provider vendor object:

```
<lookup>
    <object>PROVIDERVENDOR</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERVENDOR` |

* * *

Query and List Payment Provider Vendors
---------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the objects that map a vendor to a payment provider:

```
<query>
    <object>PROVIDERVENDOR</object>
    <select>
        <field>VENDORID</field>
        <field>PROVIDERID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERVENDOR` |
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

Query and List Payment Provider Vendors (Legacy)
------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PROVIDERVENDOR</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERVENDOR` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

#### `read`

```
<read>
    <object>PROVIDERVENDOR</object>
    <keys>7</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERVENDOR` |
| keys | Required | string | Comma-separated list of record number of payment provider vendor object |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Payment Provider Vendor
------------------------------

#### `create`

```
<create>
    <PROVIDERVENDOR>
        <PROVIDERID>CSI</PROVIDERID>
        <VENDORID>Acme</VENDORID>
        <STATUS>active</STATUS>
    </PROVIDERVENDOR>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROVIDERVENDOR` | Required | object | Object to create |

`PROVIDERVENDOR`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `VENDORID` | Required | string | ID for vendor. The vendor must have a valid street address and email address. |
| `PROVIDERID` | Required | string | ID for the payment provider |
| `STATUS` | Required | string | Status. Use `active` or `inactive`. |

* * *

Update Payment Provider Vendor
------------------------------

#### `update`

```
<update>
    <PROVIDERVENDOR>
        <RECORDNO>5</RECORDNO>
        <STATUS>inactive</STATUS>
    </PROVIDERVENDOR>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROVIDERVENDOR` | Required | object | Object to update |

`PROVIDERVENDOR`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | `RECORDNO` of the payment provider vendor update |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

