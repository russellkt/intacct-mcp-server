Title: Account Allocation Groups

URL Source: https://developer.intacct.com/api/general-ledger/account-allocation-groups/

Markdown Content:
*   [Get Account Allocation Group Object Definition](https://developer.intacct.com/api/general-ledger/account-allocation-groups/#get-account-allocation-group-object-definition)
*   [Query and List Account Allocation Groups](https://developer.intacct.com/api/general-ledger/account-allocation-groups/#query-and-list-account-allocation-groups)
*   [Query and List Account Allocation Groups (Legacy)](https://developer.intacct.com/api/general-ledger/account-allocation-groups/#query-and-list-account-allocation-groups-legacy)
*   [Get Account Allocation Group](https://developer.intacct.com/api/general-ledger/account-allocation-groups/#get-account-allocation-group)
*   [Create Account Allocation Group](https://developer.intacct.com/api/general-ledger/account-allocation-groups/#create-account-allocation-group)
*   [Update Account Allocation Group](https://developer.intacct.com/api/general-ledger/account-allocation-groups/#update-account-allocation-group)
*   [Delete Account Allocation Group](https://developer.intacct.com/api/general-ledger/account-allocation-groups/#delete-account-allocation-group)

* * *

Account allocation groups support generation of multiple account allocation entries, which is useful for organizations with many allocations that must run on the same interval and/or with dependencies.

You can also use account allocation groups to set up the order for sequential processing, where one allocation is dependent on the results of a prior one.

* * *

Get Account Allocation Group Object Definition
----------------------------------------------

#### `lookup`

> List all the fields and relationships for the account allocation group object:

```
<lookup>
    <object>GLACCTALLOCATIONGRP</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONGRP` |

* * *

Query and List Account Allocation Groups
----------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, name, and group error processing method in use for each account allocation group:

```
<query>
    <object>GLACCTALLOCATIONGRP</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
        <field>GRPERRORPROCESSINGMETHOD</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONGRP` |
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

Query and List Account Allocation Groups (Legacy)
-------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>GLACCTALLOCATIONGRP</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONGRP` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GRPERRORPROCESSINGMETHOD | Optional | string | Group error processing method in use. Use `E` for groups set to Stop if a group member in the sequence fails or `S` for groups set to Skip and continue if a group in the sequence fails. |

* * *

Get Account Allocation Group
----------------------------

#### `read`

```
<read>
    <object>GLACCTALLOCATIONGRP</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONGRP` |
| keys | Required | string | Comma-separated list of account allocation group `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

Create Account Allocation Group
-------------------------------

#### `create`

```
<create>
    <GLACCTALLOCATIONGRP>
        <NAME>Month end</NAME>
        <DESCRIPTION>All month end allocations for the company</DESCRIPTION>
        <GRPERRORPROCESSINGMETHOD>Skip and continue if a group in the sequence fails</GRPERRORPROCESSINGMETHOD>
        <GLACCTALLOCATIONGRPMEMBERS>
            <GLACCTALLOCATIONGRPMEMBER>
                <GLACCTALLOCATIONID>Allocation-1</GLACCTALLOCATIONID>
            </GLACCTALLOCATIONGRPMEMBER>
            <GLACCTALLOCATIONGRPMEMBER>
                <GLACCTALLOCATIONID>Allocation-2</GLACCTALLOCATIONID>
            </GLACCTALLOCATIONGRPMEMBER>
        </GLACCTALLOCATIONGRPMEMBERS>
    </GLACCTALLOCATIONGRP>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATIONGRP | Required | object | Object to create |

`GLACCTALLOCATIONGRP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Group name for the account allocation group |
| DESCRIPTION | Required | string | Description of the account allocation group |
| STATUS | Optional | string | Status of the group. Use `active` for Active or `inactive` for Inactive. (Default: `active`) |
| GRPERRORPROCESSINGMETHOD | Optional | string | Group error processing method. If the group contains dependencies where sequential processing is important, use `Stop if a group member in the sequence fails`. If the grouping is for convenience and sequential processing is not important, you can use `Skip and continue if a group in the sequence fails`. |
| GLACCTALLOCATIONGRPMEMBERS | Required | `GLACCTALLOCATIONGRPMEMBER[1...n]` | Account allocation group members. If one allocation is dependent on the completion of a previous allocation, order the members accordingly. |

`GLACCTALLOCATIONGRPMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATIONID | Required | string | Account allocation ID to use |

* * *

Update Account Allocation Group
-------------------------------

#### `update`

> Building on the example above that creates an allocation group, updates the array of members to include the original ones plus a new one (Allocation-3):

```
<update>
    <GLACCTALLOCATIONGRP>
        <RECORDNO>1</RECORDNO>
        <GLACCTALLOCATIONGRPMEMBERS>
            <GLACCTALLOCATIONGRPMEMBER>
                <GLACCTALLOCATIONID>Allocation-1</GLACCTALLOCATIONID>
            </GLACCTALLOCATIONGRPMEMBER>
            <GLACCTALLOCATIONGRPMEMBER>
                <GLACCTALLOCATIONID>Allocation-2</GLACCTALLOCATIONID>
            </GLACCTALLOCATIONGRPMEMBER>
            <GLACCTALLOCATIONGRPMEMBER>
                <GLACCTALLOCATIONID>Allocation-3</GLACCTALLOCATIONID>
            </GLACCTALLOCATIONGRPMEMBER>
        </GLACCTALLOCATIONGRPMEMBERS>
    </GLACCTALLOCATIONGRP>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATIONGRP | Required | object | Object to update |

`GLACCTALLOCATIONGRP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Account allocation group `RECORDNO` to update |
| NAME | Optional | string | Group name for the account allocation group |
| DESCRIPTION | Optional | string | Description of the account allocation group |
| STATUS | Optional | string | Status of the group. Use `active` for Active or `inactive` for Inactive (Default: `active`) |
| GRPERRORPROCESSINGMETHOD | Optional | string | Group error processing method. If the group contains dependencies where sequential processing is important, use `Stop if a group member in the sequence fails`. If the grouping is for convenience and sequential processing is not important, you can use `Skip and continue if a group in the sequence fails`. |
| GLACCTALLOCATIONGRPMEMBERS | Optional | `GLACCTALLOCATIONGRPMEMBER[1...n]` | Account allocation group members. If one allocation is dependent on the completion of a previous allocation, order the members accordingly. When updating group members, supply all the original members along with the ones to add. To delete a member, supply only the members you want to keep. |

`GLACCTALLOCATIONGRPMEMBER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLACCTALLOCATIONID | Optional | string | Account allocation ID to use |

* * *

Delete Account Allocation Group
-------------------------------

#### `delete`

```
<delete>
    <object>GLACCTALLOCATIONGRP</object>
    <keys>14</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLACCTALLOCATIONGRP` |
| keys | Required | string | Comma-separated list of account allocation group `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

