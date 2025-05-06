Title: Records

URL Source: https://developer.intacct.com/api/platform-services/records/

Markdown Content:
*   [Get Object Definitions](https://developer.intacct.com/api/platform-services/records/#get-object-definitions)
*   [Query and List Records](https://developer.intacct.com/api/platform-services/records/#query-and-list-records)
*   [Query and List Records (Legacy)](https://developer.intacct.com/api/platform-services/records/#query-and-list-records-legacy)
*   [Get Record](https://developer.intacct.com/api/platform-services/records/#get-record)
*   [Get Record by ID](https://developer.intacct.com/api/platform-services/records/#get-record-by-id)
*   [Create Record](https://developer.intacct.com/api/platform-services/records/#create-record)
*   [Update Record](https://developer.intacct.com/api/platform-services/records/#update-record)
*   [Delete Record](https://developer.intacct.com/api/platform-services/records/#delete-record)
*   [File Type Fields on Custom Objects](https://developer.intacct.com/api/platform-services/records/#file-type-fields-on-custom-objects)
*   [Get Related Records](https://developer.intacct.com/api/platform-services/records/#get-related-records)

* * *

A record is an instance of a custom or a standard object.

* * *

Get Object Definitions
----------------------

#### `lookup`

> List all the fields and relationships for the vendor standard object:

```
<lookup>
    <object>VENDOR</object>
</lookup>
```

> List all the fields and relationships for the MCA\_attendee custom object:

```
<lookup>
    <object>MCA_attendee</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Object type to list. |

* * *

Query and List Records
----------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List vendor standard object records:

```
<query>
    <object>VENDOR</object>
    <select>
        <field>RECORDNO</field>
        <field>TOTALDUE</field>
    </select>
</query>
```

> List MCA\_attendee custom object records where the related customer (via R\_attendee\_customer relationship) owes more than 5,000.

```
<query>
    <object>MCA_attendee</object>
    <select>
        <field>NAME</field>
        <field>R_attendee_customer.CUSTOMERID</field>
    </select>
    <filter>
        <greaterthan>
            <field>R_attendee_customer.TOTALDUE</field>
            <value>5000</value>
        </greaterthan>
    </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Object type to query. |
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

Query and List Records (Legacy)
-------------------------------

#### `readByQuery`

> List vendor standard object records:

```
<readByQuery>
    <object>VENDOR</object>
    <fields>*</fields>
    <query>STATUS = 'T'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List MCA\_attendee custom object records:

```
<readByQuery>
    <object>MCA_attendee</object>
    <fields>*</fields>
    <query>id &gt;= 10000</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Object type to query. |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| docparid | Optional | string | Used for `SODOCUMENT`, `PODOCUMENT`, or `INVDOCUMENT` records to indicate the document type. You must use this to take advantage of any custom fields on the specified document type. |

* * *

Get Record
----------

#### `Read`

> Get standard object record:

```
<read>
    <object>VENDOR</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

> Get custom object record:

```
<read>
    <object>MCA_attendee</object>
    <keys>10001</keys>
    <fields>*</fields>
</read>
```

> Get multiple standard object records:

```
<read>
    <object>VENDOR</object>
    <keys>1,2,3,9</keys>
    <fields>*</fields>
</read>
```

> Get multiple custom object records:

```
<read>
    <object>MCA_attendee</object>
    <keys>10001,10009,10015</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Object type to get. |
| keys | Required | string | Comma-separated list of object record keys to get. Standard objects use the `RECORDNO` otherwise custom objects use the `id`. Keys must be comma separated, max count of 100 keys. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used for `SODOCUMENT` and `PODOCUMENT` records to indicate the document type. You must use this to take advantage of any custom fields on the specified document type. |

* * *

Get Record by ID
----------------

#### `readByName`

```
<readByName>
    <object>VENDOR</object>
    <keys>V1234</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Object type to get. |
| keys | Required | string | Comma-separated list of record IDs or names to get. For custom object use `name`. This field varies for standard objects. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |
| docparid | Optional | string | Used for `SODOCUMENT` and `PODOCUMENT` records to indicate the document type. You must use this to take advantage of any custom fields on the specified document type. |

* * *

Create Record
-------------

#### `create`

> Create a standard object record:

```
<create>
    <VENDOR>
        <VENDORID>Unit - A-1208</VENDORID>
        <NAME>this is the name8</NAME>
        <VCF_BILL_SITEID3>FOOBAR8</VCF_BILL_SITEID3>
    </VENDOR>
</create>
```

> Create a custom object record:

```
<create>
    <api_test_record>
        <name>foobar1</name>
        <api_checkbox>true</api_checkbox>
        <api_currency>4.99</api_currency>
        <api_date>2009-05-26</api_date>
        <api_datetime>2009-05-26T12:01:01Z</api_datetime>
        <api_time>12:01:01</api_time>
        <api_decimal>10.3844</api_decimal>
        <api_email>noreply@intacct.com</api_email>
        <api_integer>123</api_integer>
        <api_percent>50.01</api_percent>
        <api_picklist>green</api_picklist>
        <api_picklistmulti>red,green</api_picklistmulti>
        <api_radio>green</api_radio>
        <api_checkboxes>red,green</api_checkboxes>
        <api_text>This is sample text 2</api_text>
        <api_textarea>This is text area
            this is a new line itext area</api_textarea>
        <api_url>https://www.intacct.com</api_url>
    </api_test_record>
</create>
```

> Create multiple standard and custom object records:

```
<create>
    <VENDOR>
        <VENDORID>Unit - A-1208</VENDORID>
        <NAME>this is the name8</NAME>
        <VCF_BILL_SITEID3>FOOBAR8</VCF_BILL_SITEID3>
    </VENDOR>
    <CUSTOMER>
        <CUSTOMERID>XML121</CUSTOMERID>
        <NAME>XML Customer 111</NAME>
    </CUSTOMER>
    <asset>
        <serial_number>123456789</serial_number>
        <date_placed_in_servi>08/10/2009</date_placed_in_servi>
        <date_of_disposition>10/12/2009</date_of_disposition>
        <asset_cost>123.45</asset_cost>
        <salvage_percentage>0.01</salvage_percentage>
        <Rasset_class>No class</Rasset_class>
    </asset>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| _object type_ | Required | object\[1…100\] | Object types to create. Max 100 records. Records of different types can be used. |

**Note:** See the [FAQ](https://developer.intacct.com/support/faq/#how-do-i-set-relationship-values-for-dimensions-custom-objects-or-standard-objects) for more examples that set relationship values.

* * *

Update Record
-------------

#### `update`

> Update a standard object record:

```
<update>
    <VENDOR>
        <RECORDNO>202</RECORDNO>
        <VCF_BILL_SITEID3>foobar 2</VCF_BILL_SITEID3>
    </VENDOR>
</update>
```

> Update a custom object record:

```
<update>
    <api_test_record>
        <id>34923</id>
        <name>updated hello world</name>
    </api_test_record>
</update>
```

> Update multiple standard and custom object records:

```
<update>
    <CUSTOMER>
        <RECORDNO>141</RECORDNO>
        <NAME>XML Customer 190</NAME>
    </CUSTOMER>
    <VENDOR>
        <RECORDNO>202</RECORDNO>
        <VCF_BILL_SITEID3>foobar 2</VCF_BILL_SITEID3>
    </VENDOR>
    <asset>
        <id>1355196</id>
        <serial_number>123456789</serial_number>
        <asset_cost>499.95</asset_cost>
    </asset>
</update>
```

> Update standard object record to set the value of a to-one relationship to a custom object record:

```
<update>
    <APBILL>
        <RECORDNO>259</RECORDNO>
        <RTEST_OBJECT>10027</RTEST_OBJECT>
    </APBILL>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| _object type_ | Required | object\[1…100\] | Type of object to update. Max 100 records. Records of different types can be used. |

**Note:** See the [FAQ](https://developer.intacct.com/support/faq/#how-do-i-set-relationship-values-for-dimensions-custom-objects-or-standard-objects) for more examples that set relationship values.

* * *

Delete Record
-------------

#### `delete`

> Delete a standard object record:

```
<delete>
    <object>VENDOR</object>
    <keys>1</keys>
</delete>
```

> Delete a custom object record:

```
<delete>
    <object>api_test_record</object>
    <keys>41145</keys>
</delete>
```

> Delete multiple standard object records:

```
<delete>
    <object>VENDOR</object>
    <keys>1,2,3,4</keys>
</delete>
```

> Delete multiple custom object records:

```
<delete>
    <object>api_test_record</object>
    <keys>41145,41146,41147</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Object type to delete. |
| keys | Required | string | Comma-separated list of object record keys to delete. Standard objects use the `RECORDNO` otherwise custom objects use the `id`. Keys must be comma separated, max count of 100 keys. |

* * *

File Type Fields on Custom Objects
----------------------------------

Setting an object to a file type field enables three fields for use on your object.

#### `OBJECT`

```
<MY_ACH_OBJECT>
    <ACHEFTFILE_contenttype>text/plain</ACHEFTFILE_contenttype>
    <ACHEFTFILE_filename>helloworld.txt</ACHEFTFILE_filename>
    <ACHEFTFILE>aGVsbG8gd29ybGQhIHRoaXMgaXMgYmFzZTY0IGVuY29kZWQgZGF0YQ==</ACHEFTFILE>
</MY_ACH_OBJECT>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FIELDNAME\_contenttype | Required | string | MIME type of file |
| FIELDNAME\_filename | Required | string | Filename of file |
| FIELDNAME | Required | string | Base64 encoded data of the file |

* * *

This will retrieve records related to one or more records by a given relationship.

Please note this only works on **custom objects**.

```
<readRelated>
    <object>asset</object>
    <keys>1160471</keys>
    <relation>Rasset_class</relation>
    <fields>*</fields>
</readRelated>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Custom object type to get. |
| relation | Required | string | Name of relation to follow from the given keys. |
| keys | Required | string | Comma-separated list of custom object record `id` to get. Keys must be comma separated, max count of 100 keys. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

