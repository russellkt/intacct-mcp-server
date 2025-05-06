Title: Inventory Transactions

URL Source: https://developer.intacct.com/api/inventory-control/inventory-transactions/

Markdown Content:
*   [Inventory Transactions](https://developer.intacct.com/api/inventory-control/inventory-transactions/#inventory-transactions)
    *   [Get Inventory Transaction Object Definition](https://developer.intacct.com/api/inventory-control/inventory-transactions/#get-inventory-transaction-object-definition)
    *   [Query and List Inventory Transactions](https://developer.intacct.com/api/inventory-control/inventory-transactions/#query-and-list-inventory-transactions)
    *   [Query and List Inventory Transactions (Legacy)](https://developer.intacct.com/api/inventory-control/inventory-transactions/#query-and-list-inventory-transactions-legacy)
    *   [Get an Inventory Transaction](https://developer.intacct.com/api/inventory-control/inventory-transactions/#get-an-inventory-transaction)
    *   [Create an Inventory Transaction (Legacy)](https://developer.intacct.com/api/inventory-control/inventory-transactions/#create-an-inventory-transaction-legacy)
    *   [Update an Inventory Transaction (Legacy)](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update-an-inventory-transaction-legacy)
    *   [Delete an Inventory Transaction](https://developer.intacct.com/api/inventory-control/inventory-transactions/#delete-an-inventory-transaction)
    *   [Delete an Inventory Transaction (Legacy)](https://developer.intacct.com/api/inventory-control/inventory-transactions/#delete-an-inventory-transaction-legacy)
*   [Inventory Transaction Lines](https://developer.intacct.com/api/inventory-control/inventory-transactions/#inventory-transaction-lines)
    *   [Get Inventory Transaction Line Object Definition](https://developer.intacct.com/api/inventory-control/inventory-transactions/#get-inventory-transaction-line-object-definition)
    *   [Query and List Inventory Transaction Lines](https://developer.intacct.com/api/inventory-control/inventory-transactions/#query-and-list-inventory-transaction-lines)
    *   [Query and List Inventory Transaction Lines (Legacy)](https://developer.intacct.com/api/inventory-control/inventory-transactions/#query-and-list-inventory-transaction-lines-legacy)
    *   [Get an Inventory Transaction Line](https://developer.intacct.com/api/inventory-control/inventory-transactions/#get-an-inventory-transaction-line)
*   [Inventory Transaction Subtotals](https://developer.intacct.com/api/inventory-control/inventory-transactions/#inventory-transaction-subtotals)
    *   [Get Inventory Transaction Subtotal Object Definition](https://developer.intacct.com/api/inventory-control/inventory-transactions/#get-inventory-transaction-subtotal-object-definition)
    *   [Query and List Inventory Transaction Subtotals](https://developer.intacct.com/api/inventory-control/inventory-transactions/#query-and-list-inventory-transaction-subtotals)
    *   [Query and List Inventory Transaction Subtotals (Legacy)](https://developer.intacct.com/api/inventory-control/inventory-transactions/#query-and-list-inventory-transaction-subtotals-legacy)
    *   [Get an Inventory Transaction Subtotal](https://developer.intacct.com/api/inventory-control/inventory-transactions/#get-an-inventory-transaction-subtotal)

* * *

An inventory transaction is usually a transfer or an adjustment.

* * *

### Get Inventory Transaction Object Definition

#### `lookup`

> List all the fields and relationships for the inventory transaction object:

```
<lookup>
    <object>INVDOCUMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENT` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Inventory Transactions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> Lists information for each inventory transaction with the given document type:

```
<query>
    <object>INVDOCUMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
        <field>TOTAL</field>
    </select>
    <docparid>Beginning Balance</docparid>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENT` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Inventory Transactions (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>INVDOCUMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Beginning Balance</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get an Inventory Transaction

#### `read`

```
<read>
    <object>INVDOCUMENT</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Beginning Balance</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENT` |
| keys | Required | string | Comma-separated list of transaction `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Create an Inventory Transaction (Legacy)

[History](https://developer.intacct.com/api/inventory-control/inventory-transactions/#history-create-inventory-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | itemdetails now supports trackable kit item types |
| 2020 Release 2 | Added costtypeid |
| 2020 Release 1 | Added adjdocentrykey |
| 2019 Release 4 | Added taskid |

#### `create_ictransaction`

```
<create_ictransaction>
    <transactiontype>Inventory Transfer</transactiontype>
    <datecreated>
        <year>2013</year>
        <month>5</month>
        <day>28</day>
    </datecreated>
    <createdfrom></createdfrom>
    <documentno></documentno>
    <referenceno></referenceno>
    <message></message>
    <basecurr>USD</basecurr>
    <state>Pending</state>
    <ictransitems>
        <ictransitem>
            <itemid>I123</itemid>
            <itemdesc></itemdesc>
            <warehouseid>W100</warehouseid>
            <quantity>10</quantity>
            <unit>Each</unit>
            <cost>49.99</cost>
            <locationid>L200</locationid>
            <departmentid>D20</departmentid>
            <projectid></projectid>
            <customerid></customerid>
            <vendorid></vendorid>
            <employeeid></employeeid>
            <classid></classid>
            <contractid></contractid>
        </ictransitem>
    </ictransitems>
</create_ictransaction>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| transactiontype | Required | string | [Transaction definition](https://developer.intacct.com/api/inventory-control/inventory-transaction-definitions/) to use. |
| datecreated | Required | object | Transaction date |
| createdfrom | Optional | string | Inventory transaction document number to convert from. |
| documentno | Optional | string | Document number. Leave blank to use auto numbering if set in transaction definition. |
| referenceno | Optional | string | Reference number |
| message | Optional | string | Message |
| externalid | Optional | string | External ID |
| basecurr | Optional | string | Base currency code |
| customfields | Optional | array of `customfield` | Custom fields |
| state | Optional | string | Action.
*   `Draft`
*   `Pending`
*   `Closed`

(Default depends on transaction definition configuration) |
| ictransitems | Required | array of [`ictransitem`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#create_ictransaction-ictransitems.ictransitem) | Transaction lines, must have at least 1. |
| subtotals | Optional | array of [`subtotal`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#create_ictransaction-subtotals.subtotal) | Subtotal lines |

`datecreated`

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

`create_ictransaction.ictransitems.ictransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | `ITEMID` of the [item](https://developer.intacct.com/api/inventory-control/items/). |
| itemdesc | Optional | string | Item description |
| warehouseid | Required | string | `WAREHOUSEID` of the [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure to base quantity off |
| cost | Optional | currency | Cost |
| sourcelinekey | Optional | integer | Source line to convert this line from. Use the `RECORDNO` of the line from the `createdfrom` transaction document. |
| itemdetails | Optional | array of [`itemdetail`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#create_ictransaction-ictransitems.ictransitem.itemdetail) | Item details pertaining to inventory tracking (applicable to inventory or stockable kit item types). |
| classid | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| contractid | Optional | string | `CONTRACTID` of a [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) |
| costtypeid | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| departmentid | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/). |
| employeeid | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| locationid | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/). |
| adjdocentrykey | Optional | string | Record number of the source transaction line this inventory adjustment will affect. The item in the source transaction line must match the `itemid` for the `ictransitem`. |
| projectid | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| taskid | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). Only available when the parent `projectid` is also specified. |
| vendorid | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| customfields | Optional | array of `customfield` | Custom fields |

`create_ictransaction.ictransitems.ictransitem.itemdetail`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| quantity | Optional | number | Quantity |
| serialno | Optional | string | Serial number |
| lotno | Optional | string | Lot number |
| aisle | Optional | string | Aisle |
| row | Optional | string | Row |
| bin | Optional | string | Bin |
| itemexpiration | Optional | [object](https://developer.intacct.com/api/inventory-control/inventory-transactions/#create_ictransaction-ictransitems.ictransitem.itemdetail.itemexpiration) | Item expiration date |

`create_ictransaction-ictransitems.ictransitem.itemdetail.itemexpiration`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`create_ictransaction.subtotals.subtotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| description | Required | string | Description |
| total | Required | currency | Total |
| absval | Optional | number | Absolute value |
| percentval | Optional | number | Percent value |
| classid | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| contractid | Optional | string | `CONTRACTID` of a [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) |
| costtypeid | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| departmentid | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/). |
| employeeid | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| itemid | Optional | string | `ITEMID` of the [item](https://developer.intacct.com/api/inventory-control/items/) |
| locationid | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/). |
| projectid | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| taskid | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). Only available when the parent `projectid` is also specified. |
| vendorid | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| customfields | Optional | array of `customfield` | Custom fields |

* * *

### Update an Inventory Transaction (Legacy)

[History](https://developer.intacct.com/api/inventory-control/inventory-transactions/#history-update-inventory-transaction-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | itemdetails now supports trackable kit item types |
| 2020 Release 2 | Added costtypeid |
| 2019 Release 4 | Added taskid |

Before using this function to modify existing lines, make sure you know the correct line numbers. For this object, the generic `read` function uses a zero-based index for entries returned in the response. However, the object-specific update function uses a one-based index for entries you supply in the request.

After using `read` to get the line number of the entry you want to modify, add one to that number to specify the correct line in your update operation. See [Working with transaction lines and legacy functions](https://developer.intacct.com/web-services/functions/#working-with-transaction-lines-and-legacy-functions) for more information.

**Warning:** Before doing any large scale update operations, perform a test to make sure you are modifying the correct lines.

#### `update_ictransaction`

```
<update_ictransaction key="Beginning Balance-BB1234">
    <updateictransitems>
        <updateictransitem line_num="1">
            <itemdesc>Components for sensors</itemdesc>
        </updateictransitem>
    </updateictransitems>
</update_ictransaction>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Document ID to update |
| datecreated | Optional | [object](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update_ictransaction-datecreated) | Transaction date |
| referenceno | Optional | string | Reference number |
| message | Optional | string | Message |
| externalid | Optional | string | External ID |
| state | Optional | string | Action.
*   `Draft`
*   `Pending`
*   `Closed`

(Default depends on transaction definition configuration) |
| updateictransitems | Required | array of [`updateictransitem`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update_ictransaction.updateictransitems.updateictransitem) or [`ictransitem`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update_ictransaction.updateictransitems.ictransitem) | You can mix types in the array.

*   `updateictransitem` - Update an existing line
*   `ictransitem` - Create a new line

 |
| updatesubtotals | Optional | array of [`updatesubtotal`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update_ictransaction-updatesubtotals.subtotal) | Subtotal lines |
| customfields | Optional | array of `customfield` | Custom fields |

`update_ictransaction.datecreated`

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

`update_ictransaction.updatetransitems.updateictransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| line\_num | Required | integer | Line number to update |
| itemid | Required | string | `ITEMID` of the [item](https://developer.intacct.com/api/inventory-control/items/). |
| itemdesc | Optional | string | Item description |
| warehouseid | Required | string | `WAREHOUSEID` of the [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure to base quantity off |
| cost | Optional | currency | Cost |
| itemdetails | Optional | array of [`itemdetail`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update_ictransaction-updateictransitems.ictransitem.itemdetail) | Item details pertaining to inventory tracking (applicable to inventory or stockable kit item types). |
| classid | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| contractid | Optional | string | `CONTRACTID` of a [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) |
| costtypeid | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| departmentid | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/). |
| employeeid | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| locationid | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/). |
| projectid | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| taskid | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). Only available when the parent `projectid` is also specified. |
| vendorid | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| customfields | Optional | array of `customfield` | Custom fields |

`update_ictransaction.updateictransitems.ictransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | `ITEMID` of the [item](https://developer.intacct.com/api/inventory-control/items/). |
| itemdesc | Optional | string | Item description |
| warehouseid | Required | string | `WAREHOUSEID` of the [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |
| quantity | Required | number | Quantity |
| unit | Optional | string | Unit of measure to base quantity off |
| cost | Optional | currency | Cost |
| sourcelinekey | Optional | integer | Source line to convert this line from. Use the `RECORDNO` of the line from the `createdfrom` transaction document. |
| itemdetails | Optional | array of [`itemdetail`](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update_ictransaction-updateictransitems.ictransitem.itemdetail) | Item details pertaining to inventory tracking (applicable to inventory or stockable kit item types). |
| classid | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| contractid | Optional | string | `CONTRACTID` of a [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) |
| costtypeid | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| departmentid | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/). |
| employeeid | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| locationid | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/). |
| projectid | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| taskid | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). Only available when the parent `projectid` is also specified. |
| vendorid | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| customfields | Optional | array of `customfield` | Custom fields |

`update_ictransaction-updateictransitems.updateictransitems.itemdetail`  
`update_ictransaction-updateictransitems.ictransitem.itemdetail`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| quantity | Optional | number | Quantity |
| serialno | Optional | string | Serial number |
| lotno | Optional | string | Lot number |
| aisle | Optional | string | Aisle |
| row | Optional | string | Row |
| bin | Optional | string | Bin |
| itemexpiration | Optional | [object](https://developer.intacct.com/api/inventory-control/inventory-transactions/#update_ictransaction-updateictransitems.ictransitem.itemdetail.itemexpiration) | Item expiration |

`update_ictransaction-updateictransitems.updateictransitems.itemdetail.itemexpiration`  
`update_ictransaction-updateictransitems.ictransitem.itemdetail.itemexpiration`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`update_ictransaction.updatesubtotals.updatesutbotal`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| description | Required | string | Description |
| total | Required | currency | Total |
| absval | Optional | number | Absolute value |
| percentval | Optional | number | Percent value |
| classid | Optional | string | `CLASSID` of a [class](https://developer.intacct.com/api/company-console/classes/). |
| contractid | Optional | string | `CONTRACTID` of a [contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/) |
| costtypeid | Optional | string | `COSTTYPEID` of a [cost type](https://developer.intacct.com/api/construction/cost-types/). Only available when `projectid` and `taskid` are specified. (Construction subscription) |
| customerid | Optional | string | `CUSTOMERID` of a [customer](https://developer.intacct.com/api/accounts-receivable/customers/). |
| departmentid | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/). |
| employeeid | Optional | string | `EMMPLOYEEID` of an [employee](https://developer.intacct.com/api/employee-expenses/employees/). |
| itemid | Optional | string | `ITEMID` of the [item](https://developer.intacct.com/api/inventory-control/items/) |
| locationid | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/). |
| projectid | Optional | string | `PROJECTID` of the related [project](https://developer.intacct.com/api/project-resource-mgmt/projects/). |
| taskid | Optional | string | `TASKID` of a [task](https://developer.intacct.com/api/project-resource-mgmt/tasks/). Only available when the parent `projectid` is also specified. |
| vendorid | Optional | string | `VENDORID` of a [vendor](https://developer.intacct.com/api/accounts-payable/vendors/). |
| customfields | Optional | array of `customfield` | Custom fields |

* * *

### Delete an Inventory Transaction

#### `delete`

```
<delete>
    <object>INVDOCUMENT</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENT` |
| keys | Required | string | Comma-separated list of transaction `RECORDNO` to delete |

* * *

### Delete an Inventory Transaction (Legacy)

#### `delete_ictransaction`

```
<delete_ictransaction key="Beginning Balance-BB1234"></delete_ictransaction>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Transaction `DOCID` to delete |

* * *

Inventory Transaction Lines
---------------------------

### Get Inventory Transaction Line Object Definition

#### `lookup`

> List all the fields and relationships for the inventory transaction line object:

```
<lookup>
    <object>INVDOCUMENTENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTENTRY` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Inventory Transaction Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> Lists information for each inventory transaction line with the given document type:

```
<query>
    <object>INVDOCUMENTENTRY</object>
    <select>
        <field>DOCHDRNO</field>
        <field>LINE_NO</field>
        <field>ITEMID</field>
        <field>PRICE</field>
    </select>
    <docparid>Beginning Balance</docparid>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTENTRY` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Inventory Transaction Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>INVDOCUMENTENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Beginning Balance</docparid>
</readByQuery>
```

> Query for lines that are inventory adjustments:

```
<readByQuery>
    <object>INVDOCUMENTENTRY</object>
    <fields>*</fields>
    <query>ADJDOCENTRYKEY IS NOT NULL</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get an Inventory Transaction Line

#### `read`

```
<read>
    <object>INVDOCUMENTENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Beginning Balance</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTENTRY` |
| keys | Required | string | Comma-separated list of transaction line `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

Inventory Transaction Subtotals
-------------------------------

### Get Inventory Transaction Subtotal Object Definition

#### `lookup`

> List all the fields and relationships for the inventory transaction subtotal object:

```
<lookup>
    <object>INVDOCUMENTSUBTOTALS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTSUBTOTALS` |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Inventory Transaction Subtotals

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List information about each inventory transaction subtotal with the given document type :

```
<query>
    <object>INVDOCUMENTSUBTOTALS</object>
    <select>
        <field>ITEMID</field>
        <field>LOCATION</field>
        <field>TOTAL</field>
        <field>DESCRIPTION</field>
    </select>
    <docparid>Beginning Balance</docparid>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTSUBTOTALS` |
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
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Query and List Inventory Transaction Subtotals (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>INVDOCUMENTSUBTOTALS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
    <docparid>Beginning Balance</docparid>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTSUBTOTALS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

### Get an Inventory Transaction Subtotal

#### `read`

```
<read>
    <object>INVDOCUMENTSUBTOTALS</object>
    <keys>1</keys>
    <fields>*</fields>
    <docparid>Beginning Balance</docparid>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `INVDOCUMENTSUBTOTALS` |
| keys | Required | string | Comma-separated list of transaction subtotal `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used to indicate the document type (Ex: `Inventory Transfer`). You must use this to take advantage of any custom fields on the specified document type. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

