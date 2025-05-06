Title: Projects

URL Source: https://developer.intacct.com/api/project-resource-mgmt/projects/

Markdown Content:
*   [Get Project Object Definition](https://developer.intacct.com/api/project-resource-mgmt/projects/#get-project-object-definition)
*   [Query and List Projects](https://developer.intacct.com/api/project-resource-mgmt/projects/#query-and-list-projects)
*   [Query and List Projects (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/projects/#query-and-list-projects-legacy)
*   [Get Project](https://developer.intacct.com/api/project-resource-mgmt/projects/#get-project)
*   [Get Project by ID](https://developer.intacct.com/api/project-resource-mgmt/projects/#get-project-by-id)
*   [Create Project](https://developer.intacct.com/api/project-resource-mgmt/projects/#create-project)
*   [Update Project](https://developer.intacct.com/api/project-resource-mgmt/projects/#update-project)
*   [Delete Project](https://developer.intacct.com/api/project-resource-mgmt/projects/#delete-project)

* * *

Projects enable services companies to automate many of the functions of project management.

* * *

Get Project Object Definition
-----------------------------

#### `lookup`

> List all the fields and relationships for the project object:

```
<lookup>
    <object>PROJECT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECT` |

* * *

Query and List Projects
-----------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the product ID and currency for each project:

```
<query>
    <object>PROJECT</object>
    <select>
        <field>PROJECTID</field>
        <field>CURRENCY</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECT` |
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

Query and List Projects (Legacy)
--------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PROJECT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Project
-----------

#### `read`

```
<read>
    <object>PROJECT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECT` |
| keys | Required | string | Comma-separated list of project `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Project by ID
-----------------

#### `readByName`

```
<readByName>
    <object>PROJECT</object>
    <keys>P1234</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECT` |
| keys | Required | string | Comma-separated list of project `PROJECTID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Project
--------------

[History](https://developer.intacct.com/api/project-resource-mgmt/projects/#history-create-project)

| Release | Changes |
| --- | --- |
| 2022 Release 1 | Added CFDA, FUNDEDNAME, AGENCY, PAYER, FUNDINGOTHERID, ASSISTANCETYPE, REVRESTRICTION, RESTRICTIONEXPIRY, RESTRICTIONEXPIRATIONDATE, TIMESATISFACTIONSCHEDULED |
| 2024 Release 4 | Added SCOPE, INCLUSIONS, EXCLUSIONS, TERMS, SCHEDULEDSTARTDATE, SCHEDULEDCOMPLETIONDATE, REVISEDCOMPLETIONDATE, SUBSTANTIALCOMPLETIONDATE, ACTUALCOMPLETIONDATE, NOTICETOPROCEED, RESPONSEDUE, EXECUTEDON, SCHEDULEDIMPACT |

#### `create`

```
<create>
    <PROJECT>
        <NAME>hello world</NAME>
        <PROJECTCATEGORY>Contract</PROJECTCATEGORY>
    </PROJECT>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECT | Required | object | Object to create |

`PROJECT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTID | Optional | string | Unique ID for the project. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value. |
| NAME | Required | string | Name |
| PROJECTCATEGORY | Required | string | Project category |
| DESCRIPTION | Optional | string | Description |
| PARENTID | Optional | string | Parent project ID |
| INVOICEWITHPARENT | Optional | boolean | Use `false` for No, `true` for Yes. (Default: `false`) |
| PROJECTTYPE | Optional | string | Project type |
| PROJECTSTATUS | Optional | string | Project status |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| CUSTOMERID | Optional | string | Customer ID |
| MANAGERID | Optional | string | Project manager employee ID |
| CUSTUSERID | Optional | string | External user ID |
| SALESCONTACTID | Optional | string | Sales contact employee ID |
| DOCNUMBER | Optional | string | Reference number |
| USERRESTRICTIONS | Optional | string | User restrictions |
| CFDA | Optional | string | Stores information about grants from the Catalog of Federal Domestic Assistance. Typically used for the CFDA number (for example, 93.053 for the Nutrition Services Incentive Program). |
| FUNDEDNAME | Optional | string | Name of the project that received funding, such as `Nutrition for children`. |
| AGENCY | Optional | string | Agency responsible for funding, such as `HHS`. |
| PAYER | Optional | string | Source of the funding, either `Federal` or `Third-party`. |
| FUNDINGOTHERID | Optional | string | Another ID for the source of the funding |
| ASSISTANCETYPE | Optional | string | Type of funding, either `Cash` or `Non-cash`. |
| REVRESTRICTION | Optional | string | Specifies how the received revenue can be restricted. Use `Purpose`, `Time`, or `NA`. |
| RESTRICTIONEXPIRY | Optional | string | Time period by which the received funds must be spent according to Federal law. Can designate years, days, or months. |
| RESTRICTIONEXPIRATIONDATE | Optional | string | Date when the received funds expire in the`mm/dd/yyyy` format. Funds often expire at the end of the fiscal year for which they were appropriated. |
| TIMESATISFACTIONSCHEDULED | Optional | boolean | If `true`, specifies that the necessary recurring entry for the release of restriction (per the schedule associated with the funding) has been created. |
| CONTACTINFO | Optional | object | Primary contact |
| BILLTO | Optional | object | Bill to contact |
| SHIPTO | Optional | object | Ship to contact |
| TERMNAME | Optional | string | Payment term |
| BILLINGTYPE | Optional | string | Billing type |
| BEGINDATE | Optional | string | Begin date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy` |
| DEPARTMENTID | Optional | string | Department ID |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| CLASSID | Optional | string | Class ID |
| SUPDOCID | Optional | string | Attachments ID |
| BILLABLEEXPDEFAULT | Optional | boolean | Billable employee expense. Use `false` for No, `true` for Yes. (Default: `false`) |
| BILLABLEAPPODEFAULT | Optional | boolean | Billable AP/purchasing. Use `false` for No, `true` for Yes. (Default: `false`) |
| CURRENCY | Optional | string | Currency code |
| SONUMBER | Optional | string | Sales order number |
| PONUMBER | Optional | string | Purchase order number |
| POAMOUNT | Optional | currency | Purchase order amount |
| PQNUMBER | Optional | string | Purchase quote number |
| CONTRACTAMOUNT | Optional | currency | Contract amount |
| PROJECT\_RULES | Optional | `PROJECT_RULES`\[\] | Transaction rules for project. Multiple `PROJECT_RULES` elements may be passed. |
| BILLINGPRICING | Optional | string | Labor pricing option |
| BILLINGRATE | Optional | number | Labor pricing default rate |
| EXPENSEPRICING | Optional | string | Expense pricing option |
| EXPENSERATE | Optional | number | Expense pricing default rate |
| POAPPRICING | Optional | string | AP/purchasing pricing option |
| POAPRATE | Optional | number | AP/purchasing pricing default rate |
| BUDGETAMOUNT | Optional | currency | Budgeted billing amount |
| BUDGETEDCOST | Optional | currency | Budgeted cost |
| BUDGETQTY | Optional | number | Budgeted duration |
| BUDGETID | Optional | string | GL budget ID |
| INVOICEMESSAGE | Optional | string | Invoice message |
| INVOICECURRENCY | Optional | string | Invoice currency code |
| SCOPE | Optional | string | Expected scope of the work for the project. |
| INCLUSIONS | Optional | string | Inclusions as part of the project. |
| EXCLUSIONS | Optional | string | Exclusions as part of the project. |
| TERMS | Optional | string | Terms of the project. |
| SCHEDULEDSTARTDATE | Optional | string | Scheduled start date of the project in format mm/dd/yyyy. |
| ACTUALSTARTDATE | Optional | string | Actual start date of the project in format mm/dd/yyyy. |
| SCHEDULEDCOMPLETIONDATE | Optional | string | Scheduled completion date in format mm/dd/yyyy. |
| REVISEDCOMPLETIONDATE | Optional | string | Revised completion date in format mm/dd/yyyy. |
| SUBSTANTIALCOMPLETIONDATE | Optional | string | Substantial completion date in format mm/dd/yyyy. |
| ACTUALCOMPLETIONDATE | Optional | string | Actual completion date in format mm/dd/yyyy. |
| NOTICETOPROCEED | Optional | string | Date of notice to proceed in format mm/dd/yyyy. |
| RESPONSEDUE | Optional | string | Date that the response for the project is due in format mm/dd/yyyy. |
| EXECUTEON | Optional | string | Date that the project is executed on in format mm/dd/yyyy. |
| SCHEDULEDIMPACT | Optional | string | Description of the impact of the project on the schedule. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Primary contact name |

`BILLTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Bill to contact name |

`SHIPTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Ship to contact name |

`PROJECT_RULES`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RULENAME | Required | string | Transaction rule name |

* * *

Update Project
--------------

[History](https://developer.intacct.com/api/project-resource-mgmt/projects/#history-update-project)

| Release | Changes |
| --- | --- |
| 2022 Release 1 | Added CFDA, FUNDEDNAME, AGENCY, PAYER, FUNDINGOTHERID, ASSISTANCETYPE, REVRESTRICTION, RESTRICTIONEXPIRY, RESTRICTIONEXPIRATIONDATE, TIMESATISFACTIONSCHEDULED |
| 2024 Release 4 | Added SCOPE, INCLUSIONS, EXCLUSIONS, TERMS, SCHEDULEDSTARTDATE, SCHEDULEDCOMPLETIONDATE, REVISEDCOMPLETIONDATE, SUBSTANTIALCOMPLETIONDATE, ACTUALCOMPLETIONDATE, NOTICETOPROCEED, RESPONSEDUE, EXECUTEDON, SCHEDULEDIMPACT |

You can update an existing project as described here. If you want to provide observed-percent-completed information for a project, see [Project Observed Percent Completed](https://developer.intacct.com/api/project-resource-mgmt/project-observed-pct-completed/).

#### `update`

```
<update>
    <PROJECT>
        <PROJECTID>P1234</PROJECTID>
        <NAME>hello world</NAME>
    </PROJECT>
</update>
```

> Update a project with 2 transaction rules:

```
<update>
    <PROJECT>
        <PROJECTID>P1234</PROJECTID>
        <PROJECT_RULES>
            <RULENAME>Test Rule</RULENAME>
        </PROJECT_RULES>
        <PROJECT_RULES>
            <RULENAME>Test Rule2</RULENAME>
        </PROJECT_RULES>
    </PROJECT>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECT | Required | object | Object to update |

`PROJECT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Project record number to update. Required if not using `PROJECTID`. |
| PROJECTID | Optional | string | Project ID. Required if not using `RECORDNO`. |
| NAME | Optional | string | Name |
| PROJECTCATEGORY | Optional | string | Project category |
| DESCRIPTION | Optional | string | Description |
| PARENTID | Optional | string | Parent project ID |
| INVOICEWITHPARENT | Optional | boolean | Use `false` for No, `true` for Yes. (Default: `false`) |
| PROJECTTYPE | Optional | string | Project type |
| PROJECTSTATUS | Optional | string | Project status |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| CUSTOMERID | Optional | string | Customer ID |
| MANAGERID | Optional | string | Project manager employee ID |
| CUSTUSERID | Optional | string | External user ID |
| SALESCONTACTID | Optional | string | Sales contact employee ID |
| DOCNUMBER | Optional | string | Reference number |
| USERRESTRICTIONS | Optional | string | User restrictions |
| CFDA | Optional | string | Stores information about grants from the Catalog of Federal Domestic Assistance. Typically used for the CFDA number (for example, 93.053 for the Nutrition Services Incentive Program). |
| FUNDEDNAME | Optional | string | Name of the project that received funding, such as `Nutrition for children`. |
| AGENCY | Optional | string | Agency responsible for funding, such as `HHS`. |
| PAYER | Optional | string | Source of the funding, either `Federal` or `Third-party`. |
| FUNDINGOTHERID | Optional | string | Another ID for the source of the funding |
| ASSISTANCETYPE | Optional | string | Type of funding, either `Cash` or `Non-cash`. |
| REVRESTRICTION | Optional | string | Specifies how the received revenue can be restricted. Use `Purpose`, `Time`, or `NA`. |
| RESTRICTIONEXPIRY | Optional | string | Time period by which the received funds must be spent according to Federal law. Can designate years, days, or months. |
| RESTRICTIONEXPIRATIONDATE | Optional | string | Date when the received funds expire in the`mm/dd/yyyy` format. Funds often expire at the end of the fiscal year for which they were appropriated. |
| TIMESATISFACTIONSCHEDULED | Optional | boolean | If `true`, specifies that the necessary recurring entry for the release of restriction (per the schedule associated with the funding) has been created. |
| CONTACTINFO | Optional | object | Primary contact |
| BILLTO | Optional | object | Bill to contact |
| SHIPTO | Optional | object | Ship to contact |
| TERMNAME | Optional | string | Payment term |
| BILLINGTYPE | Optional | string | Billing type |
| BEGINDATE | Optional | string | Begin date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy` |
| DEPARTMENTID | Optional | string | Department ID |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| CLASSID | Optional | string | Class ID |
| SUPDOCID | Optional | string | Attachments ID |
| BILLABLEEXPDEFAULT | Optional | boolean | Billable employee expense. Use `false` for No, `true` for Yes. (Default: `false`) |
| BILLABLEAPPODEFAULT | Optional | boolean | Billable AP/purchasing. Use `false` for No, `true` for Yes. (Default: `false`) |
| CURRENCY | Optional | string | Currency code |
| SONUMBER | Optional | string | Sales order number |
| PONUMBER | Optional | string | Purchase order number |
| POAMOUNT | Optional | currency | Purchase order amount |
| PQNUMBER | Optional | string | Purchase quote number |
| CONTRACTAMOUNT | Optional | currency | Contract amount |
| PROJECT\_RULES | Optional | `PROJECT_RULES`\[\] | Transaction rules for project. Multiple `PROJECT_RULES` elements may be passed. This is a complete replace, so you must pass all existing rules you want to keep. |
| BILLINGPRICING | Optional | string | Labor pricing option |
| BILLINGRATE | Optional | number | Labor pricing default rate |
| EXPENSEPRICING | Optional | string | Expense pricing option |
| EXPENSERATE | Optional | number | Expense pricing default rate |
| POAPPRICING | Optional | string | AP/purchasing pricing option |
| POAPRATE | Optional | number | AP/purchasing pricing default rate |
| BUDGETAMOUNT | Optional | currency | Budgeted billing amount |
| BUDGETEDCOST | Optional | currency | Budgeted cost |
| BUDGETQTY | Optional | number | Budgeted duration |
| BUDGETID | Optional | string | GL budget ID |
| INVOICEMESSAGE | Optional | string | Invoice message |
| INVOICECURRENCY | Optional | string | Invoice currency code |
| SCOPE | Optional | string | Expected scope of the work for the project. |
| INCLUSIONS | Optional | string | Inclusions as part of the project. |
| EXCLUSIONS | Optional | string | Exclusions as part of the project. |
| TERMS | Optional | string | Terms of the project. |
| SCHEDULEDSTARTDATE | Optional | string | Scheduled start date of the project in format mm/dd/yyyy. |
| ACTUALSTARTDATE | Optional | string | Actual start date of the project in format mm/dd/yyyy. |
| SCHEDULEDCOMPLETIONDATE | Optional | string | Scheduled completion date in format mm/dd/yyyy. |
| REVISEDCOMPLETIONDATE | Optional | string | Revised completion date in format mm/dd/yyyy. |
| SUBSTANTIALCOMPLETIONDATE | Optional | string | Substantial completion date in format mm/dd/yyyy. |
| ACTUALCOMPLETIONDATE | Optional | string | Actual completion date in format mm/dd/yyyy. |
| NOTICETOPROCEED | Optional | string | Date of notice to proceed in format mm/dd/yyyy. |
| RESPONSEDUE | Optional | string | Date that the response for the project is due in format mm/dd/yyyy. |
| EXECUTEON | Optional | string | Date that the project is executed on in format mm/dd/yyyy. |
| SCHEDULEDIMPACT | Optional | string | Description of the impact of the project on the schedule. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Primary contact name |

`BILLTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Bill to contact name |

`SHIPTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Ship to contact name |

`PROJECT_RULES`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RULENAME | Required | string | Transaction rule name |

* * *

Delete Project
--------------

#### `delete`

```
<delete>
    <object>PROJECT</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECT` |
| keys | Required | string | Comma-separated list of project `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

