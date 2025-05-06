Title: Timesheets

URL Source: https://developer.intacct.com/api/project-resource-mgmt/timesheets/

Markdown Content:
*   [Timesheet Object](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#timesheet-object)
    *   [Get Timesheet Object Definition](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#get-timesheet-object-definition)
    *   [Query and List Timesheets](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#query-and-list-timesheets)
    *   [Query and List Timesheets (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#query-and-list-timesheets-legacy)
    *   [Get Timesheet](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#get-timesheet)
    *   [Create Timesheet](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#create-timesheet)
    *   [Create Timesheet (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#create-timesheet-legacy)
    *   [Update Timesheet](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#update-timesheet)
    *   [Update Timesheet (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#update-timesheet-legacy)
    *   [Delete Timesheet](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#delete-timesheet)
    *   [Delete Timesheet (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#delete-timesheet-legacy)
*   [Timesheet Entry Object](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#timesheet-entry-object)
    *   [Query and List Timesheet Entries](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#query-and-list-timesheet-entries)
    *   [Query and List Timesheet Entries (Legacy)](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#query-and-list-timesheet-entries-legacy)
    *   [Get a Timesheet Entry](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#get-a-timesheet-entry)
*   [Timesheet Entry Approval Object](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#timesheet-entry-approval-object)
    *   [Query and List Timesheet Approval History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#query-and-list-timesheet-approval-history)
    *   [Get Timesheet Approval History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#get-timesheet-approval-history)
*   [Approve Timesheets](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#approve-timesheets)
*   [Decline Timesheets](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#decline-timesheets)

* * *

Timesheets ensure workers are paid appropriately and help project managers invoice clients and track overall project costs and expenses over time.

Timesheets are used in both Projects and Time & Expenses. You can access Timesheets from both applications, but you need a subscription to Projects if you want to approve timesheets and save timesheets as drafts.

Each time a timesheet entry is submitted, a timesheet approval history object is created for tracking purposes.

* * *

#### Approve or Decline by Proxy

You can approve or decline timesheets for another qualified user by creating and using a **Web services only** user in the UI. This user must have Project permissions that include **List** and **API Proxy** for approving timesheets.

For details, see the information about [Web Services only](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Web_services_users) users in the Sage Intacct product help.

* * *

Timesheet Object
----------------

### Get Timesheet Object Definition

#### `lookup`

> List all the fields and relationships for the timesheet object:

```
<lookup>
    <object>TIMESHEET</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEET` |

* * *

### Query and List Timesheets

#### `query`

> List the record number and employee ID for each timesheet for the given employee ID:

```
<query>
    <object>TIMESHEET</object>
    <select>
        <field>RECORDNO</field>
        <field>EMPLOYEEID</field>
    </select>
    <filter>
        <equalto>
            <field>EMPLOYEEID</field>
            <value>EMP22-JSMITH</value>
        </equalto>
    </filter>
</query>
```

> List information about timesheets that are available for approval (in `Submitted` state):

```
<query>
    <object>TIMESHEET</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
    <filter>
        <equalto>
            <field>STATE</field>
            <value>Submitted</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEET` |
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

### Query and List Timesheets (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>TIMESHEET</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEET` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | State. Use `S` for Submitted, `A` for Approved, `X` for Partially Approved, `R` for Declined, `I` for Draft, `E` for Partially Declined, or `V` for Saved. |

* * *

### Get Timesheet

#### `read`

```
<read>
    <object>TIMESHEET</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEET` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Timesheet

[History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#history-create-timesheet)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added EMPPOSITIONID, LABORCLASSID, LABORSHIFTID, LABORUNIONID |
| 2020 Release 2 | Added COSTTYPEID |
| 2019 Release 1 | Added TASKID |

#### `create`

```
<create>
    <TIMESHEET>
        <EMPLOYEEID>E1234</EMPLOYEEID>
        <BEGINDATE>10/05/2014</BEGINDATE>
        <GLPOSTDATE></GLPOSTDATE>
        <DESCRIPTION>hello world</DESCRIPTION>
        <SUPDOCID></SUPDOCID>
        <STATE></STATE>
        <TIMESHEETENTRIES>
            <TIMESHEETENTRY>
                <ENTRYDATE>10/05/2014</ENTRYDATE>
                <QTY>1</QTY>
                <BILLABLE>false</BILLABLE>
                <DEPARTMENTID>100</DEPARTMENTID>
                <LOCATIONID>Corporate</LOCATIONID>
                <PROJECTID>P002-EPSON</PROJECTID>
                <TASKKEY>18</TASKKEY>
                <TIMETYPE></TIMETYPE>
                <CUSTOMERID></CUSTOMERID>
                <VENDORID></VENDORID>
                <EMPLOYEEID></EMPLOYEEID>
                <ITEMID></ITEMID>
                <CLASSID></CLASSID>
                <DESCRIPTION></DESCRIPTION>
                <NOTES>my entry</NOTES>
                <EXTBILLRATE></EXTBILLRATE>
                <EXTCOSTRATE></EXTCOSTRATE>
            </TIMESHEETENTRY>
        </TIMESHEETENTRIES>
    </TIMESHEET>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TIMESHEET | Required | object | Object to create |

`TIMESHEET`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EMPLOYEEID | Required | string | Employee ID |
| BEGINDATE | Required | string | Begin date in format `mm/dd/yyyy` |
| GLPOSTDATE | Optional | string | GL posting date in format `mm/dd/yyyy` |
| DESCRIPTION | Optional | string | Description |
| SUPDOCID | Optional | string | Attachments ID |
| STATE | Optional | string | Action. Use `Draft` or `Submitted`. (Default: `Draft`) |
| TIMESHEETENTRIES | Required | array of `TIMESHEETENTRY` | Timesheet entries, must have at least 1. |

`TIMESHEETENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LINENO | Optional | integer | Line number to add entry to. |
| CUSTOMERID | Optional | string | Customer ID |
| ITEMID | Optional | string | Item ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID. Do not use if `TASKKEY` is set. |
| TASKKEY | Optional | integer | Task `RECORDNO`. Do not use if `TASKID` is set. |
| COSTTYPEID | Optional | string | Cost type ID. Only available when `PROJECTID` and task are specified. (Construction subscription) |
| TIMETYPE | Optional | string | Time type |
| BILLABLE | Optional | boolean | Billable. Use `false` for No, `true` for Yes. |
| EMPPOSITIONID | Optional | string | `POSITIONID` of an active [employee position](https://developer.intacct.com/api/construction/employee-position/). |
| LABORCLASSID | Optional | string | `LABORCLASSID` of an active [labor class](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-classes). |
| LABORSHIFTID | Optional | string | `LABORSHIFTID` of an active [labor shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-shifts). |
| LABORUNIONID | Optional | string | `LABORUNIONID` of an active [labor union](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-unions). |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| ENTRYDATE | Required | string | Entry date in format `mm/dd/yyyy` |
| QTY | Required | number | Hours/Quantity |
| DESCRIPTION | Optional | string | Description |
| NOTES | Optional | string | Notes |
| VENDORID | Optional | string | Vendor ID |
| CLASSID | Optional | string | Class ID |
| CONTRACTID | Optional | string | Contract ID |
| WAREHOUSEID | Optional | string | Warehouse ID |
| EXTBILLRATE | Optional | currency | External bill rate |
| EXTCOSTRATE | Optional | currency | External cost rate |
| EXTAMOUNT | Optional | currency | Labor amount |
| EXTEMPLOYERTAXES | Optional | currency | Employer taxes |
| EXTFRINGES | Optional | currency | Fringes |
| EXTCASHFRINGES | Optional | currency | Cash fringes |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Create Timesheet (Legacy)

[History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#history-create-timesheet-legacy)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added emppositionid, laborclassid, laborshiftid, laborunionid |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

#### `create_timesheet`

```
<create_timesheet>
    <employeeid>1001</employeeid>
    <begindate>
        <year>2012</year>
        <month>8</month>
        <day>16</day>
    </begindate>
    <timesheetdescription>Fred's Timesheet</timesheetdescription>
    <timesheetitems>
        <timesheetitem>
            <customerid>1001</customerid>
            <itemid>R0044</itemid>
            <locationid>ARL-VA-US</locationid>
            <departmentid>CS</departmentid>
            <entrydate>
                <year>2012</year>
                <month>8</month>
                <day>16</day>
            </entrydate>
            <qty>1.25</qty>
            <customfields>
                <customfield>
                    <customfieldname>MYFIELD</customfieldname>
                    <customfieldvalue>hello</customfieldvalue>
                </customfield>
            </customfields>
        </timesheetitem>
    </timesheetitems>
</create_timesheet>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| employeeid | Required | string | Employee ID |
| begindate | Required | object | Begin date |
| glpostdate | Optional | object | GL posting date |
| timesheetdescription | Optional | string | Description |
| state | Optional | string | Action. Use `Draft` or `Submitted`. (Default: `Submitted`) |
| timesheetitems | Required | array of `timesheetitem` | Timesheet entries, must have at least 1. |

`begindate`  
`glpostdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`timesheetitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| lineno | Optional | integer | Line number to add entry to |
| customerid | Optional | string | Customer ID |
| itemid | Optional | string | Item ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| taskname | Optional | string | Task name |
| timetype | Optional | string | Time type |
| emppositionid | Optional | string | `POSITIONID` of an active [employee position](https://developer.intacct.com/api/construction/employee-position/). |
| laborclassid | Optional | string | `LABORCLASSID` of an active [labor class](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-classes). |
| laborshiftid | Optional | string | `LABORSHIFTID` of an active [labor shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-shifts). |
| laborunionid | Optional | string | `LABORUNIONID` of an active [labor union](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-unions). |
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| entrydate | Required | object | Entry date |
| qty | Required | number | Hours/Quantity |
| extamount | Optional | currency | Labor amount |
| extemployertaxes | Optional | currency | Employer taxes |
| extfringes | Optional | currency | Fringes |
| extcashfringes | Optional | currency | Cash fringes |
| timesheetentrydescription | Optional | string | Description |
| notes | Optional | string | Notes |
| vendorid | Optional | string | Vendor ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| extbillrate | Optional | currency | External bill rate |
| extcostrate | Optional | currency | External cost rate |
| customfields | Optional | array of `customfield` | Custom fields |

`entrydate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Timesheet

[History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#history-update-timesheet)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added EMPPOSITIONID, LABORCLASSID, LABORSHIFTID, LABORUNIONID |
| 2020 Release 2 | Added COSTTYPEID |
| 2019 Release 1 | Added TASKID |

**Warning:** Updating a timesheet is effectively a complete replace of the existing timesheet and all of its entries. Use with caution.

#### `update`

```
<update>
    <TIMESHEET>
        <RECORDNO>1</RECORDNO>
        <EMPLOYEEID>E1234</EMPLOYEEID>
        <BEGINDATE>10/05/2014</BEGINDATE>
        <GLPOSTDATE></GLPOSTDATE>
        <DESCRIPTION>hello world</DESCRIPTION>
        <SUPDOCID></SUPDOCID>
        <STATE></STATE>
        <TIMESHEETENTRIES>
            <TIMESHEETENTRY>
                <ENTRYDATE>10/05/2014</ENTRYDATE>
                <QTY>1</QTY>
                <BILLABLE>false</BILLABLE>
                <DEPARTMENTID>100</DEPARTMENTID>
                <LOCATIONID>Corporate</LOCATIONID>
                <PROJECTID>P002-EPSON</PROJECTID>
                <TASKKEY>18</TASKKEY>
                <TIMETYPE></TIMETYPE>
                <CUSTOMERID></CUSTOMERID>
                <VENDORID></VENDORID>
                <EMPLOYEEID></EMPLOYEEID>
                <ITEMID></ITEMID>
                <CLASSID></CLASSID>
                <DESCRIPTION></DESCRIPTION>
                <NOTES>my entry</NOTES>
                <EXTBILLRATE></EXTBILLRATE>
                <EXTCOSTRATE></EXTCOSTRATE>
            </TIMESHEETENTRY>
        </TIMESHEETENTRIES>
    </TIMESHEET>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TIMESHEET | Required | object | Object to update |

`TIMESHEET`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Timesheet `RECORDNO` to update |
| EMPLOYEEID | Required | string | Employee ID |
| BEGINDATE | Required | string | Begin date in format `mm/dd/yyyy` |
| GLPOSTDATE | Optional | string | GL posting date in format `mm/dd/yyyy` |
| DESCRIPTION | Optional | string | Description |
| SUPDOCID | Optional | string | Attachments ID |
| STATE | Optional | string | Action. Use `Draft` or `Submitted`. |
| TIMESHEETENTRIES | Required | array of `TIMESHEETENTRY` | Timesheet entries, must have at least 1. |

`TIMESHEETENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LINENO | Optional | integer | Line number to add entry to |
| CUSTOMERID | Optional | string | Customer ID |
| ITEMID | Optional | string | Item ID |
| PROJECTID | Optional | string | Project ID |
| TASKID | Optional | string | Task ID. Do not use if `TASKKEY` is set. |
| TASKKEY | Optional | integer | Task `RECORDNO`. Do not use if `TASKID` is set. |
| COSTTYPEID | Optional | string | Cost type ID. Only available when `PROJECTID` and task are specified. (Construction subscription) |
| TIMETYPE | Optional | string | Time type |
| BILLABLE | Optional | boolean | Billable. Use `false` for No, `true` for Yes. |
| EMPPOSITIONID | Optional | string | `POSITIONID` of an active [employee position](https://developer.intacct.com/api/construction/employee-position/). |
| LABORCLASSID | Optional | string | `LABORCLASSID` of an active [labor class](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-classes). |
| LABORSHIFTID | Optional | string | `LABORSHIFTID` of an active [labor shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-shifts). |
| LABORUNIONID | Optional | string | `LABORUNIONID` of an active [labor union](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-unions). |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| DEPARTMENTID | Optional | string | Department ID |
| ENTRYDATE | Required | string | Entry date in format `mm/dd/yyyy` |
| QTY | Required | number | Hours/Quantity |
| DESCRIPTION | Optional | string | Description |
| NOTES | Optional | string | Notes |
| VENDORID | Optional | string | Vendor ID |
| CLASSID | Optional | string | Class ID |
| CONTRACTID | Optional | string | Contract ID |
| WAREHOUSEID | Optional | string | Warehouse ID |
| EXTBILLRATE | Optional | currency | External bill rate |
| EXTCOSTRATE | Optional | currency | External cost rate |
| EXTAMOUNT | Optional | currency | Labor amount |
| EXTEMPLOYERTAXES | Optional | currency | Employer taxes |
| EXTFRINGES | Optional | currency | Fringes |
| EXTCASHFRINGES | Optional | currency | Cash fringes |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Timesheet (Legacy)

[History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#history-update-timesheet-legacy)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added emppositionid, laborclassid, laborshiftid, laborunionid |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

**Warning:** Updating a timesheet is effectively a complete replace of the existing timesheet and all of its entries. Use with caution.

#### `update_timesheet`

```
<update_timesheet key="1234">
    <employeeid>E0003</employeeid>
    <begindate>
        <year>2015</year>
        <month>11</month>
        <day>15</day>
    </begindate>
    <timesheetdescription>Hello world</timesheetdescription>
    <timesheetitems>
        <timesheetitem>
            <lineno>2</lineno>
            <customerid>C0002</customerid>
            <projectid>P0005</projectid>
            <taskname>Phone Support</taskname>
            <locationid>ARL-VA-US</locationid>
            <departmentid>CS</departmentid>
            <entrydate>
                <year>2015</year>
                <month>11</month>
                <day>18</day>
            </entrydate>
            <qty>9</qty>
            <timesheetentrydescription>Supporting Bill on phone</timesheetentrydescription>
        </timesheetitem>
    </timesheetitems>
</update_timesheet>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Timesheet `RECORDNO` to update |
| employeeid | Required | string | Employee ID |
| begindate | Required | object | Begin date |
| glpostdate | Optional | object | GL posting date |
| timesheetdescription | Optional | string | Description |
| state | Optional | string | Action. Use `Draft` or `Submitted`. (Default: `Submitted`) |
| timesheetitems | Required | array of `timesheetitem` | Timesheet entries, must have at least 1. |

`begindate`  
`glpostdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`timesheetitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| lineno | Optional | integer | Line number to add entry to |
| customerid | Optional | string | Customer ID |
| itemid | Optional | string | Item ID |
| projectid | Optional | string | Project ID |
| taskid | Optional | string | Task ID. Only available when the parent `projectid` is also specified. |
| costtypeid | Optional | string | Cost type ID. Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| taskname | Optional | string | Task name |
| timetype | Optional | string | Time type |
| emppositionid | Optional | string | `POSITIONID` of an active [employee position](https://developer.intacct.com/api/construction/employee-position/). |
| laborclassid | Optional | string | `LABORCLASSID` of an active [labor class](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-classes). |
| laborshiftid | Optional | string | `LABORSHIFTID` of an active [labor shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-shifts). |
| laborunionid | Optional | string | `LABORUNIONID` of an active [labor union](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-unions). |
| billable | Optional | boolean | Billable. Use `false` for No, `true` for Yes. |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| entrydate | Required | object | Entry date |
| qty | Required | number | Hours/Quantity |
| extamount | Optional | currency | Labor amount |
| extemployertaxes | Optional | currency | Employer taxes |
| extfringes | Optional | currency | Fringes |
| extcashfringes | Optional | currency | Cash fringes |
| timesheetentrydescription | Optional | string | Description |
| notes | Optional | string | Notes |
| vendorid | Optional | string | Vendor ID |
| classid | Optional | string | Class ID |
| contractid | Optional | string | Contract ID |
| warehouseid | Optional | string | Warehouse ID |
| extbillrate | Optional | currency | External bill rate |
| extcostrate | Optional | currency | External cost rate |
| customfields | Optional | array of `customfield` | Custom fields |

`entrydate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Timesheet

#### `delete`

```
<delete>
    <object>TIMESHEET</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEET` |
| keys | Required | string | Comma-separated list of timesheet `RECORDNO` to delete |

* * *

### Delete Timesheet (Legacy)

#### `delete_timesheet`

```
<delete_timesheet key="1234"></delete_timesheet>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Timesheet `RECORDNO` to delete |

* * *

Timesheet Entry Object
----------------------

### Query and List Timesheet Entries

#### `query`

> List the record number and state for each timesheet entry:

```
<query>
    <object>TIMESHEETENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
</query>
```

> List the record number and state for each timesheet entry available for approval (in `Submitted` state):

```
<query>
    <object>TIMESHEETENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
    <filter>
        <equalto>
            <field>STATE</field>
            <value>Submitted</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEETENTRY` |
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

### Query and List Timesheet Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>TIMESHEETENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEETENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get a Timesheet Entry

#### `read`

```
<read>
    <object>TIMESHEETENTRY</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEETENTRY` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Timesheet Entry Approval Object
-------------------------------

### Query and List Timesheet Approval History

When a timesheet entry is submitted, a corresponding timesheet approval history object is created. This object tracks the state of the timesheet entry.

#### `query`

> List the record numbers and states for all timesheet approval objects:

```
<query>
    <object>TIMESHEETAPPROVAL</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
</query>
```

> Using the timesheet approval history object, list timesheet entry record numbers and descriptions if the designated approver is `JJADAMS` and the timesheet entry is available for approval (in `Submitted` state):

```
<query>
    <object>TIMESHEETAPPROVAL</object>
    <select>
        <field>TIMESHEETENTRYKEY</field>
        <field>TIMESHEETENTRY.DESCRIPTION</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>APPROVERID</field>
                <value>JJADAMS</value>
            </equalto>
            <equalto>
                <field>STATE</field>
                <value>Submitted</value>
            </equalto>
        </and>
    </filter>
</query>
```

> Assuming that `UserID1` is sending the function call, return information about timesheet entries that are approved/approvable by `UserID1` for the timesheet with record number 1:

```
<query>
    <object>TIMESHEETAPPROVAL</object>
    <select>
        <field>RECORDNO</field>
        <field>APPROVAL_STAGE</field>
        <field>APPROVAL_LEVEL</field>
        <field>APPROVERID</field>
        <field>APPROVEDBY</field>
        <field>EVENTDATE</field>
        <field>COMMENTS</field>
        <field>STATE</field>
        <field>TIMESHEETENTRY.TIMESHEET.RECORDNO</field>
        <field>TIMESHEETENTRY.RECORDNO</field>
        <field>TIMESHEETENTRY.LINENO</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>APPROVERID</field>
                <value>UserID1</value>
            </equalto>
            <equalto>
                <field>TIMESHEETENTRY.TIMESHEET.RECORDNO</field>
                <value>1</value>
            </equalto>
        </and>
    </filter>
    <orderby>
        <order>
            <field>TIMESHEETENTRY.RECORDNO</field>
            <descending />
        </order>
    </orderby>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEETAPPROVAL` |
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

### Get Timesheet Approval History

#### `read`

```
<read>
    <object>TIMESHEETAPPROVAL</object>
    <keys>79</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `TIMESHEETAPPROVAL` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Approve Timesheets
------------------

[History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#history-approve-timesheets)

| Release | Changes |
| --- | --- |
| 2020 Release 3 | Added APPROVEDBY |

You can approve all the entries on a timesheet or approve only selected ones. Timesheet entries can be approved if they are in the `Submitted` state.

#### `approve`

> Approve all entries for the timesheet:

```
<approve>
    <TIMESHEET>
        <RECORDNO>2</RECORDNO>
        <COMMENT>Approved by James</COMMENT>
    </TIMESHEET>
</approve>
```

> Approve two entries from the timesheet:

```
<approve>
    <TIMESHEET>
        <RECORDNO>2</RECORDNO>
        <ENTRYKEYS>499,328</ENTRYKEYS>
        <COMMENT>Approved by James</COMMENT>
    </TIMESHEET>
</approve>
```

> Approve all entries for the timesheet on behalf of a different user:

```
<approve>
    <TIMESHEET>
        <RECORDNO>2</RECORDNO>
        <COMMENT>Approved on behalf of James by Web services user with API Proxy permission</COMMENT>
        <APPROVEDBY>James</APPROVEDBY>
    </TIMESHEET>
</approve>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TIMESHEET | Required | string | Object to approve |

`TIMESHEET`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the timesheet |
| ENTRYKEYS | Optional | string | Comma-separated list of timesheet entry keys to approve. Omit this parameter to approve all the entries for the timesheet. |
| APPROVEDBY | Optional | string | ID of the user on whose behalf this timesheet is approved. The specified user must be an active user with permissions to approve timesheets and must be in the approval chain (or be an unrestricted approver). The `APPROVEDBY` user is recorded as the user who approved the timesheet even though a different user is executing the request. |
| COMMENT | Optional | string | Comments for the approval |

* * *

Decline Timesheets
------------------

[History](https://developer.intacct.com/api/project-resource-mgmt/timesheets/#history-decline-timesheets)

| Release | Changes |
| --- | --- |
| 2020 Release 3 | Added DECLINEDDBY |

You can decline all the entries on a timesheet or decline only selected ones.

#### `decline`

> Decline all entries for the timesheet:

```
<decline>
    <TIMESHEET>
        <RECORDNO>2</RECORDNO>
        <COMMENT>Declined by James</COMMENT>
    </TIMESHEET>
</decline>
```

> Decline two entries from the timesheet:

```
<decline>
    <TIMESHEET>
        <RECORDNO>2</RECORDNO>
        <ENTRYKEYS>497,323</ENTRYKEYS>
        <COMMENT>Declined by James</COMMENT>
    </TIMESHEET>
</decline>
```

> Decline all entries for the timesheet on behalf of a different user:

```
<decline>
    <TIMESHEET>
        <RECORDNO>2</RECORDNO>
        <COMMENT>Declined on behalf of James by Web services user with API Proxy permission</COMMENT>
        <DECLINEDBY>James</DECLINEDBY>
    </TIMESHEET>
</decline>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TIMESHEET | Required | string | Object to decline |

`TIMESHEET`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the timesheet |
| ENTRYKEYS | Optional | string | Comma-separated list of timesheet entry keys to decline. Omit this parameter to decline all the entries for the timesheet. |
| DECLINEDEDBY | Optional | string | ID of the user on whose behalf this timesheet is declined. The specified user must be an active user with permissions to approve timesheets and must be in the approval chain (or be an unrestricted approver). The `DECLINEDBY` user is recorded as the user who declined the timesheet even though a different user is executing the request. When listing or querying timesheets, a declined timesheet’s `STATE` is set to declined, but the field for the user that executed the function is `APPROVEDBY`, not `DECLINEDBY`. |
| COMMENT | Optional | string | Comments for declined entries |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

