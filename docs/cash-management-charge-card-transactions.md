Title: Charge Card Transactions

URL Source: https://developer.intacct.com/api/cash-management/charge-card-transactions/

Markdown Content:
*   [Charge Card Transactions](https://developer.intacct.com/api/cash-management/charge-card-transactions/#charge-card-transactions)
    *   [Get Charge Card Transaction Object Definition](https://developer.intacct.com/api/cash-management/charge-card-transactions/#get-charge-card-transaction-object-definition)
    *   [Query and List Charge Card Transactions](https://developer.intacct.com/api/cash-management/charge-card-transactions/#query-and-list-charge-card-transactions)
    *   [Query and List Charge Card Transactions (Legacy)](https://developer.intacct.com/api/cash-management/charge-card-transactions/#query-and-list-charge-card-transactions-legacy)
    *   [Get Charge Card Transaction](https://developer.intacct.com/api/cash-management/charge-card-transactions/#get-charge-card-transaction)
    *   [Create Charge Card Transaction (Legacy)](https://developer.intacct.com/api/cash-management/charge-card-transactions/#create-charge-card-transaction-legacy)
    *   [Update Charge Card Transaction (Legacy)](https://developer.intacct.com/api/cash-management/charge-card-transactions/#update-charge-card-transaction-legacy)
    *   [Reverse Charge Card Transaction (Legacy)](https://developer.intacct.com/api/cash-management/charge-card-transactions/#reverse-charge-card-transaction-legacy)
*   [Charge Card Transaction Lines](https://developer.intacct.com/api/cash-management/charge-card-transactions/#charge-card-transaction-lines)
    *   [Get Charge Card Transaction Line Object Definition](https://developer.intacct.com/api/cash-management/charge-card-transactions/#get-charge-card-transaction-line-object-definition)
    *   [Query and List Charge Card Transaction Lines](https://developer.intacct.com/api/cash-management/charge-card-transactions/#query-and-list-charge-card-transaction-lines)
    *   [Query and List Charge Card Transaction Lines (Legacy)](https://developer.intacct.com/api/cash-management/charge-card-transactions/#query-and-list-charge-card-transaction-lines-legacy)
    *   [Get Charge Card Transaction Line](https://developer.intacct.com/api/cash-management/charge-card-transactions/#get-charge-card-transaction-line)

* * *

Transaction record for charges against credit and debit cards.

* * *

### Get Charge Card Transaction Object Definition

#### `lookup`

> List all the fields and relationships for the charge card transaction object:

```
<lookup>
    <object>CCTRANSACTION</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTION` |

* * *

### Query and List Charge Card Transactions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each charge card transaction:

```
<query>
    <object>CCTRANSACTION</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTION` |
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

### Query and List Charge Card Transactions (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CCTRANSACTION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Charge Card Transaction

#### `read`

```
<read>
    <object>CCTRANSACTION</object>
    <keys>31</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTION` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Charge Card Transaction (Legacy)

[History](https://developer.intacct.com/api/cash-management/charge-card-transactions/#history-create-charge-card-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added billable |
| 2020 Release 4 | Added inclusivetax, taxsolutionid, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `record_cctransaction`

> Create a charge card transaction:

```
<record_cctransaction>
    <chargecardid>VISA-1234</chargecardid>
    <paymentdate>
        <year>2017</year>
        <month>01</month>
        <day>02</day>
    </paymentdate>
    <referenceno></referenceno>
    <payee>Costco</payee>
    <description>Supplies</description>
    <supdocid></supdocid>
    <currency>USD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <ccpayitems>
        <ccpayitem>
            <glaccountno>7400</glaccountno>
            <description>Office Supplies</description>
            <paymentamount>154.32</paymentamount>
            <departmentid></departmentid>
            <locationid>110-SJC</locationid>
            <customerid></customerid>
            <vendorid></vendorid>
            <employeeid></employeeid>
            <projectid></projectid>
            <itemid></itemid>
            <classid></classid>
            <contractid></contractid>
            <warehouseid></warehouseid>
        </ccpayitem>
    </ccpayitems>
</record_cctransaction>
```

> Use inclusive tax to have the system calculate the transaction amount (`trx_amount`) for the charge card transaction line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the transaction line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only):

```
<record_cctransaction>
    <chargecardid>A0000002</chargecardid>
    <paymentdate>
        <year>2020</year>
        <month>08</month>
        <day>25</day>
    </paymentdate>
    <payee>Costco9</payee>
    <description>Supplies</description>
    <currency>USD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <inclusivetax>true</inclusivetax>
    <taxsolutionid>Australia - GST</taxsolutionid>
    <ccpayitems>
        <ccpayitem>
            <glaccountno>4000</glaccountno>
            <description>Office Supplies</description>
            <paymentamount></paymentamount>
            <locationid>4</locationid>
            <totaltrxamount>100</totaltrxamount>
            <taxentries>
                <taxentry>
                    <detailid>G10 Capital Acquisition</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
                <taxentry>
                    <detailid>G13 Capital Purchases for Input Tax Sales</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
            </taxentries>
        </ccpayitem>
    </ccpayitems>
</record_cctransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| chargecardid | Required | string | Charge Card ID |
| paymentdate | Required | object | Payment date |
| referenceno | Optional | string | Reference number |
| payee | Optional | string | Payee |
| description | Optional | string | Description of transaction |
| supdocid | Optional | string | Attachments ID |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| customfields | Optional | array of `customfield` | Custom fields on transaction object |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the charge card transaction line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the transaction line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only). (Default: `false`) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. The available tax solution names can be found in the Sage Intacct UI in the Taxes application from the top level of a multi-entity company. (GB, AU, and ZA only) |
| ccpayitems | Required | `ccpayitem[1...n]` | Must have at least one line |

`paymentdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`ccpayitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | Account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | Account label. Required if not using `glaccountno`. |
| description | Optional | string | Description of line |
| paymentamount | Required | currency | Transaction amount. Do not supply if inclusive tax is set to `true`. |
| departmentid | Optional | string | Department ID |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| customfields | Optional | array of `customfield` | Custom fields on line object |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |
| billable | Optional | boolean | Set to `true` to have the transaction billable to the current project. (Default: `false`) |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the charge card line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the transaction amount (`trx_amount`). |

* * *

### Update Charge Card Transaction (Legacy)

[History](https://developer.intacct.com/api/cash-management/charge-card-transactions/#history-update-charge-card-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 2 | Added billable |
| 2020 Release 4 | Added inclusivetax, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

You cannot update a charge card transaction that was created with inclusive tax set to true.

#### `update_cctransaction`

```
<update_cctransaction key="135">
    <paymentdate>
        <year>2017</year>
        <month>01</month>
        <day>02</day>
    </paymentdate>
    <payee>Costco</payee>
    <description>Supplies</description>
    <currency>USD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <updateccpayitems>
        <updateccpayitem line_num="1">
            <glaccountno>7500</glaccountno>
            <description>Copier supplies</description>
            <paymentamount>154.32</paymentamount>
        </updateccpayitem>
    </updateccpayitems>
</update_cctransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | object | Transaction `RECORDNO` to update |
| paymentdate | Optional | object | Payment date |
| referenceno | Optional | string | Reference number |
| payee | Optional | string | Payee |
| description | Optional | string | Description of transaction |
| supdocid | Optional | string | Attachments ID |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| customfields | Optional | array of `customfield` | Custom fields on transaction object |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the charge card transaction line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the transaction line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only). (Default: `false`) |
| updateccpayitems | Optional | `(updateccpayitem | ccpayitem)[0...n]` | To update an existing line use `updateccpayitem`, otherwise to create a new line use `ccpayitem`. You can mix types in the array. |

`paymentdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`updateccpayitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| glaccountno | Optional | string | Account number. Cannot use if using `accountlabel` instead. |
| accountlabel | Optional | string | Account label. Cannot use if using `glaccountno` instead. |
| description | Optional | string | Description of line |
| paymentamount | Optional | currency | Transaction amount. Do not supply if inclusive tax is set to `true`. |
| departmentid | Optional | string | Department ID |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| customfields | Optional | array of `customfield` | Custom fields on line object |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |
| billable | Optional | boolean | Set to `true` to have the transaction billable to the current project. (Default: `false`) |

`ccpayitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | Account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | Account label. Required if not using `glaccountno`. |
| description | Optional | string | Description of line |
| paymentamount | Required | currency | Transaction amount |
| departmentid | Optional | string | Department ID |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| customfields | Optional | array of `customfield` | Custom fields on line object |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |
| billable | Optional | boolean | Set to `true` to have the transaction billable to the current project. (Default: `false`) |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the charge card line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the transaction amount (`trx_amount`). |

* * *

### Reverse Charge Card Transaction (Legacy)

#### `reverse_cctransaction`

```
<reverse_cctransaction key="132">
    <datereversed>
        <year>2017</year>
        <month>01</month>
        <day>31</day>
    </datereversed>
    <memo>Wrong card used</memo>
</reverse_cctransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Transaction `RECORDNO` to reverse |
| datereversed | Required | object | Reverse date |
| memo | Optional | string | Memo |

`datereversed`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Charge Card Transaction Lines
-----------------------------

### Get Charge Card Transaction Line Object Definition

#### `lookup`

> List all the fields and relationships for the charge card transaction line object:

```
<lookup>
    <object>CCTRANSACTIONENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTIONENTRY` |

* * *

### Query and List Charge Card Transaction Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each charge card transaction line:

```
<query>
    <object>CCTRANSACTIONENTRY</object>
    <select>
        <field>DESCRIPTION</field>
        <field>RECORDNO</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTIONENTRY` |
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

### Query and List Charge Card Transaction Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CCTRANSACTIONENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTIONENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Charge Card Transaction Line

#### `read`

```
<read>
    <object>CCTRANSACTIONENTRY</object>
    <keys></keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CCTRANSACTIONENTRY` |
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

