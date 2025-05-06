Title: AP Payments

URL Source: https://developer.intacct.com/api/accounts-payable/ap-payments/

Markdown Content:
*   [AP Payments](https://developer.intacct.com/api/accounts-payable/ap-payments/#ap-payments)
    *   [Get AP Payment Object Definition](https://developer.intacct.com/api/accounts-payable/ap-payments/#get-ap-payment-object-definition)
    *   [Query and List AP Payments](https://developer.intacct.com/api/accounts-payable/ap-payments/#query-and-list-ap-payments)
    *   [Query and List AP Payments (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#query-and-list-ap-payments-legacy)
    *   [Get AP Payment](https://developer.intacct.com/api/accounts-payable/ap-payments/#get-ap-payment)
    *   [Create AP Payment](https://developer.intacct.com/api/accounts-payable/ap-payments/#create-ap-payment)
    *   [Update AP Payment](https://developer.intacct.com/api/accounts-payable/ap-payments/#update-ap-payment)
    *   [Delete AP Payment](https://developer.intacct.com/api/accounts-payable/ap-payments/#delete-ap-payment)
*   [AP Payment Details](https://developer.intacct.com/api/accounts-payable/ap-payments/#ap-payment-details)
    *   [Get AP Payment Detail Object Definition](https://developer.intacct.com/api/accounts-payable/ap-payments/#get-ap-payment-detail-object-definition)
    *   [Query and List AP Payment Details](https://developer.intacct.com/api/accounts-payable/ap-payments/#query-and-list-ap-payment-details)
    *   [Query and List AP Payment Details (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#query-and-list-ap-payment-details-legacy)
    *   [Get AP Payment Details](https://developer.intacct.com/api/accounts-payable/ap-payments/#get-ap-payment-details)
    *   [Get AP Payment (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#get-ap-payment-legacy)
    *   [Create Manual AP Payment (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#create-manual-ap-payment-legacy)
    *   [Reverse AP Payment (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#reverse-ap-payment-legacy)
*   [AP Payment Requests](https://developer.intacct.com/api/accounts-payable/ap-payments/#ap-payment-requests)
    *   [Get AP Payment Request Object Definition](https://developer.intacct.com/api/accounts-payable/ap-payments/#get-ap-payment-request-object-definition)
    *   [Query and List AP Payment Requests](https://developer.intacct.com/api/accounts-payable/ap-payments/#query-and-list-ap-payment-requests)
    *   [Query and List AP Payment Requests (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#query-and-list-ap-payment-requests-legacy)
    *   [Get AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#get-ap-payment-request-legacy)
    *   [Create AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#create-ap-payment-request-legacy)
    *   [Approve AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#approve-ap-payment-request-legacy)
    *   [Send AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#send-ap-payment-request-legacy)
    *   [Confirm AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#confirm-ap-payment-request-legacy)
    *   [Decline AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#decline-ap-payment-request-legacy)
    *   [Void AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#void-ap-payment-request-legacy)
    *   [Delete AP Payment Request (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-payments/#delete-ap-payment-request-legacy)

* * *

An AP payment is a transaction that records a payment against an AP bill or AP adjustment.

The AP payment object, `APPYMT`, gives you access to payment details for each payment entry. For example, you can apply line level credits/discounts to a payment entry through one or more payment detail objects.

The legacy payment objects, `APPAYMENT` and `APPAYMENTREQUEST` are provided for backwards compatibility.

See the AP Payment [entity relationship diagram](https://developer.intacct.com/entity-relationship-diagrams/ap-payment/) for a high level understanding of the `APPYMT` payment object.

* * *

### Get AP Payment Object Definition

#### `lookup`

> List all the fields and relationships for the AP payment object:

```
<lookup>
    <object>APPYMT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMT` |

* * *

### Query and List AP Payments

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number for each AP payment without a description:

```
<query>
    <object>APPYMT</object>
    <select>
        <field>RECORDNO</field>
    </select>
    <filter>
        <isnull>
            <field>DESCRIPTION</field>
        </isnull>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMT` |
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

### Query and List AP Payments (Legacy)

#### `readByQuery`

> List submitted payments:

```
<readByQuery>
    <object>APPYMT</object>
    <fields>*</fields>
    <query>STATE = 'S'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`). |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | State. Use `C` for Posted, `D` for Draft, `A` for Approved, `V` for voided, or `S` for Submitted. |

* * *

### Get AP Payment

#### `read`

```
<read>
    <object>APPYMT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMT` |
| keys | Required | string | Comma-separated list of payment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create AP Payment

[History](https://developer.intacct.com/api/accounts-payable/ap-payments/#history-create-ap-payment)

| Release | Changes |
| --- | --- |
| 2021 Release 1 | Added PAYMENTPROVIDER |

> Create a printed check for a bill:

```
<create>
    <APPYMT>
        <FINANCIALENTITY>CHK-BA1145</FINANCIALENTITY>
        <PAYMENTMETHOD>Printed Check</PAYMENTMETHOD>
        <VENDORID>V0001</VENDORID>
        <PAYMENTDATE>08/07/2017</PAYMENTDATE>
        <APPYMTDETAILS>
            <APPYMTDETAIL>
                <RECORDKEY>90</RECORDKEY>
                <TRX_PAYMENTAMOUNT>50.00</TRX_PAYMENTAMOUNT>
            </APPYMTDETAIL>
        </APPYMTDETAILS>
    </APPYMT>
</create>
```

When creating a payment for a bill with multiple entries, if the`TRX_PAYMENTAMOUNT` is not for the full amount of the bill, payments are applied to line items according to the Accounts Payable configuration in the Sage Intacct UI.

For a sample query that shows bills available to pay for a given vendor, see [List Bills](https://developer.intacct.com/api/accounts-payable/bills/#query-and-list-bills).

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create`

> Create a record transfer for a specific line of a bill:

```
<create>
    <APPYMT>
        <FINANCIALENTITY>CHK-BA1145</FINANCIALENTITY>
        <PAYMENTMETHOD>EFT</PAYMENTMETHOD>
        <VENDORID>V0001</VENDORID>
        <DOCNUMBER>12345</DOCNUMBER>
        <PAYMENTDATE>08/07/2017</PAYMENTDATE>
        <APPYMTDETAILS>
            <APPYMTDETAIL>
                <RECORDKEY>90</RECORDKEY>
                <ENTRYKEY>375</ENTRYKEY>
                <TRX_PAYMENTAMOUNT>50.00</TRX_PAYMENTAMOUNT>
            </APPYMTDETAIL>
        </APPYMTDETAILS>
    </APPYMT>
</create>
```

> Pay a bill with a 2-10 Net 30 term (2% discount if paid in 10 days, otherwise due in 30). The transaction payment amount must equal the bill amount minus the discount amount. For this example, the bill is 300.00 and the discount is 6.00.

```
<create>
    <APPYMT>
        <FINANCIALENTITY>CHK-BA1145</FINANCIALENTITY>
        <PAYMENTMETHOD>Printed Check</PAYMENTMETHOD>
        <VENDORID>V1000</VENDORID>
        <PAYMENTDATE>11/13/2019</PAYMENTDATE>
        <APPYMTDETAILS>
            <APPYMTDETAIL>
                <RECORDKEY>2598</RECORDKEY>
                <TRX_PAYMENTAMOUNT>294.00</TRX_PAYMENTAMOUNT>
                <DISCOUNTDATE>11/13/2019</DISCOUNTDATE>
            </APPYMTDETAIL>
        </APPYMTDETAILS>
    </APPYMT>
</create>
```

> Pay 1.00 towards line 2 of an adjustment credit memo:

```
<create>
    <APPYMT>
        <FINANCIALENTITY>CHK-BA1145</FINANCIALENTITY>
        <PAYMENTMETHOD>Printed Check</PAYMENTMETHOD>
        <VENDORID>V1000</VENDORID>
        <PAYMENTDATE>11/13/2019</PAYMENTDATE>
        <APPYMTDETAILS>
            <APPYMTDETAIL>
                <POSADJKEY>2595</POSADJKEY>
                <POSADJENTRYKEY>42962</POSADJENTRYKEY> <!-- line 2 of adjustment credit memo -->
                <TRX_PAYMENTAMOUNT>1.00</TRX_PAYMENTAMOUNT>
            </APPYMTDETAIL>
            <APPYMTDETAIL>
                <POSADJKEY>2595</POSADJKEY>
                <POSADJENTRYKEY>42962</POSADJENTRYKEY> <!-- line 2 of adjustment credit memo -->
                <ADJUSTMENTKEY>2590</ADJUSTMENTKEY>
                <ADJUSTMENTENTRYKEY>42949</ADJUSTMENTENTRYKEY> <!-- line 2 of adjustment debit memo -->
                <TRX_ADJUSTMENTAMOUNT>1.01</TRX_ADJUSTMENTAMOUNT>
            </APPYMTDETAIL>
        </APPYMTDETAILS>
    </APPYMT>
</create>
```

> Pay 1.00, plus take 2.49 from line 1 of an advance, 2.01 from an adjustment debit memo, and apply all to line 3 of the bill.

```
<create>
    <APPYMT>
        <FINANCIALENTITY>CHK-BA1145</FINANCIALENTITY>
        <PAYMENTMETHOD>Printed Check</PAYMENTMETHOD>
        <VENDORID>V1000</VENDORID>
        <PAYMENTDATE>11/04/2019</PAYMENTDATE>
        <APPYMTDETAILS>
            <APPYMTDETAIL>
                <RECORDKEY>30</RECORDKEY>
                <ENTRYKEY>60</ENTRYKEY> <!-- line 3 from bill -->
                <TRX_PAYMENTAMOUNT>1.00</TRX_PAYMENTAMOUNT>
            </APPYMTDETAIL>
            <APPYMTDETAIL>
                <RECORDKEY>30</RECORDKEY>
                <ENTRYKEY>60</ENTRYKEY> <!-- line 3 from bill -->
                <ADVANCEKEY>2584</ADVANCEKEY>
                <ADVANCEENTRYKEY>42931</ADVANCEENTRYKEY> <!-- line 1 from advance -->
                <TRX_POSTEDADVANCEAMOUNT>2.49</TRX_POSTEDADVANCEAMOUNT>
            </APPYMTDETAIL>
            <APPYMTDETAIL>
                <RECORDKEY>30</RECORDKEY>
                <ENTRYKEY>60</ENTRYKEY> <!-- line 3 from bill -->
                <ADJUSTMENTKEY>2590</ADJUSTMENTKEY>
                <ADJUSTMENTENTRYKEY>42949</ADJUSTMENTENTRYKEY> <!-- line 2 from debit memo -->
                <TRX_ADJUSTMENTAMOUNT>2.01</TRX_ADJUSTMENTAMOUNT>
            </APPYMTDETAIL>
        </APPYMTDETAILS>
    </APPYMT>
</create>
```

> Create an electronic payment for a bill using the CSI payment provider (Early Adopter program):

```
<create>
    <APPYMT>
        <FINANCIALENTITY>CHSE</FINANCIALENTITY>
        <PAYMENTPROVIDER>CSI</PAYMENTPROVIDER>
        <PAYMENTMETHOD>VCARD</PAYMENTMETHOD>
        <VENDORID>V0001</VENDORID>
        <PAYMENTDATE>08/07/2017</PAYMENTDATE>
        <APPYMTDETAILS>
            <APPYMTDETAIL>
                <RECORDKEY>90</RECORDKEY>
                <TRX_PAYMENTAMOUNT>50.00</TRX_PAYMENTAMOUNT>
            </APPYMTDETAIL>
        </APPYMTDETAILS>
    </APPYMT>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APPYMT | Required | object | Object to create |

`APPYMT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FINANCIALENTITY | Optional | string | Financial entity from which the payment will be paid. Can be omitted when creating a credit-only payment. For all other payments, provide a checking account ID, a savings account ID, or a charge card ID. |
| PAYMENTPROVIDER | Optional | string | Name of an electronic [payment provider](https://developer.intacct.com/api/accounts-payable/payment-provider-payment-method/) for your company. Requires the Outbound Payment Services subscription. (Early Adopter program) |
| PAYMENTMETHOD | Optional | string | Payment method. Can be omitted when creating a credit-only payment. For all other payments, provide one of the following:
*   `Printed Check`
*   `Joint Check` - `PAYMENTREQUESTMETHOD` must be set to `bill`
*   `Cash`
*   `EFT`
*   `Credit Card`
*   `ACH`
*   `Check Delivery`
*   `WF Check`
*   `WF Domestic ACH`
*   `WF USD Wire`

Electronic payment providers (Early Adopter program) support their own sets of [payment methods](https://developer.intacct.com/api/accounts-payable/payment-provider-payment-method/). |
| PAYMENTREQUESTMETHOD | Optional | string | Approach for paying the bill.

*   `vendorpref` - apply the preference for the vendor as specified in the Sage Intacct UI (default)
*   `vendor` - pay all bills from the vendor in one payment
*   `bill` - pay each bill from the vendor as as separate payment
*   `payto` - merge the request into one per vendor pay-to contact

 |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format `mm/dd/yyyy` (Default: payment date of the request) |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type (Default: `Intacct Daily Rate`) |
| VENDORID | Required | string | Vendor ID |
| DOCNUMBER | Optional | string | Document number, which can be the check number or the transaction number, depending on the payment method used |
| DESCRIPTION | Optional | string | Description of the payment |
| PAYMENTDATE | Required | string | Payment date in format `mm/dd/yyyy`. Parameter value is shown in `WHENCREATED` in subsequent read operations. |
| CURRENCY | Required | string | Transaction currency code |
| BASECURR | Optional | string | Base currency code |
| AMOUNTTOPAY | Optional | currency | Amount to pay in the currency of the financial entity making the payment. Only applicable when paying from a bank with a different currency than that of the transaction. |
| ACTION | Optional | string | Use `Draft` to move the payment to the outbox in the system, or `Submit` to submit/post the payment depending on the approval workflow (Default: `Submit`). |
| APPYMTDETAILS | Required | array of `APPYMTDETAIL` | Details for the payment, including transaction payment amounts, line items, discounts, adjustments, and so forth. |

`APPYMTDETAIL`

A payment detail has two parts:

*   The AP bill or AP adjustment credit memo to pay
    *   For AP bill, use `RECORDKEY` and `ENTRYKEY`
    *   For credit memo use `POSADJKEY` and `POSADJENTRYKEY`
*   Optional transactions to apply as credits
    *   For AP adjustment debit memo, use `ADJUSTMENTKEY`, `ADJUSTMENTENTRYKEY` and `TRX_ADJUSTMENTAMOUNT`
    *   For AP advance, use `ADVANCEKEY`, `ADVANCEENTRYKEY` and `TRX_POSTEDADVANCEAMOUNT`
    *   For negative AP bill, use `INLINEKEY`, `INLINEENTRYKEY` and `TRX_INLINEAMOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDKEY | Required if not using a credit memo record number | integer | Bill record number. |
| ENTRYKEY | Optional | integer | Bill line record number. Not supported for discounts. |
| POSADJKEY | Required if not using a bill record number | integer | Credit memo record number. Not supported for joint checks. |
| POSADJENTRYKEY | Optional | integer | Credit memo entry record number. |
| TRX\_PAYMENTAMOUNT | Optional | currency | Amount of the payment. Must be the full amount of the bill (with the discount amount calculated in) in order to apply a discount. |
| INLINEKEY | Optional | integer | Negative bill transaction record number. Not supported for joint checks. |
| INLINEENTRYKEY | Optional | integer | Record number of a negative line on a bill. |
| TRX\_INLINEAMOUNT | Optional | currency | Negative bill transaction amount |
| DISCOUNTDATE | Optional | string | Discount date in format `mm/dd/yyyy`. All discounts available at this date are applied. You can supply a date in the past to access a discount whose deadline has already passed. You must provide the correct `TRX_PAYMENTAMOUNT` for the entire amount due (with the discount amount calculated in) for the discount to apply. Discounts are not applied when bill lines are provided. Not supported for joint checks. |
| ADJUSTMENTKEY | Optional | integer | Adjustment transaction record number. Not supported for joint checks. |
| ADJUSTMENTENTRYKEY | Optional | integer | Adjustment transaction entry record number |
| TRX\_ADJUSTMENTAMOUNT | Optional | currency | Adjustment transaction amount |
| ADVANCEKEY | Optional | integer | Advance record number. Not supported for joint checks. |
| ADVANCEENTRYKEY | Optional | integer | Advance entry record number |
| TRX\_POSTEDADVANCEAMOUNT | Optional | currency | Posted advance transaction amount |
| CURRENCY | Optional | string | Transaction currency code |
| JOINTPAYEEPRINTAS | Optional | string | For joint checks, the value from the `APBILLJOINTPAYEE` object. |

* * *

### Update AP Payment

> Update the date for a payment:

```
<update>
    <APPYMT>
        <RECORDNO>103</RECORDNO>
        <WHENCREATED>08/09/2017</WHENCREATED>
        <APPYMTDETAILS>
            <APPYMTDETAIL>
                <RECORDKEY>90</RECORDKEY>
                <ENTRYKEY>375</ENTRYKEY>
                <TRX_PAYMENTAMOUNT>50.00</TRX_PAYMENTAMOUNT>
            </APPYMTDETAIL>
        </APPYMTDETAILS>
    </APPYMT>
</update>
```

You can only update a payment that is in Draft state (`D`). If the payment has been Submitted (`S`) or Approved (`A`), it cannot be updated.

An update to a payment replaces the entire payment at the specified record number. Before attempting to update header information or payment details, be sure to review the following tables that list required and optional fields for both `APPYMT` (header information) and `appymtdetail` (payment details). Updates that include fields other than those listed in the following tables can cause unexpected behavior or may fail.

You can update a payment to change the header information (financial entity, document number, description, or creation date) or add/delete payment details.

*   When you want to update only header information, you must also include original payment details.
*   When you want to update only details, include the record number for the payment in the header.
*   To add a payment detail, supply original payment details along with the new one.
*   To delete a payment detail, supply only the payment details you want to keep.

It is crucial that you supply payment details (as listed in the `appymtdetail` table that follows) to retain payment information. Payment details that are omitted are deleted.

For example, if you need to update header information for a payment that includes a discount, you must supply the `DISCOUNTDATE` in the payment details. If not, the discount is removed from the payment. Also note that you should not include any other discount-related fields in an update request. Only `DISCOUNTDATE` is supported (as listed in the `appymtdetail` table that follows). Sage Intacct recalculates the discount based on the provided date.

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `update`

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APPYMT | Required | object | Type of object to update |

`APPYMT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of payment. |
| FINANCIALENTITY | Optional | string | Financial entity from which the payment will be paid. Can be a checking account ID, a savings account ID, or a credit card ID. |
| PAYMENTREQUESTMETHOD | Optional | string | Approach for paying the bill.
*   `vendorpref` - apply the preference for the vendor as specified in the Sage Intacct UI (default)
*   `vendor` - pay all bills from the vendor in one payment
*   `bill` - pay each bill from the vendor as as separate payment
*   `payto` - merge the request into one per vendor pay-to contact

 |
| DOCNUMBER | Optional | string | Document number |
| DESCRIPTION | Optional | string | Description of the payment |
| WHENCREATED | Optional | string | Payment date |
| ACTION | Optional | string | Use `Draft` to move the payment to the outbox (in the Sage Intacct UI), or `Submit` to post the payment (Default: `Submit`). |
| APPYMTDETAILS | Required | array of `APPYMTDETAIL` | Details for the payment, including line items, discounts, adjustments, and so forth. The new array of payment details will replace the existing array.

*   To add a payment detail, supply all the original payment details along with the new one
*   To delete a payment detail, supply only the payment details for the ones you want to keep.

 |

`APPYMTDETAIL`

A payment detail has two parts:

*   The AP bill or AP adjustment credit memo to pay
    *   For AP bill, use `RECORDKEY` and `ENTRYKEY`
    *   For credit memo use `POSADJKEY` and `POSADJENTRYKEY`
*   Optional transactions to apply as credits
    *   For AP adjustment debit memo, use `ADJUSTMENTKEY`, `ADJUSTMENTENTRYKEY` and `TRX_ADJUSTMENTAMOUNT`
    *   For AP advance, use `ADVANCEKEY`, `ADVANCEENTRYKEY` and `TRX_POSTEDADVANCEAMOUNT`
    *   For negative AP bill, use `INLINEKEY`, `INLINEENTRYKEY` and `TRX_INLINEAMOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDKEY | Required if not using a credit memo record number | integer | Bill record number |
| ENTRYKEY | Optional | integer | Bill line record number. Not supported for discounts. |
| POSADJKEY | Required if not using a bill record number | integer | Credit memo record number |
| POSADJENTRYKEY | Optional | integer | Credit memo entry record number |
| TRX\_PAYMENTAMOUNT | Optional | currency | Amount of the payment. Must be the full amount of the bill (with the discount amount calculated in) in order to apply a discount. |
| INLINEKEY | Optional | integer | Negative bill transaction record number |
| INLINEENTRYKEY | Optional | integer | Record number of a negative line on a bill |
| TRX\_INLINEAMOUNT | Optional | currency | Negative bill transaction amount |
| DISCOUNTDATE | Optional | string | Discount date format `mm/dd/yyyy`. All discounts available at this date are applied. You can supply a date in the past to access a discount whose deadline has already passed. You must provide the correct `TRX_PAYMENTAMOUNT` for the entire amount due (with the discount amount calculated in) for the discount to apply. |
| ADJUSTMENTKEY | Optional | integer | Debit memo record number |
| ADJUSTMENTENTRYKEY | Optional | integer | Debit memo entry record number |
| TRX\_ADJUSTMENTAMOUNT | Optional | currency | Adjustment transaction amount |
| ADVANCEKEY | Optional | integer | Advance record number |
| ADVANCEENTRYKEY | Optional | integer | Advance entry record number |
| TRX\_POSTEDADVANCEAMOUNT | Optional | currency | Posted advance transaction amount |
| CURRENCY | Optional | string | Transaction currency code |
| JOINTPAYEEPRINTAS | Optional | string | For joint checks, the value from the `APBILLJOINTPAYEE` object. |

* * *

### Delete AP Payment

#### `delete`

```
<delete>
    <object>APPYMT</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMT` |
| keys | Required | string | Comma-separated list of payment `RECORDNO` to delete |

* * *

AP Payment Details
------------------

### Get AP Payment Detail Object Definition

#### `lookup`

> List all the fields and relationships for the AP payment detail object:

```
<lookup>
    <object>APPYMTDETAIL</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMTDETAIL` |

* * *

### Query and List AP Payment Details

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and payment amount for each AP payment detail:

```
<query>
    <object>APPYMTDETAIL</object>
    <select>
        <field>RECORDNO</field>
        <field>PAYMENTAMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMTDETAIL` |
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

### Query and List AP Payment Details (Legacy)

#### `readByQuery`

> List all submitted payment details:

```
<readByQuery>
    <object>APPYMTDETAIL</object>
    <fields>*</fields>
    <query>STATE = 'S'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List all payment details for adjustment debit memos:

```
<readByQuery>
    <object>APPYMTDETAIL</object>
    <fields>*</fields>
    <query>ADJUSTMENTKEY IS NOT NULL</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMTDETAIL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Optional | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`). |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | State. Use `C` for posted, `D` for Draft, `A` for Approved, `V` for voided, or `S` for Submitted |
| RECORDKEY | Optional | string | Positive AP bill |
| POSADJKEY | Optional | string | Credit memo |
| INLINEKEY | Optional | string | Negative AP bill or inline credit |
| ADJUSTMENTKEY | Optional | string | Adjustment debit memo |
| ADVANCEKEY | Optional | string | AP advance |

* * *

### Get AP Payment Details

#### `read`

```
<read>
    <object>APPYMTDETAIL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPYMTDETAIL` |
| keys | Required | string | Comma-separated list of payment detail `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get AP Payment (Legacy)

#### `read`

```
<read>
    <object>APPAYMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPAYMENT` |
| keys | Required | string | Comma-separated list of payment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Manual AP Payment (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/ap-payments/#history-create-manual-ap-payment-legacy)

| Release | Changes |
| --- | --- |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_appayment`

```
<create_appayment>
    <bankaccountid>BOFA1435</bankaccountid>
    <vendorid>1005</vendorid>
    <memo>Hello world</memo>
    <checkdate>
        <year>2016</year>
        <month>12</month>
        <day>31</day>
    </checkdate>
    <checkno>50</checkno>
    <billno>11111</billno>
    <payitems>
        <payitem>
            <glaccountno>75300</glaccountno>
            <!--<accountlabel></accountlabel>-->
            <paymentamount>1.99</paymentamount>
            <item1099></item1099>
            <departmentid></departmentid>
            <locationid></locationid>
        </payitem>
    </payitems>
</create_appayment>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bankaccountid | Optional | string | Bank account ID. Required if not using `chargecardid`. |
| chargecardid | Optional | string | Credit card ID. Required if not using `bankaccountid`. |
| vendorid | Required | string | Vendor ID |
| memo | Optional | string | Memo |
| paymentmethod | Optional | string | Payment method. Use `Printed Check`, `Manual Check`, `Joint Check`, `Cash`, `EFT`, or `Credit`. |
| checkdate | Required | object | Payment date |
| batchkey | Optional | integer | Summary record number to place this payment in |
| checkno | Required | string | Check number or payment reference number |
| billno | Optional | string | Bill reference number |
| basepaymentamount | Optional | currency | Base payment amount |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Transaction currency code |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| paymentexchratetype | Optional | string | Payment exchange rate type. (Leave blank to use `Intacct Daily Rate`) |
| payitems | Required | `payitem[1...n]` | Lines of payment. Must have at least 1. |

`checkdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`payitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Optional | string | GL account number. Required if not using `accountlabel`. |
| accountlabel | Optional | string | AP account label. Required if not using `glaccountno`. |
| paymentamount | Required | currency | Transaction amount |
| item1099 | Optional | boolean | Form 1099. Use `false` for No, `true` for Yes. Vendor must be set up for 1099s. |
| departmentid | Optional | string | Department ID |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | Customer ID |
| vendorid | Optional | string | Vendor ID |
| employeeid | Optional | string | Employee ID |
| itemid | Optional | string | Item ID |
| classid | Optional | string | Class ID |

* * *

### Reverse AP Payment (Legacy)

#### `reverse_appayment`

```
<reverse_appayment key="1234">
    <datereversed>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </datereversed>
</reverse_appayment>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | AP payment `RECORDNO` to reverse |
| datereversed | Required | object | Reverse date |
| description | Optional | string | Memo |

`datereversed`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

AP Payment Requests
-------------------

### Get AP Payment Request Object Definition

#### `lookup`

> List all the fields and relationships for the AP payment request object:

```
<lookup>
    <object>APPAYMENTREQUEST</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPAYMENTREQUEST` |

* * *

### Query and List AP Payment Requests

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and payment amount for each AP payment request:

```
<query>
    <object>APPAYMENTREQUEST</object>
    <select>
        <field>RECORDNO</field>
        <field>PAYMENTAMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPAYMENTREQUEST` |
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

### Query and List AP Payment Requests (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APPAYMENTREQUEST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPAYMENTREQUEST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AP Payment Request (Legacy)

#### `read`

```
<read>
    <object>APPAYMENTREQUEST</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APPAYMENTREQUEST` |
| keys | Required | string | Comma-separated list of request `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create AP Payment Request (Legacy)

Creating an AP payment request begins the process of selecting an existing bill to be paid.

#### `create_paymentrequest`

> Creates a simple payment request:

```
<create_paymentrequest>
    <bankaccountid>BA1143</bankaccountid>
    <vendorid>V0001</vendorid>
    <memo>Memo</memo>
    <paymentmethod>Printed Check</paymentmethod>
    <grouppayments>true</grouppayments>
    <paymentdate>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </paymentdate>
    <paymentoption>vendorpref</paymentoption>
    <paymentrequestitems>
        <paymentrequestitem>
            <key>123</key>
            <paymentamount>100.12</paymentamount>
            <credittoapply>8.12</credittoapply>
            <discounttoapply>1.21</discounttoapply>
        </paymentrequestitem>
    </paymentrequestitems>
    <documentnumber>10000</documentnumber>
    <paymentdescription>Memo</paymentdescription>
    <paymentcontact>Jim Smith</paymentcontact>
</create_paymentrequest>
```

> Creates a payment request that uses two adjustments with one bill. You compute the discount to apply based on the terms of the bill, such as 2-10net30:

```
...
<paymentrequestitems>
    <paymentrequestitem>
        <key>206</key> <!-- AP Adjustment recordno to use -->
        <paymentamount>5</paymentamount>
        <credittoapply></credittoapply>
        <discounttoapply></discounttoapply>
    </paymentrequestitem>
    <paymentrequestitem>
        <key>207</key> <!-- AP Adjustment recordno to use -->
        <paymentamount>1</paymentamount>
        <credittoapply></credittoapply>
        <discounttoapply></discounttoapply>
    </paymentrequestitem>
    <paymentrequestitem>
        <key>205</key> <!-- AP Bill recordno to pay -->
        <paymentamount>94</paymentamount>
        <credittoapply>6</credittoapply>
        <discounttoapply></discounttoapply> <!-- Amount you compute from payment term discount -->
    </paymentrequestitem>
</paymentrequestitems>
...
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bankaccountid | Optional | string | Bank account ID. Required if not using `chargecardid`. |
| chargecardid | Optional | string | Credit card ID. Required if not using `bankaccountid`. |
| vendorid | Required | string | Vendor ID |
| memo | Optional | string | Memo |
| paymentmethod | Required | string | Payment method. Use `Printed Check` for Check, `Cash` for Cash, `EFT` for Record Transfer, `Charge Card` for Charge Card, or `ACH` for ACH. |
| grouppayments | Optional | boolean | Group payments. Use `false` for No, `true` for Yes. |
| paymentdate | Required | object | Payment date |
| paymentoption | Optional | string | Merge option. Use `vendor`, `bill`, `vendorpref`. (Default: `vendor`) |
| paymentrequestitems | Required | `paymentrequestitem[1...n]` | Items to pay |
| documentnumber | Optional | string | Document number |
| paymentdescription | Optional | string | Description |
| paymentcontact | Optional | string | Notification contact name |

`paymentdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`paymentrequestitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Apply to record number |
| paymentamount | Required | currency | Amount to apply |
| credittoapply | Optional | currency | Credit to apply |
| discounttoapply | Optional | currency | Discount to apply |

* * *

### Approve AP Payment Request (Legacy)

#### `approve_appaymentrequest`

```
<approve_appaymentrequest>
    <appaymentkeys>
        <appaymentkey>1234</appaymentkey>
    </appaymentkeys>
</approve_appaymentrequest>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| appaymentkeys | Required | `appaymentkey[1...n]` | AP payment request record numbers to approve |

* * *

### Send AP Payment Request (Legacy)

This function requires the Vendor Payment Services subscription.

#### `send_appaymentrequest`

```
<send_appaymentrequest>
    <appaymentkeys>
        <appaymentkey>1234</appaymentkey>
    </appaymentkeys>
</send_appaymentrequest>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| appaymentkeys | Required | `appaymentkey[1...n]` | AP payment request `RECORDNO`(s) to send |

* * *

### Confirm AP Payment Request (Legacy)

Use this to confirm checks have been successfully printed.

#### `confirm_appaymentrequest`

```
<confirm_appaymentrequest>
    <appaymentkeys>
        <appaymentkey>1234</appaymentkey>
    </appaymentkeys>
</confirm_appaymentrequest>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| appaymentkeys | Required | `appaymentkey[1...n]` | AP payment request `RECORDNO`(s) to confirm |

* * *

### Decline AP Payment Request (Legacy)

#### `decline_appaymentrequest`

```
<decline_appaymentrequest>
    <appaymentkeys>
        <appaymentkey>1234</appaymentkey>
    </appaymentkeys>
</decline_appaymentrequest>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| appaymentkeys | Required | `appaymentkey[1...n]` | AP payment request record numbers to decline |

* * *

### Void AP Payment Request (Legacy)

#### `void_appaymentrequest`

```
<void_appaymentrequest>
    <appaymentkeys>
        <appaymentkey>1234</appaymentkey>
    </appaymentkeys>
</void_appaymentrequest>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| appaymentkeys | Required | `appaymentkey[1...n]` | AP payment request `RECORDNO`(s) to confirm |

* * *

### Delete AP Payment Request (Legacy)

#### `delete_paymentrequest`

```
<delete_paymentrequest key="1234"></delete_paymentrequest>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | AP payment request `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

