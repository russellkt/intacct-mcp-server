Title: AR Payments

URL Source: https://developer.intacct.com/api/accounts-receivable/ar-payments/

Markdown Content:
*   [Get AR Payment Object Definition](https://developer.intacct.com/api/accounts-receivable/ar-payments/#get-ar-payment-object-definition)
*   [Query and List AR Payments](https://developer.intacct.com/api/accounts-receivable/ar-payments/#query-and-list-ar-payments)
*   [Query and List AR Payments (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-payments/#query-and-list-ar-payments-legacy)
*   [Get AR Payment](https://developer.intacct.com/api/accounts-receivable/ar-payments/#get-ar-payment)
*   [Create AR Payment](https://developer.intacct.com/api/accounts-receivable/ar-payments/#create-ar-payment)
*   [Update AR Payment](https://developer.intacct.com/api/accounts-receivable/ar-payments/#update-ar-payment)
*   [Delete AR Payment](https://developer.intacct.com/api/accounts-receivable/ar-payments/#delete-ar-payment)
*   [Create AR Payment (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-payments/#create-ar-payment-legacy)
*   [Apply AR Payment (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-payments/#apply-ar-payment-legacy)
*   [Reverse AR Payment (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-payments/#reverse-ar-payment-legacy)
*   [Query and List AR Payments (deprecated)](https://developer.intacct.com/api/accounts-receivable/ar-payments/#query-and-list-ar-payments-deprecated)
*   [Get AR Payment (deprecated)](https://developer.intacct.com/api/accounts-receivable/ar-payments/#get-ar-payment-deprecated)

* * *

An AR payment is a transaction used to record a payment against an AR invoice or an AR adjustment/debit memo.

An `ARPYMT` is composed of header information and one or more payment detail (`ARPYMTDETAIL`) objects. A payment detail object can specify either the invoice or debit memo as a whole (header level), or it can specify a line item. A payment detail object also provides the transaction amount that was received, and can include an inline credit or discount or advance. Note that the `ARPYMT` object does not support creating advances but is used to apply advances to invoices. Use [`ARADVANCE`](https://developer.intacct.com/api/accounts-receivable/ar-advances/) to create advances.

With `ARPYMT`, you can apply multiple credits to the same line by providing multiple payment details for that line. You can also apply credits or discounts from a different invoice (for the same customer) on the current invoice.

When a payment does not cover the total balance due on an invoice, it is applied one line at a time starting with the first line and continuing down the list as each line is paid in full. This is known as the waterfall method, and it means that you should list any high priority line items first in invoices/debit memos.

Note: The legacy `ARPAYMENT` object is still available for backwards compatibility. .

* * *

Get AR Payment Object Definition
--------------------------------

#### `lookup`

> List all the fields and relationships for the AR payment object:

```
<lookup>
    <object>ARPYMT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARPYMT` |

* * *

Query and List AR Payments
--------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number for each AR payment that doesn’t have a description:

```
<query>
    <object>ARPYMT</object>
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

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARPYMT` |
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

Query and List AR Payments (Legacy)
-----------------------------------

Lists AR payments including posted payments, advance payments, and overpayments.

#### `readByQuery`

> List AR payments:

```
<readByQuery>
    <object>ARPYMT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List overpayments:

```
<readByQuery>
    <object>ARPYMT</object>
    <query>RECORDTYPE = 'rp'</query>
    <fields>*</fields>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARPYMT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDTYPE | Optional | string | Type of the record. Use`rp` for overpayment, `rr` for AR advance payment, or `ro` for applied AR overpayment. |

* * *

Get AR Payment
--------------

#### `read`

```
<read>
    <object>ARPYMT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARPYMT` |
| keys | Required | string | Comma-separated list of payment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create AR Payment
-----------------

[History](https://developer.intacct.com/api/accounts-receivable/ar-payments/#history-create-ar-payment)

| Release | Changes |
| --- | --- |
| 2024 Release 3 | Added TRX\_TOTALDISCOUNTTOAPPLY to ARPYMTDETAIL |
| 2024 Release 2 | Added ACTION |

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create`

> Create a payment against the invoice header:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>JHC</CUSTOMERID>
        <DOCNUMBER>INV-007</DOCNUMBER>
        <RECEIPTDATE>05/15/2019</RECEIPTDATE>
        <PAYMENTDATE>05/16/2019</PAYMENTDATE>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>101</RECORDKEY>
                <TRX_PAYMENTAMOUNT>125</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Create a payment against two invoice lines:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>JHC</CUSTOMERID>
        <DOCNUMBER>INV-009</DOCNUMBER>
        <RECEIPTDATE>05/15/2019</RECEIPTDATE>
        <PAYMENTDATE>05/16/2019</PAYMENTDATE>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>100</RECORDKEY>
                <ENTRYKEY>200</ENTRYKEY>
                <TRX_PAYMENTAMOUNT>30</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
            <ARPYMTDETAIL>
                <RECORDKEY>100</RECORDKEY>
                <ENTRYKEY>201</ENTRYKEY>
                <TRX_PAYMENTAMOUNT>55</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Create a payment against the invoice header, applying an inline credit:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>JHC</CUSTOMERID>
        <DOCNUMBER>INV-005</DOCNUMBER>
        <RECEIPTDATE>05/15/2019</RECEIPTDATE>
        <PAYMENTDATE>05/16/2019</PAYMENTDATE>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>100</RECORDKEY>
                <INLINEKEY>200</INLINEKEY>
                <INLINEENTRYKEY>202</INLINEENTRYKEY>
                <TRX_INLINEAMOUNT>15</TRX_INLINEAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Create a payment to receive payment for multiple customers in a single request:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <DOCNUMBER>Multiple customers invoices</DOCNUMBER>
        <RECEIPTDATE>11/02/2022</RECEIPTDATE>
        <PAYMENTDATE>11/02/2022</PAYMENTDATE>
        <PAYERNAME>ABC LLC group payment</PAYERNAME>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>599</RECORDKEY>
                <TRX_PAYMENTAMOUNT>100</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
            <ARPYMTDETAIL>
                <RECORDKEY>615</RECORDKEY>
                <TRX_PAYMENTAMOUNT>200</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Create a draft payment:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>2</CUSTOMERID>
        <DOCNUMBER>DraftPayment01</DOCNUMBER>
        <RECEIPTDATE>03/01/2024</RECEIPTDATE>
        <PAYMENTDATE>03/01/2024</PAYMENTDATE>
        <ACTION>Draft</ACTION>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>61</RECORDKEY>
                <ENTRYKEY>285</ENTRYKEY>
                <TRX_PAYMENTAMOUNT>30</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
            <ARPYMTDETAIL>
                <RECORDKEY>61</RECORDKEY>
                <ENTRYKEY>286</ENTRYKEY>
                <TRX_PAYMENTAMOUNT>55</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Create a draft payment to receive payment for multiple customers in a single request:

```
<create>
  <ARPYMT>
      <FINANCIALENTITY>BOA</FINANCIALENTITY>
      <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
      <DOCNUMBER>DraftPayment02</DOCNUMBER>
      <PAYERNAME>Multiple customers invoices</PAYERNAME>
      <RECEIPTDATE>03/01/2024</RECEIPTDATE>
      <PAYMENTDATE>03/01/2024</PAYMENTDATE>
      <ACTION>Draft</ACTION>
      <ARPYMTDETAILS>
          <ARPYMTDETAIL>
              <RECORDKEY>61</RECORDKEY>
              <ENTRYKEY>285</ENTRYKEY>
              <TRX_PAYMENTAMOUNT>75</TRX_PAYMENTAMOUNT>
          </ARPYMTDETAIL>
          <ARPYMTDETAIL>
              <RECORDKEY>63</RECORDKEY>
              <ENTRYKEY>298</ENTRYKEY>
              <TRX_PAYMENTAMOUNT>50</TRX_PAYMENTAMOUNT>
          </ARPYMTDETAIL>
      </ARPYMTDETAILS>
  </ARPYMT>
</create>
```

> Create a payment that applies an overpayment:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>JHC</CUSTOMERID>
        <RECEIPTDATE>05/15/2019</RECEIPTDATE>
        <PAYMENTDATE>05/16/2019</PAYMENTDATE>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>347</RECORDKEY>
                <OVERPAYMENTKEY>348</OVERPAYMENTKEY>
                <TRX_POSTEDOVERPAYMENTAMOUNT>33</TRX_POSTEDOVERPAYMENTAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Create a payment against a debit memo line by applying a credit memo line:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>Customer_022</CUSTOMERID>
        <DOCNUMBER>INV-001</DOCNUMBER>
        <RECEIPTDATE>05/15/2019</RECEIPTDATE>
        <PAYMENTDATE>05/16/2019</PAYMENTDATE>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <POSADJKEY>104</POSADJKEY>
                <POSADJENTRYKEY>204</POSADJENTRYKEY>
                <ADJUSTMENTKEY>105</ADJUSTMENTKEY>
                <ADJUSTMENTENTRYKEY>205</ADJUSTMENTENTRYKEY>
                <TRX_ADJUSTMENTAMOUNT>10</TRX_ADJUSTMENTAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Create a payment involving multi-currency:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>JHC</CUSTOMERID>
        <DOCNUMBER>INV-021</DOCNUMBER>
        <EXCH_RATE_TYPE_ID>Intacct Daily Rate</EXCH_RATE_TYPE_ID>
        <RECEIPTDATE>05/15/2019</RECEIPTDATE>
        <PAYMENTDATE>05/16/2019</PAYMENTDATE>
        <AMOUNTTOPAY>15</AMOUNTTOPAY>
        <TRX_AMOUNTTOPAY>10</TRX_AMOUNTTOPAY>
        <BASECURR>USD</BASECURR>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>104</RECORDKEY>
                <TRX_PAYMENTAMOUNT>10</TRX_PAYMENTAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Apply an advance against an invoice:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Check</PAYMENTMETHOD>
        <CUSTOMERID>JHC</CUSTOMERID>
        <DOCNUMBER>0187540</DOCNUMBER>
        <RECEIPTDATE>05/15/2019</RECEIPTDATE>
        <PAYMENTDATE>05/16/2019</PAYMENTDATE>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>100</RECORDKEY>
                <ADVANCEKEY>78</ADVANCEKEY>
                <ADVANCEENTRYKEY>202</ADVANCEENTRYKEY>
                <TRX_POSTEDADVANCEAMOUNT>15</TRX_POSTEDADVANCEAMOUNT>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

> Apply a custom discount to an invoice:

```
<create>
    <ARPYMT>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
        <CUSTOMERID>2</CUSTOMERID>
        <RECEIPTDATE>03/01/2024</RECEIPTDATE>
        <PAYMENTDATE>03/01/2024</PAYMENTDATE>
        <CURRENCY>USD</CURRENCY>
        <ARPYMTDETAILS>
            <ARPYMTDETAIL>
                <RECORDKEY>12</RECORDKEY>
                <TRX_PAYMENTAMOUNT>90</TRX_PAYMENTAMOUNT>
                <TRX_TOTALDISCOUNTTOAPPLY>10</TRX_TOTALDISCOUNTTOAPPLY>
            </ARPYMTDETAIL>
        </ARPYMTDETAILS>
    </ARPYMT>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ARPYMT | Required | object | Object to create |

`ARPYMT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FINANCIALENTITY | Optional | string | Financial entity from which the payment will be paid. Can be a checking account ID or a savings account ID. Required if not using a summary (`PRBATCH`) or undeposited funds account (`UNDEPOSITEDACCOUNTNO`). |
| PAYMENTMETHOD | Required | string | Payment method. Payment method. Use `Printed Check`, `Cash`, `EFT`, `Credit Card`, `Online Charge Card`, or `Online ACH Debit`. |
| CUSTOMERID | Optional | string | Customer ID is required for receipt of payment from a single customer. To receive payments for multiple customers in a single request, omit the Customer ID and include the `PAYERNAME` in your request. |
| DOCNUMBER | Optional | string | Reference number, which can be a check number, an authorization code received from a charge card company, or a transaction number, depending on the payment method used. If receiving payment for multiple customers, add text to note that fact. |
| DESCRIPTION | Optional | string | Description for the payment |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Do not use if `EXCHANGE_RATE` is set. (Leave blank to use Intacct Daily Rate) |
| EXCHANGE\_RATE | Optional | string | Exchange rate value. Do not use if `EXCH_RATE_TYPE_ID` is set. |
| RECEIPTDATE | Required | string | Receipt date in the `mm/dd/yyyy` format. This is the date on which to post to the GL. |
| PAYMENTDATE | Optional | string | Payment date in the `mm/dd/yyyy` format when paying with a charge card. This is the date on which the transaction occurred, according to your statement. (Default: today’s date) |
| PAYERNAME | Optional | string | Name of the payer who is paying invoices on behalf of multiple customers. Required to receive payments for multiple customers in a single request. The payer name and the corresponding payment ID are displayed in AR Sales and other reports to identify multiple payments made in a single request. |
| AMOUNTOPAY | Optional | currency | For payment involving multi-currency, this is the translated payment base amount. (Amount is ignored if the payment is not cross currency.) |
| ACTION | Optional | string | Use `Draft` to receive a payment that is not yet finalized, or `Submit` to post a confirmed payment. (Default: `Submit`). |
| TRX\_AMOUNTTOPAY | Optional | currency | For payment involving multi-currency, this is the total transaction payment amount. (Amount is ignored if the payment is not cross currency.) |
| PRBATCH | Optional | string | Summary name to post into if AR is configured for user-specified summary posting Required if not using a financial entity (`FINANCIALENTITY`) or undeposited funds account (`UNDEPOSITEDACCOUNTNO`). |
| WHENPAID | Optional | string | Date when the invoice is fully paid in the `mm/dd/yyyy` format |
| CURRENCY | Required | string | Transaction currency code |
| BASECURR | Optional | string | Base currency code |
| UNDEPOSITEDACCOUNTNO | Optional | string | Undeposited funds account. Required if not using a financial entity (`FINANCIALENTITY`) or summary (`PRBATCH`). You can [record the deposit](https://developer.intacct.com/api/cash-management/deposits/#record_deposit) so that your books reflect the transfer of funds from your undeposited funds account to your bank account when you move the held payments. |
| OVERPAYMENTAMOUNT | Optional | currency | Overpayment amount recorded by the payment |
| OVERPAYMENTLOCATIONID | Optional | string | Location ID in which to receive an overpayment |
| OVERPAYMENTDEPARTMENTID | Optional | string | Department ID in which to receive an overpayment |
| BILLTOPAYTONAME | Optional | string | Customer contact name for adjustments |
| ARPYMTDETAILS | Required | `ARPYMTDETAIL[1...n]` | Details for the payment, including line items, discounts, adjustments, and so forth. |
| ONLINECARDPAYMENT | Optional | object | Online card payment fields. Use only if payment method is `Online Charge Card`. |

`ARPYMTDETAIL`

To make a simple payment against an invoice, provide the invoice `RECORDNO` as the `RECORDKEY` and specify a payment amount. To make a payment against a debit memo, use the `RECORDNO` from an `ARADJUSTMENT` as the `POSADJKEY`. You can only pay one or the other in a single payment detail. When a payment does not cover the total balance, lines are paid using the waterfall method.

To make a payment against a specific line of an invoice or debit memo, use `ENTRYKEY` or `POSADJENTRYKEY`, respectively.

When applying credits to payments, provide an `ARPYMTDETAIL` for each type of credit. Credits can be applied to the invoice/debit memo at the header level, or at the line level. When applying more than one type of credit against the same invoice or invoice line, provide an `ARPYMTDETAIL` for each type of credit.

When receiving payments for multiple customers in a single request, include payment details for each customer, including the `RECORDKEY` and `TRX_PAYMENTAMOUNT` for each payment.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDKEY | Required | integer | Record number of the invoice being paid. You can pay either an invoice or a debit memo (via `POSADJKEY`), but not both in one payment detail. |
| ENTRYKEY | Optional | integer | Record number of the line of the invoice being paid. If not supplied, lines of the invoice are paid using the waterfall method. |
| POSADJKEY | Optional | integer | Record number of a debit memo being paid. Use `readByQuery` on ARADJUSTMENT to get the key. You can pay either a debit memo or an invoice (via `RECORDKEY`), but not both in one payment detail. |
| POSADJENTRYKEY | Optional | integer | Record number of debit memo line |
| TRX\_PAYMENTAMOUNT | Optional | currency | Amount of the cash payment. Must be the full amount of the invoice or debit memo (with the discount amount calculated in) in order to apply a discount using the DISCOUNTDATE parameter. |
| ADJUSTMENTKEY | Optional | integer | Record number of a credit memo. Use `readByQuery` on ARADJUSTMENT to get the key. |
| ADJUSTMENTENTRYKEY | Optional | integer | Record number of a credit memo line to apply to the payment |
| TRX\_ADJUSTMENTAMOUNT | Optional | currency | Adjustment transaction amount to apply to the payment |
| INLINEKEY | Optional | integer | Record number of the invoice with inline credits to apply to the payment (typically from the same invoice that is being paid). Inline credits must be enabled in the AR configuration. |
| INLINEENTRYKEY | Optional | integer | Record number of the invoice line with the inline credit apply to the payment |
| TRX\_INLINEAMOUNT | Optional | currency | Inline credit amount to apply to the payment |
| ADVANCEKEY | Optional | integer | Record number of an advance to apply to the payment |
| ADVANCEENTRYKEY | Optional | integer | Record number of an advance line to apply to the payment |
| TRX\_POSTEDADVANCEAMOUNT | Optional | currency | Advance credit amount to apply to the payment |
| OVERPAYMENTKEY | Optional | integer | Record number of an overpayment to apply to the payment. To find available overpayments, use `readByQuery` on ARPYMT. |
| OVERPAYMENTENTRYKEY | Optional | integer | Record number of an overpayment line to apply to the payment |
| TRX\_POSTEDOVERPAYMENTAMOUNT | Optional | currency | Overpayment credit amount to apply to the payment |
| NEGATIVEINVOICEKEY | Optional | integer | Record number of a negative invoice to apply to the payment |
| NEGATIVEINVOICEENTRYKEY | Optional | integer | Record number of a negative invoice line to apply to the payment |
| TRX\_NEGATIVEINVOICEAMOUNT | Optional | currency | Negative invoice amount to apply to the payment |
| TRX\_TOTALDISCOUNTTOAPPLY | Optional | currency | Total amount of discount to apply. Custom discounts must be enabled in the AR configuration. Do not use if DISCOUNTDATE is set. |
| DISCOUNTDATE | Optional | string | Discount date in the `mm/dd/yyyy` format. All discounts available at this date are applied. You can supply a date in the past to access a discount whose deadline has already passed. You must provide the correct `TRX_PAYMENTAMOUNT` for the entire amount due (with the discount amount calculated in) for the discount to apply. Do not use if TRX\_TOTALDISCOUNTTOAPPLY is provided. |

`ONLINECARDPAYMENT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CARDNUM | Optional | string | Card number |
| EXPIRYDATE | Optional | string | Expiration date in the `mm/dd/yyyy` format. |
| CARDTYPE | Optional | string | Card type |
| SECURITYCODE | Optional | string | Security code |
| USEDEFAULTCARD | Optional | boolean | Use `false` for No, `true` for Yes. |

Update AR Payment
-----------------

[History](https://developer.intacct.com/api/accounts-receivable/ar-payments/#history-update-ar-payment)

| Release | Changes |
| --- | --- |
| 2024 Release 3 | Added TRX\_TOTALDISCOUNTTOAPPLY to ARPYMTDETAIL |
| 2024 Release 2 | Added this function to support draft payments |

You can only update a payment that is in draft state (D). If the payment has been submitted and completed (C), it cannot be updated.

You can update a draft payment to change the header information, add payment details, or delete payment details.

*   To update header information, include only the header fields that you want to update, like the financial entity or customer ID, without the payment details. Existing payment details are retained.
*   To update payment details, include all existing payment details in the request and provide new values for the fields that you want to update.
*   To add new payment details, include all original details in the update request plus the details that you want to add.
*   To delete payment details, include only those details that you want to keep in the update request. Payment details that are omitted are deleted.

#### `update`

> Update a draft payment to submit the payment:

```
<update>
  <ARPYMT>
      <RECORDNO>66</RECORDNO>
      <ACTION>Submit</ACTION>
  </ARPYMT>
</update>
```

> Submit a draft payment and update payment details:

```
<update>
  <ARPYMT>
      <RECORDNO>62</RECORDNO>
      <FINANCIALENTITY>BOA</FINANCIALENTITY>
      <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
      <CUSTOMERID>2</CUSTOMERID>
      <DOCNUMBER>Confirm01</DOCNUMBER>
      <RECEIPTDATE>03/01/2024</RECEIPTDATE>
      <PAYMENTDATE>03/01/2024</PAYMENTDATE>
      <ACTION>Submit</ACTION>
      <ARPYMTDETAILS>
          <ARPYMTDETAIL>
              <RECORDKEY>61</RECORDKEY>
              <ENTRYKEY>285</ENTRYKEY>
              <TRX_PAYMENTAMOUNT>85</TRX_PAYMENTAMOUNT>
          </ARPYMTDETAIL>
      </ARPYMTDETAILS>
  </ARPYMT>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ARPYMT | Required | object | Object to update |

`ARPYMT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of payment |
| FINANCIALENTITY | Optional | string | Financial entity from which the payment will be paid. Can be a checking account ID or a savings account ID. Required if not using a summary (`PRBATCH`) or undeposited funds account (`UNDEPOSITEDACCOUNTNO`). |
| PAYMENTMETHOD | Optional | string | Payment method. Payment method. Use `Printed Check`, `Cash`, `EFT`, `Credit Card`, `Online Charge Card`, or `Online ACH Debit`. |
| CUSTOMERID | Optional | string | Customer ID is required for receipt of payment from a single customer. |
| DOCNUMBER | Optional | string | Reference number, which can be a check number, an authorization code received from a charge card company, or a transaction number, depending on the payment method used. If receiving payment for multiple customers, add text to note that fact. |
| DESCRIPTION | Optional | string | Description for the payment |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Do not use if `EXCHANGE_RATE` is set. (Leave blank to use Intacct Daily Rate) |
| EXCHANGE\_RATE | Optional | string | Exchange rate value. Do not use if `EXCH_RATE_TYPE_ID` is set. |
| RECEIPTDATE | Optional | string | Receipt date in the `mm/dd/yyyy` format. This is the date on which to post to the GL. |
| PAYMENTDATE | Optional | string | Payment date in the `mm/dd/yyyy` format when paying with a charge card. This is the date on which the transaction occurred, according to your statement. (Default: today’s date) |
| ACTION | Optional | string | When a draft payment has been confirmed, use `Submit` to post the payment for processing. |
| TRX\_AMOUNTTOPAY | Optional | currency | For payment involving multi-currency, this is the total transaction payment amount. (Amount is ignored if the payment is not cross currency.) |
| PRBATCH | Optional | string | Summary name to post into if AR is configured for user-specified summary posting Required if not using a financial entity (`FINANCIALENTITY`) or undeposited funds account (`UNDEPOSITEDACCOUNTNO`). |
| WHENPAID | Optional | string | Date when the invoice is fully paid in the `mm/dd/yyyy` format |
| CURRENCY | Optional | string | Transaction currency code |
| BASECURR | Optional | string | Base currency code |
| UNDEPOSITEDACCOUNTNO | Optional | string | Undeposited funds account. Required if not using a financial entity (`FINANCIALENTITY`) or summary (`PRBATCH`). You can [record the deposit](https://developer.intacct.com/api/cash-management/deposits/#record_deposit) so that your books reflect the transfer of funds from your undeposited funds account to your bank account when you move the held payments. |
| OVERPAYMENTAMOUNT | Optional | currency | Overpayment amount recorded by the payment |
| OVERPAYMENTLOCATIONID | Optional | string | Location ID in which to receive an overpayment |
| OVERPAYMENTDEPARTMENTID | Optional | string | Department ID in which to receive an overpayment |
| BILLTOPAYTONAME | Optional | string | Customer contact name for adjustments |
| ARPYMTDETAILS | Optional | `ARPYMTDETAIL[1...n]` | Details for the payment, including line items, discounts, adjustments, and so forth. When issuing an update request, if you include payment details in your request, be sure to include all details you want to retain. If an update request includes payment details, any details that are omitted are deleted. |
| ONLINECARDPAYMENT | Optional | object | Online card payment fields. Use only if payment method is `Online Charge Card`. |

`ARPYMTDETAIL`

To make a simple payment against an invoice, provide the invoice `RECORDNO` as the `RECORDKEY` and specify a payment amount. To make a payment against a debit memo, use the `RECORDNO` from an `ARADJUSTMENT` as the `POSADJKEY`. You can only pay one or the other in a single payment detail. When a payment does not cover the total balance, lines are paid using the waterfall method.

To make a payment against a specific line of an invoice or debit memo, use `ENTRYKEY` or `POSADJENTRYKEY`, respectively.

When applying credits to payments, provide an `ARPYMTDETAIL` for each type of credit. Credits can be applied to the invoice/debit memo at the header level, or at the line level. When applying more than one type of credit against the same invoice or invoice line, provide an `ARPYMTDETAIL` for each type of credit.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDKEY | Required | integer | Record number of the invoice being paid. You can pay either an invoice or a debit memo (via `POSADJKEY`), but not both in one payment detail. |
| ENTRYKEY | Optional | integer | Record number of the line of the invoice being paid. If not supplied, lines of the invoice are paid using the waterfall method. |
| POSADJKEY | Optional | integer | Record number of a debit memo being paid. Use `readByQuery` on ARADJUSTMENT to get the key. You can pay either a debit memo or an invoice (via `RECORDKEY`), but not both in one payment detail. |
| POSADJENTRYKEY | Optional | integer | Record number of debit memo line |
| TRX\_PAYMENTAMOUNT | Optional | currency | Amount of the cash payment. Must be the full amount of the invoice or debit memo (with the discount amount calculated in) in order to apply a discount using the DISCOUNTDATE parameter. |
| ADJUSTMENTKEY | Optional | integer | Record number of a credit memo. Use `readByQuery` on ARADJUSTMENT to get the key. |
| ADJUSTMENTENTRYKEY | Optional | integer | Record number of a credit memo line to apply to the payment |
| TRX\_ADJUSTMENTAMOUNT | Optional | currency | Adjustment transaction amount to apply to the payment |
| INLINEKEY | Optional | integer | Record number of the invoice with inline credits to apply to the payment (typically from the same invoice that is being paid). Inline credits must be enabled in the AR configuration. |
| INLINEENTRYKEY | Optional | integer | Record number of the invoice line with the inline credit apply to the payment |
| TRX\_INLINEAMOUNT | Optional | currency | Inline credit amount to apply to the payment |
| ADVANCEKEY | Optional | integer | Record number of an advance to apply to the payment |
| ADVANCEENTRYKEY | Optional | integer | Record number of an advance line to apply to the payment |
| TRX\_POSTEDADVANCEAMOUNT | Optional | currency | Advance credit amount to apply to the payment |
| OVERPAYMENTKEY | Optional | integer | Record number of an overpayment to apply to the payment. To find available overpayments, use `readByQuery` on ARPYMT. |
| OVERPAYMENTENTRYKEY | Optional | integer | Record number of an overpayment line to apply to the payment |
| TRX\_POSTEDOVERPAYMENTAMOUNT | Optional | currency | Overpayment credit amount to apply to the payment |
| NEGATIVEINVOICEKEY | Optional | integer | Record number of a negative invoice to apply to the payment |
| NEGATIVEINVOICEENTRYKEY | Optional | integer | Record number of a negative invoice line to apply to the payment |
| TRX\_NEGATIVEINVOICEAMOUNT | Optional | currency | Negative invoice amount to apply to the payment |
| TRX\_TOTALDISCOUNTTOAPPLY | Optional | currency | Total amount of discount to apply. Custom discounts must be enabled in the AR configuration. Do not use if DISCOUNTDATE is set. |
| DISCOUNTDATE | Optional | string | Discount date in the `mm/dd/yyyy` format. All discounts available at this date are applied. You can supply a date in the past to access a discount whose deadline has already passed. You must provide the correct `TRX_PAYMENTAMOUNT` for the entire amount due (with the discount amount calculated in) for the discount to apply. Do not use if TRX\_TOTALDISCOUNTTOAPPLY is provided. |

`ONLINECARDPAYMENT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CARDNUM | Optional | string | Card number |
| EXPIRYDATE | Optional | string | Expiration date in the `mm/dd/yyyy` format. |
| CARDTYPE | Optional | string | Card type |
| SECURITYCODE | Optional | string | Security code |
| USEDEFAULTCARD | Optional | boolean | Use `false` for No, `true` for Yes. |

Delete AR Payment
-----------------

You can only delete payments that are in draft state (D). If the payments have been submitted and completed (C), they cannot be deleted.

### `delete`

> Delete a draft payment:

```
<delete>
  <object>ARPYMT</object>
  <keys>69</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARPYMT` |
| keys | Required | string | Comma-separated list of payment `RECORDNO` to delete. |

* * *

Create AR Payment (Legacy)
--------------------------

This function creates an `ARPYMT` object instead of the legacy `ARPAYMENT` object. It is recommended that you use the create function on the new `ARPYMT` object, which provides line level payments and credits/debits.

When you create an AR payment that is not applied to an invoice, the AR configuration for Open item/balance forward dictates how the payment is applied:

*   Open Item (most popular/default setting) - The system creates the payment as an AR Advance, leaving it unapplied
*   Balance Forward - The system creates the payment and applies it to the oldest invoices automatically

Note: It is recommended that you use `ARADVANCE` to create advances instead of this request.

**Note:** Currency (amount) values with more than 2 decimal places will be rounded to 2 decimal places to prevent data issues. Best practice is for your application to round long decimal numbers to 2 decimal places before sending them to Intacct.

#### `create_arpayment`

> Create a multi currency AR payment and apply it to an invoice:

```
<create_arpayment>
    <customerid>6</customerid>
    <paymentamount>10</paymentamount>
    <translatedamount>20</translatedamount>
    <bankaccountid>BOFA1435</bankaccountid>
    <refid>1234</refid>
    <overpaylocid></overpaylocid>
    <overpaydeptid></overpaydeptid>
    <datereceived>
        <year>2013</year>
        <month>5</month>
        <day>6</day>
    </datereceived>
    <paymentmethod>Printed Check</paymentmethod>
    <basecurr>USD</basecurr>
    <currency>CAD</currency>
    <exchratetype>Intacct Daily Rate</exchratetype>
    <arpaymentitem>
        <invoicekey>25</invoicekey>
        <amount>10</amount>
    </arpaymentitem>
</create_arpayment>
```

> Create an AR advance since the request does not contain `arpaymentitem` and the Customer Account Type is set to Open Item:

```
<create_arpayment>
    <customerid>C1234</customerid>
    <paymentamount>1000.00</paymentamount>
    <bankaccountid>BOFA1435</bankaccountid>
    <refid>1234567890</refid>
    <overpaylocid>100</overpaylocid>
    <datereceived>
        <year>2018</year>
        <month>11</month>
        <day>1</day>
    </datereceived>
    <paymentmethod>Printed Check</paymentmethod>
</create_arpayment>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customerid | Required | string | Customer ID |
| paymentamount | Required | currency | Transaction amount |
| translatedamount | Optional | currency | Base amount |
| batchkey | Optional | integer | AR payment summary record number to add this payment to. Required if not using `bankaccountid` or `undepfundsacct`. |
| bankaccountid | Optional | string | Bank account ID. Required if not using `undepfundsacct` or `batchkey`. |
| undepfundsacct | Optional | string | Undeposited funds GL account. Required if not using `bankaccountid` or `batchkey`. You can [record the deposit](https://developer.intacct.com/api/cash-management/deposits/#record_deposit) so that your books reflect the transfer of funds from your undeposited funds account to your bank account when you move the held payments. |
| refid | Optional | string | Reference number |
| overpaylocid | Optional | string | Overpayment location ID |
| overpaydeptid | Optional | string | Overpayment department ID |
| datereceived | Optional | object | Received payment date |
| paymentmethod | Optional | string | Payment method. Use `Printed Check`, `Cash`, `EFT`, `Credit Card`, `Online Charge Card`, or `Online ACH Debit`. |
| basecurr | Optional | string | Base currency code |
| currency | Optional | string | Payment currency code |
| exchratedate | Optional | object | Exchange rate date |
| exchratetype | Optional | string | Exchange rate type. Do not use if `exchrate` is set. (Leave blank to use `Intacct Daily Rate`) |
| exchrate | Optional | currency | Exchange rate value. Do not use if `exchangeratetype` is set. |
| cctype | Optional | string | Credit card type |
| authcode | Optional | string | Authorization code to use |
| arpaymentitem | Optional | object | Transactions records to apply the payment to. Element may appear 0 to N times. If 0 elements are provided, the AR module’s Customer Account Type setting will dictate how the payment is applied (see the description for the function above). |
| onlinecardpayment | Optional | object | Online card payment fields only used if `paymentmethod` is `Online Charge Card` |
| onlineachpayment | Optional | object | Online ACH payment fields only used if `paymentmethod` is `Online ACH Debit` |

`arpaymentitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| invoicekey | Required | integer | Transaction record number to apply payment to |
| amount | Required | currency | Amount to apply. This must be less than or equal to `paymentamount` element of payment. |

`onlinecardpayment`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| cardnum | Required | string | Card number |
| expirydate | Required | string | Expiration date |
| cardtype | Required | string | Card type |
| securitycode | Optional | string | Security code |
| usedefaultcard | Optional | boolean | Use `false` for No, `true` for Yes. |

`onlineachpayment`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bankname | Required | string | Bank name |
| accounttype | Required | string | Account type |
| accountnumber | Required | string | Account number |
| routingnumber | Required | string | Routing number |
| accountholder | Required | string | Account holder |
| usedefaultcard | Optional | boolean | Use `false` for No, `true` for Yes. |

* * *

Apply AR Payment (Legacy)
-------------------------

You can apply overpayments, advances, credit memos, or negative invoices using `apply_arpayment`. To do so, set the `arpaymentkey` as follows:

*   To apply an overpayment or an advance, use the `RECORDNO` from the `ARPAYMENT` object.
*   To apply a credit memo, use the `RECORDNO` from the `ARADJUSTMENT` object.
*   ​To apply a negative invoice or invoice with an inline credit, use the `RECORDNO` from the `ARINVOICE` object.

#### `apply_arpayment`

```
<apply_arpayment>
    <arpaymentkey>136</arpaymentkey>
    <paymentdate>
        <year>2013</year>
        <month>5</month>
        <day>16</day>
    </paymentdate>
    <memo>Apply AR Payment from API</memo>
    <overpaylocid></overpaylocid>
    <overpaydeptid></overpaydeptid>
    <arpaymentitems>
        <arpaymentitem>
            <invoicekey>135</invoicekey>
            <amount>10.99</amount>
        </arpaymentitem>
    </arpaymentitems>
</apply_arpayment>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| arpaymentkey | Required | integer | Payment record to apply. |
| paymentdate | Required | object | Apply payment date |
| memo | Optional | string | Memo |
| overpaylocid | Optional | string | Overpayment location ID |
| overpaydeptid | Optional | string | Overpayment department ID |
| arpaymentitems | Required | `arpaymentitem[1...n]` | Transactions records to apply the payment to |

`arpaymentitem`

You can apply the payments to an invoice or a debit memo. To do so, set the `invoicekey` as follows:

*   To apply to an invoice, use the `RECORDNO` from the `ARINVOICE` object. (This is not the `RECORDNO` from a sales invoice (`SODOCUMENT`). The `PRRECORDKEY` on `SODOCUMENT` is the `RECORDNO` on `ARINVOICE`.)
*   To apply to a debit memo, use the `RECORDNO` from the `ARADJUSTMENT`.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| invoicekey | Required | integer | Transaction record number to apply payment to |
| amount | Required | currency | Amount to apply. This must be less than or equal to `paymentamount` element of payment. |

* * *

Reverse AR Payment (Legacy)
---------------------------

#### `reverse_arpayment`

```
<reverse_arpayment key="1234">
    <datereversed>
        <year>2015</year>
        <month>06</month>
        <day>30</day>
    </datereversed>
</reverse_arpayment>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | AR payment record number to reverse |
| datereversed | Required | object | Reverse date |
| description | Optional | string | Memo |
| nsfclosedaccount | Optional | string | NSF closed account |

`datereversed`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

Query and List AR Payments (deprecated)
---------------------------------------

List AR payments including posted payments and advanced.

**Note:** This function is provided for backwards compatibility only. Use `readByQuery` on the `ARPYMT` object moving forward.

#### `readByQuery`

```
<readByQuery>
    <object>ARPAYMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARPAYMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDTYPE | Optional | string | Type of the record. Use`rp` for overpayment, `rr` for AR advance payment, or `ro` for applied AR overpayment. |

* * *

Get AR Payment (deprecated)
---------------------------

**Note:** This function is provided for backwards compatibility only. Use `read` on the `ARPYMT` object moving forward.

#### `read`

```
<read>
    <object>ARPAYMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARPAYMENT` |
| keys | Required | string | Comma-separated list of payment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

