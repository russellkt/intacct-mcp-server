Title: Task Observed Percent Completed

URL Source: https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/

Markdown Content:
*   [Get Observed Percent Completed Entry Object Definition](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#get-observed-percent-completed-entry-object-definition)
*   [Query and List Observed Percent Completed Entries](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#query-and-list-observed-percent-completed-entries)
*   [Query and List Observed Percent Completed Entries (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#query-and-list-observed-percent-completed-entries-legacy)
*   [Get Observed Percent Completed Entry](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#get-observed-percent-completed-entry)
*   [Create Observed Percent Completed Entry](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#create-observed-percent-completed-entry)
*   [Update Observed Percent Completed Entry](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#update-observed-percent-completed-entry)
*   [Delete Observed Percent Completed Entry](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#delete-observed-percent-completed-entry)

* * *

You can provide an estimation of how complete a task, cost type, or project is as of a specific date.

Depending on how the parent project is set up, these percentages can affect associated revenue recognition schedules.

* * *

Get Observed Percent Completed Entry Object Definition
------------------------------------------------------

#### `lookup`

> List all the fields and relationships for the observed percent completed entry object:

```
<lookup>
    <object>OBSPCTCOMPLETED</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OBSPCTCOMPLETED` |

* * *

Query and List Observed Percent Completed Entries
-------------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the type, record number, and percent for each entry:

```
<query>
    <object>OBSPCTCOMPLETED</object>
    <select>
        <field>TYPE</field>
        <field>RECORDNO</field>
        <field>PERCENT</field>
    </select>
    <filter>
        <equalto>
            <field>TYPE</field>
            <value>Task</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OBSPCTCOMPLETED` |
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

Query and List Observed Percent Completed Entries (Legacy)
----------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>OBSPCTCOMPLETED</object>
    <fields>*</fields>
    <query>TYPE = 'T'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OBSPCTCOMPLETED` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TYPE | Required | string | Type. Use `T` for tasks, `C` for cost types, or `P` for projects. |

* * *

Get Observed Percent Completed Entry
------------------------------------

#### `read`

```
<read>
    <object>OBSPCTCOMPLETED</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OBSPCTCOMPLETED` |
| keys | Required | string | Comma-separated list of record number of the observed percent completed entry to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Observed Percent Completed Entry
---------------------------------------

[History](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#history-create-observed-percent-completed-entry)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added COSTTYPEKEY |

Be aware that after creating an observed percent completed entry for a task, you need to update the parent project to trigger updates for any associated revenue recognition schedules. (The update on the project need not actually change any data.)

#### `create`

```
<create>
    <OBSPCTCOMPLETED>
        <TYPE>Task</TYPE>
        <TASKKEY>1</TASKKEY>
        <ASOFDATE>2/22/2018</ASOFDATE>
        <PERCENT>33.33</PERCENT>
        <NOTE>One third complete</NOTE>
    </OBSPCTCOMPLETED>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| OBSPCTCOMPLETED | Required | object | Object to create |

`OBSPCTCOMPLETED`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TYPE | Required | string | Type of object. Use `Task`, `CostType`, or `Project`. |
| PROJECTKEY | Optional | integer | Record number of a project. Required if type of object is `Project`. |
| TASKKEY | Optional | integer | Record number of a task. Required if type of object is `Task`. |
| COSTTYPEKEY | Optional | integer | Record number of a cost type. Required if type of object is `CostType`. |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy`. Only one observed percent completed entry is allowed for a given date. |
| PERCENT | Required | number | Observed percent completed for this entry |
| NOTE | Optional | string | Description |

* * *

Update Observed Percent Completed Entry
---------------------------------------

[History](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/#history-update-observed-percent-completed-entry)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added COSTTYPEKEY |

Be aware that after updating an observed percent completed entry, you need to call update on the parent project to trigger updates for any associated revenue recognition schedules. (The project update need not actually change any data.)

#### `update`

```
<update>
    <OBSPCTCOMPLETED>
        <RECORDNO>1</RECORDNO>
        <PERCENT>22.00</PERCENT>
    </OBSPCTCOMPLETED>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| OBSPCTCOMPLETED | Required | object | Object to update |

`OBSPCTCOMPLETED`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the observed percent completed entry to update |
| ASOFDATE | Optional | string | As of date in format `mm/dd/yyyy` |
| PERCENT | Optional | number | Observed percent completed for this entry |
| NOTE | Optional | string | Description |

* * *

Delete Observed Percent Completed Entry
---------------------------------------

#### `delete`

```
<delete>
    <object>OBSPCTCOMPLETED</object>
    <keys>1</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OBSPCTCOMPLETED` |
| keys | Required | string | Comma-separated list of record number of the observed percent completed entry to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

