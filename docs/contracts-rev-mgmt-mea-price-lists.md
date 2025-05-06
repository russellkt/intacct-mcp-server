Title: MEA Price Lists

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/

Markdown Content:
*   [MEA Price Lists](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#mea-price-lists)
    *   [Get MEA Price List Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#get-mea-price-list-object-definition)
    *   [Query and List MEA Price Lists](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#query-and-list-mea-price-lists)
    *   [Query and List MEA Price Lists (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#query-and-list-mea-price-lists-legacy)
    *   [Get MEA Price List](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#get-mea-price-list)
    *   [Get MEA Price List by ID](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#get-mea-price-list-by-id)
*   [MEA Price List Entries](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#mea-price-list-entries)
    *   [Get MEA Price List Entry Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#get-mea-price-list-entry-object-definition)
    *   [Query and List MEA Price List Entries](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#query-and-list-mea-price-list-entries)
    *   [Query and List MEA Price List Entries (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#query-and-list-mea-price-list-entries-legacy)
    *   [Get MEA Price List Entry](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#get-mea-price-list-entry)
*   [MEA Price List Entry Lines](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#mea-price-list-entry-lines)
    *   [Get MEA Price List Entry Line Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#get-mea-price-list-entry-line-object-definition)
    *   [Query and List MEA Price List Entry Lines](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#query-and-list-mea-price-list-entry-lines)
    *   [Query and List MEA Price List Entry Lines (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#query-and-list-mea-price-list-entry-lines-legacy)
    *   [Get MEA Price List Entry Line](https://developer.intacct.com/api/contracts-rev-mgmt/mea-price-lists/#get-mea-price-list-entry-line)

* * *

The MEA price list is a container for MEA price list entries, each of which defines the standalone selling price for an item in a multi-element arrangement.

Usage information for [MEA price lists](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=TOC_mea_price_lists) is available in the Sage Intacct product help.

* * *

### Get MEA Price List Object Definition

#### `lookup`

> List all the fields and relationships for the MEA price list object:

```
<lookup>
    <object>CONTRACTMEAPRICELIST</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAPRICELIST` |

* * *

### Query and List MEA Price Lists

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, name, and default setting for each MEA price list:

```
<query>
    <object>CONTRACTMEAPRICELIST</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
        <field>ISDEFAULT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAPRICELIST` |
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

### Query and List MEA Price Lists (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTMEAPRICELIST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAPRICELIST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active, `F` fo Inactive |

* * *

### Get MEA Price List

#### `read`

```
<read>
    <object>CONTRACTMEAPRICELIST</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAPRICELIST` |
| keys | Required | string | Comma-separated list of MEA price list `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get MEA Price List by ID

#### `readByName`

```
<readByName>
    <object>CONTRACTMEAPRICELIST</object>
    <keys>MEA Price List</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAPRICELIST` |
| keys | Required | string | Comma-separated list of MEA price list `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

MEA Price List Entries
----------------------

### Get MEA Price List Entry Object Definition

#### `lookup`

> List all the fields and relationships for the MEA price list entry object:

```
<lookup>
    <object>CONTRACTMEAITEMPRICELIST</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELIST` |

* * *

### Query and List MEA Price List Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and item ID for each price list entry:

```
<query>
    <object>CONTRACTMEAITEMPRICELIST</object>
    <select>
        <field>RECORDNO</field>
        <field>ITEMID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELIST` |
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

### Query and List MEA Price List Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACTMEAITEMPRICELIST</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELIST` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get MEA Price List Entry

#### `read`

```
<read>
    <object>CONTRACTMEAITEMPRICELIST</object>
    <keys>15</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELIST` |
| keys | Required | string | Comma-separated list of MEA item price list `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

MEA Price List Entry Lines
--------------------------

### Get MEA Price List Entry Line Object Definition

#### `lookup`

> List all the fields and relationships for the MEA price list entry line object:

```
<lookup>
    <object>CONTRACTMEAITEMPRICELISTENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELISTENTRY` |

* * *

### Query and List MEA Price List Entry Lines

#### [`query`](https://developer.intacct.com/web-services/queries/)

> Lists lines for the price list entry whose record number is 12:

```
<query>
    <object>CONTRACTMEAITEMPRICELISTENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>ALLOCITEMPRCLSTKEY</field>
    </select>
    <filter>
        <equalto>
            <field>ALLOCITEMPRCLSTKEY</field>
            <value>12</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELISTENTRY` |
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

### Query and List MEA Price List Entry Lines (Legacy)

#### `readByQuery`

> Lists lines for the price list entry whose record number is 12:

```
<readByQuery>
    <object>CONTRACTMEAITEMPRICELISTENTRY</object>
    <fields>*</fields>
    <query>ALLOCITEMPRCLSTKEY = 12</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELISTENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active, `F` fo Inactive |

* * *

### Get MEA Price List Entry Line

#### `read`

```
<read>
    <object>CONTRACTMEAITEMPRICELISTENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACTMEAITEMPRICELISTENTRY` |
| keys | Required | string | Comma-separated list of MEA item price list `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

