Title: Recurring Order Entry Transactions

URL Source: https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/

Markdown Content:
*   [Get Recurring Order Entry Transaction Object Definition](https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/#get-recurring-order-entry-transaction-object-definition)
*   [Query and List Recurring Order Entry Transactions](https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/#query-and-list-recurring-order-entry-transactions)
*   [Query and List Recurring Order Entry Transactions (Legacy)](https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/#query-and-list-recurring-order-entry-transactions-legacy)
*   [Get Recurring Order Entry Transaction](https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/#get-recurring-order-entry-transaction)
*   [Create Recurring Order Entry Transaction (Legacy)](https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/#create-recurring-order-entry-transaction-legacy)
*   [Delete Recurring Order Entry Transaction (Legacy)](https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/#delete-recurring-order-entry-transaction-legacy)

* * *

Recurring transactions work the same as standard transactions, except that the transaction is repeated according to a schedule you set on the recurring template.

* * *

Get Recurring Order Entry Transaction Object Definition
-------------------------------------------------------

#### `lookup`

> List all the fields and relationships for the recurring Order Entry transaction object:

```
<lookup>
    <object>SORECURDOCUMENT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SORECURDOCUMENT` |

* * *

Query and List Recurring Order Entry Transactions
-------------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and total for each recurring Order Entry transaction:

```
<query>
    <object>SORECURDOCUMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>TOTAL</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SORECURDOCUMENT` |
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

Query and List Recurring Order Entry Transactions (Legacy)
----------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>SORECURDOCUMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SORECURDOCUMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Recurring Order Entry Transaction
-------------------------------------

#### `read`

```
<read>
    <object>SORECURDOCUMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SORECURDOCUMENT` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Recurring Order Entry Transaction (Legacy)
-------------------------------------------------

[History](https://developer.intacct.com/api/order-entry/recurring-order-entry-transactions/#history-create-recurring-order-entry-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2024 Release 4 | Removed retired AMEX payment option |
| 2021 Release 1 | Added itemaliasid |
| 2020 Release 4 | Added customerponumber, taxsolutionid |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `create_recursotransaction`

```
<create_recursotransaction>
    <transactiontype>Sales Order</transactiontype>
    <customerid>C1234</customerid>
    <referenceno>5678</referenceno>
    <termname>N30</termname>
    <message>hello world</message>
    <shippingmethod>FedEx</shippingmethod>
    <recursotransitems>
        <recursotransitem>
            <itemid>I0001</itemid>
            <quantity>1</quantity>
            <price>12.99</price>
            <locationid>100</locationid>
        </recursotransitem>
    </recursotransitems>
    <paymethod>Credit Card</paymethod>
    <payinfull>true</payinfull>
    <creditcardtype>VISA</creditcardtype>
    <accounttype>Undeposited Funds Account</accounttype>
    <glaccountkey>1099</glaccountkey>
    <startdate>
        <year>2017</year>
        <month>04</month>
        <day>10</day>
    </startdate>
    <ending>
        <occur>12</occur>
    </ending>
    <modenew>Months</modenew>
    <interval>12</interval>
    <eom>false</eom>
</create_recursotransaction>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| transactiontype | Required | string | Transaction definition to use |
| customerid | Required | String | Customer ID |
| referenceno | Optional | string | Reference number |
| termname | Optional | string | Payment term |
| message | Optional | string | Message |
| contractid | Optional | string | Contract ID |
| contractdesc | Optional | string | Contract description |
| customerponumber | optional | String | Customer’s purchase order number |
| shippingmethod | Optional | string | Shipping method |
| shipto | Optional | object | Ship to contact |
| billto | Optional | object | Bill to contact |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratetype | Optional | string | Exchange rate type. (Leave blank to use `Intacct Daily Rate`) |
| customfields | Optional | array of `customfield` | Custom fields |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the recurring transaction will occur at the top level of the company. The available tax solution names can be found in the Sage Intacct UI in the Taxes application from the top level of a multi-entity company. (GB, AU, and ZA only) |
| recursotransitems | Required | `recursotransitem[1...n]` | Transaction lines, must have at least 1. |
| subtotals | Optional | `subtotal[0...n]` | Subtotal lines |
| paymethod | Optional | string | Payment method. Use `None`, `Printed Check`, `Credit Card`, `EFT`, `Cash`, `Online Charge Card`, or `Online ACH Debit`. (Default: `None`) |
| payinfull | Optional | boolean | Pay in full. Use `false` for No, `true` for Yes. (Default: `true`) |
| paymentamount | Optional | currency | Payment amount. Required if Pay in full is set to `false` |
| creditcardtype | Optional | string | Credit card type. Required if Payment method is set to `Credit Card`. Use `VISA`, `MC`, `DISCOVER`, `DINERS`, or `OTHER`. |
| customercreditcardkey | Optional | integer | Customer credit card key. Required if Payment method is set to `Online Credit Card`. |
| customerbankaccountkey | Optional | integer | Customer bank account key. Required if Payment method is set to `Online ACH Debit`. |
| accounttype | Optional | string | Account type to put payment in. Use `Bank` or `Undeposited Funds Account`. (Default: `Bank`) |
| bankaccountid | Optional | string | Bank account ID. Required if Account type is `Bank`. |
| glaccountkey | Optional | string | Undeposited funds GL account. Required if Account type is `Undeposited Funds Account` |
| startdate | Required | object | Start date |
| ending | Optional | object | Ending on. Leave element out to Never end. |
| modenew | Optional | string | Repeat mode. Use `None`, `Days`, `Weeks`, `Months`, or `Years`. (Default: `None`) |
| interval | Optional | integer | Repeat interval. Required when Repeat mode is not set to `None`. |
| eom | Optional | boolean | End of month. Only used when Repeat mode is set to `Months`. Use either `true` or `false`. (Default: `false`) |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| docstatus | Optional | string | Visible document status. Use `Active`, `Inactive`, or `Ended`. |

`shipto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Ship to contact name |

`billto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Bill to contact name |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`recursotransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | Item ID |
| itemaliasid | Optional | string | Alias name for the item as set up in an [item cross reference](https://developer.intacct.com/api/inventory-control/item-cross-references/) created for the customer on this transaction. |
| itemdesc | Optional | string | Item description |
| taxable | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. Customer must be set up for taxable. |
| warehouseid | Optional | string | Warehouse ID |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure to base quantity off |
| price | Optional | currency | Price |
| discsurchargememo | Optional | string | Discount/surcharge memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| memo | Optional | string | Memo |
| itemdetails | Optional | `itemdetail[0...n]` | Array of item details |
| customfields | Optional | array of `customfield` | Custom fields |
| revrectemplate | Optional | string | Rev rec template ID |
| revrecstartdate | Optional | object | Rev rec start date |
| revrecenddate | Optional | object | Rev rec end date |
| status | Optional | string | Status. Use `Active`, `Inactive`, or `Ended`. |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| shipto | Optional | string | Ship to contact name for the transaction line, which overrides the ship to contact name on the transaction. |

`itemdetail`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| quantity | Optional | number | Quantity |
| serialno | Optional | string | Serial number. Only used if not using `lotno`. |
| lotno | Optional | string | Lot number. Only used if not using `serialno`. |
| aisle | Optional | string | Aisle |
| row | Optional | string | Row |
| bin | Optional | string | Bin |
| itemexpiration | Optional | object | Item expiration |

`itemexpiration`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`subtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| description | Required | string | Description |
| total | Required | currency | Total |
| absval | Optional | number | Absolute value |
| percentval | Optional | number | Percent value |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| itemid | Optional | string | Item ID |
| contractid | Optional | string | Contract ID |

`ending`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| occur | Optional | integer | Number of occurrences. Required if not using End date. |
| enddate | Optional | object | End date. Required if not using Number of occurrences. |

`enddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Delete Recurring Order Entry Transaction (Legacy)
-------------------------------------------------

#### `delete_recursotransaction`

```
<delete_recursotransaction key="1"></delete_recursotransaction>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Record `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

