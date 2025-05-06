Title: Reimbursements

URL Source: https://developer.intacct.com/api/employee-expenses/reimbursements/

Markdown Content:
*   [Reimbursements](https://developer.intacct.com/api/employee-expenses/reimbursements/#reimbursements)
    *   [Get Reimbursement Object Definition](https://developer.intacct.com/api/employee-expenses/reimbursements/#get-reimbursement-object-definition)
    *   [Query and List Reimbursements](https://developer.intacct.com/api/employee-expenses/reimbursements/#query-and-list-reimbursements)
    *   [Query and List Reimbursements (Legacy)](https://developer.intacct.com/api/employee-expenses/reimbursements/#query-and-list-reimbursements-legacy)
    *   [Get Reimbursement](https://developer.intacct.com/api/employee-expenses/reimbursements/#get-reimbursement)
*   [Reimbursement Requests](https://developer.intacct.com/api/employee-expenses/reimbursements/#reimbursement-requests)
    *   [Get Reimbursement Request Object Definition](https://developer.intacct.com/api/employee-expenses/reimbursements/#get-reimbursement-request-object-definition)
    *   [Query and List Reimbursement Requests](https://developer.intacct.com/api/employee-expenses/reimbursements/#query-and-list-reimbursement-requests)
    *   [Query and List Reimbursement Requests (Legacy)](https://developer.intacct.com/api/employee-expenses/reimbursements/#query-and-list-reimbursement-requests-legacy)
    *   [Get Reimbursement Request](https://developer.intacct.com/api/employee-expenses/reimbursements/#get-reimbursement-request)
    *   [Create Reimbursement Request (Legacy)](https://developer.intacct.com/api/employee-expenses/reimbursements/#create-reimbursement-request-legacy)

* * *

Reimbursing employees for expenses involves a workflow in which entered expenses move from selection to payment.

* * *

### Get Reimbursement Object Definition

#### `lookup`

> List all the fields and relationships for the reimbursement object:

```
<lookup>
    <object>EPPAYMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENT` |

* * *

### Query and List Reimbursements

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, payment type, and amount for each reimbursement:

```
<query>
    <object>EPPAYMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>PAYMENTTYPE</field>
        <field>PAYMENTAMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENT` |
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

### Query and List Reimbursements (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EPPAYMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Reimbursement

#### `read`

```
<read>
    <object>EPPAYMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENT` |
| keys | Required | string | Comma-separated list of reimbursement `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Reimbursement Requests
----------------------

### Get Reimbursement Request Object Definition

#### `lookup`

> List all the fields and relationships for the reimbursement request object:

```
<lookup>
    <object>EPPAYMENTREQUEST</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENTREQUEST` |

* * *

### Query and List Reimbursement Requests

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, payment amount, and employee ID for each reimbursement:

```
<query>
    <object>EPPAYMENTREQUEST</object>
    <select>
        <field>RECORDNO</field>
        <field>PAYMENTAMOUNT</field>
        <field>EMPLOYEEID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENTREQUEST` |
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

### Query and List Reimbursement Requests (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EPPAYMENTREQUEST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENTREQUEST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Reimbursement Request

#### `read`

```
<read>
    <object>EPPAYMENTREQUEST</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EPPAYMENTREQUEST` |
| keys | Required | string | Comma-separated list of request `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Reimbursement Request (Legacy)

Creating a reimbursement request begins the process of selecting an existing expense report to be reimbursed.

#### `create_reimbursementrequest`

```
<create_reimbursementrequest>
    <bankaccountid>BOFA1435</bankaccountid>
    <employeeid>E1234</employeeid>
    <memo>Test Memo</memo>
    <paymentmethod>Printed Check</paymentmethod>
    <paymentdate>
        <year>2016</year>
        <month>11</month>
        <day>22</day>
    </paymentdate>
    <paymentoption>employeepref</paymentoption>
    <eppaymentrequestitems>
        <eppaymentrequestitem>
            <key>206</key>
            <paymentamount>100.99</paymentamount>
            <credittoapply></credittoapply>
        </eppaymentrequestitem>
    </eppaymentrequestitems>
    <documentnumber>12345</documentnumber>
    <paymentdescription>Test Desc</paymentdescription>
    <paymentcontact></paymentcontact>
</create_reimbursementrequest>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bankaccountid | Required | string | Bank account ID |
| employeeid | Required | string | Employee ID |
| memo | Optional | string | Memo |
| paymentmethod | Required | string | Payment method. Use `Printed Check` for Check, `Cash` for Cash, `EFT` for Record Transfer, or `ACH` for ACH. |
| paymentdate | Required | object | Payment date |
| paymentoption | Optional | string | Merge option. Use `employee`, `expense`, or `employeepref`. (Default: `employee`) |
| eppaymentrequestitems | Required | `eppaymentrequestitem[1...n]` | Items to pay |
| documentnumber | Optional | string | Document number |
| paymentdescription | Optional | string | Description |
| paymentcontact | Optional | string | Notification contact name |

`paymentdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`eppaymentrequestitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Apply to record number |
| paymentamount | Required | currency | Amount to apply |
| credittoapply | Optional | currency | Credit to apply |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

