Title: Rate Tables

URL Source: https://developer.intacct.com/api/construction/rate-tables/

Markdown Content:
*   [Rate Tables](https://developer.intacct.com/api/construction/rate-tables/#rate-tables)
    *   [Project contract line matching](https://developer.intacct.com/api/construction/rate-tables/#project-contract-line-matching)
    *   [Get Rate Table Object Definition](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-object-definition)
    *   [Query and List Rate Tables](https://developer.intacct.com/api/construction/rate-tables/#query-and-list-rate-tables)
    *   [Get a Rate Table](https://developer.intacct.com/api/construction/rate-tables/#get-a-rate-table)
    *   [Get Rate Table by ID](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-by-id)
    *   [Create Rate Table](https://developer.intacct.com/api/construction/rate-tables/#create-rate-table)
    *   [Update a Rate Table](https://developer.intacct.com/api/construction/rate-tables/#update-a-rate-table)
    *   [Delete Rate Table](https://developer.intacct.com/api/construction/rate-tables/#delete-rate-table)
*   [Rate Table Timesheet Entries](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries)
    *   [Create/Update Request Parameters](https://developer.intacct.com/api/construction/rate-tables/#createupdate-request-parameters)
    *   [Get Rate Table Timesheet Entry Object Definition](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-timesheet-entry-object-definition)
    *   [Query and List Rate Table Timesheet Entries](https://developer.intacct.com/api/construction/rate-tables/#query-and-list-rate-table-timesheet-entries)
    *   [Get a Rate Table Timesheet Entry](https://developer.intacct.com/api/construction/rate-tables/#get-a-rate-table-timesheet-entry)
*   [Rate Table Purchase Order Entries](https://developer.intacct.com/api/construction/rate-tables/#rate-table-purchase-order-entries)
    *   [Create/Update Request Parameters](https://developer.intacct.com/api/construction/rate-tables/#createupdate-request-parameters-1)
    *   [Get Rate Table Purchase Order Entry Object Definition](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-purchase-order-entry-object-definition)
    *   [Query and List Rate Table Purchase Order Entries](https://developer.intacct.com/api/construction/rate-tables/#query-and-list-rate-table-purchase-order-entries)
    *   [Get a Rate Table Purchase Order Entry](https://developer.intacct.com/api/construction/rate-tables/#get-a-rate-table-purchase-order-entry)
*   [Rate Table Credit Card Entries](https://developer.intacct.com/api/construction/rate-tables/#rate-table-credit-card-entries)
    *   [Create/Update Request Parameters](https://developer.intacct.com/api/construction/rate-tables/#createupdate-request-parameters-2)
    *   [Get Rate Table Credit Card Entry Object Definition](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-credit-card-entry-object-definition)
    *   [Query and List Rate Table Credit Card Entries](https://developer.intacct.com/api/construction/rate-tables/#query-and-list-rate-table-credit-card-entries)
    *   [Get a Rate Table Credit Card Entry](https://developer.intacct.com/api/construction/rate-tables/#get-a-rate-table-credit-card-entry)
*   [Rate Table Employee Expense Entries](https://developer.intacct.com/api/construction/rate-tables/#rate-table-employee-expense-entries)
    *   [Create/Update Request Parameters](https://developer.intacct.com/api/construction/rate-tables/#createupdate-request-parameters-3)
    *   [Get Rate Table Employee Expense Entry Object Definition](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-employee-expense-entry-object-definition)
    *   [Query and List Rate Table Employee Expense Entries](https://developer.intacct.com/api/construction/rate-tables/#query-and-list-rate-table-employee-expense-entries)
    *   [Get a Rate Table Employee Expense Entry](https://developer.intacct.com/api/construction/rate-tables/#get-a-rate-table-employee-expense-entry)
*   [Rate Table Accounts Payable Entries](https://developer.intacct.com/api/construction/rate-tables/#rate-table-accounts-payable-entries)
    *   [Create/Update Request Parameters](https://developer.intacct.com/api/construction/rate-tables/#createupdate-request-parameters-4)
    *   [Get Rate Table Accounts Payable Entry Object Definition](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-accounts-payable-entry-object-definition)
    *   [Query and List Rate Table Accounts Payable Entries](https://developer.intacct.com/api/construction/rate-tables/#query-and-list-rate-table-accounts-payable-entries)
    *   [Get a Rate Table Accounts Payable Entry](https://developer.intacct.com/api/construction/rate-tables/#get-a-rate-table-accounts-payable-entry)
*   [Rate Table General Ledger Entries](https://developer.intacct.com/api/construction/rate-tables/#rate-table-general-ledger-entries)
    *   [Create/Update Request Parameters](https://developer.intacct.com/api/construction/rate-tables/#createupdate-request-parameters-5)
    *   [Get Rate Table General Ledger Entry Object Definition](https://developer.intacct.com/api/construction/rate-tables/#get-rate-table-general-ledger-entry-object-definition)
    *   [Query and List Rate Table General Ledger Entries](https://developer.intacct.com/api/construction/rate-tables/#query-and-list-rate-table-general-ledger-entries)
    *   [Get a Rate Table General Ledger Entry](https://developer.intacct.com/api/construction/rate-tables/#get-a-rate-table-general-ledger-entry)

* * *

**About Rate Tables**

Rate tables store specific markups or discount rates and prices that can be applied to different types of construction-related expenses that use Time and Materials billing.

You can define markup/discount rates as a percentage of an original cost or as a fixed amount.

* * *

A rate table object contains header information about a rate table, including the name, description, and status. It is the parent object for arrays of owned objects that define different types of rates that you might apply to a project:

*   Timesheet Entries
*   Purchase Order Entries
*   Account Payable Entries
*   General Ledger Entries
*   Credit Card Entries
*   Employee Expense Entries

You can create separate rate tables for each type of transaction source (one for timesheets, one for credit card entries, etc.), or have several types of entries under a single rate table. You can also create multiple rate tables for any type of entry, such as multiple rate tables for timesheet entries, if that’s what you need to correctly bill for your projects.

### Project contract line matching

Rate table entries have fields that you can use to match rate tables to project contract line entries:

*   Standard task
*   Standard cost type
*   Accumulation type
*   Employee
*   Employee position
*   Item
*   Start date
*   Time type
*   Labor class, shift, and/or union

In the event that a project contract line entry matches more than one rate table entry, the number of field matches in each entry will be compared and the entry with the highest number of matches will be used. For example, if one entry has the matching standard task ID but another entry has a matching standard task ID and standard cost type ID, the second entry will be used. If two entries have the same number of matching fields, the entry that is sorted highest in the Sage Intacct UI will be used. (The API does not currently support entry sorting.)

* * *

### Get Rate Table Object Definition

#### `lookup`

> List all the fields and relationships for the rate table object:

```
<lookup>
    <object>RATETABLE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLE` |

* * *

### Query and List Rate Tables

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and original price for each rate table:

```
<query>
    <object>RATETABLE</object>
    <filter>
        <equalto>
            <field>STATUS</field>
            <value>active</value>
        </equalto>
    </filter>
    <select>
        <field>RATETABLEID</field>
        <field>NAME</field>
        <field>RECORDNO</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLE` |
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

### Get a Rate Table

#### `read`

> Return all fields of a specified rate table

```
<read>
    <object>RATETABLE</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Rate Table by ID

#### `readByName`

```
<readByName>
    <object>RATETABLE</object>
    <keys>Prime</keys>
    <fields>*</fields>
</readByName> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLE` |
| keys | Required | string | Comma-separated list of `RATETABLEID` of the rate table to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Rate Table

You can create rate tables at the top-level entity of a multi-entity company or at lower level entities.

*   Rate Tables that are created and modified at the top-level entity have read-only access at lower level entities.
*   Rate Tables created at lower-level entities can only be accessed by the entity that created it.

#### `create`

> Create a basic rate table header:

```
<create>
    <RATETABLE>
        <RATETABLEID>Prime</RATETABLEID>
    </RATETABLE>
</create>
```

> Create a rate table with two expense and credit card entries:

```
<create>
    <RATETABLE>
        <RATETABLEID>2022-LV2</RATETABLEID>
        <NAME>2022 Level 2</NAME>
        <DESCRIPTION>2022 Level 2 Rate Table</DESCRIPTION>
        <RATETABLEEXPENSEENTRIES>
            <RATETABLEEXPENSEENTRY>
                <DESCRIPTION>Aug Manager</DESCRIPTION>
                <STANDARDTASKID>TSK-RT-0081</STANDARDTASKID>
                <STANDARDCOSTTYPEID>CT-RT-0005</STANDARDCOSTTYPEID>
                <ACCUMULATIONTYPENAME>ACCT-1</ACCUMULATIONTYPENAME>
                <EMPLOYEEID>MGR3</EMPLOYEEID>
                <ITEMID>E003</ITEMID>
                <STARTDATE>08/02/2021</STARTDATE>
                <MARKUPPCT>14.8</MARKUPPCT>
            </RATETABLEEXPENSEENTRY>
            <RATETABLEEXPENSEENTRY>
                <DESCRIPTION>Materials Markup</DESCRIPTION>
                <ACCUMULATIONTYPENAME>ACCT-2</ACCUMULATIONTYPENAME>
                <MARKUPPCT>4.78</MARKUPPCT>
            </RATETABLEEXPENSEENTRY>
        </RATETABLEEXPENSEENTRIES>
        <RATETABLECCENTRIES>
            <RATETABLECCENTRY>
                <DESCRIPTION>Aug Costing SOPA</DESCRIPTION>
                <STANDARDTASKID>TSK-RT-0004</STANDARDTASKID>
                <STANDARDCOSTTYPEID>MATERIAL</STANDARDCOSTTYPEID>
                <ACCUMULATIONTYPENAME>ACCT-2</ACCUMULATIONTYPENAME>
                <EMPLOYEEID>234</EMPLOYEEID>
                <ITEMID>Costing_SOPO</ITEMID>
                <STARTDATE>08/03/2021</STARTDATE>
                <MARKUPPCT>15.9</MARKUPPCT>
            </RATETABLECCENTRY>
            <RATETABLECCENTRY>
                <DESCRIPTION>Materials Markup</DESCRIPTION>
                <STANDARDCOSTTYPEID>CT-RT-0055</STANDARDCOSTTYPEID>
                <MARKUPPCT>-25.83</MARKUPPCT>
            </RATETABLECCENTRY>
        </RATETABLECCENTRIES>
    </RATETABLE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `RATETABLE` | Required | object | Object type to create. |

`RATETABLE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Required | string | User-defined unique ID for the rate table. |
| NAME | Optional | string | Name for the rate table. |
| DESCRIPTION | Optional | string | Description of the rate table. |
| STATUS | Optional | string | Status of the rate table.
*   `active` (default)
*   `inactive`

 |
| RATETABLETSENTRIES | Optional | array of [`RATETABLETSENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Timesheet entries for this rate table. |
| RATETABLEPOENTRIES | Optional | array of [`RATETABLEPOENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Purchase order entries for this rate table. |
| RATETABLEAPENTRIES | Optional | array of [`RATETABLEAPENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Accounts payable entries for this rate table. |
| RATETABLEGLENTRIES | Optional | array of [`RATETABLEGLENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | General ledger entries for this rate table. |
| RATETABLEEXPENSEENTRIES | Optional | array of [`RATETABLEEXPENSEENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Expense entries for this rate table. |
| RATETABLECCENTRIES | Optional | array of [`RATETABLECCENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Credit card entries for this rate table. |

* * *

### Update a Rate Table

#### `update`

For each `RATETABLE<xx>ENTRIES` array, you can replace all entries, delete all entries, or leave them unchanged:

*   To replace all timesheet entries, include `RATETABLETSENTRIES` with one `RATETABLETSENTRY` for each timesheet entry that you want included in the rate table.
*   To delete all timesheet entries, include `RATETABLETSENTRIES` with no `RATETABLETSENTRY` elements.
*   To leave all timesheet entries unchanged, do not include `RATETABLETSENTRIES` in the update request.

This behavior also applies to `RATETABLEPOENTRIES`, `RATETABLEAPENTRIES`, `RATETABLEGLENTRIES`, `RATETABLEEXPENSEENTRIES`, and `RATETABLECCENTRIES`.

> Replace the credit card entries in a rate table:

```
<update>
    <RATETABLE>
        <RATETABLEID>Prime</RATETABLEID>
        <RATETABLECCENTRIES>
            <RATETABLECCENTRY>
                <DESCRIPTION>Apr Costing SOPA</DESCRIPTION>
                <STANDARDTASKID>TSK-RT-0004</STANDARDTASKID>
                <STANDARDCOSTTYPEID>MATERIAL</STANDARDCOSTTYPEID>
                <ACCUMULATIONTYPENAME>ACCT-2</ACCUMULATIONTYPENAME>
                <EMPLOYEEID>234</EMPLOYEEID>
                <ITEMID>Costing_SOPO</ITEMID>
                <STARTDATE>04/01/2022</STARTDATE>
                <MARKUPPCT>15.9</MARKUPPCT>
            </RATETABLECCENTRY>
            <RATETABLECCENTRY>
                <DESCRIPTION>Materials Markup</DESCRIPTION>
                <STANDARDCOSTTYPEID>CT-RT-0055</STANDARDCOSTTYPEID>
                <MARKUPPCT>-25.83</MARKUPPCT>
            </RATETABLECCENTRY>
        </RATETABLECCENTRIES>
    </RATETABLE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `RATETABLE` | Required | object | Object type to update. |

`RATETABLE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Required | string | The ID of the rate table to update. |
| NAME | Optional | string | Name for the rate table. |
| DESCRIPTION | Optional | string | Description of the rate table. |
| STATUS | Optional | string | Status of the rate table.
*   `active` (default)
*   `inactive`

 |
| RATETABLETSENTRIES | Optional | array of [`RATETABLETSENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Timesheet entries for this rate table. |
| RATETABLEPOENTRIES | Optional | array of [`RATETABLEPOENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Purchase order entries for this rate table. |
| RATETABLEAPENTRIES | Optional | array of [`RATETABLEAPENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Accounts payable entries for this rate table. |
| RATETABLEGLENTRIES | Optional | array of [`RATETABLEGLENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | General ledger entries for this rate table. |
| RATETABLEEXPENSEENTRIES | Optional | array of [`RATETABLEEXPENSEENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Expense entries for this rate table. |
| RATETABLECCENTRIES | Optional | array of [`RATETABLECCENTRY`](https://developer.intacct.com/api/construction/rate-tables/#rate-table-timesheet-entries) | Credit card entries for this rate table. |

* * *

### Delete Rate Table

A rate table can only be deleted if all rate table lines that belong to the contract have a null or zero `BILLEDPRICE` values.

All rate table lines that belong to a rate table will be deleted with the rate table.

#### `delete`

```
<delete>
    <object>RATETABLE</object>
    <keys>3</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table to delete. |

* * *

Rate Table Timesheet Entries
----------------------------

Rate table timesheet entry objects define the rules that are applied to timesheet entries on project contracts. They are owned objects of a rate table object. You create, update, and delete timesheet entry objects through operations on the owning rate table.

### Create/Update Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Optional | string | `RATETABLEID` of the parent rate table. |
| DESCRIPTION | Optional | string | Description of the rate table entry. |
| STARTDATE | Optional | date | Start date for when these rates will be applied to timesheet entries that are included for billing in invoices generated on or after this date. |
| MARKUPPCT | Optional | numeric | Markup percent for this rate table entry. Cannot be used with LABORRATE. |
| LABORRATE | Optional | numeric | Labor rate of this rate table entry. Cannot be used with MARKUPPCT. |
| TIMETYPENAME | Optional | string | `NAME` of a [time type](https://developer.intacct.com/api/project-resource-mgmt/time-types/) to apply it to this rate table. |
| EMPPOSITIONID | Optional | string | `EMPPOSITIONID` to apply this rate by [employee positions](https://developer.intacct.com/api/construction/employee-position/) entered on timesheets. |
| LABORCLASSID | Optional | string | `LABORCLASSID` of a [labor class](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-classes). |
| LABORSHIFTID | Optional | string | `LABORSHIFTID` of a [labor shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-shifts). |
| LABORUNIONID | Optional | string | `LABORUNIONID` of a [labor union](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-unions). |
| ACCUMULATIONTYPENAME | Optional | string | `NAME` of an [accumulation type](https://developer.intacct.com/api/construction/accumulation-types/). |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| EMPLOYEEID | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/). |
| PROJECTID | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| STANDARDCOSTTYPEID | Optional | string | `STANDARDCOSTTYPEID` of a [standard cost type](https://developer.intacct.com/api/construction/standard-cost-types/). |
| STANDARDTASKID | Optional | string | `STANDARDTASKID` of a [standard task](https://developer.intacct.com/api/construction/standard-tasks/). |
| TASKID | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). |
| VENDORID | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of a [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |

### Get Rate Table Timesheet Entry Object Definition

#### `lookup`

> List all the fields and relationships for the rate table timesheet entry object:

```
<lookup>
    <object>RATETABLETSENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLETSENTRY` |

* * *

### Query and List Rate Table Timesheet Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> For a specified rate table, list the employee position ID and labor rate in each rate table timesheet entry object:

```
<query>
    <object>RATETABLETSENTRY</object>
    <filter>
        <equalto>
            <field>RATETABLEID</field>
            <value>Com-01</value>
        </equalto>
    </filter>
    <select>
        <field>EMPPOSITIONID</field>
        <field>LABORRATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLETSENTRY` |
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

### Get a Rate Table Timesheet Entry

#### `read`

> Return all fields of a specified rate table timesheet entry

```
<read>
    <object>RATETABLETSENTRY</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLETSENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table timesheet entry to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Rate Table Purchase Order Entries
---------------------------------

Rate table purchase order entry objects define the rules that are applied to purchase order entries on project contracts. They are owned objects of a rate table object. You create, update, and delete purchase order entry objects through operations on the owning rate table.

### Create/Update Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Optional | string | ID of the parent rate table. |
| DESCRIPTION | Optional | string | Description of the rate table entry. |
| STARTDATE | Optional | Date | Start date for when these rates will be applied to purchase orders that are included for billing in invoices generated on or after this date. |
| MARKUPPCT | Optional | numeric | Markup percent for this rate table entry. |
| UNITPRICE | Optional | numeric | Unit price of a purchased item. ITEMID is required with UNITPRICE. |
| ACCUMULATIONTYPENAME | Optional | string | `NAME` of an [accumulation type](https://developer.intacct.com/api/construction/accumulation-types/). |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| EMPLOYEEID | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/). |
| PROJECTID | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| STANDARDCOSTTYPEID | Optional | string | `STANDARDCOSTTYPEID` of a [standard cost type](https://developer.intacct.com/api/construction/standard-cost-types/). |
| STANDARDTASKID | Optional | string | `STANDARDTASKID` of a [standard task](https://developer.intacct.com/api/construction/standard-tasks/). |
| TASKID | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). |
| VENDORID | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of a [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |

### Get Rate Table Purchase Order Entry Object Definition

#### `lookup`

> List all the fields and relationships for the rate table purchase order entry object:

```
<lookup>
    <object>RATETABLEPOENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEPOENTRY` |

* * *

### Query and List Rate Table Purchase Order Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and original price for each rate table purchase order entry:

```
<query>
    <object>RATETABLEPOENTRY</object>
    <filter>
        <equalto>
            <field>RATETABLEID</field>
            <value>Com-01</value>
        </equalto>
    </filter>
    <select>
        <field>STARTDATE</field>
        <field>CUSTOMERID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEPOENTRY` |
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

### Get a Rate Table Purchase Order Entry

#### `read`

> Return all fields of a specified rate table purchase order entry

```
<read>
    <object>RATETABLEPOENTRY</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEPOENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table purchase order entry to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Rate Table Credit Card Entries
------------------------------

Rate table credit card entry objects define the rules that are applied to credit card entries on project contracts. They are owned objects of a rate table object. You create, update, and delete credit card entry objects through operations on the owning rate table.

### Create/Update Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Optional | string | ID of the parent rate table. |
| DESCRIPTION | Optional | string | Description of the rate table entry. |
| STARTDATE | Optional | Date | Start date for when these rates will be applied to credit card charges that are included for billing in invoices generated on or after this date. |
| MARKUPPCT | Optional | Numeric | Markup percent for this rate table entry. |
| ACCUMULATIONTYPENAME | Optional | string | `NAME` of an [accumulation type](https://developer.intacct.com/api/construction/accumulation-types/). |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| EMPLOYEEID | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/). |
| PROJECTID | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| STANDARDCOSTTYPEID | Optional | string | `STANDARDCOSTTYPEID` of a [standard cost type](https://developer.intacct.com/api/construction/standard-cost-types/). |
| STANDARDTASKID | Optional | string | `STANDARDTASKID` of a [standard task](https://developer.intacct.com/api/construction/standard-tasks/). |
| TASKID | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). |
| VENDORID | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of a [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |

### Get Rate Table Credit Card Entry Object Definition

#### `lookup`

> List all the fields and relationships for the rate table credit card entry object:

```
<lookup>
    <object>RATETABLEAPENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLECCENTRY` |

* * *

### Query and List Rate Table Credit Card Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and original price for each rate table credit card entry:

```
<query>
    <object>RATETABLEAPENTRY</object>
    <filter>
        <equalto>
            <field>RATETABLEID</field>
            <value>Com-01</value>
        </equalto>
    </filter>
    <select>
        <field>STARTDATE</field>
        <field>CUSTOMERID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLECCENTRY` |
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

### Get a Rate Table Credit Card Entry

#### `read`

> Return all fields of a specified rate table credit card entry

```
<read>
    <object>RATETABLEAPENTRY</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLECCENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table credit card entry to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Rate Table Employee Expense Entries
-----------------------------------

Rate table employee expense entry objects define the rules that are applied to employee expense entries on project contracts. They are owned objects of a rate table object. You create, update, and delete employee expense entry objects through operations on the owning rate table.

### Create/Update Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Optional | string | ID of the parent rate table. |
| DESCRIPTION | Optional | string | Description of the rate table entry. |
| STARTDATE | Optional | Date | Start date for when these rates will be applied to employee expenses that are included for billing in invoices generated on or after this date. |
| MARKUPPCT | Optional | Numeric | Markup percent for this rate table entry. |
| ACCUMULATIONTYPENAME | Optional | string | `NAME` of an [accumulation type](https://developer.intacct.com/api/construction/accumulation-types/). |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| EMPLOYEEID | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/). |
| PROJECTID | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| STANDARDCOSTTYPEID | Optional | string | `STANDARDCOSTTYPEID` of a [standard cost type](https://developer.intacct.com/api/construction/standard-cost-types/). |
| STANDARDTASKID | Optional | string | `STANDARDTASKID` of a [standard task](https://developer.intacct.com/api/construction/standard-tasks/). |
| TASKID | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). |
| VENDORID | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of a [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |

### Get Rate Table Employee Expense Entry Object Definition

#### `lookup`

> List all the fields and relationships for the rate table employee expense entry object:

```
<lookup>
    <object>RATETABLEAPENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEEXPENSEENTRY` |

* * *

### Query and List Rate Table Employee Expense Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and original price for each rate table employee expense entry:

```
<query>
    <object>RATETABLEAPENTRY</object>
    <filter>
        <equalto>
            <field>RATETABLEID</field>
            <value>Com-01</value>
        </equalto>
    </filter>
    <select>
        <field>STARTDATE</field>
        <field>CUSTOMERID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEEXPENSEENTRY` |
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

### Get a Rate Table Employee Expense Entry

#### `read`

> Return all fields of a specified rate table employee expense entry

```
<read>
    <object>RATETABLEAPENTRY</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEEXPENSEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table employee expense entry to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Rate Table Accounts Payable Entries
-----------------------------------

Rate table accounts payable entry objects define the rules that are applied to accounts payable expenses on project contracts. They are owned objects of a rate table object. You create, update, and delete accounts payable entry objects through create and update operations on the owning rate table.

### Create/Update Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Optional | string | ID of the parent rate table. |
| DESCRIPTION | Optional | string | Description of the rate table entry. |
| MARKUPPCT | Optional | Numeric | Markup percent for this rate table entry. |
| STARTDATE | Optional | Date | Start date for when these rates will be applied to accounts payable entries that are included for billing in invoices generated on or after this date. |
| ACCUMULATIONTYPENAME | Optional | string | `NAME` of an [accumulation type](https://developer.intacct.com/api/construction/accumulation-types/). |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| EMPLOYEEID | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/). |
| PROJECTID | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| STANDARDCOSTTYPEID | Optional | string | `STANDARDCOSTTYPEID` of a [standard cost type](https://developer.intacct.com/api/construction/standard-cost-types/). |
| STANDARDTASKID | Optional | string | `STANDARDTASKID` of a [standard task](https://developer.intacct.com/api/construction/standard-tasks/). |
| TASKID | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). |
| VENDORID | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of a [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |

### Get Rate Table Accounts Payable Entry Object Definition

#### `lookup`

> List all the fields and relationships for the rate table accounts payable entry object:

```
<lookup>
    <object>RATETABLEAPENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEAPENTRY` |

* * *

### Query and List Rate Table Accounts Payable Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and original price for each rate table accounts payable entry:

```
<query>
    <object>RATETABLEAPENTRY</object>
    <filter>
        <equalto>
            <field>RATETABLEID</field>
            <value>Com-01</value>
        </equalto>
    </filter>
    <select>
        <field>STARTDATE</field>
        <field>CUSTOMERID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEAPENTRY` |
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

### Get a Rate Table Accounts Payable Entry

#### `read`

> Return all fields of a specified rate table accounts payable entry

```
<read>
    <object>RATETABLEAPENTRY</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEAPENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table accounts payable entry to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Rate Table General Ledger Entries
---------------------------------

Rate table general ledger entry objects define the rules that are applied to general ledger entries on project contracts. They are owned objects of a rate table object. You create, update, and delete general ledger entry objects through operations on the owning rate table.

### Create/Update Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RATETABLEID | Optional | string | ID of the parent rate table. |
| DESCRIPTION | Optional | string | Description of the rate table entry. |
| STARTDATE | Optional | Date | Start date for when these rates will be applied to general ledger entries that are included for billing in invoices generated on or after this date. |
| MARKUPPCT | Optional | Numeric | Markup percent for this rate table entry. |
| ACCUMULATIONTYPENAME | Optional | string | `NAME` of an [accumulation type](https://developer.intacct.com/api/construction/accumulation-types/). |
| CLASSID | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| COSTTYPEID | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). |
| CUSTOMERID | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| EMPLOYEEID | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| ITEMID | Optional | string | `ITEMID` of an [item](https://developer.intacct.com/api/inventory-control/items/). |
| PROJECTID | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| STANDARDCOSTTYPEID | Optional | string | `STANDARDCOSTTYPEID` of a [standard cost type](https://developer.intacct.com/api/construction/standard-cost-types/). |
| STANDARDTASKID | Optional | string | `STANDARDTASKID` of a [standard task](https://developer.intacct.com/api/construction/standard-tasks/). |
| TASKID | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). |
| VENDORID | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| WAREHOUSEID | Optional | string | `WAREHOUSEID` of a [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |

### Get Rate Table General Ledger Entry Object Definition

#### `lookup`

> List all the fields and relationships for the rate table general ledger entry object:

```
<lookup>
    <object>RATETABLEAPENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEGLENTRY` |

* * *

### Query and List Rate Table General Ledger Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and original price for each rate table general ledger entry:

```
<query>
    <object>RATETABLEAPENTRY</object>
    <filter>
        <equalto>
            <field>RATETABLEID</field>
            <value>Com-01</value>
        </equalto>
    </filter>
    <select>
        <field>STARTDATE</field>
        <field>CUSTOMERID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEGLENTRY` |
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

### Get a Rate Table General Ledger Entry

#### `read`

> Return all fields of a specified rate table general ledger entry

```
<read>
    <object>RATETABLEAPENTRY</object>
    <keys>4</keys>
    <fields>*</fields>
</read> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `RATETABLEGLENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the rate table general ledger entry to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

