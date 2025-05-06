Title: Bank Feeds

URL Source: https://developer.intacct.com/api/cash-management/bank-feeds/

Markdown Content:
*   [Get Bank Feed Object Definition](https://developer.intacct.com/api/cash-management/bank-feeds/#get-bank-feed-object-definition)
*   [Query and List Bank Feeds](https://developer.intacct.com/api/cash-management/bank-feeds/#query-and-list-bank-feeds)
*   [Query and List Bank Feeds (Legacy)](https://developer.intacct.com/api/cash-management/bank-feeds/#query-and-list-bank-feeds-legacy)
*   [Get Bank Feed](https://developer.intacct.com/api/cash-management/bank-feeds/#get-bank-feed)
*   [Create Bank Feed](https://developer.intacct.com/api/cash-management/bank-feeds/#create-bank-feed)
*   [Delete Bank Feed](https://developer.intacct.com/api/cash-management/bank-feeds/#delete-bank-feed)

* * *

With bank feeds, you can access transaction records for bank reconciliation directly using Sage Cloud Services, or you can provide your own transaction records as XML elements.

Bank feeds are currently supported for checking account reconciliation.

When you create a bank feed, the bank transactions become available for matching against existing transactions during [reconciliation](https://developer.intacct.com/api/cash-management/checking-accounts/#create-checking-account-reconciliation).

* * *

Get Bank Feed Object Definition
-------------------------------

#### `lookup`

> List all the fields and relationships for the bank feed object:

```
<lookup>
    <object>BANKACCTTXNFEED</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTTXNFEED` |

* * *

Query and List Bank Feeds
-------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and bank account ID for each bank feed for the given date:

```
<query>
    <object>BANKACCTTXNFEED</object>
    <select>
        <field>RECORDNO</field>
        <field>FINANCIALENTITY</field>
    </select>
    <filter>
        <equalto>
            <field>FEEDDATE</field>
            <value>01/27/2020</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTTXNFEED` |
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

Query and List Bank Feeds (Legacy)
----------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>BANKACCTTXNFEED</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTTXNFEED` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Bank Feed
-------------

#### `read`

```
<read>
    <object>BANKACCTTXNFEED</object>
    <keys>91</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTTXNFEED` |
| keys | Required | string | Comma-separated list of bank feed `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Bank Feed
----------------

[History](https://developer.intacct.com/api/cash-management/bank-feeds/#history-create-bank-feed)

| Release | Changes |
| --- | --- |
| 2022 Release 1 | Added charge and payment transaction types |

You create a bank feed using one of the following approaches:

*   Set the feed type to `onl` to fetch transactions from a bank account or credit card account subscribed to Sage Cloud Services. These transactions are available for matching using the API or in the UI.
*   Set the feed type to `xml` and provide XML bank transactions directly in the create call. These transactions must be reconciled using the API only.

#### `create`

> Create a bank feed by providing bank transactions as XML elements:

```
<create>
    <BANKACCTTXNFEED>
        <FINANCIALENTITY>BOV</FINANCIALENTITY>
        <FEEDDATE>05/15/2020</FEEDDATE>
        <FEEDTYPE>xml</FEEDTYPE>
        <BANKACCTTXNRECORDS>
            <BANKACCTTXNRECORD>
                <POSTINGDATE>04/09/2020</POSTINGDATE>
                <TRANSACTIONTYPE>withdrawal</TRANSACTIONTYPE>
                <DOCTYPE>Check</DOCTYPE>
                <DOCNO>198</DOCNO>
                <AMOUNT>-184.00</AMOUNT>
                <DESCRIPTION>Office supplies</DESCRIPTION>
            </BANKACCTTXNRECORD>
            <BANKACCTTXNRECORD>
                <POSTINGDATE>04/09/2020</POSTINGDATE>
                <TRANSACTIONTYPE>withdrawal</TRANSACTIONTYPE>
                <DOCTYPE>Check</DOCTYPE>
                <DOCNO>222</DOCNO>
                <AMOUNT>-211.14</AMOUNT>
                <DESCRIPTION>Computer service call</DESCRIPTION>
            </BANKACCTTXNRECORD>
            <BANKACCTTXNRECORD>
                <POSTINGDATE>04/17/2020</POSTINGDATE>
                <TRANSACTIONTYPE>deposit</TRANSACTIONTYPE>
                <DOCTYPE>Check</DOCTYPE>
                <DOCNO>220</DOCNO>
                <AMOUNT>2000.00</AMOUNT>
                <DESCRIPTION>From account CH to account BOV</DESCRIPTION>
            </BANKACCTTXNRECORD>
        </BANKACCTTXNRECORDS>
    </BANKACCTTXNFEED>
</create>
```

> Create a bank feed by fetching transactions from the Sage Intacct banking cloud:

```
<create>
    <BANKACCTTXNFEED>
        <FINANCIALENTITY>BOA</FINANCIALENTITY>
        <FEEDDATE>05/15/2020</FEEDDATE>
        <FEEDTYPE>onl</FEEDTYPE>
    </BANKACCTTXNFEED>
</create>
```

> Create a bank feed by providing credit card transactions as XML elements:

```
<create>
    <BANKACCTTXNFEED>
        <FINANCIALENTITY>CCB</FINANCIALENTITY>
        <FEEDDATE>04/22/2020</FEEDDATE>
        <FEEDTYPE>xml</FEEDTYPE>
        <BANKACCTTXNRECORDS>
            <BANKACCTTXNRECORD>
                <POSTINGDATE>12/09/2021</POSTINGDATE>
                <TRANSACTIONTYPE>charge</TRANSACTIONTYPE>
                <DOCNO>199</DOCNO>
                <AMOUNT>-200.26</AMOUNT>
            </BANKACCTTXNRECORD>
            <BANKACCTTXNRECORD>
                <POSTINGDATE>12/10/2021</POSTINGDATE>
                <TRANSACTIONTYPE>payment</TRANSACTIONTYPE>
                <DOCNO>200</DOCNO>
                <AMOUNT>70.00</AMOUNT>
            </BANKACCTTXNRECORD>
        </BANKACCTTXNRECORDS>
    </BANKACCTTXNFEED>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BANKACCTTXNFEED | Required | object | Object to create |

`BANKACCTTXNFEED`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FINANCIALENTITY | Required | string | Bank account or credit card account ID |
| FEEDDATE | Required | Date | Feed date in format `mm/dd/yyyy` |
| FEEDTYPE | Required | string | Feed type to create. Use `xml` to provide the transactions in XML format, or use `onl` to use online bank feeds through Sage Cloud Services. |
| FILENAME | Optional | string | File name that displays in the UI when using automatch with review (`AutomatchReview`) as the reconciliation mode. |
| BANKACCTTXNRECORDS | Optional | `BANKACCTTXNRECORD[1..n]` | Bank account or credit card account transaction records. Required only if the feed type is `xml`. |

`BANKACCTTXNRECORD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TRANSACTIONID | Optional | integer | Transaction ID of the bank feed transaction. This is available only for banking cloud transactions. |
| POSTINGDATE | Optional | date | Transaction posting date in format `mm/dd/yyyy` |
| TRANSACTIONTYPE | Required | string | Transaction type. Use `withdrawal` or `deposit` for a bank account, or `charge` or `payment` for a credit card account. |
| DOCTYPE | Optional | string | Document type |
| DOCNO | Optional | string | Document number |
| PAYEE | Optional | string | Payee |
| AMOUNT | Required | currency | Transaction amount. For a withdrawal, use a negative number. |
| DESCRIPTION | Optional | string | Description |
| CURRENCY | Optional | string | Currency |

* * *

Delete Bank Feed
----------------

You can delete a bank feed object created with a feed type of `xml` if the transactions have not yet been reconciled. You cannot delete an online bank feed from Sage Cloud Services.

```
<delete>
    <object>BANKACCTTXNFEED</object>
    <keys>91</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `BANKACCTTXNFEED` |
| keys | Required | string | Comma-separated list of record number of the `xml` bank feed |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

