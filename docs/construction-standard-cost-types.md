Title: Standard Cost Types

URL Source: https://developer.intacct.com/api/construction/standard-cost-types/

Markdown Content:
*   [Get Standard Cost Type Object Definition](https://developer.intacct.com/api/construction/standard-cost-types/#get-standard-cost-type-object-definition)
*   [Query and List Standard Cost Types](https://developer.intacct.com/api/construction/standard-cost-types/#query-and-list-standard-cost-types)
*   [Query and List Standard Cost Types (Legacy)](https://developer.intacct.com/api/construction/standard-cost-types/#query-and-list-standard-cost-types-legacy)
*   [Get Standard Cost Type](https://developer.intacct.com/api/construction/standard-cost-types/#get-standard-cost-type)
*   [Get Standard Cost Type by ID](https://developer.intacct.com/api/construction/standard-cost-types/#get-standard-cost-type-by-id)
*   [Create Standard Cost Type](https://developer.intacct.com/api/construction/standard-cost-types/#create-standard-cost-type)
*   [Update Standard Cost Type](https://developer.intacct.com/api/construction/standard-cost-types/#update-standard-cost-type)
*   [Delete Standard Cost Type](https://developer.intacct.com/api/construction/standard-cost-types/#delete-standard-cost-type)

* * *

You set up a catalog of standard cost types, such as labor, materials, and subcontracts, to use as templates for creating new cost types.

**Note:** Construction companies record expenses using the work breakdown structure (WBS). In the industry, the WBS is traditionally defined as job/cost code/category. Sage Intacct uses project/task/cost type to reflect this structure.

* * *

Get Standard Cost Type Object Definition
----------------------------------------

#### `lookup`

> List all the fields and relationships for the standard cost type object:

```
<lookup>
    <object>STANDARDCOSTTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDCOSTTYPE` |

* * *

Query and List Standard Cost Types
----------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and standard cost type ID for each cost type (with no filtering):

```
<query>
    <object>STANDARDCOSTTYPE</object>
    <select>
        <field>STANDARDCOSTTYPEID</field>
        <field>RECORDNO</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDCOSTTYPE` |
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

Query and List Standard Cost Types (Legacy)
-------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>STANDARDCOSTTYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDCOSTTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Standard Cost Type
----------------------

#### `read`

```
<read>
    <object>STANDARDCOSTTYPE</object>
    <keys>24</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDCOSTTYPE` |
| keys | Required | string | Comma-separated list of standard cost type `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Standard Cost Type by ID
----------------------------

#### `readByName`

```
<readByName>
    <object>STANDARDCOSTTYPE</object>
    <keys>LAB-REG</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDCOSTTYPE` |
| keys | Required | string | Comma-separated list of standard cost type `STANDARDCOSTTYPEID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Standard Cost Type
-------------------------

#### `create`

```
<create>
    <STANDARDCOSTTYPE>
        <STANDARDCOSTTYPEID>MAT</STANDARDCOSTTYPEID>
        <NAME>Material Cost Type</NAME>
        <DESCRIPTION>Materials</DESCRIPTION>
        <COSTUNITDESCRIPTION>Square feet</COSTUNITDESCRIPTION>
    </STANDARDCOSTTYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDCOSTTYPE | Required | object | Object to create |

`STANDARDCOSTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDCOSTTYPEID | Required | string | Unique standard cost type ID. Use 12 or fewer characters. |
| NAME | Required | string | Name of the standard cost type. Does not have to be unique. Use 200 or fewer characters. |
| DESCRIPTION | Optional | string | Description of the standard cost type. Use 1000 or fewer characters. |
| ACCUMULATIONTYPENAME | Optional | string | Accumulation type name. |
| COSTUNITDESCRIPTION | Optional | string | Cost unit description, such as feet or square yards. Use 30 or fewer characters. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| ACCOUNTNO | Optional | string | Account number |
| PARENTID | Optional | string | Parent standard cost type ID |
| ITEMID | Optional | string | Item ID |
| customfields | Optional | customfield\[0…n\] | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Standard Cost Type
-------------------------

#### `update`

```
<update>
    <STANDARDCOSTTYPE>
        <STANDARDCOSTTYPEID>LAB</STANDARDCOSTTYPEID>
        <DESCRIPTION>Hourly labor overtime</DESCRIPTION>
    </STANDARDCOSTTYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDCOSTTYPE | Required | object | Object to update |

`STANDARDCOSTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STANDARDCOSTTYPEID | Optional | string | Standard cost type ID for the object to update. Required if not using `RECORDNO`. |
| RECORDNO | Optional | integer | Record number of the standard cost type to update. Required if not using `STANDARDCOSTTYPEID`. |
| NAME | Optional | string | Name of the standard cost type. Use 12 or fewer characters. |
| DESCRIPTION | Optional | string | Description of the standard cost type. Use 200 or fewer characters. |
| ACCUMULATIONTYPENAME | Optional | string | Accumulation type name. |
| COSTUNITDESCRIPTION | Optional | string | Cost unit description, such as feet or square yards. Use 30 or fewer characters. |
| STATUS | Optional | string | Status. Use `active` or `inactive`. |
| ACCOUNTNO | Optional | string | Account number |
| PARENTID | Optional | string | Parent standard cost type ID |
| ITEMID | Optional | string | Item ID |
| customfields | Optional | customfield\[0…n\] | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Standard Cost Type
-------------------------

#### `delete`

```
<delete>
    <object>STANDARDCOSTTYPE</object>
    <keys>24</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `STANDARDCOSTTYPE` |
| keys | Required | string | Comma-separated list of standard cost type `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

