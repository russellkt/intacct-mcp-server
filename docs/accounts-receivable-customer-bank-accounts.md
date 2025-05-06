Title: Customer Bank Accounts

URL Source: https://developer.intacct.com/api/accounts-receivable/customer-bank-accounts/

Markdown Content:
*   [Create Customer Bank Account (Legacy)](https://developer.intacct.com/api/accounts-receivable/customer-bank-accounts/#create-customer-bank-account-legacy)
*   [Update Customer Bank Account (Legacy)](https://developer.intacct.com/api/accounts-receivable/customer-bank-accounts/#update-customer-bank-account-legacy)
*   [Delete Customer Bank Account (Legacy)](https://developer.intacct.com/api/accounts-receivable/customer-bank-accounts/#delete-customer-bank-account-legacy)

* * *

Customer bank accounts are used in AR Payment Services.

**Important:** The customer bank account object and its supported functions will be deprecated in 2025 Release 4.

* * *

Create Customer Bank Account (Legacy)
-------------------------------------

#### `create_customerbankaccount`

```
<create_customerbankaccount>
    <customerid>C1234</customerid>
    <accountnumber>1234567890</accountnumber>
    <routingnumber>098765432</routingnumber>
    <accounttype>Business Checking Account</accounttype>
    <bankname>Bank of Intacct</bankname>
    <accountholder>My customer XYZ</accountholder>
</create_customerbankaccount>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customerid | Required | string | Customer ID |
| accountnumber | Required | string | Bank account number |
| routingnumber | Required | string | Routing number |
| accounttype | Required | string | Bank account type. Use `Business Checking Account`, `Personal Checking Account`, or `Personal Savings Account` |
| bankname | Required | string | Bank name |
| accountholder | Required | string | Account holder |
| description | Optional | string | Description |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| mailaddress | Optional | object | Mail address |
| defaultaccount | Optional | boolean | Default bank account. Use `false` for No, `true` for Yes. (Default: `true`) |

`mailaddress`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| address1 | Optional | string | Address line 1 |
| address2 | Optional | string | Address line 2 |
| address3 | Optional | string | Address line 3 |
| city | Optional | string | City |
| state | Optional | string | State/province |
| zip | Optional | string | Zip/postal code |
| country | Optional | string | Country |
| isocountrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `isocountrycode` must be provided. |

* * *

Update Customer Bank Account (Legacy)
-------------------------------------

#### `update_customerbankaccount`

```
<update_customerbankaccount recordno="123">
    <accountholder>My customer XYZ</accountholder>
    <description>hello world</description>
</update_customerbankaccount>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | integer | Record number of customer bank account |
| accountholder | Optional | string | Account holder |
| description | Optional | string | Description |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |
| mailaddress | Optional | object | Mail address |
| defaultaccount | Optional | boolean | Default bank account. Use `false` for No, `true` for Yes. |

`mailaddress`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| address1 | Optional | string | Address line 1 |
| address2 | Optional | string | Address line 2 |
| address3 | Optional | string | Address line 3 |
| city | Optional | string | City |
| state | Optional | string | State/province |
| zip | Optional | string | Zip/postal code |
| country | Optional | string | Country |
| isocountrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `isocountrycode` must be provided. |

* * *

Delete Customer Bank Account (Legacy)
-------------------------------------

#### `delete_customerbankaccount`

```
<delete_customerbankaccount recordno="123" />
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | integer | Record number of customer bank account |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

