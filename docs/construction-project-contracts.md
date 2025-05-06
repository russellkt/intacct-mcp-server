Title: Project Contracts

URL Source: https://developer.intacct.com/api/construction/project-contracts/

Markdown Content:
*   [Project Contracts](https://developer.intacct.com/api/construction/project-contracts/#project-contracts)
    *   [Get Project Contract Object Definition](https://developer.intacct.com/api/construction/project-contracts/#get-project-contract-object-definition)
    *   [Query and List Project Contracts](https://developer.intacct.com/api/construction/project-contracts/#query-and-list-project-contracts)
    *   [Get a Project Contract](https://developer.intacct.com/api/construction/project-contracts/#get-a-project-contract)
    *   [Get Project Contract by ID](https://developer.intacct.com/api/construction/project-contracts/#get-project-contract-by-id)
    *   [Create Project Contract](https://developer.intacct.com/api/construction/project-contracts/#create-project-contract)
    *   [Update Project Contract](https://developer.intacct.com/api/construction/project-contracts/#update-project-contract)
    *   [Delete Project Contract](https://developer.intacct.com/api/construction/project-contracts/#delete-project-contract)
*   [Project Contract Lines](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines)
    *   [Get Project Contract Line Object Definition](https://developer.intacct.com/api/construction/project-contracts/#get-project-contract-line-object-definition)
    *   [Query and List Project Contract Lines](https://developer.intacct.com/api/construction/project-contracts/#query-and-list-project-contract-lines)
    *   [Get a Project Contract Line](https://developer.intacct.com/api/construction/project-contracts/#get-a-project-contract-line)
    *   [Create Project Contract Line](https://developer.intacct.com/api/construction/project-contracts/#create-project-contract-line)
    *   [Update Project Contract Line](https://developer.intacct.com/api/construction/project-contracts/#update-project-contract-line)
    *   [Delete Project Contract Line](https://developer.intacct.com/api/construction/project-contracts/#delete-project-contract-line)
*   [Project Contract Line Entries](https://developer.intacct.com/api/construction/project-contracts/#project-contract-line-entries)
    *   [Get Project Contract Line Entry Object Definition](https://developer.intacct.com/api/construction/project-contracts/#get-project-contract-line-entry-object-definition)
    *   [Query and List Project Contract Line Entries](https://developer.intacct.com/api/construction/project-contracts/#query-and-list-project-contract-line-entries)
    *   [Get a Project Contract Line Entry](https://developer.intacct.com/api/construction/project-contracts/#get-a-project-contract-line-entry)
    *   [Delete Project Contract Line Entry](https://developer.intacct.com/api/construction/project-contracts/#delete-project-contract-line-entry)

* * *

A project contract captures a mix of billable details for a project so that they can be included in construction project billing, including price summaries, scope, and schedule.

A project contract is composed of one or more [project contract lines](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines), each of which has [project contract line entries](https://developer.intacct.com/api/construction/project-contracts/#project-contract-line-entries). Summary values are calculated from project contract lines. Lines and entries can be tied to GL accounts for billing, and to dimensions such as tasks, items, and employees for granular budgeting, reporting, and billing.

You can create project contract lines at the same time you create a project contract, or you can add lines to an existing contract using one of the following approaches:

*   [Update the original contract](https://developer.intacct.com/api/construction/project-contracts/#update-project-contract) and provide new lines.
*   [Create new lines](https://developer.intacct.com/api/construction/project-contracts/#create-project-contract-line) independently and specify the ID of the owning project contract.

Your project contract can post entries to existing GL budgets based on the workflow types of the project contract line entries:

*   In the project contract, enable posting to GL budgets (`POSTED` = true).
*   Also in the project contract, set how dates will be used to determine posting periods (`POSTTO`).
*   Still in the project contract, specify the GL budgets that you want each Project Contract Line Entry to post to based on workflow type.
*   Budget entires are created and aggregated based on the combination of `ACCOUNTNO` and dimensions set in the Project Contract Lines.

You can create multiple project contracts for a single project.

**Note:** A project contract and its related objects contain fields that are designed to handle the requirements of construction projects. They are not the same as [contract objects used in the contracts dimension](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/)

* * *

A project contract object contains the header information about a project contract, including rollups of price totals from project contract lines, and additional information including scope and schedule. Details about the contract are contained in project contract line objects.

### Get Project Contract Object Definition

#### `lookup`

> List all the fields and relationships for the project contract object:

```
<lookup>
    <object>PROJECTCONTRACT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACT` |

* * *

### Query and List Project Contracts

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and original price for each project contract:

```
<query>
    <object>PROJECTCONTRACT</object>
    <select>
        <field>RECORDNO</field>
        <field>ORIGINALPRICE</field>
    </select>
</query> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACT` |
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

### Get a Project Contract

#### `read`

> Return all fields of a specified project contract

```
<read>
    <object>PROJECTCONTRACT</object>
    <keys>12</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACT` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project contract to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Project Contract by ID

#### `readByName`

```
<readByName>
    <object>PROJECTCONTRACT</object>
    <keys>SolarStar-01</keys>
    <fields>*</fields>
</readByName> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACT` |
| keys | Required | string | Comma-separated list of `PROJECTCONTRACTID` of the project contract to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Project Contract

[History](https://developer.intacct.com/api/construction/project-contracts/#history-create-project-contract)

| Release | Changes |
| --- | --- |
| 2023 Release 2 | Added WIPEXCLUDE |
| 2023 Release 1 | Added POSTED, POSTTO, ORIGINALGLBUDGETID, REVISIONGLBUDGETID, PENDINGGLBUDGETID, APPROVEDGLBUDGETID, FORECASTGLBUDGETID, OTHERGLBUDGETID |

The project and customer are required fields and must exist in Intacct before you can create a project contract.

#### `create`

```
<create>
    <PROJECTCONTRACT>
        <PROJECTCONTRACTID>001</PROJECTCONTRACTID>
        <NAME>API PCN</NAME>
        <PROJECTID>DIM - BTI</PROJECTID>
        <CUSTOMERID>BTI</CUSTOMERID>
        <CONTRACTDATE>2022-04-01</CONTRACTDATE>
    </PROJECTCONTRACT>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROJECTCONTRACT` | Required | object | Object type to create. |

`PROJECTCONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCONTRACTID | Required | string | User-defined ID for this project contract. Required if [document numbering](https://www.intacct.com/ia/docs/en_US/help_action/Company/Document_numbering/document-sequences-for-ids.htm) is not enabled for project contracts. |
| NAME | Required | string | Name of this project contract. |
| PROJECTID | Required | string | ID of a valid active [project](https://developer.intacct.com/api/project-resource-mgmt/projects/) that this contract will belong to. The project must be at the same entity level as the project contract, and must have a location set. You can create multiple project contracts for a single project. |
| CUSTOMERID | Required | string | `CUSTOMERID` of the [customer](https://developer.intacct.com/api/accounts-receivable/customers/) that this contact is associated with. |
| CONTRACTDATE | Required | Date | Date for this project contract. |
| BILLABLE | Optional | Boolean | Whether the project contract is billable or not.
*   `true`
*   `false` - (default) the project contract is excluded when generating invoices.

 |
| DESCRIPTION | Optional | string | Description for this project contract. |
| PROJECTCONTRACTTYPEID | Optional | string | `PROJECTCONTRACTTYPEID` of the selected [project contract type](https://developer.intacct.com/api/construction/project-contract-types/). |
| ARCHITECT.CONTACTNAME | Optional | string | Name of the architect contact. |
| SUPDOCID | Optional | string | `supdocid` of an [attachment](https://developer.intacct.com/api/company-console/attachments/) |
| STATUS | Optional | Enum | Whether the project contract is active or inactive.

*   `active` (default)
*   `inactive` - excluded when generating invoices

 |
| RETAINAGEPERCENTAGE | Optional | Decimal | Retainage percentage. Valid values are from 0.00 to 100.00 |
| LASTAPPLICATIONNO | Optional | Decimal | Displays the most recent billing application number. The default value is 0, and it is updated automatically when a new invoice for the project is generated. The value is not reset if an invoice is deleted. |
| SCOPE | Optional | string | Expected scope of work of this project contract. |
| INCLUSIONS | Optional | string | Inclusions as part of this project contract. |
| EXCLUSIONS | Optional | string | Exclusions as part of this project contract. |
| TERMS | Optional | string | Terms of this project contract. |
| SCHEDULEDSTARTDATE | Optional | Date | Scheduled start date. |
| ACTUALSTARTDATE | Optional | Date | Actual start date. |
| SCHEDULEDCOMPLETIONDATE | Optional | Date | Scheduled completion date. |
| REVISEDCOMPLETIONDATE | Optional | Date | Revised completion date. |
| SUBSTANTIALCOMPLETIONDATE | Optional | Date | Substantial completion date. |
| ACTUALCOMPLETIONDATE | Optional | Date | Actual completion date. |
| NOTICETOPROCEED | Optional | Date | Date of notice to proceed. |
| RESPONSEDUE | Optional | Date | Date response is due. |
| EXECUTEDON | Optional | Date | Date this project contract was executed. |
| SCHEDULEIMPACT | Optional | string | Impact to the schedule due to this project contract. |
| INTERNALREFNO | Optional | string | Internal reference number. |
| INTERNALINITIATEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who initiated this project contract. |
| INTERNALVERBALBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who verbally agreed to this project contract. |
| INTERNALISSUEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who issued this project contract. |
| INTERNALISSUEDON | Optional | Date | Date this project contract was issued. |
| INTERNALAPPROVEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who internally approved this project contract. |
| INTERNALAPPROVEDON | Optional | Date | Date this project contract was internally approved. |
| INTERNALSIGNEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who signed this project contract. |
| INTERNALSIGNEDON | Optional | Date | Date this project contract was internally signed. |
| INTERNALSOURCE | Optional | string | Internal source for this project contract. |
| INTERNALSOURCEREFNO | Optional | string | Internal source reference number. |
| EXTERNALREFNO | Optional | string | External reference number. |
| EXTERNALVERBALBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who verbally accepted this project contract. |
| EXTERNALAPPROVEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who approved this project contract. |
| EXTERNALAPPROVEDON | Optional | Date | Date this project contract was externally approved. |
| EXTERNALSIGNEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who signed this project contract. |
| EXTERNALSIGNEDON | Optional | Date | Date this project contract was externally signed. |
| POSTED | Optional | Boolean | Whether project contract lines should be posted as budget details to general ledger budgets.

*   `true` - Post to GL budgets. Requires a value for `POSTTO` and for at least one of the `GLBUDGETID` fields.
*   `false` - (default) Project contract lines are not posted to GL budgets.

 |
| POSTTO | Optional | string (enum) | Posting period to use when creating GL budget entries. Must be a budgetable posting period.

*   `Project contract date` (default) - Period containing the project contract date
*   `Project begin date` - Period containing the project begin date
*   `Project contract line date` - Each project contract line posts to the period containing the line date
*   `Entry effective date` - Each project contract line entry and change request entry posts to the period containing the entry effective date

 |
| ORIGINALGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `original`. The budget must have `ISPCNBUDGET` set to `true`. |
| REVISIONGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `revision`. The budget must have `ISPCNBUDGET` set to `true`. |
| PENDINGGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `pending change`. The budget must have `ISPCNBUDGET` set to `true`. |
| APPROVEDGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `approved change`. The budget must have `ISPCNBUDGET` set to `true`. |
| FORECASTGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `forecast`. The budget must have `ISPCNBUDGET` set to `true`. |
| OTHERGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `other`. The budget must have `ISPCNBUDGET` set to `true`. |
| WIPEXCLUDE | Optional | Boolean | Whether the project contract is excluded from WIP reporting.

*   `false` - (default) the project contract is included in reports.
*   `true` - the project contract is considered a template and is not included in WIP reports.

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Project Contract

[History](https://developer.intacct.com/api/construction/project-contracts/#history-update-project-contract)

| Release | Changes |
| --- | --- |
| 2023 Release 2 | Added WIPEXCLUDE |
| 2023 Release 1 | Added POSTED, POSTTO, ORIGINALGLBUDGETID, REVISIONGLBUDGETID, PENDINGGLBUDGETID, APPROVEDGLBUDGETID, FORECASTGLBUDGETID, OTHERGLBUDGETID |

The PROJECTID of a project contract can only be updated if one of these conditions is true:

*   No project contract lines exist in the contract
*   Project contract lines exist and the updated `PROJECTID` on the project contract is still the same or at a higher level in hierarchy than any project contract line project
*   The location on the updated project is the same location or a parent location of the projects on the project contract lines

> Set a project contract to inactive:

```
<update>
    <PROJECTCONTRACT>
        <RECORDNO>3</RECORDNO>
        <STATUS>inactive</STATUS>
    </PROJECTCONTRACT>
</update>
```

#### `update`

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROJECTCONTRACT` | Required | object | Object type to update |

`PROJECTCONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | ID of the project contract to update. Required if PROJECTCONTRACTID is not provided. |
| PROJECTCONTRACTID | Optional | string | User-defined ID for this project contract. Required if RECORDNO is not provided. |
| NAME | Optional | string | Name of this project contract. |
| PROJECTID | Optional | string | ID of a valid active [project](https://developer.intacct.com/api/project-resource-mgmt/projects/) that this contract will belong to. The project must be at the same entity level as the project contract, and must have a location set. You can create multiple project contracts for a single project. |
| CUSTOMERID | Optional | string | `CUSTOMERID` of the [customer](https://developer.intacct.com/api/accounts-receivable/customers/) that this contact is associated with. |
| CONTRACTDATE | Optional | Date | Date for this project contract. |
| BILLABLE | Optional | Boolean | Whether the project contract is billable or not.
*   `true`
*   `false` - (default) the project contract is excluded when generating invoices.

 |
| DESCRIPTION | Optional | string | Description for this project contract. |
| PROJECTCONTRACTTYPEID | Optional | string | `PROJECTCONTRACTTYPEID` of the selected [project contract type](https://developer.intacct.com/api/construction/project-contract-types/). |
| ARCHITECT.CONTACTNAME | Optional | string | Name of the architect contact. |
| SUPDOCID | Optional | string | `supdocid` of an [attachment](https://developer.intacct.com/api/company-console/attachments/) |
| STATUS | Optional | Enum | Whether the project contract is active or inactive.

*   `active` (default)
*   `inactive` - excluded when generating invoices

 |
| RETAINAGEPERCENTAGE | Optional | Decimal | Retainage percentage. Valid values are from 0.00 to 100.00 |
| LASTAPPLICATIONNO | Optional | Decimal | Displays the most recent billing application number. The default value is 0, and it is updated automatically when a new invoice for the project is generated. The value is not reset if an invoice is deleted. |
| SCOPE | Optional | string | Expected scope of work of this project contract. |
| INCLUSIONS | Optional | string | Inclusions as part of this project contract. |
| EXCLUSIONS | Optional | string | Exclusions as part of this project contract. |
| TERMS | Optional | string | Terms of this project contract. |
| SCHEDULEDSTARTDATE | Optional | Date | Scheduled start date. |
| ACTUALSTARTDATE | Optional | Date | Actual start date. |
| SCHEDULEDCOMPLETIONDATE | Optional | Date | Scheduled completion date. |
| REVISEDCOMPLETIONDATE | Optional | Date | Revised completion date. |
| SUBSTANTIALCOMPLETIONDATE | Optional | Date | Substantial completion date. |
| ACTUALCOMPLETIONDATE | Optional | Date | Actual completion date. |
| NOTICETOPROCEED | Optional | Date | Date of notice to proceed. |
| RESPONSEDUE | Optional | Date | Date response is due. |
| EXECUTEDON | Optional | Date | Date this project contract was executed. |
| SCHEDULEIMPACT | Optional | string | Impact to the schedule due to this project contract. |
| INTERNALREFNO | Optional | string | Internal reference number. |
| INTERNALINITIATEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who initiated this project contract. |
| INTERNALVERBALBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who verbally agreed to this project contract. |
| INTERNALISSUEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who issued this project contract. |
| INTERNALISSUEDON | Optional | Date | Date this project contract was issued. |
| INTERNALAPPROVEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who internally approved this project contract. |
| INTERNALAPPROVEDON | Optional | Date | Date this project contract was internally approved. |
| INTERNALSIGNEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who signed this project contract. |
| INTERNALSIGNEDON | Optional | Date | Date this project contract was internally signed. |
| INTERNALSOURCE | Optional | string | Internal source for this project contract. |
| INTERNALSOURCEREFNO | Optional | string | Internal source reference number. |
| EXTERNALREFNO | Optional | string | External reference number. |
| EXTERNALVERBALBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who verbally accepted this project contract. |
| EXTERNALAPPROVEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who approved this project contract. |
| EXTERNALAPPROVEDON | Optional | Date | Date this project contract was externally approved. |
| EXTERNALSIGNEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who signed this project contract. |
| EXTERNALSIGNEDON | Optional | Date | Date this project contract was externally signed. |
| POSTED | Optional | Boolean | Whether project contract lines should be posted as budget details to general ledger budgets.

*   `true` - Post to GL budgets. Requires a value for `POSTTO` and for at least one of the `GLBUDGETID` fields.
*   `false` - (default) Project contract lines are not posted to GL budgets.

 |
| POSTTO | Optional | string (enum) | Posting period to use when creating GL budget entries. Must be a budgetable posting period.

*   `Project contract date` (default) - Period containing the project contract date
*   `Project begin date` - Period containing the project begin date
*   `Project contract line date` - Each project contract line posts to the period containing the line date
*   `Entry effective date` - Each project contract line entry and change request entry posts to the period containing the entry effective date

 |
| ORIGINALGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `original`. The budget must have `ISPCNBUDGET` set to `true`. |
| REVISIONGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `revision`. The budget must have `ISPCNBUDGET` set to `true`. |
| PENDINGGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `pending change`. The budget must have `ISPCNBUDGET` set to `true`. |
| APPROVEDGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `approved change`. The budget must have `ISPCNBUDGET` set to `true`. |
| FORECASTGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `forecast`. The budget must have `ISPCNBUDGET` set to `true`. |
| OTHERGLBUDGETID | Optional | string | GL budget to post to for project contract line entries with `WFTYPE` = `other`. The budget must have `ISPCNBUDGET` set to `true`. |
| WIPEXCLUDE | Optional | Boolean | Whether the project contract is excluded from WIP reporting.

*   `false` - (default) the project contract is included in reports.
*   `true` - the project contract is considered a template and is not included in WIP reports.

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Project Contract

A project contract can only be deleted if none of the project contract lines that belong to the contract have ever been invoiced.

All project contract lines that belong to a project contract will be deleted with the project contract.

#### `delete`

```
<delete>
    <object>PROJECTCONTRACT</object>
    <keys>12</keys>
</delete> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACT` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project contract to delete. |

* * *

Project Contract Lines
----------------------

The Project Contract Line object contains header information for a billable project contract line, and is the owning object for project contract line entries. This header information includes billing information, summaries of price totals from project contract line entries, and additional information including scope and schedule.

Project contract lines can be nested by setting the `PARENTID` field to the `PROJECTCONTRACTLINEID` of the parent project contract line.

You can set each project contract line to a billing type, which affects how billing values are derived:

*   **Progress bill** (`Progress`)
    *   Each contract line has its own billing value
    *   Billing value can be updated by price changes from [project change orders](https://developer.intacct.com/api/construction/project-change-orders/)
*   **Time and material** (`TM`)
    *   Map project tasks to project contract lines for accurate time and material billing
    *   Cost plus to max
    *   Unlimited costs billed to customer
    *   Costs limited to contract line price
    *   Universal rate tables that can be applied to contract line for markup or passthrough purposes

### Get Project Contract Line Object Definition

#### `lookup`

> List all the fields and relationships for the project contract line object:

```
<lookup>
    <object>PROJECTCONTRACTLINE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINE` |

* * *

### Query and List Project Contract Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> For a specified project contract, list the record number and total revised price of each project contract line:

```
<query>
    <object>PROJECTCONTRACTLINE</object>
    <filter>
        <equalto>
            <field>PROJECTCONTRACTID</field>
            <value>001</value>
        </equalto>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>TOTALREVISEDPRICE</field>
    </select>
</query> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINE` |
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

### Get a Project Contract Line

#### `read`

> Return all fields of a specified project contract line

```
<read>
    <object>PROJECTCONTRACTLINE</object>
    <keys>12</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project contract line to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Project Contract Line

[History](https://developer.intacct.com/api/construction/project-contracts/#history-create-project-contract-line)

| Release | Changes |
| --- | --- |
| 2023 Release 2 | Added GLEXCLUDE, SUMMARIZEBILL |

#### `create`

> Create a simple project contract line:

```
<create>
    <PROJECTCONTRACTLINE>
        <PROJECTCONTRACTID>001</PROJECTCONTRACTID>
        <PROJECTCONTRACTLINEID>001-57</PROJECTCONTRACTLINEID>
        <NAME>Initial Electrical</NAME>
        <CONTRACTLINEDATE>03/17/2022</CONTRACTLINEDATE>
        <ACCOUNTNO>5001.02</ACCOUNTNO>
        <BILLINGTYPE>Progress</BILLINGTYPE>
        <MAXIMUMBILLING>Total revised price</MAXIMUMBILLING>
        <PROJECTID>DIM - BTI</PROJECTID>
        <ITEMID>Services</ITEMID>
    </PROJECTCONTRACTLINE>
</create>
```

> Create a project contract line that has two entries:

```
<create>
    <PROJECTCONTRACTLINE>
        <PROJECTCONTRACTID>002</PROJECTCONTRACTID>
        <PROJECTCONTRACTLINEID>002-08</PROJECTCONTRACTLINEID>
        <NAME>studs</NAME>
        <CONTRACTLINEDATE>03/17/2022</CONTRACTLINEDATE>
        <ACCOUNTNO>5001.02</ACCOUNTNO>
        <BILLINGTYPE>Progress</BILLINGTYPE>
        <MAXIMUMBILLING>Total revised price</MAXIMUMBILLING>
        <PROJECTID>DIM - BTI</PROJECTID>
        <ITEMID>Framing</ITEMID>
        <PROJECTCONTRACTLINEENTRIES>
            <PROJECTCONTRACTLINEENTRY>
                <WFTYPE>original</WFTYPE>
                <PRICE>120</PRICE>
                <PRICEEFFECTIVEDATE>01/01/2022</PRICEEFFECTIVEDATE>
            </PROJECTCONTRACTLINEENTRY>
            <PROJECTCONTRACTLINEENTRY>
                <WFTYPE>revision</WFTYPE>
                <PRICE>220</PRICE>
                <PRICEEFFECTIVEDATE>03/17/2022</PRICEEFFECTIVEDATE>
            </PROJECTCONTRACTLINEENTRY>
        </PROJECTCONTRACTLINEENTRIES>
    </PROJECTCONTRACTLINE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROJECTCONTRACTLINE` | Required | object | Object type to create. |

`PROJECTCONTRACTLINE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCONTRACTID | Required | string | `PROJECTCONTRACTID` of the selected project contract that this line belongs to. Must be an active project. |
| PROJECTCONTRACTLINEID | Required | string | User-defined unique\* ID.  
The PROJECTCONTRACTLINEID must be unique among all the project contract lines for the specified project contract. A PROJECTCONTRACTID.PROJECTCONTRACTLINEID combination must be unique within a company. |
| NAME | Required | string | Name of this project contract line. |
| DESCRIPTION | Optional | string | Description of this project contract line. |
| PARENTID | Optional | string | `PROJECTCONTRACTLINEID` of the parent project contract line, for nesting project contract lines. Project contract lines do not roll up to parents. Must be an active project contract line. |
| PROJECTCONTRACTLINEENTRIES | Optional | array of [PROJECTCONTRACTLINEENTRY](https://developer.intacct.com/api/construction/project-contracts/#project-contract-line-entries) | Project contract line entries. |
| STATUS | Optional | Enum | Status of the project contract line.
*   `active` (default)
*   `inactive` when generating invoices.

 |
| CONTRACTLINEDATE | Required | Date | Date |
| ACCOUNTNO | Required | string | `ACCOUNTNO` of the GL Account for this project contract line. Must be an active account. |
| RETAINAGEPERCENTAGE | Optional | Decimal | Retainage percentage. |
| BILLABLE | Optional | Boolean | Whether the project contract line is billable or not.

*   `false` (default) The project contract line is excluded when generating invoices.
*   `true`

 |
| BILLINGTYPE | Required | Enum | Billing Type.

*   `Progress` - Progress billing (default)
*   `TM` - Time and material

 |
| MAXIMUMBILLING | Required | Enum | Maximum billing method.

*   `Total revised price` (default) This is the only valid value when BILLINGTYPE is set to `Progress`.
*   `Specified amount`
*   `No maximum`

Validation and processing rules:

*   When BILLINGTYPE is set to `Progress` the MAXIMUMBILLING must be set to `Total revised price`.
*   When the BILLINGTYPE is set to `TM` and the MAXIMUMBILLING is set to `Specified amount`, the amount billed against this project contract line cannot exceed the MAXIMUMBILLINGAMOUNT value during invoice generation.
*   When the BILLINGTYPE is set to `TM` and the MAXIMUMBILLING is set to `No maximum`, the MAXIMUMBILLINGAMOUNT value is ignored during invoice generation, and the invoice amount against this project contract line does not have a limit.

 |
| MAXIMUMBILLINGAMOUNT | Optional | Currency | The maximum amount that can be billed against this project contract line. See MAXIMUMBILLING for validation and processing rules. |
| SUMMARIZEBILL | Optional | Boolean | Whether the project contract line is a summary line or not.

*   `false` (default) The project contract line is not a summary line.
*   `true` T&M expenses can be assigned to this line, but the billing output for this line will be to a single OE invoice line. The Extended price for this line will be the sum of all the billed expenses associated to this project contract line. All related expenses will still be marked as billed.

 |
| SCOPE | Optional | string | Expected scope of work as part of this project contract line. |
| INCLUSIONS | Optional | string | Inclusions. |
| EXCLUSIONS | Optional | string | Exclusions. |
| TERMS | Optional | string | Terms. |
| SCHEDULEDSTARTDATE | Optional | Date | Scheduled start date. |
| ACTUALSTARTDATE | Optional | Date | Actual start date. |
| SCHEDULEDCOMPLETIONDATE | Optional | Date | Scheduled completion date. |
| REVISEDCOMPLETIONDATE | Optional | Date | Revised completion date. |
| SUBSTANTIALCOMPLETIONDATE | Optional | Date | Substantial completion date. |
| ACTUALCOMPLETIONDATE | Optional | Date | Actual completion date. |
| NOTICETOPROCEED | Optional | Date | Date of notice to proceed. |
| RESPONSEDUE | Optional | Date | Response due date. |
| EXECUTEDON | Optional | Date | Date this project contract line was executed. |
| SCHEDULEIMPACT | Optional | string | Impact to the schedule due to this project contract line. |
| INTERNALREFNO | Optional | string | Internal reference number. |
| INTERNALINITIATEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who initiated this project contract line. |
| INTERNALVERBALBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who verbally agreed to this project contract line. |
| INTERNALISSUEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who issued this project contract line. |
| INTERNALISSUEDON | Optional | Date | Date this project contract line was issued. |
| INTERNALAPPROVEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who internally approved this project contract line. |
| INTERNALAPPROVEDON | Optional | Date | Date this project contract line was internally approved. |
| INTERNALSIGNEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who signed this project contract line. |
| INTERNALSIGNEDON | Optional | Date | Date this project contract line was signed internally. |
| INTERNALSOURCE | Optional | string | Internal source. |
| INTERNALSOURCEREFNO | Optional | string | Internal source reference number. |
| EXTERNALREFNO | Optional | string | External reference number |
| EXTERNALVERBALBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who verbally accepted this project contract line. |
| EXTERNALAPPROVEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who approved this project contract line. |
| EXTERNALAPPROVEDON | Optional | Date | Date this project contract line was externally approved. |
| EXTERNALSIGNEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who signed this project contract line. |
| EXTERNALSIGNEDON | Optional | Date | Date this project contract line was externally signed. |
| SUPDOCID | Optional | string | [Attachment ID](https://developer.intacct.com/api/company-console/attachments/) |
| DEFAULTRATETABLEID | Optional | string | `RATETABLEID` of the default [rate table](https://developer.intacct.com/api/construction/rate-tables/) that is used when other rate tables aren’t specified. BILLINGTYPE must be `TM`. |
| TSRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for timesheets. BILLINGTYPE must be `TM`. |
| PORATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for purchase orders. BILLINGTYPE must be `TM`. |
| APRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for accounts payable. BILLINGTYPE must be `TM`. |
| GLRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for general ledger. BILLINGTYPE must be `TM`. |
| CCRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for credit card purchases. BILLINGTYPE must be `TM`. |
| EERATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for employee expenses. BILLINGTYPE must be `TM`. |
| CLASSID | Optional | string | `CLASSID` of the selected [class](https://developer.intacct.com/api/company-console/classes/). |
| CONTRACTID | Optional | string | `CONTRACTID` of the selected [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of the selected [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| DEPARTMENTID | Optional | string | `DEPARTMENTID` of the [department](https://developer.intacct.com/api/company-console/departments/) associated with this project contract line. |
| EMPLOYEEID | Optional | string | `EMPLOYEEID` of the selected [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Required | string | `ITEMID` of the selected [item](https://developer.intacct.com/api/inventory-control/items/). Only active Items are allowed that are of Non-Inventory or Non-Inventory (Sales only) type. |
| PROJECTID | Required | string | `PROJECTID` for a valid, active [project](https://developer.intacct.com/api/project-resource-mgmt/projects/) that is same as the project on the project contract or a descendant of that project. |
| TASKID | Optional | string | `TASKID` of the [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/) related to this project contract line. `TASKID` must be a task under the same project or parent project. You cannot use the same `TASKID` in more than one project contract line. |
| VENDORID | Optional | string | `VENDORID` of the selected [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of the selected [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |
| GLEXCLUDE | Optional | Boolean | Whether to exclude all values for the project contract line from posting to a GL budget, including any linked change request entries.

*   `false` - (default) the project contract line can post to a GL budget.
*   `true` - the project contract does not post to a GL budget.

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Project Contract Line

[History](https://developer.intacct.com/api/construction/project-contracts/#history-update-project-contract-line)

| Release | Changes |
| --- | --- |
| 2023 Release 2 | Added GLEXCLUDE, SUMMARIZEBILL |

#### `update`

The PROJECTID of a project contract line can only be updated if one of these conditions is true:

*   No project contract line lines exist in the contract
*   Project contract lines exist and the updated `PROJECTID` on the project contract line is still the same or at a higher level in hierarchy than any project contract line line project
*   The location on the updated project is the same location or a parent location of the projects on the project contract line lines

When a project contract line has been saved and project contract line entries exist, all totals in the summary section of the project contract line need to be recalculated based on all entries saved to this project contract line.

> Set a project contract line to inactive:

```
<update>
    <PROJECTCONTRACTLINE>
        <RECORDNO>27</RECORDNO>
        <STATUS>inactive</STATUS>
    </PROJECTCONTRACTLINE>
</update>
```

> Updates the same project contract line, modifying the amount of an existing entry and adding a new entry:

```
<update>
    <PROJECTCONTRACTLINE>
        <RECORDNO>27</RECORDNO>
        <PROJECTCONTRACTLINEENTRIES>
            <PROJECTCONTRACTLINEENTRY>
                <RECORDNO>173</RECORDNO>
                <WFTYPE>revision</WFTYPE>
                <PRICE>300</PRICE>
                <PRICEEFFECTIVEDATE>04/01/2022</PRICEEFFECTIVEDATE>
            </PROJECTCONTRACTLINEENTRY>
            <PROJECTCONTRACTLINEENTRY>
                <WFTYPE>original</WFTYPE>
                <PRICE>179</PRICE>
                <PRICEEFFECTIVEDATE>04/01/2022</PRICEEFFECTIVEDATE>
            </PROJECTCONTRACTLINEENTRY>
        </PROJECTCONTRACTLINEENTRIES>
    </PROJECTCONTRACTLINE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `PROJECTCONTRACTLINE` | Required | object | Object type to update. |

`PROJECTCONTRACTLINE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | ID of the project contract line to update. |
| PROJECTCONTRACTLINEID | Optional | string | User-defined ID for this project contract line. |
| NAME | Optional | string | Name of this project contract line. |
| DESCRIPTION | Optional | string | Description of this project contract line. |
| PARENTID | Optional | string | `PROJECTCONTRACTLINEID` of the parent project contract line, for nesting project contract lines. Must be an active project contract line. |
| PROJECTCONTRACTLINEENTRIES | Optional | array of [PROJECTCONTRACTLINEENTRY](https://developer.intacct.com/api/construction/project-contracts/#project-contract-line-entries) | Project contract line entries. |
| STATUS | Optional | Enum | Status of the project contract line.
*   `active` (default)
*   `inactive` when generating invoices.

 |
| CONTRACTLINEDATE | Optional | Date | Date |
| ACCOUNTNO | Optional | string | `ACCOUNTNO` of the GL Account for this project contract line. Must be an active account. |
| RETAINAGEPERCENTAGE | Optional | Decimal | Retainage percentage. |
| BILLABLE | Optional | Boolean | Whether the project contract line is billable or not.

*   `false` (default) The project contract line is excluded when generating invoices.
*   `true`

 |
| BILLINGTYPE | Optional | Enum | Billing Type.

*   `Progress` (default)
*   `TM`

 |
| MAXIMUMBILLING | Optional | Enum | Maximum billing method.

*   `Total revised price` (default) This is the only valid value when BILLINGTYPE is set to `Progress`.
*   `Specified amount`
*   `No maximum`

Validation and processing rules:

*   When BILLINGTYPE is set to `Progress` the MAXIMUMBILLING must be set to `Total revised price`.
*   When the BILLINGTYPE is set to `TM` and the MAXIMUMBILLING is set to `Specified amount`, the amount billed against this project contract line cannot exceed the MAXIMUMBILLINGAMOUNT value during invoice generation.
*   When the BILLINGTYPE is set to `TM` and the MAXIMUMBILLING is set to `No maximum`, the MAXIMUMBILLINGAMOUNT value is ignored during invoice generation, and the invoice amount against this project contract line does not have a limit.

 |
| MAXIMUMBILLINGAMOUNT | Optional | Currency | The maximum amount that can be billed against this project contract line. See MAXIMUMBILLING for validation and processing rules. |
| SUMMARIZEBILL | Optional | Boolean | Whether the project contract line is a summary line or not.

*   `false` (default) The project contract line is not a summary line.
*   `true` T&M expenses can be assigned to this line, but the billing output for this line will be to a single OE invoice line. The Extended price for this line will be the sum of all the billed expenses associated to this project contract line. All related expenses will still be marked as billed.

 |
| SCOPE | Optional | string | Expected scope of work as part of this project contract line. |
| INCLUSIONS | Optional | string | Inclusions. |
| EXCLUSIONS | Optional | string | Exclusions. |
| TERMS | Optional | string | Terms. |
| SCHEDULEDSTARTDATE | Optional | Date | Scheduled start date. |
| ACTUALSTARTDATE | Optional | Date | Actual start date. |
| SCHEDULEDCOMPLETIONDATE | Optional | Date | Scheduled completion date. |
| REVISEDCOMPLETIONDATE | Optional | Date | Revised completion date. |
| SUBSTANTIALCOMPLETIONDATE | Optional | Date | Substantial completion date. |
| ACTUALCOMPLETIONDATE | Optional | Date | Actual completion date. |
| NOTICETOPROCEED | Optional | Date | Date of notice to proceed. |
| RESPONSEDUE | Optional | Date | Response due date. |
| EXECUTEDON | Optional | Date | Date this project contract line was executed. |
| SCHEDULEIMPACT | Optional | string | Impact to the schedule due to this project contract line. |
| INTERNALREFNO | Optional | string | Internal reference number. |
| INTERNALINITIATEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who initiated this project contract line. |
| INTERNALVERBALBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who verbally agreed to this project contract line. |
| INTERNALISSUEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who issued this project contract line. |
| INTERNALISSUEDON | Optional | Date | Date this project contract line was issued. |
| INTERNALAPPROVEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who internally approved this project contract line. |
| INTERNALAPPROVEDON | Optional | Date | Date this project contract line was internally approved. |
| INTERNALSIGNEDBY | Optional | string | `EMPLOYEEID` of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who signed this project contract line. |
| INTERNALSIGNEDON | Optional | Date | Date this project contract line was signed internally. |
| INTERNALSOURCE | Optional | string | Internal source. |
| INTERNALSOURCEREFNO | Optional | string | Internal source reference number. |
| EXTERNALREFNO | Optional | string | External reference number |
| EXTERNALVERBALBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who verbally accepted this project contract line. |
| EXTERNALAPPROVEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who approved this project contract line. |
| EXTERNALAPPROVEDON | Optional | Date | Date this project contract line was externally approved. |
| EXTERNALSIGNEDBY | Optional | string | `CONTACTNAME` of the [contact](https://developer.intacct.com/api/company-console/contacts/) who signed this project contract line. |
| EXTERNALSIGNEDON | Optional | Date | Date this project contract line was externally signed. |
| SUPDOCID | Optional | string | [Attachment ID](https://developer.intacct.com/api/company-console/attachments/) |
| DEFAULTRATETABLEID | Optional | string | `RATETABLEID` of the default [rate table](https://developer.intacct.com/api/construction/rate-tables/) that is used when other rate tables aren’t specified. BILLINGTYPE must be `TM`. |
| TSRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for timesheets. BILLINGTYPE must be `TM`. |
| PORATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for purchase orders. BILLINGTYPE must be `TM`. |
| APRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for accounts payable. BILLINGTYPE must be `TM`. |
| GLRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for general ledger. BILLINGTYPE must be `TM`. |
| CCRATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for credit card purchases. BILLINGTYPE must be `TM`. |
| EERATETABLEID | Optional | string | `RATETABLEID` of the [rate table](https://developer.intacct.com/api/construction/rate-tables/) for employee expenses. BILLINGTYPE must be `TM`. |
| CLASSID | Optional | string | `CLASSID` of the selected [class](https://developer.intacct.com/api/company-console/classes/). |
| CONTRACTID | Optional | string | `CONTRACTID` of the selected [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of the selected [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| DEPARTMENTID | Optional | string | `DEPARTMENTID` of the [department](https://developer.intacct.com/api/company-console/departments/) associated with this project contract line. |
| EMPLOYEEID | Optional | string | `EMPLOYEEID` of the selected [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | `ITEMID` of the selected [item](https://developer.intacct.com/api/inventory-control/items/) Only active Items are allowed that are of Non-Inventory or Non-Inventory (Sales only) type. |
| PROJECTID | Optional | string | `PROJECTID` for a valid, active [project](https://developer.intacct.com/api/project-resource-mgmt/projects/) that is same as the project on the project contract or a descendant of that project. |
| TASKID | Optional | string | `TASKID` of the [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/) related to this project contract line. |
| VENDORID | Optional | string | `VENDORID` of the selected [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of the selected [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |
| GLEXCLUDE | Optional | Boolean | Whether to exclude all values for the project contract line from posting to a GL budget, including any linked change request entries.

*   `false` - (default) the project contract line can post to a GL budget.
*   `true` - the project contract does not post to a GL budget.

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Project Contract Line

A project contract line can only be deleted if it has never been invoiced.

All project contract line entries that belong to a project contract line will be deleted with the project contract line.

#### `delete`

```
<delete>
    <object>PROJECTCONTRACT</object>
    <keys>12</keys>
</delete> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project contract line to delete. |

Project Contract Line Entries
-----------------------------

A project contract line entry object is owned by a project contract line object and contains the information about a single line item on a project contract line. This information includes the price and markup of the item, a workflow type, and a price effective date.

Project contract line entries can only be created and updated through the owning project contract line objects.

`PROJECTCONTRACTLINEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| WFTYPE | Required | string (enum) | Workflow type of the project contract line entry. If `POSTED` = `true` in the PROJECTCONTRACT object, this value determines which GL budget this entry will post to.
*   `original` (default)
*   `revision`
*   `forecast`
*   `other`

 |
| PRICEEFFECTIVEDATE | Required | Date | Price effective date. |
| PRICE | Optional | Currency | The price of the project contract line entry. If a value is not provided, it is calculated as QTY \* UNITPRICE. |
| QTY | Optional | Decimal | Quantity |
| UNITPRICE | Optional | Numeric / Currency with Decimal 10 | Unit rate for price. |
| PRICEMARKUPPERCENT | Optional | Numeric | Percent of the price that will be applied as markup. |
| PRICEMARKUPAMOUNT | Optional | Numeric | Fixed amount to be applied as markup. If a value is not provided, it is calculated as PRICE \* PRICEMARKUPPERCENT / 100. |
| EUOM | Optional | string | External Unit of Measure. |
| MEMO | Optional | string | Memo |
| CLASSID | Optional | string | ID of the selected [class](https://developer.intacct.com/api/company-console/classes/) |
| CONTRACTID | Optional | string | ID of the selected [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) |
| COSTTYPEID | Optional | string | ID of the selected [cost type](https://developer.intacct.com/api/construction/cost-types/). You must also supply a TASKID, and the cost type must belong to the task. |
| DEPARTMENTID | Optional | string | ID of the selected [department](https://developer.intacct.com/api/company-console/departments/). |
| EMPLOYEEID | Optional | string | ID of the selected [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | ID of the selected [item](https://developer.intacct.com/api/inventory-control/items/). |
| PROJECTID | Optional | string | ID of a valid, active [project](https://developer.intacct.com/api/project-resource-mgmt/projects/) that is same as the project on the project contract or a descendant of that project. |
| TASKID | Optional | string | ID of the [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/) related to this project contract line entry. You must also supply a PROJECTID, and the task must belong to the project. |
| VENDORID | Optional | string | ID of the selected [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | ID of the selected [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

### Get Project Contract Line Entry Object Definition

#### `lookup`

> List all the fields and relationships for the project contract line entry object:

```
<lookup>
    <object>PROJECTCONTRACTLINEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINEENTRY` |

* * *

### Query and List Project Contract Line Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and vendor for each project contract line entry:

```
<query>
    <object>PROJECTCONTRACTLINEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>VENDORID</field>
    </select>
</query> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINEENTRY` |
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

### Get a Project Contract Line Entry

#### `read`

> Return all fields of a specified project contract line entry

```
<read>
    <object>PROJECTCONTRACTLINEENTRY</object>
    <keys>137</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project contract line entry to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Delete Project Contract Line Entry

#### `delete`

```
<delete>
    <object>PROJECTCONTRACTLINEENTRY</object>
    <keys>7</keys>
</delete> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCONTRACTLINEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project contract line entry to delete. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

