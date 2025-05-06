Title: AR Adjustments

URL Source: https://developer.intacct.com/api/accounts-receivable/ar-adjustments/

Markdown Content:
*   [AR Adjustments](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#ar-adjustments)
    *   [Get AR Adjustment Object Definition](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#get-ar-adjustment-object-definition)
    *   [Query and List AR Adjustments](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#query-and-list-ar-adjustments)
    *   [Query and List AR Adjustments (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#query-and-list-ar-adjustments-legacy)
    *   [Get AR Adjustment](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#get-ar-adjustment)
    *   [Create AR Adjustment (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#create-ar-adjustment-legacy)
    *   [Update AR Adjustment (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#update-ar-adjustment-legacy)
    *   [Delete AR Adjustment](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#delete-ar-adjustment)
    *   [Delete AR Adjustment (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#delete-ar-adjustment-legacy)
*   [AR Adjustment Lines](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#ar-adjustment-lines)
    *   [Get AR Adjustment Line Object Definition](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#get-ar-adjustment-line-object-definition)
    *   [Query and List AR Adjustment Lines](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#query-and-list-ar-adjustment-lines)
    *   [Query and List AR Adjustment Lines (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#query-and-list-ar-adjustment-lines-legacy)
    *   [Get AR Adjustment Line](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#get-ar-adjustment-line)

* * *

An AR adjustment is a transaction that applies a credit or debit in order to modify the amount owed by a customer.

* * *

### Get AR Adjustment Object Definition

#### `lookup`

> List all the fields and relationships for the AR adjustment object:

```
<lookup>
    <object>ARADJUSTMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENT` |

* * *

### Query and List AR Adjustments

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and customer name for each AR adjustment where the customer name is `Acme Supply`:

```
<query>
    <object>ARADJUSTMENT</object>
    <select>
        <field>CUSTOMERNAME</field>
        <field>RECORDNO</field>
    </select>
    <filter>
        <equalto>
            <field>CUSTOMERNAME</field>
            <value>Acme Supply</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENT` |
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

### Query and List AR Adjustments (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ARADJUSTMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AR Adjustment

#### `read`

```
<read>
    <object>ARADJUSTMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENT` |
| keys | Required | string | Comma-separated list of adjustment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create AR Adjustment (Legacy)

[History](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#history-create-ar-adjustment-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added taxsolutionid, totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_aradjustment`

> Create an AR adjustment:

```
<create_aradjustment>
    <customerid>1000</customerid>
    <datecreated>
        <year>2013</year>
        <month>5</month>
        <day>28</day>
    </datecreated>
    <adjustmentno></adjustmentno>
    <invoiceno></invoiceno>
    <description></description>
    <aradjustmentitems>
        <lineitem>
            <glaccountno>4000</glaccountno>
            <amount>1234.56</amount>
            <memo>test line 1</memo>
            <locationid>ARL-VA-US</locationid>
            <departmentid>SAL</departmentid>
            <projectid></projectid>
            <customerid></customerid>
            <vendorid></vendorid>
            <employeeid></employeeid>
            <itemid></itemid>
            <classid></classid>
        </lineitem>
    </aradjustmentitems>
</create_aradjustment>
```

> Use inclusive tax so that the system calculates the transaction amount (`trx_amount`) for the adjustment line and the transaction tax (`trx_tax`) for the tax entry based on the value supplied for `totaltrxamount` on the adjustment line and the tax rate of the tax detail (`detailid`) for the tax entry. (AU, GB, ZA only).

```
<create_aradjustment>
    <customerid>1</customerid>
    <datecreated>
        <year>2020</year>
        <month>8</month>
        <day>18</day>
    </datecreated>
    <adjustmentno>ADJ-104</adjustmentno>
    <basecurr>AUD</basecurr>
    <currency>AUD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <taxsolutionid>Australia - GST</taxsolutionid>
    <aradjustmentitems>
        <lineitem>
            <accountlabel>Sales</accountlabel>
            <amount>110.56</amount>
            <memo>test line 1</memo>
            <locationid>4</locationid>
            <departmentid></departmentid>
            <customerid/>
            <taxentries>
                <taxentry>
                    <detailid>G1 Goods and Services Tax</detailid>
                    <trx_tax></trx_tax>
                </taxentry>
            </taxentries>
        </lineitem>
    </aradjustmentitems>
</create_aradjustment>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customerid | Required | string | Customer ID |
| datecreated | Required | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| batchkey | Optional | integer | Summary record number |
| adjustmentno | Optional | string | Adjustment number |
| action | Optional | string | Action. Use `Draft` or `Submit`. (Default: `Submit`) |
| invoiceno | Optional | string | Invoice number |
| description | Optional | string | Description |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| nogl | Optional | boolean | Do not post to GL. Use `false` for No, `true` for Yes. (Default: `false`) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. See [Tax Solutions](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/) for more information. (GB, AU, and ZA only) |
| aradjustmentitems | Required | `lineitem[1...n]` | Invoice lines, must have at least 1. |

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

`lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount. Use a positive number to create a debit memo or a negative number to create a credit memo. |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
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
| totaltrxamount | Optional | currency | Total transaction amount |
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

### Update AR Adjustment (Legacy)

[History](https://developer.intacct.com/api/accounts-receivable/ar-adjustments/#history-update-ar-adjustment-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added totaltrxamount, taxentries |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `update_aradjustment`

```
<update_aradjustment key="123">
    <customerid>C1234</customerid>
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
    <adjustmentno></adjustmentno>
    <action>Posted</action>
    <invoiceno></invoiceno>
    <description>my adjustment</description>
    <currency>USD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <updatearadjustmentitems>
        <updatelineitem line_num="1">
            <glaccountno>4000</glaccountno>
            <amount>100.25</amount>
            <memo>line 1</memo>
            <locationid>L100</locationid>
            <departmentid>D200</departmentid>
        </updatelineitem>
        <lineitem>
            <glaccountno>4000</glaccountno>
            <amount>20.99</amount>
            <memo>add a new line</memo>
            <locationid>L100</locationid>
            <departmentid>D200</departmentid>
        </lineitem>
    </updatearadjustmentitems>
</update_aradjustment>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Record number of bill to update |
| customerid | Optional | string | Customer ID |
| datecreated | Optional | object | Transaction date |
| dateposted | Optional | object | GL posting date |
| adjustmentno | Optional | string | Adjustment number |
| action | Optional | string | Action. Use `Draft` or `Submit`. (Default: `Submit`) |
| invoiceno | Optional | string | Invoice number |
| description | Optional | string | Description |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| updatearadjustmentitems | Optional | `(updatelineitem | lineitem)[0...n]` | To update an existing line use `updatelineitem` otherwise to create a new line use `lineitem`. You can mix types in the array. |

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
| amount | Required | currency | Transaction amount |
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
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| totaltrxamount | Optional | currency | Total transaction amount |
| taxentries | Optional | `taxentry[1...n]` | Tax entries for the line. Required for VAT enabled transactions. Providing multiple entries is allowed if your tax solution supports it (AU and GB only). For ZA, only one tax entry is allowed. |

`lineitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| offsetglaccountno | Optional | string | Offset GL account number |
| amount | Required | currency | Transaction amount. Use a positive number to create a debit memo or a negative number to create a credit memo. |
| memo | Optional | string | Memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
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
| totaltrxamount | Optional | currency | Total transaction amount |
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

### Delete AR Adjustment

#### `delete`

```
<delete>
    <object>ARADJUSTMENT</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENT` |
| keys | Required | string | Comma-separated list of adjustment `RECORDNO` to delete |

* * *

### Delete AR Adjustment (Legacy)

#### `delete_aradjustment`

```
<delete_aradjustment key="123"></delete_aradjustment>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Record number of adjustment to delete |

* * *

AR Adjustment Lines
-------------------

### Get AR Adjustment Line Object Definition

#### `lookup`

> List all the fields and relationships for the AR adjustment line object:

```
<lookup>
    <object>ARADJUSTMENTITEM</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENTITEM` |

* * *

### Query and List AR Adjustment Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and amount for each AR adjustment line:

```
<query>
    <object>ARADJUSTMENTITEM</object>
    <select>
        <field>RECORDNO</field>
        <field>AMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENTITEM` |
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

### Query and List AR Adjustment Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ARADJUSTMENTITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENTITEM` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AR Adjustment Line

#### `read`

```
<readByQuery>
    <object>ARADJUSTMENTITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADJUSTMENTITEM` |
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

