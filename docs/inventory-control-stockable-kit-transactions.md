Title: Stockable Kit Transactions

URL Source: https://developer.intacct.com/api/inventory-control/stockable-kit-transactions/

Markdown Content:
*   [Create a Build Kits Transaction](https://developer.intacct.com/api/inventory-control/stockable-kit-transactions/#create-a-build-kits-transaction)
*   [Create a Disassemble Kits Transaction](https://developer.intacct.com/api/inventory-control/stockable-kit-transactions/#create-a-disassemble-kits-transaction)

* * *

Stockable kit transactions created through the Intacct API describe orders to build or disassemble stockable kits. When stockable kits are built, the inventory of the components in the stockable kit is reduced and the inventory of stockable kits is increased by the number of stockable kits. When stockable kits are disassembled the inventory changes are reversed.

* * *

Create a Build Kits Transaction
-------------------------------

A `Build Kits` transaction is the record of an order to create a specified number of pre-defined stockable kits. You can include different stockable kits in the same transaction as separate `stkittransitem` objects. Each `stkittransitem` object lists the stockable kits that were built and the component items that were used to build the stockable kits, for inventory management and tracking purposes.

#### `create_stkittransaction`

> Request to assemble three cartons of eggs:

```
<create_stkittransaction>
    <transactiontype>Build Kits</transactiontype>
    <datecreated>
        <year>2022</year>
        <month>04</month>
        <day>01</day>
    </datecreated>
    <message>Restock eggs</message>
    <documentno>Eggs-04-01-22</documentno>
    <stkittransitems>
        <stkittransitem>
            <itemid>EGG12</itemid>
            <itemdesc>One dozen egss</itemdesc>
            <warehouseid>W100</warehouseid>
            <quantity>3</quantity>
            <unit>Each</unit>
            <itemdetails>
                <itemdetail>  <!-- cartons to hold the eggs -->
                    <componentid>EggCarton</componentid>
                    <quantity>3</quantity>
                    <lotno>Lot1</lotno>
                    <bin>Bin 20</bin>
                </itemdetail>
                <itemdetail>  <!-- eggs -->
                    <componentid>Eggs</componentid>
                    <quantity>36</quantity>
                    <lotno>03-30-22</lotno>
                    <itemexpiration>
                        <year>2022</year>
                        <month>04</month>
                        <day>30</day>
                    </itemexpiration>
                </itemdetail>
                <itemdetail>  <!-- The resulting stockable kits -->
                    <quantity>3</quantity>
                    <lotno>Lot M</lotno>
                    <bin>Bin R12</bin>
                    <itemexpiration>
                        <year>2022</year>
                        <month>04</month>
                        <day>30</day>
                    </itemexpiration>
                </itemdetail>
            </itemdetails>
        </stkittransitem>
    </stkittransitems>
</create_stkittransaction>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| transactiontype | Required | string | Pre-defined [transaction definition](https://developer.intacct.com/api/inventory-control/inventory-transaction-definitions/) to create a build kit transaction. Use `Build Kits` |
| datecreated | Required | [object](https://developer.intacct.com/api/inventory-control/stockable-kit-transactions/#create_stkittransaction-datecreated) | Transaction date. |
| documentno | Optional | string | Document number to identify this transaction. Leave blank if transaction numbering is enabled in the transaction definition. The document number will be appended to the transaction type to create the `DOCID`, such as `Build Kits-60`. |
| referenceno | Optional | string | Reference number that can be used to search or sort transactions. You can use purchase order numbers or request for quote numbers to help track build kit transactions. |
| message | Optional | string | Message that you want to appear on the transaction. |
| externalid | Optional | string | External ID |
| customfields | Optional | array of `customfield` | Custom fields |
| stkittransitems | Required | array of [`stkittransitem`](https://developer.intacct.com/api/inventory-control/stockable-kit-transactions/#create_stkittransaction-stkittransitem) | Transaction lines showing the stockable kits that were built. Must have at least 1. |

`create_stkittransaction.datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`create_stkittransaction.stkittransitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| itemid | Required | string | `ITEMID` of the stockable kit that was built. |
| itemdesc | Optional | string | Stockable kit description. |
| warehouseid | Required | string | `WAREHOUSEID` of the [warehouse](https://developer.intacct.com/api/inventory-control/warehouses/) where the newly built stockable kits are located. There must be sufficient inventory at the specified warehouse to build the stockable kits. |
| quantity | Required | number | Number of stockable kits that were built. |
| unit | Optional | string | Unit of measure to base quantity off, such as `Each`, `Pair`, or `Dozen`. |
| locationid | Optional | string | `LOCATIONID` of a [location](https://developer.intacct.com/api/company-console/locations/). |
| departmentid | Optional | string | `DEPARTMENTID` of a [department](https://developer.intacct.com/api/company-console/departments/). |
| itemdetails | Optional | array of `itemdetail` | Inventory tracking information for components and the stockable kits. |
| customfields | Optional | `customfield[0...n]` | Custom fields. |

`create_stkittransaction.stkittransitem.itemdetail`

An `itemdetail` object contains inventory tracking information for the stockable kit or for each tracked component. You do not need to create an `itemdetail` object for any components that do not have inventory tracking enabled (serial number, bin, lot, or expiration.).

*   Tracking information for components reflects the source inventory or locations that the components came from.
*   Tracking information for the stockable kits reflects how the stockable kits will be tracked and where they will be stocked.

You must create an `itemdetail` object for each tracked source and destination. For example:

*   If the entire quantity of a tracked component comes from the same bin or lot, you can create one `itemdetail` object for that component.
*   If you want to pull components from multiple bins or lots, or place the built stockable kits in multiple bins or lots, you must create separate `itemdetail` objects for each source or destination.
*   If you are tracking the serial numbers of components or of the built stockable kits, you must create one `itemdetail` object for each serial number.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| componentid | Optional | string | `ITEMID` of the [item or kit](https://developer.intacct.com/api/inventory-control/items/) that is a component in the stockable kit.
*   You must include this parameter for each component that you want to track.
*   Do not include this parameter for the stockable kit.

 |
| quantity | Optional | integer | Quantity of the item or stockable kit.

*   If components are drawn from different lots or bins, create separate `itemdetail` objects for each location and set `quantity` to the number of items from each.
*   Set to `1` for serial number tracking.

 |
| serialno | Optional | string | Serial number of the component item or stockable kit, or the serial number to be applied to the finished stockable kit. Required if serial number tracking is enabled for the item or stockable kit. |
| lotno | Optional | string | Lot number. `ENABLE_LOT_CATEGORY` must be `true` for the item. |
| bin | Optional | string | `BINID` of the [bin](https://developer.intacct.com/api/inventory-control/bins/) where the component is stored , or where the stockable kit will be stored. Bin tracking must be enabled. |
| itemexpiration | Optional | [object](https://developer.intacct.com/api/inventory-control/stockable-kit-transactions/#create_stkittransaction-stkittransitem.itemdetail.itemexpiration) | Expiration date of the component or of the newly created stockable kit. Expiration tracking must be enabled. |

`create_stkittransaction-stkittransitem.itemdetail.itemexpiration`

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

Create a Disassemble Kits Transaction
-------------------------------------

A `Disassemble Kits` transaction will reverse a previous build kit transaction. The inventory of built stockable kits will be reduced and the inventory of components will be increased based on the number of items specified in the build kit transaction. You don’t need to specify `stkittransitems` or `itemdetails`, as all of that information will be extracted from the build kit transaction.

#### `create_stkittransaction`

> Disassemble the stockable kits created in the previous example:

```
<create_stkittransaction>
    <transactiontype>Disassemble Kits</transactiontype>
    <datecreated>
        <year>2022</year>
        <month>04</month>
        <day>11</day>
    </datecreated>
    <createdfrom>Build Kits-Eggs-04-01-22</createdfrom>
    <message>Unstock eggs</message>
</create_stkittransaction>
```

#### `Parameters`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| transactiontype | Required | string | Pre-defined [transaction definition](https://developer.intacct.com/api/inventory-control/inventory-transaction-definitions/) to create a disassemble kit transaction. Use `Disassemble Kits` |
| datecreated | Required | [object](https://developer.intacct.com/api/inventory-control/stockable-kit-transactions/#create_stkittransaction-datecreated) | Transaction date. |
| createdfrom | Required | string | The `DOCID` from a previous Build Kit transaction. |
| documentno | Optional | string | Document number to identify this transaction. Leave blank if transaction numbering is enabled in the transaction definition. The document number will be appended to the transaction type to create the `DOCID`, such as `Build Kits-60`. |
| referenceno | Optional | string | Reference number that can be used to search or sort transactions. You can use purchase order numbers or request for quote numbers to help track build kit transactions. |
| message | Optional | string | Message that you want to include in the transaction. It appears in the PDF file when you print the build transaction. |
| externalid | Optional | string | External ID |
| customfields | Optional | array of `customfield` | Custom fields |

`create_stkittransaction.datecreated`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

