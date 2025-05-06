Title: Expense Reports

URL Source: https://developer.intacct.com/api/employee-expenses/expense-reports/

Markdown Content:
*   [Get Expense Report Object Definition](https://developer.intacct.com/api/employee-expenses/expense-reports/#get-expense-report-object-definition)
*   [Query and List Expense Reports](https://developer.intacct.com/api/employee-expenses/expense-reports/#query-and-list-expense-reports)
*   [Query and List Expense Reports (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-reports/#query-and-list-expense-reports-legacy)
*   [Get Expense Report](https://developer.intacct.com/api/employee-expenses/expense-reports/#get-expense-report)
*   [Create Expense Report (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-reports/#create-expense-report-legacy)
*   [Update Expense Report (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-reports/#update-expense-report-legacy)
*   [Reverse Expense Report (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-reports/#reverse-expense-report-legacy)
*   [Delete Expense Report](https://developer.intacct.com/api/employee-expenses/expense-reports/#delete-expense-report)
*   [Delete Expense Report (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-reports/#delete-expense-report-legacy)

* * *

Expense report for an employee.

* * *

Get Expense Report Object Definition
------------------------------------

#### `lookup`

> List all the fields and relationships for the expense report object:

```
<lookup>
    <object>EEXPENSES</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEXPENSES` |

* * *

Query and List Expense Reports
------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and state for each expense report that is approved:

```
<query>
    <object>EEXPENSES</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
    <filter>
        <equalto>
            <field>STATE</field>
            <value>Approved</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEXPENSES` |
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

Query and List Expense Reports (Legacy)
---------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>EEXPENSES</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEXPENSES` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Expense Report
------------------

#### `read`

```
<read>
    <object>EEXPENSES</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEXPENSES` |
| keys | Required | string | Comma-separated list of expense report `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Expense Report (Legacy)
------------------------------

[History](https://developer.intacct.com/api/employee-expenses/expense-reports/#history-create-expense-report-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added inclusivetax, taxsolutionid, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `create_expensereport`

```
<create_expensereport>
    <employeeid>E0008</employeeid>
    <datecreated>
        <year>2016</year>
        <month>09</month>
        <day>09</day>
    </datecreated>
    <state>Submitted</state>
    <description>Travel to client</description>
    <expenses>
        <expense>
            <expensetype>Travel-Hotel</expensetype>
            <amount>50</amount>
            <expensedate>
                <year>2015</year>
                <month>09</month>
                <day>01</day>
            </expensedate>
            <memo>Marriott</memo>
            <paidfor>Hotel</paidfor>
            <locationid>ARL-VA-US</locationid>
            <departmentid>PRS</departmentid>
            <projectid>P0004</projectid>
            <employeeid>E0008</employeeid>
            <billable>true</billable>
        </expense>
    </expenses>
</create_expensereport>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| employeeid | Required | string | Employee ID |
| datecreated | Required | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| batchkey | Optional | integer | Summary `RECORDNO` |
| expensereportno | Optional | string | Expense report number |
| state | Optional | string | Action. Use `Draft` or `Submitted`. (Default: `Submitted`) |
| description | Optional | string | Reason for expense |
| memo | Optional | string | Memo |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Reimbursement currency code |
| customfields | Optional | array of `customfield` | Custom fields |
| expenses | Required | `expense[1...n]` | Expense report lines, must have at least 1. |
| supdocid | Optional | string | Attachments ID |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the expense report line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the expense report line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. See [Tax Solutions](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/) for more information. (GB, AU, and ZA only) |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`dateposted`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`expense`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expensetype | Optional | string | Expense type. Required if not using `glaccountno`. |
| glaccountno | Optional | string | GL account number. Required if not using `expensetype`. |
| amount | Required | currency | Reimbursement amount |
| currency | Optional | string | Transaction currency code |
| trx\_amount | Optional | currency | Transaction amount |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| expensedate | Optional | object | Expense date |
| memo | Optional | string | Paid to |
| form1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Employee must be set up for 1099s. |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| paidfor | Optional | string | Paid for |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. (Default: `false`) |
| exppmttype | Optional | string | Expense payment type |
| quantity | Optional | number | Quantity |
| rate | Optional | number | Unit rate |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`expensedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the expense report line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

Update Expense Report (Legacy)
------------------------------

[History](https://developer.intacct.com/api/employee-expenses/expense-reports/#history-update-expense-report-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added inclusivetax, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `update_expensereport`

```
<update_expensereport key="1234">
    <description>Test update</description>
    <updateexpenses>
        <updateexpense line_num="1">
            <expensetype>General Travel</expensetype>
        </updateexpense>
    </updateexpenses>
</update_expensereport>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Expense report `RECORDNO` to update |
| employeeid | Optional | string | Employee ID |
| datecreated | Optional | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| expensereportno | Optional | string | Expense report number |
| state | Optional | string | Action. Use `Draft` or `Submitted`. (Default: `Submitted`) |
| description | Optional | string | Reason for expense |
| memo | Optional | string | Memo |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Reimbursement currency code |
| customfields | Optional | array of `customfield` | Custom fields |
| updateexpenses | Optional | `(updateexpense | expense)[0...n]` | Expense report lines. To update an existing line use `updateexpense` otherwise to create a new line use `expense`. You can mix types in the array. |
| supdocid | Optional | string | Attachments ID |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the expense report line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the expense report line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`dateposted`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`expense`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expensetype | Optional | string | Expense type. Required if not using `glaccountno`. |
| glaccountno | Optional | string | GL account number. Required if not using `expensetype`. |
| amount | Required | currency | Reimbursement amount |
| currency | Optional | string | Transaction currency code |
| trx\_amount | Optional | currency | Transaction amount |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| expensedate | Optional | object | Expense date |
| memo | Optional | string | Paid to |
| form1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Employee must be set up for 1099s. |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| paidfor | Optional | string | Paid for |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. (Default: `false`) |
| exppmttype | Optional | string | Expense payment type |
| quantity | Optional | number | Quantity |
| rate | Optional | number | Unit rate |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`updateexpense`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| expensetype | Optional | string | Expense type. Can use this or `glaccountno` but not both. |
| glaccountno | Optional | string | GL account number. Can use this or `expensetype` but not both. |
| amount | Optional | currency | Reimbursement amount |
| currency | Optional | string | Transaction currency code |
| trx\_amount | Optional | currency | Transaction amount |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| expensedate | Optional | object | Expense date |
| memo | Optional | string | Paid to |
| form1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Employee must be set up for 1099s. |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| paidfor | Optional | string | Paid for |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. (Default: `false`) |
| exppmttype | Optional | string | Expense payment type |
| quantity | Optional | number | Quantity |
| rate | Optional | number | Unit rate |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`expensedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the expense report line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

Reverse Expense Report (Legacy)
-------------------------------

#### `reverse_expensereport`

```
<reverse_expensereport key="1234">
    <datereversed>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </datereversed>
</reverse_expensereport>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Expense report `RECORDNO` to reverse |
| datereversed | Required | object | Reverse date |
| description | Optional | string | Memo |

`datereversed`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Delete Expense Report
---------------------

#### `delete`

```
<delete>
    <object>EEXPENSES</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEXPENSES` |
| keys | Required | string | Comma-separated list of bill `RECORDNO` to delete |

* * *

Delete Expense Report (Legacy)
------------------------------

#### `delete_expensereport`

```
<delete_expensereport key="1234"></delete_expensereport>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Expense report `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

