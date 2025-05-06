Title: Expense Adjustments

URL Source: https://developer.intacct.com/api/employee-expenses/expense-adjustments/

Markdown Content:
*   [Expense Adjustments](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#expense-adjustments)
    *   [Get Expense Adjustment Object Definition](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#get-expense-adjustment-object-definition)
    *   [Query and List Expense Adjustments](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#query-and-list-expense-adjustments)
    *   [Query and List Expense Adjustments (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#query-and-list-expense-adjustments-legacy)
    *   [Get Expense Adjustment](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#get-expense-adjustment)
    *   [Create Expense Adjustment (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#create-expense-adjustment-legacy)
    *   [Update Expense Adjustment (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#update-expense-adjustment-legacy)
    *   [Delete Expense Adjustment](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#delete-expense-adjustment)
    *   [Delete Expense Adjustment (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#delete-expense-adjustment-legacy)
*   [Expense Adjustment Lines](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#expense-adjustment-lines)
    *   [Get Expense Adjustment Line Object Definition](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#get-expense-adjustment-line-object-definition)
    *   [Query and List Adjustment Lines](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#query-and-list-adjustment-lines)
    *   [Query and List Expense Adjustment Lines (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#query-and-list-expense-adjustment-lines-legacy)
    *   [Get Expense Adjustment Line](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#get-expense-adjustment-line)

* * *

Expense adjustments provide a way to fix the balance for an employee who was overpaid or underpaid for an expense.

* * *

### Get Expense Adjustment Object Definition

#### `lookup`

> List all the fields and relationships for the expense adjustment object:

```
<lookup>
    <object>EXPENSEADJUSTMENTS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTS` |

* * *

### Query and List Expense Adjustments

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, total entered, and employee ID for each expense adjustment:

```
<query>
    <object>EXPENSEADJUSTMENTS</object>
    <select>
        <field>RECORDNO</field>
        <field>TOTALENTERED</field>
        <field>EMPLOYEEID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTS` |
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

### Query and List Expense Adjustments (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EXPENSEADJUSTMENTS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Expense Adjustment

#### `read`

```
<read>
    <object>EXPENSEADJUSTMENTS</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTS` |
| keys | Required | string | Comma-separated list of adjustment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Expense Adjustment (Legacy)

[History](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#history-create-expense-adjustment-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added inclusivetax, taxsolutionid, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `create_expenseadjustmentreport`

```
<create_expenseadjustmentreport>
    <employeeid>E1234</employeeid>
    <datecreated>
        <year>2016</year>
        <month>09</month>
        <day>09</day>
    </datecreated>
    <dateposted>
        <year>2016</year>
        <month>09</month>
        <day>09</day>
    </dateposted>
    <adjustmentno>1234</adjustmentno>
    <docnumber></docnumber>
    <description>Travel to client</description>
    <basecurr>USD</basecurr>
    <currency>USD</currency>
    <expenseadjustments>
        <expenseadjustment>
            <expensetype>Travel</expensetype>
            <amount>50.99</amount>
            <currency>USD</currency>
            <trx_amount>50.99</trx_amount>
            <exchratedate>
                <year>2016</year>
                <month>09</month>
                <day>09</day>
            </exchratedate>
            <exchratetype>Intacct Daily Rate</exchratetype>
            <expensedate>
                <year>2016</year>
                <month>09</month>
                <day>01</day>
            </expensedate>
            <memo>Marriott</memo>
            <locationid>SJC-US</locationid>
            <departmentid></departmentid>
            <projectid></projectid>
            <customerid></customerid>
            <vendorid></vendorid>
            <employeeid>E1234</employeeid>
            <itemid></itemid>
            <classid></classid>
            <billable>true</billable>
            <exppmttype></exppmttype>
            <quantity></quantity>
            <rate></rate>
        </expenseadjustment>
    </expenseadjustments>
    <supdocid></supdocid>
</create_expenseadjustmentreport>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| employeeid | Required | string | Employee ID |
| datecreated | Required | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| batchkey | Optional | integer | Summary `RECORDNO` to post adjustment to |
| adjustmentno | Optional | Expense adjustment number |   |
| docnumber | Optional | Reference expense number |   |
| description | Optional | Description |   |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Reimbursement currency code |
| expenseadjustments | Required | `expenseadjustment[1...n]` | Expense adjustment lines. Must have at least 1. |
| supdocid | Optional | string | Attachments ID |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the expense adjustment line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the expense adjustment line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |
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

`expenseadjustment`

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
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
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
| customfields | Optional | array of `customfield` | Custom fields |
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

Specifies a tax rate (defined in the system) and a manually calculated tax for the expense adjustment line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

### Update Expense Adjustment (Legacy)

[History](https://developer.intacct.com/api/employee-expenses/expense-adjustments/#history-update-expense-adjustment-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added inclusivetax, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `update_expenseadjustmentreport`

```
<update_expenseadjustmentreport key="13">
    <updateexpenseadjustments>
        <updateexpenseadjustment line_num="1">
            <expensetype>Travel</expensetype>
        </updateexpenseadjustment>
    </updateexpenseadjustments>
</update_expenseadjustmentreport>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Adjustment `RECORDNO` to update |
| employeeid | Optional | string | Employee ID |
| datecreated | Optional | object | Transaction date |
| adjustmentno | Optional | Expense adjustment number |   |
| docnumber | Optional | Reference expense number |   |
| description | Optional | Description |   |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Reimbursement currency code |
| updateexpenseadjustments | Required | `(updateexpenseadjustment | expenseadjustment)[1...n]` | To update an existing line use `updateexpenseadjustment` otherwise to create a new line use `expenseadjustment`. You can mix types in the array. |
| supdocid | Optional | string | Attachments ID |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the expense adjustment line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the expense adjustment line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |

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

`expenseadjustment`

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
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
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
| customfields | Optional | array of `customfield` | Custom fields |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`updateexpenseadjustment`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| expensetype | Optional | string | Expense type. Required if not using `glaccountno`. |
| glaccountno | Optional | string | GL account number. Required if not using `expensetype`. |
| amount | Optional | currency | Reimbursement amount |
| currency | Optional | string | Transaction currency code |
| trx\_amount | Optional | currency | Transaction amount |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| expensedate | Optional | object | Expense date |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
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
| customfields | Optional | array of `customfield` | Custom fields |
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

Specifies a tax rate (defined in the system) and a manually calculated tax for the expense adjustment line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

### Delete Expense Adjustment

#### `delete`

```
<delete>
    <object>EXPENSEADJUSTMENTS</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTS` |
| keys | Required | string | Comma-separated list of adjustment `RECORDNO` to delete |

* * *

### Delete Expense Adjustment (Legacy)

#### `delete_expenseadjustmentreport`

```
<delete_expenseadjustmentreport key="1234"></delete_expenseadjustmentreport>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Expense adjustment `RECORDNO` to delete |

* * *

Expense Adjustment Lines
------------------------

### Get Expense Adjustment Line Object Definition

#### `lookup`

> List all the fields and relationships for the expense adjustment line object:

```
<lookup>
    <object>EXPENSEADJUSTMENTSITEM</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTSITEM` |

* * *

### Query and List Adjustment Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, amount, and employee ID for each adjustment line :

```
<query>
    <object>EXPENSEADJUSTMENTSITEM</object>
    <select>
        <field>RECORDNO</field>
        <field>AMOUNT</field>
        <field>EMPLOYEEID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTSITEM` |
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

### Query and List Expense Adjustment Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EXPENSEADJUSTMENTSITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTSITEM` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Expense Adjustment Line

#### `read`

```
<read>
    <object>EXPENSEADJUSTMENTSITEM</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEADJUSTMENTSITEM` |
| keys | Required | string | Comma-separated list of adjustment line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

