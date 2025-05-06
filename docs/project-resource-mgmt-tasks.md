Title: Tasks

URL Source: https://developer.intacct.com/api/project-resource-mgmt/tasks/

Markdown Content:
*   [Get Task Object Definition](https://developer.intacct.com/api/project-resource-mgmt/tasks/#get-task-object-definition)
*   [Query and List Tasks](https://developer.intacct.com/api/project-resource-mgmt/tasks/#query-and-list-tasks)
*   [Query and List Tasks (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/tasks/#query-and-list-tasks-legacy)
*   [Get Task](https://developer.intacct.com/api/project-resource-mgmt/tasks/#get-task)
*   [Create Task](https://developer.intacct.com/api/project-resource-mgmt/tasks/#create-task)
*   [Create Task (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/tasks/#create-task-legacy)
*   [Update Task](https://developer.intacct.com/api/project-resource-mgmt/tasks/#update-task)
*   [Update Task (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/tasks/#update-task-legacy)
*   [Delete Task](https://developer.intacct.com/api/project-resource-mgmt/tasks/#delete-task)
*   [Delete Task (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/tasks/#delete-task-legacy)

* * *

A task is a unit of work to be performed for a project.

* * *

Get Task Object Definition
--------------------------

#### `lookup`

> List all the fields and relationships for the task object:

```
<lookup>
    <object>TASK</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TASK` |

* * *

Query and List Tasks
--------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the task IDs of tasks for the given project:

```
<query>
    <object>TASK</object>
    <select>
        <field>TASKID</field>
        <field>PROJECTID</field>
    </select>
    <filter>
        <equalto>
            <field>PROJECTID</field>
            <value>20-002</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TASK` |
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

Query and List Tasks (Legacy)
-----------------------------

#### `readByQuery`

```
<readByQuery>
    <object>TASK</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TASK` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TASKSTATUS | Optional | string | Task status. Use `N` for `Not Started`, `L` for `Planned`, `P` for `In Progress`, `C` for `Completed`, or `H` for `On Hold`. |

* * *

Get Task
--------

#### `read`

```
<read>
    <object>TASK</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TASK` |
| keys | Required | string | Comma-separated list of department `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Task
-----------

[History](https://developer.intacct.com/api/project-resource-mgmt/tasks/#history-create-task)

| Release | Changes |
| --- | --- |
| 2020 Release 1 | Added STANDARDTASKID |
| 2019 Release 1 | Added TASKID |

#### `create`

```
<create>
    <TASK>
        <NAME>hello world</NAME>
        <PROJECTID>P1234</PROJECTID>
        <TASKID>Prep-01</TASKID>
        <TASKSTATUS>In Progress</TASKSTATUS>
    </TASK>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TASK | Required | object | Object to create |

`TASK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Task name to create |
| PROJECTID | Required | string | Project ID |
| STANDARDTASKID | Optional | string | ID of a standard task to use |
| TASKID | Optional | string | Task ID that is unique for the given project. Use 20 characters or fewer. (Default: record number) |
| PRODUCTIONUNITDESC | Optional | string | Production unit description, such as _cubic yards_ or _window assembly_. Free form field with 30 or fewer characters. |
| PBEGINDATE | Optional | string | Planned begin date, which will default to the project begin date if one is set for the project. Set a different date using format `mm/dd/yyyy`. |
| PENDDATE | Optional | string | Planned end date, which will default to the project end date if one is set for the project. Set a different date using format `mm/dd/yyyy`. |
| CLASSID | Optional | string | Class ID |
| ITEMID | Optional | string | Item ID |
| BILLABLE | Optional | boolean | Billable. Use `false` for No, `true` for Yes. (Default: `false`) |
| DESCRIPTION | Optional | string | Description |
| ISMILESTONE | Optional | boolean | Milestone. Use `false` for No, `true` for Yes. (Default: `false`) |
| UTILIZED | Optional | boolean | Utilized. Use `false` for No, `true` for Yes. (Default: `false`) |
| PRIORITY | Optional | string | Priority |
| TASKNO | Optional | string | WBS code |
| TASKSTATUS | Required | string | Task status. Use `Not Started`, `Planned`, `In Progress`, `Completed`, or `On Hold`. |
| PARENTKEY | Optional | integer | Parent task `RECORDNO` |
| SUPDOCID | Optional | string | Attachments ID |
| BUDGETQTY | Optional | number | Planned duration |
| ESTQTY | Optional | number | Estimated duration |
| STATUS | Optional | string | Task status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Create Task (Legacy)
--------------------

#### `create_task`

```
<create_task>
    <taskname>hello world</taskname>
    <projectid>P1234</projectid>
</create_task>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| taskname | Required | string | Task name to create |
| projectid | Required | string | Project ID |
| pbegindate | Optional | object | Project begin date |
| penddate | Optional | object | Project end date |
| itemid | Optional | string | Item ID |
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. (Default: `false`) |
| taskdescription | Optional | string | Description |
| ismilestone | Optional | boolean | Milestone. Use `false` for No, `true` for Yes. (Default: `false`) |
| utilized | Optional | boolean | Utilized. Use `false` for No, `true` for Yes. (Default: `false`) |
| priority | Optional | string | Priority |
| taskno | Optional | string | WBS code |
| taskstatus | Optional | string | Task status |
| parentkey | Optional | integer | Parent task `RECORDNO` |
| parenttaskname | Optional | string | Parent task name |
| budgetqty | Optional | number | Planned duration |
| estqty | Optional | number | Estimated duration |
| timetype | Optional | string | Time type |
| customfields | Optional | array of `customfield` | Custom fields |
| classid | Optional | string | Class ID |
| supdocid | Optional | string | Attachments ID |
| dependentonkey | Optional | integer | Dependent on task `RECORDNO` |
| dependentonname | Optional | string | Dependent on task name |

`pbegindate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`penddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Task
-----------

You can update an existing task as described here. If you want to provide observed-percent-completed information for a task, see [Task Observed Percent Completed](https://developer.intacct.com/api/project-resource-mgmt/task-observed-pct-completed/).

#### `update`

```
<update>
    <TASK>
        <RECORDNO>10</RECORDNO>
        <PROJECTID>P1234</PROJECTID>
    </TASK>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TASK | Required | object | Object to update |

`TASK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Task `RECORDNO` to update |
| NAME | Optional | string | Task name |
| PBEGINDATE | Optional | string | Planned begin date, which will default to the project begin date if one is set for the project. Set a different date using format `mm/dd/yyyy`. |
| PENDDATE | Optional | string | Planned end date, which will default to the project end date if one is set for the project. Set a different date using format `mm/dd/yyyy`. |
| CLASSID | Optional | string | Class ID |
| ITEMID | Optional | string | Item ID |
| BILLABLE | Optional | boolean | Billable. Use `false` for No, `true` for Yes. (Default: `false`) |
| DESCRIPTION | Optional | string | Description |
| ISMILESTONE | Optional | boolean | Milestone. Use `false` for No, `true` for Yes. (Default: `false`) |
| UTILIZED | Optional | boolean | Utilized. Use `false` for No, `true` for Yes. (Default: `false`) |
| PRIORITY | Optional | string | Priority |
| TASKNO | Optional | string | WBS code |
| TASKSTATUS | Required | string | Task status. Use `Not Started`, `Planned`, `In Progress`, `Completed`, or `On Hold`. |
| PARENTKEY | Optional | integer | Parent task `RECORDNO` |
| SUPDOCID | Optional | string | Attachments ID |
| BUDGETQTY | Optional | number | Planned duration |
| ESTQTY | Optional | number | Estimated duration |
| STATUS | Optional | string | Task status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |

* * *

Update Task (Legacy)
--------------------

#### `update_task`

```
<update_task key="10">
    <projectid>P1234</projectid>
</update_task>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Task `RECORDNO` to update |
| taskname | Optional | string | Task name |
| projectid | Optional | string | Project ID |
| pbegindate | Optional | object | Project begin date |
| penddate | Optional | object | Project end date |
| itemid | Optional | string | Item ID |
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. |
| taskdescription | Optional | string | Description |
| ismilestone | Optional | boolean | Milestone. Use `false` for No, `true` for Yes. |
| utilized | Optional | boolean | Utilized. Use `false` for No, `true` for Yes. |
| priority | Optional | string | Priority |
| taskno | Optional | string | WBS code |
| taskstatus | Optional | string | Task status |
| parentkey | Optional | integer | Parent task `RECORDNO` |
| parenttaskname | Optional | string | Parent task name |
| budgetqty | Optional | number | Planned duration |
| estqty | Optional | number | Estimated duration |
| timetype | Optional | string | Time type |
| customfields | Optional | array of `customfield` | Custom fields |
| classid | Optional | string | Class ID |
| dependentonkey | Optional | integer | Dependent on task `RECORDNO` |
| dependentonname | Optional | string | Dependent on task name |

`pbegindate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`penddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Task
-----------

#### `delete`

```
<delete>
    <object>TASK</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TASK` |
| keys | Required | string | Comma-separated list of task `RECORDNO` to delete |

* * *

Delete Task (Legacy)
--------------------

#### `delete_task`

```
<delete_task key="10"></delete_task>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Task `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

