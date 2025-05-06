Title: Consolidation Override Accounts

URL Source: https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/

Markdown Content:
*   [Get Global Consolidation Override Account Object Definition](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/#get-global-consolidation-override-account-object-definition)
*   [Query and List Global Consolidation Override Accounts](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/#query-and-list-global-consolidation-override-accounts)
*   [Query and List Global Consolidation Override Accounts (Legacy)](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/#query-and-list-global-consolidation-override-accounts-legacy)
*   [Get Global Consolidation Override Account](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/#get-global-consolidation-override-account)
*   [Create Global Consolidation Override Account](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/#create-global-consolidation-override-account)
*   [Update Global Consolidation Override Account](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/#update-global-consolidation-override-account)
*   [Delete Global Consolidation Account Override](https://developer.intacct.com/api/consolidations/global-consolidation-override-accts/#delete-global-consolidation-account-override)

* * *

You can override the exchange rate translation method for any GL account used in a consolidation by specifying a different currency conversion method than that of the book itself.

**Note:** Most consolidation object names start with `GC` and are called “Global Coonsolidation,” but you can use them for domestic or global consolidations.

* * *

Get Global Consolidation Override Account Object Definition
-----------------------------------------------------------

#### `lookup`

> List all the fields and relationships for the Global Consolidation override account object:

```
<lookup>
    <object>GCBOOKACCTRATETYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKACCTRATETYPE` |

* * *

Query and List Global Consolidation Override Accounts
-----------------------------------------------------

#### `query`

> List the record number and book ID for each Global Consolidation override account:

```
<query>
    <object>GCBOOKACCTRATETYPE</object>
    <select>
        <field>RECORDNO</field>
        <field>BOOKID</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKACCTRATETYPE` |
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

Query and List Global Consolidation Override Accounts (Legacy)
--------------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>GCBOOKACCTRATETYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKACCTRATETYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Global Consolidation Override Account
-----------------------------------------

#### `read`

```
<read>
    <object>GCBOOKACCTRATETYPE</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKACCTRATETYPE` |
| keys | Required | string | Comma-separated list of global consolidation override account `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Global Consolidation Override Account
--------------------------------------------

#### `create`

```
<create>
    <GCBOOKACCTRATETYPE>
        <BOOKID>gc_book</BOOKID>
        <GLACCOUNTNO>1000</GLACCOUNTNO>
        <GLACCTRATETYPES>Historical rate</GLACCTRATETYPES>
        <OVERRIDERATE>Intacct Daily Rate</OVERRIDERATE>
    </GCBOOKACCTRATETYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKACCTRATETYPE | Required | object | Object to create |

`GCBOOKACCTRATETYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKID | Required | string | Consolidation book ID |
| GLACCOUNTNO | Required | string | GL account number |
| GLACCTRATETYPES | Required | string | Exchange Rate type to use.
*   `Ending spot rate` - the currency exchange rate at the close of the specified date or period
*   `Weighted average rate.` - for income statement accounts where an average value over a period of time is a generally accepted accounting principle
*   `Historical rate` - the currency exchange rate in effect at the time the transaction is performed

 |
| OVERRIDERATE | Required | string | Exchange rate table to apply. Available only for `Historical rate` rate type. Use `Intacct Daily Rate` or a custom rate. |
| OVERRIDEEXPIRYDATE | Optional | string | Use this rate table until. Last period for which the override rate is valid in format `mm/dd/yyyy`. Available only if you selected a user-defined table as the Rate table for the account. |

* * *

Update Global Consolidation Override Account
--------------------------------------------

#### `update`

```
<update>
    <GCBOOKACCTRATETYPE>
        <GCBOOKACCTRATETYPE>
            <RECORDNO>122</RECORDNO>
            <GLACCOUNTNO>1000</GLACCOUNTNO>
            <GLACCTRATETYPES>Historical rate</GLACCTRATETYPES>
            <OVERRIDERATE>Intacct Daily Rate</OVERRIDERATE>
            <OVERRIDEEXPIRYDATE>10/31/2018</OVERRIDEEXPIRYDATE>
        </GCBOOKACCTRATETYPE>
    </GCBOOKACCTRATETYPE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKACCTRATETYPE | Optional | object | Object to update |

`GCBOOKACCTRATETYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Override account `RECORDNO` to update |
| GLACCOUNTNO | Optional | string | GL account number |
| GLACCTRATETYPES | Required | string | Exchange Rate type to use.
*   `Ending spot rate` - the currency exchange rate at the close of the specified date or period
*   `Weighted average rate.` - for income statement accounts where an average value over a period of time is a generally accepted accounting principle
*   `Historical rate` - the currency exchange rate in effect at the time the transaction is performed

 |
| OVERRIDERATE | Optional | string | Rate table. Available only for `Historical rate` rate type. Use `Intacct Daily Rate` or a custom rate. |
| OVERRIDEEXPIRYDATE | Optional | string | Available only for `Historical rate` rate type. Last period for which the override rate is valid in format `mm/dd/yyyy`. |

* * *

Delete Global Consolidation Account Override
--------------------------------------------

#### `delete`

```
<delete>
    <object>GCBOOKACCTRATETYPE</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKACCTRATETYPE | Required | object | Object type to delete |
| keys | Required | string | Comma-separated list of global consolidation override account `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

