Title: Inventory Cycle Counts

URL Source: https://developer.intacct.com/api/inventory-control/cycle-counts/

Markdown Content:
*   [Inventory Cycle Counts](https://developer.intacct.com/api/inventory-control/cycle-counts/#inventory-cycle-counts)
    *   [Get Cycle Count Object Definition](https://developer.intacct.com/api/inventory-control/cycle-counts/#get-cycle-count-object-definition)
    *   [Query and List Cycle Counts](https://developer.intacct.com/api/inventory-control/cycle-counts/#query-and-list-cycle-counts)
    *   [Query and List Cycle Counts (Legacy)](https://developer.intacct.com/api/inventory-control/cycle-counts/#query-and-list-cycle-counts-legacy)
    *   [Get a Cycle Count](https://developer.intacct.com/api/inventory-control/cycle-counts/#get-a-cycle-count)
    *   [Create a Cycle Count](https://developer.intacct.com/api/inventory-control/cycle-counts/#create-a-cycle-count)
    *   [Delete a Cycle Count](https://developer.intacct.com/api/inventory-control/cycle-counts/#delete-a-cycle-count)
*   [Inventory Cycle Count Lines](https://developer.intacct.com/api/inventory-control/cycle-counts/#inventory-cycle-count-lines)
    *   [Get Inventory Cycle Count Entry Object Definition](https://developer.intacct.com/api/inventory-control/cycle-counts/#get-inventory-cycle-count-entry-object-definition)
    *   [Query and List Cycle Count Lines](https://developer.intacct.com/api/inventory-control/cycle-counts/#query-and-list-cycle-count-lines)
    *   [Query and List Inventory Cycle Count Lines (Legacy)](https://developer.intacct.com/api/inventory-control/cycle-counts/#query-and-list-inventory-cycle-count-lines-legacy)
    *   [Get Inventory Cycle Count Lines](https://developer.intacct.com/api/inventory-control/cycle-counts/#get-inventory-cycle-count-lines)
    *   [Create a Cycle Count Line](https://developer.intacct.com/api/inventory-control/cycle-counts/#create-a-cycle-count-line)
    *   [Update a Cycle Count Line](https://developer.intacct.com/api/inventory-control/cycle-counts/#update-a-cycle-count-line)
    *   [Delete a Cycle Count Line](https://developer.intacct.com/api/inventory-control/cycle-counts/#delete-a-cycle-count-line)

* * *

Cycle counting is an inventory auditing procedure in which a small amount of inventory is regularly counted in the warehouse. The general goal is to count the entire inventory over a period of time and update the inventory at the end of each count.

* * *

An `ICCYCLECOUNT` object contains high-level information about a cycle count, such as the warehouse where it’s being conducted and the employee that will count the inventory. `ICYCLECOUNTENTRY` objects represent items in a count and contain a `CYCLECOUNTKEY` field that links them to specific cycle counts.

The `COUNTSTATE` of an `ICCYCLECOUNT` object shows the state of the inventory count, including `Not Started`, `In Progress`, `Counted`, `Reconciled`, and `Voided`. Once an `ICCYCLECOUNT` object is created (`COUNTSTATE` = `Not Started`), the `COUNTSTATE` is updated by the system as users work with Cycle Counts in the Intacct UI. You cannot update an `ICCYCLECOUNT` object via the API.

### Get Cycle Count Object Definition

#### `lookup`

> List all the fields and relationships for the inventory control cycle count object:

```
<lookup>
    <object>ICCYCLECOUNT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNT` |

* * *

### Query and List Cycle Counts

#### [`query`](https://developer.intacct.com/web-services/queries/)

> Find all cycle counts that have not started and return the record number, cycle count ID, description, and warehouse ID for each:

```
<query>
    <object>ICCYCLECOUNT</object>
    <filter>
        <equalto>
            <field>COUNTSTATE</field>
            <value>Not Started</value>
        </equalto>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>CYCLECOUNTID</field>
        <field>CYCLECOUNTDESC</field>
        <field>WAREHOUSEID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNT` |
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

### Query and List Cycle Counts (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ICCYCLECOUNT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get a Cycle Count

#### `read`

```
<read>
    <object>ICCYCLECOUNT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNT`. |
| keys | Required | string | Comma-separated list of cycle count `RECORDNO` to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create a Cycle Count

#### `create`

```
<create>
  <ICCYCLECOUNT>
    <CYCLECOUNTDESC></CYCLECOUNTDESC>
    <WAREHOUSEID>1</WAREHOUSEID>
    <EMPUSERID>11</EMPUSERID>
    <SHOWQTYONHAND>true</SHOWQTYONHAND>
  </ICCYCLECOUNT>
</create>
```

#### Parameters

Note that the CYCLECOUNTID is auto-generated; you cannot specify it in a `create` request.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CYCLECOUNTDESC | Required | string | Information about the cycle count that can be used for searching and sorting. |
| WAREHOUSEID | Required | string | `WAREHOUSEID` of the [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/) where the inventory cycle count is being done. |
| EMPUSERKEY | Required | integer | The employee who will perform the count. |
| SHOWQTYONHAND | Optional | Boolean | Set to `true` to display the item quantity on hand on any worksheets that are printed for employees who are performing the manual count.
*   `false` (default)
*   `true`

 |

* * *

### Delete a Cycle Count

You can delete any cycle count that is in progress or hasn’t been started.

#### `delete`

```
<delete>
    <object>ICCYCLECOUNT</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNT` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the cycle count objects to delete. |

* * *

Inventory Cycle Count Lines
---------------------------

Every line (item) in a cycle count is represented by an `ICCYCLECOUNTENTRY` object, which is used to record the quantity and location of items counted.

### Get Inventory Cycle Count Entry Object Definition

#### `lookup`

> List all the fields and relationships for the inventory cycle count entry object:

```
<lookup>
    <object>ICCYCLECOUNTENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNTENTRY` |

* * *

### Query and List Cycle Count Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List item information for each inventory cycle count line in cycle count 130:

```
<query>
    <object>ICCYCLECOUNTENTRY</object>
    <filter>
        <equalto>
            <field>CYCLECOUNTID</field>
            <value>130</value>
        </equalto>
    </filter>
    <select>
        <field>ITEMID</field>
        <field>ITEMNAME</field>
        <field>QUANTITYONHAND</field>
        <field>QUANTITYCOUNTED</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNTENTRY` |
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

### Query and List Inventory Cycle Count Lines (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ICCYCLECOUNTENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNTENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Inventory Cycle Count Lines

#### `read`

```
<read>
    <object>ICCYCLECOUNTENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNTENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the cycle count lines to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create a Cycle Count Line

#### `create`

```
<create>
    <ICCYCLECOUNTENTRY>
        <CYCLECOUNTKEY>130</CYCLECOUNTKEY>
        <ITEMID>Flux capacitor</ITEMID>
    </ICCYCLECOUNTENTRY>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ICCYCLECOUNTENTRY | Required | object | Object type to create. |

`ICCYCLECOUNTENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CYCLECOUNTKEY | Required | Integer | `RECORDNO` of the cycle count in which this item is being counted. |
| ITEMID | Required | String | `ITEMID` of the item to be included in the cycle count. |
| BINID | Optional | String | `BINID` of a [bin](https://developer.intacct.com/api/inventory-control/bins/) where the stock is located. |
| EXPIRATIONDATE | Optional | Date | Expiration Date of items to be counted. |
| LOTNO | Optional | String | Lot no to be counte. |
| SERIALNO | Optional | String | Serial no to be counted. |

* * *

### Update a Cycle Count Line

Update cycle count lines to record actual stock counts. You cannot update cycle count lines if the associated cycle count is in the `Not Started` state.

#### `update`

```
<update>
    <ICCYCLECOUNTENTRY>
        <RECORDNO>32</RECORDNO>
        <QUANTITYCOUNTED>165</QUANTITYCOUNTED>
        <QUANTITYDAMAGED>5</QUANTITYDAMAGED>
        <ADJUSTMENTREASON>fell off the wall</ADJUSTMENTREASON>
        <COUNTEDBYID>7</COUNTEDBYID>
    </ICCYCLECOUNTENTRY>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | `RECORDNO` of cycle count line to update. |
| ACTUALADJ | Optional | decimal | Change to item quantity. |
| ACTUALDMGADJ | Optional | integer | Change to item quantity due to damage. |
| ADJUSTMENTREASON | Optional | string | Explanation of why the count was adjusted. |
| COUNTEDBYID | Optional | string | ID of the employee who did the count. |
| QUANTITYCOUNTED | Optional | decimal | Total units counted. |
| QUANTITYDAMAGED | Optional | decimal | Total units damaged. |
| REVIEWCOMMENT | Optional | string | Additional comment on the count of this item. |

* * *

### Delete a Cycle Count Line

#### `delete`

```
<delete>
    <object>ICCYCLECOUNTENTRY</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ICCYCLECOUNT` |
| keys | Required | string | Comma-separated list of `RECORDNO` of cycle count lines to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

