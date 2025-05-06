Title: Labor Class, Shift, and Union

URL Source: https://developer.intacct.com/api/construction/labor-class-shift-union/

Markdown Content:
*   [Labor Classes](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-classes)
    *   [Get labor Class Object Definition](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-labor-class-object-definition)
    *   [Query and List Labor Classes](https://developer.intacct.com/api/construction/labor-class-shift-union/#query-and-list-labor-classes)
    *   [Query and List Labor Classes (Legacy)](https://developer.intacct.com/api/construction/labor-class-shift-union/#query-and-list-labor-classes-legacy)
    *   [Get a Labor Class](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-a-labor-class)
    *   [Get a Labor Class by ID](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-a-labor-class-by-id)
    *   [Create Labor Class](https://developer.intacct.com/api/construction/labor-class-shift-union/#create-labor-class)
    *   [Update a Labor Class](https://developer.intacct.com/api/construction/labor-class-shift-union/#update-a-labor-class)
    *   [Delete Labor Class](https://developer.intacct.com/api/construction/labor-class-shift-union/#delete-labor-class)
*   [Labor Shifts](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-shifts)
    *   [Get labor Shift Object Definition](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-labor-shift-object-definition)
    *   [Query and List Labor Shifts](https://developer.intacct.com/api/construction/labor-class-shift-union/#query-and-list-labor-shifts)
    *   [Query and List Labor Shifts (Legacy)](https://developer.intacct.com/api/construction/labor-class-shift-union/#query-and-list-labor-shifts-legacy)
    *   [Get a Labor Shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-a-labor-shift)
    *   [Get a Labor Shift by ID](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-a-labor-shift-by-id)
    *   [Create Labor Shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#create-labor-shift)
    *   [Update a Labor Shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#update-a-labor-shift)
    *   [Delete Labor Shift](https://developer.intacct.com/api/construction/labor-class-shift-union/#delete-labor-shift)
*   [Labor Unions](https://developer.intacct.com/api/construction/labor-class-shift-union/#labor-unions)
    *   [Get labor Union Object Definition](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-labor-union-object-definition)
    *   [Query and List Labor Unions](https://developer.intacct.com/api/construction/labor-class-shift-union/#query-and-list-labor-unions)
    *   [Query and List Labor Unions (Legacy)](https://developer.intacct.com/api/construction/labor-class-shift-union/#query-and-list-labor-unions-legacy)
    *   [Get a Labor Union](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-a-labor-union)
    *   [Get a Labor Union by ID](https://developer.intacct.com/api/construction/labor-class-shift-union/#get-a-labor-union-by-id)
    *   [Create Labor Union](https://developer.intacct.com/api/construction/labor-class-shift-union/#create-labor-union)
    *   [Update a Labor Union](https://developer.intacct.com/api/construction/labor-class-shift-union/#update-a-labor-union)
    *   [Delete Labor Union](https://developer.intacct.com/api/construction/labor-class-shift-union/#delete-labor-union)

* * *

You can define labor class, shift, and union objects that can be applied to timesheets and used to determine billing rates and markups for employees.

* * *

Labor Classes
-------------

### Get labor Class Object Definition

#### `lookup`

> List all the fields and relationships for the labor class object:

```
<lookup>
    <object>LABORCLASS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORCLASS` |

* * *

### Query and List Labor Classes

#### `query`

> List the record number, labor class ID, and name for each labor class:

```
<query>
    <object>LABORCLASS</object>
    <select>
        <field>RECORDNO</field>
        <field>LABORCLASSID</field>
        <field>NAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORCLASS` |
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

### Query and List Labor Classes (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>LABORCLASS</object>
    <fields>*</fields>
    <query/>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORCLASS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get a Labor Class

#### `read`

```
<read>
    <object>LABORCLASS</object>
    <keys>66</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORCLASS` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the labor class to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get a Labor Class by ID

#### `readByName`

```
<readByName>
    <object>LABORCLASS</object>
    <keys>PCO-66</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORCLASS` |
| keys | Required | string | Comma-separated list of `LABORCLASSID` of the labor class to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Labor Class

#### `create`

```
<create>
    <LABORCLASS>
        <LABORCLASSID>LC001</LABORCLASSID>
        <NAME>Labor Class 001</NAME>
        <DESCRIPTION>Supervisors</DESCRIPTION>
    </LABORCLASS>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `LABORCLASS` | Required | object | Object type to create. |

`LABORCLASS`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LABORCLASSID | Required | string | User-defined unique ID of the labor class. |
| NAME | Required | string | Name of the labor class. |
| DESCRIPTION | Optional | string | Description of the labor class. |
| STATUS | Optional | enum | Whether this labor class is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update a Labor Class

#### `update`

```
<update>
    <LABORCLASS>
        <LABORCLASSID>PCO-66</LABORCLASSID>
        <NAME>Labor Class 001b</NAME>
    </LABORCLASS>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `LABORCLASS` | Required | object | Object type to update. |

`LABORCLASS`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | `RECORDNO` of the labor class to update. Required if not including `LABORCLASSID`. |
| LABORCLASSID | Optional | string | `LABORCLASSID` of the labor class to update. Required if not including `RECORDNO`. |
| NAME | Optional | string | Name of the labor class. |
| DESCRIPTION | Optional | string | Description of the labor class. |
| STATUS | Optional | enum | Whether this labor class is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Labor Class

#### `delete`

```
<delete>
    <object>LABORCLASS</object>
    <keys>66</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORCLASS` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the labor class to delete. |

* * *

Labor Shifts
------------

### Get labor Shift Object Definition

#### `lookup`

> List all the fields and relationships for the labor shift object:

```
<lookup>
    <object>LABORSHIFT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORSHIFT` |

* * *

### Query and List Labor Shifts

#### `query`

> List the record number, name, and labor shift ID for each labor shift:

```
<query>
    <object>LABORSHIFT</object>
    <select>
        <field>RECORDNO</field>
        <field>LABORSHIFTID</field>
        <field>NAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORSHIFT` |
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

### Query and List Labor Shifts (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>LABORSHIFT</object>
    <fields>*</fields>
    <query/>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORSHIFT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get a Labor Shift

#### `read`

```
<read>
    <object>LABORSHIFT</object>
    <keys>66</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORSHIFT` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the labor shift to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get a Labor Shift by ID

#### `readByName`

```
<readByName>
    <object>LABORSHIFT</object>
    <keys>PCO-66</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORSHIFT` |
| keys | Required | string | Comma-separated list of `LABORSHIFTID` of the labor shift to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Labor Shift

#### `create`

```
<create>
    <LABORSHIFT>
        <LABORSHIFTID>LS002</LABORSHIFTID>
        <NAME>Shift 2</NAME>
        <DESCRIPTION>Second shift (2pm-10pm)</DESCRIPTION>
    </LABORSHIFT>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `LABORSHIFT` | Required | object | Object type to create. |

`LABORSHIFT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LABORSHIFTID | Required | string | User-defined unique ID of the labor shift. |
| NAME | Required | string | Name of the labor shift. |
| DESCRIPTION | Optional | string | Description of the labor shift. |
| STATUS | Optional | enum | Whether this labor shift is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update a Labor Shift

#### `update`

```
<update>
    <LABORSHIFT>
        <LABORSHIFTID>LS002</LABORSHIFTID>
        <DESCRIPTION>Second shift (1pm-9pm)</DESCRIPTION>
    </LABORSHIFT>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `LABORSHIFT` | Required | object | Object type to update. |

`LABORSHIFT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | `RECORDNO` of the labor shift to update. Required if not including `LABORSHIFTID`. |
| LABORSHIFTID | Optional | string | `LABORSHIFTID` of the labor shift to update. Required if not including `RECORDNO`. |
| NAME | Optional | string | Name of the labor shift. |
| DESCRIPTION | Optional | string | Description of the labor shift. |
| STATUS | Optional | enum | Whether this labor shift is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Labor Shift

#### `delete`

```
<delete>
    <object>LABORSHIFT</object>
    <keys>66</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORSHIFT` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the labor shift to delete |

* * *

Labor Unions
------------

### Get labor Union Object Definition

#### `lookup`

> List all the fields and relationships for the labor union object:

```
<lookup>
    <object>LABORUNION</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORUNION` |

* * *

### Query and List Labor Unions

#### `query`

> List the record number, name, and labor union ID for each labor union:

```
<query>
    <object>LABORUNION</object>
    <select>
        <field>RECORDNO</field>
        <field>LABORUNIONID</field>
        <field>NAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORUNION` |
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

### Query and List Labor Unions (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>LABORUNION</object>
    <fields>*</fields>
    <query/>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORUNION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get a Labor Union

#### `read`

```
<read>
    <object>LABORUNION</object>
    <keys>66</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORUNION` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the labor union to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get a Labor Union by ID

#### `readByName`

```
<readByName>
    <object>LABORUNION</object>
    <keys>PCO-66</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORUNION` |
| keys | Required | string | Comma-separated list of `LABORUNIONID` of the labor union to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Labor Union

#### `create`

```
<create>
    <LABORUNION>
        <LABORUNIONID>IBEWC</LABORUNIONID>
        <NAME>International Brotherhood of Electrical Workers</NAME>
        <DESCRIPTION>IBEW - Chicago</DESCRIPTION>
    </LABORUNION>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `LABORUNION` | Required | object | Object type to create. |

`LABORUNION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LABORUNIONID | Required | string | User-defined unique ID of the labor union. |
| NAME | Required | string | Name of the labor union. |
| DESCRIPTION | Optional | string | Description of the labor union. |
| STATUS | Optional | enum | Whether this labor union is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Update a Labor Union

#### `update`

```
<update>
    <LABORUNION>
        <LABORUNIONID>IBEWC</LABORUNIONID>
        <DESCRIPTION>IBEW - Central</DESCRIPTION>
    </LABORUNION>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `LABORUNION` | Required | object | Object type to update. |

`LABORUNION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | `RECORDNO` of the labor union to update. Required if not including `LABORUNIONID`. |
| LABORUNIONID | Optional | string | `LABORUNIONID` of the labor union to update. Required if not including `RECORDNO`. |
| NAME | Optional | string | Name of the labor union. |
| DESCRIPTION | Optional | string | Description of the labor unio . |
| STATUS | Optional | enum | Whether this labor union is active and can be assigned to employees.
*   `active` (default)
*   `inactive`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

### Delete Labor Union

#### `delete`

```
<delete>
    <object>LABORUNION</object>
    <keys>66</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LABORUNION`. |
| keys | Required | string | Comma-separated list of `RECORDNO` of the labor union to delete. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

