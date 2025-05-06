Title: Payment Provider Payment Methods

URL Source: https://developer.intacct.com/api/accounts-payable/payment-provider-payment-method/

Markdown Content:
*   [Get Payment Provider Payment Method Object Definition](https://developer.intacct.com/api/accounts-payable/payment-provider-payment-method/#get-payment-provider-payment-method-object-definition)
*   [Query and List Payment Provider Payment Methods](https://developer.intacct.com/api/accounts-payable/payment-provider-payment-method/#query-and-list-payment-provider-payment-methods)
*   [Query and List Payment Provider Payment Methods (Legacy)](https://developer.intacct.com/api/accounts-payable/payment-provider-payment-method/#query-and-list-payment-provider-payment-methods-legacy)
*   [Get Payment Provider Payment Method](https://developer.intacct.com/api/accounts-payable/payment-provider-payment-method/#get-payment-provider-payment-method)

* * *

Payment provider services, like Vendor Payments powered by CSI, are only for US vendors accepting USD.

This object provides information about available electronic payment providers and their supported payment methods.

After confirming the payment provider information, you can associate a [vendor](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/) and a [bank account](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/) with that payment provider.

A subscription to Outbound Payment Services is required.

* * *

Get Payment Provider Payment Method Object Definition
-----------------------------------------------------

#### `lookup`

> List all the fields and relationships for the payment provider payment method object:

```
<lookup>
    <object>PROVIDERPAYMENTMETHOD</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERPAYMENTMETHOD` |

* * *

Query and List Payment Provider Payment Methods
-----------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, provider ID, and payment type for each provider payment method:

```
<query>
    <object>PROVIDERPAYMENTMETHOD</object>
    <select>
        <field>RECORDNO</field>
        <field>PROVIDERID</field>
        <field>PAYMENTTYPE</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERPAYMENTMETHOD` |
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

Query and List Payment Provider Payment Methods (Legacy)
--------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PROVIDERPAYMENTMETHOD</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERPAYMENTMETHOD` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Payment Provider Payment Method
-----------------------------------

#### `read`

```
<read>
    <object>PROVIDERPAYMENTMETHOD</object>
    <keys>2</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERPAYMENTMETHOD` |
| keys | Required | string | Comma-separated list of record number of payment provider payment method object |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

