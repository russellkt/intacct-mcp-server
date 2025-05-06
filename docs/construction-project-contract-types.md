Title: Project Contract Types

URL Source: https://developer.intacct.com/api/construction/project-contract-types/

Markdown Content:
*   [Get Project Contract Type Object Definition](https://developer.intacct.com/api/construction/project-contract-types/#get-project-contract-type-object-definition)
*   [Query and List Project Contract Types](https://developer.intacct.com/api/construction/project-contract-types/#query-and-list-project-contract-types)
*   [Get Project Contract Type](https://developer.intacct.com/api/construction/project-contract-types/#get-project-contract-type)
*   [Get Project Contract Type by ID](https://developer.intacct.com/api/construction/project-contract-types/#get-project-contract-type-by-id)
*   [Create Project Contract Type](https://developer.intacct.com/api/construction/project-contract-types/#create-project-contract-type)
*   [Update Project Contract Type](https://developer.intacct.com/api/construction/project-contract-types/#update-project-contract-type)
*   [Delete Delete Project Contract Type](https://developer.intacct.com/api/construction/project-contract-types/#delete-delete-project-contract-type)

* * *

Project contract types group project contracts for reporting purposes.

You specify a project contract type when creating [project contracts](https://developer.intacct.com/api/construction/project-contracts/).

* * *

Get Project Contract Type Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the project contract type object:

```
<lookup>
    <object>PROJECTCONTRACTTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTTYPE` |

* * *

Query and List Project Contract Types
-------------------------------------

#### `query`

> List the record number, ID, and name for each active project contract type:

```
<query>
    <object>PROJECTCONTRACTTYPE</object>
    <filter>
        <equalto>
            <field>STATUS</field>
            <value>active</value>
        </equalto>
    </filter>
    <select>
        <field>PROJECTCONTRACTTYPEID</field>
        <field>PROJECTCONTRACTTYPENAME</field>
        <field>RECORDNO</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTTYPE` |
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

Get Project Contract Type
-------------------------

#### `read`

```
<read>
    <object>PROJECTCONTRACTTYPE</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTTYPE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project contract type to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Project Contract Type by ID
-------------------------------

#### `readByName`

```
<readByName>
    <object>PROJECTCONTRACTTYPE</object>
    <keys>COM</keys>
    <fields>*</fields>
</readByName> 
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTTYPE` |
| keys | Required | string | Comma-separated list of `PROJECTCONTRACTTYPEID` of the project contract type to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Project Contract Type
----------------------------

#### `create`

```
<create>
    <PROJECTCONTRACTTYPE>
        <PROJECTCONTRACTTYPEID>COM</PROJECTCONTRACTTYPEID>
        <PROJECTCONTRACTTYPENAME>Commercial Contract</PROJECTCONTRACTTYPENAME>
    </PROJECTCONTRACTTYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCONTRACTTYPE | Required | object | Object to create |

`PROJECTCONTRACTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCONTRACTTYPEID | Required | string | Unique ID of the Project Contract Type. |
| PROJECTCONTRACTTYPENAME | Required | string | Name of the Project Contract Type. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Project Contract Type
----------------------------

You can use the `RECORDNO` or the `PROJECTCONTRACTTYPEID` to specify the project contract type to update. The only fields that can be changed are `PROJECTCONTRACTTYPENAME`, `STATUS` and any custom fields.

#### `update`

```
<update>
    <PROJECTCONTRACTTYPE>
        <PROJECTCONTRACTTYPE>COM</PROJECTCONTRACTTYPE>
        <STATUS>active</STATUS>
    </PROJECTCONTRACTTYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCONTRACTTYPE | Required | object | Object to update |

`PROJECTCONTRACTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | string | Record number of the project contract type to update. Required if not providing the project contract type ID. |
| PROJECTCONTRACTTYPEID | Optional | string | Unique ID of the project contract type. Required if not providing the record number. |
| PROJECTCONTRACTTYPENAME | Optional | string | Name of the Project Contract Type. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Delete Project Contract Type
-----------------------------------

#### `delete`

```
<delete>
    <object>PROJECTCONTRACTTYPE</object>
    <keys>3</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTTYPE` |
| keys | Required | string | Comma-separated list of project contract type `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

