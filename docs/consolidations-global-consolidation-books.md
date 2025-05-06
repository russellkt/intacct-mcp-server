Title: Consolidation Books

URL Source: https://developer.intacct.com/api/consolidations/global-consolidation-books/

Markdown Content:
*   [Get Global Consolidation Book Object Definition](https://developer.intacct.com/api/consolidations/global-consolidation-books/#get-global-consolidation-book-object-definition)
*   [Query and List Global Consolidation Books](https://developer.intacct.com/api/consolidations/global-consolidation-books/#query-and-list-global-consolidation-books)
*   [Query and List Global Consolidation Books (Legacy)](https://developer.intacct.com/api/consolidations/global-consolidation-books/#query-and-list-global-consolidation-books-legacy)
*   [Get Global Consolidation Book](https://developer.intacct.com/api/consolidations/global-consolidation-books/#get-global-consolidation-book)
*   [Get Global Consolidation Book by ID](https://developer.intacct.com/api/consolidations/global-consolidation-books/#get-global-consolidation-book-by-id)
*   [Create Global Consolidation Book](https://developer.intacct.com/api/consolidations/global-consolidation-books/#create-global-consolidation-book)
*   [Update Global Consolidation Book](https://developer.intacct.com/api/consolidations/global-consolidation-books/#update-global-consolidation-book)
*   [Delete Global Consolidation Book](https://developer.intacct.com/api/consolidations/global-consolidation-books/#delete-global-consolidation-book)

* * *

Consolidation books define how to combine the financial and operational information of selected entities within multi-entity companies. You can also configure a consolidation book to automatically convert different base currencies into a single reporting currency, which is called a Global Consolidation.

Setting up a new consolidation book is done in several phases:

*   Create the consolidation book, providing the book ID, reporting currency, elimination entity, dimensions, and so forth.
*   [Specify the entities](https://developer.intacct.com/api/consolidations/global-consolidation-entities/) to consolidate.
*   [Specify the elimination account](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/) for posting consolidation journal entries, including currency translation adjustments and elimination transactions for inter-entity balances.
*   [Add journals](https://developer.intacct.com/api/consolidations/global-consolidation-journals/) for GAAP, tax, and user-defined books.
*   For Global Consolidation, [Override the exchange rate](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/) translation method for any GL account used in a consolidation.

You can then [run the consolidation](https://developer.intacct.com/api/consolidations/global-consolidations/), specifying the reporting period and other choices.

In 2018 Release 2, the improved version of Global Consolidations was introduced and old functionality was deprecated. Any consolidation book now has a `LEGACY` parameter that indicates whether it is a new consolidation book (LEGACY=’F’) or a deprecated one. The API only supports creating and updating new consolidation books.

**Note:** Most consolidation object names start with `GC` and are called “Global Coonsolidation,” but you can use them for domestic or global consolidations.

* * *

Get Global Consolidation Book Object Definition
-----------------------------------------------

#### `lookup`

> List all the fields and relationships for the global consolidation book object:

```
<lookup>
    <object>GCBOOK</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOK` |

* * *

Query and List Global Consolidation Books
-----------------------------------------

#### `query`

> List the record number and book ID for each global consolidation book:

```
<query>
    <object>GCBOOK</object>
    <select>
        <field>RECORDNO</field>
        <field>BOOKID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOK` |
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

Query and List Global Consolidation Books (Legacy)
--------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>GCBOOK</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOK` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BSTRANMETHOD | Optional | string | Translation method for Balance sheet accounts. Use `S` for Ending spot rate or `A` for Weighted average rate. |
| ISTRANMETHOD | Optional | string | Income statement accounts. Use `S` for Ending spot rate or `A` for Weighted average rate. |

* * *

Get Global Consolidation Book
-----------------------------

Returns the details of a single global consolidation object that is specified by a `RECORDNO`.

#### `read`

```
<read>
    <object>GCBOOK</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOK` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the consolidation book to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Global Consolidation Book by ID
-----------------------------------

Returns the details of a single global consolidation object that is specified by its `BOOKID`.

#### `readByName`

```
<readByName>
    <object>GCBOOK</object>
    <keys>gc_book</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOK` |
| keys | Required | string | Comma-separated list of `BOOKID` of the consolidation book to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Global Consolidation Book
--------------------------------

[History](https://developer.intacct.com/api/consolidations/global-consolidation-books/#history-create-global-consolidation-book)

| Release | Changes |
| --- | --- |
| 2019 Release 3 | Added DIMENSIONS |
| 2019 Release 3 | Added HISTORICALRATEDATETYPE |

#### `create`

```
<create>
    <GCBOOK>
        <BOOKID>gc_book</BOOKID>
        <DESCRIPTION>Global consolidated book</DESCRIPTION>
        <CURRENCY>USD</CURRENCY>
        <CTANETASSETACCOUNTNO>1009</CTANETASSETACCOUNTNO>
        <CTANETINCOMEACCOUNTNO>1007</CTANETINCOMEACCOUNTNO>
        <BOOKSTATJOURNALSYMBOL>gc_stat</BOOKSTATJOURNALSYMBOL>
        <BOOKSTATJOURNALTITLE>Statistical journal</BOOKSTATJOURNALTITLE>
        <BSTRANMETHOD>Ending spot rate</BSTRANMETHOD>
        <ISTRANMETHOD>Weighted average rate</ISTRANMETHOD>
        <EENAME>USAE</EENAME>
        <AUTOELIMINATION>true</AUTOELIMINATION>
        <SOURCEBOOKID>ACCRUAL</SOURCEBOOKID>
        <BOOKJOURNALSYMBOL>gc_journal</BOOKJOURNALSYMBOL>
        <BOOKJOURNALTITLE>Global consolidations journal</BOOKJOURNALTITLE>
        <DIMENSIONS>location#~#department</DIMENSIONS>
    </GCBOOK>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOK | Required | object | Object to create |

`GCBOOK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKID | Required | string | Consolidation book ID (name). |
| DESCRIPTION | Required | string | Description |
| DEPARTMENTID | Optional | string | Default department |
| BOOKJOURNALSYMBOL | Required | string | Book journal symbol. Use 16 characters or fewer. |
| BOOKJOURNALTITLE | Required | string | Book journal title. Use 40 characters or fewer. |
| BOOKSTATJOURNALSYMBOL | Required | string | Default statistical journal symbol. Use 16 characters or fewer. |
| BOOKSTATJOURNALTITLE | Optional | string | Statistical journal title. Use 40 characters or fewer. |
| BUDGETID | Optional | string | Budget ID |
| BSTRANMETHOD | Required | string | Translation method for balance sheet accounts, typically `Ending spot rate`. |
| ISTRANMETHOD | Required | string | Translation method for income statement accounts, typically `weighted average`. |
| SOURCEBOOKID | Optional | string | Accounting method to use.
*   `ACCRUAL`
*   `CASH`

`CASH` is available only if you selected both Accrual and cash as your accounting method in your General Ledger Setup. |
| CURRENCY | Required | string | Currency code to use in reporting. |
| EXCHRATETYPE | Optional | string | Exchange rate type. Use `Intacct Daily Rate`. |
| CTANETASSETACCOUNTNO | Required | string | Net income account number for currency exchange gain/loss. |
| CTANETINCOMEACCOUNTNO | Required | string | Net assets account number for currency exchange gain/loss. |
| EENAME | Required | string | Elimination entity name. |
| AUTOELIMINATION | Optional | boolean | Inter-entity auto-elimination, which automatically posts inter-entity eliminations to the [elimination account](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/).

*   `false` (default)
*   `true` - use auto elimination

 |
| HISTORICALRATEDATETYPE | Optional | string | Selects the historical rate date option.

*   `LINELEVELDATE` - line level exchange rate date (default)
*   `TRANSACTIONDATE` - transaction date

 |
| DIMENSIONS | Optional | string | Dimensions to include in the consolidation. Implode multiple IDs with `#~#` (Default: `location`). |

* * *

Update Global Consolidation Book
--------------------------------

[History](https://developer.intacct.com/api/consolidations/global-consolidation-books/#history-update-global-consolidation-book)

| Release | Changes |
| --- | --- |
| 2019 Release 3 | Added DIMENSIONS |
| 2019 Release 3 | Added HISTORICALRATEDATETYPE |

Note that after _running_ a consolidation, the ability to change book setup is largely limited to adding new data, such as a completely new account. You can also modify which dimensions are included.

#### `update`

```
<update>
    <GCBOOK>
        <BOOKID>gc_book</BOOKID>
        <DESCRIPTION>gc consolidated book with more stuff, etc.</DESCRIPTION>
        <BUDGETID>Std_Budget</BUDGETID>
    </GCBOOK>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOK | Required | object | Object to update |

`GCBOOK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKID | Required | string | Consolidation book ID |
| DESCRIPTION | Optional | string | Description |
| DEPARTMENTID | Optional | string | Default department |
| BOOKJOURNALSYMBOL | Optional | string | Book journal symbol. Use 16 characters or fewer. |
| BOOKJOURNALTITLE | Optional | string | Book journal title. Use 40 characters or fewer. |
| BOOKSTATJOURNALSYMBOL | Optional | string | Default statistical journal symbol. Use 16 characters or fewer. |
| BOOKSTATJOURNALTITLE | Optional | string | Statistical journal title. Use 40 characters or fewer. |
| BUDGETID | Optional | string | Budget ID |
| BSTRANMETHOD | Optional | string | Translation method for balance sheet accounts, typically `Ending spot rate`. |
| ISTRANMETHOD | Optional | string | Translation method for income statement accounts, typically `weighted average`. |
| SOURCEBOOKID | Optional | string | Accounting method to use.
*   `ACCRUAL`
*   `CASH`

`CASH` is available only if you selected both Accrual and cash as your accounting method in your General Ledger Setup. |
| CURRENCY | Optional | string | Currency code to use in reporting |
| EXCHRATETYPE | Optional | string | Exchange rate type. Use `Intacct Daily Rate`. |
| CTANETASSETACCOUNTNO | Optional | string | Net income account number for currency exchange gain/loss |
| CTANETINCOMEACCOUNTNO | Optional | string | Net assets account number for currency exchange gain/loss |
| EENAME | Optional | string | Elimination entity name |
| AUTOELIMINATION | Optional | boolean | Inter-entity auto-elimination, which automatically posts inter-entity eliminations to the [elimination account](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/).

*   `false` (default)
*   `true` - use auto elimination

 |
| HISTORICALRATEDATETYPE | Optional | string | Selects the historical rate date option.

*   `LINELEVELDATE` - line level exchange rate date (default)
*   `TRANSACTIONDATE` - transaction date

 |
| DIMENSIONS | Optional | string | Dimensions to include in the consolidation. Implode multiple IDs with `#~#`. The set of dimensions you provide replace the previous set of dimensions. |

* * *

Delete Global Consolidation Book
--------------------------------

#### `delete`

```
<delete>
    <object>GCBOOK</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOK` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the consolidation book to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

