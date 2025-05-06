Title: Checking Accounts

URL Source: https://developer.intacct.com/api/cash-management/checking-accounts/

Markdown Content:
*   [Checking Accounts](https://developer.intacct.com/api/cash-management/checking-accounts/#checking-accounts)
    *   [Get Checking Account Object Definition](https://developer.intacct.com/api/cash-management/checking-accounts/#get-checking-account-object-definition)
    *   [Query and List Checking Accounts](https://developer.intacct.com/api/cash-management/checking-accounts/#query-and-list-checking-accounts)
    *   [Query and List Checking Accounts (Legacy)](https://developer.intacct.com/api/cash-management/checking-accounts/#query-and-list-checking-accounts-legacy)
    *   [Get Checking Account](https://developer.intacct.com/api/cash-management/checking-accounts/#get-checking-account)
    *   [Get Checking Account by ID](https://developer.intacct.com/api/cash-management/checking-accounts/#get-checking-account-by-id)
*   [Checking Account Reconciliations](https://developer.intacct.com/api/cash-management/checking-accounts/#checking-account-reconciliations)
    *   [Get Checking Account Reconciliation Object Definition](https://developer.intacct.com/api/cash-management/checking-accounts/#get-checking-account-reconciliation-object-definition)
    *   [Query and List Checking Account Reconciliations](https://developer.intacct.com/api/cash-management/checking-accounts/#query-and-list-checking-account-reconciliations)
    *   [Query and List Checking Account Reconciliations (Legacy)](https://developer.intacct.com/api/cash-management/checking-accounts/#query-and-list-checking-account-reconciliations-legacy)
    *   [Get Checking Account Reconciliation](https://developer.intacct.com/api/cash-management/checking-accounts/#get-checking-account-reconciliation)
    *   [Create Checking Account Reconciliation](https://developer.intacct.com/api/cash-management/checking-accounts/#create-checking-account-reconciliation)
    *   [Reconcile Checking Account (Legacy)](https://developer.intacct.com/api/cash-management/checking-accounts/#reconcile-checking-account-legacy)
    *   [Delete Checking Account Reconciliation](https://developer.intacct.com/api/cash-management/checking-accounts/#delete-checking-account-reconciliation)

* * *

Provides the relevant information for a checking account and supports checking account reconciliation.

You can reconcile checking accounts using online bank feeds or bank feeds that you create using XML records.

* * *

### Get Checking Account Object Definition

#### `lookup`

> List all the fields and relationships for the checking account object:

```
<lookup>
    <object>CHECKINGACCOUNT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHECKINGACCOUNT` |

* * *

### Query and List Checking Accounts

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each checking account:

```
<query>
    <object>CHECKINGACCOUNT</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHECKINGACCOUNT` |
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

### Query and List Checking Accounts (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CHECKINGACCOUNT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHECKINGACCOUNT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Checking Account

#### `read`

```
<read>
    <object>CHECKINGACCOUNT</object>
    <keys>91</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHECKINGACCOUNT` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Checking Account by ID

#### `readByName`

```
<readByName>
    <object>CHECKINGACCOUNT</object>
    <keys>BOFA-1234</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHECKINGACCOUNT` |
| keys | Required | string | Comma-separated list of account `BANKACCOUNTID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Checking Account Reconciliations
--------------------------------

### Get Checking Account Reconciliation Object Definition

#### `lookup`

> List all the fields and relationships for the checking account reconciliation object:

```
<lookup>
    <object>BANKACCTRECON</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTRECON` |

* * *

### Query and List Checking Account Reconciliations

#### [`query`](https://developer.intacct.com/web-services/queries/)

> To list checking account reconciliations, provide a checking account for the FINANCIALENTITY in the filter:

```
<query>
    <object>BANKACCTRECON</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
        <field>FINANCIALENTITY</field>
    </select>
    <filter>
        <equalto>
            <field>STATE</field>
            <value>initiated</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTRECON` |
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

### Query and List Checking Account Reconciliations (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>BANKACCTRECON</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTRECON` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Checking Account Reconciliation

#### `read`

```
<read>
    <object>BANKACCTRECON</object>
    <keys>51</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTRECON` |
| keys | Required | string | Comma-separated list of record number of the `BANKACCTRECON` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Checking Account Reconciliation

You reconcile a checking account against transaction records from a [bank feed](https://developer.intacct.com/api/cash-management/bank-feeds/) that you previously created.

You can reconcile the account by having the system attempt to match and clear all the transactions (`Automatch` mode), or you can review the system’s proposed matches in the UI and reconcile the account from there (`AutomatchReview` mode).

More information about [bank reconciliation](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Bank_rec_overview) is available in the Sage Intacct product help.

#### `create`

> Attempt to match and clear (or reconcile) all the transactions in the given period:

```
<create>
    <BANKACCTRECON>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <STMTENDINGDATE>04/01/2020</STMTENDINGDATE>
        <CUTOFFDATE>01/01/2020</CUTOFFDATE>
        <STMTENDINGBALANCE>1842</STMTENDINGBALANCE>
        <MODE>Automatch</MODE>
    </BANKACCTRECON>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BANKACCTRECON | Required | object | Object to create |

`BANKACCTRECON`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FINANCIALENTITY | Required | string | Checking account ID |
| STMTENDINGDATE | Required | date | Statement ending date |
| CUTOFFDATE | Optional | date | Cut-off date for the reconciliation, which is the date from which you want to reconcile transactions. Required only for the first reconciliation. This date can be the day before you transitioned to Sage Intacct, or another date if you don’t want to go all the way back to when you first started using Sage Intacct. (Typically, it’s the day before the statement start date.) |
| STMTENDINGBALANCE | Required | currency | Statement ending balance |
| MODE | Required | string | Reconciliation mode. Use `Automatch` to attempt to clear all the transactions or `AutomatchReview` if you want to view/complete the open reconciliation in the UI. |
| FEEDTYPE | Optional | string | Bank transaction feed type. Use `xml` for a bank feed created with XML records, or `onl` for an online bank feed from Sage Cloud Services (Default: `xml`). |
| SUPDOCKEY | Optional | string | Attachment record number |

* * *

### Reconcile Checking Account (Legacy)

This legacy function does not support online bank feeds and is not available in the UI. Consider using the new [reconciliation function](https://developer.intacct.com/api/cash-management/checking-accounts/#create-checking-account-reconciliation) instead.

#### `reconcile_bank`

```
<reconcile_bank>
    <bankaccountid>BOFACHECK-0827</bankaccountid>
    <cutoffdate>
        <year>2013</year>
        <month>06</month>
        <day>30</day>
    </cutoffdate>
    <statementendingdate>
        <year>2013</year>
        <month>07</month>
        <day>31</day>
    </statementendingdate>
    <reconmode>AutomatchReview</reconmode>
    <statementendingbalance>1000</statementendingbalance>
    <banktxns>
        <banktxn>
            <postingdate>
                <year>2013</year>
                <month>07</month>
                <day>15</day>
            </postingdate>
            <txntype></txntype>
            <doctype></doctype>
            <document>1234</document>
            <payee>Payee</payee>
            <amount>10.99</amount>
            <description>description</description>
        </banktxn>
    </banktxns>
</reconcile_bank>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bankaccountid | Required | string | Account `BANKACCOUNTID` to reconcile |
| cutoffdate | Optional | object | Beginning balance cut off date |
| statementendingdate | Required | object | Statement ending date |
| reconmode | Required | string | Reconciliation mode. Use `Automatch` or `AutomatchReview`. Default depends on mode set on checking account. If Automatch, then the entire reconciliation must clear otherwise you will get an error. Recommended to use Automatch with review. When user reviewing in UI, they must check the “Use previous uploaded file” to see this. |
| statementendingbalance | Required | currency | Statement ending balance |
| banktxns | Required | `banktxn[1...n]` | Bank statement transactions to reconcile with |

`cutoffdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`banktxn`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| postingdate | Required | object | Posting date |
| txntype | Required | string | Transaction type. Use `withdrawal` or `deposit`. If blank, the system will determine this based on the Amount being positive or negative. |
| doctype | Required | string | Document type. Use `check`, `card`, `ach`, or leave blank. |
| document | Required | string | Document number, like the check number or electronic transaction ID. |
| payee | Required | string(80) | Name of payee |
| amount | Required | currency | Amount. Must be non-zero. |
| description | Optional | string(80) | Memo |

`postingdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

### Delete Checking Account Reconciliation

You can delete a checking account reconciliation object that is in `initiated` or `draft` state.

```
<delete>
    <object>BANKACCTRECON</object>
    <keys>41</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTRECON` |
| keys | Required | string | Comma-separated list of record number of the checking account reconciliation object |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

