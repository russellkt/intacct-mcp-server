Title: Vendor Compliance Types

URL Source: https://developer.intacct.com/api/purchasing/vendor-compliance-types/

Markdown Content:
*   [Get Vendor Compliance Type Object Definition](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#get-vendor-compliance-type-object-definition)
*   [Query and List Vendor Compliance Types](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#query-and-list-vendor-compliance-types)
*   [Query and List Vendor Compliance Types (Legacy)](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#query-and-list-vendor-compliance-types-legacy)
*   [Get Vendor Compliance Types](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#get-vendor-compliance-types)
*   [Get Vendor Compliance Types by ID](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#get-vendor-compliance-types-by-id)
*   [Create a Vendor Compliance Type](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#create-a-vendor-compliance-type)
*   [Update a Vendor Compliance Type](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#update-a-vendor-compliance-type)
*   [Delete a Vendor Compliance Type](https://developer.intacct.com/api/purchasing/vendor-compliance-types/#delete-a-vendor-compliance-type)

* * *

Vendor compliance is the validation that a subcontractor or vendor has provided documents required for a job. For example, the vendor might need to supply proof of insurance, certified reports, lien waivers, or other misc documents like permits, licenses, and so forth.

Use **compliance types** to name a specific requirement that you want to track, such as “General Liability Insurance,” based on a [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/). Compliance types are used to create [compliance records](https://developer.intacct.com/api/purchasing/vendor-compliance-records/) for vendors.

NOTE: To enable the Vendor Compliance subscription, first enable Accounts Payable, Purchasing, and Construction. Vendor compliance is available only for Construction at this time.

* * *

Get Vendor Compliance Type Object Definition
--------------------------------------------

#### `lookup`

> List all the fields and relationships for the vendor compliance type object:

```
<lookup>
    <object>COMPLIANCETYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCETYPE` |

* * *

Query and List Vendor Compliance Types
--------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the specified fields for each vendor compliance type where the status is active:

```
<query>
    <object>COMPLIANCETYPE</object>
    <select>
        <field>RECORDNO</field>
        <field>COMPLIANCETYPEID</field>
        <field>NAME</field>
        <field>STATUS</field>
        <field>COMPLIANCETEMPLATE</field>
        <field>FINALCOMPLIANCETEMPLATE</field>
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
| object | Required | string | Use `COMPLIANCETYPE` |
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

Query and List Vendor Compliance Types (Legacy)
-----------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>COMPLIANCETYPE</object>
    <fields>RECORDNO, COMPLIANCETYPEID, NAME, STATUS, COMPLIANCETEMPLATE, FINALCOMPLIANCETEMPLATE</fields>
    <query>NAME = 'COMPTYPE-01'</query>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCETYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

#### `read`

> Get all vendor compliance type fields for the specified keys:

```
<read>
    <object>COMPLIANCETYPE</object>
    <fields>*</fields>
    <keys>68</keys>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCETYPE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Vendor Compliance Types by ID
---------------------------------

#### `readByName`

```
<readByName>
    <object>COMPLIANCETYPE</object>
    <keys>GL-Insurance</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCETYPE` |
| keys | Required | string | Comma-separated list of object `COMPLIANCETYPEID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create a Vendor Compliance Type
-------------------------------

#### `create`

> Create a vendor compliance type record using the required values:

```
<create>
    <COMPLIANCETYPE>
        <COMPLIANCETYPEID>GL-Insurance</COMPLIANCETYPEID>
        <NAME>General Liability Insurance</NAME>
        <COMPLIANCEDEFINITIONID>Ins-Exp-Date</COMPLIANCEDEFINITIONID>
        <SEQNUMID>AP-ADJ</SEQNUMID> 
    </COMPLIANCETYPE>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCETYPE | Required | object | Type of object to create. |

`COMPLIANCETYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCETYPEID | Required | string | Unique ID for the compliance type. |
| NAME | Required | string | Name of the compliance type, such as “GL Insurance.” In the Sage Intacct web application, this value will be used as the default name for compliance records that are created from this compliance type. |
| COMPLIANCEDEFINITIONID | Required | string | ID of the [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) that will be enforced in all [compliance records](https://developer.intacct.com/api/purchasing/vendor-compliance-records/) created from this compliance type. |
| SEQNUMID | Required | string | The ID of the document sequence to use to create the `COMPLIANCERECORDID` of compliance records that are created from this compliance type. |
| DESCRIPTION | Optional | string | Description of the compliance type. |
| STATUS | Optional | string | Status of compliance type:
*   `active` - the compliance type can be assigned to compliance records. (default)
*   `inactive` - The compliance type cannot be used to create new compliance records. Existing compliance records that use the compliance type are still active.

 |

* * *

Update a Vendor Compliance Type
-------------------------------

#### `update`

> Updates a vendor compliance type’s description:

```
<update>
    <COMPLIANCETYPE>
        <recordno>68</recordno>
        <description>Use for CA GL insurance</description>   
    </COMPLIANCETYPE>
</update>
```

#### Parameters

`COMPLIANCETYPE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | `RECORDNO` of the compliance type to update. Required if not using `COMPLIANCETYPEID` |
| COMPLIANCETYPEID | Required | string | `COMPLIANCETYPEID` of the compliance type to update. Required is not using `RECORDNO`. |
| NAME | Optional | string | Name of the compliance type, such as “GL Insurance.” In the Sage Intacct web application, this value will be used as the default name for compliance records that are created from this compliance type. |
| COMPLIANCEDEFINITIONID | Optional | string | ID of the [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) that will be enforced in all [compliance records](https://developer.intacct.com/api/purchasing/vendor-compliance-records/) created from this compliance type. |
| SEQNUMID | Optional | string | The ID of the document sequence to use to create the `COMPLIANCERECORDID` of compliance records that are created from this compliance type. |
| DESCRIPTION | Optional | string | Description of the compliance type. |
| STATUS | Optional | string | Status of compliance type:
*   `active` - the compliance type can be assigned to compliance records. (default)
*   `inactive` - The compliance type cannot be used to create new compliance records. Existing compliance records that use the compliance type are still active.

 |

* * *

Delete a Vendor Compliance Type
-------------------------------

#### `delete`

> Delete a vendor compliance type. Note that you can only delete types not in use by vendor compliance records or definitions.

```
<delete>
    <object>COMPLIANCETYPE</object>
    <keys>68</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCETYPE` |
| keys | Required | string | Comma-separated list of compliance type `RECORDNO` to delete. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

