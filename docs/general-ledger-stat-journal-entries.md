Title: Statistical Journal Entries

URL Source: https://developer.intacct.com/api/general-ledger/stat-journal-entries/

Markdown Content:
*   [Statistical Journal Entries](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#statistical-journal-entries)
    *   [Get Statistical Journal Entry Object Definition](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#get-statistical-journal-entry-object-definition)
    *   [Query and List Statistical Journal Entries](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#query-and-list-statistical-journal-entries)
    *   [Query and List Statistical Journal Entries (Legacy)](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#query-and-list-statistical-journal-entries-legacy)
    *   [Get Statistical Journal Entry](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#get-statistical-journal-entry)
    *   [Create Statistical Journal Entry](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#create-statistical-journal-entry)
    *   [Create Statistical Journal Entry (Legacy)](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#create-statistical-journal-entry-legacy)
    *   [Update Statistical Journal Entry](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#update-statistical-journal-entry)
    *   [Delete Statistical Journal Entry](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#delete-statistical-journal-entry)
*   [Statistical Journal Entry Lines](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#statistical-journal-entry-lines)
    *   [Get Statistical Journal Entry Line Object Definition](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#get-statistical-journal-entry-line-object-definition)
    *   [Query and List Statistical Journal Entry Lines](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#query-and-list-statistical-journal-entry-lines)
    *   [Query and List Statistical Journal Entry Lines (Legacy)](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#query-and-list-statistical-journal-entry-lines-legacy)
    *   [Get Statistical Journal Entry Line](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#get-statistical-journal-entry-line)

* * *

Statistical journals hold all non-financial transactions.

* * *

### Get Statistical Journal Entry Object Definition

#### `lookup`

> List all the fields and relationships for the statistical journal entry object:

```
<lookup>
    <object>GLBATCH</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBATCH` |

* * *

### Query and List Statistical Journal Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, batch number, and description for each statistical journal with the given symbol (SHC):

```
<query>
    <object>GLBATCH</object>
    <select>
        <field>RECORDNO</field>
        <field>BATCHNO</field>
        <field>BATCH_TITLE</field>
    </select>
    <filter>
        <equalto>
            <field>JOURNAL</field>
            <value>SHC</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBATCH` |
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

### Query and List Statistical Journal Entries (Legacy)

#### `readByQuery`

> List entries for the statistical journal with the given symbol (SHC):

```
<readByQuery>
    <object>GLBATCH</object>
    <fields>*</fields>
    <query>JOURNAL = 'SHC'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBATCH` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | State of the stat journal entry. Use `I` for Draft, `S` for Submitted, `X` for Partially Approved, `A` for Approved, `P` for Posted, `R` for Declined, `L` for Reversal Pending, or `Z` for Reversed. |

* * *

### Get Statistical Journal Entry

#### `read`

```
<read>
    <object>GLBATCH</object>
    <keys>31</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBATCH` |
| keys | Required | string | Comma-separated list of stat journal entry `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Statistical Journal Entry

[History](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#history-create-statistical-journal-entry)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added COSTTYPEID |
| 2019 Release 4 | Added TASKID |

#### `create`

```
<create>
    <GLBATCH>
        <JOURNAL>SHC</JOURNAL>
        <BATCH_DATE>03/31/2016</BATCH_DATE>
        <BATCH_TITLE>Headcount 03/31/2016</BATCH_TITLE>
        <ENTRIES>
            <GLENTRY>
                <ACCOUNTNO>HEADS</ACCOUNTNO>
                <DEPARTMENT>ADMIN</DEPARTMENT>
                <LOCATION>100</LOCATION>
                <TR_TYPE>1</TR_TYPE>
                <AMOUNT>2.00</AMOUNT>
                <DESCRIPTION>Headcount 03/31/2016</DESCRIPTION>
            </GLENTRY>
        </ENTRIES>
    </GLBATCH>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLBATCH | Required | object | Object to create |

`GLBATCH`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| JOURNAL | Required | string | Stat journal symbol |
| BATCH\_DATE | Required | string | Posting date in format `mm/dd/yyyy` |
| REVERSEDATE | Optional | string | Reverse date in format `mm/dd/yyyy`. Must be greater than `BATCH_DATE`. |
| BATCH\_TITLE | Required | string | Description of entry |
| HISTORY\_COMMENT | Optional | string | Comment added to history for this transaction |
| REFERENCENO | Optional | string | Reference number of transaction |
| SUPDOCID | Optional | string | Attachments ID |
| STATE | Optional | string | State to create the entry in. `Posted` to post to the GL, otherwise `Draft`. (Default: `Posted`) |
| ENTRIES | Required | `GLENTRY[1...n]` | Must have at least one line. Stat journal entries do not need to balance like regular journal entries. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`GLENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCUMENT | Optional | string | Document number of entry |
| ACCOUNTNO | Required | string | Account number |
| TRX\_AMOUNT | Required | currency | Amount. Absolute value, relates to `TR_TYPE`. |
| TR\_TYPE | Required | string | Transaction type. `1` for Increase, otherwise `-1` for Decrease. |
| DESCRIPTION | Optional | string | Memo. If left blank, set this value to match `BATCH_TITLE`. |
| ALLOCATION | Optional | string | Allocation ID. All other dimension elements are ignored if allocation is set. Use `Custom` for custom splits and see `SPLIT` element below. |
| DEPARTMENT | Optional | string | Department ID |
| LOCATION | Optional | string | Location ID. Required if multi-entity enabled. |
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
| SPLIT | Optional | `SPLIT`\[\] | Custom allocation split. Required if `ALLOCATION` equals `Custom`. Multiple `SPLIT` elements may then be passed. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`SPLIT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| AMOUNT | Required | currency | Split transaction amount. The sum of the `AMOUNT` values for all the `SPLIT` elements must equal the `TRX_AMOUNT` value for the `GLENTRY` element. |
| DEPARTMENTID | Optional | string | Department ID |
| Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |   |
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

* * *

### Create Statistical Journal Entry (Legacy)

[History](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#history-create-statistical-journal-entry-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `create_statgltransaction`

```
<create_statgltransaction>
    <journalid>SHC</journalid>
    <datecreated>
        <year>2016</year>
        <month>03</month>
        <day>31</day>
    </datecreated>
    <description>Headcount 03/31/2016</description>
    <statgltransactionentries>
        <glentry>
            <trtype>1</trtype>
            <amount>2.00</amount>
            <glaccountno>HEADS</glaccountno>
            <memo>Headcount 03/31/2016</memo>
            <locationid>100</locationid>
            <departmentid>ADMIN</departmentid>
        </glentry>
    </statgltransactionentries>
</create_statgltransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| journalid | Required | string | Stat journal symbol |
| datecreated | Required | object | Posting date |
| reversedate | Optional | object | Reverse date. Must be greater than posting date. |
| description | Required | string | Description of entry |
| statgltransactionentries | Required | `GLENTRY[1...n]` | Must have at least one line. Stat journal entries do not need to balance like regular journal entries. |

`datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`reversedate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`glentry`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| trtype | Required | string | Transaction type. `1` for Increase, otherwise `-1` for Decrease. |
| amount | Required | currency | Amount. Absolute value, relates to `trtype`. |
| glaccountno | Required | string | Account number |
| document | Optional | string | Document number of entry |
| memo | Optional | string | Memo. If left blank, set this value to match journal entry description. |
| Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |   |
| departmentid | Optional | string | Department ID |
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
| customfields | Optional | array of `customfield` | Custom fields |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Statistical Journal Entry

[History](https://developer.intacct.com/api/general-ledger/stat-journal-entries/#history-update-statistical-journal-entry)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added COSTTYPEID |
| 2019 Release 4 | Added TASKID |

#### `update`

```
<update>
    <GLBATCH>
        <RECORDNO>21</RECORDNO>
        <BATCH_DATE>03/31/2016</BATCH_DATE>
        <BATCH_TITLE>Headcount 03/31/2016</BATCH_TITLE>
        <ENTRIES>
            <GLENTRY>
                <ACCOUNTNO>HEADS</ACCOUNTNO>
                <DEPARTMENT>ADMIN</DEPARTMENT>
                <LOCATION>100</LOCATION>
                <TR_TYPE>1</TR_TYPE>
                <AMOUNT>2.00</AMOUNT>
                <DESCRIPTION>Headcount 03/31/2016</DESCRIPTION>
            </GLENTRY>
        </ENTRIES>
    </GLBATCH>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLBATCH | Required | object | Object to update |

`GLBATCH`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Stat journal entry `RECORDNO` to update |
| BATCH\_DATE | Required | string | Posting date in format `mm/dd/yyyy` |
| BATCH\_TITLE | Required | string | Description of entry |
| HISTORY\_COMMENT | Optional | string | Comment added to history for this transaction |
| REFERENCENO | Optional | string | Reference number of transaction |
| SUPDOCID | Optional | string | Attachments ID |
| STATE | Optional | string | State to update the entry to. `Posted` to post to the GL, otherwise `Draft`. |
| ENTRIES | Required | `GLENTRY[1...n]` | Must have at least one line. Stat journal entries do not need to balance like regular journal entries. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`GLENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCUMENT | Optional | string | Document number of entry |
| ACCOUNTNO | Required | string | Account number |
| TRX\_AMOUNT | Required | currency | Amount. Absolute value, relates to `TR_TYPE`. |
| TR\_TYPE | Required | string | Transaction type. `1` for Increase, otherwise `-1` for Decrease. |
| DESCRIPTION | Optional | string | Memo. If left blank, set this value to match `BATCH_TITLE`. |
| ALLOCATION | Optional | string | Allocation ID. All other dimension elements are ignored if allocation is set. Use `Custom` for custom splits and see `SPLIT` element below. |
| DEPARTMENT | Optional | string | Department ID |
| LOCATION | Optional | string | Location ID. Required if multi-entity enabled. |
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
| SPLIT | Optional | `SPLIT`\[\] | Custom allocation split. Required if `ALLOCATION` equals `Custom`. Multiple `SPLIT` elements may then be passed. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`SPLIT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| AMOUNT | Required | currency | Split transaction amount. Absolute value. The sum of the `AMOUNT` values for all the `SPLIT` elements must equal the `TRX_AMOUNT` value for the `GLENTRY` element. |
| DEPARTMENTID | Optional | string | Department ID |
| Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |   |
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

* * *

### Delete Statistical Journal Entry

#### `delete`

```
<delete>
    <object>GLBATCH</object>
    <keys>1</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBATCH` |
| keys | Required | string | Comma-separated list of stat journal entry `RECORDNO` to delete |

* * *

Statistical Journal Entry Lines
-------------------------------

### Get Statistical Journal Entry Line Object Definition

#### `lookup`

> List all the fields and relationships for the statistical journal entry line object:

```
<lookup>
    <object>GLENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLENTRY` |

* * *

### Query and List Statistical Journal Entry Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> Lists information for journal entry lines for the statistical journal whose record number is 1819:

```
<query>
    <object>GLENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>BATCHNO</field>
        <field>AMOUNT</field>
    </select>
    <filter>
        <equalto>
            <field>BATCHNO</field>
            <value>1819</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLENTRY` |
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

### Query and List Statistical Journal Entry Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>GLENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Statistical Journal Entry Line

#### `read`

```
<read>
    <object>GLENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLENTRY` |
| keys | Required | string | Comma-separated list of stat journal entry line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

