Title: Invoices

URL Source: https://developer.intacct.com/api/accounts-receivable/invoices/

Markdown Content:
*   [Get Invoice Object Definition](https://developer.intacct.com/api/accounts-receivable/invoices/#get-invoice-object-definition)
*   [Query and List Invoices](https://developer.intacct.com/api/accounts-receivable/invoices/#query-and-list-invoices)
*   [Query and List Invoices (Legacy)](https://developer.intacct.com/api/accounts-receivable/invoices/#query-and-list-invoices-legacy)
*   [Get Invoice](https://developer.intacct.com/api/accounts-receivable/invoices/#get-invoice)
*   [Get Invoice as PDF Data](https://developer.intacct.com/api/accounts-receivable/invoices/#get-invoice-as-pdf-data)
*   [Create Invoice (Legacy)](https://developer.intacct.com/api/accounts-receivable/invoices/#create-invoice-legacy)
*   [Update Invoice (Legacy)](https://developer.intacct.com/api/accounts-receivable/invoices/#update-invoice-legacy)
*   [Reverse Invoice (Legacy)](https://developer.intacct.com/api/accounts-receivable/invoices/#reverse-invoice-legacy)
*   [Delete Invoice](https://developer.intacct.com/api/accounts-receivable/invoices/#delete-invoice)
*   [Delete Invoice (Legacy)](https://developer.intacct.com/api/accounts-receivable/invoices/#delete-invoice-legacy)

* * *

An AR invoice object represents an invoice sent to a customer for goods or services provided.

**About invoice record numbers**

Certain types of transaction definitions in Order Entry (e.g. Sales Invoice, Contract Invoice, Sales Credit Memo) are configured to create corresponding invoices in the Accounts Receivable module. When a transaction is updated in Order Entry, the related AR transaction is deleted and recreated. As a result, the AR transaction will have a new `RECORDNO`. Integrations relying on these records should consider using a `MODULEKEY` filter outlined below.

* * *

Get Invoice Object Definition
-----------------------------

#### `lookup`

> List all the fields and relationships for the invoice object:

```
<lookup>
    <object>ARINVOICE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARINVOICE` |

* * *

Query and List Invoices
-----------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and customer name for each invoice where the customer name starts with the letter `B`:

```
<query>
    <object>ARINVOICE</object>
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

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARINVOICE` |
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

Query and List Invoices (Legacy)
--------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ARINVOICE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARINVOICE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| MODULEKEY | Optional | string | Source module that the transaction was created from. Use `4.AR` for Accounts Receivable or `8.SO` for Order Entry |

* * *

Get Invoice
-----------

#### `read`

```
<read>
    <object>ARINVOICE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARINVOICE` |
| keys | Required | string | Comma-separated list of invoice `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Invoice as PDF Data
-----------------------

#### `retrievepdf`

> Provides base64-encoded data for a PDF version of the specified invoice:

```
<retrievepdf>
  <ARINVOICE>
    <RECORDNO>3086</RECORDNO>
  </ARINVOICE>
</retrievepdf>
```

> Retrieve PDF versions of multiple invoices:

```
<retrievepdf>
  <ARINVOICE>
    <RECORDNO>3086</RECORDNO>
  </ARINVOICE>
</retrievepdf>
</function>
<function controlid="pdf102">
<retrievepdf>
  <ARINVOICE>
    <RECORDNO>2462</RECORDNO>
  </ARINVOICE>
</retrievepdf>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ARINVOICE | Required | object | Object type to retrieve as PDF. Use `ARINVOICE`. |

`ARINVOICE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the invoice to retrieve. |

### Response

`pdfdata`

> The returned data looks like this:

```
<data listtype="arinvoice" count="1">
  <arinvoice>
    <recordno>3086</recordno>
    <pdfdata>JVBERi0xLjQKJfbk/N8KMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwovVmVyc2lvbiAvMS40Ci9QYWdlcyAyIDAgUgo+PgplbmRvYmoKMyAwIG9iago8PAovVHlwZSAvSW5mbwovUHJvZHVjZXIgKEZPUCAwLjIwLjQpCj4+...</pdfdata>
  </arinvoice>
</data>
```

* * *

Create Invoice (Legacy)
-----------------------

[History](https://developer.intacct.com/api/accounts-receivable/invoices/#history-create-invoice-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 4 | Added taxsolutionid, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_invoice`

> Create an invoice:

```
<create_invoice>
    <customerid>CUSTOMER1</customerid>
    <datecreated>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </datecreated>
    <dateposted>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </dateposted>
    <datedue>
        <year>2020</year>
        <month>09</month>
        <day>24</day>
    </datedue>
    <termname>N30</termname>
    <batchkey>20323</batchkey>
    <action>Submit</action>
    <invoiceno>234</invoiceno>
    <ponumber>234235</ponumber>
    <description>Some description</description>
    <externalid>20394</externalid>
    <billto>
        <contactname>28952</contactname>
    </billto>
    <shipto>
        <contactname>289533</contactname>
    </shipto>
    <basecurr>USD</basecurr>
    <currency>USD</currency>
    <exchratedate>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </exchratedate>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <nogl>false</nogl>
    <supdocid>6942</supdocid>
    <customfields>
        <customfield>
            <customfieldname>customfield1</customfieldname>
            <customfieldvalue>customvalue1</customfieldvalue>
        </customfield>
    </customfields>
    <invoiceitems>
        <lineitem>
            <accountlabel>TestBill Account1</accountlabel>
            <offsetglaccountno>93590253</offsetglaccountno>
            <amount>76343.43</amount>
            <memo>Just another memo</memo>
            <locationid>Location1</locationid>
            <departmentid>Department1</departmentid>
            <key>Key1</key>
            <totalpaid>23484.93</totalpaid>
            <totaldue>0</totaldue>
            <customfields>
                <customfield>
                    <customfieldname>customfield1</customfieldname>
                    <customfieldvalue>customvalue1</customfieldvalue>
                </customfield>
            </customfields>
            <revrectemplate>RevRec1</revrectemplate>
            <defrevaccount>2100</defrevaccount>
            <revrecstartdate>
                <year>2016</year>
                <month>06</month>
                <day>01</day>
            </revrecstartdate>
            <revrecenddate>
                <year>2017</year>
                <month>05</month>
                <day>31</day>
            </revrecenddate>
            <projectid>Project1</projectid>
            <customerid>Customer1</customerid>
            <vendorid>Vendor1</vendorid>
            <employeeid>Employee1</employeeid>
            <itemid>Item1</itemid>
            <classid>Class1</classid>
            <warehouseid>Warehouse1</warehouseid>
        </lineitem>
    </invoiceitems>
</create_invoice>
```

> Create an invoice where the first line uses a single tax detail and allows the system to calculate the `trx_tax` value, and the second line overrides the calculated `trx_tax` value (AU, GB, ZA only):

```
<create_invoice>
    <customerid>Australia Customer</customerid>
    <datecreated>
        <year>2020</year>
        <month>09</month>
        <day>06</day>
    </datecreated>
    <termname>N30</termname>
    <invoiceno>INV-201</invoiceno>
    <basecurr>AUD</basecurr>
    <currency>AUD</currency>
    <exchratetype></exchratetype>
    <taxsolutionid>Australia - GST</taxsolutionid>
    <invoiceitems>
        <lineitem>
            <accountlabel>Retail Sales</accountlabel>
            <amount>345.43</amount>
            <locationid>AUS</locationid>
            <taxentries>
                <taxentry>
                    <detailid>G1 Goods and Services Tax</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
            </taxentries>
        </lineitem>
        <lineitem>
            <accountlabel>Sales</accountlabel>
            <amount>234.56</amount>
            <locationid>AUS</locationid>
            <taxentries>
                <taxentry>
                    <detailid>G4 Input Taxed Sales</detailid>
                    <trx_tax>20.00</trx_tax>
                </taxentry>
            </taxentries>
        </lineitem>
    </invoiceitems>
</create_invoice>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customerid | Required | string | Customer ID |
| datecreated | Required | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| datedue | Optional | object | Due date. Required if not using `termname`. |
| termname | Optional | string | Payment term. Required if not using `datedue`. |
| batchkey | Optional | integer | Summary `RECORDNO` |
| action | Optional | string | Action. Use `Draft` or `Submit`. (Default: `Submit`) |
| invoiceno | Optional | string | Invoice number |
| ponumber | Optional | string | Reference number |
| description | Optional | string | Description |
| externalid | Optional | string | External ID |
| billto | Optional | object | Bill to contact |
| shipto | Optional | object | Ship to contact |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code. Required if `exchratetype` used. |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. If used, then `currency` is required. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`.) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| nogl | Optional | boolean | Do not post to GL. Use `false` for No, `true` for Yes. (Default: `false`) |
| supdocid | Optional | string | Attachments ID |
| customfields | Optional | array of `customfield` | Custom fields |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. The available tax solution names can be found in the Sage Intacct UI in the Taxes application from the top level of a multi-entity company. (GB, AU, and ZA only) |
| invoiceitems | Required | `lineitem[1...n]` | Invoice lines, must have at least 1. |

`datecreated`  
`dateposted`  
`datedue`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`billto`  
`shipto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Ship to contact name |

`exchratedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AR account label. Required if not using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount |
| allocationid | Optional | string | Allocation ID |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| key | Optional | string | Key |
| totalpaid | Optional | currency | Total paid. Used when `nogl` on bill is `true` |
| totaldue | Optional | currency | Total due. Used when `nogl` on bill is `true` |
| customfields | Optional | array of `customfield` | Custom fields |
| revrectemplate | Optional | string | Rev rec template ID |
| defrevaccount | Optional | string | Deferred revenue GL account number |
| revrecstartdate | Optional | object | Rev rec start date |
| revrecenddate | Optional | object | Rev rec end date |
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
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`revrecstartdate`  
`revrecenddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) for the invoice line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the amount due (`TOTAL_DUE`) for the invoice. |

* * *

Update Invoice (Legacy)
-----------------------

[History](https://developer.intacct.com/api/accounts-receivable/invoices/#history-update-invoice-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 4 | Added taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |
| 2024 Release 4 | Added that if \`exchratetype\` used, then \`currency\` required. |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `update_invoice`

```
<update_invoice key="123">
    <updateinvoiceitems>
        <updatelineitem line_num="1">
            <memo>hello world</memo>
        </updatelineitem>
    </updateinvoiceitems>
</update_invoice>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Invoice `RECORDNO` to update |
| customerid | Optional | string | Customer ID |
| datecreated | Optional | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| datedue | Optional | object | Due date. Required if not using `termname`. |
| termname | Optional | string | Payment term. Required if not using `datedue`. |
| action | Optional | string | Action. Use `Draft` or `Submit`. (Default: `Submit`) |
| invoiceno | Optional | string | Invoice number |
| ponumber | Optional | string | Reference number |
| description | Optional | string | Description |
| payto | Optional | object | Bill to contact |
| returnto | Optional | object | Ship to contact |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code. Required if `exchratetype` used. |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. If used, then `currency` is required. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`.) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| supdocid | Optional | string | Attachments ID |
| customfields | Optional | array of `customfield` | Custom fields |
| updateinvoiceitems | Required | `(updatelineitem | lineitem)[1...n]` | To update an existing line use `updatelineitem` otherwise to create a new line use `lineitem`. You can mix types in the array. |

`datecreated`  
`dateposted`  
`datedue`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`payto`  
`returnto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Ship to contact name |

`exchratedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`updatelineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| glaccountno | Optional | string | GL account number. Cannot use if using `accountlabel`. |
| accountlabel | Optional | string | AR account label. Cannot use if using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Optional | currency | Transaction amount |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| customfields | Optional | array of `customfield` | Custom fields |
| revrectemplate | Optional | string | Rev rec template ID |
| defrevaccount | Optional | string | Deferred revenue GL account number |
| revrecstartdate | Optional | object | Rev rec start date |
| revrecenddate | Optional | object | Rev rec end date |
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
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. This a complete replacement of the existing set. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AR account label. Required if not using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount |
| allocationid | Optional | string | Allocation ID |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| key | Optional | string | Key |
| totalpaid | Optional | currency | Total paid. Used when `nogl` on bill is `true` |
| totaldue | Optional | currency | Total due. Used when `nogl` on bill is `true` |
| customfields | Optional | array of `customfield` | Custom fields |
| revrectemplate | Optional | string | Rev rec template ID |
| defrevaccount | Optional | string | Deferred revenue GL account number |
| revrecstartdate | Optional | object | Rev rec start date |
| revrecenddate | Optional | object | Rev rec end date |
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
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed.. |

`revrecstartdate`  
`revrecenddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) for the invoice line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is your manually calculated value for the tax. The amount of the tax line is automatically included in the amount due (`TOTAL_DUE`) for the invoice. Providing a value here overrides any calculated values. |

* * *

Reverse Invoice (Legacy)
------------------------

#### `reverse_invoice`

```
<reverse_invoice key="1234">
    <datereversed>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </datereversed>
</reverse_invoice>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Invoice `RECORDNO` to reverse |
| datereversed | Required | object | Reverse date |
| description | Optional | string | Memo |

`datereversed`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Delete Invoice
--------------

#### `delete`

```
<delete>
    <object>ARINVOICE</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARINVOICE` |
| keys | Required | string | Comma-separated list of invoice `RECORDNO` to delete |

* * *

Delete Invoice (Legacy)
-----------------------

#### `delete_invoice`

```
<delete_invoice key="1234"></delete_invoice>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Invoice `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

