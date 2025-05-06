Title: Contract Types

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/

Markdown Content:
*   [Get Contract Type Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#get-contract-type-object-definition)
*   [Query and List Contract Types](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#query-and-list-contract-types)
*   [Query and List Contract Types (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#query-and-list-contract-types-legacy)
*   [Get Contract Type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#get-contract-type)
*   [Get Contract Type by ID](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#get-contract-type-by-id)
*   [Create Contract Type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#create-contract-type)
*   [Update Contract Type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#update-contract-type)
*   [Delete Contract Type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/#delete-contract-type)

* * *

Contract types let you group contracts in meaningful ways to provide additional insight into your business.

After creating a contract type, you can create or update a contract with that type.

* * *

Get Contract Type Object Definition
-----------------------------------

#### `lookup`

> List all the fields and relationships for the contract type object:

```
<lookup>
    <object>CONTRACTTYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTTYPE` |

* * *

Query and List Contract Types
-----------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each contract type:

```
<query>
    <object>CONTRACTTYPE</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTTYPE` |
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

Query and List Contract Types (Legacy)
--------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTTYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTTYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active, `F` for Inactive |

* * *

Get Contract Type
-----------------

#### `read`

```
<read>
    <object>CONTRACTTYPE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTTYPE` |
| keys | Required | string | Comma-separated list of contract type `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Contract Type by ID
-----------------------

#### `readByName`

```
<readByName>
    <object>CONTRACTTYPE</object>
    <keys>Annually</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTTYPE` |
| keys | Required | string | Comma-separated list of contract type `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Contract Type
--------------------

#### `create`

```
<create>
    <CONTRACTTYPE>
        <NAME>Annually</NAME>
        <PARENT>
            <NAME>Auto-renewal</NAME>
        </PARENT>
        <STATUS>active</STATUS>
        <DESCRIPTION>Annual cycle</DESCRIPTION>
    </CONTRACTTYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTTYPE | Required | object | Object to create |

`CONTRACTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Contract type name |
| DESCRIPTION | Optional | string | Description |
| PARENT | Optional | object | Parent contract type |
| STATUS | Optional | string | Status. Use `active` for Active or `inactive` for Inactive. (Default: `active`) |

`PARENT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Parent contract type name |

* * *

Update Contract Type
--------------------

#### `update`

```
<update>
    <CONTRACTTYPE>
        <RECORDNO>1</RECORDNO>
        <STATUS>inactive</STATUS>
    </CONTRACTTYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTTYPE | Required | object | Object to update |

`CONTRACTTYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of Contract type |
| NAME | Optional | string | Contract type name |
| DESCRIPTION | Optional | string | Description |
| PARENT | Optional | object | Parent contract type |
| STATUS | Optional | string | Status. Use `active` for Active or `inactive` for Inactive. |

`PARENT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Parent contract type name |

* * *

Delete Contract Type
--------------------

#### `delete`

```
<delete>
    <object>CONTRACTTYPE</object>
    <keys>2</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTTYPE` |
| keys | Required | string | Comma-separated list of contract type `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

