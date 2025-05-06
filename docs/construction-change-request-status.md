Title: Change Request Status

URL Source: https://developer.intacct.com/api/construction/change-request-status/

Markdown Content:
*   [Get Change Request Status Object Definition](https://developer.intacct.com/api/construction/change-request-status/#get-change-request-status-object-definition)
*   [Query and List Change Request Statuses](https://developer.intacct.com/api/construction/change-request-status/#query-and-list-change-request-statuses)
*   [Query and List Change Request Statuses (Legacy)](https://developer.intacct.com/api/construction/change-request-status/#query-and-list-change-request-statuses-legacy)
*   [Get Change Request Status](https://developer.intacct.com/api/construction/change-request-status/#get-change-request-status)
*   [Get Change Request Status by ID](https://developer.intacct.com/api/construction/change-request-status/#get-change-request-status-by-id)
*   [Create Change Request Status](https://developer.intacct.com/api/construction/change-request-status/#create-change-request-status)
*   [Update Change Request Status](https://developer.intacct.com/api/construction/change-request-status/#update-change-request-status)
*   [Delete Change Request Status](https://developer.intacct.com/api/construction/change-request-status/#delete-change-request-status)

* * *

Construction companies can create their own user-defined statuses for change requests. A change request status is mapped to a workflow type, which controls whether change request entries post to the primary project estimate. A workflow type of `none` (the default) prevents change request entries from posting. Other workflow types, such as `pending change`, `approved change`, and so forth, result in posting.

As an example, you might map a status named `Not Issued` to the workflow type of `none`, or a status named `Approved Changes` to the `approved change` workflow type.

* * *

Get Change Request Status Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the change request status object:

```
<lookup>
    <object>CHANGEREQUESTSTATUS</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTSTATUS` |

* * *

Query and List Change Request Statuses
--------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List information for all change request statuses:

```
<query>
    <object>CHANGEREQUESTSTATUS</object>
    <select>
        <field>NAME</field>
        <field>WFTYPE</field>
        <field>RECORDNO</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTSTATUS` |
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

Query and List Change Request Statuses (Legacy)
-----------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CHANGEREQUESTSTATUS</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTSTATUS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

#### `read`

```
<read>
    <object>CHANGEREQUESTSTATUS</object>
    <keys>7</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTSTATUS` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the change request status to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Change Request Status by ID
-------------------------------

#### `readByName`

```
<readByName>
    <object>CHANGEREQUESTSTATUS</object>
    <keys>Approved Changes</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTSTATUS` |
| keys | Required | string | Comma-separated list of change request status IDs to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Change Request Status
----------------------------

#### `create`

> Creates a change request status named `Approved Changes` mapped to the workflow type of `approved changes`:

```
<create>
    <CHANGEREQUESTSTATUS>
        <NAME>Approved Changes</NAME>
        <WFTYPE>approved change</WFTYPE>
    </CHANGEREQUESTSTATUS>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUESTSTATUS | Required | object | Object to create |

`CHANGEREQUESTSTATUS`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Unique name for the change request status. Use 80 or fewer characters. |
| WFTYPE | Optional | string (enum) | Workflow type for the entry.
*   `none` (default)
*   `original`
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

 |
| STATUS | Optional | string | Status for the change request status. Use `active` or `inactive`. (Default: `active`) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Change Request Status
----------------------------

#### `update`

You can update a change request status that you identify either by record number or by name. You cannot change the name of an existing change request status.

> Updates the workflow type of a change request status to `approved change`:

```
<update>
    <CHANGEREQUESTSTATUS>
        <RECORDNO>14</RECORDNO>
        <WFTYPE>approved change</WFTYPE>
    </CHANGEREQUESTSTATUS>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUESTSTATUS | Required | object | Object to update |

`CHANGEREQUESTSTATUS`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | `RECORDNO` of the change request status to update. Required if not using `NAME` to specify an existing change request status. |
| NAME | Optional | string | Unique name of the change request status to update. Required if not using `RECORDNO` to specify an existing change request status. |
| WFTYPE | Optional | string (enum) | Workflow type for the entry.
*   `none` (default)
*   `original`
*   `revision`
*   `forecast`
*   `pending change`
*   `approved change`
*   `other`

 |
| use on an existing change request, its workflow type cannot be updated. |   |   |   |
| STATUS | Optional | string | Status for the change request status. Use `active` or `inactive`. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Change Request Status
----------------------------

You can delete a change request status only if it is not in use by a change request.

#### `delete`

```
<delete>
    <object>CHANGEREQUESTSTATUS</object>
    <keys>14</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTSTATUS` |
| keys | Required | integer | `RECORDNO` of the change request status to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

