Title: Advanced Audit Trails

URL Source: https://developer.intacct.com/api/company-console/advanced-audit-trails/

Markdown Content:
*   [Get Advanced Audit Trails Object Definition](https://developer.intacct.com/api/company-console/advanced-audit-trails/#get-advanced-audit-trails-object-definition)
*   [Query and List Advanced Audit Trails](https://developer.intacct.com/api/company-console/advanced-audit-trails/#query-and-list-advanced-audit-trails)
*   [Query and List Advanced Audit Trails (Legacy)](https://developer.intacct.com/api/company-console/advanced-audit-trails/#query-and-list-advanced-audit-trails-legacy)

* * *

Advanced Audit Trails provide information about read and write access to personal data in the system, which can be useful for regulatory purposes.

Sage Intacct tracks all personal data stored in contact, vendor, and customer records.

Information about read access covers:

*   Using UI listers
*   Accessing objects that reference other objects with personal data
*   Viewing reports
*   Viewing Smart Events
*   Using `query`, `read`, `readByQuery`, `readMore`, and `readByName` API calls

Information provided about write access corresponds with information that is returned by [audit trails](https://developer.intacct.com/api/company-console/audit-trails/) functions.

Returned elements indicating read access of personal data have an `ACCESSMODE` of `Personal data access`. Returned elements indicating write access of personal data have an `ACCESSMODE` of `System audit`.

The Advanced Audit Trail subscription is required, and the user associated with the API session must have **View** permission for custom reports. That permission can be enabled under the Platform Services subscription.

* * *

Get Advanced Audit Trails Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the advanced audit trails object:

```
<lookup>
    <object>ADVAUDITHISTORY</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ADVAUDITHISTORY` |

* * *

Query and List Advanced Audit Trails
------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the access mode, user ID, source, and access time for each advanced audit trail involving personal data, sorting from the newest entries to the oldest:

```
<query>
    <object>ADVAUDITHISTORY</object>
    <select>
        <field>ACCESSMODE</field>
        <field>USERID</field>
        <field>SOURCE</field>
        <field>ACCESSTIME</field>
    </select>
    <filter>
        <equalto>
            <field>ACCESSMODE</field>
            <value>Personal data access</value>
        </equalto>
    </filter>
    <orderby>
        <order>
            <field>ACCESSTIME</field>
            <descending/>
        </order>
    </orderby>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ADVAUDITHISTORY` |
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

`filter` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| OBJECTTYPE | Optional | string | Object type for one of the objects with personal data. Use `contact` for contacts shared across the entire system, `vendor` for vendors, or `customer` for customers. Otherwise, omit the value and get information about all three object types. |
| OBJECTKEY | Optional | string | Unique name field of the object, which differs based on the object type. For `CONTACT` it is the `CONTACTNAME`, for `VENDOR` it is the `VENDORID`, and for `CUSTOMER` it is the `CUSTOMERID`. |
| USERID | Optional | string | User ID |
| ACCESSTIME | Optional | string | Timestamp of access in the format `MM/DD/YYYY HH:MM:SS`. |
| ACCESSMODE | Optional | string | Type of access mode. Use `Personal data access` to get information about all read access to objects containing personal data. Use `System audit` to get information about all write access to objects containing personal data. |
| SOURCE | Optional | string | General category of the operation. Use `api`, `csv`, `system`, or `ui`. |

#### `Response`

`ADVAUDITHISTORY`

> The above function can return data such as the following (depending on the filter parameters used):

```
<ADVAUDITHISTORY>
    <ACCESSMODE>Personal data access</ACCESSMODE>
    <USERID>jjones</USERID>
    <SOURCE>ui</SOURCE>
    <OBJECTTYPE>customer</OBJECTTYPE>
    <ACCESSTIME>04/29/2020 21:34:47</ACCESSTIME>
</ADVAUDITHISTORY>
<ADVAUDITHISTORY>
    <ACCESSMODE>Personal data access</ACCESSMODE>
    <USERID>jjones</USERID>
    <SOURCE>api</SOURCE>
    <OBJECTTYPE>contact</OBJECTTYPE>
    <ACCESSTIME>04/29</ACCESSTIME>
</ADVAUDITHISTORY>
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| OBJECTTYPE | string | Name of the personal data object type. One of `contact`, `vendor`, or `customer`. |
| OBJECTKEY | string | Unique name of the record |
| USERID | string | User ID that performed the action |
| ACCESSTIME | string | Timestamp of the event. Note that the returned value will be according to the GMT time zone, regardless of Company preferences. |
| ACCESSMODE | string | Type of the event, either `Personal data access` for read access of personal data or `System audit` for write access of personal data |
| WORKFLOWACTION | string | Indicates a workflow action |
| SOURCE | string | General category of the operation. One of `api`, `csv`, `system`, or `ui`. |
| IPADDRESS | string | Originating IP address |
| ID | string | Generated unique ID for this audited action |

* * *

Query and List Advanced Audit Trails (Legacy)
---------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ADVAUDITHISTORY</object>
    <fields>*</fields>
    <query>ACCESSMODE = 'Personal data access'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ADVAUDITHISTORY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. **Note:** `like`, `not like`, `IS NOT NULL`, and `IS NULL` are not supported for `OBJECTTYPE` and `OBJECTKEY`. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| OBJECTTYPE | Optional | string | Object type for one of the objects with personal data. Use `contact` for contacts shared across the entire system, `vendor` for vendors, or `customer` for customers. Otherwise, omit the value and get information about all three object types. |
| OBJECTKEY | Optional | string | Unique name field of the object, which differs based on the object type. For `CONTACT` it is the `CONTACTNAME`, for `VENDOR` it is the `VENDORID`, and for `CUSTOMER` it is the `CUSTOMERID`. |
| USERID | Optional | string | User ID |
| ACCESSTIME | Optional | string | Timestamp of access in the format `MM/DD/YYYY HH:MM:SS`. |
| ACCESSMODE | Optional | string | Type of access mode. Use `Personal data access` to get information about all read access to objects containing personal data. Use `System audit` to get information about all write access to objects containing personal data. |
| SOURCE | Optional | string | General category of the operation. Use `api`, `csv`, `system`, or `ui`. |

#### `Response`

`advaudithistory`

> The above function returns data such as the following:

```
<advaudithistory>
	<OBJECTTYPE>Vendor</OBJECTTYPE>
	<OBJECTKEY>BANK-099</OBJECTKEY>
	<USERID>Admin</USERID>
	<ACCESSTIME>03/08/2018 01:48:24</ACCESSTIME>
	<ACCESSMODE>Personal data access</ACCESSMODE>
	<WORKFLOWACTION></WORKFLOWACTION>
	<IPADDRESS>xxx.xxx.xx.xx</IPADDRESS>
	<SOURCE>ui</SOURCE>
	<ID>sessionidxxx</ID>
</advaudithistory>
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| OBJECTTYPE | string | Name of the personal data object type. One of `contact`, `vendor`, or `customer`. |
| OBJECTKEY | string | Unique name of the record |
| USERID | string | User ID that performed the action |
| ACCESSTIME | string | Timestamp of the event. Note that the returned value will be according to the GMT time zone, regardless of Company preferences. |
| ACCESSMODE | string | Type of the event, either `Personal data access` for read access of personal data or `System audit` for write access of personal data |
| WORKFLOWACTION | string | Indicates a workflow action |
| SOURCE | string | General category of the operation. One of `api`, `csv`, `system`, or `ui`. |
| IPADDRESS | string | Originating IP address |
| ID | string | Generated unique ID for this audited action |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

