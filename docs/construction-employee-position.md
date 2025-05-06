Title: Employee Position

URL Source: https://developer.intacct.com/api/construction/employee-position/

Markdown Content:
*   [Get Employee Position Object Definition](https://developer.intacct.com/api/construction/employee-position/#get-employee-position-object-definition)
*   [Query and List Employee Positions](https://developer.intacct.com/api/construction/employee-position/#query-and-list-employee-positions)
*   [Query and List Employee Positions (Legacy)](https://developer.intacct.com/api/construction/employee-position/#query-and-list-employee-positions-legacy)
*   [Get an Employee Position](https://developer.intacct.com/api/construction/employee-position/#get-an-employee-position)
*   [Get an Employee Position by ID](https://developer.intacct.com/api/construction/employee-position/#get-an-employee-position-by-id)
*   [Create an Employee Position](https://developer.intacct.com/api/construction/employee-position/#create-an-employee-position)
*   [Update a Employee Position](https://developer.intacct.com/api/construction/employee-position/#update-a-employee-position)
*   [Delete Employee Position](https://developer.intacct.com/api/construction/employee-position/#delete-employee-position)

* * *

You can define a set of employee positions and use those positions in timesheets and rate tables to bill employee labor out at different rates, depending on the work that an employee does at various times during the day.

For example, you may want to bill a customer at one rate for the time that an employee spends unloading a truck, but then bill at a different rate when the same employee does work as an electrical apprentice. You can define a set of employee positions to use on [timesheets](https://developer.intacct.com/api/project-resource-mgmt/timesheets/) and in [rate table timesheet entries](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) to accomplish this.

* * *

Get Employee Position Object Definition
---------------------------------------

#### `lookup`

> List all the fields and relationships for the employee position object:

```
<lookup>
    <object>EMPLOYEEPOSITION</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEPOSITION` |

* * *

Query and List Employee Positions
---------------------------------

#### `query`

> List the record number and name for each employee position:

```
<query>
    <object>EMPLOYEEPOSITION</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEPOSITION` |
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

Query and List Employee Positions (Legacy)
------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>EMPLOYEEPOSITION</object>
    <fields>*</fields>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEPOSITION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get an Employee Position
------------------------

#### `read`

```
<read>
    <object>EMPLOYEEPOSITION</object>
    <keys>8</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEPOSITION` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the employee position to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get an Employee Position by ID
------------------------------

#### `readByName`

```
<readByName>
    <object>EMPLOYEEPOSITION</object>
    <keys>Labor</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEPOSITION` |
| keys | Required | string | Comma-separated list of `POSITIONID` of the employee position to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create an Employee Position
---------------------------

#### `create`

```
<create>
    <EMPLOYEEPOSITION>
        <POSITIONID>LAB-01</POSITIONID>
        <NAME>Labor</NAME>
        <DESCRIPTION>Unskilled labor</DESCRIPTION>
    </EMPLOYEEPOSITION>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `EMPLOYEEPOSITION` | Required | object | Object type to create. |

`EMPLOYEEPOSITION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| POSITIONID | Required | string | User-defined unique ID of the employee position. |
| NAME | Required | string | Name of the employee position. |
| DESCRIPTION | Optional | string | Description of the employee position. |
| STATUS | Optional | enum | Whether this employee position is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update a Employee Position
--------------------------

#### `update`

> Updates the name of an employee position:

```
<update>
    <EMPLOYEEPOSITION>
        <RECORDNO>8</RECORDNO>
        <NAME>Carpenter</NAME>
    </EMPLOYEEPOSITION>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `EMPLOYEEPOSITION` | Required | object | Object type to update. |

`EMPLOYEEPOSITION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | string | `RECORDNO` of the employee position to update. Required if not including `POSITIONID`. |
| POSITIONID | Optional | string | `POSITIONID` of the employee position to update. Required if not including `RECORDNO`. |
| NAME | Optional | string | Name of the employee position. |
| DESCRIPTION | Optional | string | Description of the employee position. |
| STATUS | Optional | enum | Whether this employee position is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Employee Position
------------------------

#### `delete`

```
<delete>
    <object>EMPLOYEEPOSITION</object>
    <keys>8</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEEPOSITION` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the employee position to delete. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

