Title: Change Requests

URL Source: https://developer.intacct.com/api/construction/change-requests/

Markdown Content:
*   [Change Requests](https://developer.intacct.com/api/construction/change-requests/#change-requests)
    *   [Get Change Request Object Definition](https://developer.intacct.com/api/construction/change-requests/#get-change-request-object-definition)
    *   [Query and List Change Requests](https://developer.intacct.com/api/construction/change-requests/#query-and-list-change-requests)
    *   [Query and List Change Requests (Legacy)](https://developer.intacct.com/api/construction/change-requests/#query-and-list-change-requests-legacy)
    *   [Get Change Request](https://developer.intacct.com/api/construction/change-requests/#get-change-request)
    *   [Get Change Request by ID](https://developer.intacct.com/api/construction/change-requests/#get-change-request-by-id)
    *   [Create Change Request](https://developer.intacct.com/api/construction/change-requests/#create-change-request)
    *   [Update Change Request](https://developer.intacct.com/api/construction/change-requests/#update-change-request)
    *   [Delete Change Request](https://developer.intacct.com/api/construction/change-requests/#delete-change-request)
*   [Change Request Entries](https://developer.intacct.com/api/construction/change-requests/#change-request-entries)
    *   [Get Change Request Entry Object Definition](https://developer.intacct.com/api/construction/change-requests/#get-change-request-entry-object-definition)
    *   [Query and List Change Request Entries](https://developer.intacct.com/api/construction/change-requests/#query-and-list-change-request-entries)
    *   [Query and List Change Request Entries (Legacy)](https://developer.intacct.com/api/construction/change-requests/#query-and-list-change-request-entries-legacy)
    *   [Get Change Request Entry](https://developer.intacct.com/api/construction/change-requests/#get-change-request-entry)
    *   [Delete Change Request Entry](https://developer.intacct.com/api/construction/change-requests/#delete-change-request-entry)

* * *

The change request object enables construction companies to track project changes by price and cost at the lowest work breakdown structure level (project + task + cost type), and post the changes to the project’s primary estimate.

A change request object typically owns multiple change request entries, where each entry represents a price and/or cost change for the project. You can create individual entries when you create the change request, or you can create a change request without entries and use `update` to add them later.

When you post a change request for the first time, the system creates corresponding estimate entries in the primary project estimate. The change request entries are now _linked_ to the primary project estimate entries. If you update the change request, its entries are re-posted, causing new project estimate entries to be created, updated, or deleted.

A change request must be set to a workflow type other than `none` via the selected change request status in order to post to the project’s primary estimate. If the primary estimate is set to post to a GL budget, the entries from the change request are included.

You can use a [project change order](https://developer.intacct.com/api/construction/project-change-orders/) to group change requests in order to present them to the customer for approval, and ultimately, for billing.

* * *

### Get Change Request Object Definition

#### `lookup`

> List all the fields and relationships for the change request object:

```
<lookup>
    <object>CHANGEREQUEST</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUEST` |

* * *

### Query and List Change Requests

#### `query`

> List information for change requests where the total price is greater than 500.00:

```
<query>
    <object>CHANGEREQUEST</object>
    <select>
        <field>CHANGEREQUESTID</field>
        <field>PROJECTID</field>
        <field>CHANGEREQUESTSTATE</field>
        <field>TOTALCOST</field>
        <field>TOTALPRICE</field>
    </select>
    <filter>
        <greaterthan>
            <field>TOTALPRICE</field>
            <value>500</value>
        </greaterthan>
    </filter>
</query>
```

> List information for change requests linked to the project change order with the ID PCO-66. Includes the sum of the change request prices, which is calculated by the project change order object in the `TOTALPRICE`:

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

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUEST` |
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

### Query and List Change Requests (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CHANGEREQUEST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUEST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Change Request

#### `read`

```
<read>
    <object>CHANGEREQUEST</object>
    <keys>22</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUEST` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the change request to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Change Request by ID

#### `readByName`

```
<readByName>
    <object>CHANGEREQUEST</object>
    <keys>CR-08</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUEST` |
| keys | Required | string | Comma-separated list of ID of the change request to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Change Request

[History](https://developer.intacct.com/api/construction/change-requests/#history-create-change-request)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Added PROJECTCHANGEORDERID |

#### `create`

> Creates a change request with two entries—the first passes the cost to the customer, the second does not (no value for `PRICE`):

```
<create>
    <CHANGEREQUEST>
        <CHANGEREQUESTID>CR-08</CHANGEREQUESTID>
        <PROJECTID>PROJ-005</PROJECTID>
        <CHANGEREQUESTDATE>11/24/2021</CHANGEREQUESTDATE>
        <CHANGEREQUESTENTRIES>
            <CHANGEREQUESTENTRY>
                <PROJECTID>PROJ-005</PROJECTID>
                <TASKID>TSK-RT-0004</TASKID>
                <COSTTYPEID>CT-RT-0003</COSTTYPEID>
                <COST>100</COST>
                <PRICE>120</PRICE>
            </CHANGEREQUESTENTRY>
            <CHANGEREQUESTENTRY>
                <PROJECTID>PROJ-005</PROJECTID>
                <TASKID>TSK-RT-0002</TASKID>
                <COSTTYPEID>CT-RT-0002</COSTTYPEID>
                <COST>200</COST>
            </CHANGEREQUESTENTRY>
        </CHANGEREQUESTENTRIES>
    </CHANGEREQUEST>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUEST | Required | object | Object to create |

`CHANGEREQUEST`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUESTID | Required | string | Unique ID for the change request |
| CHANGEREQUESTTYPENAME | Optional | string | Name of a [change request type](https://developer.intacct.com/api/construction/change-request-types/). Useful for reporting purposes. |
| PROJECTID | Required | string | ID of an existing project |
| CHANGEREQUESTDATE | Required | date | Date for the request in the `mm/dd/yyyy` format |
| CHANGEREQUESTSTATE | Optional | string | State of the change request. Use `Draft` to save without posting (regardless of the status of the change request or the mapped estimate workflow type), or `Posted` to allow posting to proceed as configured. (Default: `Draft`) |
| CHANGEREQUESTSTATUSNAME | Optional | string | Name of a [change request status](https://developer.intacct.com/api/construction/change-request-status/) that is mapped to the workflow type you want for this change request (a workflow type other than `none` enables posting to the primary project estimate). If you omit this parameter, the change request automatically gets a workflow type of `none`. |
| DESCRIPTION | Optional | string | Description of the change request. Use 1000 or fewer characters. |
| PROJECTCHANGEORDERID | Optional | string | Identifier of a [project change order](https://developer.intacct.com/api/construction/project-change-orders/) to link to. Only allowed if the change request state is `Posted`. |
| PCNINTEGRATIONLEVEL | Optional | string | Where this change request integrates with project contracts:
*   `none` - (default) PROJECTCONTRACTID and PROJECTCONTRACTLINEID cannot be used.
*   `project change order` - PROJECTCONTRACTID and PROJECTCONTRACTLINEID are inherited from the project change order.
*   `change request` - PROJECTCONTRACTID and PROJECTCONTRACTLINEID can be used on the change request and will be inherited by the change request entries.
*   `change request entry` - PROJECTCONTRACTID and PROJECTCONTRACTLINEID can be entered on change request entries.

 |
| PROJECTCONTRACTID | Optional | string | `PROJECTCONTRACTID` of the [project contract](https://developer.intacct.com/api/construction/project-contracts/#project-contracts) affected by this change request. Required if PROJECTCONTRACTLINEID is provided. |
| PROJECTCONTRACTLINEID | Optional | string | `PROJECTCONTRACTLINEID` of the specific [project contract line](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines) that is affected by this change request. Required if PROJECTCONTRACTID is provided. |
| COSTEFFECTIVEDATE | Optional | date | Cost effective date of the change request. When posting change request entries to a project estimate, the estimate entry `EFFECTIVEDATE` field will be populated from this value. If the COSTEFFECTIVEDATE is null, the estimate entry `EFFECTIVEDATE` field will be populated with the change request date. |
| PRICEEFFECTIVEDATE | Optional | date | Price effective date of the change request. |
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
| CHANGEREQUESTENTRIES | Optional | array of `CHANGEREQUESTENTRY` | Change request entries |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`CHANGEREQUESTENTRY`

You can provide a specific cost for an entry, or you can specify a quantity and unit cost and the system will calculate the cost. If all three are provided, cost is used. Likewise, you can provide a specific price for an entry, or you can specify a quantity and unit price and the system will calculate the price. If all three are provided, price is used.

If a change should not be billed to the customer, only capture the cost for the entry. To pass the cost onto the customer, use the same amount for cost and price.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROJECTID | Required | string | ID of a project, either the same project specified on the header or one of its descendants. A descendant can only be specified if it has the same customer as the parent project and either the same location as the parent or a descendant of that location. |
| TASKID | Optional | string | Task ID. Required if you specify production units. |
| COSTTYPEID | Optional | string | Cost type ID |
| ITEMID | Optional | string | Item ID |
| QTY | Optional | decimal | Quantity |
| UNITCOST | Optional | currency | Unit cost, also known as unit rate |
| COST | Optional | currency | Cost of the entry. If not supplied, the system can calculate this value using quantity times unit cost. |
| UNITPRICE | Optional | currency | Unit price |
| PRICE | Optional | currency | Price of the entry. If not supplied, the system can calculate this value using quantity times unit price. |
| PRICEMARKUPPERCENT | Optional | currency | Markup percent for the entry |
| PRICEMARKUPAMOUNT | Optional | currency | Markup amount to add to the price of the entry. If not supplied, the system can calculate this value using the price and markup percent. The sum of the price and price markup amount is the value for the read-only line price (`LINEPRICE`) parameter. |
| PRODUCTIONUNITS | Optional | numeric | Number of production units, which are units that track several inputs of cost (such as for material, labor, equipment). When specifying production units, you must also provide a task ID, from which the production unit description, if present, is inherited. |
| EUOM | Optional | string | External unit of measure. Free form field with 200 or fewer characters. |
| MEMO | Optional | string | Memo for the entry. Use 2000 or fewer characters. |
| ACCOUNTNO | Optional | string | GL account number to use when posting this change request (if you want to override the account number on the cost type for this entry). Your company must be configured to allow this override. Note that an account number is needed when the specified project ID has a primary estimate that posts to the GL budget, and the [change request status](https://developer.intacct.com/api/construction/change-request-status/) is set to a value other than `none`. |
| PROJECTCONTRACTID | Optional | string | `PROJECTCONTRACTID` of the [project contract](https://developer.intacct.com/api/construction/project-contracts/#project-contracts) affected by this change request entry. Required if PROJECTCONTRACTLINEID is provided. |
| PROJECTCONTRACTLINEID | Optional | string | `PROJECTCONTRACTLINEID` of the specific [project contract line](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines) that is affected by this change request entry. Required if PROJECTCONTRACTID is provided. |
| DEPARTMENTID | Optional | string | Department ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CLASSID | Optional | string | Class ID |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update Change Request

[History](https://developer.intacct.com/api/construction/change-requests/#history-update-change-request)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Added PROJECTCHANGEORDERID |

You can update a change request even if it has already posted.

When you update a posted change request, the system re-posts its entries, which can result in the addition, modification, or deletion of entries in the linked primary project estimate. If that project estimate previously posted to the GL, the system re-posts it using the updated entries.

#### `update`

> Updates a change request to specify a change request status:

```
<update>
    <CHANGEREQUEST>
        <RECORDNO>211</RECORDNO>
        <CHANGEREQUESTSTATUSNAME>Approved Changes</CHANGEREQUESTSTATUSNAME>
    </CHANGEREQUEST>
</update>
```

> Updates a change request to update one entry by record number and add a new entry:

```
<update>
    <CHANGEREQUEST>
        <CHANGEREQUESTID>CR-08</CHANGEREQUESTID>
        <CHANGEREQUESTENTRIES>
            <CHANGEREQUESTENTRY>
                <RECORDNO>120</RECORDNO>
                <PRICE>130</PRICE>
                <MEMO>Entry was updated</MEMO>
            </CHANGEREQUESTENTRY>
            <CHANGEREQUESTENTRY>
                <PROJECTID>PROJ-008</PROJECTID>
                <COST>300</COST>
                <PRICE>350</PRICE>
                <MEMO>Entry was added</MEMO>
            </CHANGEREQUESTENTRY>
        </CHANGEREQUESTENTRIES>
    </CHANGEREQUEST>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUEST | Required | object | Object to update |

`CHANGEREQUEST`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CHANGEREQUESTID | Optional | string | Unique ID of the change request to update. Required if not using `RECORDNO`. |
| RECORDNO | Optional | integer | `RECORDNO` of the change request to update. Required if not using `CHANGEREQUESTID`. |
| CHANGEREQUESTTYPENAME | Optional | string | Name of a [change request type](https://developer.intacct.com/api/construction/change-request-types/). Useful for reporting purposes. |
| PROJECTID | Optional | string | ID of an existing project |
| CHANGEREQUESTDATE | Optional | date | Date for the request in the `mm/dd/yyyy` format |
| CHANGEREQUESTSTATE | Optional | string | State of the change request. Use `Draft` to save without posting (regardless of the status of the change request or the mapped estimate workflow type), or `Posted` to allow posting to proceed as configured. You cannot change a `Posted` change request back to `Draft`. |
| CHANGEREQUESTSTATUSNAME | Optional | string | Name of a [change request status](https://developer.intacct.com/api/construction/change-request-status/) that is mapped to the workflow type you want for this change request (a workflow type other than `none` enables posting to the primary project estimate). If you omit this parameter, the change request automatically gets a workflow type of `none`. |
| DESCRIPTION | Optional | string | Description of the change request. Use 1000 or fewer characters. |
| PROJECTCHANGEORDERID | Optional | string | Identifier of a [project change order](https://developer.intacct.com/api/construction/project-change-orders/) to link to. Only allowed if the change request state is `Posted`. Pass an empty project change order ID to delete it. |
| PCNINTEGRATIONLEVEL | Optional | string | Where this change request integrates with project contracts:
*   `none` - (default) PROJECTCONTRACTID and PROJECTCONTRACTLINEID cannot be used.
*   `project change order` - PROJECTCONTRACTID and PROJECTCONTRACTLINEID are inherited from the project change order.
*   `change request` - PROJECTCONTRACTID and PROJECTCONTRACTLINEID can be used on the change request and will be inherited by the change request entries.
*   `change request entry` - PROJECTCONTRACTID and PROJECTCONTRACTLINEID can be entered on change request entries.

 |
| PROJECTCONTRACTID | Optional | string | `PROJECTCONTRACTID` of the [project contract](https://developer.intacct.com/api/construction/project-contracts/#project-contracts) affected by this change request. Required if PROJECTCONTRACTLINEID is provided. |
| PROJECTCONTRACTLINEID | Optional | string | `PROJECTCONTRACTLINEID` of the specific [project contract line](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines) that is affected by this change request. Required if PROJECTCONTRACTID is provided. |
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
| CHANGEREQUESTENTRIES | Optional | array of `CHANGEREQUESTENTRY` | Change request entries |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`CHANGEREQUESTENTRY`

You can provide a specific cost for an entry, or you can specify a quantity and unit cost and the system will calculate the cost. If you provide all three, cost is used. Likewise, you can provide a specific price for an entry, or you can specify a quantity and unit price and the system will calculate the price. If you provide all three, price is used.

If a change should not be billed to the customer, only capture the cost for the entry. To pass the cost onto the customer, use the same amount for cost and price.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | `RECORDNO` of a change request entry to update. Omit to create a new entry. |
| PROJECTID | Optional | string | ID of a project, either the same project specified on the header or one of its descendants. Required when creating a new change request entry. A descendant can only be specified if it has the same customer as the parent project and either the same location as the parent or a descendant of that location. |
| TASKID | Optional | string | Task ID. Required if you specify production units. |
| COSTTYPEID | Optional | string | Cost type ID |
| ITEMID | Optional | string | Item ID |
| QTY | Optional | decimal | Quantity |
| UNITCOST | Optional | currency | Unit cost, also known as unit rate |
| COST | Optional | currency | Cost of the entry. If not supplied, the system can calculate this value using quantity times unit cost. |
| UNITPRICE | Optional | currency | Unit price |
| PRICE | Optional | currency | Price of the entry. If not supplied, the system can calculate this value using quantity times unit price. |
| PRICEMARKUPPERCENT | Optional | currency | Markup percent for the entry |
| PRICEMARKUPAMOUNT | Optional | currency | Markup amount to add to the price of the entry. If not supplied, the system can calculate this value using the price and markup percent. The sum of the price and price markup amount is the value for the read-only line price (`LINEPRICE`) parameter. |
| PRODUCTIONUNITS | Optional | numeric | Number of production units, which are units that track several inputs of cost (such as for material, labor, equipment). When specifying production units, you must also provide a task ID, from which the production unit description, if present, is inherited. |
| EUOM | Optional | string | External unit of measure. Free form field with 200 or fewer characters. |
| MEMO | Optional | string | Memo for the entry. Use 2000 or fewer characters. |
| ACCOUNTNO | Optional | string | GL account number to use when posting this change request (if you want to override the account number on the cost type for this entry). Your company must be configured to allow this override. Note that an account number is needed when the specified project ID has a primary estimate that posts to the GL budget, and the [change request status](https://developer.intacct.com/api/construction/change-request-status/) is set to a value other than `none`. |
| PROJECTCONTRACTID | Optional | string | `PROJECTCONTRACTID` of the [project contract](https://developer.intacct.com/api/construction/project-contracts/#project-contracts) affected by this change request entry. Required if PROJECTCONTRACTLINEID is provided. |
| PROJECTCONTRACTLINEID | Optional | string | `PROJECTCONTRACTLINEID` of the specific [project contract line](https://developer.intacct.com/api/construction/project-contracts/#project-contract-lines) that is affected by this change request entry. Required if PROJECTCONTRACTID is provided. |
| DEPARTMENTID | Optional | string | Department ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CLASSID | Optional | string | Class ID |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Change Request

You can delete a change request even if it has already posted.

When you delete a change request that already posted, any linked project estimate entries are also deleted, and project estimates are updated accordingly. If the primary project estimate previously posted to the GL, the system re-posts it using the remaining estimate entries.

#### `delete`

```
<delete>
    <object>CHANGEREQUEST</object>
    <keys>211</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUEST` |
| keys | Required | integer | `RECORDNO` of the `CHANGEREQUEST` to delete |

* * *

Change Request Entries
----------------------

### Get Change Request Entry Object Definition

#### `lookup`

> List all the fields and relationships for the change request entry object:

```
<lookup>
    <object>CHANGEREQUESTENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTENTRY` |

* * *

### Query and List Change Request Entries

#### `query`

> Lists information about change request entries for the given project:

```
<query>
    <object>CHANGEREQUESTENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>PJESTIMATEID</field>
        <field>PROJECTID</field>
        <field>COST</field>
    </select>
    <filter>
        <equalto>
            <field>PROJECTID</field>
            <value>PROJ-005</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTENTRY` |
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

### Query and List Change Request Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CHANGEREQUESTENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Change Request Entry

#### `read`

```
<read>
    <object>CHANGEREQUESTENTRY</object>
    <keys>22</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the change request entry to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Delete Change Request Entry

#### `delete`

```
<delete>
    <object>CHANGEREQUESTENTRY</object>
    <keys>177</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CHANGEREQUESTENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the change request entry to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

