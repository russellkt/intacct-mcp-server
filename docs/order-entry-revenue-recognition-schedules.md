Title: Revenue Recognition Schedules

URL Source: https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/

Markdown Content:
*   [Revenue Recognition Schedules](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#revenue-recognition-schedules)
    *   [Get Revenue Recognition Schedule Object Definition](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#get-revenue-recognition-schedule-object-definition)
    *   [Query and List Revenue Recognition Schedules](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#query-and-list-revenue-recognition-schedules)
    *   [Get Revenue Recognition Schedule](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#get-revenue-recognition-schedule)
    *   [Hold Revenue Recognition Schedule (Legacy)](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#hold-revenue-recognition-schedule-legacy)
    *   [Resume Revenue Recognition Schedule (Legacy)](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#resume-revenue-recognition-schedule-legacy)
    *   [Terminate Revenue Recognition Schedule (Legacy)](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#terminate-revenue-recognition-schedule-legacy)
    *   [Update Revenue Recognition Schedule (Legacy)](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#update-revenue-recognition-schedule-legacy)
    *   [Reallocate Revenue Recognition Schedule (Legacy)](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#reallocate-revenue-recognition-schedule-legacy)
*   [Revenue Recognition Schedule Entries](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#revenue-recognition-schedule-entries)
    *   [Get Revenue Recognition Schedule Entry Object Definition](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#get-revenue-recognition-schedule-entry-object-definition)
    *   [Query and List Revenue Recognition Schedule Entries](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#query-and-list-revenue-recognition-schedule-entries)
    *   [Get Revenue Recognition Schedule Entry](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#get-revenue-recognition-schedule-entry)
    *   [Post Revenue Recognition Schedule Entries (Legacy)](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#post-revenue-recognition-schedule-entries-legacy)
    *   [Unpost Revenue Recognition Schedule Entries (Legacy)](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#unpost-revenue-recognition-schedule-entries-legacy)

* * *

Revenue recognition schedules track revenue deferred from Accounts Receivable or Order Entry sales transactions.

The system generates revenue recognition schedules for applicable posted sales transactions containing items with associated revenue recognition templates.

* * *

### Get Revenue Recognition Schedule Object Definition

#### `lookup`

> List all the fields and relationships for the revenue recognition schedule object:

```
<lookup>
    <object>REVRECSCHEDULE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REVRECSCHEDULE` |

* * *

### Query and List Revenue Recognition Schedules

#### `readByQuery`

```
<readByQuery>
    <object>REVRECSCHEDULE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REVRECSCHEDULE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`). |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCENTRYKEY | Optional | string | `RECORDNO` for the `SODOCUMENTENTRY` with the revenue recognition schedule to list |
| STATUS | Optional | string | Status of the revenue recognition schedule. Use `N` for Not Started, `P` for In Progress, `C` for Completed, `H` for On Hold, `D` for Terminated, or `X` for Partially Terminated. |
| REVRECTEMPLATEID | Optional | string | ID of revenue recognition template |
| RECMETHOD | Optional | string | Revenue recognition method. Use `E` for Straight line, `S` for Straight-line, prorate exact days, `P` for Straight-line, percent allocation, `F` for Straight-line, percent allocation, end of period, `X` for Exact days per period, prorate days, `D` for Exact days per period, prorate days, end of period, `T` for Percent Completed, `M` for Milestone, or `C` for Custom. |

* * *

### Get Revenue Recognition Schedule

#### `read`

```
<read>
    <object>REVRECSCHEDULE</object>
    <keys>121</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REVRECSCHEDULE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the revenue recognition schedule to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Hold Revenue Recognition Schedule (Legacy)

#### `hold_revrecschedule`

```
<hold_revrecschedule>
    <recordno>121</recordno>
    <category></category>
    <memo></memo>
</hold_revrecschedule>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of a revenue recognition schedule whose status is Not started (`N`), In progress (`P`), or Partially terminated (`X`). |
| category | Optional | string | Category defining the reason for the hold. Use `Collectability`, `Delivery Commitment`, `Dispute`, `Legal`, or `Cancelled Service`. |
| memo | Optional | string |   |

* * *

### Resume Revenue Recognition Schedule (Legacy)

#### `resume_revrecschedule`

```
<resume_revrecschedule>
    <recordno>121</recordno>
    <adjustpostingday>true</adjustpostingday>
    <memo></memo>
</resume_revrecschedule>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of a revenue recognition schedule whose status is On hold (`H`) |
| adjustpostingday | Required | boolean | Use `true` to specify that unposted scheduled journal entries will be entered using the next posting date in the schedule. |
| memo | Optional | string |   |

* * *

### Terminate Revenue Recognition Schedule (Legacy)

#### `terminate_revrecschedule`

```
<terminate_revrecschedule>
    <recordno>12</recordno>
    <category></category>
    <memo></memo>
</terminate_revrecschedule>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of a revenue recognition schedule whose STATUS is either Not Started (`N`), In Progress (`P`), Partially terminated (`X`), or On hold (H). |
| category | Optional | string | Category defining the reason for the termination. Use `Collectability`, `Delivery Commitment`, `Dispute`, `Legal`, or `Cancelled Service`. |
| memo | Optional | string |   |

* * *

### Update Revenue Recognition Schedule (Legacy)

#### `update_revrecschedule`

```
<update_revrecschedule>
    <recordno>121</recordno>
    <memo></memo>
    <revrecentries>
        <revrecentry>
            <recordno>396</recordno>
            <postingdate>
                <year>2017</year>
                <month>8</month>
                <day>21</day>
            </postingdate>
            <accountno>4010</accountno>
            <trx_amount>4513.89</trx_amount>
        </revrecentry>
    </revrecentries>
</update_revrecschedule>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of the revenue recognition schedule to update |
| memo | Optional | string |   |
| revrecentries | Required | revrecentry\[1…n\]\` | One or more entries to update |

`revrecentry`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of the revenue recognition schedule entry to update |
| postingdate | Required | object | Posting date |
| accountno | Required | string | Revenue account number |
| trx\_amount | Required | currency | Total transaction amount for the revenue recognition schedule |
| cumpercent | Optional | decimal | Cumulative Percent Complete |
| description | Optional | string | Description |

`postingdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

### Reallocate Revenue Recognition Schedule (Legacy)

[History](https://developer.intacct.com/api/order-entry/revenue-recognition-schedules/#history-reallocate_revrecschedule)

| Release | Changes |
| --- | --- |
| 2018 Release 2 | Added unpostall |

#### `reallocate_revrecschedule`

```
<reallocate_revrecschedule>
    <recordno>12</recordno>
    <revrecstartdate>
        <year>2014</year>
        <month>10</month>
        <day>31</day>
    </revrecstartdate>
    <revrecenddate>
        <year>2014</year>
        <month>10</month>
        <day>31</day>
    </revrecenddate>
</reallocate_revrecschedule>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of the revenue recognition schedule to reallocate |
| revrecstartdate | Required | object | Start date for the schedule |
| revrecenddate | Required | object | End date for the schedule |
| unpostall | Optional | boolean | Applicable only for Order Entry revenue recognition schedules. Specifies whether to unpost all posted entries so that the entire revenue recognition schedule can be reallocated to the given period. Use `true` to enable this, `false` otherwise. |

`revrecstartdate`/`revrecenddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Revenue Recognition Schedule Entries
------------------------------------

### Get Revenue Recognition Schedule Entry Object Definition

#### `lookup`

> List all the fields and relationships for the revenue recognition schedule entry object:

```
<lookup>
    <object>REVRECSCHEDULEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REVRECSCHEDULEENTRY` |

* * *

### Query and List Revenue Recognition Schedule Entries

#### `readByQuery`

```
<readByQuery>
    <object>REVRECSCHEDULEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List the revenue recognition schedule for the SODOCUMENTENTRY whose RECORDNO is 21:

```
<readByQuery>
    <object>REVRECSCHEDULEENTRY</object>
    <fields>*</fields>
    <query>DOCENTRYKEY = 21</query> <!--From the originating SODOCUMENT-->
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REVRECSCHEDULEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCENTRYKEY | Optional | string | `RECORDNO` for the `SODOCUMENTENTRY` with the revenue recognition schedule entries to list |

* * *

### Get Revenue Recognition Schedule Entry

#### `read`

```
<read>
    <object>REVRECSCHEDULEENTRY</object>
    <keys>43</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REVRECSCHEDULEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the revenue recognition schedule entry to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Post Revenue Recognition Schedule Entries (Legacy)

#### `post_revrecscheduleentry`

```
<post_revrecscheduleentry>
    <recordno>1670</recordno>
</post_revrecscheduleentry>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of the revenue recognition schedule entry to post |
| postcurrencygainandloss | Optional | boolean | Use `true` to post currency gains and losses based on the date you post the entry |
| exchratetype | Optional | string | Exchange rate type. Set this parameter when `postcurrencygainandloss` is set to `true`. |

* * *

### Unpost Revenue Recognition Schedule Entries (Legacy)

#### `unpost_revrecscheduleentry`

```
<unpost_revrecscheduleentry>
    <recordno>1670</recordno>
</unpost_revrecscheduleentry>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | string | `RECORDNO` of the revenue recognition schedule entry to unpost |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

