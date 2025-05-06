Title: Customer Charge Cards

URL Source: https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/

Markdown Content:
*   [List Customer Charge Cards (Legacy)](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#list-customer-charge-cards-legacy)
*   [Create Customer Charge Card (Legacy)](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#create-customer-charge-card-legacy)
*   [Update Customer Charge Card (Legacy)](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#update-customer-charge-card-legacy)
*   [Delete Customer Charge Card (Legacy)](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#delete-customer-charge-card-legacy)

* * *

Customer charge cards hold customer charge card information.

**Important:** The customer charge card object and its supported functions will be deprecated in 2025 Release 1.

**Important:** Intacct does not store charge card verification codes or values (CVV), and only retains card data for 90 days past a card’s expiration date.

* * *

List Customer Charge Cards (Legacy)
-----------------------------------

The `get_list` function for customer charge cards is scheduled for deprecation. This function will become unavailable in a future release, likely, 2021-R2. At this time, the only way to access customer credit card information will be through the Sage Intacct UI.

**Important:** It is recommended that you check your integrations now and remove this function to avoid future problems.

#### `get_list`

> Retrieve all details of the first 10 customer charge cards (based on `recordno`):

```
<get_list object="customerchargecard" maxitems="10">
</get_list>
```

> Find a specific customer charge card based on the card number and return the card status and customer ID:

```
<get_list object="customerchargecard">
    <filter>
        <expression>
            <field>cardnumber</field>
            <operator>=</operator>
            <value>4444333322221111</value>
        </expression>
    </filter>
    <fields>
        <field>status</field>
        <field>customerid</field>
    </fields>
</get_list>
```

> Find all active customer charge cards that expire in 2026, return the customer ID, card number, and expiration month/year, and sort the results by expiration month:

```
<get_list object="customerchargecard">
    <filter>
        <logical logical_operator="and">
            <expression>
                <field>status</field>
                <operator>=</operator>
                <value>active</value>
            </expression>
            <expression>
                <field>exp_year</field>
                <operator>=</operator>
                <value>2026</value>
            </expression>
        </logical>
    </filter>
    <fields>
        <field>customerid</field>
        <field>cardnum</field>
        <field>exp_month</field>
        <field>exp_year</field>
    </fields>
    <sorts>
        <sortfield order="asc">exp_month</sortfield>
    </sorts>
</get_list>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string attribute | Use `customerchargecard` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

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

Create Customer Charge Card (Legacy)
------------------------------------

#### `create_customerchargecard`

```
<create_customerchargecard>
    <customerid>C1234</customerid>
    <cardnum>4444333322221111</cardnum>
    <cardtype>Visa</cardtype>
    <exp_month>January</exp_month>
    <exp_year>2020</exp_year>
    <mailaddress>
        <address1></address1>
        <address2></address2>
        <city></city>
        <state></state>
        <zip></zip>
        <country></country>
    </mailaddress>
</create_customerchargecard>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customerid | Required | string | Customer ID |
| cardnum | Required | string | Card number, without spaces or dashes. For example, `4444333322221111`. |
| cardtype | Required | string | Card type. Use `Visa`, `Mastercard`, `Discover`, `American Express`, `Diners Club`, or `Other Charge Card`. |
| exp\_month | Required | string | Expiration month. Use `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, or `December` |
| exp\_year | Required | integer | Expiration year. |
| description | Optional | string | Description |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| mailaddress | Required | [object](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#create_customerchargecard.mailaddress) | Mail address |
| defaultcard | Optional | boolean | Set as the default card for this customer.
*   `false` - No (default)
*   `true` - Yes

 |
| usebilltoaddr | Optional | boolean | Use bill to contact address for verification.

*   `true` - Yes (default)
*   `false` - No

 |

`create_customerchargecard.mailaddress`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| address1 | Optional | string | Address line 1 |
| address2 | Optional | string | Address line 2 |
| address3 | Optional | string | Address line 3 |
| city | Optional | string | City |
| state | Optional | string | State/province |
| zip | Optional | string | Zip/postal code |
| country | Optional | string | Country |
| isocountrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `isocountrycode` must be provided. |

* * *

Update Customer Charge Card (Legacy)
------------------------------------

#### `update_customerchargecard`

```
<update_customerchargecard recordno="1234">
    <exp_month>January</exp_month>
    <exp_year>2026</exp_year>
</update_customerchargecard>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | integer | Record number of customer charge card |
| exp\_month | Optional | string | Expiration month. Use `January`, `February`, `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`, `November`, or `December` |
| exp\_year | Optional | integer | Expiration year. |
| description | Optional | string | Description |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |
| mailaddress | Optional | [object](https://developer.intacct.com/api/accounts-receivable/customer-charge-cards/#update_customerchargecard.mailaddress) | Mail address |
| defaultcard | Optional | boolean | Set as the default card for this customer.
*   `false` - No (default)
*   `true` - Yes

 |
| usebilltoaddr | Optional | boolean | Use bill to contact address for verification.

*   `true` - Yes (default)
*   `false` - No

 |

`update_customerchargecard.mailaddress`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| address1 | Optional | string | Address line 1 |
| address2 | Optional | string | Address line 2 |
| address3 | Optional | string | Address line 3 |
| city | Optional | string | City |
| state | Optional | string | State/province |
| zip | Optional | string | Zip/postal code |
| country | Optional | string | Country |
| isocountrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `isocountrycode` must be provided. |

* * *

Delete Customer Charge Card (Legacy)
------------------------------------

#### `delete_customerchargecard`

```
<delete_customerchargecard recordno="123" />
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | integer | Record number of customer charge card |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

