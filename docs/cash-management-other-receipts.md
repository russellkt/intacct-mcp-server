Title: Other Receipts

URL Source: https://developer.intacct.com/api/cash-management/other-receipts/

Markdown Content:
*   [Other Receipts](https://developer.intacct.com/api/cash-management/other-receipts/#other-receipts)
    *   [Get Other Receipts Object Definition](https://developer.intacct.com/api/cash-management/other-receipts/#get-other-receipts-object-definition)
    *   [Query and List Other Receipts](https://developer.intacct.com/api/cash-management/other-receipts/#query-and-list-other-receipts)
    *   [Query and List Other Receipts (Legacy)](https://developer.intacct.com/api/cash-management/other-receipts/#query-and-list-other-receipts-legacy)
    *   [List Other Receipts (Legacy)](https://developer.intacct.com/api/cash-management/other-receipts/#list-other-receipts-legacy)
    *   [Get Other Receipt](https://developer.intacct.com/api/cash-management/other-receipts/#get-other-receipt)
    *   [Get Other Receipt (legacy)](https://developer.intacct.com/api/cash-management/other-receipts/#get-other-receipt-legacy)
    *   [Create Other Receipt (Legacy)](https://developer.intacct.com/api/cash-management/other-receipts/#create-other-receipt-legacy)
    *   [Update Other Receipt (Legacy)](https://developer.intacct.com/api/cash-management/other-receipts/#update-other-receipt-legacy)
    *   [Delete Other Receipt (Legacy)](https://developer.intacct.com/api/cash-management/other-receipts/#delete-other-receipt-legacy)
*   [Other Receipt Lines](https://developer.intacct.com/api/cash-management/other-receipts/#other-receipt-lines)
    *   [Get Other Receipt Line Object Definition](https://developer.intacct.com/api/cash-management/other-receipts/#get-other-receipt-line-object-definition)
    *   [Query and List Other Receipt Lines](https://developer.intacct.com/api/cash-management/other-receipts/#query-and-list-other-receipt-lines)
    *   [Query and List Other Receipt Lines (Legacy)](https://developer.intacct.com/api/cash-management/other-receipts/#query-and-list-other-receipt-lines-legacy)
    *   [Get Other Receipt Line](https://developer.intacct.com/api/cash-management/other-receipts/#get-other-receipt-line)

* * *

Receipts that are not associated with a customer or invoice.

Can include cash, a card charge, a cash transfer, or a check payment.

* * *

### Get Other Receipts Object Definition

#### `lookup`

> List all the fields and relationships for the other receipts object:

```
<lookup>
    <object>OTHERRECEIPTS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTS` |

* * *

### Query and List Other Receipts

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, total entered, and description for each other receipt:

```
<query>
    <object>OTHERRECEIPTS</object>
    <select>
        <field>RECORDNO</field>
        <field>TOTALENTERED</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTS` |
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

### Query and List Other Receipts (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>OTHERRECEIPTS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### List Other Receipts (Legacy)

#### `get_list`

```
<get_list object="otherreceipts" maxitems="1">
</get_list>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string attribute | Use `otherreceipts` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/cash-management/other-receipts/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/cash-management/other-receipts/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/cash-management/other-receipts/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/cash-management/other-receipts/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/cash-management/other-receipts/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

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

### Get Other Receipt

#### `read`

```
<read>
    <object>OTHERRECEIPTS</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTS` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Other Receipt (legacy)

#### `get`

```
<get object="otherreceipts" key="1234"></get>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `otherreceipts` |
| key | Required | string | Object `RECORDNO` to get |

* * *

### Create Other Receipt (Legacy)

[History](https://developer.intacct.com/api/cash-management/other-receipts/#history-create-other-receipt-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 4 | Added inclusivetax, taxsolutionid, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `record_otherreceipt`

> Create an other receipt record:

```
<record_otherreceipt>
    <paymentdate>
        <year>2017</year>
        <month>01</month>
        <day>25</day>
    </paymentdate>
    <payee>Costco</payee>
    <receiveddate>
        <year>2017</year>
        <month>01</month>
        <day>26</day>
    </receiveddate>
    <paymentmethod>EFT</paymentmethod>
    <bankaccountid>BOFA1435</bankaccountid>
    <depositdate>
        <year>2017</year>
        <month>01</month>
        <day>26</day>
    </depositdate>
    <refid>1234</refid>
    <description></description>
    <receiptitems>
        <lineitem>
            <glaccountno>41100</glaccountno>
            <amount>50.99</amount>
            <memo></memo>
            <locationid>ARL-VA-US</locationid>
            <departmentid>ADM</departmentid>
        </lineitem>
    </receiptitems>
</record_otherreceipt>
```

> Use inclusive tax so that the system calculates the transaction amount (`trx_amount`) for the receipt line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the receipt line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only).

```
<record_otherreceipt>
    <paymentdate>
        <year>2020</year>
        <month>09</month>
        <day>21</day>
    </paymentdate>
    <payee>Costco</payee>
    <receiveddate>
        <year>2020</year>
        <month>09</month>
        <day>21</day>
    </receiveddate>
    <paymentmethod>Printed Check</paymentmethod>
    <bankaccountid>BMEL</bankaccountid>
    <depositdate>
        <year>2020</year>
        <month>9</month>
        <day>26</day>
    </depositdate>
    <description/>
    <inclusivetax>true</inclusivetax>
    <taxsolutionid>Australia - GST</taxsolutionid>
    <receiptitems>
        <lineitem>
            <glaccountno>4000</glaccountno>
            <amount></amount>
            <memo></memo>
            <locationid>4</locationid>
            <totaltrxamount>10000</totaltrxamount>
            <taxentries>
                <taxentry>
                    <detailid>AUS Standard1</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
            </taxentries>
        </lineitem>
    </receiptitems>
</record_otherreceipt>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| paymentdate | Required | object | Payment date |
| payee | Required | string | Payer (the parameter is incorrectly named) |
| receiveddate | Required | object | Received date |
| paymentmethod | Required | string | Payment method. Use `Printed Check`, `Cash`, `EFT`, or `Credit Card`. |
| undepglaccountno | Optional | string | Undeposited GL account. Required if not using `bankaccountid`. |
| bankaccountid | Optional | string | Bank account ID. Required if not using `undepglaccountno`. |
| depositdate | Optional | object | Deposit date. Only used if `bankaccountid` is set. |
| refid | Optional | string | Reference ID |
| description | Optional | string | Description |
| supdocid | Optional | string | Attachments ID |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| customfields | Optional | array of `customfield` | Custom fields on transaction object |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the receipt line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the receipt line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only). (Default: `false`) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. The available tax solution names can be found in the Sage Intacct UI in the Taxes application from the top level of a multi-entity company. (GB, AU, and ZA only) |
| receiptitems | Required | `lineitem[1...n]` | Receipt lines, must have at least 1 |

`paymentdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`receiveddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`depositdate`

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

`lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| amount | Required | currency | Transaction amount. Do not supply if inclusive tax is set to `true`. |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the other receipt line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

### Update Other Receipt (Legacy)

[History](https://developer.intacct.com/api/cash-management/other-receipts/#history-update-other-receipt-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 4 | Added inclusivetax, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

You cannot update an other receipt that was created with inclusive tax set to true.

#### `update_otherreceipt`

> Updates a receipt by modifying an existing line and adding a new line:

```
<update_otherreceipt key="1234">
    <receiptitems>
        <updatelineitem line_num="1">
            <memo>Organization dues</memo>
        </updatelineitem>
        <lineitem>
            <glaccountno>1907</glaccountno>
            <amount>1000</amount>
            <locationid>NY</locationid>
        </lineitem>
    </receiptitems>
</update_otherreceipt>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Other receipt `RECORDNO` to update |
| paymentdate | Optional | object | Payment date |
| payee | Optional | string | Payer (the parameter is incorrectly named) |
| receiveddate | Optional | object | Received date |
| paymentmethod | Optional | string | Payment method. Use `Printed Check`, `Cash`, `EFT`, or `Credit Card`. |
| undepglaccountno | Optional | string | Undeposited GL account. Required if not using `bankaccountid`. |
| bankaccountid | Optional | string | Bank account ID. Required if not using `undepglaccountno`. |
| depositdate | Optional | object | Deposit date. Only used if `bankaccountid` is set. |
| refid | Optional | string | Reference ID |
| description | Optional | string | Description |
| supdocid | Optional | string | Attachments ID |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| customfields | Optional | array of `customfield` | Custom fields on transaction object |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the receipt line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the receipt line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |
| receiptitems | Optional | `(lineitem | updatelineitem)[1...n]` | Receipt lines, must have at least 1 |

`paymentdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`receiveddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`depositdate`

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

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| amount | Required | currency | Transaction amount. Do not supply if inclusive tax is set to `true` on the header. |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`updatelineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | string | Line number of the entry to update |
| glaccountno | Optional | string | GL account number |
| accountlabel | Optional | string | AP account label |
| amount | Optional | currency | Transaction amount. Do not supply if inclusive tax is set to `true` on the header. |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| totaltrxamount | Optional | currency | Total transaction amount. Only allowed if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. This a complete replacement of the existing set. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the other receipt line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

### Delete Other Receipt (Legacy)

#### `delete_otherreceipt`

```
<delete_otherreceipt key="1234"></delete_otherreceipt>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Other receipt `RECORDNO` to delete |

* * *

Other Receipt Lines
-------------------

### Get Other Receipt Line Object Definition

#### `lookup`

> List all the fields and relationships for the other receipt line object:

```
<lookup>
    <object>OTHERRECEIPTSENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTENTRY` |

* * *

### Query and List Other Receipt Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, amount, and description for each other receipt line:

```
<query>
    <object>OTHERRECEIPTSENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>AMOUNT</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTENTRY` |
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

### Query and List Other Receipt Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>OTHERRECEIPTSENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTSENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Other Receipt Line

#### `read`

```
<read>
    <object>OTHERRECEIPTSENTRY</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `OTHERRECEIPTSENTRY` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

