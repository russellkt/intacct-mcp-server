Title: Expense Types

URL Source: https://developer.intacct.com/api/employee-expenses/expense-types/

Markdown Content:
*   [Get Expense Type Object Definition](https://developer.intacct.com/api/employee-expenses/expense-types/#get-expense-type-object-definition)
*   [Query and List Expense Types](https://developer.intacct.com/api/employee-expenses/expense-types/#query-and-list-expense-types)
*   [Query and List Expense Types (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-types/#query-and-list-expense-types-legacy)
*   [Get Expense Type](https://developer.intacct.com/api/employee-expenses/expense-types/#get-expense-type)
*   [Get Expense Type by ID](https://developer.intacct.com/api/employee-expenses/expense-types/#get-expense-type-by-id)
*   [Create Expense Type](https://developer.intacct.com/api/employee-expenses/expense-types/#create-expense-type)
*   [Create Expense Type (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-types/#create-expense-type-legacy)
*   [Update Expense Type](https://developer.intacct.com/api/employee-expenses/expense-types/#update-expense-type)
*   [Update Expense Type (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-types/#update-expense-type-legacy)
*   [Delete Expense Type](https://developer.intacct.com/api/employee-expenses/expense-types/#delete-expense-type)
*   [Delete Expense Type (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-types/#delete-expense-type-legacy)

* * *

An expense type is a user-defined type that is applied to line items in an expense report or expense adjustment.

* * *

Get Expense Type Object Definition
----------------------------------

#### `lookup`

> List all the fields and relationships for the expense type object:

```
<lookup>
    <object>EEACCOUNTLABEL</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEACCOUNTLABEL` |

* * *

Query and List Expense Types
----------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each expense type:

```
<query>
    <object>EEACCOUNTLABEL</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEACCOUNTLABEL` |
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

Query and List Expense Types (Legacy)
-------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>EEACCOUNTLABEL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEACCOUNTLABEL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Expense Type
----------------

#### `read`

```
<read>
    <object>EEACCOUNTLABEL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of expense type `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Expense Type by ID
----------------------

#### `readByName`

```
<readByName>
    <object>EEACCOUNTLABEL</object>
    <keys>Travel Expenses</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of expense type `ACCOUNTLABEL` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Expense Type
-------------------

#### `create`

```
<create>
    <EEACCOUNTLABEL>
        <ACCOUNTLABEL>Travel Expenses</ACCOUNTLABEL>
        <DESCRIPTION>Travel Expenses</DESCRIPTION>
        <GLACCOUNTNO>6080</GLACCOUNTNO>
        <OFFSETGLACCOUNTNO></OFFSETGLACCOUNTNO>
        <STATUS>active</STATUS>
    </EEACCOUNTLABEL>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EEACCOUNTLABEL | Required | object | Object to create |

`EEACCOUNTLABEL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTLABEL | Required | string | Expense type to create |
| DESCRIPTION | Required | string | Description |
| GLACCOUNTNO | Required | string | Account number |
| OFFSETGLACCOUNTNO | Optional | string | Offset GL account number |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Create Expense Type (Legacy)
----------------------------

#### `create_expensetype`

```
<create_expensetype>
    <glaccountno>6080</glaccountno>
    <expensetype>Travel Expenses</expensetype>
    <description>Travel Expenses</description>
    <offsetglaccountno></offsetglaccountno>
    <status>active</status>
</create_expensetype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Account number |
| expensetype | Required | string | Expense type to create |
| description | Required | string | Description |
| offsetglaccountno | Optional | string | Offset GL account number |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Update Expense Type
-------------------

#### `update`

```
<update>
    <EEACCOUNTLABEL>
        <RECORDNO>12</RECORDNO>
        <DESCRIPTION>Travel Expenses</DESCRIPTION>
        <GLACCOUNTNO>6080</GLACCOUNTNO>
        <OFFSETGLACCOUNTNO></OFFSETGLACCOUNTNO>
        <STATUS>active</STATUS>
    </EEACCOUNTLABEL>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EEACCOUNTLABEL | Required | object | Object to update |

`EEACCOUNTLABEL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of expense type to update. Required if not using `ACCOUNTLABEL`. |
| ACCOUNTLABEL | Optional | string | Account label. Required if not using `RECORDNO`. |
| DESCRIPTION | Optional | string | Description |
| GLACCOUNTNO | Optional | string | Account number |
| OFFSETGLACCOUNTNO | Optional | string | Offset GL account number |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Update Expense Type (Legacy)
----------------------------

#### `update_expensetype`

```
<update_expensetype expensetype="Travel Expenses">
    <glaccountno>6090</glaccountno>
</update_expensetype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expensetype | Required | string | Expense type to update |
| glaccountno | Optional | string | Account number |
| description | Optional | string | Description |
| offsetglaccountno | Optional | string | Offset GL account number |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |

* * *

Delete Expense Type
-------------------

#### `delete`

```
<delete>
    <object>EEACCOUNTLABEL</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EEACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of expense type `RECORDNO` to delete |

* * *

Delete Expense Type (Legacy)
----------------------------

#### `delete_expensetype`

```
<delete_expensetype expensetype="Travel Expenses"></delete_expensetype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expensetype | Required | string | Expense type to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

