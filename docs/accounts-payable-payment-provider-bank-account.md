Title: Payment Provider Bank Accounts

URL Source: https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/

Markdown Content:
*   [Get Payment Provider Bank Account Object Definition](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#get-payment-provider-bank-account-object-definition)
*   [Query and List Payment Provider Bank Accounts](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#query-and-list-payment-provider-bank-accounts)
*   [Query and List Payment Provider Bank Accounts (Legacy)](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#query-and-list-payment-provider-bank-accounts-legacy)
*   [Get Payment Provider Bank Account](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#get-payment-provider-bank-account)
*   [Create Payment Provider Bank Account](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#create-payment-provider-bank-account)
*   [Update Payment Provider Bank Account](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#update-payment-provider-bank-account)

* * *

Payment provider services, like Vendor Payments powered by CSI, are only for US vendors accepting USD.

You can link a bank account with a given electronic payment provider as part of your setup for electronic payments.

A subscription to Outbound Payment Services is required.

* * *

Get Payment Provider Bank Account Object Definition
---------------------------------------------------

#### `lookup`

> List all the fields and relationships for the payment provider bank account object:

```
<lookup>
    <object>PROVIDERBANKACCOUNT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERBANKACCOUNT` |

* * *

Query and List Payment Provider Bank Accounts
---------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the objects that map a bank account to a payment provider:

```
<query>
    <object>PROVIDERBANKACCOUNT</object>
    <select>
        <field>BANKACCOUNTID</field>
        <field>PROVIDERID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERBANKACCOUNT` |
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

Query and List Payment Provider Bank Accounts (Legacy)
------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PROVIDERBANKACCOUNT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERBANKACCOUNT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Payment Provider Bank Account
---------------------------------

#### `read`

```
<read>
    <object>PROVIDERBANKACCOUNT</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROVIDERBANKACCOUNT` |
| keys | Required | string | Comma-separated list of record number of payment provider bank account object |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Payment Provider Bank Account
------------------------------------

[History](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#history-create-payment-provider-bank-account)

| Release | Changes |
| --- | --- |
| 2021 Release 4 | Added ISREBATEACCOUNT |
| 2021 Release 2 | Added CHECKSTARTNO |

#### `create`

```
<create>
    <PROVIDERBANKACCOUNT>
        <PROVIDERID>CSI</PROVIDERID>
        <VENDORID>Acme</VENDORID>
    </PROVIDERBANKACCOUNT>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROVIDERBANKACCOUNT` | Required | object | Object to create |

`PROVIDERBANKACCOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `BANKACCOUNTID` | Required | string | ID for bank account. The bank account must have a valid street address and email address. |
| `PROVIDERID` | Required | string | ID for the payment provider |
| `STATUS` | Required | string | Status. Use `active` or `inactive`. |
| `CHECKSTARTNO` | Optional | integer | Starting number for the check sequence for check payments. |
| `ISREBATEACCOUNT` | Optional | boolean | Set this to `true` to indicate that this account should be used for rebates. (Default: `false`) |

* * *

Update Payment Provider Bank Account
------------------------------------

[History](https://developer.intacct.com/api/accounts-payable/payment-provider-bank-account/#history-update-payment-provider-bank-account)

| Release | Changes |
| --- | --- |
| 2021 Release 4 | Added ISREBATEACCOUNT |
| 2021 Release 2 | Added CHECKSTARTNO |

#### `update`

```
<update>
    <PROVIDERBANKACCOUNT>
        <RECORDNO>5</RECORDNO>
        <STATUS>inactive</STATUS>
    </PROVIDERBANKACCOUNT>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROVIDERBANKACCOUNT` | Required | object | Object to update |

`PROVIDERBANKACCOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `RECORDNO` | Required | integer | `RECORDNO` of the payment provider bank account to update |
| `STATUS` | Optional | string | Status. Use `active` or `inactive`. |
| `CHECKSTARTNO` | Optional | integer | Starting number for the check sequence for check payments. |
| `ISREBATEACCOUNT` | Optional | boolean | Set this to `true` to indicate that this account should be used for rebates. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

