Title: Credit Card Charges/Other Fees

URL Source: https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/

Markdown Content:
*   [Credit Card Charges/Other Fees](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#credit-card-chargesother-fees)
    *   [Get Credit Card Charges/Other Fees Object Definition](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#get-credit-card-chargesother-fees-object-definition)
    *   [Query and List Credit Card Charges/Other Fees](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#query-and-list-credit-card-chargesother-fees)
    *   [Query and List Credit Card Charges/Other Fees (Legacy)](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#query-and-list-credit-card-chargesother-fees-legacy)
    *   [Get Credit Card Charge/Other Fee](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#get-credit-card-chargeother-fee)
*   [Credit Card Charges/Other Fee Lines](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#credit-card-chargesother-fee-lines)
    *   [Get Credit Card Charges/Other Fee Line Object Definition](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#get-credit-card-chargesother-fee-line-object-definition)
    *   [Query and List Credit Card Charge/Other Fee Lines](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#query-and-list-credit-card-chargeother-fee-lines)
    *   [Query and List Credit Card Charge Lines/Other Fee Lines (Legacy)](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#query-and-list-credit-card-charge-linesother-fee-lines-legacy)
    *   [Get Credit Card Charge Line/Other Fee Line](https://developer.intacct.com/api/cash-management/credit-card-charges-other-fees/#get-credit-card-charge-lineother-fee-line)

* * *

Encompasses finance charges, late charges, and other fees for a credit card.

* * *

### Get Credit Card Charges/Other Fees Object Definition

#### `lookup`

> List all the fields and relationships for the credit card charges/other fees object:

```
<lookup>
    <object>CREDITCARDFEE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEE` |

* * *

### Query and List Credit Card Charges/Other Fees

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each credit card charge / other fee:

```
<query>
    <object>CREDITCARDFEE</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEE` |
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

### Query and List Credit Card Charges/Other Fees (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CREDITCARDFEE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Credit Card Charge/Other Fee

#### `read`

```
<read>
    <object>CREDITCARDFEE</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Credit Card Charges/Other Fee Lines
-----------------------------------

### Get Credit Card Charges/Other Fee Line Object Definition

#### `lookup`

> List all the fields and relationships for the credit card charges/other fees line object:

```
<lookup>
    <object>CREDITCARDFEEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEEENTRY` |

* * *

### Query and List Credit Card Charge/Other Fee Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each credit card charge / other fee line:

```
<query>
    <object>CREDITCARDFEEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEEENTRY` |
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

### Query and List Credit Card Charge Lines/Other Fee Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CREDITCARDFEEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Credit Card Charge Line/Other Fee Line

#### `read`

```
<read>
    <object>CREDITCARDFEEENTRY</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CREDITCARDFEEENTRY` |
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

