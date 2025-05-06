Title: DDS Jobs

URL Source: https://developer.intacct.com/api/data-delivery-service/dds-jobs/

Markdown Content:
*   [Get DDS Job Object Definition](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#get-dds-job-object-definition)
*   [Query and List DDS Jobs](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#query-and-list-dds-jobs)
*   [Query and List DDS Jobs (Legacy)](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#query-and-list-dds-jobs-legacy)
*   [Get DDS Job](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#get-dds-job)
*   [Run DDS Jobs](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#run-dds-jobs)

* * *

Data Delivery Service (DDS) enables you to export your data from Sage Intacct to a cloud destination.

* * *

Get DDS Job Object Definition
-----------------------------

#### `lookup`

> List all the fields and relationships for the DDS job object:

```
<lookup>
    <object>DDSJOB</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DDSJOB` |

* * *

Query and List DDS Jobs
-----------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and object for each DDS job:

```
<query>
    <object>DDSJOB</object>
    <select>
        <field>RECORDNO</field>
        <field>OBJECT</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DDSJOB` |
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

Query and List DDS Jobs (Legacy)
--------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>DDSJOB</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameter

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DDSJOB` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get DDS Job
-----------

#### `read`

```
<read>
    <object>DDSJOB</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DDSJOB` |
| keys | Required | string | Comma-separated list of job `RECORDNO` to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Run DDS Jobs
------------

[History](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#history-run-dds-jobs)

| Release | Changes |
| --- | --- |
| 2019 Release 4 | Added synchronized, objects |
| 2019 Release 2 | Added additional\_parameters |

There are several approaches for exporting data using DDS.

You can

*   run a DDS job for a single object, requesting either all changes or only changes since the last delivery.
*   run a DDS job for a set of objects, requesting either all changes or only changes since the last delivery.
*   run a synchronous DDS job for up to five objects for changes only.

### About synchronous jobs

Synchronous jobs start at the same point in time, which can help prevent reporting gaps.

When you run a set of synchronous jobs, the system checks whether there are jobs for any of the objects in your set already in the queue. If matching objects are found, those objects are not rerun as part of your set and will therefore have different starting times.

You cannot run synchronous jobs for GLACCOUNTBALANCE or GLRESOLVE.

#### `runDdsJob`

> Create a job to get all vendors:

```
<runDdsJob>
    <object>VENDOR</object>
    <cloudDelivery>AWS-S3-DDS</cloudDelivery>
    <jobType>all</jobType>
</runDdsJob>
```

> Create a job to get changed customers:

```
<runDdsJob>
    <object>CUSTOMER</object>
    <cloudDelivery>AWS-S3-DDS</cloudDelivery>
    <jobType>change</jobType>
</runDdsJob>
```

> Create a job to get GL account balances for the reporting periods January 2018 to April 2019:

```
<runDdsJob>
    <object>GLACCOUNTBALANCE</object>
    <cloudDelivery>AWS-S3-DDS</cloudDelivery>
    <jobType>all</jobType>
    <additional_parameters>
        <parameter>
            <name>PERIODSTARTDATE</name>
            <value>01/01/2018</value>
        </parameter>
        <parameter>
            <name>PERIODENDDATE</name>
            <value>04/30/2019</value>
        </parameter>
    </additional_parameters>
</runDdsJob>
```

> Create a job to get all information for multiple objects:

```
<runDdsJob>
    <objects>
        <object>APRECORD</object>
        <object>APDETAIL</object>
        <object>APBILLPAYMENT</object>
        <object>VENDOR</object>
        <object>LOCATION</object>
        <object>DEPARTMENT</object>
    </objects>
    <synchronized>false</synchronized>
    <cloudDelivery>AWS-S3-DDS</cloudDelivery>
    <jobType>all</jobType>
</runDdsJob>
```

> Create a synchronous job to get change information for multiple objects (five or fewer):

```
<runDdsJob>
    <objects>
        <object>APRECORD</object>
        <object>APDETAIL</object>
        <object>APBILLPAYMENT</object>
        <object>VENDOR</object>
        <object>LOCATION</object>
    </objects>
    <synchronized>true</synchronized>
    <cloudDelivery>AWS-S3-DDS</cloudDelivery>
    <jobType>change</jobType>
</runDdsJob>
```

> Create a job to get change information for the `APDETAIL` aggregate object and use a complex query to filter the results and specify the fields to include in the data:

```
<runDdsJob>
    <cloudDelivery>AWS-S3-DDS</cloudDelivery>
    <jobType>change</jobType>
    <timeStamp>2022-04-01T07:08:07+00:00</timeStamp>
    <query>
        <object>APDETAIL</object>
        <filter>
            <and>
                <isnotnull>
                    <field>ACCOUNTNO</field>
                </isnotnull>
                <or>
                    <greaterthan>
                        <field>ACCOUNTNO</field>
                        <value>6184</value>
                    </greaterthan>
                    <equalto>
                        <field>ACCOUNTNO</field>
                        <value>6185</value>
                    </equalto>
                </or>
            </and>
        </filter>
        <select>
            <field>AMOUNT</field>
            <field>ACCOUNTNO</field>
            <field>VENDORID</field>
        </select>
  </query>
</runDdsJob>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Optional | string | Single [DDS object or aggregate object name](https://developer.intacct.com/data-delivery-service/objects/). Required if not using `<objects>` to provide multiple object names. |
| objects | Optional | array of [`object`](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#runDdsJob.object) | List of object names. Must be five or fewer when `synchronized` is set to `true`. Required if not using `<object>` to supply a single object name. |
| cloudDelivery | Required | string | Name of a [cloud storage destination](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Setting_up_cloud_storage) set up for your company in the Sage Intacct UI. |
| jobType | Required | string | Job type.
*   `change` - all changes since the last delivery
*   `all` - all data

 |
| additional\_parameters | Optional | [`parameter[1...2]`](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#runDdsJob.parameter) | `PERIODSTARTDATE` and `PERIODENDDATE` for which to calculate balances when using the GLACCOUNTBALANCE object. If you don’t provide these parameters, historical reporting periods are used and this can generate a lot of unneeded data. |
| timeStamp | Optional | string | Timestamp to get data from if `jobType` is `change`. The time zone is UTC, and future dates are not supported.  
Format `YYYY-MM-DDThh:mm:ss`. |
| query | Optional | object | Specification of filtering criteria and the fields to include in results. |
| fileConfiguration | Optional | [object](https://developer.intacct.com/api/data-delivery-service/dds-jobs/#runDdsJob.fileConfiguration) | Output file attributes |
| synchronized | Optional | boolean | Specifies a synchronized run where each job in the set will start at the same time. Only available when `jobType` is set to `change` and when five or fewer objects are specified. Use `true` for a synchronized run, `false` otherwise. (Default: `false`) |

`runDdsJob.object`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | [DDS object or aggregate object name](https://developer.intacct.com/data-delivery-service/objects/) |

`runDdsJob.parameter`

Available for use only if the `object` is GLACCOUNTBALANCE.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Optional | string | Parameter name. Use `PERIODSTARTDATE` and `PERIODENDDATE` together, or `PERIOD`. |
| value | Optional | string | For `PERIODSTARTDATE` and `PERIODENDDATE`, provide both the period start and end date in the format `mm/dd/yyyy`. For `PERIOD`, provide the name of a budgetable reporting period (Ex: `Month Ended April 2019`) or a system reporting period (Ex: `Current Month`). Partial periods are not supported, and the system reports full period ranges. For example, the whole April period will be used if you enter a start date of 04/15/2019 and an end date of 04/29/2019. |

`runDdsJob.query`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | The name of a [DDS object or aggregate object](https://developer.intacct.com/data-delivery-service/objects/) to apply filters to. |
| filter | Optional | object | [Filter expression](https://developer.intacct.com/web-services/queries/#filter) to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, `VENDOR.CREDITLIMIT` on APBILL). |
| select | Required | sequence | `field` elements containing the names of the fields that you want included in the response, and an optional [aggregate function](https://developer.intacct.com/web-services/queries/#aggregate-functions) such as `count` or `sum`. Must be `<fields>*</fields>` for `GLACCOUNTBALANCE` object. |
| orderby | Optional | object | Provide an `order` element with a field name and choose an ascending or descending [sort order](https://developer.intacct.com/web-services/queries/#order-by), for example:  
```
<order>  
   <field>RECORDNO</field>   
   <descending/>   
</order>
``` |

`runDdsJob.fileConfiguration`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| delimiter | Optional | string | Value delimiter. Use `.` for Period, `;` for Semicolon, or `,` for Comma (Default: `,` Comma) |
| enclosure | Optional | string | Text qualifier. Use `"` for Double quote, `'` for Single quote, `[` for Left bracket, or `/` for Forward Slash (Default: `"` Double quote) |
| includeHeaders | Optional | boolean | Include column headers. Use `true` for Yes otherwise `false` for No (Default: `false`) |
| fileFormat | Optional | string | File format. Use `windows`, `mac`, or `unix` (Default: `unix`) |
| splitSize | Optional | integer | Split files after this many records. Minimum is `10000` and maximum is `100000`. |
| compress | Optional | boolean | Compress file. Use `true` for Yes otherwise `false` for No (Default: `false`). |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

