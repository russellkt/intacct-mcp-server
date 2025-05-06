Title: Project Estimates

URL Source: https://developer.intacct.com/api/construction/project-estimates/

Markdown Content:
*   [Project Estimates](https://developer.intacct.com/api/construction/project-estimates/#project-estimates)
    *   [Get Project Estimate Object Definition](https://developer.intacct.com/api/construction/project-estimates/#get-project-estimate-object-definition)
    *   [Query and List Project Estimates](https://developer.intacct.com/api/construction/project-estimates/#query-and-list-project-estimates)
    *   [Query and List Project Estimates (Legacy)](https://developer.intacct.com/api/construction/project-estimates/#query-and-list-project-estimates-legacy)
    *   [Get Project Estimate](https://developer.intacct.com/api/construction/project-estimates/#get-project-estimate)
    *   [Get Project Estimate by ID](https://developer.intacct.com/api/construction/project-estimates/#get-project-estimate-by-id)
    *   [Create Project Estimate](https://developer.intacct.com/api/construction/project-estimates/#create-project-estimate)
    *   [Update Project Estimate](https://developer.intacct.com/api/construction/project-estimates/#update-project-estimate)
    *   [Delete Project Estimate](https://developer.intacct.com/api/construction/project-estimates/#delete-project-estimate)
*   [Project Estimate Entries](https://developer.intacct.com/api/construction/project-estimates/#project-estimate-entries)
    *   [Get Project Estimate Entry Object Definition](https://developer.intacct.com/api/construction/project-estimates/#get-project-estimate-entry-object-definition)
    *   [Query and List Project Estimate Entries](https://developer.intacct.com/api/construction/project-estimates/#query-and-list-project-estimate-entries)
    *   [Query and List Project Estimate Entries (Legacy)](https://developer.intacct.com/api/construction/project-estimates/#query-and-list-project-estimate-entries-legacy)
    *   [Get Project Estimate Entry](https://developer.intacct.com/api/construction/project-estimates/#get-project-estimate-entry)
    *   [Create Project Estimate Entry](https://developer.intacct.com/api/construction/project-estimates/#create-project-estimate-entry)
    *   [Update Project Estimate Entry](https://developer.intacct.com/api/construction/project-estimates/#update-project-estimate-entry)
    *   [Delete Project Estimate Entry](https://developer.intacct.com/api/construction/project-estimates/#delete-project-estimate-entry)

* * *

A project estimate lets you compare estimated costs for a project against the actual amounts posted.

A project estimate is composed of one or more project estimate entries, which are amounts that can be tied to cost types (_categories_ in the work breakdown structure), tasks, items, or other aspects of your project. Each entry can have a workflow type of `original`, `revision`, `forecast`, `pending change`, `approved change`, or `other`.

Your project estimate can post entries to an existing GL budget that was configured for that project in the Sage Intacct UI. An optional [project estimate type](https://developer.intacct.com/api/construction/project-estimate-types/) lets you designate a subset of workflow types for posting to the GL budget.

You can create multiple project estimates for a given project/GL budget pairing. However, only one project estimate, known as the primary estimate, can post to the GL budget.

You can create individual entries at the same time you create the project estimate, or you can add entries to an existing estimate using one of the following approaches:

*   [Update the original estimate](https://developer.intacct.com/api/construction/project-estimates/#update-project-estimate) and provide new entries.
*   [Create new entries](https://developer.intacct.com/api/construction/project-estimates/#create-project-estimate-entry) independently and specify the ID of the owning estimate.

**Note:** As the project progresses, you can create [change requests](https://developer.intacct.com/api/construction/change-requests/) that update project estimate entries.

* * *

### Get Project Estimate Object Definition

#### `lookup`

> List all the fields and relationships for the project estimate object:

```
<lookup>
    <object>PJESTIMATE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATE` |

* * *

### Query and List Project Estimates

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and project estimate ID for each project estimate:

```
<query>
    <object>PJESTIMATE</object>
    <select>
        <field>RECORDNO</field>
        <field>PJESTIMATEID</field>
    </select>
</query> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATE` |
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

### Query and List Project Estimates (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>PJESTIMATE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Project Estimate

#### `read`

```
<read>
    <object>PJESTIMATE</object>
    <keys>12</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project estimate to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Project Estimate by ID

#### `readByName`

```
<readByName>
    <object>PJESTIMATE</object>
    <keys>PJE-BLD-01</keys>
    <fields>*</fields>
</readByName> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATE` |
| keys | Required | string | Comma-separated list of `PJESTIMATEID` of the project estimate to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Project Estimate

[History](https://developer.intacct.com/api/construction/project-estimates/#history-create-project-estimate)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added PRODUCTIONUNITS |
| 2020 Release 4 | Added ESTIMATEDATE, EFFECTIVEDATE, added new values for POSTTO |

#### `create`

```
<create>
    <PJESTIMATE>
        <PJESTIMATEID>PJE-BLD-01</PJESTIMATEID>
        <PROJECTID>19-100</PROJECTID>
        <ENTRIES>
            <PJESTIMATEENTRY>
                <AMOUNT>9550.00</AMOUNT>
                <WFTYPE>original</WFTYPE>
                <MEMO>Elec Subcontract</MEMO>
            </PJESTIMATEENTRY>
            <PJESTIMATEENTRY>
                <AMOUNT>2000.00</AMOUNT>
                <WFTYPE>original</WFTYPE>
                <MEMO>PM coordination</MEMO>
            </PJESTIMATEENTRY>
        </ENTRIES>
    </PJESTIMATE>
</create> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PJESTIMATE` | Required | object | Type of object to create. |

`PJESTIMATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PJESTIMATEID | Optional | string | Unique ID for the project estimate. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value. |
| DESCRIPTION | Optional | string | Description of the project estimate. |
| ISPRIMARY | Optional | boolean | Specifies whether this is the primary estimate for the project. Use `true` for primary, `false` otherwise. A project can have zero or one primary estimates and multiple non-primary estimates. The first estimate for a project is automatically set as primary when it is created. To set another estimate as primary, update the first estimate to set `ISPRIMARY` to `false` and then update the desired estimate to set it to `true`. (Default: `true` for the first estimate created for a project, `false` otherwise) |
| POSTED | Optional | boolean | Specifies whether the estimate posts entries to the GL budget. Use `true` to post to the entries. You can “unpost” an estimate by updating it and setting `POSTED` to `false`.(Default: `false`) |
| PJESTIMATETYPENAME | Optional | string | Name of a [project estimate type](https://developer.intacct.com/api/construction/project-estimate-types/) that defines a subset of workflow types. This subset specifies which entries post to the GL budget (if `POSTED` is `true`), and can be used for reporting purposes. When this parameter is not supplied, all workflow types post to the GL budget. If the given project estimate type doesn’t include workflow types, no entries post to the GL budget. |
| GLBUDGETID | Optional | string | ID of the existing GL budget to use. The budget must be configured for a project estimate in the Sage Intacct UI. |
| ESTIMATEDATE | Optional | string | Date of the project estimate, which must be in a budgetable period. Required if `POSTTO` is set to `Estimate date` and `POSTED` is `true`. The meaning of this date can vary according to the customer’s workflow. It can be the date the estimate was created, the date the estimate was presented as a quote, or the date of the forecast. Specified in the format `mm/dd/yyyy`. |
| POSTTO | Optional | boolean | GL Budget period, either `First period`, `All periods`, `Estimate date`, or `Effective date`. (Default: `First period`) |
| PROJECTID | Required | string | ID of the project for this estimate |
| STATUS | Optional | string | Status. Use `active`, `inactive`, or `finalized`. An estimate set to `finalized` cannot be modified other than to change its status. |
| ENTRIES | Optional | array of [PJESTIMATEENTRY](https://developer.intacct.com/api/construction/project-estimates/#create-PJESTIMATE.PJESTIMATEENTRY) | One or more estimate entries to create |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`PJESTIMATE.PJESTIMATEENTRY`

You can provide a specific amount for an entry, or you can specify a quantity and unit cost and the system will calculate the amount. If all three are provided, the specific amount is used instead of the calculation.

If you provide a value for production units, you can omit amount, quantity, and unit cost.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EUOM | Optional | string | External unit of measure. Free form field with 200 or fewer characters. |
| QTY | Optional | decimal | Quantity |
| UNITCOST | Optional | currency | Unit cost, also known as unit rate |
| AMOUNT | Optional | currency | Amount. Required if quantity and unit cost or production units are not supplied. |
| MEMO | Optional | string | Memo for the entry. Use 2000 or fewer characters. |
| WFTYPE | Optional | string (enum) | Workflow type for the entry.
*   `original` (default)
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

 |
| PRODUCTIONUNITS | Optional | numeric | Number of production units, which are units that track several inputs of cost (such as for material, labor, equipment). If specified, then amount, quantity, and unit cost all become optional. When specifying production units, you must also provide a task ID, from which the production unit description, if present, is inherited. (Construction subscription) |
| ACCOUNTNO | Optional | string | Account number |
| DEPARTMENTID | Optional | string | Department ID |
| CUSTOMERID | Optional | string | Customer ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CONTRACTID | Optional | string | Contract ID |
| TASKID | Optional | string | Task ID. Required if you specify production units. |
| COSTTYPEID | Optional | string | Cost type ID |
| VENDORID | Optional | string | Vendor ID |
| CLASSID | Optional | string | Class ID |
| EFFECTIVEDATE | Optional | string | Date that the transaction entry comes into effect from a GL budget or reporting perspective. This can be useful for differentiating approved change entries added later than original entries. Required if `POSTTO` is set to `Effective date` and `POSTED` is `true`. Specified in the format `mm/dd/yyyy`. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Project Estimate

[History](https://developer.intacct.com/api/construction/project-estimates/#history-update-project-estimate)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added PRODUCTIONUNITS |
| 2020 Release 4 | Added ESTIMATEDATE, EFFECTIVEDATE, added new values for POSTTO |

You can update header information for a project estimate, modify existing entries, or add new ones:

*   To modify the header information only, omit the array of entries altogether.
*   To update existing entries, specify their record numbers and the fields to change. You cannot update a project estimate entry if there is a [change request](https://developer.intacct.com/api/construction/change-requests/) entry that is linked to it.
*   To add new entries, provide the field information for the new entries (without record numbers).

You can only modify or add entries during an update, you cannot delete entries. Use the [delete](https://developer.intacct.com/api/construction/project-estimates/#delete-project-estimate-entry) function for this purpose.

**Note:** You can also [update an estimate entry directly](https://developer.intacct.com/api/construction/project-estimates/#update-project-estimate-entry) or [create new entries](https://developer.intacct.com/api/construction/project-estimates/#create-project-estimate-entry) independently.

#### `update`

> Updates the header of the project estimate created above, adding a description:

```
<update>
    <PJESTIMATE>
        <RECORDNO>12</RECORDNO>
        <DESCRIPTION>Building 1</DESCRIPTION>
    </PJESTIMATE>
</update> 
```

> Updates the same project estimate, modifying the amount of an existing entry and adding a new entry:

```
<update>
    <PJESTIMATE>
        <RECORDNO>12</RECORDNO>
        <ENTRIES>
            <PJESTIMATEENTRY>
                <RECORDNO>244</RECORDNO>
                <AMOUNT>10550.00</AMOUNT>
                <WFTYPE>original</WFTYPE>
                <MEMO>Elec Subcontract</MEMO>
            </PJESTIMATEENTRY>
            <PJESTIMATEENTRY>
                <AMOUNT>5000.00</AMOUNT>
                <WFTYPE>original</WFTYPE>
                <MEMO>Geology reports</MEMO>
            </PJESTIMATEENTRY>
        </ENTRIES>
    </PJESTIMATE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PJESTIMATE` | Required | object | Object to update |

`PJESTIMATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of the project estimate to update. Required if not providing the project estimate ID. |
| PJESTIMATEID | Optional | string | Unique ID of the project estimate. Required if not providing the record number. |
| DESCRIPTION | Optional | string | Description of the project estimate. Use 1000 or fewer characters. |
| ISPRIMARY | Optional | boolean | Specifies whether this is the primary estimate for the project. Use `true` for primary, `false` otherwise. A project can have zero or one primary estimates and multiple non-primary estimates. You cannot change `ISPRIMARY` to `false` if there are [change request](https://developer.intacct.com/api/construction/change-requests/) entries that are linked to it. |
| POSTED | Optional | boolean | Specifies whether the estimate posts entries to the GL budget. `true` posts the entries, `false` performs an unpost and deletes any existing GL budget entries. |
| PJESTIMATETYPENAME | Optional | string | Name of a [project estimate type](https://developer.intacct.com/api/construction/project-estimate-types/) that defines a subset of workflow types. This subset specifies which entries post to the GL budget (if `POSTED` is `true`), and can be used for reporting purposes. When this parameter is not supplied, all workflow types post to the GL budget. If the given project estimate type doesn’t include workflow types, no entries post to the GL budget. |
| GLBUDGETID | Optional | string | ID of the existing GL budget to use. The budget must be configured for a project estimate in the Sage Intacct UI. If you change the budget ID and `POSTED` is set to `true`, any previously posted budget entries are deleted and a new post to the specified GL budget is performed. |
| ESTIMATEDATE | Optional | string | Date of the project estimate, which must be in a budgetable period. Required if `POSTTO` is set to `Estimate date` and `POSTED` is `true`. The meaning of this date can vary according to the customer’s workflow. It can be the date the estimate was created, the date the estimate was presented as a quote, or the date of the forecast. Specified in the format `mm/dd/yyyy`. |
| POSTTO | Optional | boolean | GL Budget period, either `First period`, `All periods`, `Estimate date`, or `Effective date`. If you change the budget period and `POSTED` is set to `true`, any previously posted budget entries for that period are deleted and a new post for the specified period is performed. |
| STATUS | Optional | string | Status. Use `active`, `inactive`, or `finalized`. An estimate set to `finalized` cannot be modified other than to change its status. |
| ENTRIES | Optional | array of [PJESTIMATEENTRY](https://developer.intacct.com/api/construction/project-estimates/#update-PJESTIMATE.PJESTIMATEENTRY) | One or more estimate entries. You can add new entries or modify existing entries by supplying their record numbers. Omit this parameter to preserve the existing entries as they are. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`PJESTIMATE.PJESTIMATEENTRY`

You can provide a specific amount for the entry, or you can provide a quantity and unit cost and the system will calculate the amount. If all three are provided, the specific amount is used instead of the calculation.

If you provide a value for production units, you can omit amount, quantity, and unit cost.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of the project estimate to update. Omit this parameter to add a new entry. |
| EUOM | Optional | string | External unit of measure. Free form field with 200 or fewer characters. |
| QTY | Optional | decimal | Quantity |
| UNITCOST | Optional | currency | Unit cost, also known as unit rate |
| AMOUNT | Optional | currency | Amount. Required if quantity and unit cost or production units are not supplied. |
| MEMO | Optional | string | Memo for the entry. Use 2000 or fewer characters. |
| WFTYPE | Optional | string (enum) | Workflow type for the entry.
*   `original` (default)
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

 |
| PRODUCTIONUNITS | Optional | numeric | Number of production units, which are units that track several inputs of cost (such as for material, labor, equipment). If specified, then amount, quantity, and unit cost all become optional. When specifying production units, you must also provide a task ID, from which the production unit description, if present, is inherited. (Construction subscription) |
| ACCOUNTNO | Optional | string | Account number |
| DEPARTMENTID | Optional | string | Department ID |
| CUSTOMERID | Optional | string | Customer ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CONTRACTID | Optional | string | Contract ID |
| TASKID | Optional | string | Task ID. Required if you specify production units. |
| COSTTYPEID | Optional | string | Cost type ID |
| VENDORID | Optional | string | Vendor ID |
| CLASSID | Optional | string | Class ID |
| EFFECTIVEDATE | Optional | string | Date that the transaction entry comes into effect from a GL budget or reporting perspective. This can be useful for differentiating approved change entries added later than original entries. Required if `POSTTO` is set to `Effective date` and `POSTED` is `true`. Specified in the format `mm/dd/yyyy`. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Project Estimate

You cannot delete a primary or finalized project estimate, nor can you delete one with [change request](https://developer.intacct.com/api/construction/change-requests/) entries linked to it.

#### `delete`

```
<delete>
    <object>PJESTIMATE</object>
    <keys>12</keys>
</delete> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project estimate to delete |

* * *

Project Estimate Entries
------------------------

### Get Project Estimate Entry Object Definition

#### `lookup`

> List all the fields and relationships for the project estimate entry object:

```
<lookup>
    <object>PJESTIMATEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATEENTRY` |

* * *

### Query and List Project Estimate Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and project estimate ID for each project estimate entry:

```
<query>
    <object>PJESTIMATEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>PJESTIMATEID</field>
    </select>
</query> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATEENTRY` |
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

### Query and List Project Estimate Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>PJESTIMATEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Project Estimate Entry

#### `read`

```
<read>
    <object>PJESTIMATEENTRY</object>
    <keys>7</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project estimate entry to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Project Estimate Entry

[History](https://developer.intacct.com/api/construction/project-estimates/#history-create-project-estimate-entry)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added PRODUCTIONUNITS |
| 2020 Release 4 | Added EFFECTIVEDATE |

#### `create`

```
<create>
    <PJESTIMATEENTRY>
        <PJESTIMATEID>PJE-BLD-01</PJESTIMATEID>
        <WFTYPE>original</WFTYPE>
        <EUOM>yards</EUOM>
        <QTY>25</QTY>
        <UNITCOST>10.99</UNITCOST>
    </PJESTIMATEENTRY>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PJESTIMATEENTRY` | Required | object | Object to create |

`PJESTIMATEENTRY`

You can provide an amount for the entry, or you can specify a quantity and unit cost and the system will calculate the amount. If all three are provided, the specific amount is used instead of the calculation.

If you provide a value for production units, you can omit amount, quantity, and unit cost.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PJESTIMATEID | Required | string | Unique ID of the existing project estimate |
| EUOM | Optional | string | External unit of measure. Free form field with 200 or fewer characters. |
| QTY | Optional | decimal | Quantity |
| UNITCOST | Optional | currency | Unit cost, also known as unit rate |
| AMOUNT | Optional | currency | Amount. Required if quantity and unit cost or production units are not supplied. |
| MEMO | Optional | string | Memo for the entry. Use 2000 or fewer characters. |
| WFTYPE | Optional | string (enum) | Workflow type for the entry.
*   `original` (default)
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

 |
| PRODUCTIONUNITS | Optional | numeric | Number of production units, which are units that track several inputs of cost (such as for material, labor, equipment). If specified, then amount, quantity, and unit cost all become optional. When specifying production units, you must also provide a task ID, from which the production unit description, if present, is inherited. (Construction subscription) |
| ACCOUNTNO | Optional | string | Account number |
| DEPARTMENTID | Optional | string | Department ID |
| CUSTOMERID | Optional | string | Customer ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CONTRACTID | Optional | string | Contract ID |
| TASKID | Optional | string | Task ID. Required if you specify production units. |
| COSTTYPEID | Optional | string | Cost type ID |
| VENDORID | Optional | string | Vendor ID |
| CLASSID | Optional | string | Class ID |
| EFFECTIVEDATE | Optional | string | Date that the transaction entry comes into effect from a GL budget or reporting perspective. This can be useful for differentiating approved change entries added later than original entries. Required if `POSTTO` is set to `Effective date` and `POSTED` is `true`. Specified in the format `mm/dd/yyyy`. |
| customfields | optional | customfield\[0…n\] | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Project Estimate Entry

[History](https://developer.intacct.com/api/construction/project-estimates/#history-update-project-estimate-entry)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added PRODUCTIONUNITS |
| 2020 Release 4 | Added EFFECTIVEDATE |

You cannot update a project estimate entry if there is a [change request](https://developer.intacct.com/api/construction/change-requests/) entry that is linked to it.

#### `update`

```
<update>
    <PJESTIMATEENTRY>
        <RECORDNO>7</RECORDNO>
        <AMOUNT>700</AMOUNT>
        <WFTYPE>revision</WFTYPE>
    </PJESTIMATEENTRY>
</update> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PJESTIMATEENTRY` | Required | object | Object to update |

`PJESTIMATEENTRY`

You can provide an amount for the entry, or you can specify a quantity and unit cost and the system will calculate the amount. If all three are provided, the specific amount is used instead of the calculation.

If you provide a value for production units, you can omit amount, quantity, and unit cost.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the project estimate entry to update |
| EUOM | Optional | string | External unit of measure. Free form field with 200 or fewer characters. |
| QTY | Optional | decimal | Quantity |
| UNITCOST | Optional | currency | Unit cost, also known as unit rate |
| AMOUNT | Optional | currency | Amount. Required if quantity and unit cost or production units are not supplied. |
| MEMO | Optional | string | Memo for the entry. Use 2000 or fewer characters. |
| WFTYPE | Optional | string (enum) | Workflow type for the entry.
*   `original` (default)
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

 |
| PRODUCTIONUNITS | Optional | numeric | Number of production units, which are units that track several inputs of cost (such as for material, labor, equipment). If specified, then amount, quantity, and unit cost all become optional. When specifying production units, you must also provide a task ID, from which the production unit description, if present, is inherited. (Construction subscription) |
| ACCOUNTNO | Optional | string | Account number |
| DEPARTMENTID | Optional | string | Department ID |
| CUSTOMERID | Optional | string | Customer ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CONTRACTID | Optional | string | Contract ID |
| TASKID | Optional | string | Task ID. Required if you specify production units. |
| COSTTYPEID | Optional | string | Cost type ID |
| VENDORID | Optional | string | Vendor ID |
| CLASSID | Optional | string | Class ID |
| EFFECTIVEDATE | Optional | string | Date that the transaction entry comes into effect from a GL budget or reporting perspective. This can be useful for differentiating approved change entries added later than original entries. Required if `POSTTO` is set to `Effective date` and `POSTED` is `true`. Specified in the format `mm/dd/yyyy`. |
| customfields | optional | customfield\[0…n\] | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Project Estimate Entry

You cannot delete a project estimate entry if there is a [change request](https://developer.intacct.com/api/construction/change-requests/) entry that is linked to it.

#### `delete`

```
<delete>
    <object>PJESTIMATEENTRY</object>
    <keys>7</keys>
</delete> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project estimate entry to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

