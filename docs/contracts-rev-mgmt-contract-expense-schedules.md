Title: Contract Expense Schedules

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/

Markdown Content:
*   [Contract Expense Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#contract-expense-schedules)
    *   [Get Contract Expense Schedule Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#get-contract-expense-schedule-object-definition)
    *   [Query and List Contract Expense Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#query-and-list-contract-expense-schedules)
    *   [Query and List Contract Expense Schedules (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#query-and-list-contract-expense-schedules-legacy)
    *   [Get Contract Expense Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#get-contract-expense-schedule)
    *   [Reallocate Contract Expense Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#reallocate-contract-expense-schedule)
    *   [Post Contract Expense Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#post-contract-expense-schedule)
*   [Contract Expense Schedule Entries](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#contract-expense-schedule-entries)
    *   [Post Contract Expense Schedule Entry](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#post-contract-expense-schedule-entry)
    *   [Unpost Contract Expense Schedule Entry](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#unpost-contract-expense-schedule-entry)
*   [Contract Expense 2 Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#contract-expense-2-schedules)
    *   [Get Contract Expense 2 Schedule Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#get-contract-expense-2-schedule-object-definition)
    *   [Query and List Contract Expense 2 Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#query-and-list-contract-expense-2-schedules)
    *   [Query and List Contract Expense 2 Schedules (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#query-and-list-contract-expense-2-schedules-legacy)
    *   [Get Contract Expense 2 Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#get-contract-expense-2-schedule)
    *   [Post Contract Expense 2 Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#post-contract-expense-2-schedule)
    *   [Reallocate Contract Expense 2 Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#reallocate-contract-expense-2-schedule)

* * *

A contract expense schedule shows when the deferred expense for a contract or contract line item is expected to post during the contract term.

You can post expense schedules according to an as-of date, or you can post individual expense schedule entries.

For an expense schedule, you typically execute two posts: one to the ASC 605 set of journals (expense schedule) and one for the ASC 606 set of journals (expense 2 schedule).

* * *

### Get Contract Expense Schedule Object Definition

#### `lookup`

> List all the fields and relationships for the contract expense schedule object:

```
<lookup>
    <object>CONTRACTEXPENSESCHEDULE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSESCHEDULE` |

* * *

### Query and List Contract Expense Schedules

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and state for each contract expense schedule:

```
<query>
    <object>CONTRACTEXPENSESCHEDULE</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSESCHEDULE` |
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

### Query and List Contract Expense Schedules (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTEXPENSESCHEDULE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSESCHEDULE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Optional | string | Contract ID |
| LINENO | Optional | integer | Line number from the contract |
| STATE | Optional | string | State of the schedule. Use `I` for in progress, `H` for on hold, `C` for completed, or `T` for terminated. |

* * *

### Get Contract Expense Schedule

#### `read`

```
<read>
    <object>CONTRACTEXPENSESCHEDULE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSESCHEDULE` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Reallocate Contract Expense Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#history-reallocate-contract-expense-schedule)

| Release | Changes |
| --- | --- |
| 2018 Release 4 | New function |

You can automatically reallocate daily rate or straight line expense schedules based on different start and/or end dates.

#### `reallocate`

```
<reallocate>
    <CONTRACTEXPENSESCHEDULE>
        <SCHEDULEKEY>123</SCHEDULEKEY>
        <STARTDATE>12/31/2017</STARTDATE>
        <ENDDATE>12/31/2018</ENDDATE>
    </CONTRACTEXPENSESCHEDULE>
</reallocate>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSESCHEDULE | Required | object | Object to reallocate |

`CONTRACTEXPENSESCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SCHEDULEKEY | Required | String | Record number of the contract expense schedule |
| STARTDATE | Required | String | Start date for the reallocation in `mm/dd/yyyy` format |
| ENDDATE | Required | String | End date for the reallocation in `mm/dd/yyyy` format |
| POSTPASTDATED | Optional | String | Post past dated open periods. If you use a start date that is earlier than today’s date and there are open periods with past scheduled posting dates, this parameter indicates whether to post these. Use `true` to post the open periods, false otherwise. (Default: `false`) |

* * *

### Post Contract Expense Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#history-post-contract-expense-schedule)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | POSTINGDATE now optional |

You can post all contract expense schedule entries for a given customer (across contracts) or for a given contract.

#### `post`

```
<post>
    <CONTRACTEXPENSESCHEDULE>
        <POSTINGDATE>09/05/2017</POSTINGDATE>
        <ASOFDATE>07/05/2017</ASOFDATE>
        <CUSTOMERID>C-103</CUSTOMERID>
        <CONTRACTID>CTRC-003</CONTRACTID>
    </CONTRACTEXPENSESCHEDULE>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSESCHEDULE | Required | object | Object to post |

`CONTRACTEXPENSESCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| POSTINGDATE | Optional | string | Posting date in format `mm/dd/yyyy` (Default: Scheduled posting date). |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |
| CUSTOMERID | Optional | string | Customer ID. To post all schedule entries for the customer, omit `CONTRACTID`. Required if not not using Contract ID. |
| CONTRACTID | Optional | string | Contract ID. Required if not not using Customer ID. |

* * *

Contract Expense Schedule Entries
---------------------------------

### Post Contract Expense Schedule Entry

Posts a single contract expense schedule entry.

#### `post`

```
<post>
    <CONTRACTEXPENSESCHEDULEENTRY>
        <RECORDNO>5</RECORDNO>
        <POSTINGDATE>09/05/2017</POSTINGDATE>
    </CONTRACTEXPENSESCHEDULEENTRY>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSESCHEDULEENTRY | Required | object | Object to post |

`CONTRACTEXPENSESCHEDULEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the contract expense schedule entry to post |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |

### Unpost Contract Expense Schedule Entry

#### `unpost`

```
<unpost>
    <CONTRACTEXPENSESCHEDULEENTRY>
        <RECORDNO>5</RECORDNO>
    </CONTRACTEXPENSESCHEDULEENTRY>
</unpost>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSESCHEDULEENTRY | Optional | object | Object to unpost |

`CONTRACTEXPENSESCHEDULEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the contract expense schedule entry to unpost |

* * *

Contract Expense 2 Schedules
----------------------------

### Get Contract Expense 2 Schedule Object Definition

#### `lookup`

> List all the fields and relationships for the contract expense schedule 2 object:

```
<lookup>
    <object>CONTRACTEXPENSE2SCHEDULE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE2SCHEDULE` |

* * *

### Query and List Contract Expense 2 Schedules

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and state for each contract expense 2 schedule:

```
<query>
    <object>CONTRACTEXPENSE2SCHEDULE</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE2SCHEDULE` |
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

### Query and List Contract Expense 2 Schedules (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTEXPENSE2SCHEDULE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE2SCHEDULE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Optional | string | Contract ID |
| LINENO | Optional | integer | Line number from the contract |
| STATE | Optional | string | State of the schedule. Use `I` for in progress, `H` for on hold, `C` for completed, or `T` for terminated. |

* * *

### Get Contract Expense 2 Schedule

#### `read`

```
<read>
    <object>CONTRACTEXPENSE2SCHEDULE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSE2SCHEDULE` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Post Contract Expense 2 Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#history-post-contract-expense2-schedule)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | POSTINGDATE now optional |

Posts all contract expense 2 schedule entries for a given customer (across contracts) or for a given contract.

#### `post`

```
<post>
    <CONTRACTEXPENSE2SCHEDULE>
        <POSTINGDATE>09/05/2017</POSTINGDATE>
        <ASOFDATE>07/05/2017</ASOFDATE>
        <CUSTOMERID>C-103</CUSTOMERID>
        <CONTRACTID>CTRC-003</CONTRACTID>
    </CONTRACTEXPENSE2SCHEDULE>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE2SCHEDULE | Required | object | Object to post |

`CONTRACTEXPENSE2SCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| POSTINGDATE | Optional | string | Posting date in format `mm/dd/yyyy` (Default: Scheduled posting date). |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |
| CUSTOMERID | Optional | string | Customer ID. To post all schedule entries for the customer, omit `CONTRACTID`. Required if not not using Contract ID. |
| CONTRACTID | Optional | string | Contract ID. Required if not not using Customer ID. |

* * *

### Reallocate Contract Expense 2 Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-schedules/#history-reallocate-contract-expense2-schedule)

| Release | Changes |
| --- | --- |
| 2018 Release 4 | New function |

You can automatically reallocate daily rate or straight line expense schedules based on different start and/or end dates.

#### `reallocate`

```
<reallocate>
    <CONTRACTEXPENSE2SCHEDULE>
        <SCHEDULEKEY>123</SCHEDULEKEY>
        <STARTDATE>12/31/2017</STARTDATE>
        <ENDDATE>12/31/2018</ENDDATE>
    </CONTRACTEXPENSE2SCHEDULE>
</reallocate>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSE2SCHEDULE | Required | object | Object to reallocate |

`CONTRACTEXPENSE2SCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SCHEDULEKEY | Required | String | Record number of the contract expense schedule |
| STARTDATE | Required | String | Start date for the reallocation in `mm/dd/yyyy` format |
| ENDDATE | Required | String | End date for the reallocation in `mm/dd/yyyy` format |
| POSTPASTDATED | Optional | String | Post past dated open periods. If you use a start date that is earlier than today’s date and there are open periods with past scheduled posting dates, this parameter indicates whether to post these. Use `true` to post the open periods, false otherwise. (Default: `false`) |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

