Title: AP Adjustments

URL Source: https://developer.intacct.com/api/accounts-payable/ap-adjustments/

Markdown Content:
*   [AP Adjustments](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#ap-adjustments)
    *   [Get AP Adjustment Object Definition](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#get-ap-adjustment-object-definition)
    *   [Query and List AP Adjustments](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#query-and-list-ap-adjustments)
    *   [Query and List AP Adjustments (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#query-and-list-ap-adjustments-legacy)
    *   [Get AP Adjustment](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#get-ap-adjustment)
    *   [Create AP Adjustment (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#create-ap-adjustment-legacy)
    *   [Update AP Adjustment (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#update-ap-adjustment-legacy)
    *   [Delete AP Adjustment](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#delete-ap-adjustment)
    *   [Delete AP Adjustment (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#delete-ap-adjustment-legacy)
*   [AP Adjustment Lines](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#ap-adjustment-lines)
    *   [Query and List AP Adjustment Lines](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#query-and-list-ap-adjustment-lines)
    *   [Get AP Adjustment Line](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#get-ap-adjustment-line)

* * *

An AP adjustment is a transaction that applies an AP credit or debit memo in order to modify the amount owed to a vendor.

* * *

### Get AP Adjustment Object Definition

#### `lookup`

> List all the fields and relationships for the AP adjustment object:

```
<lookup>
    <object>APADJUSTMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APADJUSTMENT` |

* * *

### Query and List AP Adjustments

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and vendor ID for each AP adjustment where the vendor ID is `Acme Supply`:

```
<query>
    <object>APADJUSTMENT</object>
    <select>
        <field>VENDORID</field>
        <field>RECORDNO</field>
    </select>
    <filter>
        <equalto>
            <field>VENDORNAME</field>
            <value>Acme Supply</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APADJUSTMENT` |
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

### Query and List AP Adjustments (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APADJUSTMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APADJUSTMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AP Adjustment

#### `read`

```
<read>
    <object>APADJUSTMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APADJUSTMENT` |
| keys | Required | string | Comma-separated list of adjustment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create AP Adjustment (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#history-create-ap-adjustment-legacy)

| Release | Changes |
| --- | --- |
| 2024 Release 3 | Removed totalpaid, totaldue |
| 2021 Release 1 | Added inclusivetax, taxsolutionid, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

> Create an AP adjustment:

```
<create_apadjustment>
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
    <batchkey></batchkey>
    <adjustmentno>234</adjustmentno>
    <action>Submit</action>
    <billno>234235</billno>
    <description>Some description</description>
    <externalid></externalid>
    <basecurr>USD</basecurr>
    <currency>USD</currency>
    <exchratedate>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </exchratedate>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <nogl>false</nogl>
    <customfields>
        <customfield>
            <customfieldname>customfield1</customfieldname>
            <customfieldvalue>customvalue1</customfieldvalue>
        </customfield>
    </customfields>
    <apadjustmentitems>
        <lineitem>
            <glaccountno>6700</glaccountno>
            <offsetglaccountno>2020</offsetglaccountno>
            <amount>76343.43</amount>
            <memo>Just another memo</memo>
            <locationid>Location1</locationid>
            <departmentid>Department1</departmentid>
            <key></key>
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
            <warehouseid>Warehouse1</warehouseid>
        </lineitem>
    </apadjustmentitems>
</create_apadjustment>
```

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_apadjustment`

> Use inclusive tax so that the system calculates the transaction amount (`trx_amount`) for the adjustment line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the adjustment line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only).

```
<create_apadjustment>
    <vendorid>V123-I</vendorid>
    <datecreated>
        <year>2020</year>
        <month>08</month>
        <day>15</day>
    </datecreated>
    <adjustmentno>testadj1</adjustmentno>
    <action>Submit</action>
    <basecurr>AUD</basecurr>
    <currency>AUD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <inclusivetax>true</inclusivetax>
    <taxsolutionid>Australia - GST</taxsolutionid>
    <apadjustmentitems>
        <lineitem>
            <glaccountno>1200</glaccountno>
            <amount>13.45</amount>
            <locationid>4</locationid>
            <totaltrxamount>100</totaltrxamount>
            <taxentries>
                <taxentry>
                    <detailid>G10 Capital Acquisition</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
            </taxentries>
        </lineitem>
        <lineitem>
            <glaccountno>1201</glaccountno>
            <amount>56.90</amount>
            <locationid>4</locationid>
            <totaltrxamount>100</totaltrxamount>
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
    </apadjustmentitems>
</create_apadjustment>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| vendorid | Required | string | Vendor ID |
| datecreated | Required | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| batchkey | Optional | integer | Summary record number |
| adjustmentno | Optional | string | Adjustment number |
| action | Optional | string | Action. Use `Draft` or `Submit`. (Default: `Submit`) |
| billno | Optional | string | Bill number |
| description | Optional | string | Description |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| nogl | Optional | boolean | Do not post to GL. Use `false` for No, `true` for Yes. (Default: `false`) |
| customfields | Optional | array of `customfield` | Custom fields |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the adjustment line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the adjustment line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. See [Tax Solutions](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/) for more information. (GB, AU, and ZA only) |
| apadjustmentitems | Required | `lineitem[1...n]` | Adjustment lines, must have at least 1. |

`datecreated`  
`dateposted`  
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
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount. If supplying multiple lines, amounts must be all positive or all negative, not mixed. |
| allocationid | Optional | string | Allocation ID |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| item1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Vendor must be set up for 1099s. |
| key | Optional | string | Key |
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
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the adjustment line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

### Update AP Adjustment (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/ap-adjustments/#history-update-ap-adjustment-legacy)

| Release | Changes |
| --- | --- |
| 2024 Release 3 | Removed totalpaid, totaldue |
| 2021 Release 1 | Added inclusivetax, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

> Updates an adjustment by adding a new line:

```
<update_apadjustment key="1234">
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
    <adjustmentno>234</adjustmentno>
    <action>Submit</action>
    <billno>234235</billno>
    <description>Some description</description>
    <currency>USD</currency>
    <exchratedate>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </exchratedate>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <updateapadjustmentitems>
        <lineitem>
            <glaccountno>6700</glaccountno>
            <offsetglaccountno>2020</offsetglaccountno>
            <amount>76343.43</amount>
            <memo>Just another memo</memo>
            <locationid>Location1</locationid>
            <departmentid>Department1</departmentid>
            <key></key>
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
            <warehouseid>Warehouse1</warehouseid>
        </lineitem>
    </updateapadjustmentitems>
</update_apadjustment>
```

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `update_apadjustment`

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Transaction `RECORDNO` to update |
| vendorid | Optional | string | Vendor ID |
| datecreated | Required | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| adjustmentno | Optional | string | Adjustment number |
| action | Optional | string | Action. Use `Draft` or `Submit`. |
| billno | Optional | string | Bill number |
| description | Optional | string | Description |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| inclusivetax | Optional | boolean | Inclusive taxes. Set to `true` to have the system calculate the transaction amount (`trx_amount`) for the adjustment line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the adjustment line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only) |
| updateapadjustmentitems | Required | `(updatelineitem | lineitem)[1...n]` | To update an existing line use `updatelineitem` otherwise to create a new line use `lineitem`. You can mix types in the array. |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`dateposted`

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

`updatelineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| glaccountno | Optional | string | GL account number. Cannot use if using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Cannot use if using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Optional | currency | Transaction amount. If supplying multiple lines, amounts must be all positive or all negative, not mixed. |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| item1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Vendor must be set up for 1099s. |
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
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount. If supplying multiple lines, amounts must be all positive or all negative, not mixed. |
| allocationid | Optional | string | Allocation ID |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| item1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Vendor must be set up for 1099s. |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| key | Optional | string | Key |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| totaltrxamount | Optional | currency | Total transaction amount. Required if inclusive tax is set to `true`. |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`taxentry` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the adjustment line.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| detailid | Required | string | Unique ID of a [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) with the tax rate to use |
| trx\_tax | Optional | currency | Transaction tax, which is a manually calculated value to override the calculated value for the tax. The amount of the tax line is automatically included in the read-only transaction amount (`trx_amount`). |

* * *

### Delete AP Adjustment

#### `delete`

```
<delete>
    <object>APADJUSTMENT</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APADJUSTMENT` |
| keys | Required | string | Comma-separated list of adjustment `RECORDNO` to delete |

* * *

### Delete AP Adjustment (Legacy)

#### `delete_apadjustment`

```
<delete_apadjustment key="1234"></delete_apadjustment>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | AP adjustment `RECORDNO` to delete |

* * *

AP Adjustment Lines
-------------------

### Query and List AP Adjustment Lines

#### `readByQuery`

```
<readByQuery>
    <object>APADJUSTMENTITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APADJUSTMENTITEM` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AP Adjustment Line

#### `read`

```
<readByQuery>
    <object>APADJUSTMENTITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APADJUSTMENTITEM` |
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

