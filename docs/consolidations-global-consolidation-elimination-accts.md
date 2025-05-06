Title: Consolidation Elimination Accounts

URL Source: https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/

Markdown Content:
*   [Get Global Consolidation Elimination Account Object Definition](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/#get-global-consolidation-elimination-account-object-definition)
*   [Query and List Global Consolidation Elimination Accounts](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/#query-and-list-global-consolidation-elimination-accounts)
*   [Query and List Global Consolidation Elimination Accounts (Legacy)](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/#query-and-list-global-consolidation-elimination-accounts-legacy)
*   [Get Global Consolidation Elimination Account](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/#get-global-consolidation-elimination-account)
*   [Create Global Consolidation Elimination Account](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/#create-global-consolidation-elimination-account)
*   [Delete Global Consolidation Elimination Account](https://developer.intacct.com/api/consolidations/global-consolidation-elimination-accts/#delete-global-consolidation-elimination-account)

* * *

Specifies the elimination account where consolidation journal entries are posted, including currency translation adjustments and elimination transactions for inter-entity balances.

**Note:** Most consolidation object names start with `GC` and are called “Global Coonsolidation,” but you can use them for domestic or global consolidations.

* * *

Get Global Consolidation Elimination Account Object Definition
--------------------------------------------------------------

#### `lookup`

> List all the fields and relationships for the Global Consolidation elimination account object:

```
<lookup>
    <object>GCBOOKELIMACCOUNT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKELIMACCOUNT` |

* * *

Query and List Global Consolidation Elimination Accounts
--------------------------------------------------------

#### `query`

> List the record number and account key for each Global Consolidation elimination account:

```
<query>
    <object>GCBOOKELIMACCOUNT</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCOUNTKEY</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKELIMACCOUNT` |
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

Query and List Global Consolidation Elimination Accounts (Legacy)
-----------------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>GCBOOKELIMACCOUNT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKELIMACCOUNT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Global Consolidation Elimination Account
--------------------------------------------

#### `read`

```
<read>
    <object>GCBOOKELIMACCOUNT</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCBOOKELIMACCOUNT` |
| keys | Required | string | Comma-separated list of global consolidation elimination account `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Global Consolidation Elimination Account
-----------------------------------------------

#### `create`

```
<create>
    <GCBOOKELIMACCOUNT>
        <BOOKID>gc_book</BOOKID>
        <GLACCOUNTNO>1000</GLACCOUNTNO>
    </GCBOOKELIMACCOUNT>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKELIMACCOUNT | Required | object | Object to create |

`GCBOOKELIMACCOUNT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKID | Required | string | Book ID of the consolidation book |
| GLACCOUNTNO | Required | string | GL account number |

* * *

Delete Global Consolidation Elimination Account
-----------------------------------------------

#### `delete`

```
<delete>
    <object>GCBOOKELIMACCOUNT</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCBOOKELIMACCOUNT | Required | object | Object to delete |
| keys | Required | string | Comma-separated list of global consolidation elimination account `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

