Title: AP Account Labels

URL Source: https://developer.intacct.com/api/accounts-payable/ap-account-labels/

Markdown Content:
*   [Get AP Account Label Object Definition](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#get-ap-account-label-object-definition)
*   [Query and List AP Account Labels](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#query-and-list-ap-account-labels)
*   [Query and List AP Account Labels (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#query-and-list-ap-account-labels-legacy)
*   [Get AP Account Label](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#get-ap-account-label)
*   [Get AP Account Label by ID](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#get-ap-account-label-by-id)
*   [Create AP Account Label](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#create-ap-account-label)
*   [Create AP Account Label (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#create-ap-account-label-legacy)
*   [Update AP Account Label](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#update-ap-account-label)
*   [Update AP Account Label (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#update-ap-account-label-legacy)
*   [Delete AP Account Label](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#delete-ap-account-label)
*   [Delete AP Account Label (Legacy)](https://developer.intacct.com/api/accounts-payable/ap-account-labels/#delete-ap-account-label-legacy)

* * *

AP account labels provide more meaningful names for accounts and are useful for restricting account access.

This functionality must be enabled by configuring AP in the Sage Intacct UI.

* * *

Get AP Account Label Object Definition
--------------------------------------

#### `lookup`

> List all the fields and relationships for the AP account label object:

```
<lookup>
    <object>APACCOUNTLABEL</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APACCOUNTLABEL` |

* * *

Query and List AP Account Labels
--------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List each active account label:

```
<query>
    <object>APACCOUNTLABEL</object>
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
| object | Required | string | Use `APACCOUNTLABEL` |
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

Query and List AP Account Labels (Legacy)
-----------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>APACCOUNTLABEL</object>
    <fields>*</fields>
    <query>STATUS = 'T'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APACCOUNTLABEL` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active and `F` for Inactive. |

* * *

Get AP Account Label
--------------------

#### `read`

```
<read>
    <object>APACCOUNTLABEL</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of label `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get AP Account Label by ID
--------------------------

#### `readByName`

```
<readByName>
    <object>APACCOUNTLABEL</object>
    <keys>Travel Expenses</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of label `ACCOUNTLABEL` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create AP Account Label
-----------------------

#### `create`

```
<create>
    <APACCOUNTLABEL>
        <ACCOUNTLABEL>Travel Expenses</ACCOUNTLABEL>
        <DESCRIPTION>Travel Expenses</DESCRIPTION>
        <GLACCOUNTNO>6080</GLACCOUNTNO>
        <OFFSETGLACCOUNTNO></OFFSETGLACCOUNTNO>
        <STATUS>active</STATUS>
    </APACCOUNTLABEL>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APACCOUNTLABEL | Required | object | Object to create |

`APACCOUNTLABEL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTLABEL | Required | string | Account label to create |
| DESCRIPTION | Required | string | Description |
| GLACCOUNTNO | Required | string | Account number |
| OFFSETGLACCOUNTNO | Optional | string | Offset AP account number |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |

* * *

Create AP Account Label (Legacy)
--------------------------------

#### `create_apaccountlabel`

```
<create_apaccountlabel>
    <glaccountno>6080</glaccountno>
    <accountlabel>Travel Expenses</accountlabel>
    <description>Travel Expenses</description>
    <offsetglaccountno></offsetglaccountno>
    <status>active</status>
</create_apaccountlabel>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| glaccountno | Required | string | Account number |
| accountlabel | Required | string | Account label to create |
| description | Required | string | Description |
| offsetglaccountno | Optional | string | Offset AP account number |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Update AP Account Label
-----------------------

#### `update`

```
<update>
    <APACCOUNTLABEL>
        <RECORDNO>12</RECORDNO>
        <DESCRIPTION>Travel Expenses</DESCRIPTION>
        <GLACCOUNTNO>6080</GLACCOUNTNO>
        <OFFSETGLACCOUNTNO></OFFSETGLACCOUNTNO>
        <STATUS>active</STATUS>
    </APACCOUNTLABEL>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| APACCOUNTLABEL | Required | object | Object to update |

`APACCOUNTLABEL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Account label `RECORDNO` to update |
| DESCRIPTION | Optional | string | Description |
| GLACCOUNTNO | Optional | string | Account number |
| OFFSETGLACCOUNTNO | Optional | string | Offset AP account number |
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

* * *

Update AP Account Label (Legacy)
--------------------------------

#### `update_apaccountlabel`

```
<update_apaccountlabel accountlabel="Travel Expenses">
    <glaccountno>6090</glaccountno>
</update_apaccountlabel>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| accountlabel | Required | string | Account label to update |
| glaccountno | Optional | string | Account number |
| description | Optional | string | Description |
| offsetglaccountno | Optional | string | Offset AP account number |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |

* * *

Delete AP Account Label
-----------------------

#### `delete`

```
<delete>
    <object>APACCOUNTLABEL</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APACCOUNTLABEL` |
| keys | Required | string | Comma-separated list of label `RECORDNO` to delete |

* * *

Delete AP Account Label (Legacy)
--------------------------------

#### `delete_apaccountlabel`

```
<delete_apaccountlabel accountlabel="Travel Expenses"></delete_apaccountlabel>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| accountlabel | Required | string | Account label to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

