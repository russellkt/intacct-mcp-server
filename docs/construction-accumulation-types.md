Title: Accumulation Types

URL Source: https://developer.intacct.com/api/construction/accumulation-types/

Markdown Content:
*   [Get Accumulation Type Object Definition](https://developer.intacct.com/api/construction/accumulation-types/#get-accumulation-type-object-definition)
*   [Query and List Accumulation Types](https://developer.intacct.com/api/construction/accumulation-types/#query-and-list-accumulation-types)
*   [Query and List Accumulation Types (Legacy)](https://developer.intacct.com/api/construction/accumulation-types/#query-and-list-accumulation-types-legacy)
*   [Get Accumulation Type](https://developer.intacct.com/api/construction/accumulation-types/#get-accumulation-type)
*   [Get Accumulation Type by ID](https://developer.intacct.com/api/construction/accumulation-types/#get-accumulation-type-by-id)
*   [Create Accumulation Type](https://developer.intacct.com/api/construction/accumulation-types/#create-accumulation-type)
*   [Update Accumulation Type](https://developer.intacct.com/api/construction/accumulation-types/#update-accumulation-type)
*   [Delete Accumulation Type](https://developer.intacct.com/api/construction/accumulation-types/#delete-accumulation-type)

* * *

Accumulation types let construction companies report on transaction costs across cost types.

An accumulation type is typically specified at the level of the standard cost type, but it can also be provided when creating an individual cost type.

* * *

Get Accumulation Type Object Definition
---------------------------------------

#### `lookup`

> List all the fields and relationships for the accumulation type object:

```
<lookup>
    <object>ACCUMULATIONTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCUMULATIONTYPE` |

* * *

Query and List Accumulation Types
---------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each accumulation type:

```
<query>
    <object>ACCUMULATIONTYPE</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCUMULATIONTYPE` |
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

Query and List Accumulation Types (Legacy)
------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ACCUMULATIONTYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCUMULATIONTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Accumulation Type
---------------------

#### `read`

```
<read>
    <object>ACCUMULATIONTYPE</object>
    <keys>8</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCUMULATIONTYPE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the accumulation type to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Accumulation Type by ID
---------------------------

#### `readByName`

```
<readByName>
    <object>ACCUMULATIONTYPE</object>
    <keys>Labor</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCUMULATIONTYPE` |
| keys | Required | string | Comma-separated list of `NAME` of the accumulation type to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Accumulation Type
------------------------

[History](https://developer.intacct.com/api/construction/accumulation-types/#history-create-accumulation-type)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Added COSTCATEGORY |

#### `create`

```
<create>
    <ACCUMULATIONTYPE>
        <NAME>Labor</NAME>
    </ACCUMULATIONTYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `ACCUMULATIONTYPE` | Required | object | Object to create |

`ACCUMULATIONTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Name for the accumulation type to create. Use 80 or fewer characters. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. (Default: `active`) |
| COSTCATEGORY | Optional | string | Standard cost categorizations for Construction projects. Use `Material`, `Labor`, `Equipment`, `Subcontract`, `Overhead`, `Other`, or a null value. |
| customfields | Optional | customfield\[0…n\] | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Accumulation Type
------------------------

[History](https://developer.intacct.com/api/construction/accumulation-types/#history-update-accumulation-type)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Added COSTCATEGORY |

#### `update`

```
<update>
    <ACCUMULATIONTYPE>
        <RECORDNO>8</RECORDNO>
        <STATUS>inactive</STATUS>
    </ACCUMULATIONTYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `ACCUMULATIONTYPE` | Required | object | Object to update |

`ACCUMULATIONTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Optional | integer | `Name` of the accumulation type to update. Required if not using `RECORDNO`. |
| RECORDNO | Optional | integer | `RECORDNO` of the accumulation type to update. Required if not using `NAME`. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| COSTCATEGORY | Optional | string | Standard cost categorizations for Construction projects. Use `Material`, `Labor`, `Equipment`, `Subcontract`, `Overhead`, `Other`, or a null value. |
| customfields | Optional | customfield\[0…n\] | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Accumulation Type
------------------------

#### `delete`

```
<delete>
    <object>ACCUMULATIONTYPE</object>
    <keys>8</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACCUMULATIONTYPE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the accumulation type to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

