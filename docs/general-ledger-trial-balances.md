Title: Trial Balances

URL Source: https://developer.intacct.com/api/general-ledger/trial-balances/

Markdown Content:
*   [List Trial Balances (Legacy)](https://developer.intacct.com/api/general-ledger/trial-balances/#list-trial-balances-legacy)

* * *

Use trial balances to view balances of all accounts in specific reporting periods or date ranges.

* * *

List Trial Balances (Legacy)
----------------------------

[History](https://developer.intacct.com/api/general-ledger/trial-balances/#history-get_trialbalance)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | Added taskid, taskid\_subs |
| 2023 Release 1 | Added debitcreditbalance option |

#### `get_trialbalance`

> List trial balances for a reporting period, including debit and credit starting balances:

```
<get_trialbalance>
    <reportingperiodname>Calendar Year Ended December 2022</reportingperiodname>
    <showzerobalances>false</showzerobalances>
    <showdeptdetail>false</showdeptdetail>
    <showlocdetail>false</showlocdetail>
    <debitcreditbalance>true</debitcreditbalance>
</get_trialbalance>
```

> List trial balances for a date range:

```
<get_trialbalance>
    <startdate>
        <year>2022</year>
        <month>01</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2022</year>
        <month>01</month>
        <day>31</day>
    </enddate>
    <showzerobalances>false</showzerobalances>
    <showdeptdetail>false</showdeptdetail>
    <showlocdetail>false</showlocdetail>
</get_trialbalance>
```

> List trial balances for GAAP adjustment accrual books:

```
<get_trialbalance>
    <startdate>
        <year>2022</year>
        <month>11</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2022</year>
        <month>11</month>
        <day>30</day>
    </enddate>
    <reportingbook>ACCRUAL</reportingbook>
    <adjbooks>
        <adjbook>GAAP</adjbook>
    </adjbooks>
    <includereportingbook>false</includereportingbook>
    <statistical>exclude</statistical>
    <locationid>100</locationid>
</get_trialbalance>
```

> List trial balances for GAAP adjustment accrual and a user-defined book `OBL`:

```
<get_trialbalance>
    <startdate>
        <year>2022</year>
        <month>11</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2022</year>
        <month>11</month>
        <day>30</day>
    </enddate>
    <reportingbook>ACCRUAL</reportingbook>
    <adjbooks>
        <adjbook>GAAP</adjbook>
        <adjbook>OBL</adjbook>
    </adjbooks>
    <includereportingbook>false</includereportingbook>
    <statistical>exclude</statistical>
    <locationid>100</locationid>
</get_trialbalance>
```

> List trial balances for the `USDCONS` global consolidation book across all entities:

```
<get_trialbalance>
    <startdate>
        <year>2022</year>
        <month>11</month>
        <day>01</day>
    </startdate>
    <enddate>
        <year>2022</year>
        <month>11</month>
        <day>30</day>
    </enddate>
    <reportingbook>USDCONS</reportingbook>
    <includereportingbook>true</includereportingbook>
    <statistical>exclude</statistical>
</get_trialbalance>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| reportingperiodname | Optional | string | Reporting period name. Required if not using `startdate` and `enddate`. |
| startdate | Optional | [object](https://developer.intacct.com/api/general-ledger/trial-balances/#get_trialbalance.date) | Opening balance date. Required if not using `reportingperiodname`. |
| enddate | Optional | [object](https://developer.intacct.com/api/general-ledger/trial-balances/#get_trialbalance.date) | Closing balance date. Required if not using `reportingperiodname`. |
| debitcreditbalance | Optional | boolean | Set to `true` to show starting and ending balance debits and credits. (Default: `false`) |
| showzerobalances | Optional | boolean | Show zero balance accounts. Use `true` or `false`. (Default: `false`) |
| showdeptdetail | Optional | boolean | Expand department detail. Use `true` or `false`. (Default: `false`) |
| showlocdetail | Optional | boolean | Expand location detail. Use `true` or `false`. (Default: `false`) |
| reportingbook | Optional | string | Reporting book ID. Use `ACCRUAL` or `CASH` depending on the company configuration. If Global Consolidations is enabled, you can provide a consolidation book ID instead. (Default: Configured reporting book ID) |
| adjbooks | Optional | array of `adjbook` | Adjustment book IDs for journals that are enabled in the GL configuration. Use `GAAP`, `TAX`, and/or the IDs of user defined books. Do not append text to the IDs. If you need help, look at the Trial Balance page in the Sage Intacct UI to see what is enabled. |
| includereportingbook | Optional | boolean | Combine reporting book with other adjustment books. Use `true` to include the reporting book entries with entries from the specified adjustment books, or `false` to return only entries for the specified adjustment books. |
| statistical | Optional | string | Statistical accounts. Use either `include`, `exclude`, or `only`. (Default: `include`) |
| departmentid | Optional | string | Department ID. |
| dept\_subs | Optional | boolean | Include department subs. (Default: `true`) |
| locationid | Optional | string | Location ID. This field is required in a multi-base currency company. |
| loc\_subs | Optional | boolean | Include location subs. (Default: `true`) |
| projectid | Optional | string | Project ID or project group ID. |
| projectid\_subs | Optional | boolean | Include project subs. (Default: `true`) |
| projecttypeid | Optional | string | Project type. Do not use if Project ID is set. |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| taskid\_subs | Optional | boolean | Include task sub dimensions. (Default: `true`) |
| customerid | Optional | string | Customer ID or customer group ID. |
| customerid\_subs | Optional | boolean | Include customer subs. (Default: `true`) |
| customertypeid | Optional | string | Customer type. Do not use if Customer ID is set. |
| vendorid | Optional | string | Vendor ID or vendor group ID. |
| vendorid\_subs | Optional | boolean | Include vendor subs. (Default: `true`) |
| vendortypeid | Optional | string | Vendor type. Do not use if Vendor ID is set. |
| employeeid | Optional | string | Employee ID or employee group ID. |
| employeeid\_subs | Optional | boolean | Include employee subs. (Default: `true`) |
| employeetypeid | Optional | string | Employee type. Do not use if Employee ID is set. |
| itemid | Optional | string | Item ID or item group ID. |
| productlineid | Optional | string | Product line. Do not use if Item ID is set. |
| classid | Optional | string | Class ID or class group ID. |
| classid\_subs | Optional | boolean | Include class subs. (Default: `true`) |
| contractid | Optional | string | Contract ID or contract group ID. |
| contractid\_subs | Optional | boolean | Include contract subs. (Default: `true`) |
| warehouseid | Optional | string | Warehouse ID or warehouse group ID. |
| warehouseid\_subs | Optional | boolean | Include warehouse subs. (Default: `true`) |
| userDefinedDimensions | Optional | array of `userDefinedDimension` | User defined dimension filters. |

`startdate`  
`enddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`userDefinedDimension`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| objectName | Required | string | UDD object integration name. |
| recordId | Optional | string | UDD record ID. Do not use if `recordName` is set. Required if UDD `objectName` is not unique. |
| recordName | Optional | string | UDD record name. Do not use if `recordId` set. If UDD `objectName` is not unique, must use record ID instead. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

