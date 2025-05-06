Title: Contract Billing Schedules

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/

Markdown Content:
*   [Contract Billing Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#contract-billing-schedules)
    *   [Get Contract Billing Schedule Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#get-contract-billing-schedule-object-definition)
    *   [Query and List Contract Billing Schedules](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#query-and-list-contract-billing-schedules)
    *   [Query and List Contract Billing Schedules (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#query-and-list-contract-billing-schedules-legacy)
    *   [Get Contract Billing Schedule](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#get-contract-billing-schedule)
*   [Contract Billing Schedule Entries](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#contract-billing-schedule-entries)
    *   [Get Contract Billing Schedule Entry Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#get-contract-billing-schedule-entry-object-definition)
    *   [Query and List Contract Billing Schedule Entries](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#query-and-list-contract-billing-schedule-entries)
    *   [Query and List Contract Billing Schedule Entries (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#query-and-list-contract-billing-schedule-entries-legacy)
    *   [Get Contract Billing Schedule Entry](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#get-contract-billing-schedule-entry)
    *   [Update Contract Billing Schedule Entry](https://developer.intacct.com/api/contracts-rev-mgmt/contract-billing-schedules/#update-contract-billing-schedule-entry)

* * *

A billing schedule shows you when the Flat/Fixed amount associated with a contract line item is expected to be invoiced during the contract term.

The system generates a billing schedule based on one of the following:

*   The contract line billing template and the billing template start and end dates
*   The contract billing frequency, contract line start and end dates, and the contract line flat/fixed amount frequency

* * *

### Get Contract Billing Schedule Object Definition

#### `lookup`

> List all the fields and relationships for the contract billing schedule object:

```
<lookup>
    <object>CONTRACTBILLINGSCHEDULE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULE` |

* * *

### Query and List Contract Billing Schedules

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and state for each contract billing schedule:

```
<query>
    <object>CONTRACTBILLINGSCHEDULE</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULE` |
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

### Query and List Contract Billing Schedules (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTBILLINGSCHEDULE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Optional | string | Contract ID |
| LINENO | Optional | integer | Line number from the contract |

* * *

### Get Contract Billing Schedule

#### `read`

```
<read>
    <object>CONTRACTBILLINGSCHEDULE</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULE` |
| keys | Required | string | Comma-separated list of `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Contract Billing Schedule Entries
---------------------------------

### Get Contract Billing Schedule Entry Object Definition

#### `lookup`

> List all the fields and relationships for the contract billing schedule entry object:

```
<lookup>
    <object>CONTRACTBILLINGSCHEDULEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULEENTRY` |

* * *

### Query and List Contract Billing Schedule Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and amount for each contract billing schedule entry:

```
<query>
    <object>CONTRACTBILLINGSCHEDULEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>AMOUNT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULEENTRY` |
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

### Query and List Contract Billing Schedule Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTBILLINGSCHEDULEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| POSTED | Optional | boolean | Use `T` or `F` |
| STATE | Optional | string | Use `O` for open, `T` for terminated, `P` for posted |

* * *

### Get Contract Billing Schedule Entry

#### `read`

```
<read>
    <object>CONTRACTBILLINGSCHEDULEENTRY</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTBILLINGSCHEDULEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Update Contract Billing Schedule Entry

#### `update`

> Update the date for an entry:

```
<update>
    <CONTRACTBILLINGSCHEDULE>
        <RECORDNO>57</RECORDNO>
        <CONTRACTBILLINGSCHEDULEENTRIES>
            <CONTRACTBILLINGSCHEDULEENTRY>
                <RECORDNO>1133</RECORDNO>
                <POSTINGDATE>2017-01-09</POSTINGDATE>
            </CONTRACTBILLINGSCHEDULEENTRY>
        </CONTRACTBILLINGSCHEDULEENTRIES>
    </CONTRACTBILLINGSCHEDULE>
</update>
```

> Change the amounts for two entries (the total amount for the schedule must remain the same):

```
<update>
    <CONTRACTBILLINGSCHEDULE>
        <RECORDNO>57</RECORDNO>
        <CONTRACTBILLINGSCHEDULEENTRIES>
            <CONTRACTBILLINGSCHEDULEENTRY>
                <RECORDNO>1133</RECORDNO>
                <AMOUNT>50</AMOUNT>
            </CONTRACTBILLINGSCHEDULEENTRY>
            <CONTRACTBILLINGSCHEDULEENTRY>
                <RECORDNO>1134</RECORDNO>
                <AMOUNT>150</AMOUNT>
            </CONTRACTBILLINGSCHEDULEENTRY>
        </CONTRACTBILLINGSCHEDULEENTRIES>
    </CONTRACTBILLINGSCHEDULE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTBILLINGSCHEDULE | Required | string | Object to update |
| RECORDNO | Required | string | `RECORDNO` of the parent contract billing schedule |
| CONTRACTBILLINGSCHEDULEENTRIES | Required | `CONTRACTBILLINGSCHEDULEENTRY[1...n]` | Contract billing schedule entries |

`CONTRACTBILLINGSCHEDULEENTRY[1...n]`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTBILLINGSCHEDULEENTRY | Required | string | Object to update |
| RECORDNO | Required | string | `RECORDNO` of the schedule entry. Only required for updating an entry. |
| POSTINGDATE | Optional | string | Scheduled billing date. Required for a new entry. |
| AMOUNT | Optional | currency | Amount for the entry. Required for a new entry. |
| SERVICEPERIODSTARTDATE | Optional | string | Identifies the start date of a billed service period in the billing schedule. |
| SERVICEPERIODENDDATE | Optional | string | Identifies the end of the date of a billed service period in the billing schedule. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

