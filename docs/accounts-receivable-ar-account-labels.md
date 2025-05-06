Title: AR Account Labels

URL Source: https://developer.intacct.com/api/accounts-receivable/ar-account-labels/

Markdown Content:
*   [Get AR Account Label Object Definition](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#get-ar-account-label-object-definition)
*   [Query and List AR Account Labels](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#query-and-list-ar-account-labels)
*   [Query and List AR Account Labels (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#query-and-list-ar-account-labels-legacy)
*   [Get AR Account Label](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#get-ar-account-label)
*   [Get AR Account Label by ID](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#get-ar-account-label-by-id)
*   [Create AR Account Label](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#create-ar-account-label)
*   [Create AR Account Label (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#create-ar-account-label-legacy)
*   [Update AR Account Label](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#update-ar-account-label)
*   [Update AR Account Label (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#update-ar-account-label-legacy)
*   [Delete AR Account Label](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#delete-ar-account-label)
*   [Delete AR Account Label (Legacy)](https://developer.intacct.com/api/accounts-receivable/ar-account-labels/#delete-ar-account-label-legacy)

* * *

AR account labels provide more meaningful names for accounts and are useful for restricting account access.

This functionality must be enabled by configuring AR in the Sage Intacct UI.

* * *

Get AR Account Label Object Definition
--------------------------------------

#### `lookup`

> List all the fields and relationships for the AR account label object:

```
<lookup>
    <object>ARACCOUNTLABEL</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARACCOUNTLABEL` |

* * *

Query and List AR Account Labels
--------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List each active account label:

```
<query>
    <object>ARACCOUNTLABEL</object>
    <select>
        <field>ACCOUNTLABEL</field>
    </select>
    <filter>
        <equalto>
            <field>STATUS</field>
            <value>active</value>
        </equalto>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARACCOUNTLABEL` |
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

Query and List AR Account Labels (Legacy)
-----------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ARACCOUNTLABEL</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARACCOUNTLABEL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get AR Account Label
--------------------

#### `read`

```
<read>
    <object>ARACCOUNTLABEL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of label `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get AR Account Label by ID
--------------------------

#### `readByName`

```
<readByName>
    <object>ARACCOUNTLABEL</object>
    <keys>Revenue</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of label `ACCOUNTLABEL` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create AR Account Label
-----------------------

#### `create`

```
<create>
    <ARACCOUNTLABEL>
        <ACCOUNTLABEL>Revenue</ACCOUNTLABEL>
        <DESCRIPTION>Revenue</DESCRIPTION>
        <GLACCOUNTNO>4000</GLACCOUNTNO>
        <OFFSETGLACCOUNTNO></OFFSETGLACCOUNTNO>
        <STATUS>active</STATUS>
    </ARACCOUNTLABEL>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ARACCOUNTLABEL | Required | object | Object to create |

`ARACCOUNTLABEL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTLABEL | Required | string | Account label to create |
| DESCRIPTION | Required | string | Description |
| GLACCOUNTNO | Required | string | Account number |
| OFFSETGLACCOUNTNO | Optional | string | Offset AR account number |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Create AR Account Label (Legacy)
--------------------------------

#### `create_araccountlabel`

```
<create_araccountlabel>
    <glaccountno>4000</glaccountno>
    <accountlabel>Revenue</accountlabel>
    <description>Revenue</description>
    <offsetglaccountno></offsetglaccountno>
    <status>active</status>
</create_araccountlabel>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Account number |
| accountlabel | Required | string | Account label to create |
| description | Required | string | Description |
| offsetglaccountno | Optional | string | Offset AR account number |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| taxcode | Optional | string | Tax code |

* * *

Update AR Account Label
-----------------------

#### `update`

```
<update>
    <ARACCOUNTLABEL>
        <RECORDNO>12</RECORDNO>
        <DESCRIPTION>Revenue</DESCRIPTION>
        <GLACCOUNTNO>4010</GLACCOUNTNO>
        <OFFSETGLACCOUNTNO></OFFSETGLACCOUNTNO>
        <STATUS>active</STATUS>
    </ARACCOUNTLABEL>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ARACCOUNTLABEL | Required | object | Object to update |

`ARACCOUNTLABEL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Account label `RECORDNO` to update |
| DESCRIPTION | Optional | string | Description |
| GLACCOUNTNO | Optional | string | Account number |
| OFFSETGLACCOUNTNO | Optional | string | Offset AR account number |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Update AR Account Label (Legacy)
--------------------------------

#### `update_araccountlabel`

```
<update_araccountlabel accountlabel="Revenue">
    <glaccountno>4100</glaccountno>
</update_araccountlabel>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| accountlabel | Required | string | Account label to update |
| glaccountno | Optional | string | Account number |
| description | Optional | string | Description |
| offsetglaccountno | Optional | string | Offset AR account number |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |
| taxcode | Optional | string | Tax code |

* * *

Delete AR Account Label
-----------------------

#### `delete`

```
<delete>
    <object>ARACCOUNTLABEL</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of label `RECORDNO` to delete |

* * *

Delete AR Account Label (Legacy)
--------------------------------

#### `delete_araccountlabel`

```
<delete_araccountlabel accountlabel="Revenue"></delete_araccountlabel>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| accountlabel | Required | string | Account label to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

