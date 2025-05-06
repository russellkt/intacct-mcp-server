Title: Project Change Orders

URL Source: https://developer.intacct.com/api/construction/project-change-orders/

Markdown Content:
*   [Get Project Change Order Object Definition](https://developer.intacct.com/api/construction/project-change-orders/#get-project-change-order-object-definition)
*   [Query and List Project Change Orders](https://developer.intacct.com/api/construction/project-change-orders/#query-and-list-project-change-orders)
*   [Query and List Project Change Orders (Legacy)](https://developer.intacct.com/api/construction/project-change-orders/#query-and-list-project-change-orders-legacy)
*   [Get Project Change Order](https://developer.intacct.com/api/construction/project-change-orders/#get-project-change-order)
*   [Get Project Change Order by ID](https://developer.intacct.com/api/construction/project-change-orders/#get-project-change-order-by-id)
*   [Create Project Change Order](https://developer.intacct.com/api/construction/project-change-orders/#create-project-change-order)
*   [Update Project Change Order](https://developer.intacct.com/api/construction/project-change-orders/#update-project-change-order)
*   [Delete Project Change Order](https://developer.intacct.com/api/construction/project-change-orders/#delete-project-change-order)

* * *

You can use project change orders to group change requests in order to present them to the customer for approval, and ultimately, for billing. Your project change order can be associated with a [change request status](https://developer.intacct.com/api/construction/change-request-status/), which is a user-defined object that is shared by change orders and change requests.

After creating a project change order, you can create links from one or more change requests to that change order. To do this, provide the project change order ID when [creating](https://developer.intacct.com/api/construction/change-requests/#create-change-request) or [updating](https://developer.intacct.com/api/construction/change-requests/#update-change-request) change requests.

When you get a project change order, the sum of the total cost for all the linked change requests is provided in the response. This is also true for the total price.

* * *

Get Project Change Order Object Definition
------------------------------------------

#### `lookup`

> List all the fields and relationships for the project change order object:

```
<lookup>
    <object>PROJECTCHANGEORDER</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCHANGEORDER` |

* * *

Query and List Project Change Orders
------------------------------------

#### `query`

> List information for project change orders where the total cost is greater than 1000:

```
<query>
    <object>PROJECTCHANGEORDER</object>
    <select>
        <field>PROJECTCHANGEORDERID</field>
        <field>TOTALCOST</field>
        <field>CUSTOMERID</field>
    </select>
    <filter>
        <greaterthan>
            <field>TOTALCOST</field>
            <value>1000</value>
        </greaterthan>
    </filter>
</query>
```

> List information for **change requests** linked to the project change order with the given ID:

```
<query>
    <object>CHANGEREQUEST</object>
    <select>
        <field>CHANGEREQUESTID</field>
        <field>PROJECTCHANGEORDERID</field>
        <field>PJCHANGEORDER.TOTALPRICE</field>
        <field>TOTALPRICE</field>
    </select>
    <filter>
        <equalto>
            <field>PROJECTCHANGEORDERID</field>
            <value>PCO-66</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCHANGEORDER` |
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

Query and List Project Change Orders (Legacy)
---------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>PROJECTCHANGEORDER</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCHANGEORDER` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get Project Change Order
------------------------

#### `read`

```
<read>
    <object>PROJECTCHANGEORDER</object>
    <keys>66</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCHANGEORDER` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the project change order to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Project Change Order by ID
------------------------------

#### `readByName`

```
<readByName>
    <object>PROJECTCHANGEORDER</object>
    <keys>PCO-66</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCHANGEORDER` |
| keys | Required | string | Comma-separated list of ID of the project change order to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Project Change Order
---------------------------

[History](https://developer.intacct.com/api/construction/project-change-orders/#history-create-change-order)

| Release | Changes |
| --- | --- |
| 2024 Release 3 | Changed ITEMID to optional |
| 2022 Release 2 | Added PROJECTCONTRACTID and PROJECTCONTRACTLINEID |
| 2023 Release 1 | Removed the restriction that only draft project change orders are allowed |

#### `create`

> Creates a project change order:

```
<create>
    <PROJECTCHANGEORDER>
        <PROJECTCHANGEORDERID>PCO-66</PROJECTCHANGEORDERID>
        <PROJECTID>3</PROJECTID>
        <ITEMID>Design</ITEMID>
        <PROJECTCHANGEORDERDATE>6/30/2024</PROJECTCHANGEORDERDATE>
        <CHANGEREQUESTSTATUSNAME>Approved Changes</CHANGEREQUESTSTATUSNAME>
    </PROJECTCHANGEORDER>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCHANGEORDER | Required | object | Object type to create. |

`PROJECTCHANGEORDER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCHANGEORDERID | Required | string | Unique identifier for the project change order. (This parameter is optional if auto numbering is configured in your company, but you can still overwrite it.) |
| PROJECTID | Required | string | ID of an existing project |
| ITEMID | Optional | string | Billing item ID. Must be active and non-inventory. |
| PROJECTCHANGEORDERDATE | Required | string | Date for the project change order in the `mm/dd/yyyy` format |
| DESCRIPTION | Optional | string | Description for the project change order. |
| PROJECTCHANGEORDERSTATE | Optional | string | State of the project change order.
*   `Draft` (default)
*   `Posted`

Does not affect the state of linked change requests. |
| CHANGEREQUESTSTATUSNAME | Optional | string | Name of a [change request status](https://developer.intacct.com/api/construction/change-request-status/) to be inherited by linked change requests. |
| PROJECTCONTRACTID | Optional | string | `PROJECTCONTRACTID` of the [project contract](https://developer.intacct.com/api/construction/project-contracts/#project-contracts) affected by this change order. Required if PROJECTCONTRACTLINEID is provided. |
| PROJECTCONTRACTLINEID | Optional | string | `PROJECTCONTRACTLINEID` of the specific [project contract line](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines) that is affected by this change order. Required if PROJECTCONTRACTID is provided. |
| PRICEEFFECTIVEDATE | Optional | date | Price effective date of the project change order. Setting a value or null for this field will automatically set the PRICEEFFECTIVEDATE field on all linked change requests. |
| SCOPE | Optional | string | Details about the expected scope of work for the change request. Use 4000 or fewer characters. |
| INCLUSIONS | Optional | string | Details related to items that are explicitly included in the terms of this change request. Use 4000 or fewer characters. |
| EXCLUSIONS | Optional | string | Details related to items that are explicitly excluded in the terms of this change request. Use 4000 or fewer characters. |
| TERMS | Optional | string | Additional terms or performance obligations. Use 4000 or fewer characters. |
| SCHEDULEDSTARTDATE | Optional | date | Scheduled start date in the `mm/dd/yyyy` format |
| ACTUALSTARTDATE | Optional | date | Actual start date in the `mm/dd/yyyy` format |
| SCHEDULEDCOMPLETIONDATE | Optional | date | Original scheduled date for completion of the work in the `mm/dd/yyyy` format |
| REVISEDCOMPLETIONDATE | Optional | date | Revised completion date for the work (caused by changes) in the `mm/dd/yyyy` format. |
| SUBSTANTIALCOMPLETIONDATE | Optional | date | Date the work is considered substantially complete in the `mm/dd/yyyy` format. Typically used as a milestone to identify when payment obligations are due. |
| ACTUALCOMPLETIONDATE | Optional | date | Date the work is actually complete in the `mm/dd/yyyy` format |
| NOTICETOPROCEED | Optional | date | Date when a formal notice to proceed was given in the `mm/dd/yyyy` format |
| RESPONSEDUE | Optional | date | Date when a response is expected from an external party in the `mm/dd/yyyy` format |
| EXECUTEDON | Optional | date | Date the related contract document was formally executed in the `mm/dd/yyyy` format |
| SCHEDULEIMPACT | Optional | string | Details about any impacts on the current schedule. Use 100 or fewer characters. |
| INTERNALREFNO | Optional | string | Specifies an internal reference ID |
| INTERNALINITIATEDBYKEY | Optional | integer | Record number of the employee who initiated the change request |
| INTERNALINITIATEDBY | Optional | string | ID of the employee who initiated the change request |
| INTERNALINITIATEDBYNAME | Optional | string | Name of the employee who initiated the change request |
| INTERNALVERBALBYKEY | Optional | integer | Record number of of the employee who verbally agreed to the change request |
| INTERNALVERBALBY | Optional | string | ID of the employee who verbally agreed to the change request |
| INTERNALVERBALBYNAME | Optional | string | Name of the employee who verbally agreed to the change request |
| INTERNALISSUEDBYKEY | Optional | integer | Record number of the employee who issued the change request |
| INTERNALISSUEDBY | Optional | string | ID of the employee who issued the change request |
| INTERNALISSUEDBYNAME | Optional | string | Name of the employee who issued the change request |
| INTERNALISSUEDON | Optional | date | Date this change request was internally issued in the `mm/dd/yyyy` format |
| INTERNALAPPROVEDBYKEY | Optional | integer | Record number of the employee who internally approved the change request. |
| INTERNALAPPROVEDBY | Optional | string | ID of the employee who internally approved the change request |
| INTERNALAPPROVEDBYNAME | Optional | string | Name of the employee who internally approved the change request |
| INTERNALAPPROVEDON | Optional | date | Date this change request was internally approved in the `mm/dd/yyyy` format |
| INTERNALSIGNEDBYKEY | Optional | integer | Record number of the employee who signed for the change request |
| INTERNALSIGNEDBY | Optional | string | ID of the employee who signed for the change request |
| INTERNALSIGNEDBYNAME | Optional | string | Name of the employee who signed for the change request |
| INTERNALSIGNEDON | Optional | date | Date the change request was internally signed in the `mm/dd/yyyy` format. |
| INTERNALSOURCE | Optional | string | Internal source when the change request originated from another document or workflow. Can be an internal or external source. For example, a request for information (RFI) or a project change request. |
| INTERNALSOURCEREFNO | Optional | string | Internal source reference number or ID when the change request originated from another source. Can be an internal or external number. |
| EXTERNALREFNO | Optional | string | External reference number, such as one required by a vendor or customer, for this change request. |
| EXTERNALVERBALBYKEY | Optional | integer | Record number of the contact who verbally agreed to the change request. For example, a customer or vendor contact. |
| EXTERNALVERBALBY | Optional | string | Name of the contact who verbally agreed to the change request. For example, a customer or vendor contact. |
| EXTERNALAPPROVEDBYKEY | Optional | integer | Record number of the contact who approved the change request. For example, a customer or vendor contact. |
| EXTERNALAPPROVEDBY | Optional | string | Name of the contact who approved the change request. For example, a customer or vendor contact. |
| EXTERNALAPPROVEDON | Optional | date | Date the customer or vendor approved the change request in the `mm/dd/yyyy` format |
| EXTERNALSIGNEDBYKEY | Optional | integer | Record number of the contact who signed the change request. For example, a customer or vendor contact. |
| EXTERNALSIGNEDBY | Optional | string | Name of the contact who signed the change request. For example, a customer or vendor contact. |
| EXTERNALSIGNEDON | Optional | date | Date the customer or vendor signed for the change request the `mm/dd/yyyy` format |
| SUPDOCID | Optional | string | Attachments ID |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Project Change Order
---------------------------

[History](https://developer.intacct.com/api/construction/project-change-orders/#history-update-change-order)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added PROJECTCONTRACTID and PROJECTCONTRACTLINEID |
| 2023 Release 1 | Removed the restriction that only draft project change orders are allowed |

#### `update`

> Sets the change request status of a project change order to `Approved Changes`:

```
<update>
    <PROJECTCHANGEORDER>
        <PROJECTCHANGEORDERID>PCO-66</PROJECTCHANGEORDERID>
        <CHANGEREQUESTSTATUSNAME>Approved Changes</CHANGEREQUESTSTATUSNAME>
    </PROJECTCHANGEORDER>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTCHANGEORDER | Required | object | Object to update |

`PROJECTCHANGEORDER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | `RECORDNO` of the project change order to update. Required if not using `PROJECTCHANGEORDERID`. |
| PROJECTCHANGEORDERID | Optional | string | Unique identifier for the project change order to update. Required if not using `RECORDNO`. |
| PROJECTID | Optional | string | ID of an existing project |
| ITEMID | Optional | string | Billing item ID. Must be active and non-inventory. |
| PROJECTCHANGEORDERDATE | Optional | string | Date for the project change order in the `mm/dd/yyyy` format |
| DESCRIPTION | Optional | string | Description for the project change order. |
| PROJECTCHANGEORDERSTATE | Optional | string | State of the project change order, either `Draft` or `Posted`. Does not affect the state of linked change requests. You cannot change the state from `Posted` to `Draft`. (Default: `Draft`) |
| CHANGEREQUESTSTATUSNAME | Optional | string | Name of a [change request status](https://developer.intacct.com/api/construction/change-request-status/) to be inherited by linked change requests. |
| PROJECTCONTRACTID | Optional | string | `PROJECTCONTRACTID` of the [project contract](https://developer.intacct.com/api/construction/project-contracts/#project-contracts) affected by this change order. Required if PROJECTCONTRACTLINEID is provided. |
| PROJECTCONTRACTLINEID | Optional | string | `PROJECTCONTRACTLINEID` of the specific [project contract line](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines) that is affected by this change order. Required if PROJECTCONTRACTID is provided. |
| PRICEEFFECTIVEDATE | Optional | date | Price effective date of the project change order. Updating this field will automatically update the PRICEEFFECTIVEDATE field on all linked change requests. |
| SCOPE | Optional | string | Details about the expected scope of work for the change request. Use 4000 or fewer characters. |
| INCLUSIONS | Optional | string | Details related to items that are explicitly included in the terms of this change request. Use 4000 or fewer characters. |
| EXCLUSIONS | Optional | string | Details related to items that are explicitly excluded in the terms of this change request. Use 4000 or fewer characters. |
| TERMS | Optional | string | Additional terms or performance obligations. Use 4000 or fewer characters. |
| SCHEDULEDSTARTDATE | Optional | date | Scheduled start date in the `mm/dd/yyyy` format |
| ACTUALSTARTDATE | Optional | date | Actual start date in the `mm/dd/yyyy` format |
| SCHEDULEDCOMPLETIONDATE | Optional | date | Original scheduled date for completion of the work in the `mm/dd/yyyy` format |
| REVISEDCOMPLETIONDATE | Optional | date | Revised completion date for the work (caused by changes) in the `mm/dd/yyyy` format. |
| SUBSTANTIALCOMPLETIONDATE | Optional | date | Date the work is considered substantially complete in the `mm/dd/yyyy` format. Typically used as a milestone to identify when payment obligations are due. |
| ACTUALCOMPLETIONDATE | Optional | date | Date the work is actually complete in the `mm/dd/yyyy` format |
| NOTICETOPROCEED | Optional | date | Date when a formal notice to proceed was given in the `mm/dd/yyyy` format |
| RESPONSEDUE | Optional | date | Date when a response is expected from an external party in the `mm/dd/yyyy` format |
| EXECUTEDON | Optional | date | Date the related contract document was formally executed in the `mm/dd/yyyy` format |
| SCHEDULEIMPACT | Optional | string | Details about any impacts on the current schedule. Use 100 or fewer characters. |
| INTERNALREFNO | Optional | string | Specifies an internal reference ID |
| INTERNALINITIATEDBYKEY | Optional | integer | Record number of the employee who initiated the change request |
| INTERNALINITIATEDBY | Optional | string | ID of the employee who initiated the change request |
| INTERNALINITIATEDBYNAME | Optional | string | Name of the employee who initiated the change request |
| INTERNALVERBALBYKEY | Optional | integer | Record number of of the employee who verbally agreed to the change request |
| INTERNALVERBALBY | Optional | string | ID of the employee who verbally agreed to the change request |
| INTERNALVERBALBYNAME | Optional | string | Name of the employee who verbally agreed to the change request |
| INTERNALISSUEDBYKEY | Optional | integer | Record number of the employee who issued the change request |
| INTERNALISSUEDBY | Optional | string | ID of the employee who issued the change request |
| INTERNALISSUEDBYNAME | Optional | string | Name of the employee who issued the change request |
| INTERNALISSUEDON | Optional | date | Date this change request was internally issued in the `mm/dd/yyyy` format |
| INTERNALAPPROVEDBYKEY | Optional | integer | Record number of the employee who internally approved the change request. |
| INTERNALAPPROVEDBY | Optional | string | ID of the employee who internally approved the change request |
| INTERNALAPPROVEDBYNAME | Optional | string | Name of the employee who internally approved the change request |
| INTERNALAPPROVEDON | Optional | date | Date this change request was internally approved in the `mm/dd/yyyy` format |
| INTERNALSIGNEDBYKEY | Optional | integer | Record number of the employee who signed for the change request |
| INTERNALSIGNEDBY | Optional | string | ID of the employee who signed for the change request |
| INTERNALSIGNEDBYNAME | Optional | string | Name of the employee who signed for the change request |
| INTERNALSIGNEDON | Optional | date | Date the change request was internally signed in the `mm/dd/yyyy` format. |
| INTERNALSOURCE | Optional | string | Internal source when the change request originated from another document or workflow. Can be an internal or external source. For example, a request for information (RFI) or a project change request. |
| INTERNALSOURCEREFNO | Optional | string | Internal source reference number or ID when the change request originated from another source. Can be an internal or external number. |
| EXTERNALREFNO | Optional | string | External reference number, such as one required by a vendor or customer, for this change request. |
| EXTERNALVERBALBYKEY | Optional | integer | Record number of the contact who verbally agreed to the change request. For example, a customer or vendor contact. |
| EXTERNALVERBALBY | Optional | string | Name of the contact who verbally agreed to the change request. For example, a customer or vendor contact. |
| EXTERNALAPPROVEDBYKEY | Optional | integer | Record number of the contact who approved the change request. For example, a customer or vendor contact. |
| EXTERNALAPPROVEDBY | Optional | string | Name of the contact who approved the change request. For example, a customer or vendor contact. |
| EXTERNALAPPROVEDON | Optional | date | Date the customer or vendor approved the change request in the `mm/dd/yyyy` format |
| EXTERNALSIGNEDBYKEY | Optional | integer | Record number of the contact who signed the change request. For example, a customer or vendor contact. |
| EXTERNALSIGNEDBY | Optional | string | Name of the contact who signed the change request. For example, a customer or vendor contact. |
| EXTERNALSIGNEDON | Optional | date | Date the customer or vendor signed for the change request the `mm/dd/yyyy` format |
| SUPDOCID | Optional | string | Attachments ID |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Project Change Order
---------------------------

#### `delete`

```
<delete>
    <object>PROJECTCHANGEORDER</object>
    <keys>66</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `PROJECTCHANGEORDER` |
| keys | Required | integer | `RECORDNO` of the project change order to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

