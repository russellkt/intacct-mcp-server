Title: Territories

URL Source: https://developer.intacct.com/api/accounts-receivable/territories/

Markdown Content:
*   [List Territories (Legacy)](https://developer.intacct.com/api/accounts-receivable/territories/#list-territories-legacy)
*   [Get Territory by ID (Legacy)](https://developer.intacct.com/api/accounts-receivable/territories/#get-territory-by-id-legacy)
*   [Create Territory (Legacy)](https://developer.intacct.com/api/accounts-receivable/territories/#create-territory-legacy)
*   [Update Territory (Legacy)](https://developer.intacct.com/api/accounts-receivable/territories/#update-territory-legacy)
*   [Delete Territory (Legacy)](https://developer.intacct.com/api/accounts-receivable/territories/#delete-territory-legacy)

* * *

Territories are optionally included in Customer records and are used with Accounts Receivable reports.

They can be useful for filtering and categorizing data, assuming your company has multiple territories.

* * *

List Territories (Legacy)
-------------------------

#### `get_list`

```
<get_list object="territory" maxitems="10">
</get_list>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string attribute | Use `territory` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/accounts-receivable/territories/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/accounts-receivable/territories/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/accounts-receivable/territories/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/accounts-receivable/territories/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/accounts-receivable/territories/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

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

Get Territory by ID (Legacy)
----------------------------

#### `get`

```
<get object="territory" key="NCAL-01">
</get>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `territory` |
| key | Required | string | Object `territoryid` to get |
| fields | Optional | `field[0...n]` | Field(s) to return in response |

* * *

Create Territory (Legacy)
-------------------------

#### `create_territory`

```
<create_territory>
    <territoryid>NCAL-01</territoryid>
    <name>Northern CA Sacto</name>
    <parentid/>
    <managerid/>
    <status>active</status>
</create_territory>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| territoryid | Required | string | Territory ID |
| name | Required | string | Name of territory |
| parentid | Optional | string | Parent territory ID |
| managerid | Optional | string | Employee ID for the territory manager |
| status | Optional | string | Status, either `active` or `inactive` |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Territory (Legacy)
-------------------------

#### `update_territory`

```
<update_territory territoryid="NCAL-01">
    <managerid>002</managerid>
</update_territory>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| territoryid | Required | string | Territory ID |
| name | Optional | string | Name of territory |
| parentid | Optional | string | Parent territory ID |
| managerid | Optional | string | Employee ID for the territory manager |
| status | Optional | string | Status, either `active` or `inactive` |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Territory (Legacy)
-------------------------

#### `delete_territory`

```
<delete_territory territoryid="NCAL-01"></delete_territory>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Territory ID to delete |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

