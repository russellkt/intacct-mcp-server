Title: Bills

URL Source: https://developer.intacct.com/api/accounts-payable/bills/

Markdown Content:
*   [Bills](https://developer.intacct.com/api/accounts-payable/bills/#bills)
    *   [Get Bill Object Definition](https://developer.intacct.com/api/accounts-payable/bills/#get-bill-object-definition)
    *   [Query and List Bills](https://developer.intacct.com/api/accounts-payable/bills/#query-and-list-bills)
    *   [Query and List Bills (Legacy)](https://developer.intacct.com/api/accounts-payable/bills/#query-and-list-bills-legacy)
    *   [Get Bill](https://developer.intacct.com/api/accounts-payable/bills/#get-bill)
    *   [Create Bill](https://developer.intacct.com/api/accounts-payable/bills/#create-bill)
    *   [Create Bill (Legacy)](https://developer.intacct.com/api/accounts-payable/bills/#create-bill-legacy)
    *   [Update Bill](https://developer.intacct.com/api/accounts-payable/bills/#update-bill)
    *   [Update Bill (Legacy)](https://developer.intacct.com/api/accounts-payable/bills/#update-bill-legacy)
    *   [Reverse Bill (Legacy)](https://developer.intacct.com/api/accounts-payable/bills/#reverse-bill-legacy)
    *   [Delete Bill](https://developer.intacct.com/api/accounts-payable/bills/#delete-bill)
    *   [Delete Bill (Legacy)](https://developer.intacct.com/api/accounts-payable/bills/#delete-bill-legacy)
    *   [Recall Bill](https://developer.intacct.com/api/accounts-payable/bills/#recall-bill)
*   [Bill Lines](https://developer.intacct.com/api/accounts-payable/bills/#bill-lines)
    *   [Get Bill Line Object Definition](https://developer.intacct.com/api/accounts-payable/bills/#get-bill-line-object-definition)
    *   [Query and List Bill Lines](https://developer.intacct.com/api/accounts-payable/bills/#query-and-list-bill-lines)
    *   [Query and List Bill Lines (Legacy)](https://developer.intacct.com/api/accounts-payable/bills/#query-and-list-bill-lines-legacy)
    *   [Get Bill Line](https://developer.intacct.com/api/accounts-payable/bills/#get-bill-line)

* * *

An AP bill is a transaction that tracks money owed to a vendor.

Certain types of transaction definitions in Purchasing (e.g. Vendor Invoice) are configured to create corresponding bills in the Accounts Payable module. When a transaction is updated in Purchasing, the related AP transaction is deleted and recreated. As a result, the AP transaction will have a new `RECORDNO`. Integrations relying on these records should consider using a `MODULEKEY` filter outlined below.

* * *

### Get Bill Object Definition

#### `lookup`

> List all the fields and relationships for the AP bill object:

```
<lookup>
    <object>APBILL</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILL` |

* * *

### Query and List Bills

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and vendor ID for each bill where the vendor name starts with the letter `B`:

```
<query>
    <object>APBILL</object>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
    </select>
    <filter>
        <like>
            <field>VENDORNAME</field>
            <value>B%</value>
        </like>
    </filter>
</query>
```

> List bills from the given vendor that are available for payment:

```
<query>
    <object>APBILL</object>
    <select>
        <field>RECORDNO</field>
        <field>RECORDID</field>
        <field>VENDORID</field>
        <field>STATE</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>VENDORID</field>
                <value>Acme</value>
            </equalto>
            <in>
                <field>STATE</field>
                <value>Selected</value>
                <value>Posted</value>
            </in>
        </and>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILL` |
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

### Query and List Bills (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APBILL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| MODULEKEY | Optional | string | Source module transaction created from.
*   `3.AP` - Accounts Payable
*   `9.PO` - Purchasing

 |
| STATE | Optional | string | State of the bill.

*   `D` - Draft
*   `PA` - Partially Approved
*   `S` - Submitted
*   `U` - Declined
*   `A` - Posted

 |

* * *

### Get Bill

#### `read`

```
<read>
    <object>APBILL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILL` |
| keys | Required | string | Comma-separated list of bill `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Bill

[History](https://developer.intacct.com/api/accounts-payable/bills/#history-create-bill)

| Release | Changes |
| --- | --- |
| 2022 Release 1 | Changed required fields when Action==Draft |
| 2021 Release 2 | Added PARTIALEXEMPT |
| 2020 Release 2 | Added COSTTYPEID, TAXSOLUTIONID, INCLUSIVETAX, TOTALTRXAMOUNT |
| 2019 Release 4 | Added TASKID |
| 2019 Release 3 | Added TAXENTRIES |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create`

> Create a bill with one line:

```
<create>
    <APBILL>
        <WHENCREATED>12/15/2016</WHENCREATED>
        <WHENPOSTED>12/15/2016</WHENPOSTED>
        <VENDORID>20000</VENDORID>
        <RECORDID>1234</RECORDID>
        <DOCNUMBER>Ref 5678</DOCNUMBER>
        <DESCRIPTION>My bill</DESCRIPTION>
        <TERMNAME>N30</TERMNAME>
        <RECPAYMENTDATE>12/23/2016</RECPAYMENTDATE>
        <SUPDOCID>A1234</SUPDOCID>
        <WHENDUE>12/25/2016</WHENDUE>
        <PAYMENTPRIORITY>high</PAYMENTPRIORITY>
        <ONHOLD>false</ONHOLD>
        <CURRENCY>USD</CURRENCY>
        <BASECURR>USD</BASECURR>
        <APBILLITEMS>
            <APBILLITEM>
                <ACCOUNTNO>6220</ACCOUNTNO>
                <TRX_AMOUNT>100.12</TRX_AMOUNT>
                <ENTRYDESCRIPTION>Line 1 of my bill</ENTRYDESCRIPTION>
                <LOCATIONID>110</LOCATIONID>
                <DEPARTMENTID>D300</DEPARTMENTID>
            </APBILLITEM>
        </APBILLITEMS>
    </APBILL>
</create>
```

> Create a bill with a tax entry on one line and have the system calculate the total transaction amount and transaction tax (AU, GB, ZA only):

```
<create>
    <APBILL>
        <VENDORID>A-1-Auto</VENDORID>
        <WHENCREATED>07/10/2019</WHENCREATED>
        <INCLUSIVETAX>true</INCLUSIVETAX>
        <CURRENCY>USD</CURRENCY>
        <BASECURR>EUR</BASECURR>
        <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
        <EXCHANGE_RATE>1.08477</EXCHANGE_RATE>
        <APBILLITEMS>
            <APBILLITEM>
                <ACCOUNTNO>1400</ACCOUNTNO>
                <TOTALTRXAMOUNT></TOTALTRXAMOUNT>
                <TAXENTRIES>
                    <TAXENTRY>
                        <DETAILID>UK Import Goods Standard Rate</DETAILID>
                        <TRX_TAX></TRX_TAX>
                    </TAXENTRY>
                </TAXENTRIES>
                <LOCATIONID>1</LOCATIONID>
            </APBILLITEM>
        </APBILLITEMS>
    </APBILL>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APBILL | Required | [object](https://developer.intacct.com/api/accounts-payable/bills/#create-APBILL) | Object to create |

`APBILL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDORID | Optional | string | Vendor ID. Required if `Action` is not set to `Draft`. |
| WHENCREATED | Optional | string | Transaction date in format `mm/dd/yyyy`. Required if `Action` is not set to `Draft`. |
| WHENPOSTED | Optional | string | GL posting date in format `mm/dd/yyyy`. Not used if `PRBATCH` provided. |
| BILLTOPAYTOCONTACTNAME | Optional | string | Pay to contact |
| SHIPTORETURNTOCONTACTNAME | Optional | string | Return to contact |
| RECORDID | Optional | string | Bill number |
| DOCNUMBER | Optional | string | Reference number |
| DESCRIPTION | Optional | string | Description |
| TERMNAME | Optional | string | Payment term |
| RECPAYMENTDATE | Optional | string | Recommended to pay on date in format `mm/dd/yyyy` |
| SUPDOCID | Optional | string | Attachments ID |
| WHENDUE | Optional | string | Due date in format `mm/dd/yyyy`. Required if `Action` is not set to `Draft`. |
| PAYMENTPRIORITY | Optional | string | Payment priority.
*   `urgent`
*   `high`
*   `normal` (default)
*   `low`

 |
| ONHOLD | Optional | boolean | On hold.

*   `false` - No (detault)
*   `true` - Yes

 |
| PRBATCH | Optional | string | Summary name to post into. Required if bill summary option is set to user specified in AP config. |
| CURRENCY | Optional | string | Transaction currency code |
| BASECURR | Optional | string | Base currency code |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy` |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Do not use if `EXCHANGE_RATE` is set. (Leave blank to use `Intacct Daily Rate`) |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value. Do not use if `EXCH_RATE_TYPE_ID` is set. |
| INCLUSIVETAX | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`TRX_AMOUNT`) for the bill line and the transaction tax (`TRX_TAX`) for the tax entry based on the value supplied for `TOTALTRXAMOUNT` on the bill line and the tax rate of the tax detail (`DETAILID`) for the tax entry. (AU, GB, ZA only) |
| ACTION | Optional | string | Action to execute on create.

*   `Submit` (default)
*   `Draft`

 |
| TAXSOLUTIONID | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. See [Tax Solutions](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/) for more information. (GB, AU, and ZA only) |
| APBILLITEMS | Required | array of [APBILLITEM](https://developer.intacct.com/api/accounts-payable/bills/#create-APBILLITEM) | Bill lines, must have at least 1. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`APBILL.APBILLITEMS.APBILLITEM`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTNO | Optional | string | GL account number. Required if not using `ACCOUNTLABEL`. |
| ACCOUNTLABEL | Optional | string | AP account label. Required if not using `ACCOUNTNO`. |
| OFFSETGLACCOUNTNO | Optional | string | AP account number |
| TRX\_AMOUNT | Optional | currency | Transaction amount before taxes. This value is required if `INCLUSIVETAX` is set to `false` (or omitted) on the header. (This value will be ignored as an input if `INCLUSIVETAX` is `true` because the value will be calculated for you.) |
| TOTALTRXAMOUNT | Optional | currency | Transaction amount for the line including taxes, which is required if `INCLUSIVETAX` is set to `true` on the header. The system uses the value you provide here and the tax rate of the tax detail (`DETAILID`) for the tax entry to calculate the transaction amount (`TRX_AMOUNT`) for the line and transaction tax (`TRX_TAX`) for the tax entry. (AU, GB, ZA only) |
| ENTRYDESCRIPTION | Optional | string | Memo |
| FORM1099 | Optional | boolean | Form 1099. Vendor must be set up for 1099s.
*   `false` - No
*   `true` - Yes

 |
| FORM1099TYPE | Optional | string | Form 1099 type |
| FORM1099BOX | Optional | string | Form 1099 box |
| BILLABLE | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| ALLOCATION | Optional | string | Allocation ID |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID. Only valid when the parent `PROJECTID` is also specified. |
| COSTTYPEID | Optional | string | Cost type ID. Only valid when `PROJECTID` and `TASKID` are specified. (Construction subscription) |
| CUSTOMERID | Optional | string | Customer ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CLASSID | Optional | string | Class ID |
| CONTRACTID | Optional | string | Contract ID |
| WAREHOUSEID | Optional | string | Warehouse ID |
| GLDIM\* | Optional | integer | User defined dimension `id` field. UDD object integration name usually appended to `GLDIM` |
| PARTIALEXEMPT | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases. (GB only)

*   `false` - No (detault)
*   `true` - Yes

 |
| TAXENTRIES | Optional | array of [TAXENTRY](https://developer.intacct.com/api/accounts-payable/bills/#create-APBILLITEM.TAXITEM) | Tax entries for the line. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`APBILL.APBILLITEMS.APBILLITEM.TAXENTRIES.TAXENTRY` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) for the bill line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DETAILID | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| TRX\_TAX | Optional | currency | Transaction tax, which is your manually calculated value for the tax. The amount of the tax line is automatically included in the amount due (`TOTAL_DUE`) for the bill. Providing a value here overrides any calculated values. |

* * *

### Create Bill (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/bills/#history-create-bill-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added partialexempt |
| 2021 Release 1 | Added inclusivetax, taxsolutionid, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_bill`

> Create a bill:

```
<create_bill>
    <vendorid>V1234</vendorid>
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
    <action>Submit</action>
    <batchkey></batchkey>
    <billno>1234</billno>
    <ponumber>234235</ponumber>
    <onhold>false</onhold>
    <description>Some description</description>
    <externalid></externalid>
    <payto>
        <contactname>jsmith</contactname>
    </payto>
    <returnto>
        <contactname>bsmith</contactname>
    </returnto>
    <basecurr>USD</basecurr>
    <currency>USD</currency>
    <exchratedate>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </exchratedate>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <nogl>false</nogl>
    <supdocid>A1111</supdocid>
    <customfields>
        <customfield>
            <customfieldname>customfield1</customfieldname>
            <customfieldvalue>customvalue1</customfieldvalue>
        </customfield>
    </customfields>
    <billitems>
        <lineitem>
            <glaccountno>6700</glaccountno>
            <offsetglaccountno>2010</offsetglaccountno>
            <amount>76343.43</amount>
            <memo>Just another memo</memo>
            <locationid>Location1</locationid>
            <departmentid>Department1</departmentid>
            <item1099>true</item1099>
            <key></key>
            <totalpaid></totalpaid>
            <totaldue></totaldue>
            <customfields>
                <customfield>
                    <customfieldname>customfield1</customfieldname>
                    <customfieldvalue>customvalue1</customfieldvalue>
                </customfield>
            </customfields>
            <projectid>Project1</projectid>
            <customerid>Customer1</customerid>
            <vendorid>Vendor1</vendorid>
            <employeeid>Employee1</employeeid>
            <itemid>Item1</itemid>
            <classid>Class1</classid>
            <contractid>Contract1</contractid>
            <warehouseid>Warehouse1</warehouseid>
            <billable>true</billable>
        </lineitem>
    </billitems>
</create_bill>
```

> Use inclusive tax so that the system calculates the transaction amount (`trx_amount`) for the bill line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the bill line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only).

```
<create_bill>
    <vendorid>1099 Int</vendorid>
    <datecreated>
        <year>2020</year>
        <month>09</month>
        <day>02</day>
    </datecreated>
    <termname>N30</termname>
    <action>Submit</action>
    <billno>Bill-151</billno>
    <description>Bill from 2.1 API with vat amount</description>
    <basecurr>AUD</basecurr>
    <currency>AUD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <taxsolutionid>Australia - GST</taxsolutionid>
    <billitems>
        <lineitem>
            <glaccountno>1200</glaccountno>
            <amount>123.45</amount>
            <memo>line 1 with tax</memo>
            <locationid>4</locationid>
            <taxentries>
                <taxentry>
                    <detailid>G10 Capital Acquisition</detailid>
                    <trx_tax>11.11</trx_tax>
                </taxentry>
            </taxentries>
        </lineitem>
        <lineitem>
            <glaccountno>1200</glaccountno>
            <amount>256.90</amount>
            <memo>line2 with multitax</memo>
            <locationid>4</locationid>
            <taxentries>
                <taxentry>
                    <detailid>G13 Capital Purchases for Input Tax Sales</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
                <taxentry>
                    <detailid>G11 Other Acquisition</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
            </taxentries>
        </lineitem>
    </billitems>
</create_bill>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| vendorid | Required | string | Vendor ID |
| datecreated | Required | [object](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.date) | Transaction date |
| dateposted | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.date) | GL posting date |
| datedue | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.date) | Due date. Required if not using `termname`. |
| termname | Optional | string | Payment term. Required if not using `datedue`. |
| action | Optional | string | Action to execute on create.
*   `Submit` (default)
*   `Draft`

 |
| batchkey | Optional | integer | Summary record number |
| billno | Optional | string | Bill number |
| ponumber | Optional | string | Reference number |
| onhold | Optional | boolean | On hold.

*   `false` - No (detault)
*   `true` - Yes

 |
| description | Optional | string | Description |
| externalid | Optional | string | External ID |
| payto | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.payto) | Pay to contact |
| returnto | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.returnto) | Return to contact |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.date) | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| nogl | Optional | boolean | Do not post to GL.

*   `false` - No (default)
*   `true` - Yes

 |
| supdocid | Optional | string | Attachments ID |
| customfields | Optional | array of [customfield](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.customfield) | Custom fields |
| billitems | Required | array of [lineitem](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.lineitem) | Bill lines, must have at least 1. |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the bill line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the bill line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. See [Tax Solutions](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/) for more information. (GB, AU, and ZA only) |

`create_bill.datecreated`  
`create_bill.dateposted`  
`create_bill.datedue`  
`create_bill.exchangeratedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`create_bill.payto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Pay to contact name |

`create_bill.returnto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Return to contact name |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`create_bill.lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount |
| allocationid | Optional | string | Allocation ID |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| item1099 | Optional | boolean | Form 1099. Vendor must be set up for 1099s.
*   `false` - No
*   `true` - Yes

 |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| key | Optional | string | Key |
| totalpaid | Optional | currency | Total paid. Used when `nogl` on bill is `true` |
| totaldue | Optional | currency | Total due. Used when `nogl` on bill is `true` |
| customfields | Optional | array of [customfield](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.lineitem.customfield) | Custom fields |
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
| billable | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| partialexempt | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases. (GB only)

*   `false` - No (detault)
*   `true` - Yes

 |
| taxentries | Optional | array of [taxentry](https://developer.intacct.com/api/accounts-payable/bills/#create_bill.lineitem.taxentry) | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`create_bill.lineitem.taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the other bill line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the transaction amount (`trx_amount`). |

* * *

### Update Bill

[History](https://developer.intacct.com/api/accounts-payable/bills/#history-update-bill)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added PARTIALEXEMPT |
| 2020 Release 2 | Added COSTTYPEID, INCLUSIVETAX, TOTALTRXAMOUNT |
| 2019 Release 4 | Added TASKID |
| 2019 Release 3 | Added TAXENTRIES |

> Update header information only:

```
<update>
    <APBILL>
        <RECORDNO>65</RECORDNO>
        <DESCRIPTION>Changing the description</DESCRIPTION>
    </APBILL>
</update>
```

> Update header and a bill line:

```
<update>
    <APBILL>
        <RECORDNO>65</RECORDNO>
        <DESCRIPTION>Changing the description</DESCRIPTION>
        <RECPAYMENTDATE>12/25/2016</RECPAYMENTDATE>
        <WHENDUE>12/31/2016</WHENDUE>
        <APBILLITEMS>
            <APBILLITEM>
                <LINE_NO>1</LINE_NO>
                <ACCOUNTNO>6225</ACCOUNTNO>
                <TRX_AMOUNT>100.12</TRX_AMOUNT>
                <ENTRYDESCRIPTION>Line 1 of my bill</ENTRYDESCRIPTION>
                <LOCATIONID>110</LOCATIONID>
                <DEPARTMENTID>D300</DEPARTMENTID>
            </APBILLITEM>
        </APBILLITEMS>
    </APBILL>
</update>
```

When updating header information of a bill, you do not need to include all the original bill lines.

You can also modify, add, or delete lines as part of your update. To add a bill line, supply all the original lines along with the new one. To delete a line, supply only the lines that you want to keep. To modify a line, supply all the original lines and change the field values you want.

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APBILL | Required | object | Object to update |

`APBILL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Bill `RECORDNO` to update |
| WHENCREATED | Optional | string | Transaction date in format `mm/dd/yyyy` |
| WHENPOSTED | Optional | string | GL posting date in format `mm/dd/yyyy`. Not used if `PRBATCH` provided. |
| VENDORID | Optional | string | Vendor ID |
| BILLTOPAYTOCONTACTNAME | Optional | string | Pay to contact |
| SHIPTORETURNTOCONTACTNAME | Optional | string | Return to contact |
| RECORDID | Optional | string | Bill number |
| DOCNUMBER | Optional | string | Reference number |
| DESCRIPTION | Optional | string | Description |
| TERMNAME | Optional | string | Payment term |
| RECPAYMENTDATE | Optional | string | Recommended to pay on date in format `mm/dd/yyyy` |
| SUPDOCID | Optional | string | Attachments ID |
| WHENDUE | Required | string | Due date in format `mm/dd/yyyy` |
| PAYMENTPRIORITY | Optional | string | Payment priority.
*   `urgent`
*   `high`
*   `normal` (default)
*   `low`

 |
| ONHOLD | Optional | boolean | On hold.

*   `false` - No (detault)
*   `true` - Yes

 |
| PRBATCH | Optional | string | Summary name to post into. |
| CURRENCY | Optional | string | Transaction currency code |
| BASECURR | Optional | string | Base currency code |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy` |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Do not use if `EXCHANGE_RATE` is set. (Leave blank to use `Intacct Daily Rate`) |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value. Do not use if `EXCH_RATE_TYPE_ID` is set. |
| INCLUSIVETAX | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`TRX_AMOUNT`) for the bill line and the transaction tax (`TRX_TAX`) for the tax entry based on the value supplied for `TOTALTRXAMOUNT` on the bill line and the tax rate of the tax detail (`DETAILID`) for the tax entry. (AU, GB, ZA only) |
| ACTION | Optional | string | Action to execute on update.

*   `Submit` (default)
*   `Draft`

 |
| APBILLITEMS | Optional | array of [APBILLITEM](https://developer.intacct.com/api/accounts-payable/bills/#update-APBILLITEM) | Bill lines. To add a bill line, supply all the original lines along with the new one. To delete a line, supply only the lines that you want to keep. To modify a line, supply all the original lines and change the field values you want. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`APBILL.APBILLITEMS.APBILLITEM`

(AU, GB, ZA) You must include any existing tax entries in order to retain them. To delete a tax entry, perform an update and omit the `TAXENTRIES` for the line. To modify a tax entry, provide the record number and the new values.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LINE\_NO | Optional | integer | Line number to update otherwise leave blank to add a new line. |
| ACCOUNTNO | Optional | string | GL account number. Required if not using `ACCOUNTLABEL`. |
| ACCOUNTLABEL | Optional | string | AP account label. Required if not using `ACCOUNTNO`. |
| OFFSETGLACCOUNTNO | Optional | string | AP account number |
| TRX\_AMOUNT | Optional | currency | Transaction amount before taxes. This value is required if `INCLUSIVETAX` is set to `false` (or omitted) on the header. (This value will be ignored as an input if `INCLUSIVETAX` is `true` because the value will be calculated for you.) |
| TOTALTRXAMOUNT | Optional | currency | Transaction amount for the line including taxes, which is required if `INCLUSIVETAX` is set to `true` on the header. The system uses the value you provide here and the tax rate of the tax detail (`DETAILID`) for the tax entry to calculate the transaction amount (`TRX_AMOUNT`) for the line and transaction tax (`TRX_TAX`) for the tax entry. (AU, GB, ZA only) |
| ENTRYDESCRIPTION | Optional | string | Memo |
| FORM1099 | Optional | boolean | Form 1099. Vendor must be set up for 1099s.
*   `false` - No
*   `true` - Yes

 |
| FORM1099TYPE | Optional | string | Form 1099 type |
| FORM1099BOX | Optional | string | Form 1099 box |
| BILLABLE | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| ALLOCATION | Optional | string | Allocation ID |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID. Only available when the parent `PROJECTID` is also specified. |
| COSTTYPEID | Optional | string | Cost type ID. Only available when `PROJECTID` and `TASKID` are specified. (Construction subscription) |
| CUSTOMERID | Optional | string | Customer ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CLASSID | Optional | string | Class ID |
| CONTRACTID | Optional | string | Contract ID |
| WAREHOUSEID | Optional | string | Warehouse ID |
| GLDIM\* | Optional | integer | User defined dimension `id` field. UDD object integration name usually appended to `GLDIM` |
| PARTIALEXEMPT | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases. (GB only)

*   `false` - No (detault)
*   `true` - Yes

 |
| TAXENTRIES | Optional | array of [TAXENTRY](https://developer.intacct.com/api/accounts-payable/bills/#update-APBILLITEM.TAXENTRY) | Tax entries for the line. This a complete replacement of the existing set. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

\`APBILL.APBILLITEMS.APBILLITEM.TAXENTRIES.TAXENTRY (AU, GB, ZA only)

Specifies a tax rate (defined in the system) for the bill line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of an existing tax entry (associated with this line) that you want to modify. You can omit this parameter to create a new tax entry. |
| DETAILID | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| TRX\_TAX | Optional | currency | Transaction tax, which is your manually calculated value for the tax. The amount of the tax line is automatically included in the amount due (`TOTAL_DUE`) for the bill. Providing a value here overrides any calculated values. |

* * *

### Update Bill (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/bills/#history-update-bill-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added partialexempt |
| 2021 Release 1 | Added inclusivetax, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `update_bill`

```
<update_bill key="1234">
    <updatebillitems>
        <updatelineitem line_num="1">
            <glaccountno>7940</glaccountno>
        </updatelineitem>
    </updatebillitems>
</update_bill>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Bill `RECORDNO` to update |
| vendorid | Optional | string | Vendor ID |
| datecreated | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.date) | Transaction date |
| dateposted | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.date) | GL posting date |
| datedue | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.date) | Due date. Required if not using `termname`. |
| termname | Optional | string | Payment term. Required if not using `datedue`. |
| action | Optional | string | Action to execute on update.
*   `Submit` (default)
*   `Draft`

 |
| billno | Optional | string | Bill number |
| ponumber | Optional | string | Reference number |
| onhold | Optional | boolean | On hold.

*   `false` - No (detault)
*   `true` - Yes

 |
| description | Optional | string | Description |
| payto | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.payto) | Pay to contact |
| returnto | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.returnto) | Return to contact |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | [object](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.date) | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| supdocid | Optional | string | Attachments ID |
| customfields | Optional | array of [customfield](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.customfield) | Custom fields |
| updatebillitems | Required | array of [updatelineitem](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.updatelineitem) or [lineitem](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.lineitem) | You can mix types in the array.

*   `updatelineitem` - Update an existing line
*   `lineitem` - Create a new line

 |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the bill line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the bill line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |

```

update_bill.datecreated
```  
`update_bill.dateposted`  
`update_bill.datedue`  
`update_bill.exchangeratedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_bill.payto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Pay to contact name |

`update_bill.returnto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Return to contact name |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`update_bill.updatebillitems.updatelineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| glaccountno | Optional | string | GL account number. Cannot use if using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Cannot use if using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Optional | currency | Transaction amount |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| item1099 | Optional | boolean | Form 1099. Vendor must be set up for 1099s.
*   `false` - No
*   `true` - Yes

 |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| customfields | Optional | array of `customfield` | Custom fields |
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
| billable | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| partialexempt | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases. (GB only)

*   `false` - No (detault)
*   `true` - Yes

 |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`update_bill.updatebillitems.lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount |
| allocationid | Optional | string | Allocation ID |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| item1099 | Optional | boolean | Form 1099. Vendor must be set up for 1099s.
*   `false` - No
*   `true` - Yes

 |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| key | Optional | string | Key |
| totalpaid | Optional | currency | Total paid. Used when `nogl` on bill is `true` |
| totaldue | Optional | currency | Total due. Used when `nogl` on bill is `true` |
| customfields | Optional | array of `customfield` | Custom fields |
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
| billable | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| partialexempt | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases. (GB only)

*   `false` - No (detault)
*   `true` - Yes

 |
| taxentries | Optional | array of [taxentry](https://developer.intacct.com/api/accounts-payable/bills/#update_bill.lineitem.taxentry) | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`update_bill.updatebillitems.lineitem.taxentry`  
`update_bill.updatebillitems.updatelineitem.taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the bill line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the transaction amount (`trx_amount`). |

* * *

### Reverse Bill (Legacy)

#### `reverse_bill`

```
<reverse_bill key="1234">
    <datereversed>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </datereversed>
</reverse_bill>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Bill `RECORDNO` to reverse |
| datereversed | Required | object | Reverse date |
| description | Optional | string | Memo |

`datereversed`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

### Delete Bill

#### `delete`

```
<delete>
    <object>APBILL</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILL` |
| keys | Required | string | Comma-separated list of bill `RECORDNO` to delete |

* * *

### Delete Bill (Legacy)

#### `delete_bill`

```
<delete_bill key="1234"></delete_bill>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Bill `RECORDNO` to delete |

* * *

### Recall Bill

[History](https://developer.intacct.com/api/accounts-payable/bills/#history-recall-bill)

| Release | Changes |
| --- | --- |
| 2023 Release 4 | Added recallApBill |

#### `recallApBill`

```
<recallApBill>
    <recordno>41</recordno>
</recallApBill>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the bill to recall. |

* * *

Bill Lines
----------

### Get Bill Line Object Definition

#### `lookup`

> List all the fields and relationships for the bill line object:

```
<lookup>
    <object>APBILLITEM</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLITEM` |

* * *

### Query and List Bill Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, amount, and GL account title for each bill line:

```
<query>
    <object>APBILLITEM</object>
    <select>
        <field>RECORDNO</field>
        <field>AMOUNT</field>
        <field>GLACCOUNT.TITLE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLITEM` |
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

### Query and List Bill Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APBILLITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLITEM` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Bill Line

#### `read`

```
<read>
    <object>APBILLITEM</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLITEM` |
| keys | Required | string | Comma-separated list of transaction line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

