Title: Order Entry Transactions

URL Source: https://developer.intacct.com/api/order-entry/order-entry-transactions/

Markdown Content:
*   [Order Entry Transactions](https://developer.intacct.com/api/order-entry/order-entry-transactions/#order-entry-transactions)
    *   [Get Order Entry Transaction Object Definition](https://developer.intacct.com/api/order-entry/order-entry-transactions/#get-order-entry-transaction-object-definition)
    *   [Query and List Order Entry Transactions](https://developer.intacct.com/api/order-entry/order-entry-transactions/#query-and-list-order-entry-transactions)
    *   [Query and List Order Entry Transactions (Legacy)](https://developer.intacct.com/api/order-entry/order-entry-transactions/#query-and-list-order-entry-transactions-legacy)
    *   [Get Order Entry Transaction](https://developer.intacct.com/api/order-entry/order-entry-transactions/#get-order-entry-transaction)
    *   [Get Order Entry Transaction PDF Data](https://developer.intacct.com/api/order-entry/order-entry-transactions/#get-order-entry-transaction-pdf-data)
    *   [Create Order Entry Transaction (Legacy)](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create-order-entry-transaction-legacy)
    *   [Update Order Entry Transaction (Legacy)](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update-order-entry-transaction-legacy)
    *   [Delete Order Entry Transaction (Legacy)](https://developer.intacct.com/api/order-entry/order-entry-transactions/#delete-order-entry-transaction-legacy)
*   [Order Entry Transaction Lines](https://developer.intacct.com/api/order-entry/order-entry-transactions/#order-entry-transaction-lines)
    *   [Get Order Entry Transaction Line Object Definition](https://developer.intacct.com/api/order-entry/order-entry-transactions/#get-order-entry-transaction-line-object-definition)
    *   [Query and List Order Entry Transaction Lines](https://developer.intacct.com/api/order-entry/order-entry-transactions/#query-and-list-order-entry-transaction-lines)
    *   [Query and List Order Entry Transaction Lines (Legacy)](https://developer.intacct.com/api/order-entry/order-entry-transactions/#query-and-list-order-entry-transaction-lines-legacy)
    *   [Get Order Entry Transaction Line](https://developer.intacct.com/api/order-entry/order-entry-transactions/#get-order-entry-transaction-line)
*   [Order Entry Transaction Subtotals](https://developer.intacct.com/api/order-entry/order-entry-transactions/#order-entry-transaction-subtotals)
    *   [Get Order Entry Transaction Subtotals Object Definition](https://developer.intacct.com/api/order-entry/order-entry-transactions/#get-order-entry-transaction-subtotals-object-definition)
    *   [Query and List Order Entry Transaction Subtotals](https://developer.intacct.com/api/order-entry/order-entry-transactions/#query-and-list-order-entry-transaction-subtotals)
    *   [Query and List Order Entry Transaction Subtotals (Legacy)](https://developer.intacct.com/api/order-entry/order-entry-transactions/#query-and-list-order-entry-transaction-subtotals-legacy)
    *   [Get Order Entry Transaction Subtotal](https://developer.intacct.com/api/order-entry/order-entry-transactions/#get-order-entry-transaction-subtotal)

* * *

Order Entry transactions are the records of customer orders, including quotes, orders, invoices, and more.

_About related OE and AR record numbers_

Certain types of transaction definitions in Order Entry (e.g. Sales Invoice, Contract Invoice, Sales Credit Memo) are configured to create corresponding invoices in the Accounts Receivable application. When a transaction is updated in Order Entry, the related AR transaction is deleted and recreated. As a result, the AR transaction will have a new `RECORDNO`. Integrations needing to look up the related AR transaction can do so using the `PRRECORDKEY` field outlined below.

* * *

### Get Order Entry Transaction Object Definition

#### `lookup`

> List all the fields and relationships for the Order Entry transaction object:

```
<lookup>
    <object>SODOCUMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENT` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Order Entry Transactions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, document ID, and record number of the associated AR invoice for each Order Entry transaction:

```
<query>
    <object>SODOCUMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>DOCID</field>
        <field>ARINVOICE.RECORDNO</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENT` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Order Entry Transactions (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>SODOCUMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Sales Order</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PRRECORDKEY | Optional | integer | Related `RECORDNO` of the corresponding AR transaction created by the Order Entry transaction |
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

* * *

### Get Order Entry Transaction

#### `read`

```
<read>
    <object>SODOCUMENT</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Sales Order</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENT` |
| keys | Required | string | Comma-separated list of transaction `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get Order Entry Transaction PDF Data

#### `retrievepdf`

> Provides base64-encoded data for a PDF version of the specified transaction:

```
<retrievepdf>
    <SODOCUMENT>
        <DOCID>Sales Order-SO1234</DOCID>
    </SODOCUMENT>
</retrievepdf>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SODOCUMENT | Required | object | Use `SODOCUMENT` |

`SODOCUMENT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DOCID | Required | string | Document ID for the transaction |

#### Response

`pdfdata`

> The returned data looks like this:

```
<pdfdata>JVBERi0xLjQKJfbk/N8KMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwovVmVyc2lvbiAvMS40Ci9QYWdlcyAyIDAgUgo ...</pdfdata>
```

* * *

### Create Order Entry Transaction (Legacy)

[History](https://developer.intacct.com/api/order-entry/order-entry-transactions/#history-create-order-entry-transaction-legacy)

| Release | Changes |
| --- | --- |
|  | Added paymenttaxcapture field for sotransitem |
| 2023 Release 1 | Added fields to `sotransitem` to support retainage release:  
isretainagerelease |
| 2022 Release 2 | Added fields to support project contracts.  
In `create_sotransaction`:  
projectcontractid, projectcontractname, projectcontractkey, projectcontractlineid, projectcontractlinename, projectcontractlinekey, pcblexternalrefno, pcbldescription, pcblbillingtype, contractlinevalue, priorapplicationamt, completedthisperiod, storedmaterials, percentcompletedtodate  
In `create_sotransaction.sotransitems.sotransitem`:  
projectcontractid, projectcontractkey, projectcontractname, pcbexternalrefno, pcbdescription, pcbdate, architect, architectkey, billthroughdate, billapplicationno, orgcontractamt, retcompletedamt, retstoredmaterials, lesspriorapplication, tcapmaddition, tcapmdeduction, tcatmaddition, tcatmdeduction |
| 2022 Release 1 | Added linesubtotals array to allow VAT tax override |
| 2021 Release 3 | Added changelognumber, itemdetails now supports trackable kit item types |
| 2021 Release 2 | Added relateddockey, relateddoclinekey |
| 2021 Release 1 | Added conversiontype, itemaliasid |
| 2020 Release 4 | Added shipbydate, shippeddate, taxsolutionid |
| 2020 Release 3 | Added trx\_amountretained |
| 2020 Release 2 | Added parameters for Construction application |
| 2020 Release 1 | Added retainagepercentage, costtypeid |
| 2019 Release 4 | Added needbydate, cancelafterdate, donotshipbeforedate, donotshipafterdate, servicedeliverydate, datepickticketprinted, trackingnumber, customerponumber, shipby, taskid |
| 2018 Release 2 | Added linelevelsimpletaxtype |
| 2024 Release 4 | Added or updated notes about subscription requirements for retcompletedamt, retstoredmaterials, previousretainagebalance, retainagepercentage, trx\_amountretained, and isretainagerelease |

#### `create_sotransaction`

> Creates an Order Entry transaction with a single line:

```
<create_sotransaction>
    <transactiontype>Sales Invoice</transactiontype>
    <datecreated>
        <year>2017</year>
        <month>3</month>
        <day>8</day>
    </datecreated>
    <createdfrom>Sales Order-SO1234</createdfrom>
    <customerid>C1000</customerid>
    <documentno>docno001</documentno>
    <origdocdate>
        <year>2017</year>
        <month>3</month>
        <day>8</day>
    </origdocdate>
    <referenceno>1234</referenceno>
    <termname>Net 30</termname>
    <datedue>
        <year>2016</year>
        <month>4</month>
        <day>7</day>
    </datedue>
    <message>hello world</message>
    <shippingmethod>FedEx</shippingmethod>
    <shipto>
        <contactname>Ship to contact</contactname>
    </shipto>
    <billto>
        <contactname>Bill to contact</contactname>
    </billto>
    <basecurr>USD</basecurr>
    <currency>USD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <customfields></customfields>
    <state>Pending</state>
    <sotransitems>
        <sotransitem>
            <bundlenumber></bundlenumber>
            <itemid>R0044</itemid>
            <quantity>1</quantity>
            <unit>Each</unit>
            <price>100</price>
            <discsurchargememo></discsurchargememo>
            <locationid>ARL-VA-US</locationid>
            <departmentid>ADM</departmentid>
        </sotransitem>
    </sotransitems>
    <subtotals>
        <subtotal>
            <description>Shipping</description>
            <total>20</total>
            <locationid>ARL-VA-US</locationid>
            <departmentid>ADM</departmentid>
        </subtotal>
    </subtotals>
</create_sotransaction>
```

> Assuming that the transaction definition is configured as a source for change management, creates an Order Entry transaction as a source that can accept change orders (Construction subscription):

```
<create_sotransaction>
    <transactiontype>Source_Doc01</transactiontype>
    <datecreated>
        <year>2021</year>
        <month>03</month>
        <day>31</day>
    </datecreated>
    <customerid>BTI</customerid>
    <termname>N15</termname>
    <datedue>
        <year>2021</year>
        <month>04</month>
        <day>15</day>
    </datedue>
    <basecurr>USD</basecurr>
    <currency>USD</currency>
    <exchratedate>
        <year>2021</year>
        <month>03</month>
        <day>31</day>
    </exchratedate>
    <exchratetype/>
    <state>Pending</state>
    <sotransitems>
        <sotransitem>
            <itemid>A001</itemid>
            <itemdesc>Desktop-HP</itemdesc>
            <warehouseid>1</warehouseid>
            <quantity>10</quantity>
            <unit>Each</unit>
            <price>100</price>
            <locationid>1</locationid>
            <conversiontype>Quantity</conversiontype>
        </sotransitem>
        <sotransitem>
            <itemid>A002</itemid>
            <itemdesc>Desktop-Dell</itemdesc>
            <warehouseid>1</warehouseid>
            <quantity>15</quantity>
            <unit>Each</unit>
            <price>120</price>
            <locationid>1</locationid>
            <conversiontype>Quantity</conversiontype>
        </sotransitem>
        <sotransitem>
            <itemid>A001</itemid>
            <itemdesc>Desktop-HP</itemdesc>
            <warehouseid>1</warehouseid>
            <quantity>17</quantity>
            <unit>Each</unit>
            <price>200</price>
            <locationid>1</locationid>
            <conversiontype>Quantity</conversiontype>
        </sotransitem>
    </sotransitems>
</create_sotransaction>
```

> Assuming that the transaction definition is configured as a change order, creates a change order with two lines. One line is a change for an existing line (created above), and the other line is new (no relateddoclinekey is supplied) (Construction subscription):

```
<create_sotransaction>
    <transactiontype>Change_Doc01</transactiontype>
    <datecreated>
        <year>2021</year>
        <month>04</month>
        <day>01</day>
    </datecreated>
    <customerid>BTI</customerid>
    <termname>N15</termname>
    <datedue>
        <year>2021</year>
        <month>05</month>
        <day>15</day>
    </datedue>
    <basecurr>USD</basecurr>
    <currency>USD</currency>
    <exchratedate>
        <year>2021</year>
        <month>04</month>
        <day>01</day>
    </exchratedate>
    <exchratetype/>
    <state>Draft</state>
    <sotransitems>
        <sotransitem>
            <itemid>A001</itemid>
            <itemdesc>Desktop-HP</itemdesc>
            <warehouseid>1</warehouseid>
            <quantity>1</quantity>
            <unit>Each</unit>
            <price>100</price>
            <locationid>1</locationid>
            <relateddockey>14</relateddockey>
            <relateddoclinekey>24</relateddoclinekey>
        </sotransitem>
        <sotransitem>
            <itemid>A003</itemid>
            <itemdesc>Desktop-Asus</itemdesc>
            <warehouseid>1</warehouseid>
            <quantity>20</quantity>
            <unit>Each</unit>
            <price>160</price>
            <locationid>1</locationid>
            <relateddockey>14</relateddockey>
            <conversiontype>Quantity</conversiontype>
        </sotransitem>
    </sotransitems>
</create_sotransaction>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| transactiontype | Required | string | Transaction definition to use. |
| datecreated | Required | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Transaction date |
| dateposted | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | GL posting date |
| createdfrom | Optional | string | Order Entry transaction document number to convert from |
| customerid | Required | String | Customer ID |
| documentno | Optional | string | Document number. Leave blank to use auto numbering if set in definition |
| origdocdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Original document date |
| referenceno | Optional | string | Reference number |
| termname | Optional | string | Payment term. Required if not using `datedue`. |
| datedue | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Due date. Required if not using `termname`. |
| message | Optional | string | Message |
| shippingmethod | Optional | string | Shipping method |
| shipto | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.shipto) | Ship to contact |
| billto | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.billto) | Bill to contact |
| supdocid | Optional | string | Attachments ID |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| vsoepricelist | Optional | string | VSOE price list |
| customfields | Optional | array of `customfield` | Custom fields |
| state | Optional | string | Action.
*   `Draft`
*   `Pending`
*   `Closed`

Default depends on transaction definition configuration. |
| projectid | Optional | String | Project ID |
| changelognumber | Optional | integer | Log number for tracking the number of changes applied to a source transaction. When you create a source transaction, its `changelognumber` is set to 0 by default. Then, each time you submit a change transaction against it, the number on the source is incremented. When you create a change transaction, it’s `changelognumber` is set to 1 by default. (Default: 0 for a source transaction, 1 for a change transaction) (Construction subscription) |
| needbydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Need by date for shipping, which is when the customer needs the goods to arrive on their premises. (Default: Date due) |
| shipbydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Ship by date, which is the date the shipment must go out in order to arrive when the customer needs it (`needbydate`). This date will be automatically calculated based on the `needbydate` and the estimated days in transit value specified as part of the shipping method in the Sage Intacct UI. You can provide your own value to override the calculated one. (Default: Automatically calculated value) |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Cancel after date for shipping, which is the date when the transaction should be canceled if it has not already shipped. |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Do not ship before date. |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Do not ship after date. |
| servicedeliverydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Service delivery date when any related services, such as installation or customization, are scheduled. |
| trackingnumber | optional | String | Tracking number. If goods are shipped in multiple shipments, you can enter multiple numbers separated by a comma with no spaces. |
| shippeddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Shipped date, which specifies when the shipment went out. |
| customerponumber | optional | String | Customer’s purchase order number |
| scope | Optional | string | Details about the expected scope of work to be performed or materials to be delivered. Use 4000 or fewer characters. (Construction subscription) |
| inclusions | Optional | string | Details related to items that are explicitly included in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| exclusions | Optional | string | Details related to items that are explicitly excluded in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| terms | Optional | string | Additional terms or performance obligations. Use 4000 or fewer characters. (Construction subscription) |
| schedulestartdate | Optional | date | Scheduled start date in the `mm/dd/yyyy` format (Construction subscription) |
| actualstartdate | Optional | date | Actual start date in the `mm/dd/yyyy` format (Construction subscription) |
| scheduledcompletiondate | Optional | date | Original scheduled date for completion of the work in the `mm/dd/yyyy` format (Construction subscription) |
| reverseconversion | Optional | Boolean | Indicates whether a line is a reverse conversion for entries of non-inventory items. Items set as available for dropship, but-to-order, or stockable kits are not eligible for reverse conversion. Must be opposite sign used in the original entry.

*   `false` (default)
*   `true`

 |
| revisedcompletiondate | Optional | date | Revised completion date for the work (caused by changes). Specified in the `mm/dd/yyyy` format. (Construction subscription) |
| substantialcompletiondate | Optional | date | Date the work is considered substantially complete in the `mm/dd/yyyy` format. Typically used as a milestone to identify when payment obligations are due. (Construction subscription) |
| actualcompletiondate | Optional | date | Date the work is actually complete in the `mm/dd/yyyy` format (Construction subscription) |
| noticetoproceed | Optional | date | Date when a formal notice to proceed was given in the `mm/dd/yyyy` format (Construction subscription) |
| responsedue | Optional | date | Date when a response is expected from an external party in the `mm/dd/yyyy` format (Construction subscription) |
| executedon | Optional | date | Date the related contract document was formally executed in the `mm/dd/yyyy` format (Construction subscription) |
| scheduleimpact | Optional | string | Details about any impacts on the current schedule. Use 100 or fewer characters. (Construction subscription) |
| internalrefno | Optional | string | Specifies an internal reference number that can be tracked separately. Use 100 or fewer characters. (Construction subscription) |
| internalinitiatedby | Optional | string | ID of the employee who initiated the transaction. (Construction subscription) |
| internalverbalby | Optional | string | ID of the employee who verbally agreed to the transaction. (Construction subscription) |
| internalissuedby | Optional | string | ID of the employee who issued the transaction. (Construction subscription) |
| internalissuedon | Optional | date | Internal issued-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalapprovedby | Optional | string | ID of the employee who approved the transaction. (Construction subscription) |
| internalapprovedon | Optional | date | Internal approved-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalsignedby | Optional | string | ID of the employee who signed for the transaction. (Construction subscription) |
| internalsignedon | Optional | date | Internal signed-on date in the `mm/dd/yyyy` format (Construction subscription) |
| internalsource | Optional | string | Internal reference source when the transaction originated from another document or workflow. Can be an internal or external source. For example, a request for information (RFI) or a project change request. Use 100 or fewer characters. (Construction subscription) |
| internalsourcerefno | Optional | string | Internal reference source number or ID when the transaction originated from another source. Can be an internal or external number. Use 100 or fewer characters. (Construction subscription) |
| externalrefno | Optional | string | External reference number for this transaction, such as one required by a vendor or customer. Use 100 or fewer characters. (Construction subscription) |
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
| projectcontractid | Optional | string | `PROJECTCONTRACTID` of the [project contract](https://developer.intacct.com/api/construction/project-contracts/#project-contracts). Required for AIA-enabled transaction definitions. You can get this value–and many of the other project contract-related values–from the project contract. |
| pcbexternalrefno | Optional | string | External reference. Value will be taken from the project contract if not provided. |
| pcbdescription | Optional | string | Contract description. Value will be taken from the project contract if not provided. |
| pcbdate | Optional | [date object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Contract date. Value will be taken from the project contract if not provided. |
| architect | Optional | string | Architect name. Value will be taken from the project contract if not provided. |
| billthroughdate | Optional | [date object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Billing through date. |
| billapplicationno | Optional | string | Billing application number. |
| orgcontractamt | Optional | string | Original contract amount. |
| retcompletedamt | Optional | string | Retainage from completed work (Construction or Projects subscription). |
| retstoredmaterials | Optional | string | Retainage amount from stored materials (Construction or Projects subscription). |
| lesspriorapplication | Optional | string | Less previous billings amount. |
| tcapmaddition | Optional | string | Total additions amount approved in prior months. |
| tcapmdeduction | Optional | string | Total deductions amount approved in prior months. |
| tcatmaddition | Optional | string | Total additions amount approved this month. |
| tcatmdeduction | Optional | string | Total deductions amount approved this month. |
| previousretainagebalance | Optional | currency | Sum of all the pending retainage amounts from the previous invoices for the project contract (Construction or Projects subscription). |
| sotransitems | Required | array of [sotransitem](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem) | Transaction lines, must have at least 1. |
| subtotals | Optional | array of [subtotal](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.subtotals.subtotal) | Subtotal lines |

`create_sotransaction.datecreated`  
`create_sotransaction.dateposted`  
`create_sotransaction.origdocdate`  
`create_sotransaction.datedue`  
`create_sotransaction.exchratedate`  
`create_sotransaction.needbydate`  
`create_sotransaction.shipbydate`  
`create_sotransaction.cancelafterdate`  
`create_sotransaction.donotshipbeforedate`  
`create_sotransaction.donotshipbafterdate`  
`create_sotransaction.servicedeliverydate`  
`create_sotransaction.pdbdate`  
`create_sotransaction.billthroughdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`create_sotransaction.shipto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Ship to contact name |

`create_sotransaction.billto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Bill to contact name |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`create_sotransaction.sotransitems.sotransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bundlenumber | Optional | string | Bundle number |
| itemid | Required | string | Item ID |
| itemaliasid | Optional | string | Alias name for the item as set up in an [item cross reference](https://developer.intacct.com/api/inventory-control/item-cross-references/) created for the customer on this transaction. |
| itemdesc | Optional | string | Item description |
| taxable | Optional | boolean | Taxable.
*   `false` - No
*   `true` - Yes

Customer must be set up for taxable. |
| warehouseid | Optional | string | Warehouse ID |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure for `quantity` |
| linelevelsimpletaxtype | Optional | string | Simple tax rate to apply at the line level. Available only if Enable subtotals and Enable line level Simple Tax are enabled for the transaction definition. |
| discountpercent | Optional | number | Discount percentage |
| price | Optional | currency | Price |
| relateddockey | Optional | integer | Record number of the source transaction when creating a change order. See the FAQ about [change orders](https://developer.intacct.com/support/faq/#trans-changes) for information about using the API to compare original values of a source transaction to revised values. (Construction subscription) |
| relateddoclinekey | Optional | integer | Record number of a source transaction line to modify when creating a change order. If you omit this parameter but supply `relateddockey`, a new line will be created on the source transaction. (Construction subscription) |
| retainagepercentage | Optional | numeric | Percentage of the total amount to retain on a transaction that is part of a Construction project. When you supply this value, the value for `trx_amountretained` is automatically calculated. (Construction or Projects subscription). |
| trx\_amountretained | Optional | currency | Amount to retain if you want to override the `retainagepercentage`. When you supply this value, the value for `retainagepercentage` is automatically calculated. (Construction or Projects subscription). |
| conversiontype | Optional | string | Conversion type to use when converting the transaction to the next step in the workflow (for example, sales order to sales invoice).

*   `Price` - conversion based on the price (for non-inventory items only)
*   `Quantity` - conversion based on the quantity and unit

If using `Price`, set `Quantity` to 1 and provide a `unit` that is a base unit (unit factor is 1). (Construction subscription) |
| sourcelinekey | Optional | integer | Source line to convert this line from. Use the `RECORDNO` of the line from the `createdfrom` transaction document. |
| discsurchargememo | Optional | string | Discount/surcharge memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| linesubtotals | Optional | array of [linesubtotal](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.linesubtotals.linesubtotal) | VAT tax overrides. To override a single tax value you must provide overrides for all taxes on the line item. |
| departmentid | Optional | string | Department ID |
| memo | Optional | string | Memo |
| itemdetails | Optional | array of [itemdetail](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.itemdetails.itemdetail) | Item details (applicable to inventory or stockable kit item types). |
| customfields | Optional | array of `customfield` | Custom fields |
| revrectemplate | Optional | string | Rev rec template ID |
| revrecstartdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Rev rec start date |
| revrecenddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Rev rec end date |
| renewalmacro | Optional | string | Renewal macro |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| paymenttaxcapture | Optional | boolean | Generate VAT tax record when transaction line is paid. (French companies and entities only)

*   `false` - No
*   `true` - Yes

 |
| contractid | Optional | string | Contract ID |
| fulfillmentstatus | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.fulfillmentstatus) | Fulfillment Status |
| taskno | Optional | string | Task `RECORDNO` |
| billingtemplate | Optional | string | Billing template |
| dropship | Optional | boolean | Drop ship.

*   `false` - No
*   `true` - Yes

 |
| shipto | Optional | string | Ship to contact name for the transaction line, which overrides the ship to contact name on the transaction. |
| needbydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Need by date for shipping, which is when the customer needs the goods to arrive on their premises. (Default: Date due) |
| shipby | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Ship by date, which is the date the first shipment needs to be sent to meet the customer’s need by date. |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Do not ship before date. |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Do not ship after date. |
| datepickticketprinted | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Date ticket printed, which is the last date this line was printed on a pick ticket. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Cancel after date for shipping, which is the date when the transaction should be canceled if it has not already shipped. |
| shippeddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Shipped date, which specifies when the shipment went out for this line. Overrides the `shippeddate` value set on the transaction header. |
| projectcontractid | Optional | string | Project contract ID. Required for AIA-enabled transaction definitions. |
| projectcontractlineid | Optional | string | Project contract line ID. Required for AIA-enabled transaction definitions. |
| pcblexternalrefno | Optional | string | External reference. |
| pcbldescription | Optional | string | Description. |
| pcblbillingtype | Optional | string | Billing type. |
| contractlinevalue | Optional | string | Contract line value. |
| priorapplicationamt | Optional | currency | Amount from prior application. |
| completedthisperiod | Optional | string | Completed amount this period. |
| storedmaterials | Optional | string | Stored materials amount. |
| percentcompletedtodate | Optional | string | Percentage completed to date. |
| previousretainagebalance | Optional | currency | Sum of all the pending retainage amounts from the project contract lines matching the previous invoices for the project contract (Construction or Projects subscription). |
| isretainagerelease | Optional | boolean | Set to `true` to indicate that the entry is a retainage release (Construction or Projects subscription). |

`create_sotransaction.sotransitems.sotransitem.linesubtotals.linesubtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| trx\_tax | Optional | number | Amount of tax for the line item (to override the calculated VAT). |
| overridedetailid | Required | string | The ID of the [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) that you want to apply to this line subtotal. If `trx_tax` is not provided, the VAT will be calculated using the percentage value set in this tax detail. |

`create_sotransaction.sotransitems.sotransitem.itemdetails.itemdetail`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| quantity | Optional | number | Quantity |
| serialno | Optional | string | Serial number. |
| lotno | Optional | string | Lot number. |
| aisle | Optional | string | Aisle |
| row | Optional | string | Row |
| bin | Optional | string | Bin |
| itemexpiration | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Item expiration |

`create_sotransaction.sotransitems.sotransitem.needbydate`  
`create_sotransaction.sotransitems.sotransitem.shipbydate`  
`create_sotransaction.sotransitems.sotransitem.donotshipbeforedate`  
`create_sotransaction.sotransitems.sotransitem.donotshipafterdate`  
`create_sotransaction.sotransitems.sotransitem.shippeddate`  
`create_sotransaction.sotransitems.sotransitem.datepickticketprinted`  
`create_sotransaction.sotransitems.sotransitem.cancelafterdate`  
`create_sotransaction.sotransitems.sotransitem.shippeddate`  
`create_sotransaction.sotransitems.sotransitem.itemdetails.itemdetail.itemexpiration`  
`create_sotransaction.sotransitems.sotransitem.fulfillmentstatus.kitstatus.deliverydate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`create_sotransaction.sotransitems.sotransitem.fulfillmentstatus`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| deliverystatus | Optional | string | Delivery status.
*   `Delivered`
*   `Undelivered`

 |
| deliverydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Delivery date |
| deferralstatus | Optional | string | Deferral status.

*   `Defer until item is delivered`
*   `Defer bundle until item is delivered`

 |
| kitstatus | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.fulfillmentstatus.kitstatus) | Kit status |

`create_sotransaction.sotransitems.sotransitem.fulfillmentstatus.kitstatus`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number |
| invoiceprice | Optional | currency | Invoice price |
| deliverystatus | Optional | string | Delivery status.
*   `Delivered`
*   `Undelivered`

 |
| deliverydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.sotransitems.sotransitem.date) | Delivery date |
| deferralstatus | Optional | string | Deferral status.

*   `Defer until item is delivered`
*   `Defer bundle until item is delivered`

 |

`create_sotransaction.subtotals.subtotal`

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

* * *

### Update Order Entry Transaction (Legacy)

[History](https://developer.intacct.com/api/order-entry/order-entry-transactions/#history-update-order-entry-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2023 Release 1 | Added fields to `sotransitem` and `updatesotransitem` to support retainage release:  
isretainagerelease |
| 2022 Release 2 | Added fields to support project contracts.  
In `update_sotransaction`:  
projectcontractid, projectcontractname, projectcontractkey, projectcontractlineid, projectcontractlinename, projectcontractlinekey, pcblexternalrefno, pcbldescription, pcblbillingtype, contractlinevalue, priorapplicationamt, completedthisperiod, storedmaterials, percentcompletedtodate  
In `update_sotransaction.sotransitems.sotransitem`:  
projectcontractid, projectcontractkey, projectcontractname, pcbexternalrefno, pcbdescription, pcbdate, architect, architectkey, billthroughdate, billapplicationno, orgcontractamt, retcompletedamt, retstoredmaterials, lesspriorapplication, tcapmaddition, tcapmdeduction, tcatmaddition, tcatmdeduction |
| 2022 Release 1 | Added linesubtotals array to allow VAT tax override |
| 2021 Release 3 | Added changelognumber, itemdetails now supports trackable kit item types |
| 2021 Release 2 | Added relateddockey, relateddoclinekey |
| 2021 Release 1 | Added conversiontype, itemaliasid |
| 2020 Release 4 | Added shipbydate, shippeddate |
| 2020 Release 3 | Added trx\_amountretained |
| 2020 Release 2 | Added parameters for Construction application |
| 2020 Release 1 | Added retainagepercentage, costtypeid |
| 2019 Release 4 | Added needbydate, cancelafterdate, donotshipbeforedate, donotshipafterdate, servicedeliverydate, datepickticketprinted, trackingnumber, customerponumber, shipby, taskid |
| 2018 Release 2 | Added linelevelsimpletaxtype |
| 2024 Release 1 | Added reverseconversion |
| 2024 Release 4 | Added or updated notes about subscription requirements for retcompletedamt, retstoredmaterials, previousretainagebalance, retainagepercentage, trx\_amountretained, and isretainagerelease |

**Note:** You cannot update an order entry transaction or order entry transaction items if the state of the order entry transaction is In Progress, Converted, or Partially Converted. For more information, see [Order Entry transaction states](https://www.intacct.com/ia/docs/en_US/help_action/Order_Entry/Using_Order_Entry/Transactions/about-order-entry-transaction-states.htm?tocpath=Applications%7COrder%20Entry%7CTransactions%7C_____7).

Before using this function to modify existing lines, make sure you know the correct line numbers. For this object, the generic `read` function uses a zero-based index for entries returned in the response. However, the object-specific update function uses a one-based index for entries you supply in the request.

After using `read` to get the line number of the entry you want to modify, add one to that number to specify the correct line in your update operation. See [Working with transaction lines and legacy functions](https://developer.intacct.com/web-services/functions/#working-with-transaction-lines-and-legacy-functions) for more information.

**Warning:** Before doing any large scale update operations, perform a test to make sure you are modifying the correct lines.

#### `update_sotransaction`

> Updates an existing line on the transaction:

```
<update_sotransaction key="Sales Order-SO1234">
    <updatesotransitems>
        <updatesotransitem line_num="1">
            <memo>Testing1234</memo>
        </updatesotransitem>
    </updatesotransitems>
</update_sotransaction>
```

> Creates a new line on the transaction:

```
<update_sotransaction key="Sales Order-SO1234">
    <updatesotransitems>
        <sotransitem>
            <itemid>R0056</itemid>
            <quantity>1</quantity>
            <unit>Each</unit>
            <price>125</price>
            <locationid>110-SJC</locationid>
        </sotransitem>
    </updatesotransitems>
</update_sotransaction>
```

> Updates an existing change order to change the quantity for an existing line (Construction subscription):

```
<update_sotransaction key="Change_Doc01-Ord#0012#doc">
    <message>update relateddoclinekey</message>
    <updatesotransitems>
        <updatesotransitem line_num="1">
            <quantity>26</quantity>
        </updatesotransitem>
    </updatesotransitems>
</update_sotransaction>
```

> Updates an existing change order so that the first line refers to a different line on the original source transaction:

```
<update_sotransaction key="Change_Doc01-Ord#0012#doc">
    <message>update relateddoclinekey for line one of this change order</message>
    <updatesotransitems>
        <updatesotransitem line_num="1">
            <price>200</price>
            <relateddockey>11</relateddockey>
            <relateddoclinekey>21</relateddoclinekey>
        </updatesotransitem>
    </updatesotransitems>
</update_sotransaction>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Document ID to update |
| disablevalidation | Optional | boolean | Disable transaction validation on update.
*   `false` - No (default)
*   `true` - Yes

 |
| datecreated | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Transaction date |
| dateposted | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | GL posting date |
| referenceno | Optional | string | Reference number |
| termname | Optional | string | Payment term. Required if not using `datedue`. |
| datedue | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Due date. Required if not using `termname`. |
| origdocdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Original document date |
| message | Optional | string | Message |
| shippingmethod | Optional | string | Shipping method |
| shipto | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.shipto) | Ship to contact |
| billto | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.billto) | Bill to contact |
| supdocid | Optional | string | Attachments ID |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| vsoepricelist | Optional | string | VSOE price list |
| customfields | Optional | array of `customfield` | Custom fields |
| state | Optional | string | Action.

*   `Draft`
*   `Pending`
*   `Closed`

Default depends on transaction definition configuration. |
| projectid | Optional | string | Project ID |
| changelognumber | Optional | integer | Log number for tracking the number of changes applied to a source transaction. When you create a source transaction, its `changelognumber` is set to 0 by default. Then, each time you submit a change transaction against it, the number on the source is incremented. When you create a change transaction, it’s `changelognumber` is set to 1 by default. (Construction subscription) |
| needbydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Need by date for shipping, which is when the customer needs the goods to arrive on their premises. (Default: Date due) |
| shipbydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Ship by date, which is the date the shipment must go out in order to arrive when the customer needs it (`needbydate`). This date will be automatically calculated based on the `needbydate` and the estimated days in transit value specified as part of the shipping method in the Sage Intacct UI. You can provide your own value to override the calculated one. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Cancel after date for shipping, which is the date when the transaction should be canceled if it has not already shipped. |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Do not ship before date. |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Do not ship after date. |
| servicedeliverydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Service delivery date when any related services, such as installation or customization, are scheduled. |
| trackingnumber | optional | String | Tracking number. If goods are shipped in multiple shipments, you can enter multiple numbers separated by a comma with no spaces. |
| shippeddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.date) | Shipped date, which specifies when the shipment went out. |
| customerponumber | optional | String | Customer purchase order number |
| scope | Optional | string | Details about the expected scope of work to be performed or materials to be delivered. Use 4000 or fewer characters. (Construction subscription) |
| inclusions | Optional | string | Details related to items that are explicitly included in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| exclusions | Optional | string | Details related to items that are explicitly excluded in the terms of this document. Use 4000 or fewer characters. (Construction subscription) |
| terms | Optional | string | Additional terms or performance obligations. Use 4000 or fewer characters. (Construction subscription) |
| schedulestartdate | Optional | date | Scheduled start date in the `mm/dd/yyyy` format (Construction subscription) |
| actualstartdate | Optional | date | Actual start date in the `mm/dd/yyyy` format (Construction subscription) |
| scheduledcompletiondate | Optional | date | Original scheduled date for completion of the work in the `mm/dd/yyyy` format (Construction subscription) |
| reverseconversion | Optional | Boolean | Indicates whether a line is a reverse conversion for entries of non-inventory items. Items set as available for dropship, but-to-order, or stockable kits are not eligible for reverse conversion. Must be opposite sign used in the original entry.

*   `false` (default)
*   `true`

 |
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
| internalsignedon | Optional | date | Internal signed-on date in the `mm/dd/yyyy` format (Construction subscription) |
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
| pcbexternalrefno | Optional | string | External reference. |
| pcbdescription | Optional | string | Contract description. |
| pcbdate | Optional | [date object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Contract date. |
| architect | Optional | string | Architect. |
| billthroughdate | Optional | [date object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#create_sotransaction.date) | Billing through date. |
| billapplicationno | Optional | string | Billing application number. |
| orgcontractamt | Optional | string | Original contract amount. |
| retcompletedamt | Optional | string | Retainage from completed work (Construction or Projects subscription). |
| retstoredmaterials | Optional | string | Retainage amount from stored materials (Construction or Projects subscription). |
| lesspriorapplication | Optional | string | Less previous billings amount. |
| tcapmaddition | Optional | string | Total additions amount approved in prior months. |
| tcapmdeduction | Optional | string | Total deductions amount approved in prior months. |
| tcatmaddition | Optional | string | Total additions amount approved this month. |
| tcatmdeduction | Optional | string | Total deductions amount approved this month. |
| updatesotransitems | Required | array of [updatesotransitem](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem) and/or [sotransitem](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.sotransitem) | To update an existing line use `updatesotransitem` otherwise to create a new line use `sotransitem`. You can mix types in the array. |
| updatesubtotals | Optional | array of [updatesubtotal](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesubtotals.updatesubtotal) | Subtotal lines |

`update_sotransaction.datecreated`  
`update_sotransaction.dateposted`  
`update_sotransaction.origdocdate`  
`update_sotransaction.datedue`  
`update_sotransaction.exchratedate`  
`update_sotransaction.needbydate`  
`update_sotransaction.shipbydate`  
`update_sotransaction.cancelafterdate`  
`update_sotransaction.donotshipbeforedate`  
`update_sotransaction.donotshipafterdate`  
`update_sotransaction.shippeddate`  
`update_sotransaction.servicedeliverydate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_sotransaction.shipto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Ship to contact name |

`update_sotransaction.billto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Bill to contact name |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`update_sotransaction.updatesotransitems.updatesotransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update. |
| bundlenumber | Optional | string | Bundle number |
| itemid | Optional | string | Item ID |
| itemaliasid | Optional | string | Alias name for the item as set up in an [item cross reference](https://developer.intacct.com/api/inventory-control/item-cross-references/) created for the customer on this transaction. |
| itemdesc | Optional | string | Item description |
| taxable | Optional | boolean | Taxable.
*   `false` - No
*   `true` - Yes

Customer must be set up for taxable. |
| warehouseid | Optional | string | Warehouse ID |
| quantity | Optional | number | Quantity |
| unit | Optional | string | Unit of measure for `quantity` |
| linelevelsimpletaxtype | Optional | string | Simple tax rate to apply at the line level. Available only if Enable subtotals and Enable line level Simple Tax are enabled for the transaction definition. |
| discountpercent | Optional | number | Discount percentage |
| price | Optional | currency | Price |
| relateddockey | Optional | integer | Record number of the source transaction when updating a change order. See the FAQ about [change orders](https://developer.intacct.com/support/faq/#trans-changes) for information about using the API to compare original values of a source transaction to revised values. (Construction subscription) |
| relateddoclinekey | Optional | integer | Record number of a source transaction line to modify when updating a change order (which must be in draft state). If you omit this parameter but supply `relateddockey`, a new line will be created on the source transaction. (Construction subscription) |
| retainagepercentage | Optional | numeric | Percentage of the total amount to retain on a transaction that is part of a Construction project. When you supply this value, the value for `trx_amountretained` is automatically calculated (Construction or Projects subscription). |
| trx\_amountretained | Optional | currency | Amount to retain if you want to override the `retainagepercentage`. When you supply this value, the value for `retainagepercentage` is automatically calculated (Construction or Projects subscription). |
| conversiontype | Optional | string | Conversion type to use when converting the transaction to the next step in the workflow (for example, sales order to sales invoice).

*   `Price` - conversion based on the price (for non-inventory items only)
*   `Quantity` - conversion based on the quantity and unit

If using `Price`, set `Quantity` to 1 and provide a `unit` that is a base unit (unit factor is 1). (Construction subscription) |
| discsurchargememo | Optional | string | Discount/surcharge memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| memo | Optional | string | Memo |
| linesubtotals | Optional | array of [linesubtotal](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.linesubtotals.linesubtotal) | VAT tax overrides. To override a single tax value you must provide overrides for all taxes on the line item. |
| itemdetails | Optional | array of [itemdetail](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.itemdetails.itemdetail) | Item details (applicable to inventory or stockable kit item types). |
| customfields | Optional | array of `customfield` | Custom fields |
| revrectemplate | Optional | string | Rev rec template ID |
| revrecstartdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Rev rec start date |
| revrecenddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Rev rec end date |
| renewalmacro | Optional | string | Renewal macro |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| paymenttaxcapture | Optional | boolean | Generate VAT tax record when transaction line is paid. (French companies and entities only)

*   `false` - No
*   `true` - Yes

 |
| contractid | Optional | string | Contract ID |
| fulfillmentstatus | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.fulfillmentstatus) | Fulfillment Status |
| taskno | Optional | string | Task `RECORDNO` |
| billingtemplate | Optional | string | Billing template |
| dropship | Optional | boolean | Drop ship.

*   `false` - No
*   `true` - Yes

 |
| shipto | Optional | string | Ship to contact name for the transaction line, which overrides the ship to contact name on the transaction. |
| needbydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Need by date for shipping, which is when the customer needs the goods to arrive on their premisis. (Default: Date due) |
| shipby | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Ship by date, which is the date the first shipment needs to be sent to meet the customer’s need by date. |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Do not ship before date. |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Do not ship after date. |
| datepickticketprinted | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Date ticket printed, which is the last date this line was printed on a pick ticket. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Cancel after date for shipping, which is the date when the transaction should be canceled if it has not already shipped. |
| shippeddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Shipped date, which specifies when the shipment went out for this line. Overrides the `shippeddate` value set on the transaction header. |
| projectcontractlineid | Optional | string | Project contract line ID. Required for AIA-enabled transaction definitions. |
| pcblexternalrefno | Optional | string | External reference. |
| pcbldescription | Optional | string | Description. |
| pcblbillingtype | Optional | string | Billing type. |
| contractlinevalue | Optional | string | Contract line value. |
| priorapplicationamt | Optional | currency | Amount from prior application. |
| completedthisperiod | Optional | string | Completed amount this period. |
| storedmaterials | Optional | string | Stored materials amount. |
| percentcompletedtodate | Optional | string | Percentage completed to date. |
| previousretainagebalance | Optional | currency | Sum of all the pending retainage amounts from the project contract lines matching the previous invoices for the project contract (Construction or Projects subscription). |
| isretainagerelease | Optional | boolean | Set to `true` to indicate that the entry is a retainage release (Construction or Projects subscription). |

`update_sotransaction.updatesotransitems.sotransitem`

New lines are added to the bottom of the list; you cannot insert a line between existing lines.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bundlenumber | Optional | string | Bundle number |
| itemid | Required | string | Item ID |
| itemaliasid | Optional | string | Alias name for the item as set up in an [item cross reference](https://developer.intacct.com/api/inventory-control/item-cross-references/) created for the customer on this transaction. |
| itemdesc | Optional | string | Item description |
| taxable | Optional | boolean | Taxable.
*   `false` - No
*   `true` - Yes

Customer must be set up for taxable. |
| warehouseid | Optional | string | Warehouse ID |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure for `quantity` |
| linelevelsimpletaxtype | Optional | string | Simple tax rate to apply at the line level. Available only if Enable subtotals and Enable line level Simple Tax are enabled for the transaction definition. |
| discountpercent | Optional | number | Discount percentage |
| price | Optional | currency | Price |
| relateddockey | Optional | integer | Record number of the source transaction when creating a change order. See the FAQ about [change orders](https://developer.intacct.com/support/faq/#trans-changes) for information about using the API to compare original values of a source transaction to revised values. (Construction subscription) |
| relateddoclinekey | Optional | integer | Record number of a source transaction line to modify when creating a change order. If you omit this parameter but supply `relateddockey`, a new line will be created on the source transaction. (Construction subscription) |
| retainagepercentage | Optional | numeric | Percentage of the total amount to retain on a transaction. When you supply this value, the value for `trx_amountretained` is automatically calculated. (Construction subscription) |
| trx\_amountretained | Optional | currency | Amount to retain if you want to override the `retainagepercentage`. When you supply this value, the value for `retainagepercentage` is automatically calculated (Construction or Projects subscription). |
| conversiontype | Optional | string | Conversion type to use when converting the transaction to the next step in the workflow (for example, sales order to sales invoice).

*   `Price` - conversion based on the price (for non-inventory items only)
*   `Quantity` - conversion based on the quantity and unit

If using `Price`, set `Quantity` to 1 and provide a `unit` that is a base unit (unit factor is 1). (Construction subscription) |
| sourcelinekey | Optional | integer | Source line to convert this line from. Use the `RECORDNO` of the line from the `createdfrom` transaction document. |
| discsurchargememo | Optional | string | Discount/surcharge memo |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| linesubtotals | Optional | array of [linesubtotal](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.linesubtotals.linesubtotal) | VAT tax overrides. To override a single tax value you must provide overrides for all taxes on the line item. |
| departmentid | Optional | string | Department ID |
| memo | Optional | string | Memo |
| itemdetails | Optional | array of [itemdetail](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.itemdetails.itemdetail) | Item details (applicable to inventory or stockable kit item types). |
| customfields | Optional | array of `customfield` | Custom fields |
| revrectemplate | Optional | string | Rev rec template ID |
| revrecstartdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Rev rec start date |
| revrecenddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Rev rec end date |
| renewalmacro | Optional | string | Renewal macro |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| fulfillmentstatus | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.fulfillmentstatus) | Fulfillment Status |
| taskno | Optional | string | Task `RECORDNO` |
| billingtemplate | Optional | string | Billing template |
| dropship | Optional | boolean | Drop ship.

*   `false` - No
*   `true` - Yes

 |
| shipto | Optional | string | Ship to contact name for the transaction line, which overrides the ship to contact name on the transaction. |
| needbydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Need by date for shipping, which is when the customer needs the goods to arrive on their premises. (Default: Date due) |
| shipby | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Ship by date, which is the date the first shipment needs to be sent to meet the customer’s need by date. |
| donotshipbeforedate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Do not ship before date. |
| donotshipafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Do not ship after date. |
| datepickticketprinted | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Date ticket printed, which is the last date this line was printed on a pick ticket. |
| cancelafterdate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Cancel after date for shipping, which is the date when the transaction should be canceled if it has not already shipped. |
| shippeddate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Shipped date, which specifies when the shipment went out for this line. Overrides the `shippeddate` value set on the transaction. |
| projectcontractlineid | Optional | string | Project contract line ID. Required for AIA-enabled transaction definitions. |
| pcblexternalrefno | Optional | string | External reference. |
| pcbldescription | Optional | string | Description. |
| pcblbillingtype | Optional | string | Billing type. |
| contractlinevalue | Optional | string | Contract line value. |
| priorapplicationamt | Optional | currency | Amount from prior application. |
| completedthisperiod | Optional | string | Completed amount this period. |
| storedmaterials | Optional | string | Stored materials amount. |
| percentcompletedtodate | Optional | string | Percentage completed to date. |
| previousretainagebalance | Optional | currency | Sum of all the pending retainage amounts from the project contract lines matching the previous invoices for the project contract. |
| isretainagerelease | Optional | boolean | Set to `true` to indicate that the entry is a retainage release (Construction or Projects subscription). |

`update_sotransaction.updatesotransitems.sotransitem.linesubtotals.linesubtotal`  
`update_sotransaction.updatesotransitems.updatesotransitem.linesubtotals.linesubtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| trx\_tax | Optional | number | Amount of tax for the line item (to override the calculated VAT). |
| overridedetailid | Required | string | The ID of the [tax detail](https://developer.intacct.com/api/sales-tax-vat-gst/tax-details/) that you want to apply to this line subtotal. If `trx_tax` is not provided, the VAT will be calculated using the percentage value set in this tax detail. |

`update_sotransaction.updatesotransitems.sotransitem.itemdetails.itemdetail`  
`update_sotransaction.updatesotransitems.updatesotransitem.itemdetails.itemdetail`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| quantity | Optional | number | Quantity |
| serialno | Optional | string | Serial number. |
| lotno | Optional | string | Lot number. |
| aisle | Optional | string | Aisle |
| row | Optional | string | Row |
| bin | Optional | string | Bin |
| itemexpiration | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.itemdetails.itemdetail.itemexpiration) | Item expiration |

`update_sotransaction.updatesotransitems.sotransitem.itemdetails.itemdetail.itemexpiration`  
`update_sotransaction.updatesotransitems.updatesotransitem.itemdetails.itemdetail.itemexpiration`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_sotransaction.updatesotransitems.sotransitem.fulfillmentstatus`  
`update_sotransaction.updatesotransitems.updatesotransitem.fulfillmentstatus`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| deliverystatus | Optional | string | Delivery status.
*   `Delivered`
*   `Undelivered`

 |
| deliverydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Delivery date |
| deferralstatus | Optional | string | Deferral status.

*   `Defer until item is delivered`
*   `Defer bundle until item is delivered`

 |
| kitstatus | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.fulfillmentstatus.kitstatus) | Kit status |

`update_sotransaction.updatesotransitems.sotransitem.fulfillmentstatus.kitstatus`  
`update_sotransaction.updatesotransitems.updatesotransitem.fulfillmentstatus.kitstatus`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number |
| invoiceprice | Optional | currency | Invoice price |
| deliverystatus | Optional | string | Delivery status.
*   `Delivered`
*   `Undelivered`

 |
| deliverydate | Optional | [object](https://developer.intacct.com/api/order-entry/order-entry-transactions/#update_sotransaction.updatesotransitems.updatesotransitem.date) | Delivery date |
| deferralstatus | Optional | string | Deferral status.

*   `Defer until item is delivered`
*   `Defer bundle until item is delivered`

 |

`update_sotransaction.updatesotransitems.sotransitem.deliverydate`  
`update_sotransaction.updatesotransitems.sotransitem.needbydate`  
`update_sotransaction.updatesotransitems.sotransitem.shipbydate`  
`update_sotransaction.updatesotransitems.sotransitem.shipby`  
`update_sotransaction.updatesotransitems.sotransitem.donotshipbeforedate`  
`update_sotransaction.updatesotransitems.sotransitem.donotshipafterdate`  
`update_sotransaction.updatesotransitems.sotransitem.datepickticketprinted`  
`update_sotransaction.updatesotransitems.sotransitem.cancelafterdate`  
`update_sotransaction.updatesotransitems.sotransitem.shippeddate`  
`update_sotransaction.updatesotransitems.updatesotransitem.deliverydate`  
`update_sotransaction.updatesotransitems.updatesotransitem.needbydate`  
`update_sotransaction.updatesotransitems.updatesotransitem.shipbydate`  
`update_sotransaction.updatesotransitems.updatesotransitem.shipby`  
`update_sotransaction.updatesotransitems.updatesotransitem.donotshipbeforedate`  
`update_sotransaction.updatesotransitems.updatesotransitem.donotshipafterdate`  
`update_sotransaction.updatesotransitems.updatesotransitem.datepickticketprinted`  
`update_sotransaction.updatesotransitems.updatesotransitem.cancelafterdate`  
`update_sotransaction.updatesotransitems.updatesotransitem.shippeddate`  
`update_sotransaction.updatesotransitems.sotransitem.fulfillmentstatus.deliverydate`  
`update_sotransaction.updatesotransitems.updatesotransitem.fulfillmentstatus.deliverydate`  
`update_sotransaction.updatesotransitems.sotransitem.fulfillmentstatus.kitstatus.deliverydate`  
`update_sotransaction.updatesotransitems.updatesotransitem.fulfillmentstatus.kitstatus.deliverydate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_sotransaction.updatesubtotals.updatesubtotal`

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
| costtypeid | Optional | string | Cost type. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| classid | Optional | string | Class ID |
| itemid | Optional | string | Item ID |
| contractid | Optional | string | Contract ID |

* * *

### Delete Order Entry Transaction (Legacy)

#### `delete_sotransaction`

```
<delete_sotransaction key="Sales Order-SO1234"></delete_sotransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Transaction `DOCID` to delete |

* * *

Order Entry Transaction Lines
-----------------------------

### Get Order Entry Transaction Line Object Definition

#### `lookup`

> List all the fields and relationships for the Order Entry transaction line object:

```
<lookup>
    <object>SODOCUMENTENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTENTRY` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Order Entry Transaction Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number of the transaction header plus information about each transaction line:

```
<query>
    <object>SODOCUMENTENTRY</object>
    <select>
        <field>DOCHDRNO</field>
        <field>LINE_NO</field>
        <field>ITEMID</field>
        <field>TOTAL</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTENTRY` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Order Entry Transaction Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>SODOCUMENTENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Sales Order</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get Order Entry Transaction Line

#### `read`

```
<read>
    <object>SODOCUMENTENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Sales Order</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTENTRY` |
| keys | Required | string | Comma-separated list of transaction line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

Order Entry Transaction Subtotals
---------------------------------

### Get Order Entry Transaction Subtotals Object Definition

#### `lookup`

> List all the fields and relationships for the Order Entry transaction subtotals object:

```
<lookup>
    <object>SODOCUMENTSUBTOTALS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTSUBTOTALS` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Order Entry Transaction Subtotals

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, document ID, and record number of the associated AR invoice for each Order Entry transaction:

```
<query>
    <object>SODOCUMENTSUBTOTALS</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTSUBTOTALS` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Order Entry Transaction Subtotals (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>SODOCUMENTSUBTOTALS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Sales Order</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTSUBTOTALS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get Order Entry Transaction Subtotal

#### `read`

```
<read>
    <object>SODOCUMENTSUBTOTALS</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Sales Order</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `SODOCUMENTSUBTOTALS` |
| keys | Required | string | Comma-separated list of transaction subtotal `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Sales Order`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

