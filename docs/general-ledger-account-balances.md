Title: Account Balances

URL Source: https://developer.intacct.com/api/general-ledger/account-balances/

Markdown Content:
*   [List Account Balances (Legacy)](https://developer.intacct.com/api/general-ledger/account-balances/#list-account-balances-legacy)
*   [List Account Balances by Dimensions, Synchronous](https://developer.intacct.com/api/general-ledger/account-balances/#list-account-balances-by-dimensions-synchronous)
*   [List Account Balances by Dimensions, Asynchronous](https://developer.intacct.com/api/general-ledger/account-balances/#list-account-balances-by-dimensions-asynchronous)
*   [Get Raw Account Balance Object Definition](https://developer.intacct.com/api/general-ledger/account-balances/#get-raw-account-balance-object-definition)
*   [Query and List Raw Account Balances](https://developer.intacct.com/api/general-ledger/account-balances/#query-and-list-raw-account-balances)

* * *

View balances of accounts by a single account, a range of accounts, an account group, or even by dimensions.

* * *

List Account Balances (Legacy)
------------------------------

[History](https://developer.intacct.com/api/general-ledger/account-balances/#history-get-account-balances)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added costtypeid, costtypeid\_subs |
| 2019 Release 4 | Added taskid, taskid\_subs |

Account balances include a starting balance, for period/net change amounts, ending balance, and adjustments together with all book and dimension combinations. Parent-child hierarchy dimensions can be included as well. This function provides information in a readable format similar to that provided by the Sage Intacct Account Balance standard report.

#### `get_accountbalances`

> List balances of an account for a reporting period:

```
<get_accountbalances>
    <reportingperiodname>Calendar Year Ended December 2016</reportingperiodname>
    <glaccountno>4000</glaccountno>
    <showzerobalances>false</showzerobalances>
</get_accountbalances>
```

> List balances for an account group for a date range:

```
<get_accountbalances>
    <startdate>
        <year>2016</year>
        <month>01</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2016</year>
        <month>01</month>
        <day>31</day>
    </enddate>
    <accountgroupname>Total Revenue</accountgroupname>
    <showzerobalances>false</showzerobalances>
</get_accountbalances>
```

> List balances for a range of accounts for a date range:

```
<get_accountbalances>
    <startdate>
        <year>2016</year>
        <month>01</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2016</year>
        <month>01</month>
        <day>31</day>
    </enddate>
    <startaccountno>4000</startaccountno>
    <endaccountno>4999</endaccountno>
    <showzerobalances>false</showzerobalances>
</get_accountbalances>
```

> List balances for an account with GAAP adjustment and accrual book for a reporting period:

```
<get_accountbalances>
    <reportingperiodname>Calendar Year Ended December 2016</reportingperiodname>
    <glaccountno>4000</glaccountno>
    <showzerobalances>false</showzerobalances>
    <reportingbook>ACCRUAL</reportingbook>
    <adjbooks>
        <adjbook>GAAP</adjbook>
    </adjbooks>
    <includereportingbook>false</includereportingbook>
</get_accountbalances>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| reportingperiodname | Optional | string | Reporting period name. Required if not using `startdate` and `enddate`. |
| startdate | Optional | [object](https://developer.intacct.com/api/general-ledger/account-balances/#get_accountbalances.date) | Opening balance date. Required if not using `reportingperiodname`. |
| enddate | Optional | [object](https://developer.intacct.com/api/general-ledger/account-balances/#get_accountbalances.date) | Closing balance date. Required if not using `reportingperiodname`. |
| glaccountno | Optional | string | GL account number. Required if not using `accountgroupname` or `startaccountno` and `endaccountno`. |
| accountgroupname | Optional | string | Account group name. Required if not using `glaccountno` or `startaccountno` and `endaccountno`. |
| startaccountno | Optional | string | Starting GL account number. Required if not using `glaccountno` or `accountgroupname`. |
| endaccountno | Optional | string | Ending GL account number. Required if not using `glaccountno` or `accountgroupname`. |
| locationid | Optional | string | Location ID. If you pass an empty element, no data for locations is listed. This field is required in a multi-base currency company. |
| departmentid | Optional | string | Department ID. (If you pass an empty element, no data for departments is listed.) |
| showzerobalances | Optional | boolean | Return zero balances. Use `true` or `false`. (Default: `false`) |
| reportingbook | Optional | string | Reporting book ID. Use `ACCRUAL` or `CASH` depending on the company configuration. If Global Consolidations is enabled, you can provide a consolidation book ID instead. (Default: Configured reporting book ID) |
| adjbooks | Optional | array of `adjbook` | Adjustment book IDs for journals that are enabled in the GL configuration. Use `GAAP`, `TAX`, and/or the IDs of user defined books. Do not append text to the IDs. If you need help, look at the Account Balances page in the Sage Intacct UI to see what is enabled. |
| includereportingbook | Optional | boolean | Combine reporting book with other adjustment books. Use `true` to include the reporting book entries with entries from the specified adjustment books, or `false` to return only entries for the specified adjustment books. |
| statistical | Optional | string | Statistical accounts. Use either `include`, `exclude`, or `only`. (Default: `include`) |
| dept\_subs | Optional | boolean | Include department sub dimensions. (Default: `true`) |
| loc\_subs | Optional | boolean | Include location sub dimensions. (Default: `true`) |
| projectid | Optional | string | Project ID or project group ID. |
| projectid\_subs | Optional | boolean | Include project sub dimensions. (Default: `true`) |
| projecttypeid | Optional | string | Project type. Do not use if project ID is set. |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| taskid\_subs | Optional | boolean | Include task sub dimensions. (Default: `true`) |
| costtypeid | Optional | string | Cost type ID. Only available when `taskid` is also specified. |
| costtypeid\_subs | Optional | boolean | Include cost type sub dimensions. (Default: `true`) |
| customerid | Optional | string | Customer ID or customer group ID |
| customerid\_subs | Optional | boolean | Include customer sub dimensions. (Default: `true`) |
| customertypeid | Optional | string | Customer type. Do not use if Customer ID is set. |
| vendorid | Optional | string | Vendor ID or vendor group ID |
| vendorid\_subs | Optional | boolean | Include vendor sub dimensions. (Default: `true`) |
| vendortypeid | Optional | string | Vendor type. Do not use if Vendor ID is set. |
| employeeid | Optional | string | Employee ID or employee group ID |
| employeeid\_subs | Optional | boolean | Include employee sub dimensions. (Default: `true`) |
| employeetypeid | Optional | string | Employee type. Do not use if Employee ID is set. |
| itemid | Optional | string | Item ID or item group ID |
| productlineid | Optional | string | Product line. Do not use if Item ID is set. |
| classid | Optional | string | Class ID or class group ID |
| classid\_subs | Optional | boolean | Include class sub dimensions. (Default: `true`) |
| contractid | Optional | string | Contract ID or contract group ID |
| contractid\_subs | Optional | boolean | Include contract sub dimensions. (Default: `true`) |
| warehouseid | Optional | string | Warehouse ID or warehouse group ID |
| warehouseid\_subs | Optional | boolean | Include warehouse sub dimensions. (Default: `true`) |
| userDefinedDimensions | Optional | array of [`userDefinedDimension`](https://developer.intacct.com/api/general-ledger/account-balances/#get_accountbalances.userDefinedDimension) | User defined dimension filters |

`get_accountbalances.startdate`  
`get_accountbalances.enddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`get_accountbalances.userDefinedDimension`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| objectName | Required | string | UDD object integration name. |
| recordId | Optional | string | UDD record ID. Do not use if Record name is set. |
| recordName | Optional | string | UDD record name. Do not use if Record ID set. If UDD name is not unique, must use record ID instead. |

* * *

List Account Balances by Dimensions, Synchronous
------------------------------------------------

[History](https://developer.intacct.com/api/general-ledger/account-balances/#history-get-accountbalancesbydimensions)

| Release | Changes |
| --- | --- |
| 2023 Release 4 | Added showperiodbalancedetail |
| 2021 Release 2 | Added contentselection, budgetid, budgetcomparison, showzerowithactivity |
| 2020 Release 2 | Added costtypeid, costtypeid\_subs |
| 2019 Release 4 | Added taskid, taskid\_subs |

This function lists account balances grouped by any dimensions (standard or user-defined) such as location and department. You can use this function to return budget data or both actual and budget data.

#### `get_accountbalancesbydimensions`

> List balances for a range of accounts for a date range and group by location and department:

```
<get_accountbalancesbydimensions>
    <startdate>
        <year>2016</year>
        <month>01</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2016</year>
        <month>12</month>
        <day>31</day>
    </enddate>
    <startaccountno>4000</startaccountno>
    <endaccountno>4999</endaccountno>
    <locationid>1</locationid>
    <groupby>location,department</groupby>
</get_accountbalancesbydimensions>
```

> The above function returns data structured like this:

```
<data>
    <accountbalance>
        <glaccountno>4000</glaccountno>
        <startbalance>0</startbalance>
        <periodbalance>-2040.17</periodbalance>
        <endbalance>-2040.17</endbalance>
        <currency>USD</currency>
        <locationid>1</locationid>
        <locationname>United States of America</locationname>
        <departmentid>8</departmentid>
        <departmentname>Finance</departmentname>
    </accountbalance>
    <accountbalance>
        <glaccountno>4000</glaccountno>
        <startbalance>0</startbalance>
        <periodbalance>-13320.01</periodbalance>
        <endbalance>-13320.01</endbalance>
        <currency>USD</currency>
        <locationid>AZ</locationid>
        <locationname>Arizona</locationname>
        <departmentid>AU</departmentid>
        <departmentname>Auditing</departmentname>
    </accountbalance>
    <accountbalance>
        <glaccountno>4000</glaccountno>
        <startbalance>0</startbalance>
        <periodbalance>-4080.01</periodbalance>
        <endbalance>-4080.01</endbalance>
        <currency>USD</currency>
        <locationid>TX</locationid>
        <locationname>Texas</locationname>
        <departmentid>11</departmentid>
        <departmentname>Accounting</departmentname>
    </accountbalance>
    ...
</data>
```

> List account balances for a specific location, grouped by location, department, and category (a UDD):

```
<get_accountbalancesbydimensions>
    <startdate>
        <year>2016</year>
        <month>01</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2016</year>
        <month>12</month>
        <day>31</day>
    </enddate>
    <startaccountno>4000</startaccountno>
    <endaccountno>4999</endaccountno>
    <locationid>1</locationid>
    <loc_subs>true</loc_subs>
    <userDefinedDimensions>
        <userDefinedDimension>
            <objectName>category</objectName>
            <recordName>CAT1</recordName>
        </userDefinedDimension>
    </userDefinedDimensions>
    <groupby>location,department,category</groupby>
</get_accountbalancesbydimensions>
```

> List account balances for actual and budgeted amounts and calculate the difference by subtracting the actual from the budgeted:

```
<get_accountbalancesbydimensions>
    <reportingperiodname>Month Ended January 2021</reportingperiodname>
    <contentselection>Actual and Budget</contentselection>
    <budgetid>Proj_01-budget</budgetid>
    <budgetcomparison>Budget minus Actual</budgetcomparison>
    <glaccountno>4000</glaccountno>
    <locationid>CA</locationid>
    <groupby>location</groupby>
</get_accountbalancesbydimensions>
```

> The above function returns data structured like this:

```
<data>
    <accountbalance>
        <glaccountno>4000</glaccountno>
        <budgetbalance>150.00</budgetbalance>
        <periodbalance>100.00</periodbalance>
        <difference>50.00</difference>
        <currency>USD</currency>
        <locationid>CA</locationid>
    </accountbalance>
    ...
</data>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| reportingperiodname | Optional | string | Reporting period name. Required if not using `startdate` and `enddate`. |
| startdate | Optional | [object](https://developer.intacct.com/api/general-ledger/account-balances/#get_accountbalancesbydimensions.date) | Opening balance date. Required if not using `reportingperiodname`. |
| enddate | Optional | [object](https://developer.intacct.com/api/general-ledger/account-balances/#get_accountbalancesbydimensions.date) | Closing balance date. Required if not using `reportingperiodname`. |
| showperiodbalancedetail | Optional | boolean | Set to `true` to include the `periodbalancedetail` amounts in the response as well as the `periodbalance` amount. Can only be used when `contentselection` is set to `Actual`. |
| contentselection | Optional | string | Specifies the type of data to return. You can pull actual data (`Actual`), budget data (`Budget`) , or both (`Actual and Budget`). (Default: `Actual`) |
| budgetid | Optional | string | ID of a GL budget to use. Applicable when pulling budget data (`Budget`) or both actual-and-budget data (`Actual and Budget`). (Default: Uses the default budget for the company if configured) |
| budgetcomparison | Optional | string | Specifies how to compare actual data to budget data. Applicable when pulling both actual-and-budget data (`Actual and Budget`). Use `Budget minus Actual` or `Actual minus Budget`. (Default: `Budget minus Actual`) |
| showzerowithactivity | Optional | boolean | Specifies whether to show account activity even though the ending balance for the account is zero. Use `false` for No, `true` for Yes. (Default: `false`) |
| glaccountno | Optional | string | GL account number. Required if not using `accountgroupname` or `startaccountno` and `endaccountno`. |
| accountgroupname | Optional | string | Account group name. Required if not using `glaccountno` or `startaccountno` and `endaccountno`. |
| startaccountno | Optional | string | Starting GL account number. Required if not using `glaccountno` or `accountgroupname`. |
| endaccountno | Optional | string | Ending GL account number. Required if not using `glaccountno` or `accountgroupname`. |
| reportingbook | Optional | string | Reporting book ID. Reporting book ID. Use `ACCRUAL` or `CASH` depending on the company configuration. If Global Consolidations is enabled, you can provide a consolidation book ID instead. (Default: Configured reporting book ID) |
| adjbooks | Optional | array of `adjbook` | Adjustment book IDs for journals that are enabled in the GL configuration. Use `GAAP`, `TAX`, and/or the IDs of user defined books. Do not append text to the IDs. If you need help, look at the Account Balances page in the Sage Intacct UI to see what is enabled. |
| includereportingbook | Optional | boolean | Combine reporting book with other adjustment books. Use `true` to include the reporting book entries with entries from the specified adjustment books, or `false` to return only entries for the specified adjustment books. (Default: `false`) |
| statistical | Optional | string | Statistical accounts. Use either `include`, `exclude`, or `only`. (Default: `exclude`) |
| departmentid | Optional | string | Department ID or department group ID. (If you pass an empty element, no filtering is performed and all department data is listed.) |
| dept\_subs | Optional | boolean | Include department sub dimensions. (Default: `true`) |
| locationid | Optional | string | Location ID or location group ID. If you pass an empty element, no filtering is performed and all location data is listed. This field is required in a multi-base currency company. |
| loc\_subs | Optional | boolean | Include location sub dimensions. (Default: `true`) |
| projectid | Optional | string | Project ID or project group ID. |
| projectid\_subs | Optional | boolean | Include project sub dimensions. (Default: `true`) |
| projecttypeid | Optional | string | Project type. Do not use if project ID is set. |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| taskid\_subs | Optional | boolean | Include task sub dimensions. (Default: `true`) |
| costtypeid | Optional | string | Cost type ID. Only available when `taskid` is also specified. |
| costtypeid\_subs | Optional | boolean | Include cost type sub dimensions. (Default: `true`) |
| customerid | Optional | string | Customer ID or customer group ID |
| customerid\_subs | Optional | boolean | Include customer sub dimensions. (Default: `true`) |
| customertypeid | Optional | string | Customer type. Do not use if Customer ID is set. |
| vendorid | Optional | string | Vendor ID or vendor group ID |
| vendorid\_subs | Optional | boolean | Include vendor sub dimensions. (Default: `true`) |
| vendortypeid | Optional | string | Vendor type. Do not use if Vendor ID is set. |
| employeeid | Optional | string | Employee ID or employee group ID |
| employeeid\_subs | Optional | boolean | Include employee sub dimensions. (Default: `true`) |
| employeetypeid | Optional | string | Employee type. Do not use if Employee ID is set. |
| itemid | Optional | string | Item ID or item group ID |
| productlineid | Optional | string | Product line. Do not use if Item ID is set. |
| classid | Optional | string | Class ID or class group ID |
| classid\_subs | Optional | boolean | Include class sub dimensions. (Default: `true`) |
| contractid | Optional | string | Contract ID or contract group ID |
| contractid\_subs | Optional | boolean | Include contract sub dimensions. (Default: `true`) |
| warehouseid | Optional | string | Warehouse ID or warehouse group ID |
| warehouseid\_subs | Optional | boolean | Include warehouse sub dimensions. (Default: `true`) |
| userDefinedDimensions | Optional | array of [`userDefinedDimension`](https://developer.intacct.com/api/general-ledger/account-balances/#get_accountbalancesbydimensions.userDefinedDimension) | User defined dimensions to include |
| groupby | Optional | string | Comma-separated list of the names of standard and/or user-defined dimensions for grouping the results. |

`get_accountbalancesbydimensions.startdate`  
`get_accountbalancesbydimensions.enddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`get_accountbalancesbydimensions.userDefinedDimension`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| objectName | Required | string | UDD object integration name. |
| recordId | Optional | string | UDD record ID. Do not use if Record name is set. |
| recordName | Optional | string | UDD record name. Do not use if Record ID set. If UDD name is not unique, must use record ID instead. |

* * *

List Account Balances by Dimensions, Asynchronous
-------------------------------------------------

If your Account Balances by Dimensions report contains a lot of data, or if processing your report times out, you can use a `readReport` request to generate your report asynchronously and then get the report when it is ready.

> Asynchronous version of the first example, to list balances for a range of accounts for a date range, and group by location and department:

```
<readReport type="STANDARD" returnDef="false">
    <report>get_accountbalancesbydimensions</report>
    <arguments>
        <get_accountbalancesbydimensions>
            <startdate>
                <year>2016</year>
                <month>01</month>
                <day>01</day>
            </startdate>
            <enddate>
                <year>2016</year>
                <month>12</month>
                <day>31</day>
            </enddate>
            <startaccountno>4000</startaccountno>
            <endaccountno>4999</endaccountno>
            <locationid>1</locationid>
            <groupby>location,department</groupby>
        </get_accountbalancesbydimensions>
    </arguments>
    <pagesize>5</pagesize>
</readReport>
```

#### `readReport`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| type (attribute) | Required | string | Report type. Use `STANDARD`. |
| returnDef (attribute) | Required | boolean | Use `false`. |
| report | Required | string | Name of the report to run. Use `get_accountbalancesbydimensions`. |
| arguments | Required | varies | An outer element containing the name of the report, and inner elements containing input values for the report, in the same format as for the [synchronous report](https://developer.intacct.com/api/general-ledger/account-balances/#get_accountbalancesbydimensions-synchronous). |
| pagesize | Optional | integer | The number of `data` objects to return in each response. (Max: `1000`, Default: `100`) |

### Synchronous Response

`reportId`

> The system returns a unique report ID that you can use in a `readMore` request to retrieve the report:

```
<report_results>
  <REPORTID>YT_jBmIqoVXBFGLNjSVwIPCIIuJa9IKKqQ_Fq9T8PSbonJrnXZl1a2gO0dcby349</REPORTID>
  <STATUS>PENDING</STATUS>
</report_results>
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| reportId | string | Report ID to use in `readMore` requests to [retrieve the report](https://developer.intacct.com/api/general-ledger/account-balances/#retrieve-the-asynchronous-report). |

* * *

### Retrieve the Asynchronous Report

You use the reportId in a `readReport` response to retrieve the status of a report and the report itself.

> Request a report:

```
<readMore>
    <reportId>k267Hj5x93gGrmQ12I4n6z457f83bZh3</reportId>
</readMore>
```

#### `readMore`

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| reportId | Required | string | Report ID from a `readReport` response. |

If the `STATUS` in the response is `PENDING`, wait a little while and then send the request again. When the report is ready, the first page will be returned in the response.

Note the `numremaining` attribute of the `data` element in the response. If the value is not `0`, there is more data to retrieve and you should continue sending `readMore` requests until you have retrieved all of the pages.

```

<data listtype="report" count="5" totalcount="26" **numremaining="21"**>
```

When you retrieve the last page of a report, the system deletes the entire report. To get the report a second time, you must send the original `readReport` request again to generate a new report ID.

* * *

Get Raw Account Balance Object Definition
-----------------------------------------

#### `lookup`

> List all the fields and relationships for the raw account balance object:

```
<lookup>
    <object>GLACCOUNTBALANCE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNTBALANCE` |

* * *

Query and List Raw Account Balances
-----------------------------------

[History](https://developer.intacct.com/api/general-ledger/account-balances/#history-readbyquery)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | Added TASKID |

Raw account balances include an opening balance, for period/net change amounts, ending balance, and adjustments together with all book and dimension combinations. This data can be very complex and requires intricate Sage Intacct financial reporting knowledge in order to list the appropriate data so that it represents that of the Sage Intacct Account Balance standard report and Financial Report Writer.

There can be performance issues as well, since filtering–let’s say for a single GL account–may actually return thousands of records since it includes all combinations of transaction and base currencies, reporting books, and all dimensions. This list also does not roll up parent-child hierarchical balances nor allow for filtering by a parent. You also need an understanding of how multiple base currency entities and consolidation books work, so you can properly filter out the transactional currency amounts—you should likely run the list slide from the [context of an entity](https://developer.intacct.com/web-services/requests/#authentication-element) and not the top shared level.

**Note:** Using the legacy function above is recommended instead—it provides information in a summarized format similar to that provided by the Sage Intacct Account Balance standard report and Financial Report Writer.

#### `readByQuery`

> List raw account balances for the given period:

```
<readByQuery>
    <object>GLACCOUNTBALANCE</object>
    <fields>*</fields>
    <query>PERIOD = 'Month Ended June 2016'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List raw account balances for the given period, excluding entries with the specified zero balances:

```
<readByQuery>
    <object>GLACCOUNTBALANCE</object>
    <fields>*</fields>
    <query>PERIOD = 'Month Ended May 2017' AND NOT (TOTDEBIT = 0 AND TOTCREDIT = 0 AND TOTADJDEBIT = 0 AND TOTADJCREDIT = 0 AND FORBAL = 0 AND ENDBAL = 0)</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCOUNTBALANCE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. Must provide `PERIOD` as a parameter. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PERIOD | Required | string | Budgetable reporting period name. These are the reporting periods shown on the Reporting Periods list with the **budgetable** flag set to `true`. System periods (Today, Current Month, Current Year to Date, etc) and non-budgetable reporting periods are **not** supported. |
| BOOKID | Optional | string | Reporting book ID. System standard book IDs include `ACCRUAL`, `CASH`, `GAAPADJACCRUAL`, `GAAPADJCASH`, `TAXADJACCRUAL`, `TAXADJCASH`, `GAAPACCRUAL`, `GAAPCASH`, `TAXACCRUAL`, `TAXCASH`, `GAAPTAXACCRUAL`, and `GAAPTAXCASH`. Keep in mind, these are dependent on the company/GL configuration. In addition to these, a Sage Intacct company may also have User Defined Books and/or Consolidation books. In the case of User Defined Books, the system appends `ACCRUAL` and `CASH` to the end of the User Defined Book ID to come up with the appropriate Book ID for GL Account Balances. For example, a UDB setup with the ID of `TEST` would have balances using the book IDs `TESTACCRUAL` and `TESTCASH`. |
| CURRENCY | Optional | string | Currency code.
*   If the company is multi-currency and the request is run at the top level, your list will contain all currencies and not just the base. You should run the request privately in an entity or provide a currency filter with the base currency and whatever entity/location hierarchy is needed.
*   If the base and transaction currency are different, filter for the base currency or both amounts will be included in response even if running from the entity.

 |
| OPENBAL | Optional | currency | Opening account balance |
| TOTDEBIT | Optional | currency | Total debits |
| TOTCREDIT | Optional | currency | Total credits |
| TOTADJDEBIT | Optional | currency | Total adjusting debits |
| TOTADJCREDIT | Optional | currency | Total adjusting credits |
| FORBAL | Optional | currency | For period account balance (debits - credits) |
| ENDBAL | Optional | currency | Ending account account balance (opening + debits - credits) |
| WHENCREATED | Optional | string | When the account balance was created in `mm/dd/yyyy hh:mm:ss` format |
| WHENMODIFIED | Optional | string | When the account balance was last modified in `mm/dd/yyyy hh:mm:ss` format |
| CREATEDBY | Optional | integer | User record number that created the account balance |
| MODIFIEDBY | Optional | integer | User record number that last modified the account balance |
| ACCOUNTREC | Optional | integer | Account record number |
| ACCOUNTNO | Optional | string | Account number |
| ACCOUNTTITLE | Optional | string | Account title |
| DEPARTMENTDIMKEY | Optional | integer | Department record number |
| DEPARTMENTID | Optional | string | Department ID |
| DEPARTMENTTITLE | Optional | string | Department title |
| LOCATIONDIMKEY | Optional | integer | Location record number |
| LOCATIONID | Optional | string | Location ID. This field is required in a multi-base currency company. |
| LOCATIONNAME | Optional | string | Location name |
| PROJECTDIMKEY | Optional | integer | Project record number |
| PROJECTID | Optional | string | Project ID |
| PROJECTNAME | Optional | string | Project name |
| TASKID | Optional | string | Task ID |
| COSTTYPEID | Optional | string | Cost type ID |
| CUSTOMERDIMKEY | Optional | integer | Customer record number |
| CUSTOMERID | Optional | string | Customer ID |
| CUSTOMERNAME | Optional | string | Customer name |
| VENDORDIMKEY | Optional | integer | Vendor record number |
| VENDORID | Optional | string | Vendor ID |
| VENDORNAME | Optional | string | Vendor name |
| EMPLOYEEDIMKEY | Optional | integer | Employee record number |
| EMPLOYEEID | Optional | string | Employee ID |
| EMPLOYEENAME | Optional | string | Employee name |
| ITEMDIMKEY | Optional | integer | Item record number |
| ITEMID | Optional | string | Item ID |
| ITEMNAME | Optional | string | Item name |
| WAREHOUSEDIMKEY | Optional | integer | Warehouse record number |
| WAREHOUSEID | Optional | string | Warehouse ID |
| WAREHOUSENAME | Optional | string | Warehouse name |
| CLASSDIMKEY | Optional | integer | Class record number |
| CLASSID | Optional | string | Class ID |
| CLASSNAME | Optional | string | Class name |
| CONTRACTDIMKEY | Optional | integer | Contract record number |
| CONTRACTID | Optional | string | Contract ID |
| CONTRACTNAME | Optional | string | Contract name |
| GLDIM\* | Optional | integer | User defined dimension `id` field. UDD object integration name usually appended to `GLDIM` |

#### Tips

If you only need to list the changes to account balances, you can use something like `WHENMODIFIED &gt;= '04/19/2017 12:00:00'` as part of your query.

Consider excluding fields you don’t need in order to avoid the underlying table joins in the Sage Intacct system. For example, query for `DEPARTMENTDIMKEY` instead of `DEPARTMENTID` and `DEPARTMENTNAME`. Then query `DEPARTMENTID` and `DEPARTMENTNAME` separately and join them in your system with the `DEPARTMENTDIMKEY`.

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

