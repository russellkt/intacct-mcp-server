Title: Expense Summaries

URL Source: https://developer.intacct.com/api/employee-expenses/expense-summaries/

Markdown Content:
*   [List Expense Report Summaries (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-summaries/#list-expense-report-summaries-legacy)
*   [Create Expense Report Summary (Legacy)](https://developer.intacct.com/api/employee-expenses/expense-summaries/#create-expense-report-summary-legacy)

* * *

Expense summaries are collections of the same type of transactions, grouped together for processing.

* * *

List Expense Report Summaries (Legacy)
--------------------------------------

#### `get_list`

```
<get_list object="expensereportbatch" maxitems="10">
</get_list>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string attribute | Use `expensereportbatch` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/employee-expenses/expense-summaries/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/employee-expenses/expense-summaries/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/employee-expenses/expense-summaries/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/employee-expenses/expense-summaries/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/employee-expenses/expense-summaries/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

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

Create Expense Report Summary (Legacy)
--------------------------------------

#### `create_expensereportbatch`

```
<create_expensereportbatch>
    <batchtitle>Expense Reports for 2017 Week 03</batchtitle>
    <datecreated>
        <year>2017</year>
        <month>01</month>
        <day>20</day>
    </datecreated>
</create_expensereportbatch>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| batchtitle | Required | string | Expense report summary title |
| datecreated | Required | object | GL posting date |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

