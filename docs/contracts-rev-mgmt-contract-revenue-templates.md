Title: Contract Revenue Templates

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/

Markdown Content:
*   [Get Revenue Template Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#get-revenue-template-object-definition)
*   [Query and List Revenue Templates](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#query-and-list-revenue-templates)
*   [Query and List Revenue Templates (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#query-and-list-revenue-templates-legacy)
*   [Get Revenue Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#get-revenue-template)
*   [Get Revenue Template by ID](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#get-revenue-template-by-id)
*   [Create Revenue Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#create-revenue-template)
*   [Update Revenue Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#update-revenue-template)
*   [Delete Revenue Template](https://developer.intacct.com/api/contracts-rev-mgmt/contract-revenue-templates/#delete-revenue-template)

* * *

A revenue template defines the revenue recognition schedule for the flat/fixed amount associated with a contract line.

* * *

Get Revenue Template Object Definition
--------------------------------------

#### `lookup`

> List all the fields and relationships for the revenue template object:

```
<lookup>
    <object>CONTRACTREVENUETEMPLATE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUETEMPLATE` |

* * *

Query and List Revenue Templates
--------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and recognition method for each revenue template:

```
<query>
    <object>CONTRACTREVENUETEMPLATE</object>
    <select>
        <field>RECORDNO</field>
        <field>METHOD</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUETEMPLATE` |
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

Query and List Revenue Templates (Legacy)
-----------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTREVENUETEMPLATE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUETEMPLATE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active, `F` for Inactive. |
| METHOD | Optional | string | Recognition method. Use `S` for Straight line, `D` for Daily rate, `Q` for Quantity based,` P` for Predefined percentages, `C` for Project percent complete, or `T` for Task percent complete. |
| SOURCE | Optional | string | Recognition method source. Use `E` for Estimated hours, `O` for Observed % completed, `B` for Budgeted hours, or `P` for Planned hours. |
| POSTINGTYPE | Optional | string | Default posting type. Use `A` for Automatic, `M` for Manual. |
| RESUMEOPTION | Optional | string | Revenue adjustment option. Use `C` or One time, `D` for Distributed, or `W` for Walk forward. |

* * *

Get Revenue Template
--------------------

#### `read`

```
<read>
    <object>CONTRACTREVENUETEMPLATE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUETEMPLATE` |
| keys | Required | string | Comma-separated list of revenue template `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Revenue Template by ID
--------------------------

#### `readByName`

```
<readByName>
    <object>CONTRACTREVENUETEMPLATE</object>
    <keys>40-30-20-10rev</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUETEMPLATE` |
| keys | Required | string | Comma-separated list of revenue template `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Revenue Template
-----------------------

#### `create`

```
<create>
    <CONTRACTREVENUETEMPLATE>
        <NAME>BasicRev</NAME>
        <DESCRIPTION>Basic straight line</DESCRIPTION>
        <METHOD>Straight line</METHOD>
        <POSTINGTYPE>Manual</POSTINGTYPE>
    </CONTRACTREVENUETEMPLATE>
</create>
```

> Create a revenue template based on predefined percentages:

```
<create>
    <CONTRACTREVENUETEMPLATE>
        <NAME>40-30-20-10rev</NAME>
        <DESCRIPTION>Declining percentages at 2, 4, 6, and 8 months</DESCRIPTION>
        <METHOD>Predefined percentages</METHOD>
        <CONTRACTREVENUETEMPLATEENTRIES>
            <CONTRACTREVENUETEMPLATEENTRY>
                <PERIODOFFSET>2</PERIODOFFSET>
                <PERIODPERCENT>40</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
            <CONTRACTREVENUETEMPLATEENTRY>
                <PERIODOFFSET>4</PERIODOFFSET>
                <PERIODPERCENT>30</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
            <CONTRACTREVENUETEMPLATEENTRY>
                <PERIODOFFSET>6</PERIODOFFSET>
                <PERIODPERCENT>20</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
            <CONTRACTREVENUETEMPLATEENTRY>
                <PERIODOFFSET>8</PERIODOFFSET>
                <PERIODPERCENT>10</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
        </CONTRACTREVENUETEMPLATEENTRIES>
    </CONTRACTREVENUETEMPLATE>
</create>
```

> Create a revenue template based on project completion percentages and step thresholds:

```
<create>
    <CONTRACTREVENUETEMPLATE>
        <NAME>10-20-30-40Proj</NAME>
        <DESCRIPTION>Increasing recognition percentages at 25, 50, 75, and 100 percent project completed</DESCRIPTION>
        <METHOD>Project percent complete</METHOD>
        <STEPTEMPLATE>true</STEPTEMPLATE>
        <CONTRACTREVENUETEMPLATEENTRIES>
            <CONTRACTREVENUETEMPLATEENTRY>
                <STEPPERCENT>25</STEPPERCENT>
                <PERIODPERCENT>10</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
            <CONTRACTREVENUETEMPLATEENTRY>
                <STEPPERCENT>50</STEPPERCENT>
                <PERIODPERCENT>20</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
            <CONTRACTREVENUETEMPLATEENTRY>
                <STEPPERCENT>75</STEPPERCENT>
                <PERIODPERCENT>30</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
            <CONTRACTREVENUETEMPLATEENTRY>
                <STEPPERCENT>100</STEPPERCENT>
                <PERIODPERCENT>40</PERIODPERCENT>
            </CONTRACTREVENUETEMPLATEENTRY>
        </CONTRACTREVENUETEMPLATEENTRIES>
    </CONTRACTREVENUETEMPLATE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUETEMPLATE | Required | object | Object to create |

`CONTRACTREVENUETEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Revenue template name |
| DESCRIPTION | Optional | string | Description |
| METHOD | Optional | string | Recognition method. Use `Straight line`, `Daily rate`, `Quantity based`, `Predefined percentages`, `Project percent complete`, or `Task percent complete`. (Default: `Straight line`) |
| SOURCE | Optional | string | Recognition method source for `Project percent complete` or `Task percent complete` recognition methods. Use `Estimated hours`, `Observed % completed` or `Planned hours`. For `Project percent complete`, `Budgeted hours` is available as well. (Default: `Estimated hours`) |
| POSTINGTYPE | Optional | string | Default posting type. Use `Automatic` or `Manual`. For `Project percent complete` or `Task percent complete` recognition methods, this field is always set to `Manual`. (Default: `Manual`) |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| RESUMEOPTION | Optional | string | Revenue adjustment option. Determines how the system handles revenue scheduled prior to the item’s delivery date. This option is only applicable for `Straight line` or `Daily rate` revenue recognition methods. You must have Fulfillment status tracking enabled for your company. Use `One time`, `Distributed`, or `Walk forward`. |
| STEPTEMPLATE | Optional | boolean | Step revenue for `Project percent complete` or `Task percent complete` recognition methods. Use `true` to use step revenue (so that you can set threshold percentage values at which revenue can be recognized) or `false`. |
| CONTRACTREVENUETEMPLATEENTRIES | Optional | `CONTRACTREVENUETEMPLATEENTRY`\[1…n\] | Template details for either `Predefined percentages` or for `Step revenue` for Project percent complete/Task percent complete. |

`CONTRACTREVENUETEMPLATEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PERIODOFFSET | Optional | integer | Number of months offset when using the `Predefined percentages` recognition method |
| STEPPERCENT | Optional | number | Threshold percentage for `Step revenue` when using Project percent complete/Task percent complete. Useful if you recognize revenue in stages as a project progresses, but don’t recognize the revenue in exact proportion to the project’s percentage of completion as many last minute changes usually come in at the end of a project. The percentages must be in ascending order, for example, the first entry might be at 25, the next at 50, 75, then 100. |
| PERIODPERCENT | Optional | number | Percentage to recognize at either the Number of months offset or at the Threshold percentage. Must add up to 100 percent. |

* * *

Update Revenue Template
-----------------------

#### `update`

```
<update>
    <CONTRACTREVENUETEMPLATE>
        <NAME>40-30-20-10rev</NAME>
        <DESCRIPTION>New description</DESCRIPTION>
    </CONTRACTREVENUETEMPLATE>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTREVENUETEMPLATE | Required | object | Object to update |

`CONTRACTREVENUETEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of object. Required if not using name. |
| NAME | Optional | string | Revenue template name. Required if not using record number. |
| DESCRIPTION | Optional | string | Description |
| METHOD | Optional | string | Recognition method. Use `Straight line`, `Daily rate`, `Quantity based`, `Predefined percentages`, `Project percent complete`, or `Task percent complete`. |
| SOURCE | Optional | string | Recognition method source for `Project percent complete` or `Task percent complete` recognition methods. Use `Estimated hours`, `Observed % completed` or `Planned hours`. For `Project percent complete`, `Budgeted hours` is available as well. |
| POSTINGTYPE | Optional | string | Default posting type. Use `Automatic` or `Manual`. For `Project percent complete` or `Task percent complete` recognition methods, this field is always set to `Manual`. |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |
| RESUMEOPTION | Optional | string | Revenue adjustment option. Determines how the system handles revenue scheduled prior to the item’s delivery date. This option is only applicable for `Straight line` or `Daily rate` revenue recognition methods. You must have Fulfillment status tracking enabled for your company. Use `One time`, `Distributed`, or `Walk forward`. |
| STEPTEMPLATE | Optional | boolean | Step revenue for `Project percent complete` or `Task percent complete` recognition methods. Use `true` to use step revenue (so that you can set threshold percentage values at which revenue can be recognized) or `false`. |
| CONTRACTREVENUETEMPLATEENTRIES | Optional | `CONTRACTREVENUETEMPLATEENTRY`\[1…n\] | Template details for either `Predefined percentages` or for `Step revenue` for Project percent complete/Task percent complete. When updating template details, you are providing a complete new set of entries (existing entries are deleted). |

`CONTRACTREVENUETEMPLATEENTRY`

When updating template details, you are providing a complete new set of entries (existing entries are deleted).

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PERIODOFFSET | Optional | integer | Number of months offset when using the `Predefined percentages` recognition method |
| STEPPERCENT | Optional | number | Threshold percentage for `Step revenue` when using Project percent complete/Task percent complete. Useful if you recognize revenue in stages as a project progresses, but don’t recognize the revenue in exact proportion to the project’s percentage of completion as many last minute changes usually come in at the end of a project. The percentages must be in ascending order, for example, the first entry might be at 25, the next at 50, 75, then 100. |
| PERIODPERCENT | Optional | number | Percentage to recognize at either the Number of months offset or at the Threshold percentage. Must add up to 100 percent. |

* * *

Delete Revenue Template
-----------------------

#### `delete`

```
<delete>
    <object>CONTRACTREVENUETEMPLATE</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTREVENUETEMPLATE` |
| keys | Required | string | Comma-separated list of revenue template `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

