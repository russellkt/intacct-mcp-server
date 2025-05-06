Title: Account Group Purposes

URL Source: https://developer.intacct.com/api/general-ledger/account-group-purposes/

Markdown Content:
*   [Get Account Group Purpose Object Definition](https://developer.intacct.com/api/general-ledger/account-group-purposes/#get-account-group-purpose-object-definition)
*   [Query and List Account Group Purposes](https://developer.intacct.com/api/general-ledger/account-group-purposes/#query-and-list-account-group-purposes)
*   [Query and List Account Group Purposes (Legacy)](https://developer.intacct.com/api/general-ledger/account-group-purposes/#query-and-list-account-group-purposes-legacy)
*   [Get Account Group Purpose](https://developer.intacct.com/api/general-ledger/account-group-purposes/#get-account-group-purpose)
*   [Get Account Group Purpose by ID](https://developer.intacct.com/api/general-ledger/account-group-purposes/#get-account-group-purpose-by-id)
*   [Create Account Group Purpose](https://developer.intacct.com/api/general-ledger/account-group-purposes/#create-account-group-purpose)
*   [Update Account Group Purpose](https://developer.intacct.com/api/general-ledger/account-group-purposes/#update-account-group-purpose)
*   [Delete Account Group Purpose](https://developer.intacct.com/api/general-ledger/account-group-purposes/#delete-account-group-purpose)

* * *

Account group purposes let you filter account groups according to why you might use them, which is particularly useful in financial reporting. You create account group purposes, which you can then designate when creating or updating your account groups.

* * *

Get Account Group Purpose Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the account group purpose object:

```
<lookup>
    <object>GLACCTGRPPURPOSE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPPURPOSE` |

* * *

Query and List Account Group Purposes
-------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each account group purpose:

```
<query>
    <object>GLACCTGRPPURPOSE</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPPURPOSE` |
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

Query and List Account Group Purposes (Legacy)
----------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>GLACCTGRPPURPOSE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPPURPOSE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active and `F` for Inactive. |

* * *

Get Account Group Purpose
-------------------------

#### `read`

```
<read>
    <object>GLACCTGRPPURPOSE</object>
    <keys>11</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPPURPOSE` |
| keys | Required | string | Comma-separated list of account group purpose `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Account Group Purpose by ID
-------------------------------

#### `readByName`

```
<readByName>
    <object>GLACCTGRPPURPOSE</object>
    <keys>Budgeted Expenses</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPPURPOSE` |
| keys | Required | string | Comma-separated list of account group purpose name to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Account Group Purpose
----------------------------

#### `create`

```
<create>
    <GLACCTGRPPURPOSE>
        <NAME>Budgeted Expenses</NAME>
    </GLACCTGRPPURPOSE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTGRPPURPOSE | Required | object | Object to update |

`GLACCTGRPPURPOSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Name for the account group purpose |
| STATUS | Optional | boolean | Status of account group purpose. Use `active` or `inactive`. (Default: `active`) |

* * *

Update Account Group Purpose
----------------------------

#### `update`

```
<update>
    <GLACCTGRPPURPOSE>
        <RECORDNO>6</RECORDNO>
        <STATUS>inactive</STATUS>
    </GLACCTGRPPURPOSE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTGRPPURPOSE | Required | object | Object to update |

`GLACCTGRPPURPOSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of account group purpose to update. |
| STATUS | Optional | string | Use `active` for Active, otherwise `inactive` for Inactive. |

* * *

Delete Account Group Purpose
----------------------------

#### `delete`

```
<delete>
    <object>GLACCTGRPPURPOSE</object>
    <keys>6</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPPURPOSE` |
| keys | Required | string | Comma-separated list of account group purpose `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

