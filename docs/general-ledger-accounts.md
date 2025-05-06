Title: Accounts

URL Source: https://developer.intacct.com/api/general-ledger/accounts/

Markdown Content:
*   [Accounts](https://developer.intacct.com/api/general-ledger/accounts/#accounts)
    *   [Get Account Object Definition](https://developer.intacct.com/api/general-ledger/accounts/#get-account-object-definition)
    *   [Query and List Accounts](https://developer.intacct.com/api/general-ledger/accounts/#query-and-list-accounts)
    *   [Query and List Accounts (Legacy)](https://developer.intacct.com/api/general-ledger/accounts/#query-and-list-accounts-legacy)
    *   [Get Account](https://developer.intacct.com/api/general-ledger/accounts/#get-account)
    *   [Get Account by ID](https://developer.intacct.com/api/general-ledger/accounts/#get-account-by-id)
    *   [Create Account](https://developer.intacct.com/api/general-ledger/accounts/#create-account)
    *   [Create Account (Legacy)](https://developer.intacct.com/api/general-ledger/accounts/#create-account-legacy)
    *   [Update Account](https://developer.intacct.com/api/general-ledger/accounts/#update-account)
    *   [Update Account (Legacy)](https://developer.intacct.com/api/general-ledger/accounts/#update-account-legacy)
    *   [Delete Account](https://developer.intacct.com/api/general-ledger/accounts/#delete-account)
    *   [Delete Account (Legacy)](https://developer.intacct.com/api/general-ledger/accounts/#delete-account-legacy)
*   [Entity Level Account Titles](https://developer.intacct.com/api/general-ledger/accounts/#entity-level-account-titles)
    *   [Get Entity Level Account Title Object Definition](https://developer.intacct.com/api/general-ledger/accounts/#get-entity-level-account-title-object-definition)
    *   [Query and List Entity Level Account Titles](https://developer.intacct.com/api/general-ledger/accounts/#query-and-list-entity-level-account-titles)
    *   [Query and List Entity Level Account Titles (Legacy)](https://developer.intacct.com/api/general-ledger/accounts/#query-and-list-entity-level-account-titles-legacy)
    *   [Get Entity Level Account Title](https://developer.intacct.com/api/general-ledger/accounts/#get-entity-level-account-title)

* * *

The chart of accounts is the base for users tracking financial data.

* * *

### Get Account Object Definition

#### `lookup`

> List all the fields and relationships for the account object:

```
<lookup>
    <object>GLACCOUNT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNT` |

* * *

### Query and List Accounts

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, account number, and account type for each income account:

```
<query>
    <object>GLACCOUNT</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCOUNTNO</field>
        <field>ACCOUNTTYPE</field>
    </select>
    <filter>
        <equalto>
            <field>ACCOUNTTYPE</field>
            <value>incomestatement</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNT` |
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

### Query and List Accounts (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>GLACCOUNT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTTYPE | Optional | string | Account type. Use `I` for `incomestatement` or `N` for `balancesheet`. |

* * *

### Get Account

#### `read`

```
<read>
    <object>GLACCOUNT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNT` |
| keys | Required | string | Comma-separated list of account `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Account by ID

#### `readByName`

```
<readByName>
    <object>GLACCOUNT</object>
    <keys>6700</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNT` |
| keys | Required | string | Comma-separated list of account `ACCOUNTNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Account

#### `create`

```
<create>
    <GLACCOUNT>
        <ACCOUNTNO>6700</ACCOUNTNO>
        <TITLE>Payroll Expense</TITLE>
    </GLACCOUNT>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCOUNT | Required | object | Object to create |

`GLACCOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTNO | Required | string | Account number |
| TITLE | Required | string | Title |
| CATEGORY | Optional | string | System Category |
| ACCOUNTTYPE | Optional | string | Account type. Use `balancesheet` for a Balance Sheet Account otherwise use `incomestatement` for an Income Statement Account. (Default: `balancesheet`) |
| NORMALBALANCE | Required | string | Normal balance of account. Use `debit` for Debit otherwise use `credit` for Credit. (Default: `debit`) |
| CLOSINGTYPE | Required | string | Period end closing type. Use `non-closing account` for Non-Closing Account otherwise use `closing account` for Closing Account. (Default: `non-closing account`) |
| CLOSINGACCOUNTNO | Optional | string | Close into account number. Required if `CLOSINGTYPE` is set to `closing account`. |
| ALTERNATIVEACCOUNT | Optional | string | GL account alternative. Use `None` for None, `Payables account` for Payables Account, or `Receivables account` for Receivables Account. (Default: `None`) |
| STATUS | Optional | string | Account status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| REQUIREDEPT | Optional | boolean | Use `true` to make department required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRELOC | Optional | boolean | Use `true` to make location required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREPROJECT | Optional | boolean | Use `true` to make project required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRETASK | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECUSTOMER | Optional | boolean | Use `true` to make customer required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREVENDOR | Optional | boolean | Use `true` to make vendor required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREEMPLOYEE | Optional | boolean | Use `true` to make employee required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREITEM | Optional | boolean | Use `true` to make item required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECLASS | Optional | boolean | Use `true` to make class required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECONTRACT | Optional | boolean | Use `true` to make contract required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREWAREHOUSE | Optional | boolean | Use `true` to make warehouse required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREGLDIM\* | Optional | boolean | Use `true` to make user defined dimension required for this account, otherwise use `false`. UDD object integration name usually appended to `REQUIREGLDIM`. (Default: `false`) |

* * *

### Create Account (Legacy)

#### `create_glaccount`

```
<create_glaccount>
    <glaccountno>6700</glaccountno>
    <title>Payroll Expense</title>
</create_glaccount>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Account number |
| title | Required | string | Title |
| normalbalance | required | string | Normal balance of account. Use `debit` for Debit otherwise use `credit` for Credit. (Default: `debit`). |
| accounttype | Optional | string | Account type. Use `balancesheet` for a Balance Sheet Account otherwise use `incomestatement` for an Income Statement Account. (Default: `balancesheet`) |
| closingtype | Required | string | Period end closing type. Use `non-closing account` for Non-Closing Account otherwise use `closing account` for Closing Account. (Default: `non-closing account`) |
| closingaccountno | Optional | string | Close into account number. Required if `CLOSINGTYPE` is set to `closing account`. |
| status | Optional | string | Account status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| requiredept | Optional | boolean | Use `true` to make department required for this account, otherwise use `false`. (Default: `false`) |
| requireloc | Optional | boolean | Use `true` to make location required for this account, otherwise use `false`. (Default: `false`) |
| requireproject | Optional | boolean | Use `true` to make project required for this account, otherwise use `false`. (Default: `false`) |
| requiretask | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| requirecustomer | Optional | boolean | Use `true` to make customer required for this account, otherwise use `false`. (Default: `false`) |
| requirevendor | Optional | boolean | Use `true` to make vendor required for this account, otherwise use `false`. (Default: `false`) |
| requireitem | Optional | boolean | Use `true` to make item required for this account, otherwise use `false`. (Default: `false`) |
| requireemployee | Optional | boolean | Use `true` to make employee required for this account, otherwise use `false`. (Default: `false`) |
| requireclass | Optional | boolean | Use `true` to make class required for this account, otherwise use `false`. (Default: `false`) |
| requirecontract | Optional | boolean | Use `true` to make contract required for this account, otherwise use `false`. (Default: `false`) |
| requirewarehouse | Optional | boolean | Use `true` to make warehouse required for this account, otherwise use `false`. (Default: `false`) |
| customfields | Optional | array of `customfield` | Custom fields |
| category | Optional | string | System Category |
| alternativeaccount | Optional | string | GL account alternative. Use `None` for None, `Payables account` for Payables Account, or `Receivables account` for Receivables Account. (Default: `None`) |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Account

#### `update`

```
<update>
    <GLACCOUNT>
        <RECORDNO>141</RECORDNO>
        <TITLE>Payroll Expenses</TITLE>
    </GLACCOUNT>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCOUNT | Required | object | Object to update |

`GLACCOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of account to update. Required if not using `ACCOUNTNO`. |
| ACCOUNTNO | Optional | string | Account number. Required if not using `RECORDNO`. |
| TITLE | Optional | string | Title |
| CATEGORY | Optional | string | System Category |
| ACCOUNTTYPE | Optional | string | Account type. Use `balancesheet` for a Balance Sheet Account otherwise use `incomestatement` for an Income Statement Account. (Default: `balancesheet`) |
| NORMALBALANCE | required | string | Normal balance of account. Use `debit` for Debit otherwise use `credit` for Credit. (Default: `debit`) |
| CLOSINGTYPE | Required | string | Period end closing type. Use `non-closing account` for Non-Closing Account otherwise use `closing account` for Closing Account. (Default: `non-closing account`) |
| CLOSINGACCOUNTNO | Optional | string | Close into account number. Required if `CLOSINGTYPE` is set to `closing account`. |
| ALTERNATIVEACCOUNT | Optional | string | GL account alternative. Use `None` for None, `Payables account` for Payables Account, or `Receivables account` for Receivables Account. (Default: `None`) |
| STATUS | Optional | string | Account status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| REQUIREDEPT | Optional | boolean | Use `true` to make department required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRELOC | Optional | boolean | Use `true` to make location required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREPROJECT | Optional | boolean | Use `true` to make project required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRETASK | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECUSTOMER | Optional | boolean | Use `true` to make customer required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREVENDOR | Optional | boolean | Use `true` to make vendor required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREEMPLOYEE | Optional | boolean | Use `true` to make employee required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREITEM | Optional | boolean | Use `true` to make item required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECLASS | Optional | boolean | Use `true` to make class required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECONTRACT | Optional | boolean | Use `true` to make contract required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREWAREHOUSE | Optional | boolean | Use `true` to make warehouse required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREGLDIM\* | Optional | boolean | Use `true` to make user defined dimension required for this account, otherwise use `false`. UDD object integration name usually appended to `REQUIREGLDIM`. (Default: `false`) |

* * *

### Update Account (Legacy)

#### `update_glaccount`

```
<update_glaccount glaccountno="6700">
    <title>Payroll Expenses</title>
</update_glaccount>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Account number to update |
| title | Optional | string | Title |
| normalbalance | required | string | Normal balance of account. Use `debit` for Debit otherwise use `credit` for Credit. |
| accounttype | Optional | string | Account type. Use `balancesheet` for a Balance Sheet Account otherwise use `incomestatement` for an Income Statement Account. |
| closingtype | Required | string | Period end closing type. Use `non-closing account` for Non-Closing Account otherwise use `closing account` for Closing Account. |
| closingaccountno | Optional | string | Close into account number. Required if `CLOSINGTYPE` is set to `closing account`. |
| status | Optional | string | Account status. Use `active` for Active otherwise use `inactive` for Inactive. |
| requiredept | Optional | boolean | Use `true` to make department required for this account, otherwise use `false`. |
| requireloc | Optional | boolean | Use `true` to make location required for this account, otherwise use `false`. |
| requireproject | Optional | boolean | Use `true` to make project required for this account, otherwise use `false`. |
| requiretask | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| requirecustomer | Optional | boolean | Use `true` to make customer required for this account, otherwise use `false`. |
| requirevendor | Optional | boolean | Use `true` to make vendor required for this account, otherwise use `false`. |
| requireitem | Optional | boolean | Use `true` to make item required for this account, otherwise use `false`. |
| requireemployee | Optional | boolean | Use `true` to make employee required for this account, otherwise use `false`. |
| requireclass | Optional | boolean | Use `true` to make class required for this account, otherwise use `false`. |
| requirecontract | Optional | boolean | Use `true` to make contract required for this account, otherwise use `false`. |
| requirewarehouse | Optional | boolean | Use `true` to make warehouse required for this account, otherwise use `false`. |
| category | Optional | string | System Category |
| alternativeaccount | Optional | string | GL account alternative. Use `None` for None, `Payables account` for Payables Account, or `Receivables account` for Receivables Account. |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Account

#### `delete`

```
<delete>
    <object>GLACCOUNT</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNT` |
| keys | Required | string | Comma-separated list of account `RECORDNO` to delete |

* * *

### Delete Account (Legacy)

#### `delete_glaccount`

```
<delete_glaccount glaccountno="6700"></delete_glaccount>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Account number to delete |

* * *

Entity Level Account Titles
---------------------------

### Get Entity Level Account Title Object Definition

#### `lookup`

> List all the fields and relationships for the entity level account title object:

```
<lookup>
    <object>ACCTTITLEBYLOC</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCTTITLEBYLOC` |

* * *

### Query and List Entity Level Account Titles

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, account number, and location ID for each entity level account title:

```
<query>
    <object>ACCTTITLEBYLOC</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCOUNTNO</field>
        <field>LOCATIONID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCTTITLEBYLOC` |
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

### Query and List Entity Level Account Titles (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ACCTTITLEBYLOC</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCTTITLEBYLOC` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Entity Level Account Title

#### `read`

```
<read>
    <object>ACCTTITLEBYLOC</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCTTITLEBYLOC` |
| keys | Required | string | Comma-separated list of title `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

