Title: Billing Price Lists

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/

Markdown Content:
*   [Billing Price Lists](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#billing-price-lists)
    *   [Get Billing Price List Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-object-definition)
    *   [Query and List Billing Price Lists](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-lists)
    *   [Query and List Billing Price Lists (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-lists-legacy)
    *   [Get Billing Price List](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list)
    *   [Get Billing Price List by ID](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-by-id)
    *   [Create Billing Price List](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#create-billing-price-list)
    *   [Update Billing Price List](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#update-billing-price-list)
    *   [Delete Billing Price List](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#delete-billing-price-list)
*   [Billing Price List Entries](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#billing-price-list-entries)
    *   [Get Billing Price List Entry Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-entry-object-definition)
    *   [Query and List Billing Price List Entries](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-list-entries)
    *   [Query and List Billing Price List Entries (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-list-entries-legacy)
    *   [Get Billing Price List Entry](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-entry)
    *   [Create Billing Price List Entry](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#create-billing-price-list-entry)
    *   [Delete Billing Price List Entry](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#delete-billing-price-list-entry)
*   [Billing Price List Entry Details](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#billing-price-list-entry-details)
    *   [Get Billing Price List Entry Detail Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-entry-detail-object-definition)
    *   [Query and List Billing Price List Entry Details](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-list-entry-details)
    *   [Query and List Billing Price List Entry Details (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-list-entry-details-legacy)
    *   [Get Billing Price List Entry Detail](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-entry-detail)
*   [Billing Price List Entry Detail Tiers](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#billing-price-list-entry-detail-tiers)
    *   [Get Billing Price List Entry Detail Tier Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-entry-detail-tier-object-definition)
    *   [Query and List Billing Price List Entry Detail Tiers](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-list-entry-detail-tiers)
    *   [Query and List Billing Price List Entry Detail Tiers (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#query-and-list-billing-price-list-entry-detail-tiers-legacy)
    *   [Get Billing Price List Entry Detail Tier](https://developer.intacct.com/api/contracts-rev-mgmt/billing-price-lists/#get-billing-price-list-entry-detail-tier)

* * *

Billing price lists are used to create pricing strategies for items whose prices are determined based on a fixed fee, the quantity used, or the contracted quantity.

* * *

### Get Billing Price List Object Definition

#### `lookup`

> List all the fields and relationships for the billing price list object:

```
<lookup>
    <object>CONTRACTPRICELIST</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTPRICELIST` |

* * *

### Query and List Billing Price Lists

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each billing price list:

```
<query>
    <object>CONTRACTPRICELIST</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTPRICELIST` |
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

### Query and List Billing Price Lists (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTPRICELIST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTPRICELIST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active, `F` fo Inactive |

* * *

### Get Billing Price List

#### `read`

```
<read>
    <object>CONTRACTPRICELIST</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTPRICELIST` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Billing Price List by ID

#### `readByName`

```
<readByName>
    <object>CONTRACTPRICELIST</object>
    <keys>Billing Price List</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTPRICELIST` |
| keys | Required | string | Comma-separated list of record `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Billing Price List

#### `create`

```
<create>
    <CONTRACTPRICELIST>
        <NAME>Billing price list</NAME>
    </CONTRACTPRICELIST>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTPRICELIST | Required | object | Object to create |

`CONTRACTPRICELIST`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Billing price list name |
| DESCRIPTION | Optional | string | Description |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |

* * *

### Update Billing Price List

#### `update`

```
<update>
    <CONTRACTPRICELIST>
        <NAME>Billing price list</NAME>
        <DESCRIPTION>hello world</DESCRIPTION>
    </CONTRACTPRICELIST>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTPRICELIST | Required | object | Object to update |

`CONTRACTPRICELIST`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of object. Required if not using `NAME`. |
| NAME | Optional | string | Billing price list name. Required if not using `RECORDNO` |
| DESCRIPTION | Optional | string | Description |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive |

* * *

### Delete Billing Price List

#### `delete`

```
<delete>
    <object>CONTRACTPRICELIST</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTPRICELIST` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to delete |

* * *

Billing Price List Entries
--------------------------

### Get Billing Price List Entry Object Definition

#### `lookup`

> List all the fields and relationships for the billing price list entry object:

```
<lookup>
    <object>CONTRACTITEMPRICELIST</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELIST` |

* * *

### Query and List Billing Price List Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and status for each billing price list entry:

```
<query>
    <object>CONTRACTITEMPRICELIST</object>
    <select>
        <field>RECORDNO</field>
        <field>STATUS</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELIST` |
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

### Query and List Billing Price List Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTITEMPRICELIST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELIST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITMPRCLSTTYP | Optional | string | Price type. Use `R` for `Range` or `T` for `Tiered` |
| ISTIEREDSTEP | Optional | string | Tier pricing. Use `F` for Volume, `S` for Step, or `A` for Absolute |
| QTYRSTPRD | Optional | string | Reset usage quantity. Use `AER` for After each renewal or `AEI` for After each invoice |
| ISQTYRECUR | Optional | boolean | Quantity is recurring. Use `T` for true or `F` for false |
| FLTAMTFREQ | Optional | string | Flat amount frequency. Use `OT` for One-time, `BS` for Use billing template, or `INCLV` for Include with every invoice |
| ROUNDUP | Optional | string | Rounding. Use `S` for Standard, `U` for Round Up, or `D` for Round Down |

* * *

### Get Billing Price List Entry

#### `read`

```
<read>
    <object>CONTRACTITEMPRICELIST</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELIST` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Billing Price List Entry

#### `create`

> Create a range price type:

```
<create>
    <CONTRACTITEMPRICELIST>
        <PRICELISTNAME>Billing price list</PRICELISTNAME>
        <ITEMID>SFTW</ITEMID>
        <ITMPRCLSTTYP>Range</ITMPRCLSTTYP>
        <CURRENCY>USD</CURRENCY>
        <QTYRSTPRD>After each renewal</QTYRSTPRD>
        <FLTAMTFREQ>One-time</FLTAMTFREQ>
        <VARUNITDIVSR>1</VARUNITDIVSR>
        <CONTRACTITEMPRICELISTENTRIES>
            <CONTRACTITEMPRICELISTENTRY>
                <STARTDATE>01/01/2017</STARTDATE>
                <VALUE>2500.00</VALUE>
                <INCLUDEDUNITS>100</INCLUDEDUNITS>
                <VARUNITRATE>0</VARUNITRATE>
            </CONTRACTITEMPRICELISTENTRY>
        </CONTRACTITEMPRICELISTENTRIES>
    </CONTRACTITEMPRICELIST>
</create>
```

> Create a tiered price type:

```
<create>
    <CONTRACTITEMPRICELIST>
        <PRICELISTNAME>Billing price list</PRICELISTNAME>
        <ITEMID>DWNL</ITEMID>
        <ITMPRCLSTTYP>Tiered</ITMPRCLSTTYP>
        <ISTIEREDSTEP>Volume</ISTIEREDSTEP>
        <CURRENCY>USD</CURRENCY>
        <VARUNITDIVSR>1</VARUNITDIVSR>
        <CONTRACTITEMPRICELISTENTRIES>
            <CONTRACTITEMPRICELISTENTRY>
                <STARTDATE>01/01/2017</STARTDATE>
                <VALUE>24.99</VALUE>
                <INCLUDEDUNITS>100</INCLUDEDUNITS>
                <CONTRACTITEMPRCLSTENTYTIERS>
                    <CONTRACTITEMPRCLSTENTYTIER>
                        <BEGINQTY>0</BEGINQTY>
                        <TIERRATE>31.25</TIERRATE>
                    </CONTRACTITEMPRCLSTENTYTIER>
                </CONTRACTITEMPRCLSTENTYTIERS>
            </CONTRACTITEMPRICELISTENTRY>
        </CONTRACTITEMPRICELISTENTRIES>
    </CONTRACTITEMPRICELIST>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTITEMPRICELIST | Required | object | Object to create |

`CONTRACTITEMPRICELIST`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PRICELISTNAME | Required | string | Price list name |
| ITEMID | Required | string | Item ID |
| ITMPRCLSTTYP | Required | string | Price type. Use `Range` or `Tiered` (Default: `Range`) |
| ISTIEREDSTEP | Optional | string | Tier pricing. Use `Volume`, `Step`, or `Absolute` (Default: `Volume`). Only used if Price type is `Tiered` |
| CURRENCY | Optional | string | Currency. Required if company is enabled for multi-currency. |
| QTYRSTPRD | Optional | string | Reset usage quantity. Use `After each renewal` or `After each invoice` (Default: `After each renewal`) |
| ISQTYRECUR | Optional | boolean | Quantity is recurring. Use `true` or `false` (Default: `false`) |
| FLTAMTFREQ | Optional | string | Flat amount frequency. Use `One-time`, `Use billing template`, or `Include with every invoice` |
| VARUNITDIVSR | Required | decimal | Variable unit divisor. For a `Range` price type, this parameter is required. For a `Tiered` price type, a value of 1 is automatically assigned—whether you supply a value or not. |
| ROUNDUP | Optional | string | Rounding. Use either `Standard`, `Round Up`, or `Round Down` (Default: `Standard`) |
| CONTRACTITEMPRICELISTENTRIES | Optional | `CONTRACTITEMPRICELISTENTRY[0...n]` | Billing price list entry details. If supplying multiple entry details, place them in ascending order according to their start dates. |

`CONTRACTITEMPRICELISTENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STARTDATE | Required | string | Start date in format `mm/dd/yyyy`. |
| VALUE | Required | currency | Flat amount |
| INCLUDEDUNITS | Required | number | The item quantity included in VALUE. Enter zero in this field to price the item only by the contracted quantity or quantity used, to set a fixed fee, or to use the item with committed quantity billing. |
| VARUNITRATE | Optional | decimal | Variable unit rate. For a `Range` price type, this parameter is required. For a `Tiered` price type, a value of 0 is automatically assigned—whether you supply a value or not. |
| CONTRACTITEMPRCLSTENTYTIERS | Optional | `CONTRACTITEMPRCLSTENTYTIER[0...n]` | Tiers |

`CONTRACTITEMPRCLSTENTYTIER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BEGINQTY | Required | decimal | Begin quantity. Use 0 for first tier. |
| TIERRATE | Required | currency | Tier rate |

* * *

### Delete Billing Price List Entry

#### `delete`

```
<delete>
    <object>CONTRACTITEMPRICELIST</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELIST` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to delete |

* * *

Billing Price List Entry Details
--------------------------------

### Get Billing Price List Entry Detail Object Definition

#### `lookup`

> List all the fields and relationships for the billing price list entry detail object:

```
<lookup>
    <object>CONTRACTITEMPRICELISTENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELISTENTRY` |

* * *

### Query and List Billing Price List Entry Details

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, start date, and memo for each billing price list entry detail:

```
<query>
    <object>CONTRACTITEMPRICELISTENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>STARTDATE</field>
        <field>MEMO</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELISTENTRY` |
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

### Query and List Billing Price List Entry Details (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTITEMPRICELISTENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELISTENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Billing Price List Entry Detail

#### `read`

```
<read>
    <object>CONTRACTITEMPRICELISTENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRICELISTENTRY` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Billing Price List Entry Detail Tiers
-------------------------------------

### Get Billing Price List Entry Detail Tier Object Definition

#### `lookup`

> List all the fields and relationships for the billing price list entry detail tier object:

```
<lookup>
    <object>CONTRACTITEMPRCLSTENTYTIER</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRCLSTENTYTIER` |

* * *

### Query and List Billing Price List Entry Detail Tiers

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and tier rate for each billing price list entry detail tier:

```
<query>
    <object>CONTRACTITEMPRCLSTENTYTIER</object>
    <select>
        <field>RECORDNO</field>
        <field>TIERRATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRCLSTENTYTIER` |
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

### Query and List Billing Price List Entry Detail Tiers (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTITEMPRCLSTENTYTIER</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRCLSTENTYTIER` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Billing Price List Entry Detail Tier

#### `read`

```
<read>
    <object>CONTRACTITEMPRCLSTENTYTIER</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTITEMPRCLSTENTYTIER` |
| keys | Required | string | Comma-separated list of record `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

