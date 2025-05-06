Title: Contract Revenue Schedules

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/

Markdown Content:
*   [Contract Revenue Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#contract-revenue-schedules)
    *   [Get Contract Revenue Schedule Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#get-contract-revenue-schedule-object-definition)
    *   [Query and List Contract Revenue Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#query-and-list-contract-revenue-schedules)
    *   [Query and List Contract Revenue Schedules (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#query-and-list-contract-revenue-schedules-legacy)
    *   [Get Contract Revenue Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#get-contract-revenue-schedule)
    *   [Post Contract Revenue Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#post-contract-revenue-schedule)
    *   [Reallocate Contract Revenue Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#reallocate-contract-revenue-schedule)
*   [Contract Revenue Schedule Entries](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#contract-revenue-schedule-entries)
    *   [Post Contract Revenue Schedule Entry](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#post-contract-revenue-schedule-entry)
    *   [Unpost Contract Revenue Schedule Entry](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#unpost-contract-revenue-schedule-entry)
*   [Contract Revenue 2 Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#contract-revenue-2-schedules)
    *   [Get Contract Revenue 2 Schedule Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#get-contract-revenue-2-schedule-object-definition)
    *   [Query and List Contract Revenue 2 Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#query-and-list-contract-revenue-2-schedules)
    *   [Query and List Contract Revenue 2 Schedules (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#query-and-list-contract-revenue-2-schedules-legacy)
    *   [Get Contract Revenue 2 Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#get-contract-revenue-2-schedule)
    *   [Post Contract Revenue 2 Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#post-contract-revenue-2-schedule)
    *   [Reallocate Contract Revenue 2 Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#reallocate-contract-revenue-2-schedule)

* * *

A revenue schedule shows when the deferred revenue for a contract line item is expected to be recognized during the contract line term.

You can post revenue schedules according to an as-of date, or you can post individual revenue schedule entries.

For a revenue schedule, you typically execute two posts: one to the ASC 605 set of journals (revenue schedule) and one for the ASC 606 set of journals (revenue 2 schedule).

* * *

### Get Contract Revenue Schedule Object Definition

#### `lookup`

> List all the fields and relationships for the contract revenue schedule object:

```
<lookup>
    <object>CONTRACTREVENUESCHEDULE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUESCHEDULE` |

* * *

### Query and List Contract Revenue Schedules

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, contract ID, and delivery date for each contract revenue schedule:

```
<query>
    <object>CONTRACTREVENUESCHEDULE</object>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
        <field>DELIVERYDATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUESCHEDULE` |
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

### Query and List Contract Revenue Schedules (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTREVENUESCHEDULE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUESCHEDULE` |
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

### Get Contract Revenue Schedule

#### `read`

```
<read>
    <object>CONTRACTREVENUESCHEDULE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUESCHEDULE` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Post Contract Revenue Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#history-post-contract-revenue-schedule)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | POSTINGDATE now optional |

You can post all contract revenue schedule entries for a given customer (across contracts) or for a given contract.

#### `post`

```
<post>
    <CONTRACTREVENUESCHEDULE>
        <POSTINGDATE>09/05/2017</POSTINGDATE>
        <ASOFDATE>07/05/2017</ASOFDATE>
        <CUSTOMERID>C-103</CUSTOMERID>
        <CONTRACTID>CTRC-003</CONTRACTID>
    </CONTRACTREVENUESCHEDULE>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUESCHEDULE | Required | object | Object to post |

`CONTRACTREVENUESCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| POSTINGDATE | Optional | string | Posting date in format `mm/dd/yyyy` (Default: Scheduled posting date). |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |
| CUSTOMERID | Optional | string | Customer ID. To post all schedule entries for the customer, omit `CONTRACTID`. Required if not not using Contract ID. |
| CONTRACTID | Optional | string | Contract ID. Required if not not using Customer ID. |

* * *

### Reallocate Contract Revenue Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#history-reallocate-contract-revenue-schedule)

| Release | Changes |
| --- | --- |
| 2018 Release 4 | New function |

You can automatically reallocate daily rate or straight line revenue schedules based on different start and/or end dates.

#### `reallocate`

```
<reallocate>
    <CONTRACTREVENUESCHEDULE>
        <SCHEDULEKEY>123</SCHEDULEKEY>
        <STARTDATE>12/31/2017</STARTDATE>
        <ENDDATE>12/31/2018</ENDDATE>
    </CONTRACTREVENUESCHEDULE>
</reallocate>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUESCHEDULE | Required | object | Object to reallocate |

`CONTRACTREVENUESCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SCHEDULEKEY | Required | String | Record number of the contract revenue schedule |
| STARTDATE | Required | String | Start date for the reallocation in `mm/dd/yyyy` format |
| ENDDATE | Required | String | End date for the reallocation in `mm/dd/yyyy` format |
| POSTPASTDATED | Optional | String | Post past dated open periods. If you use a start date that is earlier than today’s date and there are open periods with past scheduled posting dates, this parameter indicates whether to post these. Use `true` to post the open periods, false otherwise. (Default: `false`) |

* * *

Contract Revenue Schedule Entries
---------------------------------

### Post Contract Revenue Schedule Entry

Posts a single contract revenue schedule entry.

#### `post`

```
<post>
    <CONTRACTREVENUESCHEDULEENTRY>
        <RECORDNO>5</RECORDNO>
        <POSTINGDATE>09/05/2017</POSTINGDATE>
    </CONTRACTREVENUESCHEDULEENTRY>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUESCHEDULEENTRY | Optional | object | Object to post |

`CONTRACTREVENUESCHEDULEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the contract revenue schedule entry to post |
| POSTINGDATE | Required | string | As of date in format `mm/dd/yyyy` |

### Unpost Contract Revenue Schedule Entry

#### `unpost`

```
<unpost>
    <CONTRACTREVENUESCHEDULEENTRY>
        <RECORDNO>5</RECORDNO>
    </CONTRACTREVENUESCHEDULEENTRY>
</unpost>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUESCHEDULEENTRY | Required | object | Object to unpost |

`CONTRACTREVENUESCHEDULEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the contract revenue schedule entry to unpost |

* * *

* * *

Contract Revenue 2 Schedules
----------------------------

### Get Contract Revenue 2 Schedule Object Definition

#### `lookup`

> List all the fields and relationships for the contract revenue 2 schedule object:

```
<lookup>
    <object>CONTRACTREVENUE2SCHEDULE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUE2SCHEDULE` |

* * *

### Query and List Contract Revenue 2 Schedules

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, contract ID, and delivery date for each contract revenue 2 schedule:

```
<query>
    <object>CONTRACTREVENUE2SCHEDULE</object>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
        <field>DELIVERYDATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUE2SCHEDULE` |
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

### Query and List Contract Revenue 2 Schedules (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTREVENUE2SCHEDULE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUE2SCHEDULE` |
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

### Get Contract Revenue 2 Schedule

#### `read`

```
<read>
    <object>CONTRACTREVENUE2SCHEDULE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUE2SCHEDULE` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Post Contract Revenue 2 Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#history-post-contract-revenue2-schedule)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | POSTINGDATE now optional |

You can post all contract revenue 2 schedule entries for a given customer (across contracts) or for a given contract.

#### `post`

```
<post>
    <CONTRACTREVENUE2SCHEDULE>
        <POSTINGDATE>09/05/2017</POSTINGDATE>
        <ASOFDATE>07/05/2017</ASOFDATE>
        <CUSTOMERID>C-103</CUSTOMERID>
        <CONTRACTID>CTRC-003</CONTRACTID>
    </CONTRACTREVENUE2SCHEDULE>
</post>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUE2SCHEDULE | Required | object | Object to post |

`CONTRACTREVENUE2SCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| POSTINGDATE | Optional | string | Posting date in format `mm/dd/yyyy` (Default: Scheduled posting date). |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |
| CUSTOMERID | Optional | string | Customer ID. To post all schedule entries for the customer, omit `CONTRACTID`. Required if not not using Contract ID. |
| CONTRACTID | Optional | string | Contract ID. Required if not not using Customer ID. |

* * *

### Reallocate Contract Revenue 2 Schedule

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-schedules/#history-reallocate-contract-revenue2-schedule)

| Release | Changes |
| --- | --- |
| 2018 Release 4 | New function |

You can automatically reallocate daily rate or straight line revenue schedules based on different start and/or end dates.

#### `reallocate`

```
<reallocate>
    <CONTRACTREVENUE2SCHEDULE>
        <SCHEDULEKEY>123</SCHEDULEKEY>
        <STARTDATE>12/31/2017</STARTDATE>
        <ENDDATE>12/31/2018</ENDDATE>
    </CONTRACTREVENUE2SCHEDULE>
</reallocate>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUE2SCHEDULE | Required | object | Object to reallocate |

`CONTRACTREVENUE2SCHEDULE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SCHEDULEKEY | Required | String | Record number of the contract revenue schedule |
| STARTDATE | Required | String | Start date for the reallocation in `mm/dd/yyyy` format |
| ENDDATE | Required | String | End date for the reallocation in `mm/dd/yyyy` format |
| POSTPASTDATED | Optional | String | Post past dated open periods. If you use a start date that is earlier than today’s date and there are open periods with past scheduled posting dates, this parameter indicates whether to post these. Use `true` to post the open periods, false otherwise. (Default: `false`) |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

