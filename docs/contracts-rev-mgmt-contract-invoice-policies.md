Title: Contract Invoice Policies

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/

Markdown Content:
*   [Get Contract Invoice Policy Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#get-contract-invoice-policy-object-definition)
*   [Query and List Contract Invoice Policies](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#query-and-list-contract-invoice-policies)
*   [Query and List Contract Invoice Policies (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#query-and-list-contract-invoice-policies-legacy)
*   [Get Contract Invoice Policy](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#get-contract-invoice-policy)
*   [Create Contract Invoice Policy](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#create-contract-invoice-policy)
*   [Update Contract Invoice Policy](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#update-contract-invoice-policy)
*   [Delete Contract Invoice Policy](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#delete-contract-invoice-policy)

* * *

A Contract Invoice Policy is a saved filter set that lets you repeatedly generate contract invoices based on specified parameters. For example, you might create an invoice policy to generate invoices for a particular customer or item type, or for the work of a specific employee, or you might have an invoice policy for invoices associated with a particular project.

You can set a schedule on contract invoice policies to automatically generate invoices at regular intervals, such as every month.

Note this object has been renamed from _Contract Invoice Filter Sets_ (`GENINVOICEFILTERS`) to _Contract Invoice Policy_ (`GENINVOICEPOLICY`).

* * *

Get Contract Invoice Policy Object Definition
---------------------------------------------

#### `lookup`

> List all the fields and relationships for the contract invoice policy object:

```
<lookup>
    <object>GENINVOICEPOLICY</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPOLICY` |
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

* * *

Query and List Contract Invoice Policies
----------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and dynamic ‘as of date’ for each contract invoice policies:

```
<query>
    <object>GENINVOICEPOLICY</object>
    <select>
        <field>RECORDNO</field>
        <field>SETASOFDATE</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPOLICY` |
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
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

* * *

Query and List Contract Invoice Policies (Legacy)
-------------------------------------------------

```
<readByQuery>
    <object>GENINVOICEPOLICY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

### ReadByQuery

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPOLICY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

* * *

Get Contract Invoice Policy
---------------------------

#### `read`

```
<read>
    <object>GENINVOICEPOLICY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GENINVOICEPOLICY` |
| keys | Required | string | `RECORDNO` of the policy to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| docparid | Optional | string | Used to indicate the document type, such as `Inventory Transfer`, `Sales Order`, `Purchase Order` and so forth. You must use this to take advantage of any custom fields on the specified document type. |

Create Contract Invoice Policy
------------------------------

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#history-create-contract-invoice-policy)

| Release | Changes |
| --- | --- |
| 2022 Release 3 | Added scheduling fields SCHEDULED, STARTDATE, REPEATBY, and REPEATINTERVAL |
| 2022 Release 2 | Renamed Contract Filter Set to Contract Invoice Policy |
| 2021 Release 3 | Added BILLTO as a value for INVOICEBY |
| 2020 Release 4 | Added CUSTOMER as a value for INVOICEBY |
| 2019 Release 4 | Added INVOICEBY |

#### `create`

> Creates an invoice policy for the given contract:

```
<create>
    <GENINVOICEPOLICY>
        <NAME>My policy</NAME>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <INCLUDECONTRACTS>true</INCLUDECONTRACTS>
        <INCLUDECONTRACTUSAGE>true</INCLUDECONTRACTUSAGE>
    </GENINVOICEPOLICY>
</create>
```

> Creates an invoice policy for the same contract but requests a separate invoice for each project associated with the contract:

```
<create>
    <GENINVOICEPOLICY>
        <NAME>My policy per project</NAME>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <INVOICEBY>CONTRACT#~#PROJECT</INVOICEBY>
        <INCLUDECONTRACTS>true</INCLUDECONTRACTS>
        <INCLUDECONTRACTUSAGE>true</INCLUDECONTRACTUSAGE>
    </GENINVOICEPOLICY>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GENINVOICEPOLICY | Required | string | Type of object to create. |

`GENINVOICEPOLICY`

##### General Properties

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | A short identifier for the invoice policy. This ID will appear in any applicable invoice policy selection lists in Intacct. You can’t change the Name after you save the invoice policy. |
| DESCRIPTION | Optional | string | A meaningful description of the invoice policy. |
| DOCPARID | Optional | string | The `DOCID` of the [transaction definition](https://developer.intacct.com/api/order-entry/order-entry-transaction-definitions/) to use for invoices generated using this invoice policy. The definition must be enabled for Contracts and be defined to post to Accounts Receivable and have “Track line item discount/surcharge” set to true. |
| SETASOFDATE | Optional | string | As-of date to be used when generating invoices. For example, if `SETASOFDATE` = `End of this month` and this month is June, Intacct will set the As of date to June 30 when you generate invoices using this policy.
*   `Today`
*   `Yesterday`
*   `End of this week`
*   `End of last week`
*   `Beginning of this month`
*   `End of this month`
*   `End of last month`

(Default: today’s date) |
| INVOICEBY | Optional | string | Specifies how the invoices are organized and consolidated:

*   `CUSTOMER#~#CONTRACT` - A separate invoice for each contract (Legacy value: `CONTRACT`). (default)
*   `CUSTOMER#~#CONTRACT#~#BILLTO` - A separate invoice for each contract per contract line level Bill to contact.
*   `CUSTOMER` - A separate invoice for each customer
*   `CUSTOMER#~#BILLTO` - A separate invoice for each customer per contract line level Bill to contact.
*   `CUSTOMER#~#CONTRACT#~#PROJECT` - A separate invoice for each project associated with the contract. (Legacy value: `PROJECT#~#CONTRACT` or `CONTRACT#-#PROJECT`)
*   `CUSTOMER#~#CONTRACT#~#BILLTO#~#PROJECT` - A separate invoice for each project associated with the contract per contract line level Bill to contact.

 |
| PRICELISTID | Optional | string | The `NAME` of an [order entry price list](https://developer.intacct.com/api/order-entry/price-lists/) to use to override pricing for billable transactions related to projects. This price list overrides any price list set on the selected transaction definition, customer, and so on. This field is only applicable if your company is subscribed to Projects. |
| STATUS | Optional | string | Status for the policy itself.

*   `active` - the policy can be used to generate invoices (default)
*   `inactive` - the policy cannot be used to generate invoices

 |

##### Filters

Use filters to define the work and costs to be included in invoices. For example, you can create a contract invoice policy for all work on a specific contract, or one that generates invoices for work done on a specific contract at a specified location, or invoices for an item.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/) to only include work tagged with the specified class. |
| CLASSGROUPID | Optional | string | `ID` of a [class group](https://developer.intacct.com/api/company-console/class-groups/) to only include work tagged with any of the classes in that group. |
| CONTRACTID | Optional | string | `CONTRACTID` of a [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) to only include work for the specified contract. |
| CONTRACTGROUPID | Optional | string | The `ID` of a [contract group](https://developer.intacct.com/api/contracts-rev-mgmt/contract-groups/) to generate invoices for the specified contract group. |
| CONTRACTTYPEID | Optional | string | The `NAME` of a [contract type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/) to only include work from contacts with that type. |
| CURRENCY | Optional | currency | Set a currency code to only include invoices from contracts that use that transaction currency. Only applicable to multi-currency companies. |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/) to generate invoices for a specified customer. |
| CUSTOMERTYPEID | Optional | string | The `NAME` of a [customer type](https://developer.intacct.com/api/accounts-receivable/customer-types/) to generate invoices for a specified customer type. |
| CUSTOMERGROUPID | Optional | string | `ID` of a [customer group](https://developer.intacct.com/api/accounts-receivable/customer-groups/) to only include work done for customers in that group. |
| DEPARTMENTID | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/) to generate invoices for that department. |
| DEPARTMENTGROUPID | Optional | string | `ID` of a [department group](https://developer.intacct.com/api/company-console/department-groups/) to only include work assocaited with departments in that group. |
| EMPLOYEEID | Optional | string | `EMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/) to generate invoices for the work of that employee. |
| EMPLOYEEGROUPID | Optional | string | `ID` of an [employee group](https://developer.intacct.com/api/employee-expenses/employee-groups/) to generate invoices for the work of employees in that group. |
| ITEMID | Required | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/) to generate invoices for a specified item. |
| ITEMGROUPID | Optional | string | `ID` of an [item group](https://developer.intacct.com/api/inventory-control/item-groups/) to generate invoices for items in a specified item group. |
| LOCATIONID | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/) to restrict invoices to the specified location. |
| LOCATIONGROUPID | Optional | string | `ID` of a [location group](https://developer.intacct.com/api/company-console/location-groups/) to only include work done at any of the locations in that group. |
| PROJECTID | Optional | string | `PROJECTID` of an active [project](https://developer.intacct.com/api/project-resource-mgmt/projects/) to generate invoices for that project. |
| PROJECTTYPEID | Optional | string | The `NAME` of an active [project type](https://developer.intacct.com/api/project-resource-mgmt/project-types/) to generate invoices for that project type. |
| PROJECTGROUPID | Optional | string | `ID` of a [project group](https://developer.intacct.com/api/project-resource-mgmt/project-groups/) to generate invoices for all projects in that group. |
| PROJECTMANAGERID | Optional | string | `EMPLOYEEID` of the project manager to generate invoices for projects associated with that project manager. |

##### Transactions to include

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| INCLUDECONTRACTS | Optional | Boolean | Whether contract transactions are included in invoices.
*   `false` - contract transactions are not included (default)
*   `true` - contract transactions are included

 |
| INCLUDECONTRACTUSAGE | Optional | Boolean | Whether [contract usage transactions](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/) are included in invoices.

*   `false` - usage transactions are not included (default)
*   `true` - usage transactions are included

 |
| INCLUDETIMESHEETS | Optional | string | Whether [timesheets](https://developer.intacct.com/api/project-resource-mgmt/timesheets/) are included in invoices.

*   `false` - timesheets are not included (default)
*   `true` - timesheets are included

 |
| INCLUDEEXPENSES | Optional | string | Whether [employee expenses](https://developer.intacct.com/api/employee-expenses/expense-reports/) are included in invoices.

*   `false` - expenses are not included (default)
*   `true` - expenses are included

 |
| INCLUDEAPBILLS | Optional | string | Whether [Accounts Payable bills](https://developer.intacct.com/api/accounts-payable/bills/) are included in invoices.

*   `false` - AP bills are not included (default)
*   `true` - AP bills are included

 |
| INCLUDEPODOCUMENTS | Optional | string | Whether [purchasing transactions](https://developer.intacct.com/api/purchasing/purchasing-transactions/) are included in invoices.

*   `false` - purchasing transactions are not included (default)
*   `true` - purchasing transactions are included

 |

##### Exception filters

**Note:** The Exception filters are for previewing or reporting only - you won’t be able to generate invoices that include unapproved transactions or transactions with missing prices.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APPROVALSTATUS | Optional | string | Filter to see only approved or unapproved transactions.
*   `Approved` - Billable transactions that are approved.
*   `Unapproved` - Billable transactions (such as vendor invoices, expense reports, and timesheets) that have not posted to the GL and are either in a Draft, Submitted, or Declined State.
*   `Both` - Ignore Approval status when filtering results.

 |
| BLANKPRICESONLY | Optional | string | Include only billable transactions that are missing prices. Use this option to create an exception report.

*   `false` (default)
*   `true`

 |

##### Scheduling

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SCHEDULED | Optional | Boolean | Specifies if the invoice policy is set to automatically generate invoices using the `STARTDATE`, `REPEATBY` and `REPEATINTERVAL` values.
*   `false` (default)
*   `true`

 |
| STARTDATE | Optional | string | The start date for automatically generating invoices, in `mm/dd/yyyy` format. Required if `SCHEDULED` is true. |
| REPEATBY | Optional | string | Unit of time for schedule repeat frequency. Required if `SCHEDULED` is true.

*   `Days`
*   `Weeks`
*   `Months`

 |
| REPEATINTERVAL | Optional | integer | The schedule repeat interval. Required if `SCHEDULED` is true. |

* * *

Update Contract Invoice Policy
------------------------------

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contract-invoice-policies/#history-update-contract-invoice-policy)

| Release | Changes |
| --- | --- |
| 2022 Release 3 | Added scheduling fields SCHEDULED, STARTDATE, REPEATBY, and REPEATINTERVAL |
| 2022 Release 2 | Renamed Contract Filter Set to Contract Invoice Policy |
| 2021 Release 3 | Added BILLTO as a value for INVOICEBY |
| 2020 Release 4 | Added CUSTOMER as a value for INVOICEBY |
| 2019 Release 4 | Added INVOICEBY |

#### `update`

```
<update>
    <GENINVOICEPOLICY>
        <RECORDNO>1</RECORDNO>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <SCHEDULED>true</SCHEDULED>
        <INCLUDECONTRACTS>true</INCLUDECONTRACTS>
    </GENINVOICEPOLICY>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GENINVOICEPOLICY | Required | string | Type of object to update. |

`GENINVOICEPOLICY`

##### General Properties

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of the policy to update. Required if not using `NAME`. |
| NAME | Optional | string | Name of the policy to update. Required if not using `RECORDNO`. Note that you cannot change a policy name. |
| DESCRIPTION | Optional | string | A meaningful description of the invoice policy. |
| DOCPARID | Optional | string | The `DOCID` of the [transaction definition](https://developer.intacct.com/api/order-entry/order-entry-transaction-definitions/) to use for invoices generated using this invoice policy. The definition must be enabled for Contracts and be defined to post to Accounts Receivable and have “Track line item discount/surcharge” set to true. |
| SETASOFDATE | Optional | string | As-of date to be used when generating invoices. For example, if `SETASOFDATE` = `End of this month` and this month is June, Intacct will set the As of date to June 30 when you generate invoices using this policy.
*   `Today`
*   `Yesterday`
*   `End of this week`
*   `End of last week`
*   `Beginning of this month`
*   `End of this month`
*   `End of last month`

(Default: today’s date) |
| INVOICEBY | Optional | string | Specifies how the invoices are organized and consolidated:

*   `CUSTOMER#~#CONTRACT` - A separate invoice for each contract (Legacy value: `CONTRACT`). (default)
*   `CUSTOMER#~#CONTRACT#~#BILLTO` - A separate invoice for each contract per contract line level Bill to contact.
*   `CUSTOMER` - A separate invoice for each customer
*   `CUSTOMER#~#BILLTO` - A separate invoice for each customer per contract line level Bill to contact.
*   `CUSTOMER#~#CONTRACT#~#PROJECT` - A separate invoice for each project associated with the contract. (Legacy value: `PROJECT#~#CONTRACT` or `CONTRACT#-#PROJECT`)
*   `CUSTOMER#~#CONTRACT#~#BILLTO#~#PROJECT` - A separate invoice for each project associated with the contract per contract line level Bill to contact.

 |
| PRICELISTID | Optional | string | The `NAME` of an [order entry price list](https://developer.intacct.com/api/order-entry/price-lists/) to use to override pricing for billable transactions related to projects. This price list overrides any price list set on the selected transaction definition, customer, and so on. This field is only applicable if your company is subscribed to Projects. |
| STATUS | Optional | string | Status for the policy itself.

*   `active` - the policy can be used to generate invoices (default)
*   `inactive` - the policy cannot be used to generate invoices

 |

##### Filters

Use filters to define the work and costs to be included in invoices. For example, you can create a contract invoice policy for all work on a specific contract, or one that generates invoices for work done on a specific contract at a specified location, or invoices for an item.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/) to only include work tagged with the specified class. |
| CLASSGROUPID | Optional | string | `ID` of a [class group](https://developer.intacct.com/api/company-console/class-groups/) to only include work tagged with any of the classes in that group. |
| CONTRACTID | Optional | string | `CONTRACTID` of a [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) to only include work for the specified contract. |
| CONTRACTGROUPID | Optional | string | The `ID` of a [contract group](https://developer.intacct.com/api/contracts-rev-mgmt/contract-groups/) to generate invoices for the specified contract group. |
| CONTRACTTYPEID | Optional | string | The `NAME` of a [contract type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/) to only include work from contacts with that type. |
| CURRENCY | Optional | currency | Set a currency code to only include invoices from contracts that use that transaction currency. Only applicable to multi-currency companies. |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/) to generate invoices for a specified customer. |
| CUSTOMERTYPEID | Optional | string | The `NAME` of a [customer type](https://developer.intacct.com/api/accounts-receivable/customer-types/) to generate invoices for a specified customer type. |
| CUSTOMERGROUPID | Optional | string | `ID` of a [customer group](https://developer.intacct.com/api/accounts-receivable/customer-groups/) to only include work done for customers in that group. |
| DEPARTMENTID | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/) to generate invoices for that department. |
| DEPARTMENTGROUPID | Optional | string | `ID` of a [department group](https://developer.intacct.com/api/company-console/department-groups/) to only include work assocaited with departments in that group. |
| EMPLOYEEID | Optional | string | `EMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/) to generate invoices for the work of that employee. |
| EMPLOYEEGROUPID | Optional | string | `ID` of an [employee group](https://developer.intacct.com/api/employee-expenses/employee-groups/) to generate invoices for the work of employees in that group. |
| ITEMID | Required | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/) to generate invoices for a specified item. |
| ITEMGROUPID | Optional | string | `ID` of an [item group](https://developer.intacct.com/api/inventory-control/item-groups/) to generate invoices for items in a specified item group. |
| LOCATIONID | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/) to restrict invoices to the specified location. |
| LOCATIONGROUPID | Optional | string | `ID` of a [location group](https://developer.intacct.com/api/company-console/location-groups/) to only include work done at any of the locations in that group. |
| PROJECTID | Optional | string | `PROJECTID` of an active [project](https://developer.intacct.com/api/project-resource-mgmt/projects/) to generate invoices for that project. |
| PROJECTTYPEID | Optional | string | The `NAME` of an active [project type](https://developer.intacct.com/api/project-resource-mgmt/project-types/) to generate invoices for that project type. |
| PROJECTGROUPID | Optional | string | `ID` of a [project group](https://developer.intacct.com/api/project-resource-mgmt/project-groups/) to generate invoices for all projects in that group. |
| PROJECTMANAGERID | Optional | string | `EMPLOYEEID` of the project manager to generate invoices for projects associated with that project manager. |

##### Transactions to include

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| INCLUDECONTRACTS | Optional | Boolean | Whether contract transactions are included in invoices.
*   `false` - contract transactions are not included (default)
*   `true` - contract transactions are included

 |
| INCLUDECONTRACTUSAGE | Optional | Boolean | Whether [contract usage transactions](https://developer.intacct.com/api/contracts-rev-mgmt/usage-data/) are included in invoices.

*   `false` - usage transactions are not included (default)
*   `true` - usage transactions are included

 |
| INCLUDETIMESHEETS | Optional | string | Whether [timesheets](https://developer.intacct.com/api/project-resource-mgmt/timesheets/) are included in invoices.

*   `false` - timesheets are not included (default)
*   `true` - timesheets are included

 |
| INCLUDEEXPENSES | Optional | string | Whether [employee expenses](https://developer.intacct.com/api/employee-expenses/expense-reports/) are included in invoices.

*   `false` - expenses are not included (default)
*   `true` - expenses are included

 |
| INCLUDEAPBILLS | Optional | string | Whether [Accounts Payable bills](https://developer.intacct.com/api/accounts-payable/bills/) are included in invoices.

*   `false` - AP bills are not included (default)
*   `true` - AP bills are included

 |
| INCLUDEPODOCUMENTS | Optional | string | Whether [purchasing transactions](https://developer.intacct.com/api/purchasing/purchasing-transactions/) are included in invoices.

*   `false` - purchasing transactions are not included (default)
*   `true` - purchasing transactions are included

 |

##### Exception filters

**Note:** The Exception filters are for previewing or reporting only - you won’t be able to generate invoices that include unapproved transactions or transactions with missing prices.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APPROVALSTATUS | Optional | string | Filter to see only approved or unapproved transactions.
*   `Approved` - Billable transactions that are approved.
*   `Unapproved` - Billable transactions (such as vendor invoices, expense reports, and timesheets) that have not posted to the GL and are either in a Draft, Submitted, or Declined State.
*   `Both` - Ignore Approval status when filtering results.

 |
| BLANKPRICESONLY | Optional | string | Include only billable transactions that are missing prices. Use this option to create an exception report.

*   `false` (default)
*   `true`

 |

##### Scheduling

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| SCHEDULED | Optional | Boolean | Specifies if the invoice policy is set to automatically generate invoices using the `STARTDATE`, `REPEATBY` and `REPEATINTERVAL` values.
*   `false` (default)
*   `true`

 |
| STARTDATE | Optional | string | The start date for automatically generating invoices, in `mm/dd/yyyy` format. Required if `SCHEDULED` is true. |
| REPEATBY | Optional | string | Unit of time for schedule repeat frequency. Required if `SCHEDULED` is true.

*   `Days`
*   `Weeks`
*   `Months`

 |
| REPEATINTERVAL | Optional | integer | The schedule repeat interval. Required if `SCHEDULED` is true. |

* * *

Delete Contract Invoice Policy
------------------------------

#### `delete`

```
<delete>
    <object>GENINVOICEPOLICY</object>
    <keys>1</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GENINVOICEPOLICY | Required | string | Object to delete |

`GENINVOICEPOLICY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| keys | Required | string | Comma-separated list of `RECORDNO` for the policy to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

