Title: User Groups

URL Source: https://developer.intacct.com/api/company-console/user-groups/

Markdown Content:
*   [User Groups](https://developer.intacct.com/api/company-console/user-groups/#user-groups)
    *   [Get User Group Object Definition](https://developer.intacct.com/api/company-console/user-groups/#get-user-group-object-definition)
    *   [Query and List User Groups](https://developer.intacct.com/api/company-console/user-groups/#query-and-list-user-groups)
    *   [Query and List User Groups (Legacy)](https://developer.intacct.com/api/company-console/user-groups/#query-and-list-user-groups-legacy)
    *   [Get User Group](https://developer.intacct.com/api/company-console/user-groups/#get-user-group)
*   [User Group Members](https://developer.intacct.com/api/company-console/user-groups/#user-group-members)
    *   [Get User Group Member Object Definition](https://developer.intacct.com/api/company-console/user-groups/#get-user-group-member-object-definition)
    *   [Query and List User Group Members](https://developer.intacct.com/api/company-console/user-groups/#query-and-list-user-group-members)
    *   [Query and List User Group Members (Legacy)](https://developer.intacct.com/api/company-console/user-groups/#query-and-list-user-group-members-legacy)
    *   [Get User Group Member](https://developer.intacct.com/api/company-console/user-groups/#get-user-group-member)
*   [User Group Role Assignments](https://developer.intacct.com/api/company-console/user-groups/#user-group-role-assignments)
    *   [Get User Group Role Assignment Object Definition](https://developer.intacct.com/api/company-console/user-groups/#get-user-group-role-assignment-object-definition)
    *   [Query and List User Group Role Assignments](https://developer.intacct.com/api/company-console/user-groups/#query-and-list-user-group-role-assignments)
    *   [Query and List User Group Role Assignments (Legacy)](https://developer.intacct.com/api/company-console/user-groups/#query-and-list-user-group-role-assignments-legacy)
    *   [Get User Group Role Assignment](https://developer.intacct.com/api/company-console/user-groups/#get-user-group-role-assignment)

* * *

User groups organize users into groups, which are useful for managing many users and their permissions at once.

* * *

### Get User Group Object Definition

#### `lookup`

> List all the fields and relationships for the user group object:

```
<lookup>
    <object>USERGROUP</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERGROUP` |

* * *

### Query and List User Groups

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, name, and description for each user group:

```
<query>
    <object>USERGROUP</object>
    <select>
        <field>RECORDNO</field>
        <field>NAME</field>
        <field>DESCR</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERGROUP` |
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

### Query and List User Groups (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>USERGROUP</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERGROUP` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get User Group

#### `read`

```
<read>
    <object>USERGROUP</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERGROUP` |
| keys | Required | string | Comma-separated list of group `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

User Group Members
------------------

### Get User Group Member Object Definition

#### `lookup`

> List all the fields and relationships for the user group member object:

```
<lookup>
    <object>MEMBERUSERGROUP</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `MEMBERUSERGROUP` |

* * *

### Query and List User Group Members

#### [`query`](https://developer.intacct.com/web-services/queries/)

> For each user group member, provide its record number and the user key and login ID of the associated user:

```
<query>
    <object>MEMBERUSERGROUP</object>
    <select>
        <field>RECORDNO</field>
        <field>USERKEY</field>
        <field>USERINFO.LOGINID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `MEMBERUSERGROUP` |
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

### Query and List User Group Members (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>MEMBERUSERGROUP</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `MEMBERUSERGROUP` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get User Group Member

#### `read`

```
<read>
    <object>MEMBERUSERGROUP</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `MEMBERUSERGROUP` |
| keys | Required | string | Comma-separated list of group member `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

User Group Role Assignments
---------------------------

### Get User Group Role Assignment Object Definition

#### `lookup`

> List all the fields and relationships for the user group role assignment object:

```
<lookup>
    <object>ROLEGROUPS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEGROUPS` |

* * *

### Query and List User Group Role Assignments

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each user group role assignment:

```
<query>
    <object>ROLEGROUPS</object>
    <select>
        <field>RECORDNO</field>
        <field>ROLENAME</field>
    </select>
</query>
```

> For each user group role assignment, provide its record number, name, and the login ID of users of this role group role:

```
<query>
    <object>ROLEGROUPS</object>
    <select>
        <field>RECORDNO</field>
        <field>ROLENAME</field>
        <field>ROLES.ROLEUSERS.USERINFO.LOGINID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEGROUPS` |
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

### Query and List User Group Role Assignments (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ROLEGROUPS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEGROUPS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get User Group Role Assignment

#### `read`

```
<read>
    <object>ROLEGROUPS</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEGROUPS` |
| keys | Required | string | Comma-separated list of assignment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

