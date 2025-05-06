Title: Earning Types

URL Source: https://developer.intacct.com/api/project-resource-mgmt/earning-types/

Markdown Content:
*   [Get Earning Type Object Definition](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#get-earning-type-object-definition)
*   [Query and List Earning Type](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#query-and-list-earning-type)
*   [Query and List Earning Types (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#query-and-list-earning-types-legacy)
*   [Get Earning Type](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#get-earning-type)
*   [Get Earning Type by ID](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#get-earning-type-by-id)
*   [Create Earning Type (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#create-earning-type-legacy)
*   [Update Earning Type (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#update-earning-type-legacy)
*   [Delete Earning Type (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/earning-types/#delete-earning-type-legacy)

* * *

Earning types help configure the system to post project labor costs to one or more general ledger journals.

* * *

Get Earning Type Object Definition
----------------------------------

#### `lookup`

> List all the fields and relationships for the earning type object:

```
<lookup>
    <object>EARNINGTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EARNINGTYPE` |

* * *

Query and List Earning Type
---------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, name, and method for each earning type:

```
<query>
    <object>EARNINGTYPE</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
        <field>METHOD</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EARNINGTYPE` |
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

Query and List Earning Types (Legacy)
-------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>EARNINGTYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EARNINGTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Earning Type
----------------

#### `read`

```
<read>
    <object>EARNINGTYPE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EARNINGTYPE` |
| keys | Required | string | Comma-separated list of earning type `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Earning Type by ID
----------------------

#### `readByName`

```
<readByName>
    <object>EARNINGTYPE</object>
    <keys>TEST</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EARNINGTYPE` |
| keys | Required | string | Comma-separated list of earning type name to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Earning Type (Legacy)
----------------------------

#### `create_earningtype`

```
<create_earningtype>
    <name>Full Time</name>
    <method>Salary</method>
    <billableacctno></billableacctno>
    <nonbillableacctno></nonbillableacctno>
    <ratemultiplier></ratemultiplier>
</create_earningtype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Earning type name to create |
| method | Required | string | Method. Use `Salary` or `Hourly` (Default: `Salary`) |
| billableacctno | Required | string | Billable account number |
| nonbillableacctno | Required | string | Non-billable account number |
| ratemultiplier | Optional | number | Rate multiplier |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Earning Type (Legacy)
----------------------------

#### `update_earningtype`

```
<update_earningtype key="Full Time">
    <method>Salary</method>
    <billableacctno></billableacctno>
    <nonbillableacctno></nonbillableacctno>
    <ratemultiplier></ratemultiplier>
</update_earningtype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Earning type name to update |
| method | Optional | string | Method. Use `Salary` or `Hourly`. |
| billableacctno | Optional | string | Billable account number |
| nonbillableacctno | Optional | string | Non-billable account number |
| ratemultiplier | Optional | number | Rate multiplier |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Earning Type (Legacy)
----------------------------

#### `delete_earningtype`

```
<delete_earningtype key="Full Time"></delete_earningtype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Earning type name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

