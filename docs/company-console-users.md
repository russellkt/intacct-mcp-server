Title: Users

URL Source: https://developer.intacct.com/api/company-console/users/

Markdown Content:
*   [Users](https://developer.intacct.com/api/company-console/users/#users)
    *   [Get User Object Definition](https://developer.intacct.com/api/company-console/users/#get-user-object-definition)
    *   [Query and List Users](https://developer.intacct.com/api/company-console/users/#query-and-list-users)
    *   [Query and List Users (Legacy)](https://developer.intacct.com/api/company-console/users/#query-and-list-users-legacy)
    *   [Get User](https://developer.intacct.com/api/company-console/users/#get-user)
    *   [Get User by ID](https://developer.intacct.com/api/company-console/users/#get-user-by-id)
    *   [Create User](https://developer.intacct.com/api/company-console/users/#create-user)
    *   [Update User](https://developer.intacct.com/api/company-console/users/#update-user)
    *   [Delete User](https://developer.intacct.com/api/company-console/users/#delete-user)
*   [User Permissions](https://developer.intacct.com/api/company-console/users/#user-permissions)
    *   [Get User Effective Permissions](https://developer.intacct.com/api/company-console/users/#get-user-effective-permissions)
    *   [Get User Permission Object Definition](https://developer.intacct.com/api/company-console/users/#get-user-permission-object-definition)
    *   [Query and List User Permissions](https://developer.intacct.com/api/company-console/users/#query-and-list-user-permissions)
    *   [Query and List User Permissions (Legacy)](https://developer.intacct.com/api/company-console/users/#query-and-list-user-permissions-legacy)
    *   [Get User Permission](https://developer.intacct.com/api/company-console/users/#get-user-permission)
*   [User Roles](https://developer.intacct.com/api/company-console/users/#user-roles)
    *   [Get User Role Assignment Object Definition](https://developer.intacct.com/api/company-console/users/#get-user-role-assignment-object-definition)
    *   [Query and List User Role Assignments](https://developer.intacct.com/api/company-console/users/#query-and-list-user-role-assignments)
    *   [Query and List User Role Assignments (Legacy)](https://developer.intacct.com/api/company-console/users/#query-and-list-user-role-assignments-legacy)
    *   [Get User Role Assignment](https://developer.intacct.com/api/company-console/users/#get-user-role-assignment)
    *   [Create User Role Assignment](https://developer.intacct.com/api/company-console/users/#create-user-role-assignment)
    *   [Get Computed User Role Assignment Object Definition](https://developer.intacct.com/api/company-console/users/#get-computed-user-role-assignment-object-definition)
    *   [Query and List Computed User Role Assignments](https://developer.intacct.com/api/company-console/users/#query-and-list-computed-user-role-assignments)
    *   [Query and List Computed User Role Assignments (Legacy)](https://developer.intacct.com/api/company-console/users/#query-and-list-computed-user-role-assignments-legacy)
    *   [Get Computed User Role Assignment](https://developer.intacct.com/api/company-console/users/#get-computed-user-role-assignment)
*   [User Restrictions](https://developer.intacct.com/api/company-console/users/#user-restrictions)
    *   [Get User Restriction Object Definition](https://developer.intacct.com/api/company-console/users/#get-user-restriction-object-definition)
    *   [Query and List User Restrictions](https://developer.intacct.com/api/company-console/users/#query-and-list-user-restrictions)
    *   [Query and List User Restrictions (Legacy)](https://developer.intacct.com/api/company-console/users/#query-and-list-user-restrictions-legacy)
    *   [Get User Restrictions](https://developer.intacct.com/api/company-console/users/#get-user-restrictions)
*   [User Date and Time Formatting Preferences](https://developer.intacct.com/api/company-console/users/#user-date-and-time-formatting-preferences)
    *   [List User Date and Time Formatting Preferences](https://developer.intacct.com/api/company-console/users/#list-user-date-and-time-formatting-preferences)

* * *

Any user that needs to sign into Sage Intacct must have a unique user record.

* * *

### Get User Object Definition

#### `lookup`

> List all the fields and relationships for the user object:

```
<lookup>
    <object>USERINFO</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERINFO` |

* * *

### Query and List Users

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the login ID and record number of each active user:

```
<query>
    <object>USERINFO</object>
    <select>
        <field>LOGINID</field>
        <field>RECORDNO</field>
    </select>
    <filter>
        <equalto>
            <field>STATUS</field>
            <value>active</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERINFO` |
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

### Query and List Users (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>USERINFO</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERINFO` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| USERTYPE | Optional | string | User type.
*   `B` - business user
*   `E` - employee user
*   `R` - view only user
*   `W` - writeup user
*   `D` - dashboard user
*   `P` - project manager user
*   `C` - construction manager user
*   `A` - payment approver user
*   `T` - platform user
*   `S` - CRM user
*   `H` - warehouse user

 |

* * *

### Get User

#### `read`

```
<read>
    <object>USERINFO</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERINFO` |
| keys | Required | string | Comma-separated list of user `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get User by ID

#### `readByName`

```
<readByName>
    <object>USERINFO</object>
    <keys>jsmith</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERINFO` |
| keys | Required | string | Comma-separated list of user `LOGINID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create User

When a user is created, it must be associated with a contact. The new user can be associated with a new contact created at the same time, or associated with an existing contact.

Only users with Administrative privileges can create users.

#### `create`

> Create a user with a new contact:

```
<create>
    <USERINFO>
        <LOGINID>jsmith</LOGINID>
        <CONTACTINFO>
            <LASTNAME>John</LASTNAME>
            <FIRSTNAME>Smith</FIRSTNAME>
            <EMAIL1>jsmith@example.com</EMAIL1>
        </CONTACTINFO>
        <DESCRIPTION>John Smith</DESCRIPTION>
        <USERTYPE>business user</USERTYPE>
        <ADMIN>false</ADMIN>
        <STATUS>active</STATUS>
        <SSO_ENABLED>true</SSO_ENABLED>
        <SSO_FEDERATED_ID>jsmith</SSO_FEDERATED_ID>
    </USERINFO>
</create>
```

> Create a user with an existing contact, and set location and department restrictions:

```
<create>
    <USERINFO>
        <LOGINID>jsmith</LOGINID>
        <CONTACTINFO>
            <CONTACTNAME>Smith, John</CONTACTNAME>
        </CONTACTINFO>
        <DESCRIPTION>John Smith</DESCRIPTION>
        <USERTYPE>business user</USERTYPE>
        <ADMIN>false</ADMIN>
        <STATUS>active</STATUS>
        <SSO_ENABLED>true</SSO_ENABLED>
        <SSO_FEDERATED_ID>jsmith</SSO_FEDERATED_ID>
        <USERLOCATIONS>
            <LOCATIONID>San Jose</LOCATIONID>
        </USERLOCATIONS>
        <USERDEPARTMENTS>
            <DEPARTMENTID>01 - AP</DEPARTMENTID>
        </USERDEPARTMENTS>
    </USERINFO>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| USERINFO | Required | object | Object to create |

`USERINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOGINID | Required | string | User ID |
| CONTACTINFO | Required | object | Contact info of user |
| DESCRIPTION | Optional | string | User name. This is usually a concatenation of first and last name |
| USERTYPE | Optional | string | User type.
*   `business user` - default
*   `employee user`
*   `view only user`
*   `dashboard user`
*   `project manager user`
*   `construction manager user`
*   `platform user`
*   `warehouse user`
*   `payment approver` - only for clients of Accountant consoles
*   `CRM user` - user must have \`LOGINDISABLED\` set to true

 |
| STATUS | Optional | string | User status.

*   `active` - default
*   `lockedout`

 |
| LOGINDISABLED | Optional | boolean | This user is a “web services only” user and cannot sign in to the Intacct web application.

*   `false` - default
*   `true`

 |
| SSO\_ENABLED | Optional | boolean | Single sign on enabled.

*   `false` - default
*   `true`

 |
| SSO\_FEDERATED\_ID | Optional | string | SSO federated ID for this user. |
| USERLOCATIONS | Optional | array of `LOCATIONID` | The IDs of locations that this user can access. If not specified, access is not restricted. |
| USERDEPARTMENTS | Optional | array of `DEPARTMENTID` | The IDs of departments that this user can access. If not specified, access is not restricted. |
| USERTERRITORIES | Optional | array of `TERRITORYID` | The IDs of territories that this user can access. If not specified, access is not restricted. |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LASTNAME | Optional | string | Last name. Required if you want to create the user with a new contact. |
| FIRSTNAME | Optional | string | First name. Required if you want to create the user with a new contact. |
| EMAIL1 | Optional | string | Email address. Required if you want to create the user with a new contact. |
| CONTACTNAME | Optional | string | Contact name. Required if you want to create the user with an existing contact. |

* * *

### Update User

When updating a user, you must include the original restrictions for entities, departments, or territories (if any) or they will be deleted. To add a restriction, supply the original restrictions along with the new one. To delete a restriction, supply only the ones you want to keep.

Only users with Administrative privileges can update users. Contact info cannot be changed from the API.

#### `update`

> Update a user’s location and department restrictions:

```
<update>
    <USERINFO>
        <RECORDNO>121</RECORDNO>
        <USERLOCATIONS>
            <LOCATIONID>San Jose</LOCATIONID>
            <LOCATIONID>San Francisco</LOCATIONID>
            <LOCATIONID>Dallas</LOCATIONID>
        </USERLOCATIONS>
        <USERDEPARTMENTS>
            <DEPARTMENTID>01 - AP</DEPARTMENTID>
            <DEPARTMENTID>02 - AR</DEPARTMENTID>
        </USERDEPARTMENTS>
    </USERINFO>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| USERINFO | Required | object | Object to update |

`USERINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of user to update. Required if not using `LOGINID`. |
| LOGINID | Optional | string | Login ID. Required if not using `RECORDNO`. |
| DESCRIPTION | Optional | string | User name, usually concatenation of first and last name |
| USERTYPE | Optional | string | User type.
*   `business user` - default
*   `employee user`
*   `view only user`
*   `dashboard user`
*   `project manager user`
*   `construction manager user`
*   `platform user`
*   `warehouse user`
*   `payment approver` - only for clients of Accountant consoles
*   `CRM user` - user must have \`LOGINDISABLED\` set to true

 |
| STATUS | Optional | string | User status.

*   `active` - default
*   `lockedout`

 |
| LOGINDISABLED | Optional | boolean | This user is a “web services only” user and cannot sign in to the Intacct web application.

*   `false` - default
*   `true`

 |
| SSO\_ENABLED | Optional | boolean | Single sign on enabled.

*   `false` - default
*   `true`

 |
| SSO\_FEDERATED\_ID | Optional | string | SSO federated ID for this user. |
| USERLOCATIONS | Optional | array of `LOCATIONID` | The IDs of locations that this user can access. If not specified, access is not restricted. |
| USERDEPARTMENTS | Optional | array of `DEPARTMENTID` | The IDs of departments that this user can access. If not specified, access is not restricted. |
| USERTERRITORIES | Optional | array of `TERRITORYID` | The IDs of territories that this user can access. If not specified, access is not restricted. |

* * *

### Delete User

Only users with Administrative privileges can delete users. Also, a user with Administrative privileges cannot be deleted—you can use the `update` function to set the user status to `inactive` instead.

#### `delete`

```
<delete>
    <object>USERINFO</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERINFO` |
| keys | Required | string | Comma-separated list of user `RECORDNO` to delete |

* * *

User Permissions
----------------

### Get User Effective Permissions

Effective permissions mean either the specific user-defined permissions or the effective list of permissions derived from role membership.

This function is only available to users who have the Company -\> Lists -\> Users -\> Permissions -\> View permission.

#### `getUserPermissions`

```
<getUserPermissions>
    <userId>Steve</userId>
</getUserPermissions>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| userId | Required | string | User `LOGINID` to get permissions for |

#### Response

The `rights` value is a pipe-delimited list you will need to parse appropriately.

```
<permissions>
    <appSubscription>
        <applicationName>Administration</applicationName>
        <policies>
            <policy>
                <policyName>Application Subscriptions</policyName>
                <rights>List|View|Subscribe|Configure|Remove|Assign Users</rights>
            </policy>
            <policy>
                <policyName>Grant Admin Rights</policyName>
                <rights>Grant</rights>
            </policy>
        </policies>
    </appSubscription>
    <!-- ... -->
</permissions>
```

* * *

### Get User Permission Object Definition

#### `lookup`

> List all the fields and relationships for the user permission object:

```
<lookup>
    <object>USERRIGHTS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRIGHTS` |

* * *

### Query and List User Permissions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and user login ID for each user permission:

```
<query>
    <object>USERRIGHTS</object>
    <select>
        <field>RECORDNO</field>
        <field>USERINFO.LOGINID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRIGHTS` |
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

### Query and List User Permissions (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>USERRIGHTS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRIGHTS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get User Permission

#### `read`

```
<read>
    <object>USERRIGHTS</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRIGHTS` |
| keys | Required | string | Comma-separated list of permission `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

User Roles
----------

### Get User Role Assignment Object Definition

#### `lookup`

> List all the fields and relationships for the user role assignment object:

```
<lookup>
    <object>USERROLES</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERROLES` |

* * *

### Query and List User Role Assignments

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the user ID and role name for each user role for `tsmith`:

```
<query>
    <object>USERROLES</object>
    <select>
        <field>USERID</field>
        <field>ROLENAME</field>
    </select>
    <filter>
        <equalto>
            <field>USERID</field>
            <value>tsmith</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERROLES` |
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

### Query and List User Role Assignments (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>USERROLES</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERROLES` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get User Role Assignment

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
| keys | Required | string | Comma-separated list of assignment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create User Role Assignment

Only users with Administrative privileges can create user role assignments.

#### `create`

```
<create>
    <USERROLES>
        <USERID>jsmith</USERID>
        <ROLENAME>Accountant</ROLENAME>
    </USERROLES>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| USERROLES | Required | object | Object to create |

`USERROLES`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| USERID | Required | string | User ID |
| ROLENAME | Required | string | Role name to assign to user |

* * *

### Get Computed User Role Assignment Object Definition

#### `lookup`

> List all the fields and relationships for the computed user role assignment object:

```
<lookup>
    <object>ROLEUSERS</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEUSERS` |

* * *

### Query and List Computed User Role Assignments

User role assignments can either come from direct assignment on the user, or inherited from a user group.

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the user login ID and role name for each computed role assignment:

```
<query>
    <object>ROLEUSERS</object>
    <select>
        <field>USERLOGINID</field>
        <field>ROLENAME</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEUSERS` |
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

### Query and List Computed User Role Assignments (Legacy)

User role assignments can either come from direct assignment on the user, or inherited from a user group.

#### `readByQuery`

```
<readByQuery>
    <object>ROLEUSERS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEUSERS` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Computed User Role Assignment

User role assignments can either come from direct assignment on the user, or inherited from a user group.

#### `read`

```
<read>
    <object>ROLEUSERS</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ROLEUSERS` |
| keys | Required | string | Comma-separated list of assignment `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

User Restrictions
-----------------

### Get User Restriction Object Definition

#### `lookup`

> List all the fields and relationships for the user restriction object:

```
<lookup>
    <object>USERRESTRICTION</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRESTRICTION` |

* * *

### Query and List User Restrictions

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the login ID and user type for each user restriction:

```
<query>
    <object>USERRESTRICTION</object>
    <select>
        <field>LOGINID</field>
        <field>USERTYPE</field>
    </select>
</query>
```

> List the login ID and location ID for each user restriction by location:

```
<query>
    <object>USERRESTRICTION</object>
    <select>
        <field>LOGINID</field>
        <field>LOCATIONID</field>
    </select>
    <filter>
        <equalto>
            <field>UNRESTRICTED</field>
            <value>false</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRESTRICTION` |
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

#### Response

A user restriction object is returned for each user found. If a user’s access is not limited by location or department, `UNRESTRICTED` is `true`. If a user is limited to certain locations or departments, `UNRESTRICTED` is `false` and those locations or departments are not empty.

```
<USERRESTRICTION>
    <LOGINID>jsmith</LOGINID>
    <RECORDNO>103</RECORDNO>
    <USERTYPE>business user</USERTYPE>
    <UNRESTRICTED>true</UNRESTRICTED>
    <LOCATIONID></LOCATIONID>
</USERRESTRICTION>
<USERRESTRICTION>
    <LOGINID>jjones</LOGINID>
    <RECORDNO>104</RECORDNO>
    <USERTYPE>business user</USERTYPE>
    <UNRESTRICTED>false</UNRESTRICTED>
    <LOCATIONID>9</LOCATIONID>
</USERRESTRICTION>
```

* * *

### Query and List User Restrictions (Legacy)

Users can be restricted to given departments or locations.

Only users with Administrative privileges can list or get user restrictions.

#### `readByQuery`

> List user restrictions for all users:

```
<readByQuery>
    <object>USERRESTRICTION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List user restrictions for users that are limited to the designated location:

```
<readByQuery>
    <object>USERRESTRICTION</object>
    <fields>*</fields>
    <query>LOCATIONID = 9</query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRESTRICTION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

#### Response

A user restriction object is returned for each user found. If a user’s access is not limited by location or department, `UNRESTRICTED` is `true`. If a user is limited to certain locations or departments, `UNRESTRICTED` is `false` and the locations and departments that the user _can_ access are listed.

```
<userrestriction>
    <RECORDNO>103</RECORDNO>
    <LOGINID>jsmith</LOGINID>
    <FIRSTNAME>John</FIRSTNAME>
    <LASTNAME>Smith</LASTNAME>
    <ADMIN>Full</ADMIN>
    <USERTYPE>business user</USERTYPE>
    <STATUS>active</STATUS>
    <UNRESTRICTED>true</UNRESTRICTED>
</userrestriction>
<userrestriction>
    <RECORDNO>104</RECORDNO>
    <LOGINID>jjones</LOGINID>
    <FIRSTNAME>Jen</FIRSTNAME>
    <LASTNAME>Jones</LASTNAME>
    <ADMIN>Off</ADMIN>
    <USERTYPE>business user</USERTYPE>
    <STATUS>active</STATUS>
    <UNRESTRICTED>false</UNRESTRICTED>
    <LOCATIONS>
        <LOCATION>
            <LOCATIONID>9</LOCATIONID>
            <LOCATIONNAME>France</LOCATIONNAME>
        </LOCATION>
    </LOCATIONS>
    <DEPARTMENTS>
        <DEPARTMENT>
            <DEPARTMENTID>DOC</DEPARTMENTID>
            <DEPARTMENTNAME>Documentation</DEPARTMENTNAME>
        </DEPARTMENT>
    </DEPARTMENTS>
</userrestriction>
```

* * *

### Get User Restrictions

#### `read`

```
<read>
    <object>USERRESTRICTION</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `USERRESTRICTION` |
| keys | Required | string | Comma-separated list of user restriction `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

User Date and Time Formatting Preferences
-----------------------------------------

### List User Date and Time Formatting Preferences

Returns the user preferences for date and time format, locale, timezone (GMT offset), and time clock (12 or 24). The locale, such as en\_US, is also returned.

#### `readUserFormatting`

```
<readUserFormatting>
    <key>177</key>
</readUserFormatting>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Optional | string | User `RECORDNO` for which to get formatting information. Required if not using `userId`. |
| userId | Optional | string | User `LOGINID` for which to get formatting information. Required if not using `key`. |

#### Response

`userformatting`

> The above function returns data structured like this:

```
<userformatting>
    <recordno>48</recordno>
    <locale>en_US</locale>
    <dateformat>.ymd</dateformat>
    <gmtoffset>+09:30</gmtoffset>
    <clock>12</clock>
</userformatting>
```

##### Parameters

| Name | Type | Description |
| --- | --- | --- |
| recordno | integer | Record number of the user |
| locale | string | Locale described as _`language_countrycode`_, such as `en_US` |
| dateformat | string | Date format indicated by four characters. The first character is the separator, the last three characters are `m` for the month, `d` for the day, `y` for the year in a two-digit format, or `Y` for the year in a four-digit format. The order of the last three characters indicates the ordering in the format. For example, a format of `.mdy` indicates MM.DD.YY and a format of `-Ymd` indicates YYYY-MM-DD. |
| gmtoffset | string | GMT offset in format `+/- hh:mm` |
| clock | integer | Time clock used for hours, either 12 or 24. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

