Title: Items

URL Source: https://developer.intacct.com/api/inventory-control/items/

Markdown Content:
*   [Get Item Object Definition](https://developer.intacct.com/api/inventory-control/items/#get-item-object-definition)
*   [Query and List Items](https://developer.intacct.com/api/inventory-control/items/#query-and-list-items)
*   [Query and List Items (Legacy)](https://developer.intacct.com/api/inventory-control/items/#query-and-list-items-legacy)
*   [Get an Item](https://developer.intacct.com/api/inventory-control/items/#get-an-item)
*   [Get Item by ID](https://developer.intacct.com/api/inventory-control/items/#get-item-by-id)
*   [Create an Item](https://developer.intacct.com/api/inventory-control/items/#create-an-item)
*   [Create an Item (Legacy)](https://developer.intacct.com/api/inventory-control/items/#create-an-item-legacy)
*   [Update an Item](https://developer.intacct.com/api/inventory-control/items/#update-an-item)
*   [Update an Item (Legacy)](https://developer.intacct.com/api/inventory-control/items/#update-an-item-legacy)
*   [Delete an Item](https://developer.intacct.com/api/inventory-control/items/#delete-an-item)
*   [Delete an Item (Legacy)](https://developer.intacct.com/api/inventory-control/items/#delete-an-item-legacy)

* * *

Items are goods, services, or kits that you purchase from vendors or sell to customers. Items are used in Inventory Control, Order Entry, and Purchasing.

The type of an item (`ITEMTYPE`) affects other item parameters. Possible item types are:

*   `Inventory` - Items that will be available in inventory, sales, and purchasing transactions.
*   `Non-Inventory` - Items that will be available in both sales and purchasing transactions or contracts. They can also appear in inventory if `ENABLEFULFILLMENT` is `true`.
*   `Non-Inventory (Purchase only)` - Items that will only be available in purchasing transactions or contract expenses.
*   `Non-Inventory (Sales only)` - Items that will only be available in sales transactions or contracts.
*   `Kit` - The parent item of a (non-stockable) kit (which is assembled from other items at the time of the order). This type is only available if Kits is enabled in either Order Entry or Inventory Control.
*   `Stockable Kit` - The parent item of a stockable kit (which is assembled from other items and stored before order). This type is only available if Stockable kits is enabled in Inventory Control.

* * *

Get Item Object Definition
--------------------------

#### `lookup`

> List all the fields and relationships for the item object:

```
<lookup>
    <object>ITEM</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEM` |

* * *

Query and List Items
--------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List all inventory items:

```
<query>
    <object>ITEM</object>
    <select>
        <field>ITEMID</field>
        <field>NAME</field>
        <field>RECORDNO</field>
    </select>
    <filter>
        <equalto>
            <field>ITEMTYPE</field>
            <value>Inventory</value>
        </equalto>
    </filter>
</query>
```

> List all items that allow multiple tax groups (GB, AU, and ZA only):

```
<query>
    <object>ITEM</object>
    <select>
        <field>RECORDNO</field>
        <field>ITEMID</field>
    </select>
    <filter>
        <equalto>
            <field>ALLOWMULTIPLETAXGRPS</field>
            <value>true</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEM` |
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

Query and List Items (Legacy)
-----------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEM` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

**Item-specific `query` fields and values:**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEMTYPE | Optional | string | Item type.
*   `I` - Inventory
*   `NI` - Non-Inventory
*   `NP` - Non-Inventory (Purchase only)
*   `NS` - Non-Inventory (Sales only)
*   `K` - Kit
*   `SK` - Stockable Kit

 |
| COST\_METHOD | Optional | string | Cost method.

*   `Standard`
*   `Average`
*   `FIFO`
*   `LIFO`

 |
| VSOECATEGORY | Optional | string | VSOE category.

*   `PSD` - Product - Specified
*   `PUS` - Product - Unspecified
*   `USD` - Upgrade - Specified
*   `USS` - Upgrade - Unspecified
*   `SFW` - Software
*   `SVR` - Services
*   `PCS` - Post Contract Support

 |
| VSOEDLVRSTATUS | Optional | string | VSOE default deferral status.

*   `D` - Delivered
*   `U` - Undelivered

 |
| VSOEREVDEFSTATUS | Optional | string | VSOE default deferral status.

*   `I` - Defer until item is delivered
*   `B` - Defer bundle until item is delivered.

 |
| REVPOSTING | Optional | string | Kit revenue posting.

*   `I` - Component level
*   `K` - Kit level

 |
| REVPRINTING | Optional | string | Kit print format.

*   `I` - Individual components
*   `K` - Kit

 |
| TERMPERIOD | Optional | string | Periods measured in.

*   `D` - Days
*   `W` - Weeks
*   `M` - Months
*   `Y` - Years

 |

* * *

Get an Item
-----------

#### `read`

```
<read>
    <object>ITEM</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEM`. |
| keys | Required | string | Comma-separated list of `RECORDNO` of item to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Item by ID
--------------

#### `readByName`

```
<readByName>
    <object>ITEM</object>
    <keys>I1</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEM`. |
| keys | Required | string | Comma-separated list of `ITEMID` of the item to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create an Item
--------------

[History](https://developer.intacct.com/api/inventory-control/items/#history-create-item)

| Release | Changes |
| --- | --- |
| 2024 Release 2 | Added DEFAULT\_CONVERSIONTYPE |
| 2022 Release 2 | Added ENABLEFULFILLMENT |
| 2021 Release 3 | Added DENSITYUOM, DENSITY |
| 2021 Release 2 | Added WEIGHTUOM, NETWEIGHT, LWHUOM, LENGTH, WIDTH, HEIGHT, THICKNESSUOM, THICKNESS, MINIMUMTHICKNESS, MAXIMUMTHICKNESS, AREAUOM, AREA, VOLUMEUOM, VOLUME, DIAMETERUOM, INNERDIAMETER, OUTERDIAMETER, DUROMETER, UPC12, EAN13, SAFETYITEM, RESTRICTEDITEM, COMPLIANTITEM, CONDITION, ENGINEERINGALERT, SPECIFICATION1, SPECIFICATION2, SPECIFICATION3, ENGINEERINGAPPROVAL, QUALITYCONTROLAPPROVAL, SALESAPPROVAL, PRIMARYCOUNTRYOFORIGIN, BRAND, SUBBRAND, CATEGORY, SUBCATEGORY, CATALOGREF, COLOR, STYLE, SIZE1, SIZE2, GIFTCARD, WEBENABLED, WEBNAME, WEBSHORTDESC, WEBLONGDESC |
| 2020 Release 3 | Added ALLOWMULTIPLETAXGRPS, ITEMTAXGRPITEMMAPS |
| 2019 Release 4 | Added AUTOPRINTLABEL |
| 2018 Release 4 | Added ENABLE\_REPLENISHMENT, DEFAULT\_REPLENISHMENT\_UOM, REPLENISHMENT\_METHOD, SAFETY\_STOCK, MAX\_ORDER\_QTY, REORDER\_POINT, REORDER\_QTY, FORECAST\_DEMAND\_IN\_LEAD\_TIME, VENDORINFO, WAREHOUSEINFO |
| 2018 Release 3 | Added ENABLELANDEDCOST and LANDEDCOSTINFO |
| 2023 Release 4 | Added CONTRACTENABLED |

#### `create`

> Create an item:

```
<create>
    <ITEM>
        <ITEMID>I1</ITEMID>
        <NAME>hello world</NAME>
        <ITEMTYPE>Inventory</ITEMTYPE>
    </ITEM>
</create>
```

> Create an item with landed costs:

```
<create>
    <ITEM>
        <ITEMID>I1</ITEMID>
        <NAME>TESTING</NAME>
        <ITEMTYPE>Inventory</ITEMTYPE>
        <ENABLELANDEDCOST>true</ENABLELANDEDCOST>
        <LANDEDCOSTINFO>
            <ITEMLANDEDCOST>
                <METHOD>Volume</METHOD>
                <VALUE>2</VALUE>
                <ACTIVE>true</ACTIVE>
            </ITEMLANDEDCOST>
            <ITEMLANDEDCOST>
                <METHOD>Weight</METHOD>
                <VALUE>1</VALUE>
                <ACTIVE>true</ACTIVE>
            </ITEMLANDEDCOST>
        </LANDEDCOSTINFO>
    </ITEM>
</create>
```

> Create an item with replenishment features. For this example, warehouse WH01 has a shorter lead time (3 days) for parts ordered from the nearby Snap Hardware distributor. For other warehouses, the lead time would be taken from the vendor entry under VENDORINFO.

```
<create>
    <ITEM>
        <ITEMID>Hex bolt-033</ITEMID>
        <NAME>Hex bolt 2 inch</NAME>
        <ITEMTYPE>Inventory</ITEMTYPE>
        <!-- Apply across vendors (Vendor history tab) -->
        <ENABLE_REPLENISHMENT>true</ENABLE_REPLENISHMENT>
        <REPLENISHMENT_METHOD>Reorder point</REPLENISHMENT_METHOD>
        <DEFAULT_REPLENISHMENT_UOM>Each</DEFAULT_REPLENISHMENT_UOM>
        <REORDER_POINT>12</REORDER_POINT>
        <REORDER_QTY>24</REORDER_QTY>
        <SAFETY_STOCK>6</SAFETY_STOCK>
        <!-- end -->
        <WAREHOUSEINFO>
            <ITEMWAREHOUSEINFO>
                <WAREHOUSEID>WH01</WAREHOUSEID>
                <!-- Apply for warehouse/vendor combo (General tab, Warehouse, VENDOR ENTRIES) -->
                <ITEMWAREHOUSEVENDORENTRIES>
                    <VENDORID>Acme</VENDORID>
                    <STOCKNO>163</STOCKNO>
                    <LEAD_TIME>5</LEAD_TIME>
                    <ECONOMIC_ORDER_QTY>36</ECONOMIC_ORDER_QTY>
                </ITEMWAREHOUSEVENDORENTRIES>
                <ITEMWAREHOUSEVENDORENTRIES>
                    <VENDORID>Snap Hardware</VENDORID>
                    <STOCKNO>x993</STOCKNO>
                    <LEAD_TIME>3</LEAD_TIME>  <!-- Short lead time from Snap Hardware to WH01 -->
                </ITEMWAREHOUSEVENDORENTRIES>
                <!-- end -->
            </ITEMWAREHOUSEINFO>
        </WAREHOUSEINFO>
        <VENDORINFO>
            <!-- Apply for this vendor for all except warehouse WH01 (Vendor history tab, Vendor entries) -->
            <ITEMVENDOR>
                <VENDORID>Bosco Parts</VENDORID>
                <STOCKNO>167</STOCKNO>
                <REORDER_POINT>24</REORDER_POINT>
                <REORDER_QTY>12</REORDER_QTY>
                <SAFETY_STOCK>6</SAFETY_STOCK>
            </ITEMVENDOR>
            <ITEMVENDOR>
                <VENDORID>Snap Hardware</VENDORID>
                <STOCKNO>x993</STOCKNO>
                <LEAD_TIME>7</LEAD_TIME>
            </ITEMVENDOR>
            <!-- end -->
        </VENDORINFO>
    </ITEM>
</create>
```

> Create an item with two tax groups:

```
<create>
    <ITEM>
        <ITEMID>Car_Spark_Plugs</ITEMID>
        <NAME>Spark Plugs for Car</NAME>
        <ALLOWMULTIPLETAXGRPS>true</ALLOWMULTIPLETAXGRPS>
        <ITEMTAXGRPITEMMAPS>
            <ITEMTAXGRPITEMMAP>
                <TAXGROUP>
                    <NAME>Goods Standard Rate</NAME>
                </TAXGROUP>
            </ITEMTAXGRPITEMMAP>
            <ITEMTAXGRPITEMMAP>
                <TAXGROUP>
                    <NAME>No VAT</NAME>
                </TAXGROUP>
            </ITEMTAXGRPITEMMAP>
        </ITEMTAXGRPITEMMAPS>
    </ITEM>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEM | Required | object | Object type to create. |

`ITEM`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEMID | Required | string | Item ID to create. |
| NAME | Required | string | Item name |
| STATUS | Optional | string | Status.
*   `active` (default)
*   `inactive`

 |
| ITEMTYPE | Required | string | Item type.

*   `Inventory`
*   `Non-Inventory`
*   `Non-Inventory (Purchase only)`
*   `Non-Inventory (Sales only)`
*   `Kit`
*   `Stockable Kit`

 |
| ENABLEFULFILLMENT | Optional | boolean | Set to `true` to enable fulfillment for a non-inventory item that you want to be able to include in kits. |
| CONTRACTENABLED | Optional | boolean | If `ITEMTYPE` is set to kit, this field must be set to `true` to indicate that kits are enabled for contracts and that the item must adhere to restrictions for the kit. |
| PRODUCTLINEID | Optional | string | [`PRODUCTLINEID`](https://developer.intacct.com/api/inventory-control/product-lines/) of the product line that you want to add this product to. |
| COST\_METHOD | Optional | string | Cost method.

*   `Standard`
*   `Average`
*   `FIFO`
*   `LIFO`

 |
| EXTENDED\_DESCRIPTION | Optional | string | Extended description |
| PODESCRIPTION | Optional | string | Purchasing description |
| SODESCRIPTION | Optional | string | Sales description |
| UOMGRP | Optional | string | Unit of measure group.

*   `Area`
*   `Count`
*   `Duration`
*   `Length`
*   `Numbers`
*   `Time`
*   `Volume`
*   `Weight`
*   an existing custom group name

 |
| NOTE | Optional | string | Note |
| GLGROUP | Optional | string | Item GL group name |
| DEFAULT\_CONVERSIONTYPE | Optional | string | Transaction workflow conversion type. Required if `Enable price conversion` Order Entry/Purchasing configuration option is enabled.

*   `Price`
*   `Quantity (default)`

 |
| STANDARD\_COST | Optional | currency | Standard cost |
| BASEPRICE | Optional | currency | Base price |
| TAXABLE | Optional | boolean | Taxable.

*   `true` - Yes (default)
*   `false` - No

 |
| TAXGROUP | Optional | [object](https://developer.intacct.com/api/inventory-control/items/#create-ITEM.TAXGROUP) | Item tax group |
| ALLOWMULTIPLETAXGRPS | Optional | boolean | Allow multiple item tax groups per item, which is needed when an item is taxed at different rates in different tax jurisdictions.

*   `false` (default)
*   `true` - allow multiple item tax groups

When you set this to `true` and provide an item tax group mapping (`ITEMTAXGRPITEMMAPS`), the tax group at the header level is ignored and the mapping is used instead. (GB, AU, and ZA only) |
| ITEMTAXGRPITEMMAPS | Optional | array of [`ITEMTAXGRPITEMMAP`](https://developer.intacct.com/api/inventory-control/items/#create-ITEM.ITEMTAXGRPITEMMAPS.ITEMTAXGRPITEMMAP) | Required when `ALLOWMULTIPLETAXGRPS` is set to `true`. Maps item to different tax groups that are available with the given tax solution. (GB, AU, and ZA only) |
| DEFAULTREVRECTEMPLKEY | Optional | string | Default revenue recognition template ID |
| INCOMEACCTKEY | Optional | string | Revenue GL account number |
| INVACCTKEY | Optional | string | Inventory GL account number |
| EXPENSEACCTKEY | Optional | string | Expense GL account number |
| COGSACCTKEY | Optional | string | COGS GL account number |
| OFFSETOEGLACCOUNTKEY | Optional | string | AR GL account number |
| OFFSETPOGLACCOUNTKEY | Optional | string | AP GL account number |
| DEFERREDREVACCTKEY | Optional | string | Deferred revenue GL account number |
| VSOECATEGORY | Optional | string | VSOE category.

*   `Product - Specified`
*   `Product - Unspecified`
*   `Upgrade - Specified`
*   `Upgrade - Unspecified`
*   `Software`
*   `Services`
*   `Post Contract Support(PCS)`

 |
| VSOEDLVRSTATUS | Optional | string | VSOE default delivery status.

*   `Delivered`
*   `Undelivered`

 |
| VSOEREVDEFSTATUS | Optional | string | VSOE default deferral status.

*   `Defer until item is delivered`
*   `Defer bundle until item is delivered`

 |
| REVPOSTING | Optional | string | Kit revenue posting.

*   `Component Level`
*   `Kit Level`

 |
| REVPRINTING | Optional | string | Kit print format.

*   `Individual Components`
*   `Kit`

 |
| SUBSTITUTEID | Optional | string | Substitute item ID |
| ENABLE\_SERIALNO | Optional | boolean | Serial tracking enabled.

*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| SERIAL\_MASKKEY | Optional | string | Serial number mask to enforce a specific format. Applicable to inventory or stockable kit item types. |
| ENABLE\_LOT\_CATEGORY | Optional | boolean | Lot tracking enabled.

*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| LOT\_CATEGORYKEY | Optional | string | Lot category. Applicable to inventory or stockable kit item types. |
| ENABLE\_BINS | Optional | boolean | Bin tracking enabled.

*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| ENABLE\_EXPIRATION | Optional | boolean | Expiration tracking enabled.

*   `false` - No (default)
*   `true` - Yes

 |
| UPC | Optional | string | UPC |
| INV\_PRECISION | Optional | integer | Inventory unit cost precision |
| SO\_PRECISION | Optional | integer | Sales unit cost precision |
| PO\_PRECISION | Optional | integer | Purchasing unit cost precision |
| ENABLELANDEDCOST | Optional | boolean | Enable landed costs for Inventory item.

*   `false` - No (default)
*   `true` - Yes

 |
| LANDEDCOSTINFO | Optional | array of [`ITEMLANDEDCOST`](https://developer.intacct.com/api/inventory-control/items/#create-ITEM.LANDEDCOSTINFO.ITEMLANDEDCOST) | Information about landed cost mechanisms. `ENABLELANDEDCOST` must be set to `true`. |
| HASSTARTENDDATES | Optional | boolean | Item has start and end dates.

*   `false` - No (default)
*   `true` - Yes

 |
| TERMPERIOD | Optional | string | Periods measured in.

*   `Days`
*   `Weeks`
*   `Months`
*   `Years`

 |
| TOTALPERIODS | Optional | integer | Number of periods |
| COMPUTEFORSHORTTERM | Optional | boolean | Prorate price allowed.

*   `false` - No (default)
*   `true` - Yes

 |
| RENEWALMACROID | Optional | string | Default renewal macro ID |
| ENABLE\_REPLENISHMENT | Optional | boolean | Enable replenishment for this item in the Vendor history.

*   `true` - Enable (default)
*   `false` - disable

 |
| DEFAULT\_REPLENISHMENT\_UOM | Optional | string | Units of measure default for base units for inventory replenishment for this item in the Vendor history. For example, with the `Count` unit of measure group, you can specify `each`, `dozen`, or `pair`. See the information about [unit of measure groups](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=About_unit_of_measure_groups) in the Sage Intacct product help. |
| REPLENISHMENT\_METHOD | Optional | string | Replenishment method for this item in the Vendor history. Specifies how the amount to reorder is calculated.

*   `Reorder point` - base calculation on a specific reorder quantity and optional safety stock quantity
*   `Demand forecast by single value` - base calculation on lead time for the vendor
*   `Demand forecast by fluctuating values` - base calculation on fluctuating forecast for an item

See the information about [replenishment methods and calculations](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Replenishment_methods_and_calculations) in the Sage Intacct product help. (Default: Reorder point or as configured for inventory) |
| SAFETY\_STOCK | Optional | integer | Safety stock for this item in the Vendor history. Extra quantity held in inventory to reduce the risk of stock outs due to uncertainty in supply and demand. (Default: 0) |
| MAX\_ORDER\_QTY | Optional | integer | Maximum order quantity for this item in the Vendor history. Largest amount you can order in any one order. The value you provide may be affected by the economic order quantity and/or unit of measure set on the vendor. (Default is 0, meaning no maximum) |
| REORDER\_POINT | Optional | integer | Reorder point specifying the quantity of inventory that you don’t want to fall below. When the current net inventory falls to the reorder point plus the safety stock, the item is triggered for reorder. Use blank or positive integers. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. (Default: 1) |
| REORDER\_QTY | Optional | integer | Reorder quantity for this item in the Vendor history. As an example, if 12 units are needed according to other replenishment calculations, a reorder quantity of 50 would cause the generated purchase order to be for 50. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. (Default is 0, meaning no suggestion) |
| FORECAST\_DEMAND\_IN\_LEAD\_TIME | Optional | integer | Forecast demand in lead time. Specifies the quantity of this item expected to be sold during the lead time. Valid values are blank, 0, and positive integers. Only applicable when the REPLENISHMENT\_METHOD is `Demand forecast by a single value`. |
| WAREHOUSEINFO | Optional | array of [`ITEMWAREHOUSEINFO`](https://developer.intacct.com/api/inventory-control/items/#create-ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO) | Item Warehouse information. These parameter values override the replenishment values specified for the item in the Vendor history. |
| VENDORINFO | Optional | array of [`ITEMVENDOR`](https://developer.intacct.com/api/inventory-control/items/#create-ITEM.VENDORINFO.ITEMVENDOR) | Container for Vendor entries in Vendor history. |
| AUTOPRINTLABEL | Optional | boolean | Auto print label. This parameter is used to trigger an integrated third-party tool that creates scanner labels.

*   `false` - do not print labels (default)
*   `true` - print labels

 |
| WEIGHTUOM  
NETWEIGHT  
SHIP\_WEIGHT | Optional | string  
decimal  
decimal | The weight of the item: unit of measure, net weight and shipping weight (also called gross weight). You can specify `SHIP_WEIGHT` without `WEIGHTUOM` or `NETWEIGHT`, but if you specify `NETWEIGHT` you must also specify the other two. `WEIGHTUOM` must be set to one of the values defined for the `Weight` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| LWHUOM  
LENGTH  
WIDTH  
HEIGHT | Optional | string  
decimal  
decimal  
decimal | The size of the item, useful for calculating storage bin and shipping box size requirements. Specify the unit of measure and the length, width, and height. You must specify all four values or none. `LWHUOM` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| THICKNESSUOM  
THICKNESS  
MINIMUMTHICKNESS  
MAXIMUMTHICKNESS | Optional | string  
decimal  
decimal  
decimal | The thickness of the item, useful for calculating storage bin or shipping box size requirements. Specify the unit of measure, actual thickness, and minimum and maximum thickness. You must specify all four values or none. If the item thickness does not vary, set all three thickness fields to the same value. `THICKNESSUOM` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| AREAUOM  
AREA | Optional | string  
decimal | The area of the item: unit of measure and area. You must specify both or neither. `AREAUOM` must be set to one of the values defined for the `Area` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| VOLUMEUOM  
VOLUME | Optional | string  
decimal | The volume of the item: unit of measure and total volume. You must specify both or neither. `VOLUMEUOM` must be set to one of the values defined for the `Volume` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| DIAMETERUOM  
INNERDIAMETER  
OUTERDIAMETER | Optional | string  
decimal  
decimal | The diameter of the item: Unit of measure, and inner and outer diameter. You must specify all three or none. `DIAMETERUOM` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| DUROMETER | Optional | string | Durometer (hardness) measurement of the item. |
| DENSITYUOM  
DENSITY | Optional | string  
decimal | The density of the item: unit of measure and density value. |
| UPC12 | Optional | Integer | UPC-12, the 12-digit Univieral Product Code of the item. |
| EAN13 | Optional | integer | EAN-13, the 13-digit International Article Number of the item. |
| SAFETYITEM | Optional | boolean | Use `true` if item is classified as a Safety Item. (Default `false`) |
| RESTRICTEDITEM | Optional | boolean | Use `true` if item is classified as a Restricted Item. (Default `false`) |
| COMPLIANTITEM | Optional | boolean | Use `true` if item is classified as a Compliant Item. (Default `false`) |
| CONDITION | Optional | string | Condition name or descriptor. |
| ENGINEERINGALERT | Optional | string | Engineering Alert name or descriptor. |
| SPECIFICATION1 | Optional | string | Specification name/descriptor 1. |
| SPECIFICATION2 | Optional | string | Specification name/descriptor 2. |
| SPECIFICATION3 | Optional | string | Specification name/descriptor 3. |
| ENGINEERINGAPPROVAL | Optional | boolean | 

*   `true` - the item is approved by Engineering
*   `false` - the item is not approved (default)

 |
| QUALITYCONTROLAPPROVAL | Optional | boolean | 

*   `true` - the item is approved by Quality Control
*   `false` - the item is not approved (default)

 |
| SALESAPPROVAL | Optional | boolean | 

*   `true` - the item is approved by Sales
*   `false` - the item is not approved (default)

 |
| PRIMARYCOUNTRYOFORIGIN | Optional | string | Primary country of origin, for example “China 75%”. |
| BRAND | Optional | string | Brand of the item. |
| SUBBRAND | Optional | string | Sub brand of the item. |
| CATEGORY | Optional | string | Category of the item. |
| SUBCATEGORY | Optional | string | Sub category of the item. |
| CATALOGREF | Optional | string | Catalog reference for the item. |
| COLOR | Optional | string | Color of the item. |
| STYLE | Optional | string | Style of the item. |
| SIZE1 | Optional | string | Size 1 of the item. |
| SIZE2 | Optional | string | Size 2 of the item. |
| GIFTCARD | Optional | boolean | 

*   `true` - the item is a gift card
*   `false` - the item is not a gift card (default)

 |
| WEBENABLED | Optional | boolean | 

*   `true` - the item is web enabled
*   `false` - the item is not web enabled (default)

 |
| WEBNAME | Optional | string | Name of the item to appear on the web. |
| WEBSHORTDESC | Optional | string | Short description for the web. |
| WEBLONGDESC | Optional | string | Long description for the web. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`ITEM.TAXGROUP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Tax group name |

`ITEM.ITEMTAXGRPITEMMAPS.ITEMTAXGRPITEMMAP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TAXGROUP | Optional | object | Provides the tax group name. (GB, AU, and ZA only) |
| NAME | Optional | string | Name of an item tax group name from the an available tax solution. (GB, AU, and ZA only) |

`ITEM.LANDEDCOSTINFO.ITEMLANDEDCOST`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEMID | Required | string | Item ID |
| METHOD | Required | string | Landed cost mechanism.
*   `Volume`
*   `Weight`
*   `Count`

 |
| VALUE | Required | string | Value for the landed cost |
| ACTIVE | Optional | boolean | Status.

*   `true` - active
*   `false` - inactive

 |

`ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO`

For the given warehouse, these parameter values override any replenishment values specified for the item in the Vendor history.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| WAREHOUSEID | Required | string | `WAREHOUSEID` of an active [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/). |
| ENABLE\_REPLENISHMENT | Optional | boolean | Enable replenishment for this item and warehouse combination.
*   `true` - enable replenishment (default)
*   `false` - do not enable

 |
| REPLENISHMENT\_METHOD | Optional | string | Replenishment method. Specifies how the amount to reorder is calculated.

*   `Reorder point` - base calculation on a specific reorder quantity and optional safety stock quantity
*   `Demand forecast by single value` - base calculation on lead time for the vendor
*   `Demand forecast by fluctuating values` - base calculation on fluctuating forecast for an item

See the information about [replenishment methods and calculations](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Replenishment_methods_and_calculations) in the Sage Intacct product help. (Default: Reorder point or as configured for inventory) |
| SAFETY\_STOCK | Optional | integer | Safety stock. Extra quantity held in inventory to reduce the risk of stock outs due to uncertainty in supply and demand. (Default: 0) |
| MAX\_ORDER\_QTY | Optional | integer | Maximum order quantity allowed in any one order. The value you provide may be affected by the economic order quantity and/or unit of measure set on the vendor. (Default is 0, meaning no maximum) |
| REORDER\_POINT | Optional | integer | Reorder point specifying the quantity of inventory that you don’t want to fall below. When the current net inventory falls to the reorder point plus the safety stock, the item is triggered for reorder. Use blank or positive integers. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. |
| REORDER\_QTY | Optional | integer | Reorder quantity for this item. As an example, if 12 units are needed according to other replenishment calculations, a reorder quantity of 50 would cause the generated purchase order to be for 50. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. (Default is 0, meaning no suggestion) |
| ITEMWAREHOUSEVENDORENTRIES | optional | array of [`ITEMWAREHOUSEVENDORENTRIES`](https://developer.intacct.com/api/inventory-control/items/#create-ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO.ITEMWAREHOUSEVENDORENTRIES) | Vendor Entries. Provides replenishment parameters for this item according to given warehouse and vendor combinations. These parameters override the values for the Vendor entries in the Vendor history. Multiple `ITEMWAREHOUSEVENDORENTRIES` elements may be passed. |

`ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO.ITEMWAREHOUSEVENDORENTRIES`

For the given warehouse, these entries override any Vendor entries in Vendor history.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDORID | Required | string | Vendor ID of an existing vendor that ships the item to this warehouse |
| PREFERRED\_VENDOR | Optional | boolean | Preferred vendor status.
*   `true` - designate as preferred
*   `false` - not a preferred vendor

There can only be one preferred vendor. (Default: `true` for the first vendor in the list (the lowest record number), `false` for the others) |
| STOCKNO | Optional | string | Stock number the vendor uses for the item |
| LEAD\_TIME | Optional | string | Lead time in days when ordering this particular item. Valid values are blank, 0, and positive integers. (Default: lead time for the vendor) |
| FORECAST\_DEMAND\_IN\_LEAD\_TIME | Optional | integer | Forecast demand in lead time. Specifies the quantity of this item expected to be sold during the lead time. Valid values are blank, 0, and positive integers. Only applicable when the REPLENISHMENT\_METHOD is `Demand forecast by a single value`. |
| ECONOMIC\_ORDER\_QTY | Optional | integer | Economic order quantity. Specifies the number of units per order to minimize the total costs of inventory—such as holding costs and order costs (Default: `1`) |
| MIN\_ORDER\_QTY | Optional | integer | Minimum order quantity allowed (Default: `1`) |
| UOM | Optional | string | Unit of measure that the vendor sells this item in—should match the UOM used for the Purchase Order. (Default: Base unit of the item’s UOM group for inventory replenishment.) |

`ITEM.VENDORINFO.ITEMVENDOR`

These entries apply when there are no corresponding warehouse-specific Vendor entries.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDORID | Required | string | Vendor ID of an existing vendor that ships the item from this warehouse |
| PREFERRED\_VENDOR | Optional | boolean | Preferred vendor status.
*   `true` - designate as preferred
*   `false` - not a preferred vendor

There can only be one preferred vendor. (Default: `true` for the first vendor in the list (the lowest record number), `false` for the others) |
| STOCKNO | Optional | string | Stock number the vendor uses for the item |
| LEAD\_TIME | Optional | string | Lead time in days when ordering this particular item. Valid values are blank, 0, and positive integers. (Default: lead time for the vendor) |
| FORECAST\_DEMAND\_IN\_LEAD\_TIME | Optional | integer | Forecast demand in lead time. Specifies the quantity of this item expected to be sold during the lead time. Valid values are blank, 0, and positive integers. Only applicable when the replenishment method is `Demand forecast by a single value`. |
| ECONOMIC\_ORDER\_QTY | Optional | string | Quantity of units per order to minimize the total costs of inventory—such as holding costs and order costs. (Default: `1`) |
| MIN\_ORDER\_QTY | Optional | integer | Minimum order quantity allowed (Default: `1`) |
| UOM | Optional | string | Unit of measure that the vendor sells this item in—should match the UOM used for the Purchase Order. (Default: Base unit of the item’s UOM group for inventory replenishment) |

* * *

Create an Item (Legacy)
-----------------------

[History](https://developer.intacct.com/api/inventory-control/items/#history-create-item-legacy)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added enablefulfillment |
| 2021 Release 3 | Added densityuom, density |
| 2021 Release 2 | Added weightuom, netweight, lwhuom, length, width, height, thicknessuom, thickness, minimumthickness, maximumthickness, areauom, area, volumeuom, volume, diameteruom, innerdiameter, outerdiameter, durometer, upc12, ean13, safetyitem, restricteditem, compliantitem, condition, engineeringalert, specification1, specification2, specification3, engineeringapproval, qualitycontrolapproval, salesapproval, primarycountryoforigin, brand, subbrand, category, subcategory, catalogref, color, style, size1, size2, giftcard, webenabled, webname, webshortdesc, weblongdesc |
| 2019 Release 4 | Added autoprintlabel |

#### `create_item`

```
<create_item>
    <itemid>I1234</itemid>
    <name>hello world</name>
    <itemtype>Inventory</itemtype>
</create_item>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | Item ID to create |
| name | Required | string | Item name |
| status | Optional | string | Status.
*   `active` (default)
*   `inactive`

 |
| itemtype | Required | string | Item type.

*   `Inventory`
*   `Non-Inventory`
*   `Non-Inventory (Purchase only)`
*   `Non-Inventory (Sales only)`
*   `Kit`
*   `Stockable Kit`

 |
| enablefulfillment | Optional | boolean | Set to `true` to enable fulfillment for a non-inventory item that you want to be able to include in kits. |
| enable\_bins | Optional | boolean | Bin tracking enabled.

*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| extended\_description | Optional | string | Extended description |
| productlineid | Optional | string | [`PRODUCTLINEID`](https://developer.intacct.com/api/inventory-control/product-lines/) of the product line that you want to add this product to. |
| substituteid | Optional | string | Substitute item ID |
| ship\_weight | Optional | decimal | Shipping weight |
| taxable | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
| cost\_method | Optional | string | Cost method. Use `Standard`, `Average`, `FIFO`, or `LIFO`. |
| standard\_cost | Optional | currency | Standard cost |
| base\_price | Optional | currency | Base price |
| glgroup | Optional | string | Item GL group name |
| note | Optional | string | Note |
| inventory\_precision | Optional | integer | Inventory unit cost precision |
| purchasing\_precision | Optional | integer | Purchasing unit cost precision |
| sales\_precision | Optional | integer | Sales unit cost precision |
| upc | Optional | string | UPC |
| hasstartenddates | Optional | boolean | Item has start and end dates. Use `false` for No, `true` for Yes. (Default: `false`) |
| term\_period | Optional | string | Periods measured in.

*   `Days`
*   `Weeks`
*   `Months`
*   `Years`

 |
| defaultnoofperiods | Optional | integer | Number of periods |
| computepriceforshortterm | Optional | boolean | Prorate price allowed. Use `false` for No, `true` for Yes. (Default: `false`) |
| itaxgroup | Optional | string | Item tax group name. |
| revenue\_posting | Optional | string | Kit revenue posting. Use `Component Level` or `Kit Level`. |
| vsoecategory | Optional | string | VSOE category. Use `Product - Specified`, `Software`, `Product - Unspecified`, `Upgrade - Unspecified`, `Upgrade - Specified`, `Services`, or `Post Contract Support(PCS)`. |
| vsoedlvrstatus | Optional | string | VSOE default delivery status. Use `Delivered` or `Undelivered`. |
| vsoerevdefstatus | Optional | string | VSOE default deferral status. Use `Defer until item is delivered` or `Defer bundle until item is delivered`. |
| incomeaccount | Optional | string | Revenue GL account number |
| invaccount | Optional | string | Inventory GL account number |
| expenseaccount | Optional | string | Expense GL account number |
| cogsaccount | Optional | string | COGS GL account number |
| offsetoeglaccount | Optional | string | AR GL account number |
| offsetpoglaccount | Optional | string | AP GL account number |
| defrevaccount | Optional | string | Deferred revenue GL account number |
| uomgrp | Optional | string | Unit of measure |
| customfields | Optional | array of `customfield` | Custom fields |
| autoprintlabel | Optional | boolean | Auto print label. This parameter is used to trigger an integrated third-party tool that creates scanner labels. Use `true` to print labels, `false` otherwise. (Default: `false`) |
| weightuom | Optional | string | Unit of measure for weight values. Required when `netweight` is specified for an item. |
| netweight | Optional | integer | Actual weight of the base item. Must be less than `ship_weight`. |
| lwhuom  
length  
width  
height | Optional | string  
decimal  
decimal  
decimal | The size of the item, useful for calculating storage bin and shipping box size requirements. Specify the unit of measure and the length, width, and height. You must specify all four values or none. `lwhuom` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| thicknessuom  
thickness  
minimumthickness  
maximumthickness | Optional | string  
decimal  
decimal  
decimal | The thickness of the item, useful for calculating storage bin or shipping box size requirements. Specify the unit of measure, actual thickness, and minimum and maximum thickness. You must specify all four values or none. If the item thickness does not vary, set all three thickness fields to the same value. `thicknessuom` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| areauom  
area | Optional | string  
decimal | The area of the item: unit of measure and area. You must specify both or neither. `areauom` must be set to one of the values defined for the `Area` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| volumeuom  
volume | Optional | string  
decimal | The volume of the item: unit of measure and total volume. You must specify both or neither. `VOLUMEUOM` must be set to one of the values defined for the `Volume` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| diameteruom  
innerdiameter  
outerdiameter | Optional | string  
decimal  
decimal | The diameter of the item: Unit of measure, and inner and outer diameter. You must specify all three or none. `diameteruom` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| durometer | Optional | string | Durometer (hardness) measurement of the item. |
| densityuom  
density | Optional | string  
decimal | The density of the item: unit of measure and density value. |
| upc12 | Optional | Integer | UPC-12, the 12-digit Univieral Product Code of the item. |
| ean13 | Optional | integer | EAN-13, the 13-digit International Article Number of the item. |
| safetyitem | Optional | boolean | Use `true` if item is classified as a Safety Item. (Default `false`) |
| restricteditem | Optional | boolean | Use `true` if item is classified as a Restricted Item. (Default `false`) |
| compliantitem | Optional | boolean | Use `true` if item is classified as a Compliant Item. (Default `false`) |
| condition | Optional | string | Condition name or descriptor. |
| engineeringalert | Optional | string | Engineering Alert name or descriptor. |
| specification1 | Optional | string | Specification name/descriptor 1. |
| specification2 | Optional | string | Specification name/descriptor 2. |
| specification3 | Optional | string | Specification name/descriptor 3. |
| engineeringapproval | Optional | boolean | Use `true` if item is approved by Engineering. (Default `false`) |
| qualitycontrolapproval | Optional | boolean | Use `true` if item is approved by Quality Control. (Default `false`) |
| salesapproval | Optional | boolean | Use `true` if item is approved by Sales. (Default `false`) |
| primarycountryoforigin | Optional | string | Primary country of origin, for example “China 75%”. |
| brand | Optional | string | Brand of the item. |
| subbrand | Optional | string | Sub brand of the item. |
| category | Optional | string | Category of the item. |
| subcategory | Optional | string | Sub category of the item. |
| catalogref | Optional | string | Catalog reference for the item. |
| color | Optional | string | Color of the item. |
| style | Optional | string | Style of the item. |
| size1 | Optional | string | Size 1 of the item. |
| size2 | Optional | string | Size 2 of the item. |
| giftcard | Optional | boolean | Use `true` if the item is a gift card (Default `false`) |
| webenabled | Optional | boolean | Use `true` if the item is Web enabled. (Default `false`) |
| webname | Optional | string | Name of the item to appear on the web. |
| webshortdesc | Optional | string | Short description for the web. |
| weblongdesc | Optional | string | Long description for the web. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update an Item
--------------

[History](https://developer.intacct.com/api/inventory-control/items/#history-update-item)

| Release | Changes |
| --- | --- |
| 2024 Release 2 | Added DEFAULT\_CONVERSIONTYPE |
| 2022 Release 2 | Added ENABLEFULFILLMENT |
| 2021 Release 3 | Added DENSITYUOM, DENSITY |
| 2021 Release 2 | Added WEIGHTUOM, NETWEIGHT, LWHUOM, LENGTH, WIDTH, HEIGHT, THICKNESSUOM, THICKNESS, MINIMUMTHICKNESS, MAXIMUMTHICKNESS, AREAUOM, AREA, VOLUMEUOM, VOLUME, DIAMETERUOM, INNERDIAMETER, OUTERDIAMETER, DUROMETER, UPC12, EAN13, SAFETYITEM, RESTRICTEDITEM, COMPLIANTITEM, CONDITION, ENGINEERINGALERT, SPECIFICATION1, SPECIFICATION2, SPECIFICATION3, ENGINEERINGAPPROVAL, QUALITYCONTROLAPPROVAL, SALESAPPROVAL, PRIMARYCOUNTRYOFORIGIN, BRAND, SUBBRAND, CATEGORY, SUBCATEGORY, CATALOGREF, COLOR, STYLE, SIZE1, SIZE2, GIFTCARD, WEBENABLED, WEBNAME, WEBSHORTDESC, WEBLONGDESC |
| 2020 Release 3 | Added ALLOWMULTIPLETAXGRPS, ITEMTAXGRPITEMMAPS |
| 2019 Release 4 | Added AUTOPRINTLABEL |
| 2018 Release 4 | Added ENABLE\_REPLENISHMENT, DEFAULT\_REPLENISHMENT\_UOM, REPLENISHMENT\_METHOD, SAFETY\_STOCK, MAX\_ORDER\_QTY, REORDER\_POINT, REORDER\_QTY, FORECAST\_DEMAND\_IN\_LEAD\_TIME, VENDORINFO, WAREHOUSEINFO |
| 2018 Release 3 | Added ENABLELANDEDCOST and LANDEDCOSTINFO |
| 2023 Release 4 | Added CONTRACTENABLED |

#### `update`

```
<update>
    <ITEM>
        <RECORDNO>12</RECORDNO>
        <NAME>hello world</NAME>
    </ITEM>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEM | Required | object | Object to update |

`ITEM`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Item `RECORDNO` to update |
| NAME | Required | string | Item name |
| STATUS | Optional | string | Status.
*   `active` (default)
*   `inactive`

 |
| ENABLEFULFILLMENT | Optional | boolean | Set to `true` to enable fulfillment for a non-inventory item that you want to be able to include in kits. |
| CONTRACTENABLED | Optional | boolean | If `ITEMTYPE` is set to kit, this field must be set to `true` to indicate that kits are enabled for contracts and that the item must adhere to restrictions for the kit. |
| PRODUCTLINEID | Optional | string | [`PRODUCTLINEID`](https://developer.intacct.com/api/inventory-control/product-lines/) of the product line that you want to add this product to. |
| EXTENDED\_DESCRIPTION | Optional | string | Extended description |
| PODESCRIPTION | Optional | string | Purchasing description |
| SODESCRIPTION | Optional | string | Sales description |
| UOMGRP | Optional | string | Unit of measure group.

*   `Area`
*   `Count`
*   `Duration`
*   `Length`
*   `Numbers`
*   `Time`
*   `Volume`
*   `Weight`
*   an existing custom group name

 |
| NOTE | Optional | string | Note |
| GLGROUP | Optional | string | Item GL group name |
| DEFAULT\_CONVERSIONTYPE | Optional | string | Transaction workflow conversion type. Required if `Enable price conversion` Order Entry/Purchasing configuration option is enabled.

*   `Price`
*   `Quantity (default)`

 |
| STANDARD\_COST | Optional | currency | Standard cost |
| BASEPRICE | Optional | currency | Base price |
| TAXABLE | Optional | boolean | Taxable.

*   `true` - Yes (default)
*   `false` - No

 |
| TAXGROUP | Optional | [object](https://developer.intacct.com/api/inventory-control/items/#update-ITEM.TAXGROUP) | Item tax group |
| ALLOWMULTIPLETAXGRPS | Optional | boolean | Allow multiple item tax groups per item, which is needed when an item is taxed at different rates in different tax jurisdictions.

*   `false` (default)
*   `true` - allow multiple item tax groups

When you set this to `true` and provide an item tax group mapping (`ITEMTAXGRPITEMMAPS`), the tax group at the header level is ignored and the mapping is used instead. (GB, AU, and ZA only) |
| ITEMTAXGRPITEMMAPS | Optional | array of [`ITEMTAXGRPITEMMAP`](https://developer.intacct.com/api/inventory-control/items/#update-ITEM.ITEMTAXGRPITEMMAPS.ITEMTAXGRPITEMMAP) | Required when `ALLOWMULTIPLETAXGRPS` is set to `true`. Maps item to different tax groups that are available with the given tax solution. (GB, AU, and ZA only) |
| DEFAULTREVRECTEMPLKEY | Optional | string | Default revenue recognition template ID |
| INCOMEACCTKEY | Optional | string | Revenue GL account number |
| INVACCTKEY | Optional | string | Inventory GL account number |
| EXPENSEACCTKEY | Optional | string | Expense GL account number |
| COGSACCTKEY | Optional | string | COGS GL account number |
| OFFSETOEGLACCOUNTKEY | Optional | string | AR GL account number |
| OFFSETPOGLACCOUNTKEY | Optional | string | AP GL account number |
| DEFERREDREVACCTKEY | Optional | string | Deferred revenue GL account number |
| VSOECATEGORY | Optional | string | VSOE category.

*   `Product - Specified`
*   `Product - Unspecified`
*   `Upgrade - Specified`
*   `Upgrade - Unspecified`
*   `Software`
*   `Services`
*   `Post Contract Support(PCS)`

 |
| VSOEDLVRSTATUS | Optional | string | VSOE default delivery status.

*   `Delivered`
*   `Undelivered`

 |
| VSOEREVDEFSTATUS | Optional | string | VSOE default deferral status.

*   `Defer until item is delivered`
*   `Defer bundle until item is delivered`

 |
| REVPOSTING | Optional | string | Kit revenue posting.

*   `Component Level`
*   `Kit Level`

 |
| REVPRINTING | Optional | string | Kit print format.

*   `Individual Components`
*   `Kit`

 |
| SUBSTITUTEID | Optional | string | Substitute item ID |
| ENABLE\_SERIALNO | Optional | boolean | Serial tracking enabled.

*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| SERIAL\_MASKKEY | Optional | string | Serial number mask. Applicable to inventory or stockable kit item types. Applicable to inventory or stockable kit item types. |
| ENABLE\_LOT\_CATEGORY | Optional | boolean | Lot tracking enabled.

*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| LOT\_CATEGORYKEY | Optional | string | Lot category. Applicable to inventory or stockable kit item types. |
| ENABLE\_BINS | Optional | boolean | Bin tracking enabled.

*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| ENABLE\_EXPIRATION | Optional | boolean | Expiration tracking enabled.

*   `false` - No (default)
*   `true` - Yes

 |
| UPC | Optional | string | UPC |
| INV\_PRECISION | Optional | integer | Inventory unit cost precision |
| SO\_PRECISION | Optional | integer | Sales unit cost precision |
| PO\_PRECISION | Optional | integer | Purchasing unit cost precision |
| ENABLELANDEDCOST | Optional | boolean | Enable landed costs for Inventory item.

*   `false` - No (default)
*   `true` - Yes

 |
| LANDEDCOSTINFO | Optional | array of [`ITEMLANDEDCOST`](https://developer.intacct.com/api/inventory-control/items/#update-ITEM.LANDEDCOSTINFO.ITEMLANDEDCOST) | Information about landed cost mechanisms. `ENABLELANDEDCOST` must be set to `true`. |
| HASSTARTENDDATES | Optional | boolean | Item has start and end dates.

*   `false` - No (default)
*   `true` - Yes

 |
| TERMPERIOD | Optional | string | Periods measured in.

*   `Days`
*   `Weeks`
*   `Months`
*   `Years`

 |
| TOTALPERIODS | Optional | integer | Number of periods |
| COMPUTEFORSHORTTERM | Optional | boolean | Prorate price allowed.

*   `false` - No (default)
*   `true` - Yes

 |
| RENEWALMACROID | Optional | string | Default renewal macro ID |
| ENABLE\_REPLENISHMENT | Optional | boolean | Enable replenishment for this item in the Vendor history.

*   `true` - Enable (default)
*   `false` - disable

 |
| DEFAULT\_REPLENISHMENT\_UOM | Optional | string | Units of measure default for base units for inventory replenishment for this item in the Vendor history. For example, with the `Count` unit of measure group, you can specify `each`, `dozen`, or `pair`. See the information about [unit of measure groups](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=About_unit_of_measure_groups) in the Sage Intacct product help. |
| REPLENISHMENT\_METHOD | Optional | string | Replenishment method for this item in the Vendor history. Specifies how the amount to reorder is calculated.

*   `Reorder point` - base calculation on a specific reorder quantity and optional safety stock quantity
*   `Demand forecast by single value` - base calculation on lead time for the vendor
*   `Demand forecast by fluctuating values` - base calculation on fluctuating forecast for an item

See the information about [replenishment methods and calculations](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Replenishment_methods_and_calculations) in the Sage Intacct product help. (Default: Reorder point or as configured for inventory) |
| SAFETY\_STOCK | Optional | integer | Safety stock for this item in the Vendor history. Extra quantity held in inventory to reduce the risk of stock outs due to uncertainty in supply and demand. (Default: 0) |
| MAX\_ORDER\_QTY | Optional | integer | Maximum order quantity for this item in the Vendor history. Largest amount you can order in any one order. The value you provide may be affected by the economic order quantity and/or unit of measure set on the vendor. (Default is 0, meaning no maximum) |
| REORDER\_POINT | Optional | integer | Reorder point specifying the quantity of inventory that you don’t want to fall below. When the current net inventory falls to the reorder point plus the safety stock, the item is triggered for reorder. Use blank or positive integers. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. (Default: 1) |
| REORDER\_QTY | Optional | integer | Reorder quantity for this item in the Vendor history. As an example, if 12 units are needed according to other replenishment calculations, a reorder quantity of 50 would cause the generated purchase order to be for 50. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. (Default is 0, meaning no suggestion) |
| FORECAST\_DEMAND\_IN\_LEAD\_TIME | Optional | integer | Forecast demand in lead time. Specifies the quantity of this item expected to be sold during the lead time. Valid values are blank, 0, and positive integers. Only applicable when the REPLENISHMENT\_METHOD is `Demand forecast by a single value`. |
| WAREHOUSEINFO | Optional | array of [`ITEMWAREHOUSEINFO`](https://developer.intacct.com/api/inventory-control/items/#update-ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO) | Item Warehouse information. These parameter values override the replenishment values specified for the item in the Vendor history. |
| VENDORINFO | Optional | array of [`ITEMVENDOR`](https://developer.intacct.com/api/inventory-control/items/#update-ITEM.VENDORINFO.ITEMVENDOR) | Container for Vendor entries in Vendor history. |
| AUTOPRINTLABEL | Optional | boolean | Auto print label. This parameter is used to trigger an integrated third-party tool that creates scanner labels.

*   `false` - do not print labels (default)
*   `true` - print labels

 |
| WEIGHTUOM  
NETWEIGHT  
SHIP\_WEIGHT | Optional | string  
decimal  
decimal | The weight of the item: unit of measure, net weight and shipping weight (also called gross weight). You can specify `SHIP_WEIGHT` without `WEIGHTUOM` or `NETWEIGHT`, but if you specify `NETWEIGHT` you must also specify the other two. `WEIGHTUOM` must be set to one of the values defined for the `Weight` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| LWHUOM  
LENGTH  
WIDTH  
HEIGHT | Optional | string  
decimal  
decimal  
decimal | The size of the item, useful for calculating storage bin and shipping box size requirements. Specify the unit of measure and the length, width, and height. You must specify all four values or none. `LWHUOM` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| THICKNESSUOM  
THICKNESS  
MINIMUMTHICKNESS  
MAXIMUMTHICKNESS | Optional | string  
decimal  
decimal  
decimal | The thickness of the item, useful for calculating storage bin or shipping box size requirements. Specify the unit of measure, actual thickness, and minimum and maximum thickness. You must specify all four values or none. If the item thickness does not vary, set all three thickness fields to the same value. `THICKNESSUOM` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| AREAUOM  
AREA | Optional | string  
decimal | The area of the item: unit of measure and area. You must specify both or neither. `AREAUOM` must be set to one of the values defined for the `Area` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| VOLUMEUOM  
VOLUME | Optional | string  
decimal | The volume of the item: unit of measure and total volume. You must specify both or neither. `VOLUMEUOM` must be set to one of the values defined for the `Volume` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| DIAMETERUOM  
INNERDIAMETER  
OUTERDIAMETER | Optional | string  
decimal  
decimal | The diameter of the item: Unit of measure, and inner and outer diameter. You must specify all three or none. `DIAMETERUOM` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| DUROMETER | Optional | string | Durometer (hardness) measurement of the item. |
| DENSITYUOM  
DENSITY | Optional | string  
decimal | The density of the item: unit of measure and density value. |
| UPC12 | Optional | Integer | UPC-12, the 12-digit Univieral Product Code of the item. |
| EAN13 | Optional | integer | EAN-13, the 13-digit International Article Number of the item. |
| SAFETYITEM | Optional | boolean | Use `true` if item is classified as a Safety Item. (Default `false`) |
| RESTRICTEDITEM | Optional | boolean | Use `true` if item is classified as a Restricted Item. (Default `false`) |
| COMPLIANTITEM | Optional | boolean | Use `true` if item is classified as a Compliant Item. (Default `false`) |
| CONDITION | Optional | string | Condition name or descriptor. |
| ENGINEERINGALERT | Optional | string | Engineering Alert name or descriptor. |
| SPECIFICATION1 | Optional | string | Specification name/descriptor 1. |
| SPECIFICATION2 | Optional | string | Specification name/descriptor 2. |
| SPECIFICATION3 | Optional | string | Specification name/descriptor 3. |
| ENGINEERINGAPPROVAL | Optional | boolean | 

*   `true` - the item is approved by Engineering
*   `false` - the item is not approved (default)

 |
| QUALITYCONTROLAPPROVAL | Optional | boolean | 

*   `true` - the item is approved by Quality Control
*   `false` - the item is not approved (default)

 |
| SALESAPPROVAL | Optional | boolean | 

*   `true` - the item is approved by Sales
*   `false` - the item is not approved (default)

 |
| PRIMARYCOUNTRYOFORIGIN | Optional | string | Primary country of origin, for example “China 75%”. |
| BRAND | Optional | string | Brand of the item. |
| SUBBRAND | Optional | string | Sub brand of the item. |
| CATEGORY | Optional | string | Category of the item. |
| SUBCATEGORY | Optional | string | Sub category of the item. |
| CATALOGREF | Optional | string | Catalog reference for the item. |
| COLOR | Optional | string | Color of the item. |
| STYLE | Optional | string | Style of the item. |
| SIZE1 | Optional | string | Size 1 of the item. |
| SIZE2 | Optional | string | Size 2 of the item. |
| GIFTCARD | Optional | boolean | 

*   `true` - the item is a gift card
*   `false` - the item is not a gift card (default)

 |
| WEBENABLED | Optional | boolean | 

*   `true` - the item is Web enabled
*   `false` - the item is not Web enabled (default)

 |
| WEBNAME | Optional | string | Name of the item to appear on the web. |
| WEBSHORTDESC | Optional | string | Short description for the web. |
| WEBLONGDESC | Optional | string | Long description for the web. |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`ITEM.TAXGROUP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Tax group name |

`ITEM.ITEMTAXGRPITEMMAPS.ITEMTAXGRPITEMMAP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TAXGROUP | Optional | object | Provides the tax group name. (GB, AU, and ZA only) |
| NAME | Optional | string | Name of an item tax group name from the an available tax solution. (GB, AU, and ZA only) |

`ITEM.LANDEDCOSTINFO.ITEMLANDEDCOST`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ITEMID | Required | string | Item ID |
| METHOD | Required | string | Landed cost mechanism.
*   `Volume`
*   `Weight`
*   `Count`

 |
| VALUE | Required | string | Value for the landed cost |
| ACTIVE | Optional | boolean | Status.

*   `true` - active
*   `false` - inactive

 |

`ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO`

For the given warehouse, these parameter values override any replenishment values specified for the item in the Vendor history.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| WAREHOUSEID | Required | string | Warehouse ID for an existing warehouse. |
| ENABLE\_REPLENISHMENT | Optional | boolean | Enable replenishment for this item and warehouse combination.
*   `true` - enable replenishment (default)
*   `false` - do not enable

 |
| REPLENISHMENT\_METHOD | Optional | string | Replenishment method. Specifies how the amount to reorder is calculated.

*   `Reorder point` - base calculation on a specific reorder quantity and optional safety stock quantity
*   `Demand forecast by single value` - base calculation on lead time for the vendor
*   `Demand forecast by fluctuating values` - base calculation on fluctuating forecast for an item

See the information about [replenishment methods and calculations](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Replenishment_methods_and_calculations) in the Sage Intacct product help. (Default: Reorder point or as configured for inventory) |
| SAFETY\_STOCK | Optional | integer | Safety stock. Extra quantity held in inventory to reduce the risk of stock outs due to uncertainty in supply and demand. (Default: 0) |
| MAX\_ORDER\_QTY | Optional | integer | Maximum order quantity allowed in any one order. The value you provide may be affected by the economic order quantity and/or unit of measure set on the vendor. (Default is 0, meaning no maximum) |
| REORDER\_POINT | Optional | integer | Reorder point specifying the quantity of inventory that you don’t want to fall below. When the current net inventory falls to the reorder point plus the safety stock, the item is triggered for reorder. Use blank or positive integers. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. |
| REORDER\_QTY | Optional | integer | Reorder quantity for this item. As an example, if 12 units are needed according to other replenishment calculations, a reorder quantity of 50 would cause the generated purchase order to be for 50. Applies when the REPLENISHMENT\_METHOD is `Reorder point`. (Default is 0, meaning no suggestion) |
| ITEMWAREHOUSEVENDORENTRIES | optional | array of [`ITEMWAREHOUSEVENDORENTRIES`](https://developer.intacct.com/api/inventory-control/items/#update-ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO.ITEMWAREHOUSEVENDORENTRIES) | Vendor Entries. Provides replenishment parameters for this item according to given warehouse and vendor combinations. These parameters override the values for the Vendor entries in the Vendor history. Multiple `ITEMWAREHOUSEVENDORENTRIES` elements may be passed. |

`ITEM.WAREHOUSEINFO.ITEMWAREHOUSEINFO.ITEMWAREHOUSEVENDORENTRIES`

For the given warehouse, these entries override any Vendor entries in Vendor history.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDORID | Required | string | Vendor ID of an existing vendor that ships the item to this warehouse |
| PREFERRED\_VENDOR | Optional | boolean | Preferred vendor status.
*   `true` - designate as preferred
*   `false` - not a preferred vendor

There can only be one preferred vendor. (Default: `true` for the first vendor in the list (the lowest record number), `false` for the others) |
| STOCKNO | Optional | string | Stock number the vendor uses for the item |
| LEAD\_TIME | Optional | string | Lead time in days when ordering this particular item. Valid values are blank, 0, and positive integers. (Default: lead time for the vendor) |
| FORECAST\_DEMAND\_IN\_LEAD\_TIME | Optional | integer | Forecast demand in lead time. Specifies the quantity of this item expected to be sold during the lead time. Valid values are blank, 0, and positive integers. Only applicable when the REPLENISHMENT\_METHOD is `Demand forecast by a single value`. |
| ECONOMIC\_ORDER\_QTY | Optional | integer | Economic order quantity. Specifies the number of units per order to minimize the total costs of inventory—such as holding costs and order costs (Default: `1`) |
| MIN\_ORDER\_QTY | Optional | integer | Minimum order quantity allowed (Default: `1`) |
| UOM | Optional | string | Unit of measure that the vendor sells this item in—should match the UOM used for the Purchase Order. (Default: Base unit of the item’s UOM group for inventory replenishment.) |

`ITEM.VENDORINFO.ITEMVENDOR`

These entries apply when there are no corresponding warehouse-specific Vendor entries.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDORID | Required | string | Vendor ID of an existing vendor that ships the item from this warehouse |
| PREFERRED\_VENDOR | Optional | boolean | Preferred vendor status.
*   `true` - designate as preferred
*   `false` - not a preferred vendor

There can only be one preferred vendor. (Default: `true` for the first vendor in the list (the lowest record number), `false` for the others) |
| STOCKNO | Optional | string | Stock number the vendor uses for the item |
| LEAD\_TIME | Optional | string | Lead time in days when ordering this particular item. Valid values are blank, 0, and positive integers. (Default: lead time for the vendor) |
| FORECAST\_DEMAND\_IN\_LEAD\_TIME | Optional | integer | Forecast demand in lead time. Specifies the quantity of this item expected to be sold during the lead time. Valid values are blank, 0, and positive integers. Only applicable when the replenishment method is `Demand forecast by a single value`. |
| ECONOMIC\_ORDER\_QTY | Optional | string | Quantity of units per order to minimize the total costs of inventory—such as holding costs and order costs. (Default: `1`) |
| MIN\_ORDER\_QTY | Optional | integer | Minimum order quantity allowed (Default: `1`) |
| UOM | Optional | string | Unit of measure that the vendor sells this item in—should match the UOM used for the Purchase Order. (Default: Base unit of the item’s UOM group for inventory replenishment) |

* * *

Update an Item (Legacy)
-----------------------

[History](https://developer.intacct.com/api/inventory-control/items/#history-update-item-legacy)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added enablefulfillment |
| 2021 Release 3 | Added densityuom, density |
| 2021 Release 2 | Added weightuom, netweight, lwhuom, length, width, height, thicknessuom, thickness, minimumthickness, maximumthickness, areauom, area, volumeuom, volume, diameteruom, innerdiameter, outerdiameter, durometer, upc12, ean13, safetyitem, restricteditem, compliantitem, condition, engineeringalert, specification1, specification2, specification3, engineeringapproval, qualitycontrolapproval, salesapproval, primarycountryoforigin, brand, subbrand, category, subcategory, catalogref, color, style, size1, size2, giftcard, webenabled, webname, webshortdesc, weblongdesc |
| 2019 Release 4 | Added autoprintlabel |
| 2024 Release 2 | Update option for replenishment method-Demand forecast by statistical account, replace with Demand forecast by fluctuating values |

#### `update_item`

```
<update_item itemid="I1234">
    <name>hello world</name>
</update_item>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | Item ID to update |
| name | Optional | string | Item name |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |
| enable\_bins | Optional | boolean | Bin tracking enabled.
*   `false` - No (default)
*   `true` - Yes

Applicable to inventory or stockable kit item types. |
| enablefulfillment | Optional | boolean | Set to `true` to enable fulfillment for a non-inventory item that you want to be able to include in kits. |
| extended\_description | Optional | string | Extended description |
| productlineid | Optional | string | [`PRODUCTLINEID`](https://developer.intacct.com/api/inventory-control/product-lines/) of the product line that you want to add this product to. |
| substituteid | Optional | string | Substitute item ID |
| ship\_weight | Optional | decimal | Shipping weight |
| taxable | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. |
| standard\_cost | Optional | currency | Standard cost |
| base\_price | Optional | currency | Base price |
| glgroup | Optional | string | Item GL group name |
| note | Optional | string | Note |
| inventory\_precision | Optional | integer | Inventory unit cost precision |
| purchasing\_precision | Optional | integer | Purchasing unit cost precision |
| sales\_precision | Optional | integer | Sales unit cost precision |
| upc | Optional | string | UPC |
| hasstartenddates | Optional | boolean | Item has start and end dates. Use `false` for No, `true` for Yes. |
| term\_period | Optional | string | Periods measured in.

*   `Days`
*   `Weeks`
*   `Months`
*   `Years`

 |
| defaultnoofperiods | Optional | integer | Number of periods |
| computepriceforshortterm | Optional | boolean | Prorate price allowed. Use `false` for No, `true` for Yes. |
| itaxgroup | Optional | string | Item tax group name. |
| revenue\_posting | Optional | string | Kit revenue posting. Use `Component Level` or `Kit Level`. |
| vsoecategory | Optional | string | VSOE category. Use `Product - Specified`, `Software`, `Product - Unspecified`, `Upgrade - Unspecified`, `Upgrade - Specified`, `Services`, or `Post Contract Support(PCS)`. |
| vsoedlvrstatus | Optional | string | VSOE default delivery status. Use `Delivered` or `Undelivered`. |
| vsoerevdefstatus | Optional | string | VSOE default deferral status. Use `Defer until item is delivered` or `Defer bundle until item is delivered`. |
| incomeaccount | Optional | string | Revenue GL account number |
| invaccount | Optional | string | Inventory GL account number |
| expenseaccount | Optional | string | Expense GL account number |
| cogsaccount | Optional | string | COGS GL account number |
| offsetoeglaccount | Optional | string | AR GL account number |
| offsetpoglaccount | Optional | string | AP GL account number |
| defrevaccount | Optional | string | Deferred revenue GL account number |
| uomgrp | Optional | string | Unit of measure |
| customfields | Optional | array of `customfield` | Custom fields |
| autoprintlabel | Optional | boolean | Auto print label. This parameter is used to trigger an integrated third-party tool that creates scanner labels. Use `true` to print labels, `false` otherwise. (Default: `false`) |
| weightuom | Optional | string | Unit of measure for weight values. Required when `netweight` is specified for an item. |
| netweight | Optional | integer | Actual weight of the base item. Must be less than `ship_weight`. |
| lwhuom  
length  
width  
height | Optional | string  
decimal  
decimal  
decimal | The size of the item, useful for calculating storage bin and shipping box size requirements. Specify the unit of measure and the length, width, and height. You must specify all four values or none. `lwhuom` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| thicknessuom  
thickness  
minimumthickness  
maximumthickness | Optional | string  
decimal  
decimal  
decimal | The thickness of the item, useful for calculating storage bin or shipping box size requirements. Specify the unit of measure, actual thickness, and minimum and maximum thickness. You must specify all four values or none. If the item thickness does not vary, set all three thickness fields to the same value. `thicknessuom` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| areauom  
area | Optional | string  
decimal | The area of the item: unit of measure and area. You must specify both or neither. `areauom` must be set to one of the values defined for the `Area` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| volumeuom  
volume | Optional | string  
decimal | The volume of the item: unit of measure and total volume. You must specify both or neither. `VOLUMEUOM` must be set to one of the values defined for the `Volume` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| diameteruom  
innerdiameter  
outerdiameter | Optional | string  
decimal  
decimal | The diameter of the item: Unit of measure, and inner and outer diameter. You must specify all three or none. `diameteruom` must be set to one of the values defined for the `length` [unit of measure](https://developer.intacct.com/api/inventory-control/units-of-measure/). |
| durometer | Optional | string | Durometer (hardness) measurement of the item. |
| densityuom  
density | Optional | string  
decimal | The density of the item: unit of measure and density value. |
| upc12 | Optional | Integer | UPC-12, the 12-digit Univieral Product Code of the item. |
| ean13 | Optional | integer | EAN-13, the 13-digit International Article Number of the item. |
| safetyitem | Optional | boolean | Use `true` if item is classified as a Safety Item. (Default `false`) |
| restricteditem | Optional | boolean | Use `true` if item is classified as a Restricted Item. (Default `false`) |
| compliantitem | Optional | boolean | Use `true` if item is classified as a Compliant Item. (Default `false`) |
| condition | Optional | string | Condition name or descriptor. |
| engineeringalert | Optional | string | Engineering Alert name or descriptor. |
| specification1 | Optional | string | Specification name/descriptor 1. |
| specification2 | Optional | string | Specification name/descriptor 2. |
| specification3 | Optional | string | Specification name/descriptor 3. |
| engineeringapproval | Optional | boolean | Use `true` if item is approved by Engineering. (Default `false`) |
| qualitycontrolapproval | Optional | boolean | Use `true` if item is approved by Quality Control. (Default `false`) |
| salesapproval | Optional | boolean | Use `true` if item is approved by Sales. (Default `false`) |
| primarycountryoforigin | Optional | string | Primary country of origin, for example “China 75%”. |
| brand | Optional | string | Brand of the item. |
| subbrand | Optional | string | Sub brand of the item. |
| category | Optional | string | Category of the item. |
| subcategory | Optional | string | Sub category of the item. |
| catalogref | Optional | string | Catalog reference for the item. |
| color | Optional | string | Color of the item. |
| style | Optional | string | Style of the item. |
| size1 | Optional | string | Size 1 of the item. |
| size2 | Optional | string | Size 2 of the item. |
| giftcard | Optional | boolean | Use `true` if the item is a gift card (Default `false`) |
| webenabled | Optional | boolean | Use `true` if the item is Web enabled. (Default `false`) |
| webname | Optional | string | Name of the item to appear on the web. |
| webshortdesc | Optional | string | Short description for the web. |
| weblongdesc | Optional | string | Long description for the web. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete an Item
--------------

#### `delete`

```
<delete>
    <object>ITEM</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ITEM` |
| keys | Required | string | Comma-separated list of item `RECORDNO` to delete |

* * *

Delete an Item (Legacy)
-----------------------

#### `delete_item`

```
<delete_item itemid="I1234"></delete_item>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | Item ID to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

