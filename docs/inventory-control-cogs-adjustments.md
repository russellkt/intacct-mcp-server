Title: COGS Adjustments for Prior Periods

URL Source: https://developer.intacct.com/api/inventory-control/cogs-adjustments/

Markdown Content:
*   [Get Cost of Goods Sold Adjustment Object Definition](https://developer.intacct.com/api/inventory-control/cogs-adjustments/#get-cost-of-goods-sold-adjustment-object-definition)
*   [Query and List Cost of Goods Sold Adjustments](https://developer.intacct.com/api/inventory-control/cogs-adjustments/#query-and-list-cost-of-goods-sold-adjustments)
*   [Query and List Cost of Goods Sold Adjustments (Legacy)](https://developer.intacct.com/api/inventory-control/cogs-adjustments/#query-and-list-cost-of-goods-sold-adjustments-legacy)
*   [Get Cost of Goods Sold Adjustment](https://developer.intacct.com/api/inventory-control/cogs-adjustments/#get-cost-of-goods-sold-adjustment)
*   [Create Cost of Goods Sold Adjustment](https://developer.intacct.com/api/inventory-control/cogs-adjustments/#create-cost-of-goods-sold-adjustment)
*   [Delete Cost of Goods Sold Adjustment](https://developer.intacct.com/api/inventory-control/cogs-adjustments/#delete-cost-of-goods-sold-adjustment)

* * *

Landed costs and other inventory operations, such as changing an item’s standard cost, can affect the cost of goods sold (COGS) in prior periods.

Consider the following examples:

*   You add/modify landed costs for an item and want the changes to apply for purchase orders in prior periods.
*   You change the standard cost of an item and use the Maintain Inventory Valuation tool to adjust the unit cost in the inventory subledger for prior periods.

In both scenarios, the inventory subledger is correctly updated, but the general ledger is not. You can balance out such discrepancies using `COGSCLOSEDJE` to apply adjustments to the general ledger in an open period.

You must define the journal to use for prior period COGS adjustments in your Inventory Control configuration. It is considered a best practice to use a separate journal for adjustments for audit purposes. You also need to create the necessary permissions for posting prior period COGS adjustments.

* * *

Get Cost of Goods Sold Adjustment Object Definition
---------------------------------------------------

#### `lookup`

> List all the fields and relationships for the cost of goods sold adjustment object:

```
<lookup>
    <object>COGSCLOSEDJE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COGSCLOSEDJE` |

* * *

Query and List Cost of Goods Sold Adjustments
---------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and current cost for each potential adjusting journal entry:

```
<query>
    <object>COGSCLOSEDJE</object>
    <select>
        <field>RECORDNO</field>
        <field>CURRENTCOST</field>
    </select>
    <filter>
        <equalto>
            <field>NEEDSADJUSTMENT</field>
            <value>true</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COGSCLOSEDJE` |
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

Query and List Cost of Goods Sold Adjustments (Legacy)
------------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>COGSCLOSEDJE</object>
    <fields>*</fields>
    <query>NEEDSADJUSTMENT = 'true'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COGSCLOSEDJE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NEEDSADJUSTMENT | Optional | string | Needs adjustment. Use `true` to list all potential adjusting journal entries, or use `false` to list adjustments that have already been applied. Adjustments already applied have a `FIXUNIQUEID` value that can be used to reverse the adjustment. (Default: `true`) |

#### `Response`

`cogsclosedje`

> The above function returns data structured like this:

```
<cogsclosedje>
    <RECORDNO>299</RECORDNO>
    <ASOFDATE>5/20/2018</ASOFDATE>
    <ITEMID>computer-87</ITEMID>
    <WAREHOUSE>1</WAREHOUSE>
    <LOCATION>1</LOCATION>
    <DOCUMENTNAME>Sales Invoice-SUBINV#0105#doc</DOCUMENTNAME>
    <CUSTOMER>FP--Future Products Inc</CUSTOMER>
    <CURRENTCOST>515</CURRENTCOST>
    <CURRENTGLCOGS>500</CURRENTGLCOGS>
    <DIFFERENCE>15</DIFFERENCE>
</cogsclosedje>
```

> The same function returns data structured like this if `NEEDSADJUSTMENT` is set to false:

```
<cogsclosedje>
    <RECORDNO>302</RECORDNO>
    <ASOFDATE>12/18/2017</ASOFDATE>
    <ITEMID>HH Avg Inv</ITEMID>
    <WAREHOUSE>1</WAREHOUSE>
    <LOCATION>1</LOCATION>
    <DOCUMENTNAME>Sales Invoice-SUBINV#0106#doc</DOCUMENTNAME>
    <CUSTOMER>CG--Catalyst Gaming</CUSTOMER>
    <CREATEDON>2018-09-21</CREATEDON>
    <COST>2000</COST>
    <FIXUNIQUEID>302--1537558720</FIXUNIQUEID>
</cogsclosedje>
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| RECORDNO | string | Record number of the sales line item |
| ASOFDATE | string | As of date for the sales transaction |
| ITEMID | string | Item Id |
| WAREHOUSE | string | Warehouse ID |
| LOCATION | string | Location ID of warehouse (for multi-entity/multi-currency company) |
| DOCUMENTNAME | string | Sales order full document name |
| CUSTOMER | string | Customer name |
| CURRENTCOST | number | Current cost of the line |
| CURRENTGLCOGS | number | Current GL journal post amount |
| DIFFERENCE | number | Difference between current cost of the line and current GL journal post |
| CREATEDON | string | GL post date of a previously applied COGS adjustment |
| COST | number | Amount of the previously applied adjustment |
| FIXUNIQUEID | string | Unique ID of the adjustment |

* * *

Get Cost of Goods Sold Adjustment
---------------------------------

#### `read`

```
<read>
    <object>COGSCLOSEDJE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COGSCLOSEDJE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Cost of Goods Sold Adjustment
------------------------------------

Applies the specified adjustments to the configured GL journal for prior period COGS adjustments. The generated GL journal entries cannot be adjusted, but they can be rolled back by deleting the cost of goods sold adjustment.

#### `create`

```
<create>
    <COGSClosedJE>
        <RECORDNO>6</RECORDNO>
        <POSTINGDATE>09/18/2018</POSTINGDATE>
    </COGSClosedJE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COGSClosedJE | Required | object | Object to create |

`COGSCLOSEDJE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the cost of goods sold adjustment to apply |
| POSTINGDATE | Optional | string | Posting date in format `mm/dd/yyyy` (Default: first date in first available open period) |

* * *

Delete Cost of Goods Sold Adjustment
------------------------------------

When you delete a cost of goods sold adjustment, the adjusting GL journal entry is rolled back and the `COGSCLOSEDJE` entry with the given key becomes available as a potential adjustment again.

#### `delete`

> Deletes the adjustment with the given unique identifier:

```
<delete>
    <object>COGSCLOSEDJE</object>
    <keys>302--1537558720</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COGSCLOSEDJE` |
| keys | Required | string | Comma-separated list of tnique identifier for the fix (`FIXUNIQUEID`) for the `COGSCLOSEDJE` to delete. You can only delete one at a time. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

