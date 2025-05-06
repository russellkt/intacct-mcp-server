Title: Account Groups

URL Source: https://developer.intacct.com/api/general-ledger/account-groups/

Markdown Content:
*   [Account Group](https://developer.intacct.com/api/general-ledger/account-groups/#account-group)
    *   [Get Account Group Object Definition](https://developer.intacct.com/api/general-ledger/account-groups/#get-account-group-object-definition)
    *   [Query and List Account Groups](https://developer.intacct.com/api/general-ledger/account-groups/#query-and-list-account-groups)
    *   [Query and List Account Groups (Legacy)](https://developer.intacct.com/api/general-ledger/account-groups/#query-and-list-account-groups-legacy)
    *   [Get Account Group](https://developer.intacct.com/api/general-ledger/account-groups/#get-account-group)
    *   [Get Account Group by ID](https://developer.intacct.com/api/general-ledger/account-groups/#get-account-group-by-id)
    *   [Create Account Group](https://developer.intacct.com/api/general-ledger/account-groups/#create-account-group)
    *   [Update Account Group](https://developer.intacct.com/api/general-ledger/account-groups/#update-account-group)
    *   [Delete Account Group](https://developer.intacct.com/api/general-ledger/account-groups/#delete-account-group)
*   [Account Group Hierarchy](https://developer.intacct.com/api/general-ledger/account-groups/#account-group-hierarchy)
    *   [Get Account Group Hierarchy Object Definition](https://developer.intacct.com/api/general-ledger/account-groups/#get-account-group-hierarchy-object-definition)
    *   [Query and List Account Group Hierarchy](https://developer.intacct.com/api/general-ledger/account-groups/#query-and-list-account-group-hierarchy)
    *   [Query and List Account Group Hierarchy (Legacy)](https://developer.intacct.com/api/general-ledger/account-groups/#query-and-list-account-group-hierarchy-legacy)

* * *

Account groups are the fundamental building blocks of financial reporting.

Every account must be part of an account group if its data is to be used in a balance sheet, income statement, cash flow, or other report. The most basic types of account groups contain either individual accounts or other account groups.

* * *

Account Group
-------------

### Get Account Group Object Definition

#### `lookup`

> List all the fields and relationships for the account group object:

```
<lookup>
    <object>GLACCTGRP</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRP` |

* * *

### Query and List Account Groups

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each account group:

```
<query>
    <object>GLACCTGRP</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRP` |
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

### Query and List Account Groups (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>GLACCTGRP</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRP` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Account Group

#### `read`

```
<read>
    <object>GLACCTGRP</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRP` |
| keys | Required | string | Comma-separated list of account group `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |

* * *

### Get Account Group by ID

#### `readByName`

```
<readByName>
    <object>GLACCTGRP</object>
    <keys>Cash and Cash Equivalents</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRP` |
| keys | Required | string | Comma-separated list of account group `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Account Group

[History](https://developer.intacct.com/api/general-ledger/account-groups/#history-create-account-group)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | Added GLACCTGRPPURPOSEID, ACCTGROUPMANAGER |

#### `create`

```
<create>
    <GLACCTGRP>
        <NAME>BS - Cash</NAME>
        <TITLE>Cash</TITLE>
        <TOTALTITLE>Total Cash</TOTALTITLE>
        <NORMAL_BALANCE>debit</NORMAL_BALANCE>
        <ISKPI>false</ISKPI>
        <MEMBERTYPE>Accounts</MEMBERTYPE>
        <ASOF>E</ASOF>

        <GLACCTRANGES>
            <ACCTRANGE>
                <RANGEFROM>1000</RANGEFROM>
                <RANGETO>1099</RANGETO>
            </ACCTRANGE>
        </GLACCTRANGES>

        <DBCR></DBCR>
        <FILTERDEPT></FILTERDEPT>
        <DEPTNO></DEPTNO>
        <FILTERLOC></FILTERLOC>
        <LOCNO></LOCNO>
        <FILTERVENDOR></FILTERVENDOR>
        <VENDORID></VENDORID>
        <FILTERCUSTOMER></FILTERCUSTOMER>
        <CUSTOMERID></CUSTOMERID>
        <FILTERPROJECT></FILTERPROJECT>
        <PROJECTID></PROJECTID>
        <FILTEREMPLOYEE></FILTEREMPLOYEE>
        <EMPLOYEEID></EMPLOYEEID>
        <FILTERITEM></FILTERITEM>
        <ITEMID></ITEMID>
        <FILTERCLASS></FILTERCLASS>
        <CLASSID></CLASSID>

    </GLACCTGRP>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTGRP | Required | object | Object to create |

`GLACCTGRP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Name |
| TITLE | Optional | string | Display on report as |
| TOTALTITLE | Optional | string | Display total line as |
| NORMAL\_BALANCE | Optional | string | Normal balance. Use either `debit` or `credit`. (Default: `debit`) |
| ISKPI | Optional | boolean | Is a KPI. Use either `true` or `false`. (Default: `false`) |
| GLACCTGRPPURPOSEID | Optional | string | Account group purpose ID, which is used for financial reporting. |
| ACCTGROUPMANAGER | Optional | string | Person to consult if there are questions about the account group. This is a free form field not tied to users (you can provide a partner name, or any other name). |
| MEMBERTYPE | Required | string | Structure type. Use either `Accounts`, `Groups`, `Statistical Accounts`, `Computation`, `Category`, `Statistical Category`. |
| ASOF | Optional | string | Calculation method. Use either `P` for For period, `B` for Start of period, or `E` for End of period. (Default: `P`) |
| GLACCTRANGES | Optional | `ACCTRANGE[0...n]` | Account range group members. Only used if Structure type is `Accounts` |
| GLACCTGRPS | Optional | `GLACCTGRPMEMBER[0...n]` | Account group members. Only used if Structure type is `Groups` |
| GLSTATACCTRANGES | Optional | `ACCTRANGE[0...n]` | Statistical account group members. Only used if Structure type is `Statistical Accounts` |
| GLCOMPGRPS | Optional | `GLCOMPGRPMEMBER[0...n]` | Computation members. Only used if Structure type is `Computation` |
| GLCATGRPS | Optional | `GLCOACATMEMBER[0...n]` | Category members. Only used if Structure type is `Category` |
| GLSTATCATGRPS | Optional | `GLCOACATMEMBER[0...n]` | Statistical category members. Only used if Structure type is `Statistical Category` |
| DBCR | Optional | string | Debit/Credit report filter. Use either `Both`, `Debit Only`, or `Credit Only`. (Default: `Both`) |
| FILTERDEPT | Optional | string | Department report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| DEPTNO | Optional | string | Department ID or department group ID. Only used if FILTERDEPT set to specific. |
| FILTERLOC | Optional | string | Location report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| LOCNO | Optional | string | Location ID or location group ID. Only used if FILTERLOC set to specific. |
| FILTERVENDOR | Optional | string | Vendor report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| VENDORID | Optional | string | Vendor ID or vendor group ID. Only used if FILTERVENDOR set to specific. |
| FILTERCUSTOMER | Optional | string | Customer report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| CUSTOMERID | Optional | string | Customer ID or customer group ID. Only used if FILTERCUSTOMER set to specific. |
| FILTERPROJECT | Optional | string | Project report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| PROJECTID | Optional | string | Project ID or project group ID. Only used if FILTERPROJECT set to specific. |
| FILTEREMPLOYEE | Optional | string | Employee report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| EMPLOYEEID | Optional | string | Employee ID or employee group ID. Only used if FILTEREMPLOYEE set to specific. |
| FILTERITEM | Optional | string | Item report filter option. Use either `nofilter`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| ITEMID | Optional | string | Item ID or item group ID. Only used if FILTERITEM set to specific. |
| FILTERCLASS | Optional | string | Class report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| CLASSID | Optional | string | Class ID or class group ID. Only used if FILTERCLASS set to specific. |
| FILTERGLDIM\* | Optional | string | User defined dimension filter option. UDD object integration name usually appended to `FILTERGLDIM`. Use either `nofilter`, `specific`, or `nullvalue`. (Default: `nofilter`) |
| GLDIM\* | Optional | integer | User defined dimension `id` field. UDD object integration name usually appended to `GLDIM`. Only used if FILTERGLDIM\* set to specific. |

`ACCTRANGE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RANGEFROM | Required | string | Range from account number |
| RANGETO | Required | string | Range to account number |

`GLACCTGRPMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHILDNAME | Required | string | Account group name |

`GLCOMPGRPMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LHSACCTNO | Optional | string | Left hand side account number |
| LHSACCTGRPNAME | Optional | string | Left hand side account group name |
| LHSCONST | Optional | number | Left hand side constant. |
| LHSASOF | Optional | string | Left hand side calculated amount. Use `P` for For period, `B` for Start of period, or `E` for End of period. |
| OPERATOR | Optional | string | Operator. Use either `A` for add, `S` for subtract, `M` for multiply, or `D` for divide. |
| RHSACCTNO | Optional | string | Right hand side account number |
| RHSACCTGRPNAME | Optional | string | Right hand side account group name |
| RHSCONST | Optional | number | Right hand side constant. |
| RHSASOF | Optional | string | Right hand side calculated amount. Use `P` for For period, `B` for Start of period, or `E` for End of period. |
| PRECISION | Optional | integer | Decimal places. Must be between 0-9. |
| DISPLAYAS | Optional | string | Display as. Use `V` for Number, `P` for Percent, `R` for Ratio with decimals, `F` for Ratio without decimals, `D` for Daily average, `W` for Weekly average, `M` for Monthly average, `Q` for Quarterly average |
| UOM | Optional | string | Unit |

`GLCOACATMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CATEGORYNAME | Required | string | Category name |

* * *

### Update Account Group

[History](https://developer.intacct.com/api/general-ledger/account-groups/#history-update-account-group)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | Added GLACCTGRPPURPOSEID, ACCTGROUPMANAGER |

The members, based on the structure type of the group, must also be passed with any update.

#### `update`

```
<update>
    <GLACCTGRP>
        <RECORDNO>123</RECORDNO>
        <TITLE>Cash and Cash Equivalents</TITLE>
        <TOTALTITLE>Total Cash and Cash Equivalents</TOTALTITLE>
        <GLACCTRANGES>
            <ACCTRANGE>
                <RANGEFROM>1000</RANGEFROM>
                <RANGETO>1099</RANGETO>
            </ACCTRANGE>
        </GLACCTRANGES>
    </GLACCTGRP>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTGRP | Required | object | Object to update |

`GLACCTGRP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of account group to update. Required if not using `NAME`. |
| NAME | Optional | string | Account group name. Required if not using `RECORDNO`. |
| TITLE | Optional | string | Display on report as |
| TOTALTITLE | Optional | string | Display total line as |
| NORMAL\_BALANCE | Optional | string | Normal balance. Use either `debit` or `credit`. |
| ISKPI | Optional | boolean | Is a KPI. Use either `true` or `false`. (Default: `false`) |
| GLACCTGRPPURPOSEID | Optional | string | Account group purpose ID, which is used for financial reporting. |
| ACCTGROUPMANAGER | Optional | string | Person to consult if there are questions about the account group. This is a free form field not tied to users (you can provide a partner name, or any other name). |
| ASOF | Optional | string | Calculation method. Use either `P` for For period, `B` for Start of period, or `E` for End of period. |
| GLACCTRANGES | Optional | `ACCTRANGE[0...n]` | Account range group members. Only used if Structure type is `Accounts` |
| GLACCTGRPS | Optional | `GLACCTGRPMEMBER[0...n]` | Account group members. Only used if Structure type is `Groups` |
| GLSTATACCTRANGES | Optional | `ACCTRANGE[0...n]` | Statistical account group members. Only used if Structure type is `Statistical Accounts` |
| GLCOMPGRPS | Optional | `GLCOMPGRPMEMBER[0...n]` | Computation members. Only used if Structure type is `Computation` |
| GLCATGRPS | Optional | `GLCOACATMEMBER[0...n]` | Category members. Only used if Structure type is `Category` |
| GLSTATCATGRPS | Optional | `GLCOACATMEMBER[0...n]` | Statistical category members. Only used if Structure type is `Statistical Category` |
| DBCR | Optional | string | Debit/Credit report filter. Use either `Both`, `Debit Only`, or `Credit Only`. |
| FILTERDEPT | Optional | string | Department report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. |
| DEPTNO | Optional | string | Department ID or department group ID. Only used if FILTERDEPT set to specific. |
| FILTERLOC | Optional | string | Location report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. |
| LOCNO | Optional | string | Location ID or location group ID. Only used if FILTERLOC set to specific. |
| FILTERVENDOR | Optional | string | Vendor report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. |
| VENDORID | Optional | string | Vendor ID or vendor group ID. Only used if FILTERVENDOR set to specific. |
| FILTERCUSTOMER | Optional | string | Customer report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. |
| CUSTOMERID | Optional | string | Customer ID or customer group ID. Only used if FILTERCUSTOMER set to specific. |
| FILTERPROJECT | Optional | string | Project report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. |
| PROJECTID | Optional | string | Project ID or project group ID. Only used if FILTERPROJECT set to specific. |
| FILTEREMPLOYEE | Optional | string | Employee report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. |
| EMPLOYEEID | Optional | string | Employee ID or employee group ID. Only used if FILTEREMPLOYEE set to specific. |
| FILTERITEM | Optional | string | Item report filter option. Use either `nofilter`, `specific`, or `nullvalue`. |
| ITEMID | Optional | string | Item ID or item group ID. Only used if FILTERITEM set to specific. |
| FILTERCLASS | Optional | string | Class report filter option. Use either `nofilter`, `specifichierarchy`, `specific`, or `nullvalue`. |
| CLASSID | Optional | string | Class ID or class group ID. Only used if FILTERCLASS set to specific. |
| FILTERGLDIM\* | Optional | string | User defined dimension filter option. UDD object integration name usually appended to `FILTERGLDIM`. Use either `nofilter`, `specific`, or `nullvalue`. |
| GLDIM\* | Optional | integer | User defined dimension `id` field. UDD object integration name usually appended to `GLDIM`. Only used if FILTERGLDIM\* set to specific. |

`ACCTRANGE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RANGEFROM | Required | string | Range from account number |
| RANGETO | Required | string | Range to account number |

`GLACCTGRPMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHILDNAME | Required | string | Account group name |

`GLCOMPGRPMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LHSACCTNO | Optional | string | Left hand side account number |
| LHSACCTGRPNAME | Optional | string | Left hand side account group name |
| LHSCONST | Optional | number | Left hand side constant. |
| LHSASOF | Optional | string | Left hand side calculated amount. Use `P` for For period, `B` for Start of period, or `E` for End of period. |
| OPERATOR | Optional | string | Operator. Use either `A` for add, `S` for subtract, `M` for multiply, or `D` for divide. |
| RHSACCTNO | Optional | string | Right hand side account number |
| RHSACCTGRPNAME | Optional | string | Right hand side account group name |
| RHSCONST | Optional | number | Right hand side constant. |
| RHSASOF | Optional | string | Right hand side calculated amount. Use `P` for For period, `B` for Start of period, or `E` for End of period. |
| PRECISION | Optional | integer | Decimal places. Must be between 0-9. |
| DISPLAYAS | Optional | string | Display as. Use `V` for Number, `P` for Percent, `R` for Ratio with decimals, `F` for Ratio without decimals, `D` for Daily average, `W` for Weekly average, `M` for Monthly average, `Q` for Quarterly average |
| UOM | Optional | string | Unit |

`GLCOACATMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CATEGORYNAME | Required | string | Category name |

* * *

### Delete Account Group

#### `delete`

```
<delete>
    <object>GLACCTGRP</object>
    <keys>1169</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRP` |
| keys | Required | string | Comma-separated list of account group `RECORDNO` to delete |

* * *

Account Group Hierarchy
-----------------------

### Get Account Group Hierarchy Object Definition

#### `lookup`

> List all the fields and relationships for the account group hierarchy object:

```
<lookup>
    <object>GLACCTGRPHIERARCHY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPHIERARCHY` |

* * *

### Query and List Account Group Hierarchy

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the entire hierarchy of the Revenue group:

```
<query>
    <object>GLACCTGRPHIERARCHY</object>
    <select>
        <field>RECORDNO</field>
        <field>GLACCTGRPNAME</field>
        <field>ACCOUNTNO</field>
    </select>
    <filter>
        <equalto>
            <field>GLACCTGRPNAME</field>
            <value>Revenue</value>
        </equalto>
    </filter>
</query>
```

> List the groups containing account 1010:

```
<query>
    <object>GLACCTGRPHIERARCHY</object>
    <select>
        <field>RECORDNO</field>
        <field>GLACCTGRPNAME</field>
        <field>ACCOUNTNO</field>
    </select>
    <filter>
        <equalto>
            <field>ACCOUNTNO</field>
            <value>1010</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPHIERARCHY` |
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

### Query and List Account Group Hierarchy (Legacy)

#### `readByQuery`

> List the entire hierarchy of the Assets group:

```
<readByQuery>
    <object>GLACCTGRPHIERARCHY</object>
    <fields>*</fields>
    <query>GLACCTGRPNAME = 'Assets'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List the groups containing account 1010:

```
<readByQuery>
    <object>GLACCTGRPHIERARCHY</object>
    <fields>*</fields>
    <query>ACCOUNTNO = '1010'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTGRPHIERARCHY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTGRPNAME | Optional | string | Account group name |
| GLACCTGRPKEY | Optional | integer | Acount group record number |
| ACCOUNTNO | Optional | string | Account number |
| ACCOUNTKEY | Optional | integer | Account record number |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

