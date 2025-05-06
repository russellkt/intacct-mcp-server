Title: AR Terms

URL Source: https://developer.intacct.com/api/accounts-receivable/ar-terms/

Markdown Content:
*   [Get AR Term Object Definition](https://developer.intacct.com/api/accounts-receivable/ar-terms/#get-ar-term-object-definition)
*   [Query and List AR Terms](https://developer.intacct.com/api/accounts-receivable/ar-terms/#query-and-list-ar-terms)
*   [Query and List AR Terms (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-terms/#query-and-list-ar-terms-legacy)
*   [Get AR Term](https://developer.intacct.com/api/accounts-receivable/ar-terms/#get-ar-term)
*   [Get AR Term by ID](https://developer.intacct.com/api/accounts-receivable/ar-terms/#get-ar-term-by-id)
*   [Create AR Term (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-terms/#create-ar-term-legacy)
*   [Update AR Term (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-terms/#update-ar-term-legacy)
*   [Delete AR Term (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-terms/#delete-ar-term-legacy)

* * *

An AR term is a rule (such as net 30) that a company establishes for extending credit to customers.

AR terms can be associated with AR transactions or with specific customers.

* * *

Get AR Term Object Definition
-----------------------------

#### `lookup`

> List all the fields and relationships for the AR term object:

```
<lookup>
    <object>ARTERM</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARTERM` |

* * *

Query and List AR Terms
-----------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List information about each AR term:

```
<query>
    <object>ARTERM</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
        <field>DUEDATE</field>
        <field>DUEFROM</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARTERM` |
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

Query and List AR Terms (Legacy)
--------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ARTERM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARTERM` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get AR Term
-----------

#### `read`

```
<read>
    <object>ARTERM</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARTERM` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get AR Term by ID
-----------------

#### `readByName`

```
<readByName>
    <object>ARTERM</object>
    <keys>N15</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARTERM` |
| keys | Required | string | Comma-separated list of object `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create AR Term (Legacy)
-----------------------

#### `create_arterm`

```
<create_arterm>
    <name>2-10 N30</name>
    <description>2%/10 net 30</description>
    <due>
        <dueday>30</dueday>
        <duefrom>from invoice/bill date</duefrom>
    </due>
    <discount>
        <discday>10</discday>
        <discfrom>from invoice/bill date</discfrom>
        <discamount>2</discamount>
        <discpercamn>%</discpercamn>
        <discgracedays></discgracedays>
    </discount>
    <disccalcon>Line items total</disccalcon>
    <penalty>
        <pen_type>Weekly</pen_type>
        <penamount>1</penamount>
        <penpercamn>%</penpercamn>
        <pengracedays></pengracedays>
    </penalty>
</create_arterm>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Term name |
| description | Optional | string | Description |
| status | Optional | string | Term status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| due | Optional | object | Due |
| discount | Optional | object | Discount |
| disccalcon | Optional | string | Calculate discount on. Use either `Line items total` or `Invoice total`. (Default: `Invoice total`) |
| penalty | Optional | object | Penalty |

`due`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| dueday | Optional | integer | Due day |
| duefrom | Optional | string | Due from. Use `from invoice/bill date`, `of the month of invoice/bill date`, `of next month from invoice/bill date`, `of 2nd month from invoice/bill date`, `of 3rd month from invoice/bill date`, `of 4th month from invoice/bill date`, `of 5th month from invoice/bill date`, or `of 6th month from invoice/bill date`. (Default: `from invoice/bill date`) |

`discount`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| discday | Optional | integer | Discount day |
| discfrom | Optional | string | Due from. Use `from invoice/bill date`, `of the month of invoice/bill date`, `of next month from invoice/bill date`, `of 2nd month from invoice/bill date`, `of 3rd month from invoice/bill date`, `of 4th month from invoice/bill date`, `of 5th month from invoice/bill date`, or `of 6th month from invoice/bill date`. (Default: `from invoice/bill date`) |
| discamount | Optional | currency | Discount amount |
| discpercamn | Optional | number | Discount amount type. Use either `$` or `%`. (Default: `$`) |
| discgracedays | Optional | integer | Discount grace days |

`penalty`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| pen\_type | Optional | string | Cycle. Use `No Penalty`, `Daily`, `Weekly`, `Biweekly`, `Monthly`, `Bimonthly`, `Quarterly`, `Half yearly`, or `Annually`. (Default: `No Penalty`) |
| penamount | Optional | currency | Penalty amount |
| penpercamn | Optional | number | Penalty percent. Use either `$` or `%`. (Default: `$`) |
| pengracedays | Optional | integer | Penalty grace days |

* * *

Update AR Term (Legacy)
-----------------------

#### `update_arterm`

```
<update_arterm name="2-10 N30">
    <description>2% discount if paid in 10 days, otherwise due in 30 days</description>
</update_arterm>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Term name to update |
| description | Optional | string | Description |
| status | Optional | string | Term status. Use `active` for Active otherwise use `inactive` for Inactive. |
| due | Optional | object | Due |
| discount | Optional | object | Discount |
| disccalcon | Optional | string | Calculate discount on. Use either `Line items total` or `Invoice total`. |
| penalty | Optional | object | Penalty |

`due`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| dueday | Optional | integer | Due day |
| duefrom | Optional | string | Due from. Use `from invoice/bill date`, `of the month of invoice/bill date`, `of next month from invoice/bill date`, `of 2nd month from invoice/bill date`, `of 3rd month from invoice/bill date`, `of 4th month from invoice/bill date`, `of 5th month from invoice/bill date`, or `of 6th month from invoice/bill date`. |

`discount`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| discday | Optional | integer | Discount day |
| discfrom | Optional | string | Due from. Use `from invoice/bill date`, `of the month of invoice/bill date`, `of next month from invoice/bill date`, `of 2nd month from invoice/bill date`, `of 3rd month from invoice/bill date`, `of 4th month from invoice/bill date`, `of 5th month from invoice/bill date`, or `of 6th month from invoice/bill date`. |
| discamount | Optional | currency | Discount amount |
| discpercamn | Optional | number | Discount amount type. Use either `$` or `%`. |
| discgracedays | Optional | integer | Discount grace days |

`penalty`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| pen\_type | Optional | string | Cycle. Use `No Penalty`, `Daily`, `Weekly`, `Biweekly`, `Monthly`, `Bimonthly`, `Quarterly`, `Half yearly`, or `Annually`. |
| penamount | Optional | currency | Penalty amount |
| penpercamn | Optional | number | Penalty percent. Use either `$` or `%`. |
| pengracedays | Optional | integer | Penalty grace days |

* * *

Delete AR Term (Legacy)
-----------------------

#### `delete_arterm`

```
<delete_arterm name="2-10 N30"></delete_arterm>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Term name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

