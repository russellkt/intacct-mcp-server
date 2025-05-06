Title: Roles

URL Source: https://developer.intacct.com/api/company-console/roles/

Markdown Content:
*   [Roles](https://developer.intacct.com/api/company-console/roles/#roles)
    *   [Get Role Object Definition](https://developer.intacct.com/api/company-console/roles/#get-role-object-definition)
    *   [Query and List Roles](https://developer.intacct.com/api/company-console/roles/#query-and-list-roles)
    *   [Query and List Roles (Legacy)](https://developer.intacct.com/api/company-console/roles/#query-and-list-roles-legacy)
    *   [Get Role](https://developer.intacct.com/api/company-console/roles/#get-role)
    *   [Get Role by ID](https://developer.intacct.com/api/company-console/roles/#get-role-by-id)
*   [Role Assignments](https://developer.intacct.com/api/company-console/roles/#role-assignments)
    *   [Get Role Assignment Object Definition](https://developer.intacct.com/api/company-console/roles/#get-role-assignment-object-definition)
    *   [Query and List Role Assignments](https://developer.intacct.com/api/company-console/roles/#query-and-list-role-assignments)
    *   [Query and List Role Assignments (Legacy)](https://developer.intacct.com/api/company-console/roles/#query-and-list-role-assignments-legacy)
    *   [Get Role Assignment](https://developer.intacct.com/api/company-console/roles/#get-role-assignment)
*   [Role Permissions](https://developer.intacct.com/api/company-console/roles/#role-permissions)
    *   [Get Role Permission Object Definition](https://developer.intacct.com/api/company-console/roles/#get-role-permission-object-definition)
    *   [Query and List Role Permissions](https://developer.intacct.com/api/company-console/roles/#query-and-list-role-permissions)
    *   [Query and List Role Permissions (Legacy)](https://developer.intacct.com/api/company-console/roles/#query-and-list-role-permissions-legacy)
    *   [Get Role Permission](https://developer.intacct.com/api/company-console/roles/#get-role-permission)

* * *

Roles can be defined for various job functions.

Permissions to perform certain tasks can be assigned to specific roles, and roles can then be assigned to users or user groups.

* * *

### Get Role Object Definition

#### `lookup`

> List all the fields and relationships for the role object:

```
<lookup>
    <object>ROLES</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLES` |

* * *

### Query and List Roles

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name of each role:

```
<query>
    <object>ROLES</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
    </select>
</query>
```

> List the record number and name of each role that is used by the user with the login ID `jsmith`:

```
<query>
    <object>ROLES</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
        <field>ROLEUSERS.USERLOGINID</field>
    </select>
    <filter>
        <equalto>
            <field>ROLEUSERS.USERLOGINID</field>
            <value>jsmith</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLES` |
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

### Query and List Roles (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ROLES</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLES` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Role

#### `read`

```
<read>
    <object>ROLES</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLES` |
| keys | Required | string | Comma-separated list of role `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Role by ID

#### `readByName`

```
<readByName>
    <object>ROLES</object>
    <keys>Accountant</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLES` |
| keys | Required | string | Comma-separated list of tser `LOGINID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Role Assignments
----------------

### Get Role Assignment Object Definition

#### `lookup`

> List all the fields and relationships for the role assignment object:

```
<lookup>
    <object>ROLEASSIGNMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEASSIGNMENT` |

* * *

### Query and List Role Assignments

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and role name for each role assignment:

```
<query>
    <object>ROLEASSIGNMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>ROLENAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEASSIGNMENT` |
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

### Query and List Role Assignments (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ROLEASSIGNMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEASSIGNMENT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Role Assignment

#### `read`

```
<read>
    <object>ROLEASSIGNMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEASSIGNMENT` |
| keys | Required | string | Comma-separated list of assignment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Role Permissions
----------------

### Get Role Permission Object Definition

#### `lookup`

> List all the fields and relationships for the role permission object for Sage Intacct subscriptions:

```
<lookup>
    <object>ROLEPOLICYASSIGNMENT</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEPOLICYASSIGNMENT` for Sage Intacct subscriptions, otherwise use `CUSTOMROLEPOLASSIGNMENT` for platform applications. |

* * *

### Query and List Role Permissions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, policy name, and role name for each role permission:

```
<query>
    <object>ROLEPOLICYASSIGNMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>POLICYNAME</field>
        <field>ROLES.NAME</field>
    </select>
</query>
```

> List the record number, key, and name for each role permission in any Platform applications:

```
<query>
    <object>CUSTOMROLEPOLASSIGNMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>CUSTAPPKEY</field>
        <field>CUSTAPPNAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEPOLICYASSIGNMENT` for Sage Intacct subscriptions, otherwise use `CUSTOMROLEPOLASSIGNMENT` for platform applications. |
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

### Query and List Role Permissions (Legacy)

#### `readByQuery`

> List role permissions for Sage Intacct subscriptions:

```
<readByQuery>
    <object>ROLEPOLICYASSIGNMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List role permissions for platform applications:

```
<readByQuery>
    <object>CUSTOMROLEPOLASSIGNMENT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEPOLICYASSIGNMENT` for Sage Intacct subscriptions, otherwise use `CUSTOMROLEPOLASSIGNMENT` for platform applications. |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Role Permission

#### `read`

> Get role permission for Sage Intacct subscriptions:

```
<read>
<object>ROLEPOLICYASSIGNMENT</object>
<keys>1</keys>
<fields>*</fields>
</read>
```

> Get role permission for platform applications:

```
<read>
    <object>CUSTOMROLEPOLASSIGNMENT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEPOLICYASSIGNMENT` for Sage Intacct subscriptions, otherwise use `CUSTOMROLEPOLASSIGNMENT` for platform applications. |
| keys | Required | string | Comma-separated list of role permission `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

