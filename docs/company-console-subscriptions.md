Title: Subscriptions

URL Source: https://developer.intacct.com/api/company-console/subscriptions/

Markdown Content:
*   [List Subscriptions](https://developer.intacct.com/api/company-console/subscriptions/#list-subscriptions)
*   [List Subscription Preferences](https://developer.intacct.com/api/company-console/subscriptions/#list-subscription-preferences)

* * *

Subscriptions are the financial management applications offered by Sage Intacct.

* * *

#### `get_applications`

```
<get_applications/>
```

#### Parameters

#### `Response`

> The above function returns data structured like this:

```
<data>
    <application>CO</application>
    <application>CM</application>
    <application>GL</application>
    <application>AP</application>
</data>
```

* * *

List Subscription Preferences
-----------------------------

#### `get_companyprefs`

> Lists preferences for the General Ledger application:

```
<get_companyprefs application="GL"/>
```

> The above function returns data structured like this:

```
<companypref>
    <application>GL</application>
    <preference>EMPLOYEEDIMENSION</preference>
    <prefvalue>T</prefvalue>
</companypref>
```

> Lists preferences for general accounting information for the company:

```
<get_companyprefs application="GEN"/>
```

> The above function returns data structured like this:

```
<companypref>
   <application>GEN</application>
   <preference>PRIMARY_ACCTNO_LENGTH</preference>
   <prefvalue>4</prefvalue>
</companypref>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| application | Required | string | Subscription to list preferences for. Use `GEN` for General Company Info, `ME` for Multi-Entity, `GL` for General Ledger, `CM` for Cash Management, `AP` for Accounts Payable, `AR` for Accounts Receivable, `EE` for Employee Expenses, `PO` for Purchasing, `SO` for Order Entry, `INV` for Inventory Control, `PA` for Projects, `CS` for Global Consolidations. |

#### `Response`

When supplying `GEN` to return company information, the response includes the following data:

| Name | Description |
| --- | --- |
| PRIMARY\_ACCTNO\_LENGTH | Length of the primary account number. |
| ACCTNO\_SEPARATOR | Separator for the account number. |
| SUBACCTNO\_LENGTH | Length of the sub account number. |
| FISCAL\_FIRST\_MONTH | First fiscal month. 1 for January. |
| FISCAL\_FIRST\_MONTH\_TAX | First fiscal tax month. 1 for January. |
| WEEK\_START | Day of the week. 1 for Sunday. |
| CUSTOM\_ACCOUNTING\_PERIODS | Specifies whether custom accounting periods are enabled. |
| PACKAGE\_TYPE | Ignore this value. |

**Note:** Be aware that FISCAL\_FIRST\_MONTH, FISCAL\_FIRST\_MONTH\_TAX, and WEEK\_START for the company can be overridden at the entity level.

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

