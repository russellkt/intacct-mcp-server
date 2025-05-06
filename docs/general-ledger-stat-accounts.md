Title: Statistical Accounts

URL Source: https://developer.intacct.com/api/general-ledger/stat-accounts/

Markdown Content:
*   [Get Statistical Account Object Definition](https://developer.intacct.com/api/general-ledger/stat-accounts/#get-statistical-account-object-definition)
*   [Query and List Statistical Accounts](https://developer.intacct.com/api/general-ledger/stat-accounts/#query-and-list-statistical-accounts)
*   [Query and List Statistical Accounts (Legacy)](https://developer.intacct.com/api/general-ledger/stat-accounts/#query-and-list-statistical-accounts-legacy)
*   [Get Statistical Account](https://developer.intacct.com/api/general-ledger/stat-accounts/#get-statistical-account)
*   [Get Statistical Account by ID](https://developer.intacct.com/api/general-ledger/stat-accounts/#get-statistical-account-by-id)
*   [Create Statistical Account](https://developer.intacct.com/api/general-ledger/stat-accounts/#create-statistical-account)
*   [Create Statistical Account (Legacy)](https://developer.intacct.com/api/general-ledger/stat-accounts/#create-statistical-account-legacy)
*   [Update Statistical Account](https://developer.intacct.com/api/general-ledger/stat-accounts/#update-statistical-account)
*   [Update Statistical Account (Legacy)](https://developer.intacct.com/api/general-ledger/stat-accounts/#update-statistical-account-legacy)
*   [Delete Statistical Account](https://developer.intacct.com/api/general-ledger/stat-accounts/#delete-statistical-account)
*   [Delete Statistical Account (Legacy)](https://developer.intacct.com/api/general-ledger/stat-accounts/#delete-statistical-account-legacy)

* * *

Statistical accounts are used for tracking non-financial data.

* * *

Get Statistical Account Object Definition
-----------------------------------------

#### `lookup`

> List all the fields and relationships for the statistical account object:

```
<lookup>
    <object>STATACCOUNT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STATACCOUNT` |

* * *

Query and List Statistical Accounts
-----------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, account number, and title for each statistical account:

```
<query>
    <object>STATACCOUNT</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCOUNTNO</field>
        <field>TITLE</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STATACCOUNT` |
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

Query and List Statistical Accounts (Legacy)
--------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>STATACCOUNT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STATACCOUNT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Statistical Account
-----------------------

#### `read`

```
<read>
    <object>STATACCOUNT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STATACCOUNT` |
| keys | Required | string | Comma-separated list of account `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Statistical Account by ID
-----------------------------

#### `readByName`

```
<readByName>
    <object>STATACCOUNT</object>
    <keys>9000</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STATACCOUNT` |
| keys | Required | string | Comma-separated list of account `ACCOUNTNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Statistical Account
--------------------------

#### `create`

```
<create>
    <STATACCOUNT>
        <ACCOUNTNO>9000</ACCOUNTNO>
        <TITLE>Headcount</TITLE>
    </STATACCOUNT>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATACCOUNT | Required | object | Object to create |

`STATACCOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTNO | Required | string | Statistical Account number |
| TITLE | Required | string | Title |
| CATEGORY | Optional | string | System Category |
| ACCOUNTTYPE | Optional | string | Non-functional |
| STATUS | Optional | string | Statistical Account status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| REQUIREDEPT | Optional | boolean | Use `true` to make department required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRELOC | Optional | boolean | Use `true` to make location required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREPROJECT | Optional | boolean | Use `true` to make project required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRETASK | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECUSTOMER | Optional | boolean | Use `true` to make customer required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREVENDOR | Optional | boolean | Use `true` to make vendor required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREEMPLOYEE | Optional | boolean | Use `true` to make employee required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREITEM | Optional | boolean | Use `true` to make item required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECLASS | Optional | boolean | Use `true` to make class required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRETASK | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREGLDIM\* | Optional | boolean | Use `true` to make user defined dimension required for this account, otherwise use `false`. UDD object integration name usually appended to `REQUIREGLDIM`. (Default: `false`) |

* * *

Create Statistical Account (Legacy)
-----------------------------------

#### `create_statglaccount`

```
<create_statglaccount>
    <glaccountno>9000</glaccountno>
    <title>Headcount</title>
</create_statglaccount>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Statistical account number |
| title | Required | string | Title |
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
| status | Optional | string | Account status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Statistical Account
--------------------------

#### `update`

```
<update>
    <STATACCOUNT>
        <RECORDNO>141</RECORDNO>
        <TITLE>Employee Headcount</TITLE>
    </STATACCOUNT>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATACCOUNT | Required | object | Object to update |

`STATACCOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of account to update. Required if not using `ACCOUNTNO`. |
| ACCOUNTNO | Optional | string | Account number. Required if not using `RECORDNO`. |
| TITLE | Required | string | Title |
| CATEGORY | Optional | string | System Category |
| ACCOUNTTYPE | Optional | string | Non-functional |
| STATUS | Optional | string | Statistical Account status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| REQUIREDEPT | Optional | boolean | Use `true` to make department required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRELOC | Optional | boolean | Use `true` to make location required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREPROJECT | Optional | boolean | Use `true` to make project required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRETASK | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECUSTOMER | Optional | boolean | Use `true` to make customer required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREVENDOR | Optional | boolean | Use `true` to make vendor required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREEMPLOYEE | Optional | boolean | Use `true` to make employee required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREITEM | Optional | boolean | Use `true` to make item required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRECLASS | Optional | boolean | Use `true` to make class required for this account, otherwise use `false`. (Default: `false`) |
| REQUIRETASK | Optional | boolean | Use `true` to make task required for this account, otherwise use `false`. (Default: `false`) |
| REQUIREGLDIM\* | Optional | boolean | Use `true` to make user defined dimension required for this account, otherwise use `false`. UDD object integration name usually appended to `REQUIREGLDIM`. (Default: `false`) |

* * *

Update Statistical Account (Legacy)
-----------------------------------

#### `update_statglaccount`

```
<update_statglaccount glaccountno="9000">
    <title>Employee Headcount</title>
</update_statglaccount>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Statistical account number to update |
| title | Optional | string | Title |
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
| status | Optional | string | Account status. Use `active` for Active otherwise use `inactive` for Inactive. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Statistical Account
--------------------------

#### `delete`

```
<delete>
    <object>STATACCOUNT</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STATACCOUNT` |
| keys | Required | string | Comma-separated list of account `RECORDNO` to delete |

* * *

Delete Statistical Account (Legacy)
-----------------------------------

#### `delete_statglaccount`

```
<delete_statglaccount glaccountno="9000"></delete_statglaccount>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Account number to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

