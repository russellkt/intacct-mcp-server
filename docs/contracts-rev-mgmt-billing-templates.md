Title: Billing Templates

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/

Markdown Content:
*   [Billing Templates](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#billing-templates)
    *   [Get Billing Template Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#get-billing-template-object-definition)
    *   [Query and List Billing Templates](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#query-and-list-billing-templates)
    *   [Query and List Billing Templates (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#query-and-list-billing-templates-legacy)
    *   [Get Billing Template](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#get-billing-template)
    *   [Get Billing Template by ID](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#get-billing-template-by-id)
    *   [Create Billing Template](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#create-billing-template)
    *   [Update Billing Template](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#update-billing-template)
    *   [Delete Billing Template](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#delete-billing-template)
*   [Billing Template Details](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#billing-template-details)
    *   [Get Billing Template Detail Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#get-billing-template-detail-object-definition)
    *   [Query and List Billing Template Details](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#query-and-list-billing-template-details)
    *   [Query and List Billing Template Details (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#query-and-list-billing-template-details-legacy)
    *   [Get Billing Template Detail](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#get-billing-template-detail)

* * *

A billing template defines the schedule to invoice the flat/fixed amount for a contract line over the contract term.

* * *

### Get Billing Template Object Definition

#### `lookup`

> List all the fields and relationships for the billing template object:

```
<lookup>
    <object>CONTRACTBILLINGTEMPLATE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATE` |

* * *

### Query and List Billing Templates

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and description for each billing template:

```
<query>
    <object>CONTRACTBILLINGTEMPLATE</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATE` |
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

### Query and List Billing Templates (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTBILLINGTEMPLATE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active, `F` fo Inactive |

* * *

### Get Billing Template

#### `read`

```
<read>
    <object>CONTRACTBILLINGTEMPLATE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATE` |
| keys | Required | string | Comma-separated list of billing template `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Billing Template by ID

#### `readByName`

```
<readByName>
    <object>CONTRACTBILLINGTEMPLATE</object>
    <keys>Contract Billing Template</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATE` |
| keys | Required | string | Comma-separated list of billing template `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Billing Template

[History](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#history-create-billing-template)

| Release | Changes |
| --- | --- |
| 2019 Release 1 | Added METHOD and SOURCE |

#### `create`

> Creates a billing template with predefined percentages:

```
<create>
    <CONTRACTBILLINGTEMPLATE>
        <NAME>40-30-20-10AA</NAME>
        <DESCRIPTION>Declining percentages at 2, 4, 6, and 8 months</DESCRIPTION>
        <METHOD>Predefined percentages</METHOD>
        <CONTRACTBILLINGTEMPLATEENTRIES>
            <CONTRACTBILLINGTEMPLATEENTRY>
                <PERIODOFFSET>2</PERIODOFFSET>
                <PERCENTBILLED>40</PERCENTBILLED>
            </CONTRACTBILLINGTEMPLATEENTRY>
            <CONTRACTBILLINGTEMPLATEENTRY>
                <PERIODOFFSET>4</PERIODOFFSET>
                <PERCENTBILLED>30</PERCENTBILLED>
            </CONTRACTBILLINGTEMPLATEENTRY>
            <CONTRACTBILLINGTEMPLATEENTRY>
                <PERIODOFFSET>6</PERIODOFFSET>
                <PERCENTBILLED>20</PERCENTBILLED>
            </CONTRACTBILLINGTEMPLATEENTRY>
            <CONTRACTBILLINGTEMPLATEENTRY>
                <PERIODOFFSET>8</PERIODOFFSET>
                <PERCENTBILLED>10</PERCENTBILLED>
            </CONTRACTBILLINGTEMPLATEENTRY>
        </CONTRACTBILLINGTEMPLATEENTRIES>
    </CONTRACTBILLINGTEMPLATE>
</create>
```

> Creates a billing template for project percent complete:

```
<CONTRACTBILLINGTEMPLATE>
    <NAME>Proj est. hrs</NAME>
    <DESCRIPTION>Project percent complete - based on estimated hours</DESCRIPTION>
    <METHOD>Project percent complete</METHOD>
    <SOURCE>Estimated hours</SOURCE>
    <STATUS>active</STATUS>
</CONTRACTBILLINGTEMPLATE>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTBILLINGTEMPLATE | Required | object | Object to create |

`CONTRACTBILLINGTEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Billing template name |
| DESCRIPTION | Optional | string | Description |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| METHOD | Optional | string | Template type. Use `Predefined percentages`, `Project percent complete`, or `Task percent complete`. (Default: `Predefined percentages`) |
| SOURCE | Optional | string | When creating `Project percent complete`, or `Task percent complete` templates, specifies whether to base the percentages on `Estimated hours`, `Observed % completed`, or `Planned hours`. `Budgeted hours` is also available for `Project percent complete`. (Default: `Estimated hours`) |
| CONTRACTBILLINGTEMPLATEENTRIES | Optional | `CONTRACTBILLINGTEMPLATEENTRY[0...n]` | Template detail when using predefined percentages. Percent to bill’s must add up to 100. |

`CONTRACTBILLINGTEMPLATEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PERIODOFFSET | Required | integer | Number of months offset |
| PERCENTBILLED | Required | decimal | Percent to bill |

* * *

### Update Billing Template

[History](https://developer.intacct.com/api/contracts-rev-mgmt/billing-templates/#history-update-billing-template)

| Release | Changes |
| --- | --- |
| 2019 Release 1 | Added METHOD and SOURCE |

When updating template details, you are providing a complete new set of entries (existing entries are deleted).

#### `update`

```
<update>
    <CONTRACTBILLINGTEMPLATE>
        <NAME>40-30-20-10AA</NAME>
        <DESCRIPTION>Hello world</DESCRIPTION>
    </CONTRACTBILLINGTEMPLATE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTBILLINGTEMPLATE | Required | object | Object to update |

`CONTRACTBILLINGTEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of object. Required if not using `NAME`. |
| NAME | Optional | string | Billing template name. Required if not using `RECORDNO`. |
| DESCRIPTION | Optional | string | Description |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| METHOD | Optional | string | Template type. Use `Predefined percentages`, `Project percent complete`, or `Task percent complete`. (Default: `Predefined percentages`) |
| SOURCE | Optional | string | When creating `Project percent complete`, or `Task percent complete` templates, specifies whether to base the percentages on `Estimated hours`, `Observed % completed`, or `Planned hours`. `Budgeted hours` is also available for `Project percent complete`. (Default: `Estimated hours`) |
| CONTRACTBILLINGTEMPLATEENTRIES | Optional | `CONTRACTBILLINGTEMPLATEENTRY[0...n]` | Template detail when using predefined percentages. Percent to bill’s must add up to 100. |

`CONTRACTBILLINGTEMPLATEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PERIODOFFSET | Required | integer | Number of months offset |
| PERCENTBILLED | Required | decimal | Percent to bill |

* * *

### Delete Billing Template

#### `delete`

```
<delete>
    <object>CONTRACTBILLINGTEMPLATE</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATE` |
| keys | Required | string | Comma-separated list of billing template `RECORDNO` to delete |

* * *

Billing Template Details
------------------------

### Get Billing Template Detail Object Definition

#### `lookup`

> List all the fields and relationships for the billing template detail object:

```
<lookup>
    <object>CONTRACTBILLINGTEMPLATEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATEENTRY` |

* * *

### Query and List Billing Template Details

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and percent billed for each billing template detail:

```
<query>
    <object>CONTRACTBILLINGTEMPLATEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>PERCENTBILLED</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATEENTRY` |
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

### Query and List Billing Template Details (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTBILLINGTEMPLATEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Billing Template Detail

#### `read`

```
<read>
    <object>CONTRACTBILLINGTEMPLATEENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGTEMPLATEENTRY` |
| keys | Required | string | Comma-separated list of billing template detail `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

