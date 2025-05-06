Title: Recurring Bills

URL Source: https://developer.intacct.com/api/accounts-payable/recurring-bills/

Markdown Content:
*   [Recurring Bills](https://developer.intacct.com/api/accounts-payable/recurring-bills/#recurring-bills)
    *   [Get Recurring Bill Object Definition](https://developer.intacct.com/api/accounts-payable/recurring-bills/#get-recurring-bill-object-definition)
    *   [Query and List Recurring Bills](https://developer.intacct.com/api/accounts-payable/recurring-bills/#query-and-list-recurring-bills)
    *   [Query and List Recurring Bills (Legacy)](https://developer.intacct.com/api/accounts-payable/recurring-bills/#query-and-list-recurring-bills-legacy)
    *   [Get Recurring Bill](https://developer.intacct.com/api/accounts-payable/recurring-bills/#get-recurring-bill)
    *   [Create Recurring Bill (Legacy)](https://developer.intacct.com/api/accounts-payable/recurring-bills/#create-recurring-bill-legacy)
    *   [Delete Recurring Bill (Legacy)](https://developer.intacct.com/api/accounts-payable/recurring-bills/#delete-recurring-bill-legacy)
*   [Recurring Bill Lines](https://developer.intacct.com/api/accounts-payable/recurring-bills/#recurring-bill-lines)
    *   [Get Recurring Bill Line Object Definition](https://developer.intacct.com/api/accounts-payable/recurring-bills/#get-recurring-bill-line-object-definition)
    *   [Query and List Recurring Bill Lines](https://developer.intacct.com/api/accounts-payable/recurring-bills/#query-and-list-recurring-bill-lines)
    *   [Query and List Recurring Bill Lines (Legacy)](https://developer.intacct.com/api/accounts-payable/recurring-bills/#query-and-list-recurring-bill-lines-legacy)
    *   [Get Recurring Bill Line](https://developer.intacct.com/api/accounts-payable/recurring-bills/#get-recurring-bill-line)

* * *

An AP recurring bill provides the ability to schedule and automate the process of creating AP bills. It is commonly used for regularly-recurring, fixed-amount bills.

* * *

### Get Recurring Bill Object Definition

#### `lookup`

> List all the fields and relationships for the recurring bill object:

```
<lookup>
    <object>APRECURBILL</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILL` |

* * *

### Query and List Recurring Bills

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and vendor name for each recurring bill where the vendor name starts with the letter `B`:

```
<query>
    <object>APRECURBILL</object>
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

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILL` |
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

### Query and List Recurring Bills (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APRECURBILL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Recurring Bill

#### `read`

```
<read>
    <object>APRECURBILL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILL` |
| keys | Required | string | Comma-separated list of recurring bill `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Recurring Bill (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/recurring-bills/#history-create-recurring-bill-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_recurringbill`

```
<create_recurringbill>
    <vendorid>V1234</vendorid>
    <datecreated>
        <year>2017</year>
        <month>04</month>
        <day>10</day>
    </datecreated>
    <recordid>Recurring Rent</recordid>
    <docnumber>5678</docnumber>
    <description>Monthly rent</description>
    <termname>Net 10</termname>
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
    <recurbillitems>
        <recurlineitem>
            <glaccountno>6500</glaccountno>
            <amount>1000.00</amount>
            <locationid>LAX-US</locationid>
            <departmentid>ADM</departmentid>
        </recurlineitem>
    </recurbillitems>
</create_recurringbill>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| vendorid | Required | string | Vendor ID |
| datecreated | Required | object | Transaction date. Make this match Start date. |
| recordid | Optional | string | Bill sequence number |
| docnumber | Optional | string | Reference number |
| description | Optional | string | Description |
| contractid | Optional | string | Contract ID |
| contractdesc | Optional | string | Contract description |
| termname | Required | string | Payment term |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| status | Optional | string | Status. Use `active` or `inactive`. (Default: `active`) |
| supdocid | Optional | string | Attachments ID |
| paytocontactname | Optional | string | Pay to contact name |
| returntocontactname | Optional | string | Return to contact name |
| startdate | Required | object | Start date |
| ending | Optional | object | Ending on. Leave element out to Never end. |
| modenew | Optional | string | Repeat mode. Use `None`, `Days`, `Weeks`, `Months`, or `Years`. (Default: `None`) |
| interval | Optional | integer | Repeat interval. Required when Repeat mode is not set to `None`. |
| eom | Optional | boolean | End of month. Only used when Repeat mode is set to `Months`. Use either `true` or `false`. (Default: `false`) |
| recurbillitems | Required | `recurlineitem[1...n]` | Bill lines, must have at least 1. |

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
| form1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Vendor must be set up for 1099s. |
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
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. (Default: `false`) |
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Recurring Bill (Legacy)

#### `delete_bill`

```
<delete_recurringbill key="1234"></delete_recurringbill>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Recurring bill `RECORDNO` to delete |

* * *

Recurring Bill Lines
--------------------

### Get Recurring Bill Line Object Definition

#### `lookup`

> List all the fields and relationships for the recurring bill line object:

```
<lookup>
    <object>APRECURBILLENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILLENTRY` |

* * *

### Query and List Recurring Bill Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and amount for each recurring bill line:

```
<query>
    <object>APRECURBILLENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>AMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILLENTRY` |
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

### Query and List Recurring Bill Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APRECURBILLENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILLENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Recurring Bill Line

#### `read`

```
<read>
    <object>APRECURBILLENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRECURBILLENTRY` |
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

