Title: Contract Expenses

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/

Markdown Content:
*   [Get Contract Expense Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#get-contract-expense-object-definition)
*   [Query and List Contract Expenses](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#query-and-list-contract-expenses)
*   [Query and List Contract Expenses (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#query-and-list-contract-expenses-legacy)
*   [Get Contract Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#get-contract-expense)
*   [Create Contract Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#create-contract-expense)
*   [Update Contract Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#update-contract-expense)
*   [Hold Contract Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#hold-contract-expense)
*   [Resume Contract Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#resume-contract-expense)
*   [Delete Contract Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expenses/#delete-contract-expense)

* * *

A contract expense is the cost incurred to obtain or fulfill a contract with a customer.

* * *

Get Contract Expense Object Definition
--------------------------------------

#### `lookup`

> List all the fields and relationships for the contract expense object:

```
<lookup>
    <object>CONTRACTEXPENSE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |

* * *

Query and List Contract Expenses
--------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and associated contract ID for each contract expense:

```
<query>
    <object>CONTRACTEXPENSE</object>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |
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

Query and List Contract Expenses (Legacy)
-----------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTEXPENSE</object>
    <fields>*</fields>
    <query>TYPE = 'C'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TYPE | Required | string | Type. Use `C` for Contract expenses. |
| STATE | Optional | string | State. Use `P` for In progress, `C` for Cancelled |

* * *

Get Contract Expense
--------------------

#### `read`

```
<read>
    <object>CONTRACTEXPENSE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |
| keys | Required | string | Comma-separated list of contract expense `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Contract Expense
-----------------------

#### `create`

```
<create>
    <CONTRACTEXPENSE>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <ITEMID>SUPP</ITEMID>
        <POSTINGDATE>05/01/2017</POSTINGDATE>
        <AMOUNT>400.00</AMOUNT>
        <LOCATIONID>US</LOCATIONID>
        <TEMPLATENAME>SL Man (Exp)</TEMPLATENAME>
    </CONTRACTEXPENSE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE | Required | object | Object to create |

`CONTRACTEXPENSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Required | string | Contract ID |
| ITEMID | Required | string | Item ID |
| POSTINGDATE | Required | string | Posting date in format `mm/dd/yyyy` |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy`. Leave blank to use posting date. |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value. |
| AMOUNT | Required | currency | Amount |
| LOCATIONID | Required | string | Location ID |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CLASSID | Optional | string | Class ID |
| TEMPLATENAME | Optional | string | 606 expense template |
| STARTDATE | Optional | string | 606 expense start date in format `mm/dd/yyyy`. Leave blank to use contract/line start date |
| ENDDATE | Optional | string | 606 expense end date in format `mm/dd/yyyy`. Leave blank to use contract/line end date |
| TEMPLATE2NAME | Optional | string | Legacy expense template |
| START2DATE | Optional | string | Legacy expense start date in format `mm/dd/yyyy`. Leave blank to use contract/line start date |
| END2DATE | Optional | string | Legacy expense end date in format `mm/dd/yyyy`. Leave blank to use contract/line end date |

* * *

Update Contract Expense
-----------------------

#### `update`

```
<update>
    <CONTRACTEXPENSE>
        <RECORDNO>123</RECORDNO>
        <DEPARTMENTID>500</DEPARTMENTID>
    </CONTRACTEXPENSE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE | Required | object | Object to update |

`CONTRACTEXPENSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of contract expense to update. |
| ITEMID | Optional | string | Item ID |
| POSTINGDATE | Optional | string | Posting date in format `mm/dd/yyyy` |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy` |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value. |
| AMOUNT | Optional | currency | Amount |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CLASSID | Optional | string | Class ID |
| TEMPLATENAME | Optional | string | 606 expense template |
| STARTDATE | Optional | string | 606 expense start date in format `mm/dd/yyyy`. Leave blank to use contract/line start date |
| ENDDATE | Optional | string | 606 expense end date in format `mm/dd/yyyy`. Leave blank to use contract/line end date |
| TEMPLATE2NAME | Optional | string | Legacy expense template |
| START2DATE | Optional | string | Legacy expense start date in format `mm/dd/yyyy`. Leave blank to use contract/line start date |
| END2DATE | Optional | string | Legacy expense end date in format `mm/dd/yyyy`. Leave blank to use contract/line end date |

* * *

Hold Contract Expense
---------------------

When you use this function, the state of the contract expense remains in progress, but any [expense schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/) are put on hold.

#### `hold`

```
<hold>
    <CONTRACTEXPENSE>
        <RECORDNO>7</RECORDNO>
        <ASOFDATE>07/31/2017</ASOFDATE>
    </CONTRACTEXPENSE>
</hold>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE | Required | object | Object to hold |

`CONTRACTEXPENSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the contract expense to hold |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |

* * *

Resume Contract Expense
-----------------------

#### `resume`

```
<resume>
    <CONTRACTEXPENSE>
        <RECORDNO>7</RECORDNO>
        <ASOFDATE>07/31/2017</ASOFDATE>
    </CONTRACTEXPENSE>
</resume>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE | Optional | object | Object to resume |

`CONTRACTEXPENSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the contract expense to resume |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |

* * *

Delete Contract Expense
-----------------------

#### `delete`

```
<delete>
    <object>CONTRACTEXPENSE</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |
| keys | Required | string | Comma-separated list of contract expense `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

