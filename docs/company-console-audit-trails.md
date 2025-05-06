Title: Audit Trails

URL Source: https://developer.intacct.com/api/company-console/audit-trails/

Markdown Content:
*   [Audit History](https://developer.intacct.com/api/company-console/audit-trails/#audit-history)
    *   [Get Audit History Object Definition](https://developer.intacct.com/api/company-console/audit-trails/#get-audit-history-object-definition)
    *   [Query and List Audit History](https://developer.intacct.com/api/company-console/audit-trails/#query-and-list-audit-history)
    *   [Query and List Audit History (Legacy)](https://developer.intacct.com/api/company-console/audit-trails/#query-and-list-audit-history-legacy)
*   [Audit Trail Logs](https://developer.intacct.com/api/company-console/audit-trails/#audit-trail-logs)
    *   [List Standard Object Record Audit Trail Logs](https://developer.intacct.com/api/company-console/audit-trails/#list-standard-object-record-audit-trail-logs)
    *   [Get Custom Object Record Audit Trail Logs Object Definition](https://developer.intacct.com/api/company-console/audit-trails/#get-custom-object-record-audit-trail-logs-object-definition)
    *   [Query and List Custom Object Record Audit Trail Logs](https://developer.intacct.com/api/company-console/audit-trails/#query-and-list-custom-object-record-audit-trail-logs)
    *   [Query and List Custom Object Record Audit Trail Logs (Legacy)](https://developer.intacct.com/api/company-console/audit-trails/#query-and-list-custom-object-record-audit-trail-logs-legacy)
    *   [Get Custom Object Record Audit Trail Logs](https://developer.intacct.com/api/company-console/audit-trails/#get-custom-object-record-audit-trail-logs)

* * *

Audit trails provide information about who made changes to a particular record, and when.

See [Advanced Audit Trails](https://developer.intacct.com/api/company-console/advanced-audit-trails/) for information about read and write access of personal data in contact, vendor, and customer records.

To work with this object the user associated with the API session must have **View** permission for custom reports. That permission can be enabled under the Platform Services subscription.

* * *

Audit History
-------------

### Get Audit History Object Definition

#### `lookup`

> List all the fields and relationships for the audit history object:

```
<lookup>
    <object>AUDITHISTORY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `AUDITHISTORY` |

* * *

### Query and List Audit History

Return information about multiple types of objects based on query parameters. This object is a combination of standard object record audit trail logs, custom object record audit trail logs, user access logs, and smart event log records. You can use this function to return the aggregated history for a given user, return all records of a specific object type, return all records across a defined period of time, and so forth.

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the object type, source ID, and user ID for each audit history log item where the user ID is `jjackson`:

```
<query>
    <object>AUDITHISTORY</object>
    <select>
        <field>OBJECTTYPE</field>
        <field>SOURCE</field>
        <field>USERID</field>
    </select>
    <filter>
        <equalto>
            <field>USERID</field>
            <value>jjackson</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `AUDITHISTORY` |
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

### Query and List Audit History (Legacy)

Return information about multiple types of objects based on query parameters. This object is a combination of standard object record audit trail logs, custom object record audit trail logs, user access logs, and smart event log records. You can use this function to return the aggregated history for a given user, return all records of a specific object type, return all records across a defined period of time, and so forth.

#### `readByQuery`

```
<readByQuery>
    <object>AUDITHISTORY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `AUDITHISTORY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| USERID | Optional | string | User ID |
| ACCESSTIME | Optional | string | Timestamp in the format `MM/DD/YYYY HH:MM:SS` |
| ACCESSMODE | Optional | string | 
*   For `query`: Use `A` for Access, `M` for Modify, `C` for Create, `D` for Delete, `W` for Workflow, `T` for Activity, and `U` for User Action. Use full words for `Login`, `Platform Def`, and `Platform Action`.
*   For `readByQuery` (Legacy): Use `Access`, `Modify`, `Create`, `Delete`, `Workflow`, `Activity`, `User Action`, `Login`, `Platform Def`, and `Platform Action`

. |
| SOURCE | Optional | string | General category of the operation. Use `api`, `csv`, `system`, or `ui` |
| OBJECTTYPE | Optional | string | Object type, which can be a record type such as `apbill` or a type such as `ddsjob`, `userinfo`, and so forth. |
| OBJECTKEY | Optional | string | Unique name field of the object, which differs based on the object type. For example, on `APBILL` it is the `RECORDNO`, and on `USERINFO`, it is the `LOGINID`. |

* * *

Audit Trail Logs
----------------

### List Standard Object Record Audit Trail Logs

Return information about field level changes for a given record. The user associated with the API session must have permission to view the object in the audit trail.

#### `getAuditTrail`

> List all audit trail logs for the given record:

```
<getAuditTrail>
    <object>APBILL</object>
    <recordNo>1</recordNo>
</getAuditTrail>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Any valid audited object type. |
| recordNo | Optional | integer | `RECORDNO` for the record to get. Required if not using `objectKey`. |
| objectKey | Optional | string | Unique name field of the object, which differs based on the object type. For example, on `APBILL` it is the `RECORDNO`, and on `USERINFO`, it is the `LOGINID`. |

**Note:** If no information is returned, it means the record was created (or last modified) before the audit trail feature was implemented.

#### `Response`

`auditTrailDetail`

> The above function returns data structured like this:

```
<auditTrailDetail>
  <userId>admin</userId> 
  <object>apbill</object>
  <objectKey>204</objectKey> 
  <accessTime>2017-04-01T08:29:34+00:00</accessTime>
  <accessMode>access</accessMode> 
  <workflowAction></workflowAction> 
  <webServer>web49</webServer> 
  <trackingId>WN9k7cCoA5UAAFrQKesAAAAA</trackingId> 
  <ipAddress>xxx.xxx.xxx.xxx</ipAddress> 
  <source>ui</source> 
</auditTrailDetail>
```

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| userId | string | User ID that performed the action |
| object | string | Name of the object |
| objectKey | string | Unique name field of the object, which differs based on the object type. For example, on `APBILL` it is the `RECORDNO`, and on `USERINFO`, it is the `LOGINID`. |
| accessTime | datetime | Timestamp of the access |
| accessMode | string | Access mode (delete, modify, create, access, workflow, activity, user action) |
| workflowAction | string | Workflow action (paid, voided, etc.) |
| webServer | string | Webserver that performed the action |
| trackingId | string | Internal tracking ID |
| ipAddress | string | IP address of the end user |
| source | string | Source of the action (ui, api, csv, or system) |

* * *

### Get Custom Object Record Audit Trail Logs Object Definition

#### `lookup`

> List all the fields and relationships for the custom object record audit trail logs object:

```
<lookup>
    <object>ACTIVITYLOG</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACTIVITYLOG` |

* * *

### Query and List Custom Object Record Audit Trail Logs

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, object ID, relevant user, and created-at time for custom objects (IDs greater than 10000):

```
<query>
    <object>ACTIVITYLOG</object>
    <select>
        <field>RECORDNO</field>
        <field>OBJ_ID</field>
        <field>CREATEDBYUSER</field>
        <field>CREATED_AT</field>
    </select>
    <filter>
        <greaterthanorequalto>
            <field>OBJ_ID</field>
            <value>10000</value>
        </greaterthanorequalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACTIVITYLOG` |
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
| OBJ\_ID | Required | integer | ID of the record. All record IDs begin above `10000`. Use the record’s `id` value or find it on the record view’s System Information tab in the UI. |
| CREATED\_BY | Optional | integer | Created by user record number |
| CREATEDBYUSER | Optional | string | Created by user ID |
| CREATED\_AT | Optional | datetime | Created at timestamp in format `mm/dd/yyyy hh:mm:ss` |

#### `Response`

`ACTIVITYLOG`

> The above function returns data structured like this:

```
<ACTIVITYLOG>
    <RECORDNO>11139</RECORDNO>
    <OBJ_ID>10007</OBJ_ID>
    <CREATEDBYUSER>jjackson</CREATEDBYUSER>
    <CREATED_AT>06/11/2019 16:37:57</CREATED_AT>
</ACTIVITYLOG>
<ACTIVITYLOG>
    <RECORDNO>11138</RECORDNO>
    <OBJ_ID>10007</OBJ_ID>
    <CREATEDBYUSER>jjackson</CREATEDBYUSER>
    <CREATED_AT>06/11/2019 16:37:57</CREATED_AT>
</ACTIVITYLOG>
```

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| RECORDNO | integer | `RECORDNO` for the activity log |
| OBJ\_ID | integer | ID of the record. All record IDs begin above `10000`. Use the record’s `id` value or find it on the record view’s System Information tab in the UI. |
| TRAIL\_TEXT | string | Information about the change |
| EMAIL\_TEXT | string |   |
| CREATED\_BY | integer | Created by user record number |
| CREATEDBYUSER | string | Created by user ID |
| CREATED\_AT | datetime | Created at timestamp in format `mm/dd/yyyy hh:mm:ss` |

* * *

### Query and List Custom Object Record Audit Trail Logs (Legacy)

#### `readByQuery`

> List audit trail logs for all records on April 19, 2012:

```
<readByQuery>
    <object>ACTIVITYLOG</object>
    <fields>*</fields>
    <query>OBJ_ID &gt; 10000 AND CREATED_AT &gt;= '04/19/2012 12:00:00' AND CREATED_AT &lt; '04/20/2012 12:00:00'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACTIVITYLOG` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| OBJ\_ID | Required | integer | ID of the record. All record IDs begin above `10000`. Use the record’s `id` value or find it on the record view’s System Information tab in the UI. |
| CREATED\_BY | Optional | integer | Created by user record number |
| CREATEDBYUSER | Optional | string | Created by user ID |
| CREATED\_AT | Optional | datetime | Created at timestamp in format `mm/dd/yyyy hh:mm:ss` |

#### `Response`

`activitylog`

> The above function returns data structured like this:

```
<activitylog>
    <RECORDNO>11034</RECORDNO>
    <OBJ_ID>10049</OBJ_ID>
    <TRAIL_TEXT>Value of &quot;Name&quot; field has been changed from &quot;Test1&quot; to &quot;Test2&quot;.</TRAIL_TEXT>
    <EMAIL_TEXT></EMAIL_TEXT>
    <CREATED_BY>4</CREATED_BY>
    <CREATEDBYUSER>jsmith</CREATEDBYUSER>
    <CREATED_AT>04/19/2012 15:50:05</CREATED_AT>
</activitylog>
```

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| RECORDNO | integer | `RECORDNO` for the activity log |
| OBJ\_ID | integer | ID of the record. All record IDs begin above `10000`. Use the record’s `id` value or find it on the record view’s System Information tab in the UI. |
| TRAIL\_TEXT | string | Information about the change |
| EMAIL\_TEXT | string |   |
| CREATED\_BY | integer | Created by user record number |
| CREATEDBYUSER | string | Created by user ID |
| CREATED\_AT | datetime | Created at timestamp in format `mm/dd/yyyy hh:mm:ss` |

* * *

### Get Custom Object Record Audit Trail Logs

Please note this only works on **custom objects**.

#### `read`

```
<read>
    <object>ACTIVITYLOG</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACTIVITYLOG` |
| keys | Required | string | Comma-separated list of log `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

