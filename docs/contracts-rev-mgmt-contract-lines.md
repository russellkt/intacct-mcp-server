Title: Contract Lines

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/

Markdown Content:
*   [Contract Lines](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#contract-lines)
    *   [Get Contract Line Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#get-contract-line-object-definition)
    *   [Query and List Contract Lines](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#query-and-list-contract-lines)
    *   [Query and List Contract Lines (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#query-and-list-contract-lines-legacy)
    *   [Get Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#get-contract-line)
    *   [Create Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#create-contract-line)
    *   [Update Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#update-contract-line)
    *   [Post Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#post-contract-line)
    *   [Deliver Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#deliver-contract-line)
    *   [Hold Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#hold-contract-line)
    *   [Resume Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#resume-contract-line)
    *   [Delete Contract Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#delete-contract-line)
*   [Contract Line Expenses](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#contract-line-expenses)
    *   [Get Contract Line Expense Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#get-contract-line-expense-object-definition)
    *   [Query and List Contract Line Expenses](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#query-and-list-contract-line-expenses)
    *   [Query and List Contract Line Expenses (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#query-and-list-contract-line-expenses-legacy)
    *   [Get Contract Line Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#get-contract-line-expense)
    *   [Create Contract Line Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#create-contract-line-expense)
    *   [Update Contract Line Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#update-contract-line-expense)
    *   [Post Contract Line Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#post-contract-line-expense)
    *   [Delete Contract Line Expense](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#delete-contract-line-expense)

* * *

A contract line is a product or service associated with the contract.

* * *

### Get Contract Line Object Definition

#### `lookup`

> List all the fields and relationships for the contract line object:

```
<lookup>
    <object>CONTRACTDETAIL</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTDETAIL` |

* * *

### Query and List Contract Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, line number, and associated contract ID for each contract line:

```
<query>
    <object>CONTRACTDETAIL</object>
    <select>
        <field>RECORDNO</field>
        <field>LINENO</field>
        <field>CONTRACTID</field>
    </select>
</query>
```

> List the Evergreen template in use for each recurring contract line:

```
<query>
    <object>CONTRACTDETAIL</object>
    <filter>
        <equalto>
            <field>RECURRING</field>
            <value>true</value>
        </equalto>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
        <field>CONTRACT.EVERGREENMACRO</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTDETAIL` |
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

### Query and List Contract Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTDETAIL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTDETAIL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | State. Use `P` for In progress, `O` for Renewal only, `C` for Cancelled, `N` for Not renewed. |
| BILLINGMETHOD | Optional | string | Billing method. Use `F` for Fixed price, `Q` for Quantity based. |
| BILLINGOPTIONS | Optional | string | Flat/fixed amount frequency. Use `O` for One-time, `U` for Use billing template, or `I` for Include with every invoice. |
| LINETYPE | Optional | string | Line type of the contract line. Use `S` for Sale (positive contract lines), `D` for Discount (contract lines with positive Quantity and negative Flat/Fixed), or `B` for Debook (contract lines with a negative Quantity and a positive Rate). |

* * *

### Get Contract Line

#### `read`

```
<read>
    <object>CONTRACTDETAIL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTDETAIL` |
| keys | Required | string | Comma-separated list of contract line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Contract Line

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#history-create-contract-line)

| Release | Changes |
| --- | --- |
| 2023 Release 4 | Added REV\_REC\_ON\_INVOICE |
| 2022 Release 2 | Added RECURRING |
| 2021 Release 3 | Added USAGELINETYPE, COMMITTEDUSAGEENDACTION, and COMMITTEDUSAGEEXCESS, and added Renewal only as an option for STATE |
| 2021 Release 2 | Added BILLTOCONTACTNAME and BILLTOSOURCE |
| 2021 Release 1 | Added SHIPTOSOURCE, SHIPTOCONTACTNAME, BILLINGFREQUENCY |
| 2020 Release 4 | Added PRORATEBILLINGPERIOD |
| 2020 Release 1 | Added STATE |
| 2019 Release 1 | Added TASKID |
| 2018 Release 3 | Added RENEWALBILLINGTEMPLATENAME |
| 2018 Release 2 | Added GLPOSTINGDATE |

#### `create`

```
<create>
    <CONTRACTDETAIL>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <ITEMID>DWNL</ITEMID>
        <BILLINGMETHOD>Fixed price</BILLINGMETHOD>
        <BILLINGOPTIONS>One-time</BILLINGOPTIONS>
        <BEGINDATE>09/01/2017</BEGINDATE>
        <ENDDATE>09/01/2018</ENDDATE>
        <BILLINGTEMPLATENAME>40-30-20-10</BILLINGTEMPLATENAME>
        <FLATAMOUNT>1000.00</FLATAMOUNT>
        <REVENUETEMPLATENAME>SL Man (Rev)</REVENUETEMPLATENAME>
        <LOCATIONID>US</LOCATIONID>
    </CONTRACTDETAIL>
</create>
```

> Creates a line with its own ship to contact:

```
<create>
    <CONTRACTDETAIL>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <BEGINDATE>09/01/2017</BEGINDATE>
        <ENDDATE>09/01/2018</ENDDATE>
        <ITEMID>055</ITEMID>
        <SHIPTOCONTACTNAME>Millian Group</SHIPTOCONTACTNAME>
        <BILLINGMETHOD>Fixed price</BILLINGMETHOD>
        <BILLINGOPTIONS>Use billing template</BILLINGOPTIONS>
        <BILLINGTEMPLATENAME>12-months, equal</BILLINGTEMPLATENAME>
        <BILLINGSTARTDATE>09/01/2017</BILLINGSTARTDATE>
        <BILLINGENDDATE>09/01/2018</BILLINGENDDATE>
        <FLATAMOUNT>1000.00</FLATAMOUNT>
        <REVENUETEMPLATENAME>Daily rate</REVENUETEMPLATENAME>
        <REVENUESTARTDATE>10/01/2017</REVENUESTARTDATE>
        <REVENUEENDDATE>10/01/2018</REVENUEENDDATE>
    </CONTRACTDETAIL>
</create>
```

> Creates a line for a quantity-based billing method:

```
<create>
    <CONTRACTDETAIL>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <BEGINDATE>05/01/2020</BEGINDATE>
        <ENDDATE>05/01/2021</ENDDATE>
        <ITEMID>055</ITEMID>
        <BILLINGMETHOD>Quantity based</BILLINGMETHOD>
        <USAGELINETYPE>Variable</USAGELINETYPE>
        <BILLINGOPTIONS>One-time</BILLINGOPTIONS>
        <USAGEQTYRESETPERIOD>After each invoice</USAGEQTYRESETPERIOD>
        <USAGEQTYRECUR>false</USAGEQTYRECUR>
        <REVENUETEMPLATENAME>Daily rate</REVENUETEMPLATENAME>
        <REVENUESTARTDATE>09/01/2020</REVENUESTARTDATE>
        <REVENUEENDDATE>09/01/2021</REVENUEENDDATE>
    </CONTRACTDETAIL>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTDETAIL | Required | object | Object to create |

`CONTRACTDETAIL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Required | string | Contract ID |
| ITEMID | Required | string | Item ID |
| STATE | Optional | string | State in which to create the contract line. Use `Draft` for a contract line that will not yet post to the GL, `Renewal only` for a contract line that will be included in the next renewal, or `In progress`. To move a contract line from `Draft` to `In progress`, use the [post](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#post-contract-line) function. (Default: `In progress`) |
| BEGINDATE | Optional | string | Start date in format `mm/dd/yyyy`. Required for non-recurring contracts. |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy`. Required for non-recurring contracts. |
| ITEMDESC | Optional | string | Item description |
| RENEWAL | Optional | boolean | Renewal. Use `false` for No, `true` for Yes. (Default: `false`) |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy`. Leave blank to use the start date (if the start is in the future, today’s date is used instead). |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value. |
| BILLINGMETHOD | Required | string | Billing method. Use either `Fixed price` or `Quantity based`. (Default: `Fixed price`) |
| BILLINGOPTIONS | Optional | string | Flat/fixed amount frequency. Only used if `BILLINGMETHOD` is `Fixed price`. Use either `One-time`, `Use billing template`, or `Include with every invoice`. (Default: `Use billing template`) |
| BILLINGFREQUENCY | Optional | string | Billing frequency, which is required if `BILLINGOPTIONS` is set to `Include with every invoice`. Use `Monthly`, `Quarterly`,`Annually`, or omit value to inherit from the contract level. (Default: billing frequency for the contract) |
| RECURRING | Optional | boolean | Indicates whether the line is recurring for an Evergreen contract. Use `false` for No, `true` for Yes. Defaults to `true` for an Evergreen contract. |
| PRORATEBILLINGPERIOD | Optional | string | Specifies whether to prorate partial months. Use `true` to prorate, `false` otherwise. The `BILLINGMETHOD` must be set to `Fixed price` and `BILLINGOPTIONS` must be set to `Include with every invoice`. (Default: `false`) |
| BILLINGTEMPLATENAME | Optional | string | Billing template. Only used if `BILLINGOPTIONS` is `Use billing template`. |
| BILLINGSTARTDATE | Optional | string | Billing start date in format `mm/dd/yyyy`. Only used if `BILLINGOPTIONS` is `Use billing template`. Leave blank to use line start date |
| BILLINGENDDATE | Optional | string | Billing end date in format `mm/dd/yyyy`. Only used if `BILLINGOPTIONS` is `Use billing template`. Leave blank to use line end date |
| USAGEQTYRESETPERIOD | Optional | string | Reset usage quantity. Determines when the included units are counted and determines when the system billing counter resets. Use either `After each invoice` or `After each renewal`. Only applicable if `BILLINGMETHOD` is set to `Quantity based`. Also, the contract must have a billing price list set (via `PRCLIST`). |
| USAGEQTYRECUR | Optional | boolean | Usage quantity recurs. If set to `true`, every usage record for a line item is treated as a recurring usage record. This means that each period, new usage records are created in order to re-invoice the quantities (for example, user licenses). Changing this field affects how the system calculates usage billing. Only applicable if `BILLINGMETHOD` is set to `Quantity based`. |
| RENEWALBILLINGTEMPLATENAME | Optional | string | Name of a renewal billing template. Ensure the renewal billing template term is less than or equal to the contract renewal term. Only used if `RENEWAL` is `true`. If `BILLINGOPTIONS` is set to `Use billing template` on the contract line, a billing template is required. If `RENEWALBILLINGTEMPLATENAME` is omitted, the system first defaults to the `BILLINGTEMPLATENAME` on the contract line, then to the default billing template defined on the item. |
| GLPOSTINGDATE | Optional | string | Date the Unbilled AR and Unbilled deferred revenue posts, in format `mm/dd/yyyy`. Leave blank to use the contract line start date minus the bill-in-advance period (if this would occur in a closed period, the first date in the first available open period is used instead). |
| QUANTITY | Optional | number | Flat/fixed amount calculate quantity. Only used if `BILLINGMETHOD` is `Fixed price`. |
| PRICE | Optional | number | Flat/fixed amount calculate rate. Only used if `BILLINGMETHOD` is `Fixed price`. |
| MULTIPLIER | Optional | number | Flat/fixed amount calculate multiplier. Only used if `BILLINGMETHOD` is `Fixed price`. |
| REV\_REC\_ON\_INVOICE | Opitional | boolean | Set to `false` to defer revenue for the contract line. Set to `true` to automatically post the contract line as revenue when it is invoiced. (Default: `false`) |
| DISCOUNTPERCENT | Optional | number | Flat/fixed amount calculate discount. Only used if `BILLINGMETHOD` is `Fixed price`. |
| FLATAMOUNT | Optional | currency | Base/flat fixed amount. |
| USAGELINETYPE | Optional | string | Specifies the quantity type. Use `Variable` for a variable quantity or `Committed` to predefine a quantity to consume over the course of the contract. (Default: `Variable`) |
| COMMITTEDUSAGEENDACTION | Optional | string | Specifies how to handle the unused quantity. Required when using the `Committed` quantity type (via `USAGELINETYPE`). Use `Bill unused quantity`, `Cancel unused quantity` or `Do nothing`. (Default: `Bill unused quantity`) |
| COMMITTEDUSAGEEXCESS | Optional | string | Specifies the action to take when the contract detail end date occurs. Required when using the `Committed` quantity type (via `USAGELINETYPE`). Use `Bill overage`, `Don’t allow overage` or `Do nothing`. (Default: `Bill overage`) |
| REVENUETEMPLATENAME | Optional | string | 606 revenue template |
| REVENUESTARTDATE | Optional | string | 606 revenue start date in format `mm/dd/yyyy`. Leave blank to use line start date |
| REVENUEENDDATE | Optional | string | 606 revenue end date in format `mm/dd/yyyy`. Leave blank to use line end date |
| REVENUE2TEMPLATENAME | Optional | string | Legacy revenue template |
| REVENUE2STARTDATE | Optional | string | Legacy revenue start date in format `mm/dd/yyyy`. Leave blank to use line start date |
| REVENUE2ENDDATE | Optional | string | Legacy revenue end date in format `mm/dd/yyyy`. Leave blank to use line end date |
| BILLTOCONTACTNAME | Optional | string | Bill to contact name for the detail, which can override the Bill to contact name on the contract depending on the value of the Bill to source. |
| BILLTOSOURCE | Optional | string | Specifies whether the Bill to contact name on the line is overridden when the Bill to contact name on the contract itself is modified. Use `Contract value` to allow this overriding or `User-specified value` to preserve the Bill to contact name on the line. (Default: If `BILLTOCONTACTNAME` is set and not equal to the contract Bill to, defaults to `User-specified value`, otherwise, defaults to `Contract value`). |
| SHIPTOCONTACTNAME | Optional | string | Ship to contact name for the detail, which can override the Ship to contact name on the contract depending on the value of the Ship to source. |
| SHIPTOSOURCE | Optional | string | Specifies whether the Ship to contact name on the line is overridden when the Ship to contact name on the contract itself is modified. Use `Contract value` to allow this overriding or `User-specified value` to preserve the Ship to contact name on the line. (Default: If `SHIPTOCONTACTNAME` is set and not equal to the contract Ship to, defaults to `User-specified value`, otherwise, defaults to `Contract value`) |
| LOCATIONID | Required | string | Location ID |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |

* * *

### Update Contract Line

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#history-update-contract-line)

| Release | Changes |
| --- | --- |
| 2023 Release 4 | Added REV\_REC\_ON\_INVOICE |
| 2022 Release 2 | Added RECURRING |
| 2021 Release 3 | Added USAGELINETYPE, COMMITTEDUSAGEENDACTION, and COMMITTEDUSAGEEXCESS |
| 2021 Release 2 | Added BILLTOCONTACTNAME and BILLTOSOURCE |
| 2021 Release 1 | Added SHIPTOSOURCE, SHIPTOCONTACTNAME, BILLINGFREQUENCY |
| 2020 Release 4 | Added PRORATEBILLINGPERIOD |
| 2019 Release 1 | Added TASKID |
| 2018 Release 3 | Added RENEWALBILLINGTEMPLATENAME |
| 2018 Release 2 | Added GLPOSTINGDATE |

#### `update`

```
<update>
    <CONTRACTDETAIL>
        <RECORDNO>123</RECORDNO>
        <DEPARTMENTID>300</DEPARTMENTID>
    </CONTRACTDETAIL>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTDETAIL | Required | object | Object to update |

`CONTRACTDETAIL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of contract line to update |
| ITEMID | Optional | string | Item ID |
| BEGINDATE | Optional | string | Start date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy` |
| ITEMDESC | Optional | string | Item description |
| RENEWAL | Optional | boolean | Renewal. Use `false` for No, `true` for Yes. |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy` |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value |
| BILLINGMETHOD | Optional | string | Billing method. Use either `Fixed price` or `Quantity based`. |
| PRORATEBILLINGPERIOD | Optional | string | Specifies whether to prorate partial months. Use `true` to prorate, `false` otherwise. The `BILLINGMETHOD` must be set to `Fixed price` and `BILLINGOPTIONS` must be set to `Include with every invoice`. |
| BILLINGOPTIONS | Optional | string | Flat/fixed amount frequency. Only used if `BILLINGMETHOD` is `Fixed price`. Use either `One-time`, `Use billing template`, or `Include with every invoice`. |
| BILLINGFREQUENCY | Optional | string | Billing frequency, which is required if `BILLINGOPTIONS` is set to `Include with every invoice`. Use `Monthly`, `Quarterly`, `Annually`, or omit value to inherit from the contract level. |
| RECURRING | Optional | boolean | Indicates whether the line is recurring for an Evergreen contract. Use `false` for No, `true` for Yes. |
| BILLINGTEMPLATENAME | Optional | string | Billing template. Only used if `BILLINGOPTIONS` is `Use billing template`. |
| BILLINGSTARTDATE | Optional | string | Billing start date in format `mm/dd/yyyy`. Only used if `BILLINGOPTIONS` is `Use billing template`. |
| BILLINGENDDATE | Optional | string | Billing end date in format `mm/dd/yyyy`. Only used if `BILLINGOPTIONS` is `Use billing template`. |
| BILLINGENDDATE | Optional | string | Billing end date in format `mm/dd/yyyy`. Only used if `BILLINGOPTIONS` is `Use billing template`. Leave blank to use line end date |
| USAGEQTYRESETPERIOD | Optional | string | Reset usage quantity. Determines when the included units are counted and determines when the system billing counter resets. Use either `After each invoice` or `After each renewal`. Only applicable if `BILLINGMETHOD` is set to `Quantity based`. Also, the contract must have a billing price list set (via `PRCLIST`). |
| RENEWALBILLINGTEMPLATENAME | Optional | string | Name of a renewal billing template. Ensure the renewal billing template term is less than or equal to the contract renewal term. Only used if `RENEWAL` is `true`. If `BILLINGOPTIONS` is set to `Use billing template` on the contract line, a billing template is required. If `RENEWALBILLINGTEMPLATENAME` is omitted, the system first defaults to the `BILLINGTEMPLATENAME` on the contract line, then to the default billing template defined on the item. |
| GLPOSTINGDATE | Optional | string | Date the Unbilled AR and Unbilled deferred revenue posts, in format `mm/dd/yyyy`. Leave blank to use the contract line start date minus the bill-in-advance period (if this would occur in a closed period, the first date in the first available open period is used instead). |
| QUANTITY | Optional | number | Flat/fixed amount calculate quantity. Only used if `BILLINGMETHOD` is `Fixed price`. |
| PRICE | Optional | number | Flat/fixed amount calculate rate. Only used if `BILLINGMETHOD` is `Fixed price`. |
| MULTIPLIER | Optional | number | Flat/fixed amount calculate multiplier. Only used if `BILLINGMETHOD` is `Fixed price`. |
| REV\_REC\_ON\_INVOICE | Opitional | boolean | Set to `false` to defer revenue for the contract line. Set to `true` to automatically post the contract line as revenue when it is invoiced. (Default: `false`) |
| DISCOUNTPERCENT | Optional | number | Flat/fixed amount calculate discount. Only used if `BILLINGMETHOD` is `Fixed price`. |
| FLATAMOUNT | Optional | currency | Base/flat fixed amount |
| USAGELINETYPE | Optional | string | Specifies the quantity type. Use `Variable` for a variable quantity or `Committed` to predefine a quantity to consume over the course of the contract. |
| COMMITTEDUSAGEENDACTION | Optional | string | Specifies how to handle the unused quantity. Required when using the `Committed` quantity type (via `USAGELINETYPE`). Use `Bill unused quantity`, `Cancel unused quantity` or `Do nothing`. |
| COMMITTEDUSAGEEXCESS | Optional | string | Specifies the action to take when the contract detail end date occurs. Required when using the `Committed` quantity type (via `USAGELINETYPE`). Use `Bill overage`, `Don’t allow overage` or `Do nothing`. |
| REVENUETEMPLATENAME | Optional | string | 606 revenue template |
| REVENUESTARTDATE | Optional | string | 606 revenue start date in format `mm/dd/yyyy` |
| REVENUEENDDATE | Optional | string | 606 revenue end date in format `mm/dd/yyyy` |
| REVENUE2TEMPLATENAME | Optional | string | Legacy revenue template |
| REVENUE2STARTDATE | Optional | string | Legacy revenue start date in format `mm/dd/yyyy` |
| REVENUE2ENDDATE | Optional | string | Legacy revenue end date in format `mm/dd/yyyy` |
| BILLTOCONTACTNAME | Optional | string | Bill to contact name for the detail, which can override the Bill to contact name on the contract depending on the value of the Bill to source. |
| BILLTOSOURCE | Optional | string | Specifies whether the Bill to contact name on the line is overridden when the Bill to contact name on the contract itself is modified. Use `Contract value` to allow this overriding or `User-specified value` to preserve the Bill to contact name on the line. (Default: If `BILLTOCONTACTNAME` is set and not equal to the contract Bill to, defaults to `User-specified value`, otherwise, defaults to `Contract value`). |
| SHIPTOCONTACTNAME | Optional | string | Ship to contact name for the detail, which overrides the ship to contact name on the contract. |
| SHIPTOSOURCE | Optional | string | Specifies whether the Ship to contact name on the line is overridden when the Ship to contact name on the contract itself is modified. Use `Contract value` to allow this overriding or `User-specified value` to preserve the Ship to contact name on the line. |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CLASSID | Optional | string | Class ID |

* * *

### Post Contract Line

You can post a contract line that is in `Draft` state so that it is fully validated and posted to the GL. The state of a posted contract line is changed from `Draft` to `In progress`. You can only post contract lines when the contract state is `In progress`.

If your draft contract line is missing required parameter values, check the error messages from the `post` response and use the [update](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#update-contract-line) function to correct any issues before trying to post again.

#### `post`

```
<post>
    <CONTRACTDETAIL>
        <RECORDNO>529</RECORDNO>
        <GLPOSTINGDATE>01/01/2020</GLPOSTINGDATE>
        <POSTMEMO>Contract line has been finalized</POSTMEMO>
    </CONTRACTDETAIL>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | object | Use `CONTRACTDETAIL` |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the contract line to post |
| GLPOSTINGDATE | Required | string | GL posting date in format `mm/dd/yyyy` |
| POSTMEMO | Optional | string | Memo about the post |

* * *

### Deliver Contract Line

This function is applicable when using event-driven revenue recognition. It changes the Delivery status of the given contract line to Delivered.

#### `deliver`

```
<deliver>
    <CONTRACTDETAIL>
        <RECORDNO>123</RECORDNO>
        <DELIVERYDATE>07/31/2017</DELIVERYDATE>
    </CONTRACTDETAIL>
</deliver>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTDETAIL | Required | object | Object to operate on |

`CONTRACTDETAIL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Contract line `RECORDNO` to set to Delivered. |
| DELIVERYDATE | Required | string | Delivery date in format `mm/dd/yyyy` |

* * *

### Hold Contract Line

When you use this function, the state of the contract line remains in progress, but the [billing](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/) and [revenue](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/) schedules and/or [expense schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/) can be put on hold.

#### `hold`

```
<hold>
    <CONTRACTDETAIL>
        <RECORDNO>123</RECORDNO>
        <ASOFDATE>07/31/2017</ASOFDATE>
        <BILLING>true</BILLING>
        <REVENUE>true</REVENUE>
        <EXPENSE>true</EXPENSE>
    </CONTRACTDETAIL>
</hold>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTDETAIL | Required | object | Object to hold |

`CONTRACTDETAIL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of contract line to hold |
| ASOFDATE | Optional | string | Hold date in format `mm/dd/yyyy` (Default: Last posted schedule entry date + 1) |
| BILLING | Optional | boolean | Hold billing. Use `false` for No, `true` for Yes. (Default: `false`) |
| REVENUE | Optional | boolean | Hold revenue. Use `false` for No, `true` for Yes. (Default: `false`) |
| EXPENSE | Optional | boolean | Hold expense. Use `false` for No, `true` for Yes. (Default: `false`) |
| MEMO | Optional | string | Description of the hold. 500 character limit. |

* * *

### Resume Contract Line

#### `resume`

```
<resume>
    <CONTRACTDETAIL>
        <RECORDNO>123</RECORDNO>
        <ASOFDATE>07/31/2017</ASOFDATE>
        <BILLING>true</BILLING>
        <REVENUE>true</REVENUE>
        <EXPENSE>true</EXPENSE>
    </CONTRACTDETAIL>
</resume>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTDETAIL | Required | object | Object to resume |

`CONTRACTDETAIL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of contract line to resume. |
| ASOFDATE | Required | string | Resume date in format `mm/dd/yyyy` |
| BILLING | Optional | boolean | Resume billing. Use `false` for No, `true` for Yes. (Default: `false`) |
| REVENUE | Optional | boolean | Resume revenue. Use `false` for No, `true` for Yes. (Default: `false`) |
| EXPENSE | Optional | boolean | Resume expense. Use `false` for No, `true` for Yes. (Default: `false`) |
| MEMO | Optional | string | Description of the hold. 500 character limit. |
| REVENUEADJUSTMENTTYPE | Optional | String | Use `One time` to set the scheduled posting date for all revenue that was scheduled prior to the resume date to the resume date, `Distributed` to recalculate the revenue schedule term using the resume date as the start date and spread the total revenue amount across the shortened schedule so that any skipped periods during the hold period are eventually caught up, or `Walk forward` to regenerate the revenue schedule using the resume date and push the end date out to the date that is equal to the number of days from the original revenue template start date to the resume date. The system prorates any partial periods. The whole period amount remains equal to the originally scheduled whole period amount. (Default: revenue adjustment option specified in the revenue template) |

* * *

### Delete Contract Line

#### `delete`

```
<delete>
    <object>CONTRACTDETAIL</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTDETAIL` |
| keys | Required | string | Comma-separated list of contract line `RECORDNO` to delete |

* * *

Contract Line Expenses
----------------------

### Get Contract Line Expense Object Definition

#### `lookup`

> List all the fields and relationships for the contract line expense object:

```
<lookup>
    <object>CONTRACTEXPENSE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |

* * *

### Query and List Contract Line Expenses

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, associated contract ID, and type for each contract line expense:

```
<query>
    <object>CONTRACTEXPENSE</object>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
        <field>TYPE</field>
    </select>
    <filter>
        <equalto>
            <field>TYPE</field>
            <value>Contract line</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

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

### Query and List Contract Line Expenses (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTEXPENSE</object>
    <fields>*</fields>
    <query>TYPE = 'L'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TYPE | Required | string | Type. Use `L` for Contract line expenses. |
| STATE | Optional | string | State. Use `P` for In progress, `C` for Cancelled |

* * *

### Get Contract Line Expense

#### `read`

```
<read>
    <object>CONTRACTEXPENSE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |
| keys | Required | string | Comma-separated list of contract line expense `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Contract Line Expense

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#history-create-contract-line-expense)

| Release | Changes |
| --- | --- |
| 2020 Release 1 | Added STATE |

#### `create`

```
<create>
    <CONTRACTEXPENSE>
        <CONTRACTDETAILKEY>15</CONTRACTDETAILKEY>
        <ITEMID>SUPP</ITEMID>
        <POSTINGDATE>05/01/2017</POSTINGDATE>
        <AMOUNT>400.00</AMOUNT>
        <LOCATIONID>US</LOCATIONID>
        <TEMPLATENAME>SL Man (Exp)</TEMPLATENAME>
    </CONTRACTEXPENSE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE | Required | object | Object to create |

`CONTRACTEXPENSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTDETAILKEY | Required | integer | Contract Line Record Number |
| ITEMID | Required | string | Item ID |
| STATE | Optional | string | State in which to create the contract line expense. Use `Draft` for a contract line expense that will not yet post to the GL (Default: `In progress`). To move a contract line expense from `Draft` to `In progress`, use the [post](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#post-contract-line-expense) function. |
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

### Update Contract Line Expense

#### `update`

```
<update>
    <CONTRACTEXPENSE>
        <RECORDNO>123</RECORDNO>
        <DEPARTMENTID>500</DEPARTMENTID>
    </CONTRACTEXPENSE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE | Required | object | Object to update |

`CONTRACTEXPENSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of contract line expense to update. |
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

### Post Contract Line Expense

You can post a contract line expense that is in `Draft` state so that it is fully validated and posted to the GL. The state of a posted contract line expense is changed from `Draft` to `In progress`. You can only post contract line expenses when the contract state is `In progress`.

If your draft contract line expense is missing required parameter values, check the error messages from the `post` response and use the [update](https://developer.intacct.com/api/contracts-rev-mgmt/contract-lines/#update-contract-line-expense) function to correct any issues before trying to post again.

#### `post`

```
<post>
    <CONTRACTEXPENSE>
        <RECORDNO>321</RECORDNO>
        <GLPOSTINGDATE>01/01/2020</GLPOSTINGDATE>
        <POSTMEMO>Contract expense has been finalized</POSTMEMO>
    </CONTRACTEXPENSE>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | object | Use `CONTRACTEXPENSE` |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the contract line expense to post |
| GLPOSTINGDATE | Required | string | GL posting date in format `mm/dd/yyyy` |
| POSTMEMO | Optional | string | Memo about the post |

* * *

### Delete Contract Line Expense

#### `delete`

```
<delete>
    <object>CONTRACTEXPENSE</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE` |
| keys | Required | string | Comma-separated list of contract line expense `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

