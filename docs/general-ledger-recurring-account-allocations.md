Title: Recurring Account Allocations

URL Source: https://developer.intacct.com/api/general-ledger/recurring-account-allocations/

Markdown Content:
*   [Get Recurring Account Allocation Object Definition](https://developer.intacct.com/api/general-ledger/recurring-account-allocations/#get-recurring-account-allocation-object-definition)
*   [Query and List Recurring Account Allocations](https://developer.intacct.com/api/general-ledger/recurring-account-allocations/#query-and-list-recurring-account-allocations)
*   [Query and List Recurring Account Allocations (Legacy)](https://developer.intacct.com/api/general-ledger/recurring-account-allocations/#query-and-list-recurring-account-allocations-legacy)
*   [Get Recurring Account Allocation](https://developer.intacct.com/api/general-ledger/recurring-account-allocations/#get-recurring-account-allocation)
*   [Create Recurring Account Allocation](https://developer.intacct.com/api/general-ledger/recurring-account-allocations/#create-recurring-account-allocation)
*   [Delete Recurring Account Allocation](https://developer.intacct.com/api/general-ledger/recurring-account-allocations/#delete-recurring-account-allocation)

* * *

You can set up recurring account allocations to automatically distribute amounts across multiple dimensions according to a schedule you define.

There are two models for setting up the recurring allocation:

*   Run the recurring allocation for a given number of occurrences
*   Run the recurring allocation until a given date

You can set up recurrence for an account allocation or an account allocation group.

Your company must have a subscription for Dynamic Allocations, and you need the appropriate permissions for account allocations.

* * *

Get Recurring Account Allocation Object Definition
--------------------------------------------------

#### `lookup`

> List all the fields and relationships for the recurring account allocation object:

```
<lookup>
    <object>RECURGLACCTALLOCATION</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RECURGLACCTALLOCATION` |

* * *

Query and List Recurring Account Allocations
--------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and plan name for each recurring account allocation:

```
<query>
    <object>RECURGLACCTALLOCATION</object>
    <select>
        <field>RECORDNO</field>
        <field>PLANNAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RECURGLACCTALLOCATION` |
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

Query and List Recurring Account Allocations (Legacy)
-----------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>RECURGLACCTALLOCATION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RECURGLACCTALLOCATION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Recurring Account Allocation
--------------------------------

#### `read`

```
<read>
    <object>RECURGLACCTALLOCATION</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RECURGLACCTALLOCATION` |
| keys | Required | string | Comma-separated list of recurring account allocation `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Recurring Account Allocation
-----------------------------------

#### `create`

> Creates an ongoing recurring account allocation that runs every month:

```
<create>
    <RECURGLACCTALLOCATION>
        <PLANNAME>monthlyOngoing - Alloc 02</PLANNAME>
        <STARTDATE>04/01/2019</STARTDATE>
        <ENDINGON>Never</ENDINGON>
        <REPEATBY>Months</REPEATBY>
        <REPEATINTERVAL>1</REPEATINTERVAL>
        <ISPERIODEND>true</ISPERIODEND>
        <EMAIL>noreply@intacct.com</EMAIL>
        <GLACCTALLOCATION>Allocation 02</GLACCTALLOCATION>
    </RECURGLACCTALLOCATION>
</create>
```

> Creates a recurring account allocation that ends after two occurrences:

```
<create>
    <RECURGLACCTALLOCATION>
        <PLANNAME>Rebalance - Alloc 05</PLANNAME>
        <STARTDATE>04/01/2019</STARTDATE>
        <ENDINGON>Number of Occurrences</ENDINGON>
        <OCCURRENCES>2</OCCURRENCES>
        <EMAIL>noreply@intacct.com</EMAIL>
        <GLACCTALLOCATION>Allocation 02</GLACCTALLOCATION>
    </RECURGLACCTALLOCATION>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RECURGLACCTALLOCATION` |

`RECURGLACCTALLOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PLANNAME | Required | string | Name for the recurring allocation |
| STARTDATE | Required | string | Journal entry start date in format `mm/dd/yyyy`. |
| ENDINGON | Required | string | Ending on. Use `Never`, `Number of Occurrences`, or `End Date` |
| ENDDATE | Optional | string | End on date. Valid when `ENDINGON` is set to `End Date`. |
| OCCURRENCES | Optional | string | End After the given number of occurrences. Valid when `ENDINGON` is set to `Number of Occurrences`. |
| REPEATBY | Required | string | Repeat by period. Use `None`, `Days`, `Weeks`, `Months`, or `Years`. |
| REPEATINTERVAL | Required | integer | Every. Value to indicate the interval for the Repeat by period. For example, if `REPEAT` is set to `Months`, a value of 3 for `REPEATINTERVAL` means the allocation runs every 3 months. A value of 1 means the allocation runs monthly. |
| ISPERIODEND | Optional | boolean | Allocate through period end. Use `true` to specify that the recurring allocation will run on the day following the end of selected period, which ensures all entries for the period are considered in the allocation. Sage Intacct will use an As Of Date and a GL Posting date that corresponds to the last day of the period. Use `false` otherwise. (Default: false). |
| EMAIL | Required | string | Email address for success or failure notification |
| GLACCTALLOCATION | Optional | string | Account allocation ID. Required if not using `GLACCTALLOCATIONGRP`. |
| GLACCTALLOCATIONGRP | Optional | string | Group name for the account allocation group. Required if not using `GLACCTALLOCATION`. |

* * *

Delete Recurring Account Allocation
-----------------------------------

#### `delete`

```
<delete>
    <object>RECURGLACCTALLOCATION</object>
    <keys>1</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RECURGLACCTALLOCATION` |
| keys | Required | string | Comma-separated list of recurring account allocation `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

