Title: Bank Interest Income / Charges

URL Source: https://developer.intacct.com/api/cash-management/bank-interest-charges/

Markdown Content:
*   [Bank Interest Income/Charges](https://developer.intacct.com/api/cash-management/bank-interest-charges/#bank-interest-incomecharges)
    *   [Get Bank Interest Income/Charge Object Definition](https://developer.intacct.com/api/cash-management/bank-interest-charges/#get-bank-interest-incomecharge-object-definition)
    *   [Query and List Bank Interest Income/Charges](https://developer.intacct.com/api/cash-management/bank-interest-charges/#query-and-list-bank-interest-incomecharges)
    *   [Query and List Bank Interest Income/Charges (Legacy)](https://developer.intacct.com/api/cash-management/bank-interest-charges/#query-and-list-bank-interest-incomecharges-legacy)
    *   [Get Bank Interest Income/Charge](https://developer.intacct.com/api/cash-management/bank-interest-charges/#get-bank-interest-incomecharge)
*   [Bank Interest Income Line/Charges](https://developer.intacct.com/api/cash-management/bank-interest-charges/#bank-interest-income-linecharges)
    *   [Get Bank Interest Income Line/Charge Line Object Definition](https://developer.intacct.com/api/cash-management/bank-interest-charges/#get-bank-interest-income-linecharge-line-object-definition)
    *   [Query and List Bank Interest Income Lines/Charge Lines](https://developer.intacct.com/api/cash-management/bank-interest-charges/#query-and-list-bank-interest-income-linescharge-lines)
    *   [Query and List Bank Interest Income Lines/Charge Lines (Legacy)](https://developer.intacct.com/api/cash-management/bank-interest-charges/#query-and-list-bank-interest-income-linescharge-lines-legacy)
    *   [Get Bank Interest Income Line/Charge Line](https://developer.intacct.com/api/cash-management/bank-interest-charges/#get-bank-interest-income-linecharge-line)

* * *

Encompasses bank interest and service charges.

* * *

### Get Bank Interest Income/Charge Object Definition

#### `lookup`

> List all the fields and relationships for the bank interest income/charge object:

```
<lookup>
    <object>BANKFEE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEE` |

* * *

### Query and List Bank Interest Income/Charges

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each interest or service charge record:

```
<query>
    <object>BANKFEE</object>
    <select>
        <field>DESCRIPTION</field>
        <field>RECORDNO</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEE` |
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

### Query and List Bank Interest Income/Charges (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>BANKFEE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TRANSACTIONTYPE | Optional | string | Transaction type. Use `ch` for Service charge, otherwise use `cn` for Interest earned. |

* * *

### Get Bank Interest Income/Charge

#### `read`

```
<read>
    <object>BANKFEE</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Bank Interest Income Line/Charges
---------------------------------

### Get Bank Interest Income Line/Charge Line Object Definition

#### `lookup`

> List all the fields and relationships for the bank interest income line/charge line object:

```
<lookup>
    <object>BANKFEEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEEENTRY` |

* * *

### Query and List Bank Interest Income Lines/Charge Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each interest or service charge line:

```
<query>
    <object>BANKFEEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEEENTRY` |
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

### Query and List Bank Interest Income Lines/Charge Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>BANKFEEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Bank Interest Income Line/Charge Line

#### `read`

```
<read>
    <object>BANKFEEENTRY</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKFEEENTRY` |
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

