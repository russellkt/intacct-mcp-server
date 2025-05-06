Title: Smart Events

URL Source: https://developer.intacct.com/api/customization-services/smart-events/

Markdown Content:
*   [List Smart Event Log Records (Legacy)](https://developer.intacct.com/api/customization-services/smart-events/#list-smart-event-log-records-legacy)

* * *

Smart Events are events that get triggered when certain conditions are met.

An event could be something as simple as an email to the sales manager when a sales quote over $10,000 is created.

* * *

List Smart Event Log Records (Legacy)
-------------------------------------

#### `get_list`

> List all Order Entry transaction event logs on April 3, 2013:

```
<get_list object="smarteventlog" maxitems="10" showprivate="false">
    <filter>
        <logical logical_operator="and">
            <expression>
                <field>ownerobject</field>
                <operator>=</operator>
                <value>SODOCUMENT</value>
            </expression>
            <expression>
                <field>timestamp</field>
                <operator>&gt;=</operator>
                <value>04/03/2013 12:00:00</value>
            </expression>
            <expression>
                <field>timestamp</field>
                <operator>&lt;</operator>
                <value>04/04/2013 12:00:00</value>
            </expression>
        </logical>
    </filter>
    <sorts>
        <sortfield order="asc">timestamp</sortfield>
    </sorts>
</get_list>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string attribute | Use `smarteventlog` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/customization-services/smart-events/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/customization-services/smart-events/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/customization-services/smart-events/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/customization-services/smart-events/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/customization-services/smart-events/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

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

#### `Response`

`smarteventlog`

> The above function returns data structured like this:

```
<smarteventlog>
    <recordno>38</recordno>
    <smartlinkid>AU_SODOCUMENT</smartlinkid>
    <topic>ADD_SODOCUMENT</topic>
    <ownerobject>SODOCUMENT</ownerobject>
    <timestamp>04/03/2013 16:42:11</timestamp>
    <userid>jsmith</userid>
    <objectkey>Sales Invoice-INV10045</objectkey>
</smarteventlog>
```

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

