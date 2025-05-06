Title: Exchange Rates

URL Source: https://developer.intacct.com/api/company-console/exchange-rates/

Markdown Content:
*   [Exchange Rate Type](https://developer.intacct.com/api/company-console/exchange-rates/#exchange-rate-type)
    *   [Get Exchange Rate Type Object Definition](https://developer.intacct.com/api/company-console/exchange-rates/#get-exchange-rate-type-object-definition)
    *   [Query and List Exchange Rate Types](https://developer.intacct.com/api/company-console/exchange-rates/#query-and-list-exchange-rate-types)
    *   [Query and List Exchange Rate Types (Legacy)](https://developer.intacct.com/api/company-console/exchange-rates/#query-and-list-exchange-rate-types-legacy)
    *   [Get Exchange Rate Type](https://developer.intacct.com/api/company-console/exchange-rates/#get-exchange-rate-type)
    *   [Get Exchange Rate Type by ID](https://developer.intacct.com/api/company-console/exchange-rates/#get-exchange-rate-type-by-id)
*   [Exchange Rate](https://developer.intacct.com/api/company-console/exchange-rates/#exchange-rate)
    *   [Get Exchange Rate Object Definition](https://developer.intacct.com/api/company-console/exchange-rates/#get-exchange-rate-object-definition)
    *   [Query and List Exchange Rates](https://developer.intacct.com/api/company-console/exchange-rates/#query-and-list-exchange-rates)
    *   [Query and List Exchange Rates (Legacy)](https://developer.intacct.com/api/company-console/exchange-rates/#query-and-list-exchange-rates-legacy)
    *   [Get Exchange Rate](https://developer.intacct.com/api/company-console/exchange-rates/#get-exchange-rate)
    *   [Create Exchange Rate](https://developer.intacct.com/api/company-console/exchange-rates/#create-exchange-rate)
*   [Exchange Rate Entry](https://developer.intacct.com/api/company-console/exchange-rates/#exchange-rate-entry)
    *   [Get Exchange Rate Entry Object Definition](https://developer.intacct.com/api/company-console/exchange-rates/#get-exchange-rate-entry-object-definition)
    *   [Query and List Exchange Rate Entries](https://developer.intacct.com/api/company-console/exchange-rates/#query-and-list-exchange-rate-entries)
    *   [Query and List Exchange Rate Entries (Legacy)](https://developer.intacct.com/api/company-console/exchange-rates/#query-and-list-exchange-rate-entries-legacy)
    *   [Get Exchange Rate Entry](https://developer.intacct.com/api/company-console/exchange-rates/#get-exchange-rate-entry)

* * *

An exchange rate type is a container record to hold the exchange rates (from one currency to another) and subsequently the exchange rate entries.

All companies have the `Intacct Daily Rate`, but this is hidden from the API list and get operations.

* * *

Exchange Rate Type
------------------

### Get Exchange Rate Type Object Definition

#### `lookup`

> List all the fields and relationships for the exchange rate type object:

```
<lookup>
    <object>EXCHANGERATETYPES</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATETYPES` |

* * *

### Query and List Exchange Rate Types

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the ID, name, and default behavior for each exchange rate type:

```
<query>
    <object>EXCHANGERATETYPES</object>
    <select>
        <field>ID</field>
        <field>NAME</field>
        <field>ISDEFAULT</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATETYPES` |
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

### Query and List Exchange Rate Types (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EXCHANGERATETYPES</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATETYPES` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Exchange Rate Type

#### `read`

```
<read>
    <object>EXCHANGERATETYPES</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATETYPES` |
| keys | Required | string | Comma-separated list of exchange rate type `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Exchange Rate Type by ID

#### `readByName`

```
<readByName>
    <object>EXCHANGERATETYPES</object>
    <keys>2</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATETYPES` |
| keys | Required | string | Comma-separated list of object `ID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Exchange Rate
-------------

### Get Exchange Rate Object Definition

#### `lookup`

> List all the fields and relationships for the exchange rate object:

```
<lookup>
    <object>EXCHANGERATE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATE` |

* * *

### Query and List Exchange Rates

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and type name for each exchange rate:

```
<query>
    <object>EXCHANGERATE</object>
    <select>
        <field>RECORDNO</field>
        <field>TYPENAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATE` |
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

### Query and List Exchange Rates (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EXCHANGERATE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Exchange Rate

#### `read`

```
<read>
    <object>EXCHANGERATE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATE` |
| keys | Required | string | Comma-separated list of exchange rate `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Exchange Rate

#### `create`

```
<create>
    <EXCHANGERATE>
        <TYPENAME>Test</TYPENAME>
        <FROM_CURRENCY>CAD</FROM_CURRENCY>
        <TO_CURRENCY>USD</TO_CURRENCY>
        <EXCHANGERATEENTRIES>
            <EXCHANGERATEENTRY>
                <EFFECTIVE_START_DATE>01/12/2015</EFFECTIVE_START_DATE>
                <EXCHANGE_RATE>4.56</EXCHANGE_RATE>
                <RECIPROCAL_RATE></RECIPROCAL_RATE>
            </EXCHANGERATEENTRY>
            <EXCHANGERATEENTRY>
                <EFFECTIVE_START_DATE>02/20/2015</EFFECTIVE_START_DATE>
                <EXCHANGE_RATE>2.63</EXCHANGE_RATE>
                <RECIPROCAL_RATE></RECIPROCAL_RATE>
            </EXCHANGERATEENTRY>
        </EXCHANGERATEENTRIES>
    </EXCHANGERATE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EXCHANGERATE | Required | object | Object to create |

`EXCHANGERATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| TYPENAME | Required | string | Exchange rate type name |
| FROM\_CURRENCY | Required | string | From currency code |
| TO\_CURRENCY | Required | string | To currency code |
| EXCHANGERATEENTRIES | Optional | `EXCHANGERATEENTRY[0...n]` | Exchange rate entries |

`EXCHANGERATEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EFFECTIVE\_START\_DATE | Required | string | Effective Start Date |
| EXCHANGE\_RATE | Required | currency | Exchange rate |
| RECIPROCAL\_RATE | Optional | currency | Reciprocal rate. If left blank Sage Intacct calculates this for you. |

* * *

Exchange Rate Entry
-------------------

### Get Exchange Rate Entry Object Definition

#### `lookup`

> List all the fields and relationships for the exchange rate entry object:

```
<lookup>
    <object>EXCHANGERATEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATEENTRY` |

* * *

### Query and List Exchange Rate Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and exchange rate for each entry:

```
<query>
    <object>EXCHANGERATEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>EXCHANGE_RATE</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATEENTRY` |
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

### Query and List Exchange Rate Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>EXCHANGERATEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Exchange Rate Entry

#### `read`

```
<read>
    <object>EXCHANGERATEENTRY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EXCHANGERATEENTRY` |
| keys | Required | string | Comma-separated list of exchange rate entry `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

