Title: Contract Expense Templates

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/

Markdown Content:
*   [Get Expense Template Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#get-expense-template-object-definition)
*   [Query and List Expense Templates](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#query-and-list-expense-templates)
*   [Query and List Expense Templates (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#query-and-list-expense-templates-legacy)
*   [Get Expense Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#get-expense-template)
*   [Get Expense Template by ID](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#get-expense-template-by-id)
*   [Create Expense Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#create-expense-template)
*   [Update Expense Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#update-expense-template)
*   [Delete Expense Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-expense-templates/#delete-expense-template)

* * *

An expense template defines the schedule to recognize an expense amount for a contract or contract line over the contract term.

* * *

Get Expense Template Object Definition
--------------------------------------

#### `lookup`

> List all the fields and relationships for the expense template object:

```
<lookup>
    <object>CONTRACTEXPENSETEMPLATE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSETEMPLATE` |

* * *

Query and List Expense Templates
--------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and amortization method for each expense template:

```
<query>
    <object>CONTRACTEXPENSETEMPLATE</object>
    <select>
        <field>RECORDNO</field>
        <field>METHOD</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSETEMPLATE` |
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

Query and List Expense Templates (Legacy)
-----------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTEXPENSETEMPLATE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSETEMPLATE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active, `F` fo Inactive. |
| METHOD | Optional | string | Recognition method. Use `S` for Straight line, `D` for Daily rate, or `P` for Predefined percentages. |
| POSTINGTYPE | Optional | string | Default posting type. Use `A` for Automatic, `M` for Manual |

* * *

Get Expense Template
--------------------

#### `read`

```
<read>
    <object>CONTRACTEXPENSETEMPLATE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSETEMPLATE` |
| keys | Required | string | Comma-separated list of expense template `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Expense Template by ID
--------------------------

#### `readByName`

```
<readByName>
    <object>CONTRACTEXPENSETEMPLATE</object>
    <keys>10-20-30-40exp</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSETEMPLATE` |
| keys | Required | string | Comma-separated list of expense template `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Expense Template
-----------------------

#### `create`

```
<create>
    <CONTRACTEXPENSETEMPLATE>
        <NAME>BasicExp</NAME>
        <DESCRIPTION>Basic straight line</DESCRIPTION>
        <METHOD>Straight line</METHOD>
        <POSTINGTYPE>Manual</POSTINGTYPE>
    </CONTRACTEXPENSETEMPLATE>
</create>
```

> Create an expense template based on predefined percentages:

```
<create>
    <CONTRACTEXPENSETEMPLATE>
        <NAME>10-20-30-40exp</NAME>
        <DESCRIPTION>Increasing percentages at 2, 4, 6, and 8 months</DESCRIPTION>
        <METHOD>Predefined percentages</METHOD>
        <CONTRACTEXPENSETEMPLATEENTRIES>
            <CONTRACTEXPENSETEMPLATEENTRY>
                <PERIODOFFSET>2</PERIODOFFSET>
                <PERIODPERCENT>40</PERIODPERCENT>
            </CONTRACTEXPENSETEMPLATEENTRY>
            <CONTRACTEXPENSETEMPLATEENTRY>
                <PERIODOFFSET>4</PERIODOFFSET>
                <PERIODPERCENT>30</PERIODPERCENT>
            </CONTRACTEXPENSETEMPLATEENTRY>
            <CONTRACTEXPENSETEMPLATEENTRY>
                <PERIODOFFSET>6</PERIODOFFSET>
                <PERIODPERCENT>20</PERIODPERCENT>
            </CONTRACTEXPENSETEMPLATEENTRY>
            <CONTRACTEXPENSETEMPLATEENTRY>
                <PERIODOFFSET>8</PERIODOFFSET>
                <PERIODPERCENT>10</PERIODPERCENT>
            </CONTRACTEXPENSETEMPLATEENTRY>
        </CONTRACTEXPENSETEMPLATEENTRIES>
    </CONTRACTEXPENSETEMPLATE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSETEMPLATE | Required | object | Object to create |

`CONTRACTEXPENSETEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Expense template name |
| DESCRIPTION | Optional | string | Description |
| METHOD | Optional | string | Amortization method. Use `Straight line`, `Daily rate`, or `Predefined percentages`. (Default: `Straight line`) |
| POSTINGTYPE | Optional | string | Default posting type. Use `Automatic` or `Manual`. (Default: `Manual`) |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| CONTRACTEXPENSETEMPLATEENTRIES | Optional | `CONTRACTEXPENSETEMPLATEENTRY`\[1…n\] | Template details for `Predefined percentages`. |

`CONTRACTEXPENSETEMPLATEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PERIODOFFSET | Optional | integer | Number of months offset for the `Predefined percentages` recognition method |
| PERIODPERCENT | Optional | number | Percentage to recognize. Must add up to 100 percent. |

* * *

Update Expense Template
-----------------------

#### `update`

```
<update>
    <CONTRACTEXPENSETEMPLATE>
        <NAME>10-20-30-40exp</NAME>
        <DESCRIPTION>New description</DESCRIPTION>
    </CONTRACTEXPENSETEMPLATE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTEXPENSETEMPLATE | Required | object | Object to update |

`CONTRACTEXPENSETEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of expense template. Required if not using `NAME`. |
| NAME | Optional | string | Expense template name. Required if not using `RECORDNO`. |
| DESCRIPTION | Optional | string | Description |
| METHOD | Optional | string | Amortization method. Use `Straight line`, `Daily rate`, or `Predefined percentages`. (Default: `Straight line`) |
| POSTINGTYPE | Optional | string | Default posting type. Use `Automatic` or `Manual`. (Default: `Manual`) |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| CONTRACTEXPENSETEMPLATEENTRIES | Optional | `CONTRACTREVENUETEMPLATEENTRY`\[1…n\] | Template details for `Predefined percentages`. When updating template details, you are providing a complete new set of entries (existing entries are deleted). |

`CONTRACTEXPENSETEMPLATEENTRY`

When updating template details, you are providing a complete new set of entries (existing entries are deleted).

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PERIODOFFSET | Optional | integer | Number of months offset for the `Predefined percentages` recognition method |
| PERIODPERCENT | Optional | number | Percentage to recognize. Must add up to 100 percent. |

* * *

Delete Expense Template
-----------------------

#### `delete`

```
<delete>
    <object>CONTRACTEXPENSETEMPLATE</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTEXPENSETEMPLATE` |
| keys | Required | string | Comma-separated list of expense template `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

