Title: Cost Types

URL Source: https://developer.intacct.com/api/construction/cost-types/

Markdown Content:
*   [Get Cost Type Object Definition](https://developer.intacct.com/api/construction/cost-types/#get-cost-type-object-definition)
*   [Query and List Cost Types](https://developer.intacct.com/api/construction/cost-types/#query-and-list-cost-types)
*   [Query and List Cost Types (Legacy)](https://developer.intacct.com/api/construction/cost-types/#query-and-list-cost-types-legacy)
*   [Get Cost Type](https://developer.intacct.com/api/construction/cost-types/#get-cost-type)
*   [Create Cost Type](https://developer.intacct.com/api/construction/cost-types/#create-cost-type)
*   [Update Cost Type](https://developer.intacct.com/api/construction/cost-types/#update-cost-type)
*   [Delete Cost Type](https://developer.intacct.com/api/construction/cost-types/#delete-cost-type)

* * *

Cost type is a standard dimension used to record expenses in Construction projects.

Each project typically has several cost types related to labor, materials, subcontracts, and so forth. You use the [standard cost types](https://developer.intacct.com/api/construction/standard-cost-types/) in the catalog as templates for creating new cost types.

Each cost type is associated with a task, which in turn is associated with a project. A cost type record is uniquely identified by the standard cost type used to create it as well as the combination of project/task to which it applies.

**Note:** Cost type corresponds with _category_ in the work breakdown structure in the construction industry.

* * *

Get Cost Type Object Definition
-------------------------------

#### `lookup`

> List all the fields and relationships for the cost type object:

```
<lookup>
    <object>COSTTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COSTTYPE` |

* * *

Query and List Cost Types
-------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the cost type ID and record number for cost types for the given project/task:

```
<query>
    <object>COSTTYPE</object>
    <select>
        <field>COSTTYPEID</field>
        <field>RECORDNO</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>PROJECTID</field>
                <value>20-001</value>
            </equalto>
            <equalto>
                <field>TASKID</field>
                <value>1-010</value>
            </equalto>
        </and>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COSTTYPE` |
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

Query and List Cost Types (Legacy)
----------------------------------

List all cost types:

#### `readByQuery`

```
<readByQuery>
    <object>COSTTYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List all cost types for the given task:

```
<readByQuery>
    <object>COSTTYPE</object>
    <fields>*</fields>
    <query>projectid = '20-001' and taskid = '1-010'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COSTTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Cost Type
-------------

#### `read`

```
<read>
    <object>COSTTYPE</object>
    <keys>24</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COSTTYPE` |
| keys | Required | string | Comma-separated list of cost type `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Cost Type
----------------

When you create a cost type, the following field values from the given standard cost type are used unless you override them:

*   `ACCUMULATIONTYPENAME`
*   `ACCOUNTNO`
*   `PARENTID`
*   `ITEMID`

Custom field values from the standard cost type can also be used by the cost type. For this to work, the standard cost type and the cost type must have same custom fields with the same IDs, types, and lengths. Custom fields of type `Sequence` are not copied.

Parent-child relationships defined by standard cost types are preserved when cost types are created.

#### `create`

```
<create>
    <COSTTYPE>
        <STANDARDCOSTTYPEID>Material</STANDARDCOSTTYPEID>
        <PROJECTID>19-002-CR2</PROJECTID>
        <TASKID>09-000</TASKID>
        <DESCRIPTION>Material Cost Type description</DESCRIPTION>
        <COSTUNITDESCRIPTION>Square feet</COSTUNITDESCRIPTION>
        <ACTUALBEGINDATE>01/10/2020</ACTUALBEGINDATE>
    </COSTTYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COSTTYPE | Required | object | Object to create |

`COSTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDCOSTTYPEID | Required | string | Standard cost type ID to use as a template for this cost type |
| NAME | Optional | string | Name of the cost type, which does not have to be unique. Use 200 or fewer characters. |
| DESCRIPTION | Optional | string | Description of the cost type. Use 1000 or fewer characters. |
| PROJECTID | Optional | string | Project ID. Required if not using `TASKKEY`. |
| TASKKEY | Optional | string | Record number of a task object. Required if not using `PROJECTID` and `TASKID`. |
| TASKID | Optional | string | Task ID. Required if not using `TASKKEY`. |
| ACCUMULATIONTYPENAME | Optional | string | Name of an accumulation type to use |
| COSTUNITDESCRIPTION | Optional | string | Cost unit description, such as feet or square yards. Use 30 or fewer characters. |
| ACCOUNTNO | Optional | string | Account number |
| ITEMID | Optional | string | Item ID for corresponding Inventory Control item |
| PLANNEDBEGINDATE | Optional | date | Planned begin date in format `mm/dd/yyyy` |
| PLANNEDENDDATE | Optional | date | Planned end date in format `mm/dd/yyyy` |
| ACTUALBEGINDATE | Optional | date | Actual begin date in format `mm/dd/yyyy` |
| ACTUALENDDATE | Optional | date | Actual end date in format `mm/dd/yyyy` |
| STATUS | Optional | boolean | Status. Use `active` or `inactive` (Default: `active`). |

* * *

Update Cost Type
----------------

#### `update`

```
<update>
    <COSTTYPE>
        <RECORDNO>24</RECORDNO>
        <ACTUALBEGINDATE>01/16/2020</ACTUALBEGINDATE>
    </COSTTYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COSTTYPE | Required | object | Object to update |

`COSTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Cost type `RECORDNO` to update |
| PARENTID | Optional | string | ID of a parent cost type if hierarchical cost types are used |
| NAME | Optional | string | Name of the cost type, which does not have to be unique. Use 200 or fewer characters. |
| DESCRIPTION | Optional | string | Description of the cost type. Use 1000 or fewer characters. |
| PROJECTID | Optional | string | Project ID. Required if not using `TASKKEY`. |
| TASKKEY | Optional | string | Record number of a task object. Required if not using `PROJECTID` and `TASKID`. |
| TASKID | Optional | string | Task ID. Required if not using `TASKKEY`. |
| ACCUMULATIONTYPENAME | Optional | string | Name of an accumulation type to use |
| COSTUNITDESCRIPTION | Optional | string | Cost unit description, such as feet or square yards. Use 30 or fewer characters. |
| ACCOUNTNO | Optional | string | Account number |
| ITEMID | Optional | string | Item ID for corresponding Inventory Control item |
| PLANNEDBEGINDATE | Optional | date | Planned begin date in format `mm/dd/yyyy` |
| PLANNEDENDDATE | Optional | date | Planned end date in format `mm/dd/yyyy` |
| ACTUALBEGINDATE | Optional | date | Actual begin date in format `mm/dd/yyyy` |
| ACTUALENDDATE | Optional | date | Actual end date in format `mm/dd/yyyy` |
| STATUS | Optional | boolean | Status. Use `active` or `inactive`. |
| customfields | optional | customfield\[0…n\] | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Cost Type
----------------

#### `delete`

```
<delete>
    <object>COSTTYPE</object>
    <keys>24</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COSTTYPE` |
| keys | Required | string | Comma-separated list of cost type `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

