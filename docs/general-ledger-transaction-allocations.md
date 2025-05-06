Title: Transaction Allocations

URL Source: https://developer.intacct.com/api/general-ledger/transaction-allocations/

Markdown Content:
*   [Transaction Allocations](https://developer.intacct.com/api/general-ledger/transaction-allocations/#transaction-allocations)
    *   [Get Transaction Allocation Object Definition](https://developer.intacct.com/api/general-ledger/transaction-allocations/#get-transaction-allocation-object-definition)
    *   [Query and List Transaction Allocations](https://developer.intacct.com/api/general-ledger/transaction-allocations/#query-and-list-transaction-allocations)
    *   [Query and List Transaction Allocations (Legacy)](https://developer.intacct.com/api/general-ledger/transaction-allocations/#query-and-list-transaction-allocations-legacy)
    *   [Get Transaction Allocation](https://developer.intacct.com/api/general-ledger/transaction-allocations/#get-transaction-allocation)
    *   [Get Transaction Allocation by ID](https://developer.intacct.com/api/general-ledger/transaction-allocations/#get-transaction-allocation-by-id)
    *   [Create Transaction Allocation](https://developer.intacct.com/api/general-ledger/transaction-allocations/#create-transaction-allocation)
    *   [Update Transaction Allocation](https://developer.intacct.com/api/general-ledger/transaction-allocations/#update-transaction-allocation)
    *   [Delete Transaction Allocation](https://developer.intacct.com/api/general-ledger/transaction-allocations/#delete-transaction-allocation)
*   [Transaction Allocation Lines](https://developer.intacct.com/api/general-ledger/transaction-allocations/#transaction-allocation-lines)
    *   [Get Transaction Allocation Line Object Definition](https://developer.intacct.com/api/general-ledger/transaction-allocations/#get-transaction-allocation-line-object-definition)
    *   [Query and List Allocation Lines](https://developer.intacct.com/api/general-ledger/transaction-allocations/#query-and-list-allocation-lines)
    *   [Query and List Allocation Lines (Legacy)](https://developer.intacct.com/api/general-ledger/transaction-allocations/#query-and-list-allocation-lines-legacy)
    *   [Get Allocation Line](https://developer.intacct.com/api/general-ledger/transaction-allocations/#get-allocation-line)

* * *

Transaction allocations enable you to distribute transaction amounts across multiple dimensions such as departments, locations, projects, or classes.

Transaction allocations are intended for use on single line items, allowing you to distribute amounts during entry of a transaction, usually a one-time action. Transaction allocations are only available for distribution across eight of the ten standard dimensions and have other restrictions as well.

If you want to automatically pull updated source balances and distribute them across dimensions according to defined basis calculations, you should use the Dynamic Allocations subscription. See [Account Allocations](https://developer.intacct.com/api/general-ledger/account-allocations/) for more info.

* * *

### Get Transaction Allocation Object Definition

#### `lookup`

> List all the fields and relationships for the transaction allocation object:

```
<lookup>
    <object>ALLOCATION</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATION` |

* * *

### Query and List Transaction Allocations

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, description, and status for each transaction allocation:

```
<query>
    <object>ALLOCATION</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
        <field>STATUS</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATION` |
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

### Query and List Transaction Allocations (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ALLOCATION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Transaction Allocation

#### `read`

```
<read>
    <object>ALLOCATION</object>
    <keys>31</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATION` |
| keys | Required | string | Comma-separated list of transaction allocation `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Transaction Allocation by ID

#### `readByName`

```
<readByName>
    <object>ALLOCATION</object>
    <keys>TEST</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATION` |
| keys | Required | string | Comma-separated list of transaction allocation `ALLOCATIONID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Transaction Allocation

[History](https://developer.intacct.com/api/general-ledger/transaction-allocations/#history-create-transaction-allocation)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | Added Fixed amount with over/under logic for TYPE, added VALUETYPE |

#### `create`

> Allocates expenses for locations using percentages:

```
<create>
    <ALLOCATION>
        <ALLOCATIONID>ExpenseSwap</ALLOCATIONID>
        <DESCRIPTION></DESCRIPTION>
        <STATUS>active</STATUS>
        <TYPE>Percentage</TYPE>
        <DOCNUMBER></DOCNUMBER>
        <SUPDOCID></SUPDOCID>
        <ALLOCATIONENTRIES>
            <ALLOCATIONENTRY>
                <VALUE>40</VALUE>
                <LOCATIONID>5000</LOCATIONID>
                <DEPARTMENTID></DEPARTMENTID>
                <PROJECTID></PROJECTID>
                <CUSTOMERID></CUSTOMERID>
                <VENDORID></VENDORID>
                <EMPLOYEEID></EMPLOYEEID>
                <ITEMID></ITEMID>
                <CLASSID></CLASSID>
                <CONTRACTID></CONTRACTID>
                <WAREHOUSEID></WAREHOUSEID>
            </ALLOCATIONENTRY>
            <ALLOCATIONENTRY>
                <VALUE>60</VALUE>
                <LOCATIONID>2000</LOCATIONID>
                <DEPARTMENTID></DEPARTMENTID>
                <PROJECTID></PROJECTID>
                <CUSTOMERID></CUSTOMERID>
                <VENDORID></VENDORID>
                <EMPLOYEEID></EMPLOYEEID>
                <ITEMID></ITEMID>
                <CLASSID></CLASSID>
                <CONTRACTID></CONTRACTID>
                <WAREHOUSEID></WAREHOUSEID>
            </ALLOCATIONENTRY>
        </ALLOCATIONENTRIES>
    </ALLOCATION>
</create>
```

> Allocates expenses for departments using amounts and percentages:

```
<create>
    <ALLOCATION>
        <ALLOCATIONID>ExpenseAllocByDept</ALLOCATIONID>
        <DESCRIPTION/>
        <STATUS>active</STATUS>
        <TYPE>Fixed amount with over/under logic</TYPE>
        <DOCNUMBER/>
        <SUPDOCID/>
        <ALLOCATIONENTRIES>
            <ALLOCATIONENTRY>
                <VALUETYPE>Amount</VALUETYPE>
                <VALUE>500</VALUE>
                <DEPARTMENTID>01</DEPARTMENTID>
            </ALLOCATIONENTRY>
            <ALLOCATIONENTRY>
                <VALUETYPE>Percent</VALUETYPE>
                <VALUE>40</VALUE>
                <DEPARTMENTID>02</DEPARTMENTID>
            </ALLOCATIONENTRY>
            <ALLOCATIONENTRY>
                <VALUETYPE>Percent</VALUETYPE>
                <VALUE>60</VALUE>
                <DEPARTMENTID>03</DEPARTMENTID>
            </ALLOCATIONENTRY>
        </ALLOCATIONENTRIES>
    </ALLOCATION>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ALLOCATION | Optional | object | Object to create |

`ALLOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ALLOCATIONID | Required | string | Transaction allocation ID |
| DESCRIPTION | Optional | string | Description of transaction allocation |
| STATUS | Optional | string | Transaction allocation status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| TYPE | Optional | string | How the transaction allocation is split across dimensions.
*   Use `Percentage` to specify entries as percentages (default).
*   Use `Absolute` to specify entries as fixed amounts.
*   Use `Fixed amount with over/under logic` for a combination of both. Exact amounts are distributed first, in the order they occur in the transaction allocation definition. Any remaining amount is distributed using the percentage allocations. Entries for exact amounts must come before entries for percentages, and percentages must always total 100%. (Use the `VALUETYPE` parameter on each entry to specify amount or percent.)

 |
| DOCNUMBER | Optional | string | Document number |
| ALLOCATIONENTRIES | Required | `ALLOCATIONENTRY[1...n]` | Transaction allocation entries must add up to 100 if `TYPE` is `Percentage` or `Fixed amount with over/under logic`. |

`ALLOCATIONENTRY`

| Name | Required | Type | Description |   |
| --- | --- | --- | --- | --- |
| VALUETYPE | Optional | decimal | Value type, either `Amount` or `Percent`. This parameter is required if allocation `TYPE` is set to `Fixed amount with over/under logic`. If `TYPE` is set to `Percentage` or `Absolute`, `VALUETYPE` defaults to the correct value and can be omitted. |   |
| VALUE | Required | decimal | Value to allocate by |   |
| DEPARTMENTID | Optional | string | Department ID |   |
| LOCATIONID | Optional | string. |   | Location ID. Required if company is multi-entity enabled. |
| PROJECTID | Optional | string | Project ID |   |
| CUSTOMERID | Optional | string | Customer ID |   |
| VENDORID | Optional | string | Vendor ID |   |
| EMPLOYEEID | Optional | string | Employee ID |   |
| ITEMID | Optional | string | Item ID |   |
| CLASSID | Optional | string | Class ID |   |
| CONTRACTID | Optional | string | Contract ID |   |
| WAREHOUSEID | Optional | string | Warehouse ID |   |
| LINE\_NO | Optional | integer | Line number |   |

* * *

### Update Transaction Allocation

[History](https://developer.intacct.com/api/general-ledger/transaction-allocations/#history-update-transaction-allocation)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | Added Fixed amount with over/under logic for TYPE, added VALUETYPE |

#### `update`

```
<update>
    <ALLOCATION>
        <RECORDNO>7</RECORDNO>
        <DESCRIPTION></DESCRIPTION>
        <STATUS>active</STATUS>
        <TYPE>Percentage</TYPE>
        <DOCNUMBER></DOCNUMBER>
        <SUPDOCID></SUPDOCID>
        <ALLOCATIONENTRIES>
            <ALLOCATIONENTRY>
                <VALUE>40</VALUE>
                <LOCATIONID>5000</LOCATIONID>
                <DEPARTMENTID></DEPARTMENTID>
                <PROJECTID></PROJECTID>
                <CUSTOMERID></CUSTOMERID>
                <VENDORID></VENDORID>
                <EMPLOYEEID></EMPLOYEEID>
                <ITEMID></ITEMID>
                <CLASSID></CLASSID>
                <CONTRACTID></CONTRACTID>
                <WAREHOUSEID></WAREHOUSEID>
            </ALLOCATIONENTRY>
            <ALLOCATIONENTRY>
                <VALUE>60</VALUE>
                <LOCATIONID>2000</LOCATIONID>
                <DEPARTMENTID></DEPARTMENTID>
                <PROJECTID></PROJECTID>
                <CUSTOMERID></CUSTOMERID>
                <VENDORID></VENDORID>
                <EMPLOYEEID></EMPLOYEEID>
                <ITEMID></ITEMID>
                <CLASSID></CLASSID>
                <CONTRACTID></CONTRACTID>
                <WAREHOUSEID></WAREHOUSEID>
            </ALLOCATIONENTRY>
        </ALLOCATIONENTRIES>
    </ALLOCATION>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ALLOCATION | Optional | object | Object to update |

`ALLOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of transaction allocation to update. Required if not using `ALLOCATIONID`. |
| ALLOCATIONID | Optional | string | Transaction allocation ID. Required if not using `RECORDNO`. |
| DESCRIPTION | Optional | string | Description of transaction allocation |
| STATUS | Optional | string | Transaction allocation status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| TYPE | Optional | string | How the transaction allocation is split across dimensions.
*   Use `Percentage` to specify entries as percentages (default).
*   Use `Absolute` to specify entries as fixed amounts.
*   Use `Fixed amount with over/under logic` for a combination of both. Exact amounts are distributed first, in the order they occur in the transaction allocation definition. Any remaining amount is distributed using the percentage allocations. Entries for exact amounts must come before entries for percentages, and percentages must always total 100%. (Use the `VALUETYPE` parameter on each entry to specify amount or percent.)

 |
| DOCNUMBER | Optional | string | Document number |
| SUPDOCID | Optional | string | Attachments ID |
| ALLOCATIONENTRIES | Required | `ALLOCATIONENTRY[1...n]` | Transaction allocation entries must add up to 100 if `TYPE` is `Percentage` |

`ALLOCATIONENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VALUETYPE | Optional | decimal | Value type, either `Amount` or `Percent`. This parameter is required if allocation `TYPE` is set to `Fixed amount with over/under logic`. If `TYPE` is set to `Percentage` or `Absolute`, `VALUETYPE` defaults to the correct value and can be omitted. |
| VALUE | Required | decimal | Value to allocate by |
| DEPARTMENTID | Optional | string | Department ID |
| Optional | string | `LOCATIONID` of an active [location](https://developer.intacct.com/api/company-console/locations/). Required if company is multi-entity enabled. |   |
| PROJECTID | Optional | string | Project ID |
| CUSTOMERID | Optional | string | Customer ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| ITEMID | Optional | string | Item ID |
| CLASSID | Optional | string | Class ID |
| CONTRACTID | Optional | string | Contract ID |
| WAREHOUSEID | Optional | string | Warehouse ID |

* * *

### Delete Transaction Allocation

#### `delete`

```
<delete>
    <object>ALLOCATION</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATION` |
| keys | Required | string | Comma-separated list of transaction allocation `RECORDNO` to delete |

* * *

Transaction Allocation Lines
----------------------------

### Get Transaction Allocation Line Object Definition

#### `lookup`

> List all the fields and relationships for the transaction allocation line object:

```
<lookup>
    <object>ALLOCATIONENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATIONENTRY` |

* * *

### Query and List Allocation Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, value, and the record number of the owning allocation for each entry:

```
<query>
    <object>ALLOCATIONENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>VALUE</field>
        <field>ALLOCATIONKEY</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATIONENTRY` |
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

### Query and List Allocation Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ALLOCATIONENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATIONENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Allocation Line

#### `read`

```
<read>
    <object>ALLOCATIONENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ALLOCATIONENTRY` |
| keys | Required | string | Comma-separated list of transaction allocation line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

