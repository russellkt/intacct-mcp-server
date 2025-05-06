Title: Expense Payment Types

URL Source: https://developer.intacct.com/api/employee-expenses/expense-payment-types/

Markdown Content:
*   [Get Expense Payment Type Object Definition](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#get-expense-payment-type-object-definition)
*   [Query and List Expense Payment Types](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#query-and-list-expense-payment-types)
*   [Query and List Expense Payment Types (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#query-and-list-expense-payment-types-legacy)
*   [Get Expense Payment Type](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#get-expense-payment-type)
*   [Get Expense Payment Type by ID](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#get-expense-payment-type-by-id)
*   [Create Expense Payment Type (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#create-expense-payment-type-legacy)
*   [Update Expense Payment Type (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#update-expense-payment-type-legacy)
*   [Delete Expense Payment Type (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-payment-types/#delete-expense-payment-type-legacy)

* * *

Expense payment types are used to track how expenses are paid, such as by a company credit card.

* * *

Get Expense Payment Type Object Definition
------------------------------------------

#### `lookup`

> List all the fields and relationships for the expense payment type object:

```
<lookup>
    <object>EXPENSEPAYMENTTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEPAYMENTTYPE` |

* * *

Query and List Expense Payment Types
------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, name, and description for each expense payment type:

```
<query>
    <object>EXPENSEPAYMENTTYPE</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEPAYMENTTYPE` |
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

Query and List Expense Payment Types (Legacy)
---------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>EXPENSEPAYMENTTYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEPAYMENTTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Expense Payment Type
------------------------

#### `read`

```
<read>
    <object>EXPENSEPAYMENTTYPE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEPAYMENTTYPE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Expense Payment Type by ID
------------------------------

#### `readByName`

```
<readByName>
    <object>EXPENSEPAYMENTTYPE</object>
    <keys>Full Time</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXPENSEPAYMENTTYPE` |
| keys | Required | string | Comma-separated list of object `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Expense Payment Type (Legacy)
------------------------------------

#### `create_expensepaymenttype`

```
<create_expensepaymenttype>
    <name>VISA1544</name>
    <description>Corporate VISA ending 1544</description>
    <nonreimbursable>true</nonreimbursable>
    <offsetacctno>2165</offsetacctno>
</create_expensepaymenttype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Expense payment name to create |
| description | Optional | string | Description |
| nonreimbursable | Optional | boolean | Non-reimbursable. Use `false` for No, `true` for Yes. (Default: `false`) |
| offsetacctno | Optional | string | Offset account number |
| status | Optional | string | Expense payment type status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Update Expense Payment Type (Legacy)
------------------------------------

#### `update_expensepaymenttype`

```
<update_expensepaymenttype name="VISA1544">
    <offsetacctno>2180</offsetacctno>
</update_expensepaymenttype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Expense payment name to update |
| description | Optional | string | Description |
| nonreimbursable | Optional | boolean | Non-reimbursable. Use `false` for No, `true` for Yes. |
| offsetacctno | Optional | string | Offset account number |
| status | Optional | string | Expense payment type status. Use `active` for Active otherwise use `inactive` for Inactive. |

* * *

Delete Expense Payment Type (Legacy)
------------------------------------

#### `delete_expensepaymenttype`

```
<delete_expensepaymenttype name="VISA1544"></delete_expensepaymenttype>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Expense payment name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

