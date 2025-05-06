Title: Charge Payoffs

URL Source: https://developer.intacct.com/api/cash-management/charge-payoffs/

Markdown Content:
*   [Charge Payoffs](https://developer.intacct.com/api/cash-management/charge-payoffs/#charge-payoffs)
    *   [Get Charge Payoff Object Definition](https://developer.intacct.com/api/cash-management/charge-payoffs/#get-charge-payoff-object-definition)
    *   [Query and List Charge Payoffs](https://developer.intacct.com/api/cash-management/charge-payoffs/#query-and-list-charge-payoffs)
    *   [Query and List Charge Payoffs (Legacy)](https://developer.intacct.com/api/cash-management/charge-payoffs/#query-and-list-charge-payoffs-legacy)
    *   [Get Charge Payoff](https://developer.intacct.com/api/cash-management/charge-payoffs/#get-charge-payoff)
*   [Charge Payoff Lines](https://developer.intacct.com/api/cash-management/charge-payoffs/#charge-payoff-lines)
    *   [Get Charge Payoff Line Object Definition](https://developer.intacct.com/api/cash-management/charge-payoffs/#get-charge-payoff-line-object-definition)
    *   [Query and List Charge Payoff Lines](https://developer.intacct.com/api/cash-management/charge-payoffs/#query-and-list-charge-payoff-lines)
    *   [Query and List Charge Payoff Lines (Legacy)](https://developer.intacct.com/api/cash-management/charge-payoffs/#query-and-list-charge-payoff-lines-legacy)
    *   [Get Charge Payoff Line](https://developer.intacct.com/api/cash-management/charge-payoffs/#get-charge-payoff-line)

* * *

Transaction record for the payoff of a credit card.

* * *

### Get Charge Payoff Object Definition

#### `lookup`

> List all the fields and relationships for the charge payoff object:

```
<lookup>
    <object>CHARGEPAYOFF</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHARGEPAYOFF` |

* * *

### Query and List Charge Payoffs

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and total transaction amount for each charge payoff:

```
<query>
    <object>CHARGEPAYOFF</object>
    <select>
        <field>RECORDNO</field>
        <field>TRX_TOTALENTERED</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHARGEPAYOFF` |
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

### Query and List Charge Payoffs (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CHARGEPAYOFF</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHARGEPAYOFF` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Charge Payoff

#### `read`

```
<read>
    <object>CHARGEPAYOFF</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHARGEPAYOFF` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Charge Payoff Lines
-------------------

### Get Charge Payoff Line Object Definition

#### `lookup`

> List all the fields and relationships for the charge payoff line object:

```
<lookup>
    <object>CHARGEPAYOFFENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHARGEPAYOFFENTRY` |

* * *

### Query and List Charge Payoff Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, account number and amount for each charge payoff line:

```
<query>
    <object>CHARGEPAYOFFENTRY</object>
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
| object | Required | string | Use `CHARGEPAYOFFENTRY` |
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

### Query and List Charge Payoff Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CHARGEPAYOFFENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHARGEPAYOFFENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Charge Payoff Line

#### `read`

```
<read>
    <object>CHARGEPAYOFFENTRY</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHARGEPAYOFFENTRY` |
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

