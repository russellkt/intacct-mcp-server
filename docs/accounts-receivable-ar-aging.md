Title: AR Aging

URL Source: https://developer.intacct.com/api/accounts-receivable/ar-aging/

Markdown Content:
*   [List Accounts Receivable Aging](https://developer.intacct.com/api/accounts-receivable/ar-aging/#list-accounts-receivable-aging)
*   [List Accounts Receivable Aging (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-aging/#list-accounts-receivable-aging-legacy)

* * *

AR aging refers to how many days it took customers to pay you or how many days past due their payments are.

* * *

List Accounts Receivable Aging
------------------------------

Detailed AR aging information can be obtained by creating a [custom report](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=TOC_custom_reports) on the Customer AR Aging object. From the API, you would then [run the custom report](https://developer.intacct.com/api/customization-services/custom-reports/#run-an-original-custom-report).

* * *

List Accounts Receivable Aging (Legacy)
---------------------------------------

#### `get_araging`

> Get an aging report for several aging periods:

```
<get_araging>
    <agingperiods>31-60,61-90,91-120,121-</agingperiods>
    <customerid></customerid>
    <showdetails>true</showdetails>
</get_araging>
```

> Specify a date from which to report aging based on invoice due dates:

```
<get_araging>
    <agingperiods>31-60,61-90,91-120,121-</agingperiods>
    <asofdate>
        <year>2021</year>
        <month>06</month>
        <day>31</day>
    </asofdate>
    <useduedate>true</useduedate>
    <showdetails>true</showdetails>
</get_araging>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| agingperiods | Optional | string | Aging period. Use a comma-separated list of aging periods that do not overlap. The default is `0-30,31-60,61-90,91-120,121-`. |
| customerid | Optional | string | Customer ID |
| invoiceno | Optional | string | Invoice number |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| asofdate | Optional | object | Date on which to calculate aging information (Default: today’s date) |
| useduedate | Optional | boolean | Use `true` to generate aging information based on the invoice due date or `false` to use the invoice creation date (Default: `false`) |
| showdetails | Optional | boolean | Use `true` to include details in the output (Default: `false`) |
| useglpostdate | Optional | boolean | Use `true` to generate aging information based on the GL posting date |
| showzerowithactivity | Optional | boolean | Use `true` to include customers with a zero balance in the output |

`asofdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

