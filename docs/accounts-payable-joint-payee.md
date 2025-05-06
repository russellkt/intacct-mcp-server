Title: Joint Payee

URL Source: https://developer.intacct.com/api/accounts-payable/joint-payee/

Markdown Content:
*   [Get Joint Payee Object Definition](https://developer.intacct.com/api/accounts-payable/joint-payee/#get-joint-payee-object-definition)
*   [Query and List Joint Payees](https://developer.intacct.com/api/accounts-payable/joint-payee/#query-and-list-joint-payees)
*   [Query and List Joint Payees (Legacy)](https://developer.intacct.com/api/accounts-payable/joint-payee/#query-and-list-joint-payees-legacy)
*   [Get Joint Payee](https://developer.intacct.com/api/accounts-payable/joint-payee/#get-joint-payee)
*   [Create Joint Payee](https://developer.intacct.com/api/accounts-payable/joint-payee/#create-joint-payee)
*   [Update Joint Payee](https://developer.intacct.com/api/accounts-payable/joint-payee/#update-joint-payee)

* * *

A joint payee is an additional payee that is associated with an AP bill so that payments against the bill can be issued as joint checks that must be signed by both parties.

In construction and some other fields, companies hire subcontractors to work on part or all of their projects. In some cases, the subcontractor that is hired also hires their own subcontractors to complete the contracted work. In these cases, joint checks can be issued for a primary vendor (subcontractor) and their secondary vendor (the subcontractor’s subcontractor). This ensures that the secondary subcontractor is paid for their work and can help avoid unnecessary churn and possible liens against projects by unpaid secondary vendors.

When paying a bill that has associated joint payees, create separate payment detail objects for each payee:

*   To pay the primary vendor, do not set a value for `JOINTPAYEEPRINTAS` in the payment detail.
*   To pay a secondary vendor, set `JOINTPAYEEPRINTAS` to the value from the `APBILLJOINTPAYEE` object.
*   To pay additional secondary vendors, create separate payment detail objects for each one.

Note: If an AP Bill is deleted, the associated joint payee records will also be deleted.

A Construction subscription is required to use this feature and Joint Checks must be enabled in the Accounts Payable Configuration.

* * *

Get Joint Payee Object Definition
---------------------------------

#### `lookup`

> List all the fields and relationships for the Joint Payee object:

```
<lookup>
  <object>APBILLJOINTPAYEE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLJOINTPAYEE` |

* * *

Query and List Joint Payees
---------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and AP bill key for each joint payee object where the payee name is “DW Drywall”:

```
<query>
  <object>APBILLJOINTPAYEE</object>
  <select>
    <field>RECORDNO</field>
    <field>APBILLKEY</field>
  </select>
  <filter>
    <like>
      <field>JOINTPAYEENAME</field>
      <value>DW Drywall</value>
    </like>
  </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLJOINTPAYEE` |
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

Query and List Joint Payees (Legacy)
------------------------------------

#### `readByQuery`

```
<readByQuery>
  <object>APBILLJOINTPAYEE</object>
  <fields>*</fields>
  <query></query>
  <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLJOINTPAYEE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

#### `read`

```
<read>
    <object>APBILLJOINTPAYEE</object>
    <keys>7</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLJOINTPAYEE` |
| keys | Required | string | Comma-separated list of joint payee `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Joint Payee
------------------

#### `create`

```
<create>
  <APBILLJOINTPAYEE>
    <APBILLKEY>14</APBILLKEY>
    <JOINTPAYEENAME>DW Drywall</JOINTPAYEENAME>
    <JOINTPAYEEPRINTAS>Johnson Construction and DW Drywall</JOINTPAYEEPRINTAS>
  </APBILLJOINTPAYEE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `APBILLJOINTPAYEE` | Required | object | Type of object to create. |

`APBILLJOINTPAYEE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `APBILLKEY` | Required | integer | `RECORDNO` of the AP bill that this joint payee will be paid from. |
| `JOINTPAYEENAME` | Required | string | Name of the joint payee (secondary vendor), such as “Joe Smith Plumbing Contractor”. |
| `JOINTPAYEEPRINTAS` | Required | string | Name as you want it to print on the check which includes the primary vendor AND the joint payee, e.g. “A-1 Plumbing AND Joe Smith”. No two joint payees for the same AP Bill can have the same `JOINTPAYEEPRINTAS` value. |

* * *

Update Joint Payee
------------------

A joint payee cannot be updated if it has been used in a payment.

#### `update`

```
<update>
  <APBILLJOINTPAYEE>
    <RECORDNO>5</RECORDNO>
    <JOINTPAYEENAME>Mac Air</JOINTPAYEENAME>
    <JOINTPAYEEPRINTAS>Sunset Hardware AND Mac Air</JOINTPAYEEPRINTAS>
  </APBILLJOINTPAYEE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `APBILLJOINTPAYEE` | Required | object | Type of object to update. |

`APBILLJOINTPAYEE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `APBILLKEY` | Required | integer | `RECORDNO` for the AP Bill that will be paid to this joint payee. |
| `JOINTPAYEENAME` | Required | string | Name of the joint payee (secondary vendor), such as “Joe Smith Plumbing Contractor”. |
| `JOINTPAYEEPRINTAS` | Required | string | Name as you want it to print on the check which includes the primary vendor AND the joint payee, e.g. “A-1 Plumbing AND Joe Smith”. No two joint payees for the same AP Bill can have the same JOINTPAYEEPRINTAS value. |

* * *

### Delete Joint Payee

A joint payee cannot be deleted if it has been used in a payment.

#### `delete`

```
<delete>
  <object>APBILLJOINTPAYEE</object>
  <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLJOINTPAYEE` |
| keys | Required | string | Comma-separated list of joint payee `RECORDNO` to delete. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

