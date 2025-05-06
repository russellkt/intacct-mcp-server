Title: Account Allocations

URL Source: https://developer.intacct.com/api/general-ledger/account-allocations/

Markdown Content:
*   [Account Allocation](https://developer.intacct.com/api/general-ledger/account-allocations/#account-allocation)
    *   [Get Account Allocation Definition Object Definition](https://developer.intacct.com/api/general-ledger/account-allocations/#get-account-allocation-definition-object-definition)
    *   [Query and List Account Allocation Definitions](https://developer.intacct.com/api/general-ledger/account-allocations/#query-and-list-account-allocation-definitions)
    *   [Query and List Account Allocation Definitions (Legacy)](https://developer.intacct.com/api/general-ledger/account-allocations/#query-and-list-account-allocation-definitions-legacy)
    *   [Get Account Allocation Definition](https://developer.intacct.com/api/general-ledger/account-allocations/#get-account-allocation-definition)
    *   [Create Account Allocation Definition](https://developer.intacct.com/api/general-ledger/account-allocations/#create-account-allocation-definition)
    *   [Update Account Allocation Definition](https://developer.intacct.com/api/general-ledger/account-allocations/#update-account-allocation-definition)
    *   [Delete Account Allocation Definition](https://developer.intacct.com/api/general-ledger/account-allocations/#delete-account-allocation-definition)
*   [Account Allocation Run](https://developer.intacct.com/api/general-ledger/account-allocations/#account-allocation-run)
    *   [Get Account Allocation Run Object Definition](https://developer.intacct.com/api/general-ledger/account-allocations/#get-account-allocation-run-object-definition)
    *   [Query and List Account Allocation Runs](https://developer.intacct.com/api/general-ledger/account-allocations/#query-and-list-account-allocation-runs)
    *   [Query and List Account Allocation Runs (Legacy)](https://developer.intacct.com/api/general-ledger/account-allocations/#query-and-list-account-allocation-runs-legacy)
    *   [Get Account Allocation Run](https://developer.intacct.com/api/general-ledger/account-allocations/#get-account-allocation-run)
    *   [Create Account Allocation Run](https://developer.intacct.com/api/general-ledger/account-allocations/#create-account-allocation-run)

* * *

Account allocations let you automatically distribute amounts across multiple dimensions such as departments, locations, projects, or classes.

An account allocation definition is a template for allocations. After it’s created, you can generate the allocation as often as needed using the same definition to streamline the overall allocation process. For example, you can create an allocation definition that distributes expenses across revenue-earning departments, then run an allocation using that definition for the dates you want.

Note that intra-entity (not inter-entity) revenue and expense allocations are supported at this time.

Your company must have a subscription for Dynamic Allocations, and you need the appropriate permissions for account allocations. Usage information for [account allocations](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Account_allocations_overview) is available in the Sage Intacct product help.

[Transaction Allocations](https://developer.intacct.com/api/general-ledger/transaction-allocations/) also let you distribute transaction amounts across multiple dimensions—such as departments, locations, projects, or classes. However, a transaction allocation is intended for use on single line item as a one-time action.

* * *

Account Allocation
------------------

### Get Account Allocation Definition Object Definition

#### `lookup`

> List all the fields and relationships for the account allocation definition object:

```
<lookup>
    <object>GLACCTALLOCATION</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATION` |

* * *

### Query and List Account Allocation Definitions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and ID for each account allocation definition:

```
<query>
    <object>GLACCTALLOCATION</object>
    <select>
        <field>RECORDNO</field>
        <field>ACCTALLOCATIONID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATION` |
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

### Query and List Account Allocation Definitions (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>GLACCTALLOCATION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status.
*   `T` - Active
*   `F` - Inactive

 |
| ACTIVITYDELTA | Optional | string | Activity delta.

*   `T` - Activity Delta
*   `F` - not selected

 |

* * *

### Get Account Allocation Definition

#### `read`

```
<read>
    <object>GLACCTALLOCATION</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATION` |
| keys | Required | string | Comma-separated list of account allocation definition `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

### Create Account Allocation Definition

[History](https://developer.intacct.com/api/general-ledger/account-allocations/#history-create-account-allocation-definition)

| Release | Changes |
| --- | --- |
| 2022 Release 3 | Added "Per dimension value" allocation type for FOCUSEMPLOYEE and FOCUSPROJECT. |
| 2020 Release 3 | Added ALLOWALLOCATION, EXCH\_RATE\_TYPE\_ID |

#### `create`

> Distributes expenses for the month to the departments that generate revenue:

```
<create>
    <GLACCTALLOCATION>
        <ACCTALLOCATIONID>Monthly expenses</ACCTALLOCATIONID>
        <DESCRIPTION>Monthly allocation of expenses</DESCRIPTION>
        <METHODOLOGY>Expense allocation across revenue earning departments</METHODOLOGY>
        <FOCUSLOCATION>Preserve values</FOCUSLOCATION>
        <FOCUSDEPARTMENT>Allocation focus</FOCUSDEPARTMENT>
        <FOCUSPROJECT>Preserve values</FOCUSPROJECT>
        <GLACCTALLOCATIONSOURCE>
            <GLACCTGRP>Expenses</GLACCTGRP>
            <PERCENT2ALLOCATE>100</PERCENT2ALLOCATE>
            <REPORTINGBOOK>ACCRUAL</REPORTINGBOOK>
            <GLACCTALLOCATIONSOURCEADJBOOKS>
                <GLACCTALLOCATIONSOURCEADJBOOK>
                    <ADJBOOKID>GAAPADJ</ADJBOOKID>
                </GLACCTALLOCATIONSOURCEADJBOOK>
                <GLACCTALLOCATIONSOURCEADJBOOK>
                    <ADJBOOKID>TAXADJ</ADJBOOKID>
                </GLACCTALLOCATIONSOURCEADJBOOK>
            </GLACCTALLOCATIONSOURCEADJBOOKS>
            <SOURCEINCLUDEREPORTINGBOOK>Main reporting book and alternate books</SOURCEINCLUDEREPORTINGBOOK>
            <TIMEPERIOD>Current Month</TIMEPERIOD>
            <LOCNO>1st Level Locations--Level 1 Locations</LOCNO>
        </GLACCTALLOCATIONSOURCE>
        <GLACCTALLOCATIONBASIS>
            <GLACCTGRP>Revenues</GLACCTGRP>
            <ACCUMULATION>Activity</ACCUMULATION>
            <ALLOCATIONMETHOD>Dynamic-relative account financial</ALLOCATIONMETHOD>
            <TIMEPERIOD>Current Month</TIMEPERIOD>
            <REPORTINGBOOK>ACCRUAL</REPORTINGBOOK>
            <SKIPNEGATIVE>false</SKIPNEGATIVE>
            <LOCNO>1st Level Locations--Level 1 Locations</LOCNO>
        </GLACCTALLOCATIONBASIS>
        <GLACCTALLOCATIONTARGET>
            <REPORTINGBOOK>ACCRUAL</REPORTINGBOOK>
            <JOURNALSYMBOL>Travel</JOURNALSYMBOL>
            <GLACCOUNTNO>8000</GLACCOUNTNO>
        </GLACCTALLOCATIONTARGET>
        <GLACCTALLOCATIONREVERSE>
            <USESOURCEACCOUNT>true</USESOURCEACCOUNT>
        </GLACCTALLOCATIONREVERSE>
    </GLACCTALLOCATION>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATION | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#create-GLACCTALLOCATION) | Object to create |

Provides basic information for the allocation and specifies how dimensions are to be handled in the allocation calculations.

`GLACCTALLOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCTALLOCATIONID | Required | string | Allocation ID. Must be 20 character or fewer. |
| DESCRIPTION | Required | string | Description of the allocation definition |
| STATUS | Optional | boolean | Status of the allocation definition.
*   `active` (default)
*   `inactive`

 |
| METHODOLOGY | Optional | string | Description of methodology used for the allocation definition |
| ACTIVITYDELTA | Optional | string | Activity Delta.

*   `false` (default)
*   `true`: Before allocation, validate that the account setup is designed to clear the source amounts with each allocation generation. This is done by making sure that the accounts selected for your source pool are used as the reversing source pool selection, or if an alternate specific account is used for the reversal, that it's included in the source pool account group so that it removes any prior allocation activity. This option is only effective if the source account is used for the pool reversal in the allocation target, either via `GLACCOUNTNO` or `USESOURCEACCOUNT`.

 |
| ALLOWALLOCATION | Optional | string | Specifies whether to allow allocations across entities.

*   `Within one entity` (default)
*   `Across entities` When you allocate across entities, you need to specify an exchange rate type (`EXCH_RATE_TYPE_ID`) for the allocation target (`GLACCTALLOCATIONTARGET`).

 |
| FOCUSLOCATION | Optional | string | Dimensions treatment for Location. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSVENDOR | Optional | string | Dimensions treatment for Vendor. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSPROJECT | Optional | string | Dimensions treatment for Project. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.
*   `Per dimension value` - Allocate based on the value of the dimension.

 |
| FOCUSDEPARTMENT | Optional | string | Dimensions treatment for Department. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSCUSTOMER | Optional | string | Dimensions treatment for Customer. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSITEM | Optional | string | Dimensions treatment for Item. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSCLASS | Optional | string | Dimensions treatment for Class. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSEMPLOYEE | Optional | string | Dimensions treatment for Employee. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.
*   `Per dimension value` - Allocate based on the value of the dimension.

 |
| FOCUSWAREHOUSE | Optional | string | Dimensions treatment for Warehouse. Specifies how the dimension is used in the allocation calculation. Currently, only `Not considered` is allowed. |
| FOCUSCONTRACT | Optional | string | Dimensions treatment for Contract. Specifies how the dimension is used in the allocation calculation. Currently, only `Not considered` is allowed. |
| GLACCTALLOCATIONSOURCE | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#create-GLACCTALLOCATIONSOURCE) | Source pool for the allocation. |
| GLACCTALLOCATIONBASIS | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#create-GLACCTALLOCATIONBASIS) | Basis information that specifies how the allocation splits source amounts into each target. |
| GLACCTALLOCATIONTARGET | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#create-GLACCTALLOCATIONTARGET) | Allocation destination in the target entry. Specifies where the allocation will be recorded. The debit and credit accounts selected depend on your allocation setup. For example, expense allocations typically have the allocation as a debit. |
| GLACCTALLOCATIONREVERSE | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#create-GLACCTALLOCATIONREVERSE) | Reversing source pool in the target entry |

`GLACCTALLOCATION.GLACCTALLOCATIONSOURCE`

If choosing dimensions for filtering from the source pool, remember your choices for dimension treatment. For example, if you specified that the Vendor dimension should not be considered, choosing a Vendor ID for the source does not impact the allocation calculations.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTGRP | Required | string | Account group for the source of the allocation. To use a single account, provide an account group with one account. |
| PERCENT2ALLOCATE | Required | string | Percentage to allocate. |
| REPORTINGBOOK | Required | string | Reporting Book. Accounting method to use.
*   `ACCRUAL`
*   `CASH`

 |
| GLACCTALLOCATIONSOURCEADJBOOKS | Optional | array of [GLACCTALLOCATIONSOURCEADJBOOK](https://developer.intacct.com/api/general-ledger/account-allocations/#create-GLACCTALLOCATIONSOURCEADJBOOK) | Alternate Book selections |
| SOURCEINCLUDEREPORTINGBOOK | Optional | string | Use entries from.

*   `Main reporting book and alternate books` (default)
*   `Alternate books only`

 |
| TIMEPERIOD | Required | string | Source pool time period.

*   `Current Month`
*   `Prior Month`
*   `Current Quarter`
*   `Prior Quarter`
*   `Current Year`
*   `Current Year To Date`
*   `Prior Year`
*   `Prior Year Current Month`
*   `Prior Year Current Quarter`
*   `Fiscal - Current Quarter`
*   `Fiscal - Prior Quarter`
*   `Fiscal - Current Year`
*   `Fiscal - Current Year To Date`
*   `Fiscal - Prior Year`
*   `Inception To Date`

(applies only for Project dimension allocation focus). |
| LOCNO | Optional | string | Entity/Location for dimension filtering from the source pool |
| VENDORID | Optional | string | Vendor for dimension filtering from the source pool |
| PROJECTID | Optional | string | Project for dimension filtering from the source pool |
| DEPTNO | Optional | string | Department for dimension filtering from the source pool |
| CUSTOMERID | Optional | string | Customer for dimension filtering from the source pool |
| WAREHOUSE | Optional | string | Warehouse for dimension filtering from the source pool. |
| CONTRACTID | Optional | string | Contract for dimension filtering from the source pool |
| ITEMID | Optional | string | Item for dimension filtering from the source pool |
| CLASSID | Optional | string | Class for dimension filtering from the source pool |
| EMPLOYEEID | Optional | string | Employee for dimension filtering from the source pool |

`GLACCTALLOCATION.GLACCTALLOCATIONSOURCE.GLACCTALLOCATIONSOURCEADJBOOK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ADJBOOKID | Optional | string | Book ID for the adjustment book.
*   `GAAPADJ`
*   `TAXADJ`
*   a user-defined book

 |

`GLACCTALLOCATION.GLACCTALLOCATIONBASIS`

If choosing dimensions for filtering for the basis, remember your choices for dimension treatment. For example, if you specified that the Vendor dimension should not be considered, choosing a Vendor ID for the basis does not impact the allocation calculations.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ALLOCATIONMETHOD | Required | string | Allocation method.
*   `Dynamic-relative account financial`
*   `Dynamic-relative account statistical`

 |
| GLACCTGRP | Required | string | Account group for the basis of the allocation. To use a single account, provide an account group with one account. |
| ACCUMLUATION | Required | string | Accumulation. Use `Activity`. |
| REPORTINGBOOK | Required | string | Reporting Book. Set this to `ACCRUAL`. |
| GLACCTALLOCATIONBASISADJBOOKS | Optional | array of [GLACCTALLOCATIONBASISADJBOOK](https://developer.intacct.com/api/general-ledger/account-allocations/#create-GLACCTALLOCATIONBASISADJBOOK) | Alternate Book selections. |
| BASISINCLUDEREPORTINGBOOK | Optional | string | Use entries from.

*   `Main reporting book and alternate books` (default)
*   `Alternate books only`

 |
| TIMEPERIOD | Required | string | Basis time period. You can use the same time period as the source pool, or you can select a different time period for your basis.

*   `Current Month`
*   `Prior Month`
*   `Current Quarter`
*   `Prior Quarter`
*   `Current Year`
*   `Current Year To Date`
*   `Prior Year`
*   `Prior Year Current Month`
*   `Prior Year Current Quarter`
*   `Fiscal - Current Quarter`
*   `Fiscal - Prior Quarter`
*   `Fiscal - Current Year`
*   `Fiscal - Current Year To Date`
*   `Fiscal - Prior Year`
*   `Inception To Date`

(applies only for Project dimension allocation focus). |
| SKIPNEGATIVE | Optional | boolean | Drop negative basis lines from consideration.

*   `false` (default)
*   `true` - drop negative lines

 |
| LOCNO | Optional | string | Entity/Location for dimension filtering to narrow the scope for the basis methodology |
| VENDORID | Optional | string | Vendor for dimension filtering to narrow the scope for the basis methodology |
| PROJECTID | Optional | string | Project for dimension filtering to narrow the scope for the basis methodology |
| DEPTNO | Optional | string | Department for dimension filtering to narrow the scope for the basis methodology |
| CUSTOMERID | Optional | string | Customer for dimension filtering to narrow the scope for the basis methodology |
| WAREHOUSEID | Optional | string | Warehouse for dimension filtering to narrow the scope for the basis methodology |
| CONTRACTID | Optional | string | Contract for dimension filtering to narrow the scope for the basis methodology |
| ITEMID | Optional | string | Item for dimension filtering to narrow the scope for the basis methodology |
| CLASSID | Optional | string | Class for dimension filtering to narrow the scope for the basis methodology |
| EMPLOYEEID | Optional | string | Employee for dimension filtering to narrow the scope for the basis methodology |

`GLACCTALLOCATION.GLACCTALLOCATIONBASIS.GLACCTALLOCATIONBASISADJBOOK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ADJBOOKID | Optional | string | Book ID for the adjustment book. Use `GAAPADJ`, `TAXADJ`, or a user-defined book. |

`GLACCTALLOCATION.GLACCTALLOCATIONTARGET`

When choosing dimensions for filtering to the target, you can override dimension treatments. For example, if you specified that the Vendor dimension should not be considered, you can use the vendor override parameter to provide a vendor to be used in the allocation for the target.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCOUNTNO | Required | string | Account that is the target destination of the allocation. |
| JOURNALSYBMOL | Required | string | Journal for the allocation journal entries |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Required if `ALLOWALLOCATION` is set to `Across entities` in the header. |
| OVERRIDELOCATION | Optional | string | Dimension override for Entity/Location. Applies only if the dimension treatment for Location is set to `Not considered`. |
| OVERRIDEVENDOR | Optional | string | Dimension override for Vendor. Applies only if the dimension treatment for Vendor is set to `Not considered`. |
| OVERRIDEPROJECT | Optional | string | Dimension override for Project. Applies only if the dimension treatment for Project is set to `Not considered`. |
| OVERRIDEDEPARTMENT | Optional | string | Dimension override for Department. Applies only if the dimension treatment for Department is set to `Not considered`. |
| OVERRIDECUSTOMER | Optional | string | Dimension override for Customer. Applies only if the dimension treatment for Customer is set to `Not considered`. |
| OVERRIDEWAREHOUSE | Optional | string | Dimension override for Warehouse. Applies only if the dimension treatment for Warehouse is set to `Not considered`. |
| OVERRIDECONTRACT | Optional | string | Dimension override for Contract. Applies only if the dimension treatment for Contract is set to `Not considered`. |
| OVERRIDEITEM | Optional | string | Dimension override for Item. Applies only if the dimension treatment for Item is set to `Not considered`. |
| BILLABLE | Optional | boolean | Specifies that lines in the allocation target are billable. Applies only if Project is part of the allocation and Project billing is enabled for General Ledger. Use `true` for billable, `false` otherwise. (Default: `false`) |
| OVERRIDECLASS | Optional | string | Dimension override for Class. Applies only if the dimension treatment for Class is set to `Not considered`. |
| OVERRIDEEMPLOYEE | Optional | string | Dimension override for Employee. Applies only if the dimension treatment for Employee is set to `Not considered`. |

`GLACCTALLOCATION.GLACCTALLOCATIONREVERSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCOUNTNO | Optional | string | Account to use for the reversal pool for the account allocation. Required if not using the source account. |
| USESOURCEACCOUNT | Optional | boolean | Use the source account for the reversal pool for the account allocation. Required if not providing an account. |
| OVERRIDELOCATION | Optional | string | Dimension override for Entity/Location. |
| OVERRIDEVENDOR | Optional | string | Dimension override for Vendor. |
| OVERRIDEPROJECT | Optional | string | Dimension override for Project. |
| OVERRIDEDEPARTMENT | Optional | string | Dimension override for Department. |
| OVERRIDECUSTOMER | Optional | string | Dimension override for Customer. |
| OVERRIDEWAREHOUSE | Optional | string | Dimension override for Warehouse. |
| OVERRIDECONTRACT | Optional | string | Dimension override for Contract. |
| OVERRIDEITEM | Optional | string | Dimension override for Item. |
| OVERRIDECLASS | Optional | string | Dimension override for Class. |
| OVERRIDEEMPLOYEE | Optional | string | Dimension override for Employee. |

* * *

### Update Account Allocation Definition

[History](https://developer.intacct.com/api/general-ledger/account-allocations/#history-update-account-allocation-definition)

| Release | Changes |
| --- | --- |
| 2022 Release 3 | Added "Per dimension value" allocation type for FOCUSEMPLOYEE and FOCUSPROJECT. |
| 2020 Release 3 | Added ALLOWALLOCATION, EXCH\_RATE\_TYPE\_ID |

#### `update`

> Change the account allocation such that negative basis lines are excluded:

```
<update>
    <GLACCTALLOCATION>
        <RECORDNO>46</RECORDNO>
        <GLACCTALLOCATIONBASIS>
            <SKIPNEGATIVE>true</SKIPNEGATIVE>
        </GLACCTALLOCATIONBASIS>
    </GLACCTALLOCATION>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATION | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#update-GLACCTALLOCATION) | Object to update |

Provides basic information for the allocation and specifies how dimensions are to be handled in the allocation calculations.

`GLACCTALLOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of account allocation to update. |
| DESCRIPTION | Optional | string | Description of the allocation definition |
| STATUS | Optional | boolean | Status of the allocation definition.
*   `active` (default)
*   `inactive`

 |
| METHODOLOGY | Optional | string | Description of methodology used for the allocation definition |
| ACTIVITYDELTA | Optional | string | Activity Delta.

*   `false` (default)
*   `true`: Before allocation, validate that the account setup is designed to clear the source amounts with each allocation generation. This is done by making sure that the accounts selected for your source pool are used as the reversing source pool selection, or if an alternate specific account is used for the reversal, that it's included in the source pool account group so that it removes any prior allocation activity. This option is only effective if the source account is used for the pool reversal in the allocation target, either via `GLACCOUNTNO` or `USESOURCEACCOUNT`.

 |
| ALLOWALLOCATION | Optional | string | Specifies whether to allow allocations across entities.

*   `Within one entity` (default)
*   `Across entities` When you allocate across entities, you need to specify an exchange rate type (`EXCH_RATE_TYPE_ID`) for the allocation target (`GLACCTALLOCATIONTARGET`).

 |
| FOCUSLOCATION | Optional | string | Dimensions treatment for Location. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSVENDOR | Optional | string | Dimensions treatment for Vendor. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSPROJECT | Optional | string | Dimensions treatment for Project. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.
*   `Per dimension value` - Allocate based on the value of the dimension.

 |
| FOCUSDEPARTMENT | Optional | string | Dimensions treatment for Department. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSCUSTOMER | Optional | string | Dimensions treatment for Customer. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSITEM | Optional | string | Dimensions treatment for Item. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSCLASS | Optional | string | Dimensions treatment for Class. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.

 |
| FOCUSEMPLOYEE | Optional | string | Dimensions treatment for Employee. Specifies how the dimension is used in the allocation calculation.

*   `Not considered` - (default) The dimension is not used for calculations during the generation of the allocation but can still be used as a filter to narrow the source pool or basis. You can either leave the dimension with no value in the allocated entry, or apply a single value by using the override parameters in the `GLACCTALLOCATIONTARGET`.
*   `Allocation focus` - Allocate or reclassify based on the calculation method selected in the `GLACCTALLOCATIONBASIS`.
*   `Preserve values` - Retain the original value assigned during initial entry. The dimension is included in the calculations for the source and the basis to ensure that the proportional distribution is kept when the allocated entry is recorded.
*   `Per dimension value` - Allocate based on the value of the dimension.

 |
| FOCUSWAREHOUSE | Optional | string | Dimensions treatment for Warehouse. Specifies how the dimension is used in the allocation calculation. Currently, only `Not considered` is allowed. |
| FOCUSCONTRACT | Optional | string | Dimensions treatment for Contract. Specifies how the dimension is used in the allocation calculation. Currently, only `Not considered` is allowed. |
| GLACCTALLOCATIONSOURCE | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#update-GLACCTALLOCATIONSOURCE) | Source pool for the allocation |
| GLACCTALLOCATIONBASIS | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#update-GLACCTALLOCATIONBASIS) | Basis information that specifies how the allocation splits source amounts into each target |
| GLACCTALLOCATIONTARGET | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#update-GLACCTALLOCATIONTARGET) | Target entry that specifies where the allocation will be recorded. The debit and credit accounts selected depend on your allocation setup. For example, expense allocations typically have the allocation as a debit. |
| GLACCTALLOCATIONREVERSE | Required | [object](https://developer.intacct.com/api/general-ledger/account-allocations/#update-GLACCTALLOCATIONREVERSE) | Reversing source pool |

`GLACCTALLOCATION.GLACCTALLOCATIONSOURCE`

If choosing dimensions for filtering from the source pool, remember your choices for dimension treatment. For example, if you specified that the Vendor dimension should not be considered, choosing a Vendor ID for the source does not impact the allocation calculations.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTGRP | Optional | string | Account group for the source of the allocation. To use a single account, provide an account group with one account. |
| PERCENT2ALLOCATE | Optional | string | Percentage to allocate. |
| REPORTINGBOOK | Optional | string | Reporting Book. Set this to `ACCRUAL`. |
| GLACCTALLOCATIONSOURCEADJBOOKS | Optional | array of [GLACCTALLOCATIONSOURCEADJBOOK](https://developer.intacct.com/api/general-ledger/account-allocations/#update-GLACCTALLOCATIONSOURCEADJBOOK) | Alternate Book selections |
| SOURCEINCLUDEREPORTINGBOOK | Optional | string | Use entries from.
*   `Main reporting book and alternate books` (default)
*   `Alternate books only`

 |
| TIMEPERIOD | Required | string | Source pool time period.

*   `Current Month`
*   `Prior Month`
*   `Current Quarter`
*   `Prior Quarter`
*   `Current Year`
*   `Current Year To Date`
*   `Prior Year`
*   `Prior Year Current Month`
*   `Prior Year Current Quarter`
*   `Fiscal - Current Quarter`
*   `Fiscal - Prior Quarter`
*   `Fiscal - Current Year`
*   `Fiscal - Current Year To Date`
*   `Fiscal - Prior Year`
*   `Inception To Date`

(applies only for Project dimension allocation focus). |
| LOCNO | Optional | string | Entity/Location for dimension filtering from the source pool |
| VENDORID | Optional | string | Vendor for dimension filtering from the source pool |
| PROJECTID | Optional | string | Project for dimension filtering from the source pool |
| DEPTNO | Optional | string | Department for dimension filtering from the source pool |
| CUSTOMERID | Optional | string | Customer for dimension filtering from the source pool |
| WAREHOUSE | Optional | string | Warehouse for dimension filtering from the source pool |
| CONTRACTID | Optional | string | Contract for dimension filtering from the source pool |
| ITEMID | Optional | string | Item for dimension filtering from the source pool |
| CLASSID | Optional | string | Class for dimension filtering from the source pool |
| EMPLOYEEID | Optional | string | Employee for dimension filtering from the source pool |

`GLACCTALLOCATION.GLACCTALLOCATIONSOURCE.GLACCTALLOCATIONSOURCEADJBOOK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ADJBOOKID | Optional | string | Book ID for the adjustment book.
*   `GAAPADJ`
*   `TAXADJ`
*   a user-defined book

 |

`GLACCTALLOCATION.GLACCTALLOCATIONBASIS`

If choosing dimensions for filtering for the basis, remember your choices for dimension treatment. For example, if you specified that the Vendor dimension should not be considered, choosing a Vendor ID for the basis does not impact the allocation calculations.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ALLOCATIONMETHOD | Required | string | Allocation method.
*   `Dynamic-relative account financial`
*   `Dynamic-relative account statistical`

 |
| GLACCTGRP | Optional | string | Account group for the basis of the allocation. To use a single account, provide an account group with one account. |
| ACCUMLUATION | Optional | string | Accumulation. Use `Activity`. |
| REPORTINGBOOK | Optional | string | Reporting Book. Set this to `ACCRUAL`. |
| GLACCTALLOCATIONBASISADJBOOKS | Optional | GLACCTALLOCATIONBASISADJBOOK\[\] | Alternate Book selections. |
| BASISINCLUDEREPORTINGBOOK | Optional | string | Use entries from.

*   `Main reporting book and alternate books` (default)
*   `Alternate books only`

 |
| TIMEPERIOD | Required | string | Basis time period. You can use the same time period as the source pool, or you can select a different time period for your basis.

*   `Current Month`
*   `Prior Month`
*   `Current Quarter`
*   `Prior Quarter`
*   `Current Year`
*   `Current Year To Date`
*   `Prior Year`
*   `Prior Year Current Month`
*   `Prior Year Current Quarter`
*   `Fiscal - Current Quarter`
*   `Fiscal - Prior Quarter`
*   `Fiscal - Current Year`
*   `Fiscal - Current Year To Date`
*   `Fiscal - Prior Year`
*   `Inception To Date`

(applies only for Project dimension allocation focus). |
| SKIPNEGATIVE | Optional | boolean | Drop negative basis lines from consideration.

*   `false` (default)
*   `true` - drop negative lines

 |
| LOCNO | Optional | string | Entity/Location for dimension filtering to narrow the scope for the basis methodology |
| VENDORID | Optional | string | Vendor for dimension filtering to narrow the scope for the basis methodology |
| PROJECTID | Optional | string | Project for dimension filtering to narrow the scope for the basis methodology |
| DEPTNO | Optional | string | Department for dimension filtering to narrow the scope for the basis methodology |
| CUSTOMERID | Optional | string | Customer for dimension filtering to narrow the scope for the basis methodology |
| WAREHOUSEID | Optional | string | Warehouse for dimension filtering to narrow the scope for the basis methodology |
| CONTRACTID | Optional | string | Contract for dimension filtering to narrow the scope for the basis methodology |
| ITEMID | Optional | string | Item for dimension filtering to narrow the scope for the basis methodology |
| CLASSID | Optional | string | Class for dimension filtering to narrow the scope for the basis methodology |
| EMPLOYEEID | Optional | string | Employee for dimension filtering to narrow the scope for the basis methodology |

`GLACCTALLOCATION.GLACCTALLOCATIONBASIS.GLACCTALLOCATIONBASISADJBOOK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ADJBOOKID | Optional | string | Book ID for the adjustment book. Use `GAAPADJ`, `TAXADJ`, or a user-defined book. |

`GLACCTALLOCATION.GLACCTALLOCATIONTARGET`

When choosing dimensions for filtering to the target, you can override dimension treatments. For example, if you specified that the Vendor dimension should not be considered, you can use the vendor override parameter to provide a vendor to be used in the allocation for the target.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCOUNTNO | Optional | string | Account that is the target destination of the allocation. |
| JOURNALSYBMOL | Optional | string | Journal for the allocation journal entries |
| EXCH\_RATE\_TYPE\_ID | Optional | string | Exchange rate type. Required if `ALLOWALLOCATION` is set to `Across entities` in the header. |
| OVERRIDELOCATION | Optional | string | Dimension override for Entity/Location. Applies only if the dimension treatment for Location is set to `Not considered`. |
| OVERRIDEVENDOR | Optional | string | Dimension override for Vendor. Applies only if the dimension treatment for Vendor is set to `Not considered`. |
| OVERRIDEPROJECT | Optional | string | Dimension override for Project. Applies only if the dimension treatment for Project is set to `Not considered`. |
| OVERRIDEDEPARTMENT | Optional | string | Dimension override for Department. Applies only if the dimension treatment for Department is set to `Not considered`. |
| OVERRIDECUSTOMER | Optional | string | Dimension override for Customer. Applies only if the dimension treatment for Customer is set to `Not considered`. |
| OVERRIDEWAREHOUSE | Optional | string | Dimension override for Warehouse. Applies only if the dimension treatment for Warehouse is set to `Not considered`. |
| OVERRIDECONTRACT | Optional | string | Dimension override for Contract. Applies only if the dimension treatment for Contract is set to `Not considered`. |
| OVERRIDEITEM | Optional | string | Dimension override for Item. Applies only if the dimension treatment for Item is set to `Not considered`. |
| BILLABLE | Optional | boolean | Specifies that lines in the allocation target are billable. Applies only if Project is part of the allocation and Project billing is enabled for General Ledger. Use `true` for billable, `false` otherwise. (Default: `false`) |
| OVERRIDECLASS | Optional | string | Dimension override for Class. Applies only if the dimension treatment for Class is set to `Not considered`. |
| OVERRIDEEMPLOYEE | Optional | string | Dimension override for Employee. Applies only if the dimension treatment for Employee is set to `Not considered`. |

`GLACCTALLOCATION.GLACCTALLOCATIONREVERSE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCOUNTNO | Optional | string | Account to use for the reversal pool for the account allocation. Required if not using the source account. |
| USESOURCEACCOUNT | Optional | boolean | Use the source account for the reversal pool for the account allocation. Required if not providing an account. |
| OVERRIDELOCATION | Optional | string | Dimension override for Entity/Location. |
| OVERRIDEVENDOR | Optional | string | Dimension override for Vendor. |
| OVERRIDEPROJECT | Optional | string | Dimension override for Project. |
| OVERRIDEDEPARTMENT | Optional | string | Dimension override for Department. |
| OVERRIDECUSTOMER | Optional | string | Dimension override for Customer. |
| OVERRIDEWAREHOUSE | Optional | string | Dimension override for Warehouse. |
| OVERRIDECONTRACT | Optional | string | Dimension override for Contract. |
| OVERRIDEITEM | Optional | string | Dimension override for Item. |
| OVERRIDECLASS | Optional | string | Dimension override for Class. |
| OVERRIDEEMPLOYEE | Optional | string | Dimension override for Employee. |

* * *

### Delete Account Allocation Definition

#### `delete`

```
<delete>
    <object>GLACCTALLOCATION</object>
    <keys>46</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATION` |
| keys | Required | string | Comma-separated list of account allocation `RECORDNO` to delete |

* * *

Account Allocation Run
----------------------

### Get Account Allocation Run Object Definition

#### `lookup`

> List all the fields and relationships for the account allocation run object:

```
<lookup>
    <object>GLACCTALLOCATIONRUN</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONRUN` |

* * *

### Query and List Account Allocation Runs

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, GL allocation, and posting date for each run:

```
<query>
    <object>GLACCTALLOCATIONRUN</object>
    <select>
        <field>RECORDNO</field>
        <field>GLACCTALLOCATION</field>
        <field>GLPOSTINGDATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONRUN` |
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

### Query and List Account Allocation Runs (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>GLACCTALLOCATIONRUN</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONRUN` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | State of the allocation run. Use `Q` for in queue, `I` for in progress, `F` for failed, or `P` for passed. |

* * *

### Get Account Allocation Run

#### `read`

```
<read>
    <object>GLACCTALLOCATIONRUN</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONRUN` |
| keys | Required | string | Comma-separated list of account allocation run `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

### Create Account Allocation Run

#### `create`

```
<create>
    <GLACCTALLOCATIONRUN>
        <GLACCTALLOCATION>Monthly expenses</GLACCTALLOCATION>
        <ASOFDATE>2018-09-01/</ASOFDATE>
        <GLPOSTINGDATE>2018-09-25</GLPOSTINGDATE>
        <EMAIL>myEmailAddress.com</EMAIL>
    </GLACCTALLOCATIONRUN>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATIONRUN | Required | object | Object to create |

`GLACCTALLOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATION | Optional | string | Account allocation ID. Required if not providing an account allocation group. |
| GLACCTALLOCATIONGRP | Optional | string | Account allocation group name. Required if not providing an account allocation ID. |
| ASOFDATE | Required | string | As of date for processing the account allocation |
| GLPOSTINGDATE | Required | string | GL posting date |
| EMAIL | Required | string | Your email address |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

