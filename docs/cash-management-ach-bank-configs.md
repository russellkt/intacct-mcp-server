Title: ACH Bank Configurations

URL Source: https://developer.intacct.com/api/cash-management/ach-bank-configs/

Markdown Content:
*   [Get ACH Bank Configuration Object Definition](https://developer.intacct.com/api/cash-management/ach-bank-configs/#get-ach-bank-configuration-object-definition)
*   [Query and List ACH Bank Configurations](https://developer.intacct.com/api/cash-management/ach-bank-configs/#query-and-list-ach-bank-configurations)
*   [Query and List ACH Bank Configurations (Legacy)](https://developer.intacct.com/api/cash-management/ach-bank-configs/#query-and-list-ach-bank-configurations-legacy)
*   [Get ACH Bank Configuration](https://developer.intacct.com/api/cash-management/ach-bank-configs/#get-ach-bank-configuration)
*   [Get ACH Bank Configuration by ID](https://developer.intacct.com/api/cash-management/ach-bank-configs/#get-ach-bank-configuration-by-id)
*   [Create ACH Bank Configuration (Legacy)](https://developer.intacct.com/api/cash-management/ach-bank-configs/#create-ach-bank-configuration-legacy)
*   [Update ACH Bank Configuration (Legacy)](https://developer.intacct.com/api/cash-management/ach-bank-configs/#update-ach-bank-configuration-legacy)
*   [Delete ACH Bank Configuration (Legacy)](https://developer.intacct.com/api/cash-management/ach-bank-configs/#delete-ach-bank-configuration-legacy)

* * *

ACH banks are used for making automated clearing house (ACH) transactions.

* * *

Get ACH Bank Configuration Object Definition
--------------------------------------------

#### `lookup`

> List all the fields and relationships for the ACH bank configuration object:

```
<lookup>
    <object>ACHBANK</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACHBANK` |

* * *

Query and List ACH Bank Configurations
--------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the ID and record number for each bank configuration:

```
<query>
    <object>ACHBANK</object>
    <select>
        <field>ACHBANKID</field>
        <field>RECORDNO</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACHBANK` |
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

Query and List ACH Bank Configurations (Legacy)
-----------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>ACHBANK</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACHBANK` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

Get ACH Bank Configuration
--------------------------

#### `read`

```
<read>
    <object>ACHBANK</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACHBANK` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get ACH Bank Configuration by ID
--------------------------------

#### `readByName`

```
<readByName>
    <object>ACHBANK</object>
    <keys>BOFAACH</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ACHBANK` |
| keys | Required | string | Comma-separated list of config `ACHBANKID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create ACH Bank Configuration (Legacy)
--------------------------------------

#### `create_achbankconfiguration`

```
<create_achbankconfiguration>
    <achbankid>BOFI1234</achbankid>
    <destinationid>DEST</destinationid>
    <destinationname></destinationname>
    <originid>12345</originid>
    <originname></originname>
    <referencecode></referencecode>
    <status>active</status>
    <eofmarker></eofmarker>
</create_achbankconfiguration>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| achbankid | Required | string | ACH Bank ID |
| destinationid | Required | string | Immediate destination ID. The bank’s routing number. |
| destinationname | Optional | string | Immediate destination name. The bank’s name as specified by your bank. |
| originid | Required | string | Immediate origin ID. Your 10-digit company number including hyphens as specified by your bank. |
| originname | Optional | string | Immediate origin name. Your company’s name, as specified by your bank. |
| referencecode | Optional | string | Reference code. |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| eofmarker | Optional | boolean | Include EOF marker. Use `true` for Yes otherwise use `false` for No (Default: `false`) |

* * *

Update ACH Bank Configuration (Legacy)
--------------------------------------

#### `update_achbankconfiguration`

```
<update_achbankconfiguration achbankid="BOFI1234">
    <destinationid>DEST</destinationid>
    <destinationname></destinationname>
    <originid>12345</originid>
    <originname></originname>
    <referencecode></referencecode>
    <status>active</status>
    <eofmarker></eofmarker>
</update_achbankconfiguration>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| achbankid | Required | string | ACH Bank ID |
| destinationid | Optional | string | Immediate destination ID. The bank’s routing number. |
| destinationname | Optional | string | Immediate destination name. The bank’s name as specified by your bank. |
| originid | Optional | string | Immediate origin ID. Your 10-digit company number including hyphens as specified by your bank. |
| originname | Optional | string | Immediate origin name. Your company’s name, as specified by your bank. |
| referencecode | Optional | string | Reference code. |
| status | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive. |
| eofmarker | Optional | boolean | Include EOF marker. Use `true` for Yes otherwise use `false` for No. |

* * *

Delete ACH Bank Configuration (Legacy)
--------------------------------------

#### `delete_achbankconfiguration`

```
<delete_achbankconfiguration achbankid="BOFI1234"></delete_achbankconfiguration>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| achbankid | Required | string | Record number of bank configuration |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

