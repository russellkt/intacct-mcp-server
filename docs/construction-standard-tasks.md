Title: Standard Tasks

URL Source: https://developer.intacct.com/api/construction/standard-tasks/

Markdown Content:
*   [Get Standard Task Object Definition](https://developer.intacct.com/api/construction/standard-tasks/#get-standard-task-object-definition)
*   [Query and List Standard Tasks](https://developer.intacct.com/api/construction/standard-tasks/#query-and-list-standard-tasks)
*   [Query and List Standard Tasks (Legacy)](https://developer.intacct.com/api/construction/standard-tasks/#query-and-list-standard-tasks-legacy)
*   [Get Standard Task](https://developer.intacct.com/api/construction/standard-tasks/#get-standard-task)
*   [Get Standard Task by ID](https://developer.intacct.com/api/construction/standard-tasks/#get-standard-task-by-id)
*   [Create Standard Task](https://developer.intacct.com/api/construction/standard-tasks/#create-standard-task)
*   [Update Standard Task](https://developer.intacct.com/api/construction/standard-tasks/#update-standard-task)
*   [Delete Standard Task](https://developer.intacct.com/api/construction/standard-tasks/#delete-standard-task)

* * *

You set up a catalog of standard tasks to use as templates when creating new tasks.

Standard tasks are independent of projects. Your standard task can link to multiple [standard cost types](https://developer.intacct.com/api/construction/standard-cost-types/). When you create a task based on a standard task like this, the corresponding cost types are created for your task.

**Note:** Task corresponds with _cost code_ in the work breakdown structure in the Construction industry.

* * *

Get Standard Task Object Definition
-----------------------------------

#### `lookup`

> List all the fields and relationships for the standard task object:

```
<lookup>
    <object>STANDARDTASK</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDTASK` |

* * *

Query and List Standard Tasks
-----------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each standard task:

```
<query>
    <object>STANDARDTASK</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDTASK` |
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

Query and List Standard Tasks (Legacy)
--------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>STANDARDTASK</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDTASK` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Standard Task
-----------------

#### `read`

```
<read>
    <object>STANDARDTASK</object>
    <keys>66</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDTASK` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the standard task to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Standard Task by ID
-----------------------

#### `readByName`

```
<readByName>
    <object>STANDARDTASK</object>
    <keys>CNCRT-F</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDTASK` |
| keys | Required | string | Comma-separated list of `ID` of the standard task to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Standard Task
--------------------

#### `create`

```
<create>
    <STANDARDTASK>
        <STANDARDTASKID>CNCRT-F</STANDARDTASKID>
        <NAME>Concrete Finishing</NAME>
        <DESCRIPTION>Concrete finishing, interior/exterior</DESCRIPTION>
        <COSTUNITDESCRIPTION>Sqft</COSTUNITDESCRIPTION>
        <TIMETYPENAME>Contract</TIMETYPENAME>
        <TASKNO>03-3500</TASKNO>
        <STANDARDTASKSTANDARDCOSTTYPES>
            <STANDARDTASKSTANDARDCOSTTYPE>
                <STANDARDCOSTTYPEID>MAT</STANDARDCOSTTYPEID>
            </STANDARDTASKSTANDARDCOSTTYPE>
            <STANDARDTASKSTANDARDCOSTTYPE>
                <STANDARDCOSTTYPEID>LAB-REG</STANDARDCOSTTYPEID>
            </STANDARDTASKSTANDARDCOSTTYPE>
        </STANDARDTASKSTANDARDCOSTTYPES>
    </STANDARDTASK>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDTASK | Required | object | Object to create |

`STANDARDTASK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDTASKID | Required | string | Unique ID for the standard task. Use 20 or fewer characters. |
| NAME | Optional | string | Name for the standard task. Does not have to be unique. Use 200 or fewer characters. |
| DESCRIPTION | Optional | string | Description for the standard task. Use 1000 or fewer characters. |
| PRODUCTIONUNITDESC | Optional | string | Production unit description, such as _cubic yards_ or _window assembly_. Free form field with 30 or fewer characters. |
| ITEMID | Optional | string | ID of the item. `Only Non-Inventory` and `Non-Inventory (Sales only)` items are valid. Required if `BILLABLE` is `true`. |
| BILLABLE | Optional | boolean | Billable. Use `true` for yes, `false` for no. (Default: `false`) |
| ISMILESTONE | Optional | boolean | Is this a milestone? Use `true` for yes, `false` for no. (Default: `false`) |
| UTILIZED | Optional | boolean | Utilized. Use `true` for yes, `false` for no. (Default: `false`) |
| PRIORITY | Optional | string | Priority |
| TIMETYPENAME | Optional | string | Name of the [time type](https://developer.intacct.com/api/project-resource-mgmt/time-types/) to use. |
| TASKNO | Optional | string | Work breakdown structure code. Free form field with 8 or fewer characters. |
| PARENTKEY | Optional | integer | Unique ID of the parent standard task |
| CLASSID | Optional | string | Class ID |
| STANDARDTASKSTANDARDCOSTTYPES | Optional | `STANDARDTASKSTANDARDCOSTTYPE[1..n]` | Existing [standard cost types](https://developer.intacct.com/api/construction/standard-cost-types/) to associate with the standard task |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| customfields | optional | customfield\[0…n\] | Custom fields |

`STANDARDTASKSTANDARDCOSTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDCOSTTYPEID | Required | string | Unique ID for the standard cost type. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Standard Task
--------------------

When updating a standard task to modify the associated cost types, be aware that it is a complete replacement of the existing set. So, to add a cost type, supply all the original ones and the new one. To delete a cost type, supply only the ones you want to keep. To remove all cost types, provide an empty set.

#### `update`

```
<update>
    <STANDARDTASK>
        <STANDARDTASKID>CNCRT-F</STANDARDTASKID>
        <TIMETYPENAME>Regular</TIMETYPENAME>
    </STANDARDTASK>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDTASK | Required | object | Object to update |

`STANDARDTASK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDTASKID | Optional | string | Unique ID of the standard task to update. Required if not using `RECORDNO`. |
| RECORDNO | Optional | integer | Record number of the standard task to update. Required if not using `STANDARDTASKID`. |
| NAME | Optional | string | Name for the standard task. Does not have to be unique. Use 200 or fewer characters. |
| DESCRIPTION | Optional | string | Description for the standard task. Use 1000 or fewer characters. |
| PRODUCTIONUNITDESC | Optional | string | Production unit description. Free form field with 30 or fewer characters. |
| ITEMID | Optional | string | ID of the item. `Only Non-Inventory` and `Non-Inventory (Sales only)` items are valid. Required if `BILLABLE` is `true`. |
| BILLABLE | Optional | boolean | Billable. Use `true` for yes, `false` for no. (Default: `false`) |
| ISMILESTONE | Optional | boolean | Is this a milestone? Use `true` for yes, `false` for no. (Default: `false`) |
| UTILIZED | Optional | boolean | Utilized. Use `true` for yes, `false` for no. (Default: `false`) |
| PRIORITY | Optional | string | Priority |
| TIMETYPENAME | Optional | string | Name of the [time type](https://developer.intacct.com/api/project-resource-mgmt/time-types/) to use. |
| TASKNO | Optional | string | Work breakdown structure code. Free form field with 8 or fewer characters. |
| PARENTKEY | Optional | integer | Unique ID of the parent standard task |
| CLASSID | Optional | string | Class ID |
| STANDARDTASKSTANDARDCOSTTYPES | Optional | `STANDARDTASKSTANDARDCOSTTYPE[1..n]` | Existing [standard cost types](https://developer.intacct.com/api/construction/standard-cost-types/) to associate with the standard task. To add a cost type, supply all the original ones and the new one. To delete a cost type, supply only the ones you want to keep. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| customfields | optional | customfield\[0…n\] | Custom fields |

`STANDARDTASKSTANDARDCOSTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDCOSTTYPEID | Required | string | Unique ID for the standard cost type. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Standard Task
--------------------

#### `delete`

```
<delete>
    <object>STANDARDTASK</object>
    <keys>66</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDTASK` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the standard task to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

