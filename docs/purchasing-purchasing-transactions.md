Title: Purchasing Transactions

URL Source: https://developer.intacct.com/api/purchasing/purchasing-transactions/

Markdown Content:
*   [Purchasing Transactions](https://developer.intacct.com/api/purchasing/purchasing-transactions/#purchasing-transactions)
    *   [Get Purchasing Transaction Object Definition](https://developer.intacct.com/api/purchasing/purchasing-transactions/#get-purchasing-transaction-object-definition)
    *   [Query and List Purchasing Transactions](https://developer.intacct.com/api/purchasing/purchasing-transactions/#query-and-list-purchasing-transactions)
    *   [Query and List Purchasing Transactions (Legacy)](https://developer.intacct.com/api/purchasing/purchasing-transactions/#query-and-list-purchasing-transactions-legacy)
    *   [Get Purchasing Transaction](https://developer.intacct.com/api/purchasing/purchasing-transactions/#get-purchasing-transaction)
    *   [Create Purchasing Transaction (Legacy)](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create-purchasing-transaction-legacy)
    *   [Update Purchasing Transaction (Legacy)](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update-purchasing-transaction-legacy)
    *   [Partial Update Purchasing Transaction (Legacy)](https://developer.intacct.com/api/purchasing/purchasing-transactions/#partial-update-purchasing-transaction-legacy)
    *   [Query and List Purchasing Transactions To Approve](https://developer.intacct.com/api/purchasing/purchasing-transactions/#query-and-list-purchasing-transactions-to-approve)
    *   [Approve Purchasing Transactions](https://developer.intacct.com/api/purchasing/purchasing-transactions/#approve-purchasing-transactions)
    *   [Decline Purchasing Transactions](https://developer.intacct.com/api/purchasing/purchasing-transactions/#decline-purchasing-transactions)
    *   [Get Purchasing Transaction Approval History](https://developer.intacct.com/api/purchasing/purchasing-transactions/#get-purchasing-transaction-approval-history)
    *   [Delete Purchasing Transaction](https://developer.intacct.com/api/purchasing/purchasing-transactions/#delete-purchasing-transaction)
    *   [Delete Purchasing Transaction (Legacy)](https://developer.intacct.com/api/purchasing/purchasing-transactions/#delete-purchasing-transaction-legacy)
*   [Purchasing Transaction Lines](https://developer.intacct.com/api/purchasing/purchasing-transactions/#purchasing-transaction-lines)
    *   [Get Purchasing Transaction Line Object Definition](https://developer.intacct.com/api/purchasing/purchasing-transactions/#get-purchasing-transaction-line-object-definition)
    *   [Query and List Purchasing Transaction Lines](https://developer.intacct.com/api/purchasing/purchasing-transactions/#query-and-list-purchasing-transaction-lines)
    *   [Query and List Purchasing Transaction Lines (Legacy)](https://developer.intacct.com/api/purchasing/purchasing-transactions/#query-and-list-purchasing-transaction-lines-legacy)
    *   [Get Purchasing Transaction Line](https://developer.intacct.com/api/purchasing/purchasing-transactions/#get-purchasing-transaction-line)
*   [Purchasing Transaction Subtotals](https://developer.intacct.com/api/purchasing/purchasing-transactions/#purchasing-transaction-subtotals)
    *   [Get Purchasing Transaction Subtotal Object Definition](https://developer.intacct.com/api/purchasing/purchasing-transactions/#get-purchasing-transaction-subtotal-object-definition)
    *   [Query and List Purchasing Transaction Subtotals](https://developer.intacct.com/api/purchasing/purchasing-transactions/#query-and-list-purchasing-transaction-subtotals)
    *   [Query and List Purchasing Transaction Subtotals (Legacy)](https://developer.intacct.com/api/purchasing/purchasing-transactions/#query-and-list-purchasing-transaction-subtotals-legacy)
    *   [Get Purchasing Transaction Subtotal](https://developer.intacct.com/api/purchasing/purchasing-transactions/#get-purchasing-transaction-subtotal)

* * *

Purchasing transactions are the records of a company’s purchases, including purchase requisitions, purchase orders, vendor invoices, and more.

#### About related Purchasing and AP record numbers

Certain types of transaction definitions in Purchasing (such as Vendor Invoice) are configured to create corresponding bills in the Accounts Payable module. When a transaction is updated in Purchasing, the related AP transaction is deleted and recreated. As a result, the AP transaction will have a new `RECORDNO`. Integrations needing to look up the related AP transaction can do so using the `PRRECORDKEY` field outlined below.

#### About converting from source documents

Many purchasing documents are created by converting from other “source” documents. There are two types of conversions available:

*   Convert from a single document: Use the `createdfrom` field in the `<create_potransaction>` request body and the `sourcelinekey` field in the `<potransitem>` transaction line.
*   Convert from multiple documents: Use the `sourcedocid` and `sourcedoclineid` fields for each `<potransitem>` in the `<create_potransaction>` request body. The company must have a Construction subscription to do multi-document conversion.

* * *

### Get Purchasing Transaction Object Definition

#### `lookup`

> List all the fields and relationships for the purchasing transaction object:

```
<lookup>
    <object>PODOCUMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENT` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Purchasing Transactions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, document number, and document type for each purchasing transaction:

```
<query>
    <object>PODOCUMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>DOCNO</field>
        <field>DOCPARID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENT` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Purchasing Transactions (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>PODOCUMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Purchase Order</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PRRECORDKEY | Optional | integer | Related `RECORDNO` of the corresponding AP transaction created by the Purchasing transaction. |
| STATE | Optional | string | State.
*   `S` - Submitted
*   `A` - Approved
*   `X` - Partially Approved
*   `R` - Declined
*   `I` - Draft
*   `O` - Pending
*   `D` - Closed
*   `G` - In Progress
*   `C` - Converted
*   `P` - Partially Converted

 |
| UPDATES\_INV | Optional | string | Inventory effect.

*   `T` - Quantity and value
*   `V` - Value
*   `Q` - Quantity

 |

* * *

### Get Purchasing Transaction

#### `read`

```
<read>
    <object>PODOCUMENT</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Purchase Order</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENT` |
| keys | Required | string | Comma-separated list of transaction `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Create Purchasing Transaction (Legacy)

[History](https://developer.intacct.com/api/purchasing/purchasing-transactions/#history-create-purchasing-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2024 Release 3 | Added sourcedocid and sourcedoclineid fields for potransitem |
| 2024 Release 2 | Added paymenttaxcapture field for potransitem |
| 2023 Release 2 | Added reverseconversion field for potransitem |
| 2022 Release 1 | Added linesubtotals array to allow VAT tax override |
| 2021 Release 3 | Added partialexempt, projectid (on the header), changelognumber, itemdetails now supports trackable kit item types |
| 2021 Release 1 | Added itemaliasid |
| 2020 Release 4 | Added taxsolutionid, relateddockey, relateddoclinekey, conversiontype |
| 2020 Release 3 | Added trx\_amountretained |
| 2020 Release 2 | Added parameters for Construction application |
| 2020 Release 1 | Added retainagepercentage, costtypeid |
| 2020 Release 1 | Added allocationid |
| 2019 Release 4 | Added needbydate, donotshipbeforedate, donotshipafterdate, promiseddate, contractstartdate, contractenddate, cancelafterdate, dateconfirmed, dateshiptosupplier, taskid |
| 2018 Release 2 | Added deliverto, linelevelsimpletaxtype |
| 2024 Release 4 | Updated note about retainagepercentage and trx amountretained |

#### `create_potransaction`

> Creates a Purchasing transaction with a single line:

```
<create_potransaction>
    <transactiontype>Purchase Requisition</transactiontype>
    <datecreated>
        <year>2013</year>
        <month>6</month>
        <day>19</day>
    </datecreated>
    <vendorid>1001</vendorid>
    <referenceno>1234</referenceno>
    <vendordocno>vendordocno001</vendordocno>
    <datedue>
        <year>2013</year>
        <month>6</month>
        <day>20</day>
    </datedue>
    <payto>
        <contactname>Jameson Company</contactname>
    </payto>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <customfields></customfields>
    <potransitems>
        <potransitem>
            <itemid>75300GL</itemid>
            <quantity>100</quantity>
            <unit>Each</unit>
            <price>1</price>
            <locationid>MGMT-US</locationid>
            <departmentid>IT</departmentid>
        </potransitem>
    </potransitems>
</create_potransaction>
```

> Assuming that the transaction definition is configured as a source document for change management, creates a Purchasing transaction as a source that can accept change orders (Construction subscription):

```
<create_potransaction>
    <transactiontype>Source-001</transactiontype>
    <datecreated>
        <year>2020</year>
        <month>06</month>
        <day>17</day>
    </datecreated>
    <vendorid>201</vendorid>
    <datedue>
        <year>2020</year>
        <month>07</month>
        <day>05</day>
    </datedue>
    <message>Source for project 19</message>
    <returnto>
        <contactname></contactname>
    </returnto>
    <payto>
        <contactname></contactname>
    </payto>
    <state>Pending</state>
    <potransitems>
        <potransitem>
            <itemid>A001</itemid>
            <warehouseid>WareHouse10004</warehouseid>
            <quantity>10</quantity>
            <unit>Each</unit>
            <price>99.99</price>
            <locationid>1</locationid>
        </potransitem>
    </potransitems>
</create_potransaction>
```

> Assuming that the transaction definition is configured as a change order, creates a Purchasing transaction as a change order with two lines. One line is a change for an existing line (created above), and the other line is new. (Construction subscription):

```
<create_potransaction>
    <transactiontype>Change-001</transactiontype>
    <datecreated>
        <year>2020</year>
        <month>06</month>
        <day>30</day>
    </datecreated>
    <createdfrom></createdfrom>
    <vendorid>201</vendorid>
    <message>Change for new requirements</message>
    <returnto>
        <contactname></contactname>
    </returnto>
    <payto>
        <contactname></contactname>
    </payto>
    <state>Pending</state>
    <potransitems>
        <potransitem>
            <itemid>A001</itemid>
            <warehouseid>WareHouse10004</warehouseid>
            <quantity>15</quantity>
            <unit>Each</unit>
            <price>100.99</price>
            <locationid>1</locationid>
            <relateddockey>255</relateddockey>
            <relateddoclinekey>256</relateddoclinekey>
        </potransitem>
        <potransitem>
            <itemid>A006</itemid>
            <warehouseid>WareHouse10006</warehouseid>
            <quantity>100</quantity>
            <unit>Each</unit>
            <price>80.99</price>
            <locationid>1</locationid>
            <relateddockey>255</relateddockey>
        </potransitem>
    </potransitems>
</create_potransaction>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| transactiontype | Required | string | Transaction definition to use, such as a Purchase Order |
| datecreated | Required | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Transaction date |
| dateposted | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | GL posting date |
| createdfrom | Optional | string | For single-document conversions, the purchasing transaction document number to convert from. Also see [sourcelinekey](https://developer.intacct.com/api/purchasing/purchasing-transactions/#potransitem.sourcelinekey) in `<potransitem>`. |
| vendorid | Required | String | Vendor ID |
| documentno | Optional | string | Document number. Leave blank to use auto numbering if set in definition |
| referenceno | Optional | string | Reference number |
| vendordocno | Optional | string | Vendor document number |
| termname | Optional | string | Payment term. Required if not using `datedue`. |
| datedue | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Due date. Required if not using `termname`. |
| message | Optional | string | Message |
| shippingmethod | Optional | string | Shipping method |
| returnto | Required | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.contact) | Return to contact. Set it to null to use vendor’s default. |
| payto | Required | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.contact) | Pay to contact. Set it null to use vendor’s default. |
| deliverto | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.contact) | Deliver to contact for tax calculation |
| supdocid | Optional | string | Attachments ID |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Leave blank to use `Intacct Daily Rate`. Do not use if `exchrate` is set. |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| customfields | Optional | array of `customfield` | Custom fields |
| state | Optional | string | Action.
*   `Draft`
*   `Pending`
*   `Closed`

Default depends on transaction definition configuration. |
| projectid | Optional | String | Project ID |
| changelognumber | Optional | integer | Change log number for tracking the number of changes applied to a source transaction. When you create a source transaction, its `changelognumber` is set to 0 by default. Then, each time you submit a change transaction against it, the number on the source is incremented. When you create a change transaction, it’s `changelognumber` is set to 1 by default. (Default: 0 for a source transaction, 1 for a change transaction) (Construction subscription) |
| needbydate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Need by date, which is the date you need the goods to arrive on your premises. (Default: Due date) |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Do not ship before date |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Do not ship after date |
| promiseddate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Promised by date, which is the date the vendor promised to deliver the goods. |
| contractstartdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Contract start date, which is the valid start date of a purchase order or purchase contract. |
| contractenddate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Contract end date , which is the valid end date of a purchase order or purchase contract. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.date) | Cancel after date, which is the date after which the transaction should be canceled. |
| scope | Optional | string | Details about the expected scope of work to be performed or materials to be delivered. Use 4000 or fewer characters. (Construction subscription) |
| inclusions | Optional | string | Details related to items that are explicitly included in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| exclusions | Optional | string | Details related to items that are explicitly excluded in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| terms | Optional | string | Additional terms or performance obligations. Use 4000 or fewer characters. (Construction subscription) |
| schedulestartdate | Optional | date | Scheduled start date in the `mm/dd/yyyy` format (Construction subscription) |
| actualstartdate | Optional | date | Actual start date in the `mm/dd/yyyy` format (Construction subscription) |
| scheduledcompletiondate | Optional | date | Original scheduled date for completion of the work in the `mm/dd/yyyy` format (Construction subscription) |
| revisedcompletiondate | Optional | date | Revised completion date for the work (caused by changes). Specified in the `mm/dd/yyyy` format. (Construction subscription) |
| substantialcompletiondate | Optional | date | Date the work is considered substantially complete in the `mm/dd/yyyy` format. Typically used as a milestone to identify when payment obligations are due. (Construction subscription) |
| actualcompletiondate | Optional | date | Date the work is actually complete in the `mm/dd/yyyy` format (Construction subscription) |
| noticetoproceed | Optional | date | Date when a formal notice to proceed was given in the `mm/dd/yyyy` format (Construction subscription) |
| responsedue | Optional | date | Date when a response is expected from an external party in the `mm/dd/yyyy` format (Construction subscription) |
| executedon | Optional | date | Date the related contract document was formally executed in the `mm/dd/yyyy` format (Construction subscription) |
| scheduleimpact | Optional | string | Details about any impacts on the current schedule. Use 100 or fewer characters. (Construction subscription) |
| internalrefno | Optional | string | Specifies an internal reference ID that can be tracked separately from the formal document number (`documentno`) (Construction subscription) |
| internalinitiatedby | Optional | string | ID of the employee who initiated the transaction. (Construction subscription) |
| internalverbalby | Optional | string | ID of the employee who verbally agreed to the transaction. (Construction subscription) |
| internalissuedby | Optional | string | ID of the employee who issued the transaction. (Construction subscription) |
| internalissuedon | Optional | date | Internal issued-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalapprovedby | Optional | string | ID of the employee who approved the transaction. (Construction subscription) |
| internalapprovedon | Optional | date | Internal approved-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalsignedby | Optional | string | ID of the employee who signed for the transaction. (Construction subscription) |
| internalsignedon | Optional | string | Internal signed-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalsource | Optional | string | Internal reference source when the transaction originated from another document or workflow. Can be an internal or external source. For example, a request for information (RFI) or a project change request. Use 100 or fewer characters. (Construction subscription) |
| internalsourcerefno | Optional | string | Internal reference source number or ID when the transaction originated from another source. Can be an internal or external number. Use 100 or fewer characters. (Construction subscription) |
| externalrefno | Optional | string | External reference number for this transaction, such as one required by a vendor or customer. (Construction subscription) |
| externalverbalby | Optional | string | Name of the contact who verbally agreed to the transaction. For example, a customer or vendor contact. (Construction subscription) |
| externalapprovedby | Optional | string | Name of the contact who approved the document. For example, a customer or vendor contact. (Construction subscription) |
| externalapprovedon | Optional | date | Date the customer or vendor approved the transaction in the `mm/dd/yyyy` format (Construction subscription) |
| externalsignedby | Optional | string | Name of the external contact who signed for the transaction. For example, a customer or vendor contact. (Construction subscription) |
| externalsignedon | Optional | date | Date the customer or vendor signed for the transaction in the `mm/dd/yyyy` format (Construction subscription) |
| performancebondrequired | Optional | boolean | Whether a performance bond is required.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| performancebondreceived | Optional | boolean | Whether performance bond documentation was received.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| performancebondamount | Optional | currency | Amount of the performance bond (Construction subscription) |
| performancesuretycompany | Optional | string | ID of the vendor for the related surety company providing the performance bond (Construction subscription) |
| paymentbondrequired | Optional | boolean | Whether a payment bond is required.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| paymentbondreceived | Optional | boolean | Whether payment bond was received.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| paymentbondamount | Optional | currency | Amount of the payment bond (Construction subscription) |
| paymentsuretycompany | Optional | string | ID of the vendor for the related surety company providing the payment bond (Construction subscription) |
| taxsolutionid | Optional | string | Tax solution name, such as `United Kingdom - VAT` or `Australia - GST`. Required only if the company is configured for multiple tax jurisdictions and the transaction is occurring at the top level of the company. The available tax solution names can be found in the Sage Intacct UI in the Taxes application from the top level of a multi-entity company. (GB, AU, and ZA only) |
| potransitems | Required | array of [potransitem](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem) | Transaction lines, must have at least 1. |
| subtotals | Optional | array of [subtotal](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.subtotal) | Subtotal lines |

`create_potransaction.datecreated`  
`create_potransaction.dateposted`  
`create_potransaction.datedue`  
`create_potransaction.exchratedate`  
`create_potransaction.needbydate`  
`create_potransaction.donotshipbeforedate`  
`create_potransaction.donotshipafterdate`  
`create_potransaction.promiseddate`  
`create_potransaction.contractstartdate`  
`create_potransaction.contractenddate`  
`create_potransaction.cancelafterdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`create_potransaction.returnto` `create_potransaction.payto` `create_potransaction.deliverto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`create_potransaction.potransitems.potransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | Item ID |
| itemaliasid | Optional | string | Alias name for the item as set up in an [item cross reference](https://developer.intacct.com/api/inventory-control/item-cross-references/) created for the vendor on this transaction. |
| itemdesc | Optional | string | Item description |
| taxable | Optional | boolean | Taxable.
*   `false` - No
*   `true` - Yes

Customer must be set up for taxable. |
| warehouseid | Optional | string | Warehouse ID |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure for `quantity` |
| linelevelsimpletaxtype | Optional | string | Simple tax rate to apply at the line level. Available only if Enable subtotals and Enable line level Simple Tax are enabled for the transaction definition. |
| price | Optional | currency | Price |
| sourcelinekey | Optional | integer | `RECORDNO` of the source line to convert from in the `createdfrom` transaction document. |
| overridetaxamount | Optional | currency | Override tax amount |
| deliverto | Optional | object | Deliver to contact for tax calculation |
| tax | Optional | currency | Tax amount |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| memo | Optional | string | Memo |
| itemdetails | Optional | array of [itemdetail](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.itemdetails.itemdetail) | Item details (applicable to inventory or stockable kit item types). |
| form1099 | Optional | boolean | Form 1099.

*   `false` - No
*   `true` - Yes

Vendor must be set up for 1099s. |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID for Construction projects. Only available when `projectid` and `taskid` are specified. |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| billable | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| needbydate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Need by date, which is the date you need the goods to arrive on your premises. (Default value: Due date) |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Do not ship before date |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Do not ship after date |
| promiseddate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Promised by date, which is the date the vendor promised to deliver the goods. |
| dateconfirmed | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Date confirmed, which is the date the vendor confirms that they can provide the item being ordered. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Cancel after date, which is the date after which the transaction should be canceled. |
| dateshiptosupplier | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Date shipped to supplier, which is the date that goods were returned to the supplier. |
| allocationid | Optional | string | Transaction allocation ID. Applicable only for non-inventory items such as services. The `quantity` value must be set to 1. |
| retainagepercentage | Optional | numeric | Percentage of the total amount to retain on a transaction that is part of a Construction project. When you supply this value, the value for `trx_amountretained` is automatically calculated (Construction or Projects subscription). |
| trx\_amountretained | Optional | currency | Amount to retain if you want to override the `retainagepercentage`. When you supply this value, the value for `retainagepercentage` is automatically calculated (Construction or Projects subscription). |
| relateddockey | Optional | integer | Record number of the source transaction when creating a change order. See the FAQ about [change orders](https://developer.intacct.com/support/faq/#trans-changes) for information about using the API to compare original values of a source document to revised values. (Construction subscription) |
| relateddoclinekey | Optional | integer | Record number of a source transaction line to modify when creating a change order. If you omit this parameter but supply `relateddockey`, a new line will be created on the source transaction. (Construction subscription) |
| conversiontype | Optional | string | Conversion type to use when converting the transaction to the next step in the workflow (for example, purchase order to vendor invoice).

*   `Price` - conversion based on the price (for non-inventory items only)
*   `Quantity` - conversion based on the quantity and unit

If using `Price`, set `Quantity` to 1 and provide a `unit` that is a base unit (unit factor is 1). (Construction subscription) |
| partialexempt | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases.

*   `false` - No (default)
*   `true` - Yes

(GB only) |
| paymenttaxcapture | Optional | boolean | Generate VAT tax record when transaction line is paid. (French companies and entities only)

*   `false` - No
*   `true` - Yes

 |
| reverseconversion | Optional | boolean | Enables downstream conversions to be either positive or negative so that you can reduce the previously converted amount of a line item.

*   `false` - No (default)
*   `true` - Yes

Purchasing configuration option to enable conversion reversal for non-inventory items must be set. (Construction subscription) |
| linesubtotals | Optional | array of [linesubtotal](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.linesubtotals.linesubtotal) | VAT tax overrides. To override a single tax value you must provide overrides for all taxes on the line item. |
| taxscxheduleid | Optional | string | Tax schedule ID |
| sourcedocid | Optional | string | For multi-document conversions, the document ID of a source document to convert from to create the purchasing transaction. Different `potransitem` objects in the `potransitems` array can convert from different source documents. |
| sourcedoclineid | Optional | string | For multi-document conversions, the `RECORDNO` of the source line to convert from in the `createdfrom` transaction document. `sourcelinekey` must also be set. |

`create_potransaction.potransitems.potransitem.linesubtotals.linesubtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| trx\_tax | Optional | number | Amount of tax for the line item (to override the calculated VAT). |
| overridedetailid | Required | string | The ID of the [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) that you want to apply to this line subtotal. If `trx_tax` is not provided, the VAT will be calculated using the percentage value set in this tax detail. |

`create_potransaction.potransitems.potransitem.itemdetails.itemdetail`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| quantity | Optional | number | Quantity |
| serialno | Optional | string | Serial number. |
| lotno | Optional | string | Lot number. |
| aisle | Optional | string | Aisle |
| row | Optional | string | Row |
| bin | Optional | string | Bin |
| itemexpiration | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#create_potransaction.potransitems.potransitem.date) | Item expiration date |

`create_potransaction.potransitems.potransitem.needbydate`  
`create_potransaction.potransitems.potransitem.donotshipbeforedate`  
`create_potransaction.potransitems.potransitem.donotshipafterdate`  
`create_potransaction.potransitems.potransitem.promiseddate`  
`create_potransaction.potransitems.potransitem.dateconfirmed`  
`create_potransaction.potransitems.potransitem.cancelafterdate`  
`create_potransaction.potransitems.potransitem.dateshiptosupplier`  
`create_potransaction.potransitems.potransitem.itemdetails.itemdetail.itemexpiration`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`create_potransaction.potransitems.potransitem.subtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| description | Required | string | Description |
| total | Required | currency | Total |
| absval | Optional | number | Absolute value |
| percentval | Optional | number | Percent value |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| itemid | Optional | string | Item ID |
| contractid | Optional | string | Contract ID |
| customfields | Optional | array of `customfield` | Custom fields |

* * *

### Update Purchasing Transaction (Legacy)

[History](https://developer.intacct.com/api/purchasing/purchasing-transactions/#history-update-purchasing-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2024 Release 3 | Added sourcedocid and sourcedoclineid fields for potransitem |
| 2023 Release 2 | Added reverseconversion field for potransitem |
| 2022 Release 1 | Added linesubtotals array to allow VAT tax override |
| 2021 Release 3 | Added partialexempt, projectid (on the header), changelognumber, itemdetails now supports trackable kit item types |
| 2021 Release 1 | Added itemaliasid |
| 2020 Release 4 | Added relateddockey, relateddoclinekey, conversiontype |
| 2020 Release 3 | Added trx\_amountretained |
| 2020 Release 2 | Added parameters for Construction application |
| 2020 Release 1 | Added retainagepercentage, costtypeid |
| 2020 Release 1 | Added allocationid |
| 2019 Release 4 | Added needbydate, donotshipbeforedate, donotshipafterdate, promiseddate, contractstartdate, contractenddate, cancelafterdate, dateconfirmed, dateshiptosupplier, taskid |
| 2018 Release 2 | Added deliverto, linelevelsimpletaxtype |
| 2024 Release 4 | Updated note about retainagepercentage and trx amountretained |

**Note:** You cannot update a purchasing transaction or purchasing transaction items if the state of the purchasing transaction is Submitted, In Progress, Converted, or Partially Converted. For more information, see [Purchasing transaction states](https://www.intacct.com/ia/docs/en_US/help_action/Purchasing/Using_Purchasing/Transactions/about-purchasing-transaction-states.htm?cshid=About_purchasing_transaction_states).

Before using this function to modify existing lines, make sure you know the correct line numbers. For this object, the generic `read` function uses a zero-based index for entries returned in the response. However, the object-specific update function uses a one-based index for entries you supply in the request.

After using `read` to get the line number of the entry you want to modify, add one to that number to specify the correct line in your update operation. See [Working with transaction lines and legacy functions](https://developer.intacct.com/web-services/functions/#working-with-transaction-lines-and-legacy-functions) for more information.

**Warning:** Before doing any large scale update operations, perform a test to make sure you are modifying the correct lines.

#### `update_potransaction`

> Update the transaction to add a memo:

```
<update_potransaction key="Purchase Order-PO0213">
    <updatepotransitems>
        <updatepotransitem line_num="1">
            <memo>High priority</memo>
        </updatepotransitem>
    </updatepotransitems>
</update_potransaction>
```

> Update the transaction to include an item alias that was set up in an item cross reference:

```
<update_potransaction key="Purchase Order-PO0213">
    <updatepotransitems>
        <updatepotransitem line_num="1">
            <itemaliasid>PBC001</itemaliasid>
        </updatepotransitem>
    </updatepotransitems>
</update_potransaction>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Document ID to update |
| datecreated | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Transaction date |
| dateposted | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | GL posting date |
| referenceno | Optional | string | Reference number |
| vendordocno | Optional | string | Vendor document number |
| termname | Optional | string | Payment term |
| datedue | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Due date |
| message | Optional | string | Message |
| shippingmethod | Optional | string | Shipping method |
| returnto | Optional | object | Return to contact |
| payto | Optional | object | Pay to contact |
| deliverto | Optional | object | Deliver to contact for tax calculation |
| supdocid | Optional | string | Attachments ID |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Exchange rate date. |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| customfields | Optional | array of `customfield` | Custom fields |
| state | Optional | string | Action.
*   `Draft`
*   `Pending`
*   `Closed`

Default depends on transaction definition configuration. |
| projectid | Optional | String | Project ID |
| changelognumber | Optional | integer | Change log number for tracking the number of changes applied to a source transaction. When you create a source transaction, its `changelognumber` is set to 0 by default. Then, each time you submit a change transaction against it, the number on the source is incremented. When you create a change transaction, it’s `changelognumber` is set to 1 by default. (Construction subscription) |
| needbydate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Need by date, which is the date you need the goods to arrive on your premises. (Default value: Due date) |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Do not ship before date |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Do not ship after date |
| promiseddate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Promised by date, which is the date the vendor promised to deliver the goods. |
| contractstartdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Contract start date, which is the valid start date of a purchase order or purchase contract. |
| contractenddate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Contract end date , which is the valid end date of a purchase order or purchase contract. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.date) | Cancel after date, which is the date after which the transaction should be canceled. |
| scope | Optional | string | Details about the expected scope of work to be performed or materials to be delivered. Use 4000 or fewer characters. (Construction subscription) |
| inclusions | Optional | string | Details related to items that are explicitly included in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| exclusions | Optional | string | Details related to items that are explicitly excluded in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| terms | Optional | string | Additional terms or performance obligations. Use 4000 or fewer characters. (Construction subscription) |
| schedulestartdate | Optional | date | Scheduled start date in the `mm/dd/yyyy` format (Construction subscription) |
| actualstartdate | Optional | date | Actual start date in the `mm/dd/yyyy` format (Construction subscription) |
| scheduledcompletiondate | Optional | date | Original scheduled date for completion of the work in the `mm/dd/yyyy` format (Construction subscription) |
| revisedcompletiondate | Optional | date | Revised completion date for the work (caused by changes). Specified in the `mm/dd/yyyy` format. (Construction subscription) |
| substantialcompletiondate | Optional | date | Date the work is considered substantially complete in the `mm/dd/yyyy` format. Typically used as a milestone to identify when payment obligations are due. (Construction subscription) |
| actualcompletiondate | Optional | date | Date the work is actually complete in the `mm/dd/yyyy` format (Construction subscription) |
| noticetoproceed | Optional | date | Date when a formal notice to proceed was given in the `mm/dd/yyyy` format (Construction subscription) |
| responsedue | Optional | date | Date when a response is due from an external party in the `mm/dd/yyyy` format (Construction subscription) |
| executedon | Optional | date | Date the related contract document was formally executed in the `mm/dd/yyyy` format (Construction subscription) |
| scheduleimpact | Optional | string | Details about any impacts on the current schedule. Use 100 or fewer characters. (Construction subscription) |
| internalrefno | Optional | string | Specifies an internal reference ID that can be tracked separately from the formal document number (`documentno`) (Construction subscription) |
| internalinitiatedby | Optional | string | ID of the employee who initiated the transaction. (Construction subscription) |
| internalverbalby | Optional | string | ID of the employee who verbally agreed to the transaction. (Construction subscription) |
| internalissuedby | Optional | string | ID of the employee who issued the transaction. (Construction subscription) |
| internalissuedon | Optional | date | Internal issued-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalapprovedby | Optional | string | ID of the employee who approved the transaction. (Construction subscription) |
| internalapprovedon | Optional | date | Internal approved-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalsignedby | Optional | string | ID of the employee who signed for the transaction. (Construction subscription) |
| internalsignedon | Optional | string | Internal signed-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalsource | Optional | string | Internal reference source when the transaction originated from another document or workflow. Can be an internal or external source. For example, a request for information (RFI) or a project change request. Use 100 or fewer characters. (Construction subscription) |
| internalsourcerefno | Optional | string | Internal reference source number or ID when the transaction originated from another source. Can be an internal or external number. Use 100 or fewer characters. (Construction subscription) |
| externalrefno | Optional | string | External ref-erence number for this transaction, such as one required by a vendor or customer. (Construction subscription) |
| externalverbalby | Optional | string | Name of the contact who verbally agreed to the transaction. For example, a customer or vendor contact. (Construction subscription) |
| externalapprovedby | Optional | string | Name of the contact who approved the document. For example, a customer or vendor contact. (Construction subscription) |
| externalapprovedon | Optional | date | Date the customer or vendor approved the transaction in the `mm/dd/yyyy` format (Construction subscription) |
| externalsignedby | Optional | string | Name of the external contact who signed for the transaction. For example, a customer or vendor contact. (Construction subscription) |
| externalsignedon | Optional | date | Date the customer or vendor signed for the transaction in the `mm/dd/yyyy` format (Construction subscription) |
| performancebondrequired | Optional | boolean | Whether a performance bond is required.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| performancebondreceived | Optional | boolean | Whether performance bond documentation was received.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| performancebondamount | Optional | currency | Amount of the performance bond (Construction subscription) |
| performancesuretycompany | Optional | string | ID of the vendor for the related surety company providing the performance bond (Construction subscription) |
| paymentbondrequired | Optional | boolean | Whether a payment bond is required.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| paymentbondreceived | Optional | boolean | Whether payment bond was received.

*   `false` - No (default)
*   `true` - Yes

(Construction subscription) |
| paymentbondamount | Optional | currency | Amount of the payment bond (Construction subscription) |
| paymentsuretycompany | Optional | string | ID of the vendor for the related surety company providing the payment bond (Construction subscription) |
| updatepotransitems | optional | array of [updatepotransitem](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem) and/or [potransitem](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.potransitem) | To update an existing line use `updatepotransitem` otherwise to create a new line use `potransitem`. You can mix types in the array. |
| updatesubtotals | Optional | array of [updatesubtotal](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.updatesubtotal) | Subtotal lines |

`update_potransaction.datecreated`  
`update_potransaction.dateposted`  
`update_potransaction.datedue`  
`update_potransaction.exchratedate`  
`update_potransaction.needbydate`  
`update_potransaction.donotshipbeforedate`  
`update_potransaction.donotshipafterdate`  
`update_potransaction.promiseddate`  
`update_potransaction.contractstartdate`  
`update_potransaction.contractenddate`  
`update_potransaction.cancelafterdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_potransaction.returnto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Return to contact name |

`update_potransaction.payto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Pay to contact name |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`update_potransaction.updatepotransitems.updatepotransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| itemid | Optional | string | Item ID |
| itemaliasid | Optional | string | Alias name for the item as set up in an [item cross reference](https://developer.intacct.com/api/inventory-control/item-cross-references/) created for the vendor on this transaction. |
| itemdesc | Optional | string | Item description |
| taxable | Optional | boolean | Taxable.
*   `false` - No
*   `true` - Yes

Customer must be set up for taxable. |
| warehouseid | Optional | string | Warehouse ID |
| quantity | Optional | number | Quantity |
| unit | Optional | string | Unit of measure for `quantity` |
| linelevelsimpletaxtype | Optional | string | Simple tax rate to apply at the line level. Available only if Enable subtotals and Enable line level Simple Tax are enabled for the transaction definition. |
| price | Optional | currency | Price |
| deliverto | Optional | object | Deliver to contact for tax calculation |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| memo | Optional | string | Memo |
| itemdetails | Optional | array of [itemdetail](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.potransitem.itemdetails.itemdetail) | Item details (applicable to inventory or stockable kit item types). |
| form1099 | Optional | boolean | Form 1099.

*   `false` - No
*   `true` - Yes

Vendor must be set up for 1099s. |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| billable | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| needbydate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Need by date, which is the date you need the goods to arrive on your premises. (Default value: Due date) |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Do not ship before date. |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Do ot ship after date |
| promiseddate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Promised by date, which is the date the vendor promised to deliver the goods. |
| dateconfirmed | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Date confirmed, which is the date the vendor confirms that they can provide the item being ordered. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Cancel after date, which is the date after which the transaction should be canceled. |
| dateshiptosupplier | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Date shipped to supplier, which is the date that goods were returned to the supplier. |
| allocationid | Optional | string | Transaction allocation ID. Applicable only for non-inventory items such as services. The `quantity` value must be set to 1. |
| relateddockey | Optional | integer | Record number of the source transaction when creating a change order. See the FAQ about [change orders](https://developer.intacct.com/support/faq/#trans-changes) for information about using the API to compare original values of a source document to revised values. (Construction subscription) |
| relateddoclinekey | Optional | integer | Record number of a source transaction line to modify when creating a change order. If you omit this parameter but supply `relateddockey`, a new line will be created on the source transaction. (Construction subscription) |
| retainagepercentage | Optional | numeric | Percentage of the total amount to retain on a transaction that is part of a Construction project. When you supply this value, the value for `trx_amountretained` is automatically calculated. (Construction or Projects subscription). |
| trx\_amountretained | Optional | currency | Amount to retain if you want to override the `retainagepercentage`. When you supply this value, the value for `retainagepercentage` is automatically calculated. (Construction or Projects subscription). |
| conversiontype | Optional | string | Conversion type to use when converting the transaction to the next step in the workflow (for example, purchase order to vendor invoice).

*   `Price` - conversion based on the price (for non-inventory items only)
*   `Quantity` - conversion based on the quantity and unit

If using `Price`, set `Quantity` to 1 and provide a `unit` that is a base unit (unit factor is 1). (Construction subscription) |
| partialexempt | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases. Use `false` for No, `true` for Yes. (Default: `false`) (GB only) |
| paymenttaxcapture | Optional | boolean | Generate VAT tax record when transaction line is paid. (French companies and entities only)

*   `false` - No
*   `true` - Yes

 |
| reverseconversion | Optional | boolean | Enables downstream conversions to be either positive or negative so that you can reduce the previously converted amount of a line item.

*   `false` - No (default)
*   `true` - Yes

Purchasing configuration option to enable conversion reversal for non-inventory items must be set. (Construction subscription) |
| linesubtotals | Optional | array of [linesubtotal](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.potransitem.linesubtotals.linesubtotal) | VAT tax overrides. To override a single tax value you must provide overrides for all taxes on the line item. |
| taxscxheduleid | Optional | string | Tax schedule ID |
| sourcedocid | Optional | string | For multi-document conversions, the document ID of a source document to convert from to create the purchasing transaction. Different `potransitem` objects in the `potransitems` array can convert from different source documents. |
| sourcedoclineid | Optional | string | For multi-document conversions, the `RECORDNO` of the source line to convert from in the `createdfrom` transaction document. `sourcelinekey` must also be set. |

`update_potransaction.updatepotransitems.potransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | Item ID |
| itemaliasid | Optional | string | Alias name for the item as set up in an [item cross reference](https://developer.intacct.com/api/inventory-control/item-cross-references/) created for the vendor on this transaction. |
| itemdesc | Optional | string | Item description |
| taxable | Optional | boolean | Taxable.
*   `false` - No
*   `true` - Yes

Customer must be set up for taxable. |
| warehouseid | Optional | string | Warehouse ID |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure for `quantity` |
| linelevelsimpletaxtype | Optional | string | Simple tax rate to apply at the line level. Available only if Enable subtotals and Enable line level Simple Tax are enabled for the transaction definition. |
| price | Optional | currency | Price |
| sourcelinekey | Optional | integer | Source line to convert this line from. Use the `RECORDNO` of the line from the `createdfrom` transaction document. |
| overridetaxamount | Optional | currency | Override tax amount |
| deliverto | Optional | object | Deliver to contact for tax calculation |
| tax | Optional | currency | Tax amount |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| memo | Optional | string | Memo |
| itemdetails | Optional | array of [itemdetail](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.potransitem.itemdetails.itemdetail) | Item details (applicable to inventory or stockable kit item types). |
| form1099 | Optional | boolean | Form 1099.

*   `fale` - No
*   `true` - Yes

Vendor must be set up for 1099s. |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| customfields | Optional | array of `customfield` | Custom fields |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| billable | Optional | boolean | Billable.

*   `false` - No (default)
*   `true` - Yes

 |
| needbydate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Need by date, which is the date you need the goods to arrive on your premises. (Default value: Due date) |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Do not ship before date. |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Do ot ship after date |
| promiseddate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Promised by date, which is the date the vendor promised to deliver the goods. |
| dateconfirmed | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Date confirmed, which is the date the vendor confirms that they can provide the item being ordered. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Cancel after date, which is the date after which the transaction should be canceled. |
| dateshiptosupplier | Optional | [object](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.updatepotransitem.date) | Date shipped to supplier, which is the date that goods were returned to the supplier. |
| allocationid | Optional | string | Transaction allocation ID. Applicable only for non-inventory items such as services. The `quantity` value must be set to 1. |
| retainagepercentage | Optional | numeric | Percentage of the total amount to retain on a transaction that is part of a Construction project. When you supply this value, the value for `trx_amountretained` is automatically calculated. (Construction or Projects subscription). |
| trx\_amountretained | Optional | currency | Amount to retain if you want to override the `retainagepercentage`. When you supply this value, the value for `retainagepercentage` is automatically calculated. (Construction or Projects subscription). |
| relateddockey | Optional | integer | Record number of the source transaction when creating a change order. See the FAQ about [change orders](https://developer.intacct.com/support/faq/#trans-changes) for information about using the API to compare original values of a source document to revised values. (Construction subscription) |
| relateddoclinekey | Optional | integer | Record number of a source transaction line to modify when creating a change order. If you omit this parameter but supply `relateddockey`, a new line will be created on the source transaction. (Construction subscription) |
| conversiontype | Optional | string | Conversion type to use when converting the transaction to the next step in the workflow (for example, purchase order to vendor invoice).

*   `Price` - conversion based on the price (for non-inventory items only)
*   `Quantity` - conversion based on the quantity and unit

If using `Price`, set `Quantity` to 1 and provide a `unit` that is a base unit (unit factor is 1). (Construction subscription) |
| partialexempt | Optional | boolean | Enables partial exemption so that you can reclaim a portion of your input VAT on purchases. Use `false` for No, `true` for Yes. (Default: `false`) (GB only) |
| linesubtotals | Optional | array of [linesubtotal](https://developer.intacct.com/api/purchasing/purchasing-transactions/#update_potransaction.updatepotransitems.potransitem.linesubtotals.linesubtotal) | VAT tax overrides. To override a single tax value you must provide overrides for all taxes on the line item. |
| taxscxheduleid | Optional | string | Tax schedule ID |
| sourcedocid | Optional | string | For multi-document conversions, the document ID of a source document to convert from to create the purchasing transaction. Different `potransitem` objects in the `potransitems` array can convert from different source documents. |
| sourcedoclineid | Optional | string | For multi-document conversions, the `RECORDNO` of the source line to convert from in the `createdfrom` transaction document. `sourcelinekey` must also be set. |

`update_potransaction.updatepotransitems.updatepotransitem.linesubtotals.linesubtotal`  
`update_potransaction.updatepotransitems.potransitem.linesubtotals.linesubtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| trx\_tax | Optional | number | Amount of tax for the line item (to override the calculated VAT). |
| overridedetailid | Required | string | The ID of the [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) that you want to apply to this line subtotal. If `trx_tax` is not provided, the VAT will be calculated using the percentage value set in this tax detail. |

`update_potransaction.updatepotransitems.potransitem.itemdetails.itemdetail`  
`update_potransaction.updatepotransitems.updatepotransitem.itemdetails.itemdetail`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| quantity | Optional | number | Quantity |
| serialno | Optional | string | Serial number. |
| lotno | Optional | string | Lot number. |
| aisle | Optional | string | Aisle |
| row | Optional | string | Row |
| bin | Optional | string | Bin |
| itemexpiration | Optional | object | Item expiration |

`update_potransaction.updatepotransitems.potransitem.itemdetails.itemdetail.itemexpiration`  
`update_potransaction.updatepotransitems.updatepotransitem.itemdetails.itemdetail.itemexpiration`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_potransaction.updatepotransitems.potransitem.needbydate`  
`update_potransaction.updatepotransitems.potransitem.donotshipbeforedate`  
`update_potransaction.updatepotransitems.potransitem.donotshipafterdate`  
`update_potransaction.updatepotransitems.potransitem.promiseddate`  
`update_potransaction.updatepotransitems.potransitem.dateconfirmed`  
`update_potransaction.updatepotransitems.potransitem.cancelafterdate`  
`update_potransaction.updatepotransitems.potransitem.dateshiptosupplier` `update_potransaction.updatepotransitems.updatepotransitem.needbydate`  
`update_potransaction.updatepotransitems.updatepotransitem.donotshipbeforedate`  
`update_potransaction.updatepotransitems.updatepotransitem.donotshipafterdate`  
`update_potransaction.updatepotransitems.updatepotransitem.promiseddate`  
`update_potransaction.updatepotransitems.updatepotransitem.dateconfirmed`  
`update_potransaction.updatepotransitems.updatepotransitem.cancelafterdate`  
`update_potransaction.updatepotransitems.updatepotransitem.dateshiptosupplier`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_potransaction.updatepotransitems.potransitem.updatesubtotal`  
`update_potransaction.updatepotransitems.updatepotransitem.updatesubtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| description | Required | string | Description |
| total | Required | currency | Total |
| absval | Optional | number | Absolute value |
| percentval | Optional | number | Percent value |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| itemid | Optional | string | Item ID |
| contractid | Optional | string | Contract ID |
| customfields | Optional | array of `customfield` | Custom fields |

* * *

### Partial Update Purchasing Transaction (Legacy)

This function is used to partially update a purchasing transaction, usually adjusting its GL posting date.

#### `partialupdate_potransaction`

```
<partialupdate_potransaction key="Vendor Invoice-VI1234">
    <dateposted>
        <year>2017</year>
        <month>3</month>
        <day>1</day>
    </dateposted>
</partialupdate_potransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Document ID of transaction to update |
| dateposted | Optional | object | GL posting date |

`dateposted`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

### Query and List Purchasing Transactions To Approve

Lists purchasing transactions that you are authorized to approve or decline.

#### `getTransactionsToApprove`

```
<getTransactionsToApprove>
    <module>purchasing</module>
</getTransactionsToApprove>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| module | Required | string | Use `purchasing` |

* * *

### Approve Purchasing Transactions

#### `approve`

```
<approve>
    <PODOCUMENT>
        <DOCID>Purchase Order-PO0213</DOCID>
        <COMMENT>Final approval for the quarter</COMMENT>
    </PODOCUMENT>
</approve>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PODOCUMENT | Required | string | Object to approve |

`PODOCUMENT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCID | Required | string | Transaction `DOCID` to approve. |
| COMMENT | Optional | string | Comments |

* * *

### Decline Purchasing Transactions

#### `decline`

```
<decline>
    <PODOCUMENT>
        <DOCID>Purchase Order-PO0213</DOCID>
        <COMMENT>Need to wait on this</COMMENT>
    </PODOCUMENT>
</decline>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PODOCUMENT | Required | string | Object to decline |

`PODOCUMENT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCID | Required | string | Transaction `DOCID` to decline. |
| COMMENT | Optional | string | Comments |

* * *

### Get Purchasing Transaction Approval History

Provides the approval history for a purchasing transaction.

#### `getApprovalHistory`

```
<getApprovalHistory>
    <module>purchasing</module>
    <docid>Purchase Order-PO0213</docid>
</getApprovalHistory>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| module | Required | string | Use `purchasing` |
| docid | Required | string | `docid` for the transaction |

* * *

### Delete Purchasing Transaction

#### `delete`

```
<delete>
    <object>PODOCUMENT</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENT` |
| keys | Required | string | Comma-separated list of transaction `RECORDNO` to delete |

* * *

### Delete Purchasing Transaction (Legacy)

#### `delete_potransaction`

```
<delete_potransaction key="Purchase Order-PO0213"></delete_potransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Transaction `DOCID` to delete |

* * *

Purchasing Transaction Lines
----------------------------

### Get Purchasing Transaction Line Object Definition

#### `lookup`

> List all the fields and relationships for the purchasing transaction line object:

```
<lookup>
    <object>PODOCUMENTENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTENTRY` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Purchasing Transaction Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, document header number, and item ID for each purchasing transaction line:

```
<query>
    <object>PODOCUMENTENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>DOCHDRNO</field>
        <field>ITEMID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTENTRY` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Purchasing Transaction Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>PODOCUMENTENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Purchase Order</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get Purchasing Transaction Line

#### `read`

```
<read>
    <object>PODOCUMENTENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Purchase Order</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTENTRY` |
| keys | Required | string | Comma-separated list of transaction line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

Purchasing Transaction Subtotals
--------------------------------

### Get Purchasing Transaction Subtotal Object Definition

#### `lookup`

> List all the fields and relationships for the Purchasing transaction subtotal object:

```
<lookup>
    <object>PODOCUMENTSUBTOTALS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTSUBTOTALS` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Purchasing Transaction Subtotals

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, description, and total for each Purchasing transaction subtotal:

```
<query>
    <object>PODOCUMENTSUBTOTALS</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
        <field>TOTAL</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTSUBTOTALS` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Purchasing Transaction Subtotals (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>PODOCUMENTSUBTOTALS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Purchase Order</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTSUBTOTALS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get Purchasing Transaction Subtotal

#### `read`

```
<read>
    <object>PODOCUMENTSUBTOTALS</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Purchase Order</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PODOCUMENTSUBTOTALS` |
| keys | Required | string | Comma-separated list of transaction subtotal `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Purchase Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

