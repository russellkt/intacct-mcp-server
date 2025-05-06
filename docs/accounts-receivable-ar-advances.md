Title: AR Advances

URL Source: https://developer.intacct.com/api/accounts-receivable/ar-advances/

Markdown Content:
*   [Get AR Advance Object Definition](https://developer.intacct.com/api/accounts-receivable/ar-advances/#get-ar-advance-object-definition)
*   [Query and List AR Advances](https://developer.intacct.com/api/accounts-receivable/ar-advances/#query-and-list-ar-advances)
*   [Query and List AR Advances (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-advances/#query-and-list-ar-advances-legacy)
*   [Get AR Advance](https://developer.intacct.com/api/accounts-receivable/ar-advances/#get-ar-advance)
*   [Create AR Advance](https://developer.intacct.com/api/accounts-receivable/ar-advances/#create-ar-advance)
*   [Update AR Advance](https://developer.intacct.com/api/accounts-receivable/ar-advances/#update-ar-advance)

* * *

AR advances let you receive customer advance payments before creating an invoice, such as if a customer sends you a retainer.

The Accounts Receivable configuration can be set to post advances to automatically created payment summaries (one per advance, daily, or monthly) or to existing summaries.

Use [`ARPYMT`](https://developer.intacct.com/api/accounts-receivable/ar-payments/) to apply advances against invoices after invoices are created.

* * *

Get AR Advance Object Definition
--------------------------------

#### `lookup`

> List all the fields and relationships for the AR advance object:

```
<lookup>
    <object>ARADVANCE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADVANCE` |

* * *

Query and List AR Advances
--------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List each advance for a specified customer:

```
<query>
    <object>ARADVANCE</object>
    <select>
        <field>RECORDNO</field>
    </select>
    <filter>
        <equalto>
            <field>CUSTOMERNAME</field>
            <value>Acme Inc.</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADVANCE` |
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

Query and List AR Advances (Legacy)
-----------------------------------

#### `readByQuery`

> List each advance for a specified customer:

```
<readByQuery>
    <object>ARADVANCE</object>
    <fields>*</fields>
    <query>CUSTOMERNAME = 'Acme Inc'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADVANCE` |
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

Get AR Advance
--------------

#### `read`

```
<read>
    <object>ARADVANCE</object>
    <keys>1486</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARADVANCE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the AR advance to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create AR Advance
-----------------

[History](https://developer.intacct.com/api/accounts-receivable/ar-advances/#history-create-ar-advance)

| Release | Changes |
| --- | --- |
| 2023 Release 3 | Added PRBATCHKEY |

#### `create`

> Create a cash advance payment:

```
<create>
  <ARADVANCE>
    <CUSTOMERID>C-00053</CUSTOMERID>
    <PAYMENTDATE>09/12/2021</PAYMENTDATE>
    <RECEIPTDATE>09/12/2021</RECEIPTDATE>
    <PAYMENTMETHOD>Cash</PAYMENTMETHOD>
    <UNDEPOSITEDACCOUNTNO>1020</UNDEPOSITEDACCOUNTNO>
    <ARADVANCEITEMS>
      <ARADVANCEITEM>
        <ACCOUNTLABEL>Misc Sales</ACCOUNTLABEL>
        <TRX_AMOUNT>9.18</TRX_AMOUNT>
      </ARADVANCEITEM>
    </ARADVANCEITEMS>
  </ARADVANCE>
</create>
```

> Create an advance and post it to an existing summary:

```
<create>
  <ARADVANCE>
    <PRBATCH>Advances(Bank-CHK0001): 2021/09/10 Batch</PRBATCH>
    <FINANCIALENTITY>CHK0001</FINANCIALENTITY>
    <PAYMENTMETHOD>Printed Check</PAYMENTMETHOD>
    <CUSTOMERID>C-00054</CUSTOMERID>
    <DOCNUMBER>Advance01</DOCNUMBER>
    <DESCRIPTION>Contract startup</DESCRIPTION>
    <RECEIPTDATE>09/10/2021</RECEIPTDATE>
    <PAYMENTDATE>09/10/2021</PAYMENTDATE>
    <ARADVANCEITEMS>
      <ARADVANCEITEM>
        <ACCOUNTNO>4055</ACCOUNTNO>
        <ACCOUNTLABEL>Misc Sales</ACCOUNTLABEL>
        <TRX_AMOUNT>1000</TRX_AMOUNT>
        <LOCATIONID>CA</LOCATIONID>
      </ARADVANCEITEM>
    </ARADVANCEITEMS>
  </ARADVANCE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `ARADVANCE` | Required | object | Type of object to create |

`ARADVANCE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CUSTOMERID | Required | string | ID of the customer who paid the advance. |
| PAYMENTMETHOD | Required | string | Payment method used for the advance. Use `Printed Check`, `Cash`, `EFT`, or `Credit Card`. |
| PAYMENTDATE | Required | string | Date the advance payment was made, in the mm/dd/yyyy format. |
| RECEIPTDATE | Required | string | Receipt date in the mm/dd/yyyy format. If automatic summaries are enabled, this is the date on which the advance will be posted to the General Ledger. |
| FINANCIALENTITY | Optional | string | ID of the checking or savings account to deposit the funds to. A `create` request must contain `FINANCIALENTITY` or `UNDEPOSITEDACCOUNTNO` when automatic summaries are enabled. |
| UNDEPOSITEDACCOUNTNO | Optional | string | Undeposited funds account number. A `create` request must contain `FINANCIALENTITY` or `UNDEPOSITEDACCOUNTNO` when automatic summaries are enabled. |
| PRBATCH | Optional | string | Name of the summary to post to. A request must contain either `PRBATCH` or `PRBATCHKEY` if AR is configured for user-specified summary posting. Ignored if automatic summaries are enabled. (If values for both `PRBATCHKEY` and `PRBATCH` are included in your request and those values indicate different summaries, Sage Intacct posts to the summary identified by `PRBATCHKEY`.) |
| PRBATCHKEY | Optional | string | Key (`RECORDNO`) of the summary to post to. A request must contain either `PRBATCH` or `PRBATCHKEY` if AR is configured for user-specified summary posting. Ignored if automatic summaries are enabled. (If values for both `PRBATCHKEY` and `PRBATCH` are included in your request and those values indicate different summaries, Sage Intacct posts to the summary identified by `PRBATCHKEY`.) |
| DOCNUMBER | Optional | string | Reference number such as a check number, an authorization code received from a charge card company, or a transaction number. |
| DESCRIPTION | Optional | string | Description of the advance. |
| CURRENCY | Optional | string | Transaction currency code. |
| BASECURR | Optional | string | Base currency code. |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format mm/dd/yyyy. |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Do not use if `EXCHANGE_RATE` is set. (Leave blank to use Intacct Daily Rate.) |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value. Do not use if `EXCH_RATE_TYPE_ID` is set. |
| SUPDOCID | Optional | string | Attachments ID. |
| ACTION | Optional | string | Action to execute on create. Use `Submit` or `Draft`. (Default: Submit) |
| ARADVANCEITEMS | Required | `ARADVANCEITEM[1...n]` | Advance lines, must have at least 1. |

`ARADVANCEITEM`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTNO | Optional | string | GL account number. Required if AR configuration is not set to Enable account labels. |
| ACCOUNTLABEL | Optional | string | AR account label. Required if AR configuration is set to Enable account labels. |
| TRX\_AMOUNT | Required | currency | Transaction amount of line |
| ENTRYDESCRIPTION | Optional | string | Memo |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID. Only available when the parent `PROJECTID` is also specified. |
| CUSTOMERID | Optional | string | Customer ID. Must be the same as the `CUSTOMERID` in the `ARADVANCE` object, or a child of that customer ID. |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CLASSID | Optional | string | Class ID |
| CONTRACTID | Optional | string | Contract ID |
| WAREHOUSEID | Optional | string | Warehouse ID |
| GLDIM\* | Optional | integer | User defined dimension id field. UDD object integration name usually appended to GLDIM |

* * *

Update AR Advance
-----------------

[History](https://developer.intacct.com/api/accounts-receivable/ar-advances/#history-update-ar-advance)

| Release | Changes |
| --- | --- |
| 2023 Release 3 | Added PRBATCHKEY |

When updating header information of an AR advance, you do not need to include all the original advance lines.

You can also modify, add, or delete lines as part of your update:

*   To add an advance line, supply all the original lines along with the new one.
*   To delete a line, supply only the lines that you want to keep.
*   To modify a line, supply all the original lines and change the field values you want.

#### `update`

> Update header information only:

```
<update>
    <ARADVANCE>
        <RECORDNO>1479</RECORDNO>
        <DESCRIPTION>Updated description</DESCRIPTION>
    </ARADVANCE>
</update>
```

> Add a second line to an existing AR advance:

```
<update>
    <ARADVANCE>
        <RECORDNO>1479</RECORDNO>
        <ARADVANCEITEMS>
            <ARADVANCEITEM>
                <ACCOUNTNO>4055</ACCOUNTNO>
                <ACCOUNTLABEL>Misc Sales</ACCOUNTLABEL>
                <TRX_AMOUNT>1000</TRX_AMOUNT>
                <ENTRYDESCRIPTION>line1</ENTRYDESCRIPTION>
                <LOCATIONID>CA</LOCATIONID>
            </ARADVANCEITEM>
            <ARADVANCEITEM>
                <ACCOUNTNO>4000.01</ACCOUNTNO>
                <ACCOUNTLABEL>Misc Sales</ACCOUNTLABEL>
                <TRX_AMOUNT>900</TRX_AMOUNT>
                <ENTRYDESCRIPTION>line2</ENTRYDESCRIPTION>
                <LOCATIONID>CA</LOCATIONID>
            </ARADVANCEITEM>
        </ARADVANCEITEMS>
    </ARADVANCE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `ARADVANCE` | Required | object | Type of object to update. |

`ARADVANCE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | `RECORDNO` of the AR Advance to update |
| PAYMENTMETHOD | Optional | string | Payment method used for the advance. Use `Printed Check`, `Cash`, `EFT`, `Credit Card`. |
| PAYMENTDATE | Optional | string | Date the advance payment was made, in the mm/dd/yyyy format. |
| RECEIPTDATE | Optional | string | Receipt date in the mm/dd/yyyy format. If automatic summaries are enabled, this is the date on which the advance will be posted to the General Ledger. |
| FINANCIALENTITY | Optional | string | ID of the checking or savings account to deposit the funds to. A `create` request must contain `FINANCIALENTITY` or `UNDEPOSITEDACCOUNTNO` when automatic summaries are enabled. |
| UNDEPOSITEDACCOUNTNO | Optional | string | Undeposited funds account number. A `create` request must contain `FINANCIALENTITY` or `UNDEPOSITEDACCOUNTNO` when automatic summaries are enabled. |
| PRBATCH | Optional | string | Name of the summary to post to. A request must contain either `PRBATCH` or `PRBATCHKEY` if AR is configured for user-specified summary posting. Ignored if automatic summaries are enabled. (If values for both `PRBATCHKEY` and `PRBATCH` are included in your request and those values indicate different summaries, Sage Intacct posts to the summary identified by `PRBATCHKEY`.) |
| PRBATCHKEY | Optional | string | Key (`RECORDNO`) of the summary to post to. A request must contain either `PRBATCH` or `PRBATCHKEY` if AR is configured for user-specified summary posting. Ignored if automatic summaries are enabled. (If values for both `PRBATCHKEY` and `PRBATCH` are included in your request and those values indicate different summaries, Sage Intacct posts to the summary identified by `PRBATCHKEY`.) |
| DOCNUMBER | Optional | string | Reference number such as a check number, an authorization code received from a charge card company, or a transaction number. |
| DESCRIPTION | Optional | string | Description of the advance. |
| CURRENCY | Optional | string | Transaction currency code. |
| BASECURR | Optional | string | Base currency code. |
| EXCH\_RATE\_DATE | Optional | string | Exchange rate date in format mm/dd/yyyy. |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Do not use if `EXCHANGE_RATE` is set. (Leave blank to use Intacct Daily Rate.) |
| EXCHANGE\_RATE | Optional | currency | Exchange rate value. Do not use if `EXCH_RATE_TYPE_ID` is set. |
| SUPDOCID | Optional | string | Attachments ID. |
| ARADVANCEITEMS | Required | `ARADVANCEITEM[1...n]` | Advance lines. To add an advance line, supply all the original lines along with the new one. To delete a line, supply only the lines that you want to keep. To modify a line, supply all the original lines and change the field values you want. |

`ARADVANCEITEM`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTNO | Optional | string | GL account number. Required if AR configuration is not set to Enable account labels. |
| ACCOUNTLABEL | Optional | string | AR account label. Required if AR configuration is set to Enable account labels. |
| TRX\_AMOUNT | Required | currency | Transaction amount of line |
| ENTRYDESCRIPTION | Optional | string | Memo |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID. Only available when the parent `PROJECTID` is also specified. |
| CUSTOMERID | Optional | string | Customer ID. Must be the same as the `CUSTOMERID` in the `ARADVANCE` object, or a child of that customer ID. |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CLASSID | Optional | string | Class ID |
| CONTRACTID | Optional | string | Contract ID |
| WAREHOUSEID | Optional | string | Warehouse ID |
| GLDIM\* | Optional | integer | User defined dimension id field. UDD object integration name usually appended to GLDIM |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

