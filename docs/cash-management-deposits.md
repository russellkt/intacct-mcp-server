Title: Deposits

URL Source: https://developer.intacct.com/api/cash-management/deposits/

Markdown Content:
*   [Deposits](https://developer.intacct.com/api/cash-management/deposits/#deposits)
    *   [Get Deposit Object Definition](https://developer.intacct.com/api/cash-management/deposits/#get-deposit-object-definition)
    *   [Query and List Deposits](https://developer.intacct.com/api/cash-management/deposits/#query-and-list-deposits)
    *   [Query and List Deposits (Legacy)](https://developer.intacct.com/api/cash-management/deposits/#query-and-list-deposits-legacy)
    *   [Get Deposit](https://developer.intacct.com/api/cash-management/deposits/#get-deposit)
    *   [Create Deposit (Legacy)](https://developer.intacct.com/api/cash-management/deposits/#create-deposit-legacy)
*   [Deposit Lines](https://developer.intacct.com/api/cash-management/deposits/#deposit-lines)
    *   [Get Deposit Line Object Definition](https://developer.intacct.com/api/cash-management/deposits/#get-deposit-line-object-definition)
    *   [Query and List Deposit Lines](https://developer.intacct.com/api/cash-management/deposits/#query-and-list-deposit-lines)
    *   [Query and List Deposit Lines (Legacy)](https://developer.intacct.com/api/cash-management/deposits/#query-and-list-deposit-lines-legacy)
    *   [Get Deposit Line](https://developer.intacct.com/api/cash-management/deposits/#get-deposit-line)

* * *

Transaction record for a deposit.

* * *

### Get Deposit Object Definition

#### `lookup`

> List all the fields and relationships for the deposit object:

```
<lookup>
    <object>DEPOSIT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSIT` |

* * *

### Query and List Deposits

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, financial entity, and total entered for each deposit:

```
<query>
    <object>DEPOSIT</object>
    <select>
        <field>RECORDNO</field>
        <field>FINANCIALENTITY</field>
        <field>TOTALENTERED</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSIT` |
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

### Query and List Deposits (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>DEPOSIT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSIT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Deposit

#### `read`

```
<read>
    <object>DEPOSIT</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSIT` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Deposit (Legacy)

#### `record_deposit`

```
<record_deposit>
    <bankaccountid>BA1145</bankaccountid>
    <depositdate>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </depositdate>
    <depositid>Deposit Slip 2015-06-30</depositid>
    <receiptkeys>
        <receiptkey>1234</receiptkey>
    </receiptkeys>
    <description>Desc</description>
    <supdocid>AT111</supdocid>
    <customfields>
        <customfield>
            <customfieldname>customfield1</customfieldname>
            <customfieldvalue>customvalue1</customfieldvalue>
        </customfield>
    </customfields>
</record_deposit>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bankaccountid | Required | string | Bank account ID |
| depositdate | Required | object | Deposit date |
| depositid | Required | string | Deposit slip ID |
| receiptkeys | Required | `receiptkey[1...n]` | Record numbers of undeposited AR payments/other receipts you want to deposit |
| description | Optional | string | Description |
| supdocid | Optional | string | Attachments ID |
| customfields | Optional | array of `customfield` | Custom fields |

`depositdate`

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

* * *

Deposit Lines
-------------

### Get Deposit Line Object Definition

#### `lookup`

> List all the fields and relationships for the deposit line object:

```
<lookup>
    <object>DEPOSITENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSITENTRY` |

* * *

### Query and List Deposit Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, account number, and amount for each deposit line:

```
<query>
    <object>DEPOSITENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCOUNTNO</field>
        <field>AMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSITENTRY` |
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

### Query and List Deposit Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>DEPOSITENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSITENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Deposit Line

#### `read`

```
<read>
    <object>DEPOSITENTRY</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DEPOSITENTRY` |
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

