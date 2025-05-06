Title: Recurring Invoices

URL Source: https://developer.intacct.com/api/accounts-receivable/recurring-invoices/

Markdown Content:
*   [Recurring Invoices](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#recurring-invoices)
    *   [Get Recurring Invoice Object Definition](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#get-recurring-invoice-object-definition)
    *   [Query and List Recurring Invoices](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#query-and-list-recurring-invoices)
    *   [Query and List Recurring Invoices (Legacy)](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#query-and-list-recurring-invoices-legacy)
    *   [Get Recurring Invoice](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#get-recurring-invoice)
    *   [Create Recurring Invoice (Legacy)](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#create-recurring-invoice-legacy)
    *   [Delete Recurring Invoice (Legacy)](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#delete-recurring-invoice-legacy)
*   [Recurring Invoice Lines](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#recurring-invoice-lines)
    *   [Get Recurring Invoice Line Object Definition](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#get-recurring-invoice-line-object-definition)
    *   [Query and List Recurring Invoice Lines](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#query-and-list-recurring-invoice-lines)
    *   [Query and List Recurring Invoice Lines (Legacy)](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#query-and-list-recurring-invoice-lines-legacy)
    *   [Get Recurring Invoice Line](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#get-recurring-invoice-line)

* * *

An AR recurring invoice provides the ability to schedule and automate the process of creating AR invoices.

It is commonly used for regularly-recurring, fixed-amount invoices.

* * *

### Get Recurring Invoice Object Definition

#### `lookup`

> List all the fields and relationships for the recurring invoice object:

```
<lookup>
    <object>ARRECURINVOICE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICE` |

* * *

### Query and List Recurring Invoices

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and customer name for each recurring invoice where the customer name starts with the letter `B`:

```
<query>
    <object>ARRECURINVOICE</object>
    <select>
        <field>RECORDNO</field>
        <field>CUSTOMERNAME</field>
    </select>
    <filter>
        <like>
            <field>CUSTOMERNAME</field>
            <value>B%</value>
        </like>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICE` |
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

### Query and List Recurring Invoices (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ARRECURINVOICE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Recurring Invoice

#### `read`

```
<read>
    <object>ARRECURINVOICE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICE` |
| keys | Required | string | Comma-separated list of recurring invoice `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Recurring Invoice (Legacy)

[History](https://developer.intacct.com/api/accounts-receivable/recurring-invoices/#history-create-recurring-invoice-legacy)

| Release | Changes |
| --- | --- |
| 2024 Release 4 | Removed retired AMEX payment option |
| 2020 Release 4 | Added taxsolutionid, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_recurringinvoice`

> Create a recurring invoice:

```
<create_recurringinvoice>
    <customerid>V1234</customerid>
    <datecreated>
        <year>2017</year>
        <month>04</month>
        <day>10</day>
    </datecreated>
    <recordid>Recurring Services</recordid>
    <docnumber>12345678</docnumber>
    <description>Monthly services</description>
    <termname>Net 20</termname>
    <startdate>
        <year>2017</year>
        <month>01</month>
        <day>01</day>
    </startdate>
    <ending>
        <occur>12</occur>
    </ending>
    <modenew>Months</modenew>
    <interval>12</interval>
    <eom>true</eom>
    <recurinvoiceitems>
        <recurlineitem>
            <glaccountno>4100</glaccountno>
            <amount>349.99</amount>
            <locationid>SJC-US</locationid>
            <departmentid>ADM</departmentid>
        </recurlineitem>
    </recurinvoiceitems>
</create_recurringinvoice>
```

> Create a recurring invoice with a single line that uses two tax entries. The first tax entry allows the system to calculate the `trx_tax` value, and the second entry overrides the calculated `trx_tax` value (AU, GB, ZA only):

```
<create_recurringinvoice>
    <customerid>BTI</customerid>
    <datecreated>
        <year>2020</year>
        <month>04</month>
        <day>10</day>
    </datecreated>
    <recordid>Recurring Services</recordid>
    <docnumber>5685</docnumber>
    <description>Monthly services</description>
    <termname>Net 15</termname>
    <currency>USD</currency>
    <exchrate>1</exchrate>
    <startdate>
        <year>2020</year>
        <month>04</month>
        <day>20</day>
    </startdate>
    <ending>
        <occur>12</occur>
    </ending>
    <modenew>Months</modenew>
    <interval>12</interval>
    <eom>true</eom>
    <taxsolutionid>United Kingdom - VAT</taxsolutionid>
    <recurinvoiceitems>
        <recurlineitem>
            <accountlabel>Sales</accountlabel>
            <amount>100</amount>
            <locationid>3</locationid>
            <taxentries>
                <taxentry>
                    <detailid>UK Sale Services Standard Rate</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
                <taxentry>
                    <detailid>UK Sale Services Reduced Rate</detailid>
                    <trx_tax>5.6</trx_tax>
                </taxentry>
            </taxentries>
        </recurlineitem>
    </recurinvoiceitems>
</create_recurringinvoice>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customerid | Required | string | Customer ID |
| datecreated | Required | object | Transaction date. Make this match Start date. |
| recordid | Required | string | Invoice sequence number |
| docnumber | Optional | string | Reference number |
| description | Optional | string | Description |
| contractid | Optional | string | Contract ID |
| contractdesc | Optional | string | Contract description |
| termname | Required | string | Payment term |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| status | Optional | string | Status. Use `active` or `inactive`. (Default: `active`) |
| supdocid | Optional | string | Attachments ID |
| billtocontactname | Optional | string | Bill to contact name |
| shiptocontactname | Optional | string | Ship to contact name |
| startdate | Required | object | Start date |
| ending | Optional | object | Ending on. Leave element out to Never end. |
| modenew | Optional | string | Repeat mode. Use `None`, `Days`, `Weeks`, `Months`, or `Years`. (Default: `None`) |
| interval | Optional | integer | Repeat interval. Required when Repeat mode is not set to `None`. |
| eom | Optional | boolean | End of month. Only used when Repeat mode is set to `Months`. Use either `true` or `false`. (Default: `false`) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. The available tax solution names can be found in the Sage Intacct UI in the Taxes application from the top level of a multi-entity company. (GB, AU, and ZA only) |
| recurinvoiceitems | Required | `recurlineitem[1...n]` | Bill lines, must have at least 1. |
| paymethod | Optional | string | Payment method. Use `None`, `Printed Check`, `Credit Card`, `EFT`, `Cash`, `Online Charge Card`, or `Online ACH Debit`. (Default: `None`) |
| payinfull | Optional | boolean | Pay in full. Use `false` for No, `true` for Yes. (Default: `true`) |
| paymentamount | Optional | currency | Payment amount. Required if Pay in full is set to `false` |
| customercreditcardkey | Optional | integer | Customer credit card key. Required if Payment method is set to `Online Credit Card`. |
| customerbankaccountkey | Optional | integer | Customer bank account key. Required if Payment method is set to `Online ACH Debit`. |
| creditcardtype | Optional | string | Credit card type. Required if Payment method is set to `Credit Card`. Use `VISA`, `MC`, `DISCOVER`, `DINERS`, or `OTHER`. |
| accounttype | Optional | string | Account type to put payment in. Use `Bank` or `Undeposited Funds Account`. (Default: `Bank`) |
| bankaccountid | Optional | string | Bank account ID. Required if Account type is `Bank`. |
| glaccountkey | Optional | string | Undeposited funds GL account. Required if Account type is `Undeposited Funds Account`. |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`exchratedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`startdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`recurlineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| amount | Required | currency | Transaction amount |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| customfields | Optional | array of `customfield` | Custom fields |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) for the recurring invoice line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the amount due (`TOTAL_DUE`) for the recurring invoice. |

* * *

### Delete Recurring Invoice (Legacy)

#### `delete_recurringinvoice`

```
<delete_recurringinvoice key="1234"></delete_recurringinvoice>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Recurring invoice `RECORDNO` to delete |

* * *

Recurring Invoice Lines
-----------------------

### Get Recurring Invoice Line Object Definition

#### `lookup`

> List all the fields and relationships for the recurring invoice line object:

```
<lookup>
    <object>ARRECURINVOICEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICEENTRY` |

* * *

### Query and List Recurring Invoice Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and line number for each recurring invoice line:

```
<query>
    <object>ARRECURINVOICEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>LINE_NO</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICEENTRY` |
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

### Query and List Recurring Invoice Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ARRECURINVOICEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Recurring Invoice Line

#### `read`

```
<readByQuery>
    <object>ARRECURINVOICEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRECURINVOICEENTRY` |
| keys | Required | string | Comma-separated list of object line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

