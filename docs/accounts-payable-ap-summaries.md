Title: AP Summaries

URL Source: https://developer.intacct.com/api/accounts-payable/ap-summaries/

Markdown Content:
*   [AP Bill Summaries](https://developer.intacct.com/api/accounts-payable/ap-summaries/#ap-bill-summaries)
    *   [Get Bill Summary Object Definition](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get-bill-summary-object-definition)
    *   [Query and List Bill Summaries](https://developer.intacct.com/api/accounts-payable/ap-summaries/#query-and-list-bill-summaries)
    *   [Query and List Bill Summaries (Legacy readByQuery)](https://developer.intacct.com/api/accounts-payable/ap-summaries/#query-and-list-bill-summaries-legacy-readbyquery)
    *   [List Bill Summaries (Legacy get\_list)](https://developer.intacct.com/api/accounts-payable/ap-summaries/#list-bill-summaries-legacy-get_list)
    *   [Get Bill Summary](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get-bill-summary)
    *   [Create Bill Summary (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-summaries/#create-bill-summary-legacy)
*   [AP Adjustment Summaries](https://developer.intacct.com/api/accounts-payable/ap-summaries/#ap-adjustment-summaries)
    *   [List AP Adjustment Summaries (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-summaries/#list-ap-adjustment-summaries-legacy)
    *   [Create AP Adjustment Summary (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-summaries/#create-ap-adjustment-summary-legacy)

* * *

AP summaries are collections of the same type of transactions, grouped together for processing.

* * *

### Get Bill Summary Object Definition

#### `lookup`

> List all the fields and relationships for the bill summary object:

```
<lookup>
    <object>APBILLBATCH</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLBATCH` |

* * *

### Query and List Bill Summaries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number for each active and open bill summary:

```
<query>
    <object>APBILLBATCH</object>
    <select>
        <field>RECORDNO</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>STATUS</field>
                <value>active</value>
            </equalto>
            <equalto>
                <field>OPEN</field>
                <value>Open</value>
            </equalto>
        </and>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLBATCH` |
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

### Query and List Bill Summaries (Legacy readByQuery)

#### `readByQuery`

> List active and open bill summaries:

```
<readByQuery>
    <object>APBILLBATCH</object>
    <fields>*</fields>
    <query>STATUS = 'T' AND OPEN = 'T'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLBATCH` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### List Bill Summaries (Legacy get\_list)

#### `get_list`

```
<get_list object="billbatch" maxitems="10">
</get_list>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string attribute | Use `billbatch` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

`get_list.filter.expression`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| field | Required | string | Name of the field to be compared. |
| operator | Required | string | Comparison operator. Valid operators are
*   `=`
*   `!=`
*   `<`
*   `<=`
*   `>`
*   `>=`
*   `like`
*   `is null`

 |
| value | Required | string | Comparison value. |

`get_list.sort.sortfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order (attribute) | Required | string | Sort order for this named field. Use either `asc` or `desc`. |

* * *

### Get Bill Summary

#### `read`

```
<read>
    <object>APBILLBATCH</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLBATCH` |
| keys | Required | string | Comma-separated list of summary `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Bill Summary (Legacy)

#### `create_billbatch`

```
<create_billbatch>
    <batchtitle>Bills for 2017 Week 03</batchtitle>
    <datecreated>
        <year>2017</year>
        <month>01</month>
        <day>20</day>
    </datecreated>
</create_billbatch>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| batchtitle | Required | string | Bill summary title |
| datecreated | Required | object | GL posting date |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

AP Adjustment Summaries
-----------------------

### List AP Adjustment Summaries (Legacy)

#### `get_list`

```
<get_list object="apadjustmentbatch" maxitems="10">
</get_list>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `apadjustmentbatch` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/accounts-payable/ap-summaries/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

`get_list.filter.expression`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| field | Required | string | Name of the field to be compared. |
| operator | Required | string | Comparison operator. Valid operators are
*   `=`
*   `!=`
*   `<`
*   `<=`
*   `>`
*   `>=`
*   `like`
*   `is null`

 |
| value | Required | string | Comparison value. |

`get_list.sort.sortfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order (attribute) | Required | string | Sort order for this named field. Use either `asc` or `desc`. |

* * *

### Create AP Adjustment Summary (Legacy)

```
<create_apadjustmentbatch>
    <batchtitle>AP Adjustments for 2017 Week 03</batchtitle>
    <datecreated>
        <year>2017</year>
        <month>01</month>
        <day>20</day>
    </datecreated>
</create_apadjustmentbatch>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| batchtitle | Required | string | AP adjustment summary title |
| datecreated | Required | object | GL posting date |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

