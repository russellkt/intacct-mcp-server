Title: General Ledger Details

URL Source: https://developer.intacct.com/api/general-ledger/general-ledger-detail/

Markdown Content:
*   [Get General Ledger Detail Object Definition](https://developer.intacct.com/api/general-ledger/general-ledger-detail/#get-general-ledger-detail-object-definition)
*   [Query and List General Ledger Details](https://developer.intacct.com/api/general-ledger/general-ledger-detail/#query-and-list-general-ledger-details)
*   [Query and List General Ledger Details (Legacy)](https://developer.intacct.com/api/general-ledger/general-ledger-detail/#query-and-list-general-ledger-details-legacy)

* * *

Many journal entries are created by the system based on activity in sub ledgers like Accounts Receivable and Accounts Payable.

General ledger details help understand the relationships between journal entries and their source sub ledger transactions. See the General Ledger Detail [entity relationship diagram](https://developer.intacct.com/entity-relationship-diagrams/gl-detail/) for more information.

**Important Performance Considerations**

`GLDETAIL` represents an API query against a view, not a table. This query against a view impacts performance. When building solutions, consider the size of the company and dataset for which the solution is developed and follow these recommendations:

*   When using General Ledger Details, [Journal Entry](https://developer.intacct.com/api/general-ledger/journal-entries/), and [Journal Entry Lines](https://developer.intacct.com/api/general-ledger/journal-entries/), apply appropriate filters (dates, states, modified date, and so forth). Limited or no filters can greatly impact performance and lead to timeouts, especially for large datasets.
*   To avoid timeouts with larger datasets, create a custom report. Then, use the async [`readReport`](https://developer.intacct.com/api/customization-services/custom-reports/) function to execute the report. This method can help mitigate performance issues and avoid timeouts.

Alternatively, for dimensional line-level detail with GL entries, consider gathering the required data from [journal entry lines](https://developer.intacct.com/api/general-ledger/journal-entries/).

* * *

Get General Ledger Detail Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the general ledger detail object:

```
<lookup>
    <object>GLDETAIL</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLDETAIL` |

* * *

Query and List General Ledger Details
-------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and module key for each General Ledger Detail for Cash Management:

```
<query>
    <object>GLDETAIL</object>
    <select>
        <field>RECORDNO</field>
        <field>MODULEKEY</field>
    </select>
    <filter>
        <equalto>
            <field>MODULEKEY</field>
            <value>11.CM</value>
        </equalto>
    </filter>
</query>
```

> List General Ledger Details for the journal with the given symbol:

```
<query>
    <object>GLDETAIL</object>
    <select>
        <field>BATCH_TITLE</field>
        <field>BATCH_DATE</field>
        <field>TRX_AMOUNT</field>
        <field>JOURNAL.SYMBOL</field>
        <field>JOURNAL.TITLE</field>
    </select>
    <filter>
        <equalto>
            <field>JOURNAL.SYMBOL</field>
            <value>APJ</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLDETAIL` |
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

`filter` Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| MODULEKEY | Optional | string | Module key for the application area. Use `2.GL` for General Ledger, `3.AP` for Accounts Payable, `4.AR` for Accounts Receivable, `6.EE` for Employee Expenses, `7.INV` for Inventory Control, `8.SO` for Order Entry, `9.PO` for Purchasing, `11.CM` for Cash Management, `48.PROJACCT` for Project and Resource Management, `55.CONTRACT` for Contracts and Revenue Management. |
| BOOKID | Optional | string | Book ID. Use `ACCRUAL`, `CASH`, or the name of a user-defined book with the accounting method appended, for example, `UDB1ACCRUAL`. |

* * *

Query and List General Ledger Details (Legacy)
----------------------------------------------

#### `readByQuery`

> List General Ledger Details:

```
<readByQuery>
    <object>GLDETAIL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List General Ledger Details for the Cash Management module:

```
<readByQuery>
    <object>GLDETAIL</object>
    <fields>*</fields>
    <query>MODULEKEY = '11.CM'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLDETAIL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| MODULEKEY | Optional | string | Module key for the application area. Use `2.GL` for General Ledger, `3.AP` for Accounts Payable, `4.AR` for Accounts Receivable, `6.EE` for Employee Expenses, `7.INV` for Inventory Control, `8.SO` for Order Entry, `9.PO` for Purchasing, `11.CM` for Cash Management, `48.PROJACCT` for Project and Resource Management, `55.CONTRACT` for Contracts and Revenue Management. |
| BOOKID | Optional | string | Book ID. Use `ACCRUAL`, `CASH`, or the name of a user-defined book with the accounting method appended, for example, `UDB1ACCRUAL`. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

