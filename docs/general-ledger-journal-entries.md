Title: Journal Entries

URL Source: https://developer.intacct.com/api/general-ledger/journal-entries/

Markdown Content:
*   [Journal Entries](https://developer.intacct.com/api/general-ledger/journal-entries/#journal-entries)
    *   [Get Journal Entry Object Definition](https://developer.intacct.com/api/general-ledger/journal-entries/#get-journal-entry-object-definition)
    *   [Query and List Journal Entries](https://developer.intacct.com/api/general-ledger/journal-entries/#query-and-list-journal-entries)
    *   [Query and List Journal Entries (Legacy)](https://developer.intacct.com/api/general-ledger/journal-entries/#query-and-list-journal-entries-legacy)
    *   [Get Journal Entry](https://developer.intacct.com/api/general-ledger/journal-entries/#get-journal-entry)
    *   [Create Journal Entry](https://developer.intacct.com/api/general-ledger/journal-entries/#create-journal-entry)
    *   [Create Journal Entry (Legacy)](https://developer.intacct.com/api/general-ledger/journal-entries/#create-journal-entry-legacy)
    *   [Update Journal Entry](https://developer.intacct.com/api/general-ledger/journal-entries/#update-journal-entry)
    *   [Delete Journal Entry](https://developer.intacct.com/api/general-ledger/journal-entries/#delete-journal-entry)
    *   [Delete Journal Entry (Legacy)](https://developer.intacct.com/api/general-ledger/journal-entries/#delete-journal-entry-legacy)
*   [Journal Entry Lines](https://developer.intacct.com/api/general-ledger/journal-entries/#journal-entry-lines)
    *   [Get Journal Entry Line Object Definition](https://developer.intacct.com/api/general-ledger/journal-entries/#get-journal-entry-line-object-definition)
    *   [Query and List Journal Entry Lines](https://developer.intacct.com/api/general-ledger/journal-entries/#query-and-list-journal-entry-lines)
    *   [Query and List Journal Entry Lines (Legacy)](https://developer.intacct.com/api/general-ledger/journal-entries/#query-and-list-journal-entry-lines-legacy)
    *   [Get Journal Entry Line](https://developer.intacct.com/api/general-ledger/journal-entries/#get-journal-entry-line)

* * *

A journal entry can add, edit, or reverse a transaction to a journal.

When writing journal entries, be sure to balance the general ledger by posting offsetting entries. A journal entry is an owned element of general ledger transaction (`GLBATCH`).

**Note:** If GL Outlier Detection is enabled for a company, information about outliers is included in journal entries and allocation splits when you get a journal entry object. See the [FAQ](https://developer.intacct.com/support/faq/#gl-outlier-detection) for more information.

**Potential Timeouts with Large Journal Entries** If you create journal entries with thousands of lines, you might experience timeouts. As a best practice, create multiple, smaller journal entries. If you cannot create multiple journal entries, work with our support team to set up an asynchronous transport policy. [Read more about asynchronous processing in this topic](https://developer.intacct.com/web-services/sync-vs-async/#setting-up-asynchronous-processing).

* * *

### Get Journal Entry Object Definition

#### `lookup`

> List all the fields and relationships for the journal entry object:

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

### Query and List Journal Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, description, and date for each journal entry:

```
<query>
    <object>GLBATCH</object>
    <select>
        <field>RECORDNO</field>
        <field>BATCH_TITLE</field>
        <field>BATCH_DATE</field>
    </select>
</query>
```

> List submitted journal entries for the general journal (GJ):

```
<query>
    <object>GLBATCH</object>
    <select>
        <field>RECORDNO</field>
        <field>BATCH_TITLE</field>
        <field>BATCH_DATE</field>
        <field>JOURNAL</field>
        <field>STATE</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>JOURNAL</field>
                <value>GJ</value>
            </equalto>
            <equalto>
                <field>STATE</field>
                <value>Submitted</value>
            </equalto>
        </and>
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

### Query and List Journal Entries (Legacy)

> List journal entries:

#### `readByQuery`

```
<readByQuery>
    <object>GLBATCH</object>
    <fields>*</fields>
    <query>JOURNAL = 'GJ'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

> The above function returns data structured like this:

```
<glbatch>
    <RECORDNO>6679</RECORDNO>
    <BATCHNO>249</BATCHNO>
    <BATCH_TITLE>Paying some folks</BATCH_TITLE>
    <BALANCE></BALANCE>
    <JOURNAL>GJ</JOURNAL>
    <JOURNALKEY>5</JOURNALKEY>
    <JOURNAL_BILLABLE></JOURNAL_BILLABLE>
    <ADJ>F</ADJ>
    <BATCH_DATE>01/09/2019</BATCH_DATE>
    <MODULE>2.GL</MODULE>
    <CHILDENTITY></CHILDENTITY>
    <USERKEY>20</USERKEY>
    <REFERENCENO></REFERENCENO>
    <REVERSED></REVERSED>
    <REVERSEDKEY></REVERSEDKEY>
    <REVERSEDFROM></REVERSEDFROM>
    <TEMPLATEKEY></TEMPLATEKEY>
    <PRBATCHKEY></PRBATCHKEY>
    <PRBATCHRECTYPE></PRBATCHRECTYPE>
    <MODIFIED>01/09/2019 22:01:29</MODIFIED>
    <MODIFIEDBYID>jsmith</MODIFIEDBYID>
    <SCHOPKEY></SCHOPKEY>
    <RRSENTRYKEY></RRSENTRYKEY>
    <RRSKEY></RRSKEY>
    <CONTRACTSCHEDULEENTRYKEY></CONTRACTSCHEDULEENTRYKEY>
    <CONTRACTSCHEDULEKEY></CONTRACTSCHEDULEKEY>
    <GLACCTALLOCATIONRUNKEY></GLACCTALLOCATIONRUNKEY>
    <BASELOCATION>1</BASELOCATION>
    <BASELOCATION_NO>100</BASELOCATION_NO>
    <BASELOCATION_NAME>ACME USA</BASELOCATION_NAME>
    <USERINFO.LOGINID>jsmith</USERINFO.LOGINID>
    <LOCATIONKEY></LOCATIONKEY>
    <WHENCREATED>01/09/2019 22:01:29</WHENCREATED>
    <WHENMODIFIED>01/09/2019 22:01:29</WHENMODIFIED>
    <CREATEDBY>20</CREATEDBY>
    <MODIFIEDBY>20</MODIFIEDBY>
    <STATE>Submitted</STATE>
    ...
</glbatch>
...
```

> List submitted journal entries:

```
<readByQuery>
    <object>GLBATCH</object>
    <fields>*</fields>
    <query>JOURNAL = 'GJ' AND STATE = 'S'</query>
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
| STATE | Optional | string | State of the journal entry.
*   `I` - Draft
*   `S` - Submitted
*   `X` - Partially Approved
*   `A` - Approved
*   `P` - Posted
*   `R` - Declined
*   `L` - Reversal Pending
*   `Z` - Reversed

 |

* * *

### Get Journal Entry

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
| keys | Required | string | Comma-separated list of journal entry `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Journal Entry

[History](https://developer.intacct.com/api/general-ledger/journal-entries/#history-create-journal-entry)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added TRANSACTIONSOURCE |
| 2021 Release 2 | Added TAXSOLUTIONID |
| 2020 Release 2 | Added COSTTYPEID |
| 2019 Release 4 | Added TASKID |
| 2019 Release 3 | Added TAXIMPLICATIONS, VATVENDORID, VATCUSTOMERID, VATCONTACTID, TAXENTRIES |

#### `create`

> Create a journal entry with a reversal:

```
<create>
    <GLBATCH>
        <JOURNAL>PYRJ</JOURNAL>
        <BATCH_DATE>03/31/2016</BATCH_DATE>
        <REVERSEDATE>04/01/2016</REVERSEDATE>
        <BATCH_TITLE>Payroll accrual 03/31/2016</BATCH_TITLE>
        <ENTRIES>
            <GLENTRY>
                <ACCOUNTNO>2080</ACCOUNTNO>
                <DEPARTMENT>ADMIN</DEPARTMENT>
                <LOCATION>100</LOCATION>
                <CURRENCY>USD</CURRENCY>
                <TR_TYPE>-1</TR_TYPE>
                <AMOUNT>1450.80</AMOUNT>
                <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                <DESCRIPTION>Accrued salaries</DESCRIPTION>
            </GLENTRY>
            <GLENTRY>
                <ACCOUNTNO>6500</ACCOUNTNO>
                <DEPARTMENT>ADMIN</DEPARTMENT>
                <LOCATION>100</LOCATION>
                <CURRENCY>USD</CURRENCY>
                <TR_TYPE>1</TR_TYPE>
                <AMOUNT>1450.80</AMOUNT>
                <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                <DESCRIPTION>Salary expense</DESCRIPTION>
            </GLENTRY>
        </ENTRIES>
    </GLBATCH>
</create>
```

> Create a journal entry with a custom allocation:

```
<create>
    <GLBATCH>
        <JOURNAL>PYRJ</JOURNAL>
        <BATCH_DATE>03/31/2016</BATCH_DATE>
        <REVERSEDATE>04/01/2016</REVERSEDATE>
        <BATCH_TITLE>Payroll accrual 03/31/2016</BATCH_TITLE>
        <ENTRIES>
            <GLENTRY>
                <ACCOUNTNO>2080</ACCOUNTNO>
                <DEPARTMENT>ADMIN</DEPARTMENT>
                <LOCATION>100</LOCATION>
                <CURRENCY>USD</CURRENCY>
                <TR_TYPE>-1</TR_TYPE>
                <AMOUNT>1450.80</AMOUNT>
                <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                <DESCRIPTION>Accrued salaries</DESCRIPTION>
            </GLENTRY>
            <GLENTRY>
                <ACCOUNTNO>6500</ACCOUNTNO>
                <CURRENCY>USD</CURRENCY>
                <TR_TYPE>1</TR_TYPE>
                <AMOUNT>1450.80</AMOUNT>
                <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                <DESCRIPTION>Salary expense</DESCRIPTION>
                <ALLOCATION>Custom</ALLOCATION>
                <SPLIT>
                    <AMOUNT>450.80</AMOUNT>
                    <LOCATIONID>100</LOCATIONID>
                    <DEPARTMENTID>ADMIN</DEPARTMENTID>
                </SPLIT>
                <SPLIT>
                    <AMOUNT>700.00</AMOUNT>
                    <LOCATIONID>100</LOCATIONID>
                    <DEPARTMENTID>SUPPORT</DEPARTMENTID>
                </SPLIT>
                <SPLIT>
                    <AMOUNT>300.00</AMOUNT>
                    <LOCATIONID>100</LOCATIONID>
                    <DEPARTMENTID>SALES</DEPARTMENTID>
                </SPLIT>
            </GLENTRY>
        </ENTRIES>
    </GLBATCH>
</create>
```

> Create a journal entry with a tax entry (AU, GB, ZA only):

```
<create>
    <GLBATCH>
        <JOURNAL>APJ</JOURNAL>
        <BATCH_DATE>06/12/2019</BATCH_DATE>
        <BATCH_TITLE>Manual journal for AP</BATCH_TITLE>
        <TAXIMPLICATIONS>Inbound</TAXIMPLICATIONS>
        <VATVENDORID>AUS_VEND_1</VATVENDORID>
        <ENTRIES>
            <GLENTRY>
                <ACCOUNTNO>1220</ACCOUNTNO>
                <DEPARTMENT></DEPARTMENT>
                <LOCATION>7</LOCATION>
                <CURRENCY>AUD</CURRENCY>
                <TR_TYPE>1</TR_TYPE>
                <AMOUNT>5000.00</AMOUNT>
                <TAXENTRIES>
                    <TAXENTRY>
                        <TRX_TAX>500</TRX_TAX>
                        <DETAILID>Capital Purchases for Input Tax Sales</DETAILID>
                    </TAXENTRY>
                </TAXENTRIES>
            </GLENTRY>
            <GLENTRY>
                <ACCOUNTNO>2000</ACCOUNTNO>
                <DEPARTMENT></DEPARTMENT>
                <LOCATION>7</LOCATION>
                <CURRENCY>AUD</CURRENCY>
                <TR_TYPE>-1</TR_TYPE>
                <AMOUNT>5500</AMOUNT>
                <DESCRIPTION>Offset</DESCRIPTION>
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
| JOURNAL | Required | string | GL journal symbol. This determines the type of journal entry as visible in the UI, for example, Regular, Adjustment, User-defined, Statistical, GAAP, Tax, and so forth. |
| BATCH\_DATE | Required | string | Posting date in format `mm/dd/yyyy`. |
| REVERSEDATE | Optional | string | Reverse date in format `mm/dd/yyyy`. Must be greater than `BATCH_DATE`. |
| BATCH\_TITLE | Required | string | Description of entry |
| TAXIMPLICATIONS | Optional | string | Tax implications. Use `None`, `Inbound` for purchase tax, or `Outbound` for sales tax. (Default: `None`) (AU, GB, ZA only) |
| VATVENDORID | Optional | string | Vendor ID when tax implications is set to `Inbound` for tax on purchases (AU, GB, ZA only) |
| VATCUSTOMERID | Optional | string | Customer ID when tax implications is set to `Outbound` for tax on sales (AU, GB, ZA only) |
| VATCONTACTID | Optional | string | Contact name for the customer `SHIPTO` contact for sales journals or the vendor ID for the vendor `PAYTO` contact for purchase journals (AU, GB, ZA only) |
| HISTORY\_COMMENT | Optional | string | Comment added to history for this transaction |
| REFERENCENO | Optional | string | Reference number of transaction |
| BASELOCATION\_NO | Optional | string | Source entity ID. Required if multi-entity enabled and entries do not balance by entity. |
| SUPDOCID | Optional | string | Attachments ID |
| STATE | Optional | string | State to create the entry in. `Posted` to post to the GL, otherwise `Draft`. (Default: `Posted`) |
| TAXSOLUTIONID | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. See [Tax Solutions](https://developer.intacct.com/api/sales-tax-vat-gst/tax-solutions/) for more information. (GB, AU, and ZA only) |
| TRANSACTIONSOURCE | Optional | string | The source of the entry. Will be set to `BANK` if the entry is created from a bank transaction. (Default: Null) |
| ENTRIES | Required | `GLENTRY[2...n]` | Must have at least two lines (one debit, one credit). |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`GLENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCUMENT | Optional | string | Document number of entry |
| ACCOUNTNO | Required | string | Account number |
| CURRENCY | Optional | string | Transaction currency code. Required if multi-currency enabled. |
| TRX\_AMOUNT | Required | currency | Transaction amount. Absolute value, relates to `TR_TYPE`. |
| TR\_TYPE | Required | string | Transaction type. `1` for Debit, otherwise `-1` for Credit. |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy`. If null, defaults to `BATCH_DATE`. |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Required if multi-currency enabled and `EXCHANGE_RATE` left blank. (Default `custom`) |
| EXCHANGE\_RATE | Optional | currency | Exchange rate. Required if multi currency enabled and `EXCH_RATE_TYPE_ID` left blank. Exchange rate amount to 4 decimals. |
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
| BILLABLE | Optional | string | Billable option for project-related transactions imported into the GL through external systems. Use `true` for billable transactions (Default: `false`). See the Sage Intacct product help for [project configuration](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Setting_Up_the_Projects_Application) information. |
| SPLIT | Optional | `SPLIT`\[\] | Custom allocation split. Required if `ALLOCATION` equals `Custom`. Multiple `SPLIT` elements may then be passed. |
| TAXENTRIES | Optional | `TAXENTRY[1]` | Tax entry for the line (AU, GB, ZA only) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`TAXENTRY` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the journal entry.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DETAILID | Required | string | Tax rate specified via the unique ID of a tax detail |
| TRX\_TAX | Required | currency | Transaction tax, which is your manually calculated value for the tax. |

`SPLIT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| AMOUNT | Required | currency | Split transaction amount. Absolute value. All `SPLIT` element’s `AMOUNT` values must sum up to equal `GLENTRY` element’s `TRX_AMOUNT` |
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

### Create Journal Entry (Legacy)

[History](https://developer.intacct.com/api/general-ledger/journal-entries/#history-create-journal-entry-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `create_gltransaction`

```
<create_gltransaction>
    <journalid>PYRJ</journalid>
    <datecreated>
        <year>2017</year>
        <month>03</month>
        <day>31</day>
    </datecreated>
    <reversedate>
        <year>2017</year>
        <month>04</month>
        <day>01</day>
    </reversedate>
    <description>Payroll accrual 03/31/2016</description>
    <gltransactionentries>
        <glentry>
            <trtype>-1</trtype>
            <amount>1450.80</amount>
            <glaccountno>2080</glaccountno>
            <memo>Accrued salaries</memo>
            <locationid>100</locationid>
            <departmentid>ADMIN</departmentid>
            <currency>USD</currency>
            <exchratetype>Intacct Daily Rate</exchratetype>
        </glentry>
        <glentry>
            <trtype>1</trtype>
            <amount>1450.80</amount>
            <glaccountno>6500</glaccountno>
            <memo>Salary expense</memo>
            <locationid>100</locationid>
            <departmentid>ADMIN</departmentid>
            <currency>USD</currency>
            <exchratetype>Intacct Daily Rate</exchratetype>
        </glentry>
    </gltransactionentries>
</create_gltransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| journalid | Required | string | GL journal symbol. This determines the type of journal entry as visible in the UI, for example, Regular, Adjustment, User-defined, Statistical, GAAP, Tax, and so forth. |
| datecreated | Required | object | Posting date |
| reversedate | Optional | object | Reverse date. Must be greater than posting date. |
| description | Required | string | Description of entry |
| referenceno | Optional | string | Reference number of transaction |
| sourceentity | Optional | string | Source entity ID. Required if multi-entity enabled and entries do not balance by entity. |
| customfields | Optional | array of `customfield` | Custom fields |
| gltransactionentries | Required | `GLENTRY[2...n]` | Must have at least two lines (one debit, one credit). |

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

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`glentry`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| trtype | Required | string | Transaction type. Use `debit` or `credit`. |
| amount | Required | currency | Transaction amount. Absolute value, relates to `trtype`. |
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
| currency | Optional | string | Transaction currency code. Required if multi-currency enabled. |
| exchratedate | Optional | string | Exchange rate date in format `mm/dd/yyyy`. If null, defaults to journal entry posting date. |
| exchratetype | Optional | string | Exchange rate type. Required if multi-currency enabled and `exchrate` left blank. (Default `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate. Required if multi currency enabled and `exchratetype` left blank. Exchange rate amount to 4 decimals. |

* * *

### Update Journal Entry

[History](https://developer.intacct.com/api/general-ledger/journal-entries/#history-update-journal-entry)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added COSTTYPEID |
| 2019 Release 4 | Added TASKID |
| 2019 Release 3 | Added TAXIMPLICATIONS, VATVENDORID, VATCUSTOMERID, VATCONTACTID, TAXENTRIES |

To add an entry, supply all the original entries along with the new one. To delete an entry, supply only the entries you want to keep.

#### `update`

```
<update>
    <GLBATCH>
        <RECORDNO>1</RECORDNO>
        <JOURNAL>PYRJ</JOURNAL>
        <BATCH_DATE>03/31/2016</BATCH_DATE>
        <REVERSEDATE>04/01/2016</REVERSEDATE>
        <BATCH_TITLE>Payroll accrual 03/31/2016</BATCH_TITLE>
        <ENTRIES>
            <GLENTRY>
                <ACCOUNTNO>2080</ACCOUNTNO>
                <DEPARTMENT>ADMIN</DEPARTMENT>
                <LOCATION>100</LOCATION>
                <CURRENCY>USD</CURRENCY>
                <TR_TYPE>-1</TR_TYPE>
                <AMOUNT>1450.80</AMOUNT>
                <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                <DESCRIPTION>Accrued salaries</DESCRIPTION>
            </GLENTRY>
            <GLENTRY>
                <ACCOUNTNO>6500</ACCOUNTNO>
                <DEPARTMENT>ADMIN</DEPARTMENT>
                <LOCATION>100</LOCATION>
                <CURRENCY>USD</CURRENCY>
                <TR_TYPE>1</TR_TYPE>
                <AMOUNT>1450.80</AMOUNT>
                <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
                <DESCRIPTION>Salary expense</DESCRIPTION>
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
| RECORDNO | Required | integer | Journal entry `RECORDNO` to update |
| BATCH\_DATE | Required | string | Posting date in format `mm/dd/yyyy` |
| BATCH\_TITLE | Required | string | Description of entry |
| TAXIMPLICATIONS | Optional | string | Tax implications. Use `None`, `Inbound` for purchase tax, or `Outbound` for sales tax. (AU, GB, ZA only) |
| VATVENDORID | Optional | string | Vendor ID when tax implications is set to `Inbound` for tax on purchases (AU, GB, ZA only) |
| VATCUSTOMERID | Optional | string | Customer ID when tax implications is set to `Outbound` for tax on sales (AU, GB, ZA only) |
| VATCONTACTID | Optional | string | Contact name for the customer `SHIPTO` contact for sales journals or the vendor ID for the vendor `PAYTO` contact for purchase journals (AU, GB, ZA only) |
| HISTORY\_COMMENT | Optional | string | Comment added to history for this transaction. |
| REFERENCENO | Optional | string | Reference number of transaction |
| BASELOCATION\_NO | Optional | string | Source entity ID. Required if multi-entity enabled and entries do not balance by entity. |
| SUPDOCID | Optional | string | Attachments ID |
| STATE | Optional | string | State to update the entry to. `Posted` to post to the GL, otherwise `Draft`. |
| ENTRIES | Required | `GLENTRY[2...n]` | Must have at least two lines (one debit, one credit). |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`GLENTRY`

(AU, GB, ZA) You must include any existing tax entries in order to retain them. To delete a tax entry, perform an update and omit the `TAXENTRIES` for the line. To modify a tax entry, provide the record number and the new values for the entry’s parameters.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCUMENT | Optional | string | Document number of entry |
| ACCOUNTNO | Required | string | Account number |
| CURRENCY | Optional | string | Transaction currency code. Required if multi-currency enabled. |
| TRX\_AMOUNT | Required | currency | Transaction amount. Absolute value, relates to `TR_TYPE`. |
| TR\_TYPE | Required | string | Transaction type. `1` for Debit, otherwise `-1` for Credit. |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy`. If null, defaults to `BATCH_DATE`. |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Required if multi-currency enabled and `EXCHANGE_RATE` left blank. (Default `custom`) |
| EXCHANGE\_RATE | Optional | currency | Exchange rate. Required if multi currency enabled and `EXCH_RATE_TYPE_ID` left blank. Exchange rate amount to 4 decimals. |
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
| BILLABLE | Optional | string | Billable option for project-related transactions imported into the GL through external systems. Use `true` for billable transactions (Default: `false`). See the Sage Intacct product help for [project configuration](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Setting_Up_the_Projects_Application) information. |
| SPLIT | Optional | `SPLIT`\[\] | Custom allocation split. Required if `ALLOCATION` equals `Custom`. Multiple `SPLIT` elements may then be passed. |
| TAXENTRIES | Optional | `TAXENTRY[1]` | Tax entry for the line (AU, GB, ZA only) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`TAXENTRY` (AU, GB, ZA only)

Specifies a tax rate (defined in the system) and a manually calculated tax for the journal entry.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of an existing tax entry (associated with this line) that you want to modify. You can omit this parameter to create a new tax entry. |
| DETAILID | Required | string | Tax rate specified via the unique ID of a tax detail |
| TRX\_TAX | Required | currency | Transaction tax, which is your manually calculated value for the tax. |

`SPLIT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| AMOUNT | Required | currency | Split transaction amount. Absolute value. All `SPLIT` element’s `AMOUNT` values must sum up to equal `GLENTRY` element’s `TRX_AMOUNT`. |
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

### Delete Journal Entry

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
| keys | Required | string | Comma-separated list of journal entry `RECORDNO` to delete |

* * *

### Delete Journal Entry (Legacy)

#### `delete_gltransaction`

```
<delete_gltransaction key="1234"></delete_gltransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Journal entry record number to delete |

* * *

Journal Entry Lines
-------------------

### Get Journal Entry Line Object Definition

#### `lookup`

> List all the fields and relationships for the journal entry line object:

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

### Query and List Journal Entry Lines

#### `query`

> List the record number, batch number, and amount for each journal entry line:

```
<query>
    <object>GLENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>BATCHNO</field>
        <field>AMOUNT</field>
    </select>
</query>
```

> List journal entry lines for a journal whose record number is 6679:

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
            <value>6679</value>
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

### Query and List Journal Entry Lines (Legacy)

#### `readByQuery`

> Lists journal entry lines:

```
<readByQuery>
    <object>GLENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> Lists journal entry lines for a journal whose record number is 6679:

```
<readByQuery>
    <object>GLENTRY</object>
    <fields>*</fields>
    <query>BATCHNO = '6679'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

> The above function returns data structured like this:

```
<glentry>
    <RECORDNO>99612</RECORDNO>
    <BATCHNO>6679</BATCHNO>
    <USERNO>20</USERNO>
    <LINE_NO>1</LINE_NO>
    <TR_TYPE>1</TR_TYPE>
    <ENTRY_DATE>01/09/2019</ENTRY_DATE>
    <AMOUNT>50000</AMOUNT>
    <TRX_AMOUNT>50000</TRX_AMOUNT>
    <BATCH_NUMBER>249</BATCH_NUMBER>
    <BATCH_DATE>01/09/2019</BATCH_DATE>
    <BATCHTITLE>Paying some folks</BATCHTITLE>
    <ACCOUNTKEY>64</ACCOUNTKEY>
    <ACCOUNTNO>6100</ACCOUNTNO>
    <ACCOUNTTITLE>Salaries</ACCOUNTTITLE>
    <STATISTICAL>F</STATISTICAL>
    ...
</glentry>
<glentry>
    <RECORDNO>99613</RECORDNO>
    <BATCHNO>6679</BATCHNO>
    <USERNO>20</USERNO>
    <LINE_NO>2</LINE_NO>
    <TR_TYPE>-1</TR_TYPE>
    <ENTRY_DATE>01/09/2019</ENTRY_DATE>
    <AMOUNT>50000</AMOUNT>
    <TRX_AMOUNT>50000</TRX_AMOUNT>
    <BATCH_NUMBER>249</BATCH_NUMBER>
    <BATCH_DATE>01/09/2019</BATCH_DATE>
    <BATCHTITLE>Paying some folks</BATCHTITLE>
    <ACCOUNTKEY>114</ACCOUNTKEY>
    <ACCOUNTNO>2010</ACCOUNTNO>
    <ACCOUNTTITLE>Inter Entity Payable</ACCOUNTTITLE>
    <STATISTICAL>F</STATISTICAL>
    ...
</glentry>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Journal Entry Line

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
| keys | Required | string | Comma-separated list of journal entry line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

