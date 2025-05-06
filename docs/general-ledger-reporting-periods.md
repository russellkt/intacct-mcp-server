Title: Reporting Periods

URL Source: https://developer.intacct.com/api/general-ledger/reporting-periods/

Markdown Content:
*   [Get Reporting Period Object Definition](https://developer.intacct.com/api/general-ledger/reporting-periods/#get-reporting-period-object-definition)
*   [Query and List Reporting Periods](https://developer.intacct.com/api/general-ledger/reporting-periods/#query-and-list-reporting-periods)
*   [Query and List Reporting Periods (Legacy)](https://developer.intacct.com/api/general-ledger/reporting-periods/#query-and-list-reporting-periods-legacy)
*   [Get Reporting Period](https://developer.intacct.com/api/general-ledger/reporting-periods/#get-reporting-period)
*   [Get Reporting Period by ID](https://developer.intacct.com/api/general-ledger/reporting-periods/#get-reporting-period-by-id)
*   [Create Reporting Period](https://developer.intacct.com/api/general-ledger/reporting-periods/#create-reporting-period)
*   [Update Reporting Period](https://developer.intacct.com/api/general-ledger/reporting-periods/#update-reporting-period)
*   [Delete Reporting Period](https://developer.intacct.com/api/general-ledger/reporting-periods/#delete-reporting-period)

* * *

Reporting periods are used when creating reports and budgets, and when opening and closing books.

They limit the information on the report to specific time ranges.

* * *

Get Reporting Period Object Definition
--------------------------------------

#### `lookup`

> List all the fields and relationships for the budgetable period object:

```
<lookup>
    <object>REPORTINGPERIOD</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REPORTINGPERIOD` |

* * *

Query and List Reporting Periods
--------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each budgetable period:

```
<query>
    <object>REPORTINGPERIOD</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
        <field>BUDGETING</field>
    </select>
    <filter>
        <equalto>
            <field>BUDGETING</field>
            <value>true</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REPORTINGPERIOD` |
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

Query and List Reporting Periods (Legacy)
-----------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>REPORTINGPERIOD</object>
    <fields>*</fields>
    <query>budgeting = 'T'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REPORTINGPERIOD` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| budgeting | Optional | boolean | Period is budgetable. Use `T` for true or `F` for false. |

* * *

Get Reporting Period
--------------------

#### `read`

```
<read>
    <object>REPORTINGPERIOD</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REPORTINGPERIOD` |
| keys | Required | string | Comma-separated list of reporting period `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Reporting Period by ID
--------------------------

#### `readByName`

```
<readByName>
    <object>REPORTINGPERIOD</object>
    <keys>TEST</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REPORTINGPERIOD` |
| keys | Required | string | Comma-separated list of reporting period `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Reporting Period
-----------------------

#### `create`

```
<create>
    <REPORTINGPERIOD>
        <NAME>Month Ended January 2017</NAME>
        <HEADER1>Month Ended</HEADER1>
        <HEADER2>January 2017</HEADER2>
        <START_DATE>01/01/2017</START_DATE>
        <END_DATE>01/31/2017</END_DATE>
        <BUDGETING>true</BUDGETING>
        <STATUS>active</STATUS>
    </REPORTINGPERIOD>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| REPORTINGPERIOD | Required | object | Object to create |

`REPORTINGPERIOD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Reporting Period Name |
| HEADER1 | Required | string | Header 1 |
| HEADER2 | Optional | string | Header 2 |
| START\_DATE | Required | string | Start date in format `mm/dd/yyyy`. |
| END\_DATE | Required | string | End date in format `mm/dd/yyyy`. |
| BUDGETING | Optional | boolean | Use `true` to make this period budgetable, otherwise use `false`. Budgeting periods cannot overlap. (Default: `false`) |
| STATUS | Optional | string | Use `active` for Active, otherwise `inactive` for Inactive. (Default: `active`) |

* * *

Update Reporting Period
-----------------------

#### `update`

```
<update>
    <REPORTINGPERIOD>
        <RECORDNO>124</RECORDNO>
        <HEADER1>Month Ended</HEADER1>
        <HEADER2>January 2017</HEADER2>
        <START_DATE>01/01/2017</START_DATE>
        <END_DATE>01/31/2017</END_DATE>
        <BUDGETING>true</BUDGETING>
        <STATUS>active</STATUS>
    </REPORTINGPERIOD>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| REPORTINGPERIOD | Required | object | Object to update |

`REPORTINGPERIOD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of the reporting period to update. Required if not using `NAME`. |
| NAME | Optional | string | Name of the reporting period. Required if not using `RECORDNO`. |
| HEADER1 | Required | string | Header 1 |
| HEADER2 | Optional | string | Header 2 |
| START\_DATE | Required | string | Start date in format `mm/dd/yyyy`. |
| END\_DATE | Required | string | End date in format `mm/dd/yyyy`. |
| BUDGETING | Optional | boolean | Use `true` to make this period budgetable, otherwise use `false`. Budgeting periods cannot overlap. |
| STATUS | Optional | string | Use `active` for Active, otherwise `inactive` for Inactive. |

* * *

Delete Reporting Period
-----------------------

#### `delete`

```
<delete>
    <object>REPORTINGPERIOD</object>
    <keys>12</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `REPORTINGPERIOD` |
| keys | Required | string | Comma-separated list of reporting period `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

