Title: Contract Invoices

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/

Markdown Content:
*   [Contract Invoice Previews](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#contract-invoice-previews)
    *   [Get Contract Invoice Preview Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#get-contract-invoice-preview-object-definition)
    *   [Query and List Contract Invoice Previews](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#query-and-list-contract-invoice-previews)
    *   [Query and List Contract Invoice Previews (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#query-and-list-contract-invoice-previews-legacy)
    *   [Get Contract Invoice Preview](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#get-contract-invoice-preview)
    *   [Create Contract Invoice Preview](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#create-contract-invoice-preview)
*   [Contract Invoice Preview Lines](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#contract-invoice-preview-lines)
    *   [Get Contract Invoice Preview Line Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#get-contract-invoice-preview-line-object-definition)
    *   [Query and List Contract Invoice Preview Lines](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#query-and-list-contract-invoice-preview-lines)
    *   [Query and List Contract Invoice Preview Lines (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#query-and-list-contract-invoice-preview-lines-legacy)
    *   [Get Contract Invoice Preview Line](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#get-contract-invoice-preview-line)
*   [Contract Invoice Runs](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#contract-invoice-runs)
    *   [Get Contract Invoice Run Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#get-contract-invoice-run-definition)
    *   [Query and List Contract Invoice Runs](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#query-and-list-contract-invoice-runs)
    *   [Query and List Contract Invoice Runs (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#query-and-list-contract-invoice-runs-legacy)
    *   [Get Contract Invoice Run](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#get-contract-invoice-run)
    *   [Create Contract Invoice Run](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#create-contract-invoice-run)

* * *

You can create invoices for any contracts with billable transactions.

You can use filters to preview a set of potential invoices, then execute an invoice run based on that preview. You can choose to aggregate invoices by customer, contract, project, or bill-to contact.

**Note:** `FILTERNAME` may be removed in a future release. `POLICYNAME` should be used instead.

**Note:** Do not confuse a contract invoice preview with a preview _snapshot_, which is used for reporting purposes in the Sage Intacct UI.

* * *

Contract Invoice Previews
-------------------------

### Get Contract Invoice Preview Object Definition

#### `lookup`

> List all the fields and relationships for the contract invoice preview object:

```
<lookup>
    <object>GENINVOICEPREVIEW</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEW` |
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Contract Invoice Previews

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and start date for each contract invoice preview:

```
<query>
    <object>GENINVOICEPREVIEW</object>
    <select>
        <field>RECORDNO</field>
        <field>BILLSCHSTARTDATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEW` |
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
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Contract Invoice Previews (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>GENINVOICEPREVIEW</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEW` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get Contract Invoice Preview

#### `read`

```
<read>
    <object>GENINVOICEPREVIEW</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEW` |
| keys | Required | string | Comma-separated list of invoice preview `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Create Contract Invoice Preview

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoices/#history-create-contract-invoice-preview)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Replaced FILTERNAME with POLICYNAME to use Contract Invoice Policies |
| 2021 Release 3 | Added BILLTO as a value for INVOICEBY |
| 2020 Release 4 | Added CUSTOMER as a value for INVOICEBY |
| 2019 Release 4 | Added INVOICEBY |
| 2024 Release 4 | Added SERVICEPERIODSTARTDATE, SERVICEPERIODENDDATE, SERVICEPERIODOVERRIDEOPTION |

#### `create`

```
<create>
    <GENINVOICEPREVIEW>
        <INVOICEDATE>11/02/2017</INVOICEDATE>
        <ASOFDATE>11/02/2017</ASOFDATE>
        <GLPOSTDATE>11/02/2017</GLPOSTDATE>
        <DOCPARID>Contract Invoice</DOCPARID>
        <INVOICEBY>CUSTOMER#~#BILLTO</INVOICEBY>
        <INCLUDECONTRACTS>true</INCLUDECONTRACTS>
        <INCLUDECONTRACTUSAGE>true</INCLUDECONTRACTUSAGE>
    </GENINVOICEPREVIEW>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GENINVOICEPREVIEW | Required | string | Object to create |

`GENINVOICEPREVIEW`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCPARID | Required | string | Transaction definition to use. Definition must be enabled for Contracts. |
| INVOICEDATE | Required | string | Invoice date in format `mm/dd/yyyy` |
| GLPOSTDATE | Required | string | GL posting date in format `mm/dd/yyyy` |
| ASOFDATE | Required | string | As of date in format `mm/dd/yyyy` |
| INVOICEBY | Optional | string | Specifies how the invoices are organized and consolidated:  
• `CUSTOMER#~#CONTRACT`: A separate invoice for each contract (Legacy value: `CONTRACT`).  
• `CUSTOMER#~#CONTRACT#~#BILLTO`: A separate invoice for each contract per contract line level Bill to contact.  
• `CUSTOMER`: A separate invoice for each customer.  
• `CUSTOMER#~#BILLTO`: A separate invoice for each customer per contract line level Bill to contact.  
• `CUSTOMER#~#CONTRACT#~#PROJECT`: A separate invoice for each project associated with the contract. (Legacy value: `PROJECT#~#CONTRACT` or `CONTRACT#-#PROJECT`)  
• `CUSTOMER#~#CONTRACT#~#BILLTO#~#PROJECT`: A separate invoice for each project associated with the contract per contract line level Bill to contact.  
(Default: `CUSTOMER#~#CONTRACT`) |
| POLICYNAME | Optional | string | Name of a saved invoice policy. To override a filter in the invoice policy, provide a value for the corresponding parameter (for example, use `CONTRACTID` to use the saved invoice policy with a different contract). |
| BILLSCHSTARTDATE | Optional | string | Start date (in format `mm/dd/yyyy`) when using a date range to filter for open billing. The `ASOFDATE` is used as the end of the range. This parameter applies only to scheduled contract billing (not usage, timesheets, expenses, AP bills, or Purchasing transactions). |
| PRICELISTID | Optional | string | Billing price list ID |
| CONTRACTID | Optional | string | Contract ID |
| CONTRACTGROUPID | Optional | string | Contract group ID |
| CURRENCY | Optional | string | Contract currency code |
| PROJECTID | Optional | string | Project ID |
| PROJECTTYPEID | Optional | string | Project type ID |
| PROJECTMANAGERID | Optional | string | Project manager ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CUSTOMERID | Optional | string | Customer ID |
| CUSTOMERTYPEID | Optional | string | Customer type ID |
| ITEMID | Optional | string | Item ID |
| ITEMGROUPID | Optional | string | Item group ID |
| DEPARTMENTID | Optional | string | Department ID |
| LOCATIONID | Optional | string | Location ID |
| INCLUDECONTRACTS | Optional | boolean | Include contracts in the preview. Use `false` for No, `true` for Yes. (Default: `false`) |
| INCLUDECONTRACTUSAGE | Optional | boolean | Include contract usage in the preview. Use `false` for No, `true` for Yes. (Default: `false`) |
| FILTERNAME | Optional | string | This field has been deprecated. Use `POLICYNAME` instead. Name of a saved filter set. To override a filter in the set, provide a value for the corresponding parameter (for example, use `CONTRACTID` to use the saved filter with a different contract). |
| SERVICEPERIODSTARTDATE | Optional | string | Identifies the start date of a billed service period in a contract invoice preview. Not used when SERVICEPERIODOVERRIDEOPTION is set to “Do not override”. |
| SERVICEPERIODENDDATE | Optional | string | Identifies the end date of a billed service period in a contract invoice preview. Not used when SERVICEPERIODOVERRIDEOPTION set to “Do not override.” |
| SERVICEPERIODOVERRIDEOPTION | Optional | string | Indicates whether SERVICEPERIODSTARTDATE and SERVICEPERIODENDDATE in the invoice lines that come from a CONTRACTBILLINGSCHEDULEENTRY or CONTRACTUSAGE record are overridden. Valid options are:
*   `Do not override` - Indicates that the values in SERVICEPERIODSTARTDATE and SERVICEPERIODENDDATE from CONTRACTBILLINGSCHEDULEENTRY or CONTRACTUSAGE are used to generate the invoice preview.
*   `Override empty dates only` - When used, include values for SERVICEPERIODSTARTDATE and SERVICEPERIODENDDATE, which override null values used in CONTRACTBILLINGSCHEDULEENTRY or CONTRACTUSAGE.
*   `Override all dates` - When used, include values for SERVICEPERIODSTARTDATE and SERVICEPERIODENDDATE, which override all values in CONTRACTBILLINGSCHEDULEENTRY or CONTRACTUSAGE.

 |

* * *

Contract Invoice Preview Lines
------------------------------

### Get Contract Invoice Preview Line Object Definition

#### `lookup`

> List all the fields and relationships for the contract invoice preview line object:

```
<lookup>
    <object>GENINVOICEPREVIEWLINE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEWLINE` |

* * *

### Query and List Contract Invoice Preview Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and type for each contract invoice preview line for the contract with the given ID:

```
<query>
    <object>GENINVOICEPREVIEWLINE</object>
    <select>
        <field>RECORDNO</field>
        <field>TYPE</field>
        <field>CONTRACTID</field>
    </select>
    <filter>
        <equalto>
            <field>CONTRACTID</field>
            <value>CTRC-001</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEWLINE` |
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

### Query and List Contract Invoice Preview Lines (Legacy)

```
<readByQuery>
    <object>GENINVOICEPREVIEWLINE</object>
    <fields>*</fields>
    <query>CONTRACTID='CTRC-001'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### `ReadByQuery`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEWLINE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Contract Invoice Preview Line

#### `read`

```
<read>
    <object>GENINVOICEPREVIEWLINE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPREVIEWLINE` |
| keys | Required | string | Comma-separated list of invoice preview line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Contract Invoice Runs
---------------------

### Get Contract Invoice Run Definition

#### `lookup`

> List all the fields and relationships for the contract invoice run object:

```
<lookup>
    <object>GENINVOICERUN</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICERUN` |

* * *

### Query and List Contract Invoice Runs

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number of the invoice run and the record number of the associated invoice preview:

```
<query>
    <object>GENINVOICERUN</object>
    <select>
        <field>RECORDNO</field>
        <field>PREVIEWKEY</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICERUN` |
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

### Query and List Contract Invoice Runs (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>GENINVOICERUN</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICERUN` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | State. Use `S` for Success, `F` for Failed, `I` for In Transit, or `L` for Partial Success. |

* * *

### Get Contract Invoice Run

#### `read`

```
<read>
    <object>GENINVOICERUN</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICERUN` |
| keys | Required | string | Comma-separated list of invoice run `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Contract Invoice Run

#### `create`

```
<create>
    <GENINVOICERUN>
        <PREVIEWKEY>1</PREVIEWKEY>
    </GENINVOICERUN>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GENINVOICERUN | Required | string | Object to create |

`GENINVOICERUN`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PREVIEWKEY | Required | integer | Invoice preview `RECORDNO` to use for the run |
| EXECUTIONMODE | Optional | string | Execution mode for the operation. You can use`Online` for fewer than 50 invoices, but must use `Offline` for more than 50. (Default: `Offline`) |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

