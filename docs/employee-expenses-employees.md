Title: Employees

URL Source: https://developer.intacct.com/api/employee-expenses/employees/

Markdown Content:
*   [Employees](https://developer.intacct.com/api/employee-expenses/employees/#employees)
    *   [Get Employee Object Definition](https://developer.intacct.com/api/employee-expenses/employees/#get-employee-object-definition)
    *   [Query and List Employees](https://developer.intacct.com/api/employee-expenses/employees/#query-and-list-employees)
    *   [Query and List Employees (Legacy)](https://developer.intacct.com/api/employee-expenses/employees/#query-and-list-employees-legacy)
    *   [Get Employees](https://developer.intacct.com/api/employee-expenses/employees/#get-employees)
    *   [Get Employees by ID](https://developer.intacct.com/api/employee-expenses/employees/#get-employees-by-id)
    *   [Create Employee](https://developer.intacct.com/api/employee-expenses/employees/#create-employee)
    *   [Create Employee (Legacy)](https://developer.intacct.com/api/employee-expenses/employees/#create-employee-legacy)
    *   [Update Employee](https://developer.intacct.com/api/employee-expenses/employees/#update-employee)
    *   [Update Employee (Legacy)](https://developer.intacct.com/api/employee-expenses/employees/#update-employee-legacy)
    *   [Delete Employee](https://developer.intacct.com/api/employee-expenses/employees/#delete-employee)
    *   [Delete Employee (Legacy)](https://developer.intacct.com/api/employee-expenses/employees/#delete-employee-legacy)
*   [Employee Cost Rates](https://developer.intacct.com/api/employee-expenses/employees/#employee-cost-rates)
    *   [Create Employee Cost Rate (Legacy)](https://developer.intacct.com/api/employee-expenses/employees/#create-employee-cost-rate-legacy)
    *   [Update Employee Cost Rate (Legacy)](https://developer.intacct.com/api/employee-expenses/employees/#update-employee-cost-rate-legacy)
    *   [Delete Employee Cost Rate (Legacy)](https://developer.intacct.com/api/employee-expenses/employees/#delete-employee-cost-rate-legacy)

* * *

An employee is a resource that executes work for a company and is associated with a financial transaction such as a timesheet entry or expense transaction.

If the employee is also a user in Sage Intacct (which is required if they will be entering Time & Expenses), the employee must be associated with the correct Sage Intacct user.

* * *

### Get Employee Object Definition

#### `lookup`

> List all the fields and relationships for the employee object:

```
<lookup>
    <object>EMPLOYEE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEE` |

* * *

### Query and List Employees

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, employee ID, and employee’s location :

```
<query>
    <object>EMPLOYEE</object>
    <select>
        <field>RECORDNO</field>
        <field>EMPLOYEEID</field>
        <field>LOCATION.LOCATIONID</field>
    </select>
</query>
```

> List the record number and employee ID for the employee with the given first and last name:

```
<query>
    <object>EMPLOYEE</object>
    <select>
        <field>RECORDNO</field>
        <field>EMPLOYEEID</field>
    </select>
    <filter>
        <and>
            <equalto>
                <field>CONTACT.FIRSTNAME</field>
                <value>dan</value>
            </equalto>
            <equalto>
                <field>CONTACT.LASTNAME</field>
                <value>smith</value>
            </equalto>
        </and>
    </filter>
    <options>
        <caseinsensitive>true</caseinsensitive>
    </options>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEE` |
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

### Query and List Employees (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EMPLOYEE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active and `F` for Inactive. |

**Note:** You cannot use readByQuery to find an employee by first and last name because these names are in an associated record. See the `query` function above, or see the [FAQ](https://developer.intacct.com/support/faq/#how-do-i-query-for-an-object-based-on-a-joined-field-or-how-do-i-query-for-an-employee-by-name) for a workaround.

* * *

### Get Employees

#### `read`

```
<read>
    <object>EMPLOYEE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEE` |
| keys | Required | string | Comma-separated list of employee `RECORDNO` values to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Employees by ID

#### `readByName`

```
<readByName>
    <object>EMPLOYEE</object>
    <keys>E1234</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEE` |
| keys | Required | string | Comma-separated list of `EMPLOYEEID` values of the employees to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Employee

[History](https://developer.intacct.com/api/employee-expenses/employees/#history-create-employee)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added EMPPOSITIONID |

#### `create`

```
<create>
    <EMPLOYEE>
        <PERSONALINFO>
            <CONTACTNAME>John Smith</CONTACTNAME>
        </PERSONALINFO>
    </EMPLOYEE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EMPLOYEE | Required | object | Object to create |

`EMPLOYEE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EMPLOYEEID | Optional | string | Unique ID for the employee. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value. |
| PERSONALINFO | Required | object | Contact info |
| STARTDATE | Optional | string | Start date in format `mm/dd/yyyy` |
| TITLE | Optional | string | Title |
| SSN | Optional | string | Social security number. Do not include dashes. |
| EMPLOYEETYPE | Optional | string | Employee type |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| BIRTHDATE | Optional | string | Birth date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy` |
| TERMINATIONTYPE | Optional | string | Termination type. Use `voluntary`, `involuntary`, `deceased`, `disability`, or `retired`. |
| SUPERVISORID | Optional | string | Manager employee ID |
| GENDER | Optional | string | Gender |
| DEPARTMENTID | Optional | string | Department ID |
| LOCATIONID | Optional | string | Location ID. Required only when an employee is created at the top level in a multi-entity, multi-base-currency company. |
| CLASSID | Optional | string | Class ID |
| EMPPOSITIONID | Optional | string | `POSITIONID` of an active [employee position](https://developer.intacct.com/api/construction/employee-position/). |
| CURRENCY | Optional | string | Default currency code |
| EARNINGTYPENAME | Optional | string | Earning type name |
| POSTACTUALCOST | Optional | boolean | Post actual cost. Use `false` for No, `true` for Yes. (Default: `false`) |
| NAME1099 | Optional | string | Form 1099 name |
| FORM1099TYPE | Optional | string | Form 1099 type |
| FORM1099BOX | Optional | string | Form 1099 box |
| SUPDOCFOLDERNAME | Optional | string | Attachment folder name |
| PAYMETHODKEY | Optional | string | Preferred payment method |
| PAYMENTNOTIFY | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. (Default: `false`) |
| MERGEPAYMENTREQ | Optional | boolean | Merge payment requests. Use `false` for No, `true` for Yes. (Default: `true`) |
| ACHENABLED | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. (Default: `false`) |
| ACHBANKROUTINGNUMBER | Optional | string | ACH bank routing number |
| ACHACCOUNTNUMBER | Optional | string | ACH bank account number |
| ACHACCOUNTTYPE | Optional | string | ACH bank account type |
| ACHREMITTANCETYPE | Optional | string | ACH bank account class |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`PERSONALINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Contact name of an existing contact |

* * *

### Create Employee (Legacy)

[History](https://developer.intacct.com/api/employee-expenses/employees/#history-create-employee-legacy)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added emppositionid |

#### `create_employee`

```
<create_employee>
    <employeeid>E1234</employeeid>
    <title>Project Manager</title>
    <locationid>100</locationid>
    <personalinfo>
        <contactname>Bill Jones (EE1234)</contactname>
    </personalinfo>
</create_employee>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| employeeid | Required | string | Unique ID for the employee. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value. |
| ssn | Optional | string | Social security number. Do not include dashes. |
| title | Optional | string | Title |
| locationid | Optional | string | Location ID. Required only when an employee is created at the top level in a multi-entity, multi-base-currency company. |
| departmentid | Optional | string | Department ID |
| classid | Optional | string | Class ID |
| supervisorid | Optional | string | Manager employee ID |
| birthdate | Optional | object | Birth date |
| startdate | Optional | object | Start date |
| enddate | Optional | object | End date |
| terminationtype | Optional | string | Termination type. Use `voluntary`, `involuntary`, `deceased`, `disability`, or `retired` |
| employeetype | Optional | string | Employee type |
| gender | Optional | string | Gender |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| currency | Optional | string | Default currency code |
| name1099 | Optional | string | Form 1099 name |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| earningtypename | Optional | string | Earning type name |
| postactualcost | Optional | boolean | Post actual cost. Use `false` for No, `true` for Yes. (Default: `false`) |
| emppositionid | Optional | string | `POSITIONID` of an active [employee position](https://developer.intacct.com/api/construction/employee-position/). |
| personalinfo | Required | object | Primary contact info |
| contactlist | Optional | `contactitem[0...n]` | Contact list |
| paymethod | Optional | string | Preferred payment method |
| paymentnotify | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. (Default: `false`) |
| achenabled | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. (Default: `false`) |
| achbankroutingnumber | Optional | string | ACH bank routing number |
| achaccountnumber | Optional | string | ACH bank account number |
| achaccounttype | Optional | string | ACH bank account type |
| achremittancetype | Optional | string | ACH bank account class |
| customfields | Optional | array of `customfield` | Custom fields |
| mergepaymentreq | Optional | boolean | Merge payment requests. Use `false` for No, `true` for Yes. (Default: `true`) |

`personalinfo`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`birthdate`  
`startdate`  
`enddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`contactitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| category | Required | string | Category |
| contactname | Required | string | Contact name of an existing contact |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Employee

[History](https://developer.intacct.com/api/employee-expenses/employees/#history-update-employee)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added EMPPOSITIONID |

#### `update`

```
<update>
    <EMPLOYEE>
        <RECORDNO>12</RECORDNO>
        <TITLE>CEO</TITLE>
    </EMPLOYEE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EMPLOYEE | Required | object | Object to update |

`EMPLOYEE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of employee to update. Required if not using `EMPLOYEEID`. |
| EMPLOYEEID | Optional | string | Employee ID. Required if not using `RECORDNO`. |
| PERSONALINFO | Optional | object | Contact info |
| STARTDATE | Optional | string | Start date in format `mm/dd/yyyy` |
| TITLE | Optional | string | Title |
| SSN | Optional | string | Social security number. Do not include dashes. |
| EMPLOYEETYPE | Optional | string | Employee type |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| BIRTHDATE | Optional | string | Birth date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy` |
| TERMINATIONTYPE | Optional | string | Termination type. Use `voluntary`, `involuntary`, `deceased`, `disability`, or `retired` |
| SUPERVISORID | Optional | string | Manager employee ID |
| GENDER | Optional | string | Gender |
| DEPARTMENTID | Optional | string | Department ID |
| LOCATIONID | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| CLASSID | Optional | string | Class ID |
| CURRENCY | Optional | string | Default currency code |
| EARNINGTYPENAME | Optional | string | Earning type name |
| POSTACTUALCOST | Optional | boolean | Post actual cost. Use `false` for No, `true` for Yes. (Default: `false`) |
| NAME1099 | Optional | string | Form 1099 name |
| FORM1099TYPE | Optional | string | Form 1099 type |
| FORM1099BOX | Optional | string | Form 1099 box |
| SUPDOCFOLDERNAME | Optional | string | Attachment folder name |
| PAYMETHODKEY | Optional | string | Preferred payment method |
| PAYMENTNOTIFY | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. (Default: `false`) |
| ACHENABLED | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. (Default: `false`) |
| ACHBANKROUTINGNUMBER | Optional | string | ACH bank routing number |
| ACHACCOUNTNUMBER | Optional | string | ACH bank account number |
| ACHACCOUNTTYPE | Optional | string | ACH bank account type |
| ACHREMITTANCETYPE | Optional | string | ACH bank account class |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`PERSONALINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Contact name |

* * *

### Update Employee (Legacy)

[History](https://developer.intacct.com/api/employee-expenses/employees/#history-update-employee-legacy)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added emppositionid |

#### `update_employee`

```
<update_employee employeeid="E1234">
    <title>CEO</title>
    <personalinfo>
        <contactname>Bill Jones (EE1234)</contactname>
    </personalinfo>
</update_employee>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| employeeid | Required | string | Employee ID to update |
| ssn | Optional | string | Social security number. Do not include dashes. |
| title | Optional | string | Title |
| locationid | Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |
| departmentid | Optional | string | Department ID |
| classid | Optional | string | Class ID |
| supervisorid | Optional | string | Manager employee ID |
| birthdate | Optional | object | Birth date |
| startdate | Optional | object | Start date |
| enddate | Optional | object | End date |
| terminationtype | Optional | string | Termination type. Use `voluntary`, `involuntary`, `deceased`, `disability`, or `retired`. |
| employeetype | Optional | string | Employee type |
| gender | Optional | string | Gender |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |
| currency | Optional | string | Default currency code |
| name1099 | Optional | string | Form 1099 name |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| earningtypename | Optional | string | Earning type name |
| postactualcost | Optional | boolean | Post actual cost. Use `false` for No, `true` for Yes. |
| emppositionid | Optional | string | `POSITIONID` of an active [employee position](https://developer.intacct.com/api/construction/employee-position/). |
| personalinfo | Required | object | Primary contact info |
| contactlist | Optional | `contactitem[0...n]` | Contact list |
| paymethod | Optional | string | Preferred payment method |
| paymentnotify | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. |
| achenabled | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. |
| achbankroutingnumber | Optional | string | ACH bank routing number |
| achaccountnumber | Optional | string | ACH bank account number |
| achaccounttype | Optional | string | ACH bank account type |
| achremittancetype | Optional | string | ACH bank account class |
| customfields | Optional | array of `customfield` | Custom fields |
| mergepaymentreq | Optional | boolean | Merge payment requests. Use `false` for No, `true` for Yes. |

`personalinfo`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`birthdate`  
`startdate`  
`enddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`contactitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| category | Required | string | Category |
| contactname | Required | string | Contact name of an existing contact |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Employee

#### `delete`

```
<delete>
    <object>EMPLOYEE</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEE` |
| keys | Required | string | Comma-separated list of employee `RECORDNO` to delete |

* * *

### Delete Employee (Legacy)

#### `delete_employee`

```
<delete_employee employeeid="E1234"></delete_employee>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| employeeid | Required | string | Employee ID to delete |

* * *

Employee Cost Rates
-------------------

### Create Employee Cost Rate (Legacy)

#### `create_employeerate`

```
<create_employeerate>
    <employeeid>E1234</employeeid>
    <ratestartdate>
        <year>2016</year>
        <month>2</month>
        <day>1</day>
    </ratestartdate>
    <billingrate></billingrate>
    <salaryrate>75000.00</salaryrate>
</create_employeerate>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| employeeid | Required | string | Employee ID |
| ratestartdate | Required | object | Start date |
| billingrate | Optional | currency | Hourly rate. Do not use if `salaryrate` is set. |
| salaryrate | Optional | currency | Annual salary. Do not use if `billingrate` is set. |
| customfields | Optional | array of `customfield` | Custom fields |

`ratestartdate`

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

### Update Employee Cost Rate (Legacy)

#### `update_employeerate`

```
<update_employeerate key="1234">
    <ratestartdate>
        <year>2016</year>
        <month>9</month>
        <day>15</day>
    </ratestartdate>
    <billingrate></billingrate>
    <salaryrate>80000.00</salaryrate>
</update_employeerate>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | integer | Record number of rate to update |
| ratestartdate | Optional | object | Start date |
| billingrate | Optional | currency | Hourly rate. Do not use if `salaryrate` is set. |
| salaryrate | Optional | currency | Annual salary. Do not use if `billingrate` is set. |
| customfields | Optional | array of `customfield` | Custom fields |

`ratestartdate`

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

### Delete Employee Cost Rate (Legacy)

#### `delete_employeerate`

```
<delete_employeerate key="1234"/>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Record number of rate to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

