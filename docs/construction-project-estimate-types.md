Title: Project Estimate Types

URL Source: https://developer.intacct.com/api/construction/project-estimate-types/

Markdown Content:
*   [Get Project Estimate Type Object Definition](https://developer.intacct.com/api/construction/project-estimate-types/#get-project-estimate-type-object-definition)
*   [Query and List Project Estimate Types](https://developer.intacct.com/api/construction/project-estimate-types/#query-and-list-project-estimate-types)
*   [Query and List Project Estimate Types (Legacy)](https://developer.intacct.com/api/construction/project-estimate-types/#query-and-list-project-estimate-types-legacy)
*   [Get Project Estimate Type](https://developer.intacct.com/api/construction/project-estimate-types/#get-project-estimate-type)
*   [Get Project Estimate Type by ID](https://developer.intacct.com/api/construction/project-estimate-types/#get-project-estimate-type-by-id)
*   [Create Project Estimate Type](https://developer.intacct.com/api/construction/project-estimate-types/#create-project-estimate-type)
*   [Update Project Estimate Type](https://developer.intacct.com/api/construction/project-estimate-types/#update-project-estimate-type)
*   [Delete Project Estimate Type](https://developer.intacct.com/api/construction/project-estimate-types/#delete-project-estimate-type)

* * *

Project estimate types categorize project estimates for reporting purposes and for filtering which project estimate entries post to the GL.

You specify a project estimate type when creating [project estimates](https://developer.intacct.com/api/construction/project-estimates/).

* * *

Get Project Estimate Type Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the project estimate type object:

```
<lookup>
    <object>PJESTIMATETYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATETYPE` |

* * *

Query and List Project Estimate Types
-------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the name, record number, and selected workflow types for each project estimate type:

```
<query>
    <object>PJESTIMATETYPE</object>
    <select>
        <field>NAME</field>
        <field>RECORDNO</field>
        <field>SELECTEDWFTYPES</field>
    </select>
</query> 
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATETYPE` |
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

Query and List Project Estimate Types (Legacy)
----------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PJESTIMATETYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery> 
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATETYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Project Estimate Type
-------------------------

#### `read`

```
<read>
    <object>PJESTIMATETYPE</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATETYPE` |
| keys | Required | string | Comma-separated list of project estimate type `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Project Estimate Type by ID
-------------------------------

#### `readByName`

```
<readByName>
    <object>PJESTIMATETYPE</object>
    <keys>Post all</keys>
    <fields>*</fields>
</readByName> 
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATETYPE` |
| keys | Required | string | Comma-separated list of project estimate type `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Project Estimate Type
----------------------------

[History](https://developer.intacct.com/api/construction/project-estimate-types/#history-create-project-estimate-type)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Added ESTIMATECATEGORY |

#### `create`

```
<create>
    <PJESTIMATETYPE>
        <NAME>Revision</NAME>
        <SELECTEDWFTYPES>original#~#revision</SELECTEDWFTYPES>
    </PJESTIMATETYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PJESTIMATETYPE | Required | object | Object to create |

`PJESTIMATETYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Name of the project estimate type, which must be unique. Use 80 or fewer characters. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| SELECTEDWFTYPES | Optional | string | One or more workflow types.
*   `original`
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

Implode multiple workflow types with `#~#`, for example, `original#~#revision`. |
| ESTIMATECATEGORY | Optional | string | Standard project estimate categories for Construction projects. Use one of the following or a null value:

*   `Current Estimate`
*   `Original Estimate`
*   `Current Forecast - At Completion`
*   `Historical Forecast - At Completion`
*   `Future Forecast - At Completion`
*   `Current Forecast - To Completion`
*   `Historical Forecast - To Completion`
*   `Future Forecast - To Completion`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Project Estimate Type
----------------------------

[History](https://developer.intacct.com/api/construction/project-estimate-types/#history-update-project-estimate-type)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Added ESTIMATECATEGORY |

#### `update`

```
<update>
    <PJESTIMATETYPE>
        <NAME>Revision</NAME>
        <SELECTEDWFTYPES>revision</SELECTEDWFTYPES>
    </PJESTIMATETYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PJESTIMATETYPE | Required | object | Object to update |

`PJESTIMATETYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Optional | string | Name of the project estimate type to update. Required if not providing a record number. |
| RECORDNO | Optional | integer | Record number of the project estimate type to update. Required if not providing a name. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| SELECTEDWFTYPES | Optional | string | One or more workflow types.
*   `original`
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

Implode multiple workflow types with `#~#`, for example, `original#~#revision`. The values supplied are a complete replacement of the existing set. |
| ESTIMATECATEGORY | Optional | string | Standard project estimate categories for Construction projects. Use one of the following or a null value:

*   `Current Estimate`
*   `Original Estimate`
*   `Current Forecast - At Completion`
*   `Historical Forecast - At Completion`
*   `Future Forecast - At Completion`
*   `Current Forecast - To Completion`
*   `Historical Forecast - To Completion`
*   `Future Forecast - To Completion`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Project Estimate Type
----------------------------

#### `delete`

```
<delete>
    <object>PJESTIMATETYPE</object>
    <keys>3</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PJESTIMATETYPE` |
| keys | Required | string | Comma-separated list of project estimate type `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

