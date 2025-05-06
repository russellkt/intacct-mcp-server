Title: MEA Allocations

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/mea-allocations/

Markdown Content:
*   [Get MEA Allocation Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/mea-allocations/#get-mea-allocation-object-definition)
*   [Query and List MEA Allocations](https://developer.intacct.com/api/contracts-rev-mgmt/mea-allocations/#query-and-list-mea-allocations)
*   [Query and List MEA Allocations (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/mea-allocations/#query-and-list-mea-allocations-legacy)
*   [Get MEA Allocation](https://developer.intacct.com/api/contracts-rev-mgmt/mea-allocations/#get-mea-allocation)
*   [Create MEA Allocation](https://developer.intacct.com/api/contracts-rev-mgmt/mea-allocations/#create-mea-allocation)

* * *

If your company provides multiple products as part of a single arrangement, you create an MEA allocation for the contract.

When you create the allocation, you group the applicable contract lines into one or more bundles. For each bundle, the system uses the items’ fair value prices from the contract’s MEA price list to allocate the total bundle contract value between the participating contract lines. Alternatively, you can override the automatic calculation of the MEA amounts and input your own values. In either case, the system uses the allocated amounts in the revenue schedules associated with the applicable contract lines.

You can create multiple allocations, each with its own specific effective date so that balances posted prior to the effective date are not affected. If you create multiple allocations with the same effective date, the last one created will be active.

For information about how to clear MEA allocations from contracts, see [clearallmea](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#clear-all-mea-allocations) and [clearlastactivemea](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#clear-individual-mea-allocations).

* * *

Get MEA Allocation Object Definition
------------------------------------

#### `lookup`

> List all the fields and relationships for the MEA allocation object:

```
<lookup>
    <object>CONTRACTMEABUNDLE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEABUNDLE` |

* * *

Query and List MEA Allocations
------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, contract ID, and type for each MEA allocation:

```
<query>
    <object>CONTRACTMEABUNDLE</object>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
        <field>TYPE</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEABUNDLE` |
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

Query and List MEA Allocations (Legacy)
---------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTMEABUNDLE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEABUNDLE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ADJUSTMENTPROCESS | Optional | string | State. Use `C` for One time, `D` for Distributed. |

Get MEA Allocation
------------------

#### `read`

```
<read>
    <object>CONTRACTMEABUNDLE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEABUNDLE` |
| keys | Required | string | Comma-separated list of MEA allocation `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create MEA Allocation
---------------------

#### `create`

```
<create>
    <CONTRACTMEABUNDLE>
        <CONTRACTID>CON-007</CONTRACTID>
        <NAME>Second allocation</NAME>
        <DESCRIPTION>First Bundle</DESCRIPTION>
        <EFFECTIVEDATE>8/1/2018</EFFECTIVEDATE>
        <ADJUSTMENTPROCESS>Distributed</ADJUSTMENTPROCESS>
        <TYPE>MEA Bundle</TYPE>
        <APPLYTOJOURNAL1>true</APPLYTOJOURNAL1>
        <CONTRACTMEABUNDLEENTRIES>
            <CONTRACTMEABUNDLEENTRY>
                <CONTRACTDETAILLINENO>1</CONTRACTDETAILLINENO>
                <BUNDLENO>1</BUNDLENO>
            </CONTRACTMEABUNDLEENTRY>
            <CONTRACTMEABUNDLEENTRY>
                <CONTRACTDETAILLINENO>2</CONTRACTDETAILLINENO>
                <BUNDLENO>1</BUNDLENO>
            </CONTRACTMEABUNDLEENTRY>
        </CONTRACTMEABUNDLEENTRIES>
    </CONTRACTMEABUNDLE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTMEABUNDLE | Required | object | Object to create |

`CONTRACTMEABUNDLE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Required | string | Contract ID |
| NAME | Required | string | Name for the allocation. Must be unique within the contract |
| DESCRIPTION | Required | string | Description for the allocation. |
| EFFECTIVEDATE | Required | string | Date the MEA allocation becomes active in format `mm/dd/yyyy`. Must fall on or after the latest contract line Start date and before the earliest revenue template End date of all contract lines included in the bundle. |
| ADJUSTMENTPROCESS | Required | string | Adjustment process. Use One time or Distributed. |
| TYPE | Required | string | Use `MEA Bundle` |
| APPLYTOJOURNAL1 | Required | boolean | Apply to journal 1. Use ‘true’ or ‘false’. |
| APPLYTOJOURNAL2 | Required | boolean | Apply to journal 2 (typically used for ASC 606). Use ‘true’ or ‘false’. |
| COMMENTS | Required | string | Comments for the allocation |
| CONTRACTMEABUNDLEENTRIES | Required | `CONTRACTMEABUNDLEENTRY[1...n]` | MEA allocation entries for contract lines. Must have at least two entries per allocation. |

`CONTRACTMEABUNDLELENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTDETAILLINENO | Required | string | Line number of the contract line |
| BUNDLENO | Required | integer | Number for the allocation. |
| MEA\_AMOUNT | Optional | currency | Override amount for the allocation. Only used if you want to override the calculated amount, which would otherwise be generated based on the MEA price list. The MEA amount total for a bundle must equal the Extended transaction value of the lines being bundled. See [MEA allocations](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Adding_Editing_and_Viewing_a_MEA_bundle) in the Sage Intacct product help for more information. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

