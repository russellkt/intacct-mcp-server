Title: Fund Transfers

URL Source: https://developer.intacct.com/api/cash-management/fund-transfers/

Markdown Content:
*   [Fund Transfers](https://developer.intacct.com/api/cash-management/fund-transfers/#fund-transfers)
    *   [Get Funds Transfer Object Definition](https://developer.intacct.com/api/cash-management/fund-transfers/#get-funds-transfer-object-definition)
    *   [Query and List Fund Transfers](https://developer.intacct.com/api/cash-management/fund-transfers/#query-and-list-fund-transfers)
    *   [Query and List Fund Transfers (Legacy)](https://developer.intacct.com/api/cash-management/fund-transfers/#query-and-list-fund-transfers-legacy)
    *   [Get Fund Transfer](https://developer.intacct.com/api/cash-management/fund-transfers/#get-fund-transfer)
*   [Fund Transfer Lines](https://developer.intacct.com/api/cash-management/fund-transfers/#fund-transfer-lines)
    *   [Get Funds Transfer Line Object Definition](https://developer.intacct.com/api/cash-management/fund-transfers/#get-funds-transfer-line-object-definition)
    *   [Query and List Fund Transfer Lines](https://developer.intacct.com/api/cash-management/fund-transfers/#query-and-list-fund-transfer-lines)
    *   [Query and List Fund Transfer Lines (Legacy)](https://developer.intacct.com/api/cash-management/fund-transfers/#query-and-list-fund-transfer-lines-legacy)
    *   [Get Fund Transfer Line](https://developer.intacct.com/api/cash-management/fund-transfers/#get-fund-transfer-line)

* * *

Transaction record for the transfer of funds from one cash account to another.

* * *

### Get Funds Transfer Object Definition

#### `lookup`

> List all the fields and relationships for the funds transfer object:

```
<lookup>
    <object>FUNDSTRANSFER</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFER` |

* * *

### Query and List Fund Transfers

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and total entered for each fund transfer:

```
<query>
    <object>FUNDSTRANSFER</object>
    <select>
        <field>RECORDNO</field>
        <field>TOTALENTERED</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFER` |
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

### Query and List Fund Transfers (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>FUNDSTRANSFER</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFER` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Fund Transfer

#### `read`

```
<read>
    <object>FUNDSTRANSFER</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFER` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Fund Transfer Lines
-------------------

### Get Funds Transfer Line Object Definition

#### `lookup`

> List all the fields and relationships for the funds transfer line object:

```
<lookup>
    <object>FUNDSTRANSFER</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFERENTRY` |

* * *

### Query and List Fund Transfer Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, account number, and amount for each fund transfer line :

```
<query>
    <object>FUNDSTRANSFERENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCOUNTNO</field>
        <field>AMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFERENTRY` |
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

### Query and List Fund Transfer Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>FUNDSTRANSFERENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFERENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Fund Transfer Line

#### `read`

```
<readByQuery>
    <object>FUNDSTRANSFERENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `FUNDSTRANSFERENTRY` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

