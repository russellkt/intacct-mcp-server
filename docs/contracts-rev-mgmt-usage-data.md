Title: Usage Data

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/

Markdown Content:
*   [Get Usage Data Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#get-usage-data-object-definition)
*   [Query and List Usage Data](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#query-and-list-usage-data)
*   [Query and List Usage Data (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#query-and-list-usage-data-legacy)
*   [Get Usage Data](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#get-usage-data)
*   [Create Usage Data](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#create-usage-data)
*   [Update Usage Data](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#update-usage-data)
*   [Delete Usage Data](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#delete-usage-data)

* * *

A usage record contains the quantity of a contract line item that a customer used or consumed during a specific time period.

* * *

Get Usage Data Object Definition
--------------------------------

#### `lookup`

> List all the fields and relationships for the usage data object:

```
<lookup>
    <object>CONTRACTUSAGE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTUSAGE` |

* * *

Query and List Usage Data
-------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, usage type, usage date, and quantity used for contract lines:

```
<query>
    <object>CONTRACTUSAGE</object>
    <select>
        <field>RECORDNO</field>
        <field>USAGETYPE</field>
        <field>USAGEDATE</field>
        <field>QUANTITY</field>
    </select>
</query>
```

> List the same information for contract lines with the usage type, `Billing - committed`:

```
<query>
    <object>CONTRACTUSAGE</object>
    <select>
        <field>RECORDNO</field>
        <field>USAGETYPE</field>
        <field>USAGEDATE</field>
        <field>DOCID</field>
    </select>
    <filter>
        <equalto>
            <field>USAGETYPE</field>
            <value>Billing – committed</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTUSAGE` |
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

Query and List Usage Data (Legacy)
----------------------------------

[History](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/#history-list-usage-data-legacy)

| Release | Changes |
| --- | --- |

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTUSAGE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTUSAGE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| USAGETYPE | Optional | string | Usage type. Use `T` for Billing - variable, `M` for Billing - committed, `O` for Billing - overage, `F` for Revenue, `U` for Tracked - revenue, `N` for Tracked - variable. |

* * *

#### `read`

```
<read>
    <object>CONTRACTUSAGE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTUSAGE` |
| keys | Required | string | Comma-separated list of data `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Usage Data
-----------------

#### `create`

```
<create>
    <CONTRACTUSAGE>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <CONTRACTLINENO>2</CONTRACTLINENO>
        <USAGEDATE>04/01/2017</USAGEDATE>
        <QUANTITY>55.00</QUANTITY>
    </CONTRACTUSAGE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTUSAGE | Required | object | Object to create |

`CONTRACTUSAGE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Required | string | Contract ID. |
| CONTRACTLINENO | Optional | integer | Contract line number. Required if not using Item ID |
| ITEMID | Optional | string | Item ID. Required if not using Contract line number. If the Item ID is unique in the contract lines, the system will find the appropriate line number for you. If it is not unique you must instead pass the contract line number. |
| USAGEDATE | Required | string | Usage data in format `mm/dd/yyyy` |
| QUANTITY | Required | number | Quantity |
| SERVICEPERIODSTARTDATE | Optional | string | Identifies the start date of a billed service period based on usage. When used, the service period start date should be the first day of the month of USAGEDATE. For example, if USAGEDATE falls anytime in September, 2024, then SERVICEPERIODSTARTDATE should be 09/01/2024. |
| SERVICEPERIODENDDATE | Optional | string | Identifies the end date of a billed service period based on usage. When used, the service period should be the last day of the month of USAGEDATE. For example, if USAGEDATE falls anytime in September, 2024, then SERVICEPERIODENDDATE should be 09/30/2024. |

* * *

Update Usage Data
-----------------

#### `update`

```
<update>
    <CONTRACTUSAGE>
        <RECORDNO>12345</RECORDNO>
        <USAGEDATE>04/01/2017</USAGEDATE>
        <QUANTITY>85.00</QUANTITY>
    </CONTRACTUSAGE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTUSAGE | Required | object | Object to update |

`CONTRACTUSAGE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of usage data |
| USAGEDATE | Optional | string | Usage data in format `mm/dd/yyyy` |
| QUANTITY | Optional | number | Quantity |
| SERVICEPERIODSTARTDATE | Optional | string | Identifies the start date of a billed service period based on usage. When used, the service period start date should be the first day of the month of USAGEDATE. For example, if USAGEDATE falls anytime in September, 2024, then SERVICEPERIODSTARTDATE should be 09/01/2024. |
| SERVICEPERIODENDDATE | Optional | string | Identifies the end date of a billed service period based on usage. When used, the service period should be the last day of the month of USAGEDATE. For example, if USAGEDATE falls anytime in September, 2024, then SERVICEPERIODENDDATE should be 09/30/2024. |

* * *

Delete Usage Data
-----------------

#### `delete`

```
<delete>
    <object>CONTRACTUSAGE</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTUSAGE` |
| keys | Required | string | Comma-separated list of contract `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

