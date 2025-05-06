Title: Vendor Compliance Definitions

URL Source: https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/

Markdown Content:
*   [Get the Vendor Compliance Object Definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#get-the-vendor-compliance-object-definition)
*   [Query and List Vendor Compliance Definitions](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#query-and-list-vendor-compliance-definitions)
*   [Query and List Vendor Compliance Definitions (Legacy)](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#query-and-list-vendor-compliance-definitions-legacy)
*   [Get Vendor Compliance Definitions](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#get-vendor-compliance-definitions)
*   [Get Vendor Compliance Definitions by ID](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#get-vendor-compliance-definitions-by-id)
*   [Create a Vendor Compliance Definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#create-a-vendor-compliance-definition)
*   [Update a Vendor Compliance Definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#update-a-vendor-compliance-definition)
*   [Delete a Vendor Compliance Definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/#delete-a-vendor-compliance-definition)

* * *

Vendor compliance is the validation that a subcontractor or vendor has provided documents required for a job. For example, the vendor might need to supply proof of insurance, certified reports, lien waivers, or other misc documents like permits, licenses, and so forth.

A **compliance definition** sets a compliance category (insurance, lien waiver, or miscellaneous), how validation is tracked, and whether payment is allowed if a vendor is not in compliance. Validation is based on an expiration date or whether a compliance document is received.

NOTE: To enable the Vendor Compliance subscription, first enable Accounts Payable, Purchasing, and Construction. Vendor compliance is available only for Construction at this time.

* * *

Get the Vendor Compliance Object Definition
-------------------------------------------

#### `lookup`

> List all the fields and relationships for the vendor compliance definition object:

```
<lookup>
    <object>COMPLIANCEDEFINITION</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCEDEFINITION` |

* * *

Query and List Vendor Compliance Definitions
--------------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the specified fields for each vendor compliance definition where the status is active:

```
<query>
    <object>COMPLIANCEDEFINITION</object>
          <select>
            <field>RECORDNO</field>
            <field>COMPLIANCEDEFINITIONID</field>
            <field>NAME</field>
            <field>DESCRIPTION</field>
            <field>CATEGORY</field>
            <field>STATUS</field>
            <field>TRACKBY</field>
            <field>GENERATERULE</field>
            <field>VALIDATIONRULE</field>
            <field>PAYMENTNOTIFICATION</field>
            <field>GENERATEFOREACH</field>
            <field>MINLIENWAIVERAMOUNT</field>
            <field>MINPRIMARYDOCAMOUNT</field>
            <field>ALLOWNEGATIVELIENWAIVERS</field>
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
| object | Required | string | Use `COMPLIANCEDEFINITION` |
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

Query and List Vendor Compliance Definitions (Legacy)
-----------------------------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>COMPLIANCEDEFINITION</object>
    <fields>RECORDNO, COMPLIANCEDEFINITIONID, NAME, ALLOWNEGATIVELIENWAIVERS</fields>
    <query>CATEGORY = 'I'</query>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCEDEFINITION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

#### `read`

> Get all vendor compliance definition fields for the specified keys:

```
<read>
    <object>COMPLIANCEDEFINITION</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCEDEFINITION` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the vendor compliance definition to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Vendor Compliance Definitions by ID
---------------------------------------

#### `readByName`

```
<readByName>
    <object>COMPLIANCEDEFINITION</object>
    <keys>Ins-Exp-Date</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCEDEFINITION` |
| keys | Required | string | Comma-separated list of `COMPLIANCEDEFINITIONID` of the compliance definition to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create a Vendor Compliance Definition
-------------------------------------

#### `create`

NOTE: Compliance definitions for lien waivers uses the primary document feature to generate compliance records. Set [PRIMARYDOC](https://developer.intacct.com/api/purchasing/purchasing-transaction-definitions/) to true to use primary documents in Construction.

> Create an insurance compliance definition record for specific vendor types:

```
<create>
    <COMPLIANCEDEFINITION>
        <COMPLIANCEDEFINITIONID>Vend123</COMPLIANCEDEFINITIONID>
        <NAME>Vendor Insurance</NAME>
        <DESCRIPTION>Verify vendor insurance</DESCRIPTION>
        <CATEGORY>Insurance</CATEGORY>
        <TRACKBY>Vendor</TRACKBY>
        <GENERATERULE>Automatic by type</GENERATERULE>
        <VALIDATIONRULE>Expiration date</VALIDATIONRULE>
        <PAYMENTNOTIFICATION>Ignore</PAYMENTNOTIFICATION>
        <COMPDEFENTRIES>
            <VENDTYPENAME>Retailer</VENDTYPENAME>
            <VENDTYPENAME>Wholesaler</VENDTYPENAME>
        </COMPDEFENTRIES>
    </COMPLIANCEDEFINITION>
</create>
```

> Create a lien waiver compliance definition record that allows lien waivers with negative amounts:

```
<create>
    <COMPLIANCEDEFINITION>
        <COMPLIANCEDEFINITIONID>LW124</COMPLIANCEDEFINITIONID>
        <NAME>LienWaiver-San Jose</NAME>
        <DESCRIPTION>Lien waiver for main office</DESCRIPTION>
        <CATEGORY>Lien waiver</CATEGORY>
        <TRACKBY>PrimaryDoc</TRACKBY>
        <GENERATERULE>Automatic by type</GENERATERULE>
        <VALIDATIONRULE>Document received</VALIDATIONRULE>
        <PAYMENTNOTIFICATION>Warning</PAYMENTNOTIFICATION>
        <GENERATEFOREACH>APPayment</GENERATEFOREACH>
        <MINLIENWAIVERAMOUNT>25000</MINLIENWAIVERAMOUNT>
        <MINPRIMARYDOCAMOUNT>35000</MINPRIMARYDOCAMOUNT>
        <ALLOWNEGATIVELIENWAIVERS>true</ALLOWNEGATIVELIENWAIVERS>
        <COMPDEFENTRIES>
            <DOCPARID>Prim-PO</DOCPARID>
        </COMPDEFENTRIES>
    </COMPLIANCEDEFINITION>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCEDEFINITION | Required | object | Type of object to create. |

`COMPLIANCEDEFINITION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCEDEFINITIONID | Required | string | Unique ID for the compliance definition. |
| NAME | Required | string | The compliance definition name. |
| CATEGORY | Required | string | Requirement category:
*   `Insurance` - use for general liability insurance, workers comp insurance, etc.
*   `Lien waiver` - use to ensure that subcontractors and suppliers have signed lien waiver agreements before releasing payment. Automatically generates lien waiver documents at AP bill or AP payment creation for transaction definitions in which `PRIMARYDOC` is set to true. When `Lien waiver` is used, then `ALLOWNEGATIVELIENWAIVERS` may be set.
*   `Miscellaneous` - use for permits, licenses, bonds, etc.

 |
| VALIDATIONRULE | Required | string | How compliance will be validated. Options depend on the `CATEGORY` value:

*   `Expiration date` - For `Insurance` and `Miscellaneous` categories.
*   `Document received` - For `Miscellaneous` and `Lien waiver` categories.

 |
| PAYMENTNOTIFICATION | Required | string | Action to take when a vendor is out of compliance with this definition and a payment is attempted:

*   `Ignore` - no error returned and payments to the vendor are allowed (default)
*   `Warning` - a warning is returned and payments to the vendor are still allowed
*   `Error` - an error is returned and payments to the vendor are blocked.

 |
| DESCRIPTION | Optional | string | Description of the compliance definition. |
| STATUS | Optional | string | Status of compliance definition.

*   `active` - the compliance record can be assigned to compliance types, and compliance records are validated against the definition. (default)
*   `inactive` - The compliance definition is not used in compliance validation, and cannot be used to create a new compliance type.

 |
| TRACKBY | Optional | string | The objects that the compliance definition can be applied to.

*   `Vendor` - When `CATEGORY` is set to `Insurance` or `Miscellaneous`.
*   `Primarydoc` - When `CATEGORY` is set to `Lien waiver`, `Insurance`, or `Miscellaneous`

 |
| GENERATERULE | Optional | string | Indicates whether to automatically generate compliance records and how to do so. For example, users can select which vendor types automatically generate compliance records.

*   `Do not generate` - Compliance records are not generated automatically. (default)
*   `Automatic by type` - Generate compliance records based on the list of types in `COMPDEFENTRIES`.

 |
| COMPDEFENTRIES | Optional | array | List of vendor types or primary document IDs for which to generate compliance records when `GENERATERULE` is set to `Automatic by type`. Options are:

*   `VENDTYPENAME` - The name of a vendor type. Used when `TRACKBY` is set to `Vendor`.
*   `DOCPARID` - The ID of a purchasing transaction definition that has `PRIMARYDOCUMENT` set to `true`. Used when `TRACKBY` is set to `Primarydoc`.

 |
| GENERATEFOREACH | Optional | string | The type of transaction for which to generate lien waiver documents. Required if `CATEGORY` is set to `Lien waiver`; not applicable to other categories.

*   `APBill` - Generate lien waiver documents for bills (default)
*   `APPayment` - Generate lien waiver documents for payments

 |
| MINLIENWAIVERAMOUNT | Optional | currency | When `CATEGORY` is set to `Lien waiver`, sets a minimum amount required for a lien waiver to be generated. For example, users might want orders of less than $10,000, which might be partial orders, to not require a lien waiver. Use `0` or a null value for no minimum. |
| MINPRIMARYDOCAMOUNT | Optional | currency | When `CATEGORY` is set to `Lien waiver`, sets a minimum amount required for a lien waiver to be generated based on the primary document. For example, users might want orders of less than $10,000, which might be partial orders, to not require a lien waiver. Use `0` or a null value for no minimum. |
| ALLOWNEGATIVELIENWAIVERS | Optional | boolean | Use `true` (default) to indicate that lien waivers can be generated with negative amounts, otherwise use `false`. Applies only when `CATEGORY` is set to ‘Lien waiver’. If `CATEGORY` is not ‘Lien waiver’ and a value is supplied, an error is returned. |

* * *

Update a Vendor Compliance Definition
-------------------------------------

#### `update`

NOTE: Lien waivers uses the primary document feature to generate compliance records. Set [PRIMARYDOC](https://developer.intacct.com/api/purchasing/purchasing-transaction-definitions/) to true to use primary documents in Construction.

> Update a vendor compliance definition record using `COMPLIANCEDEFINITIONID` or `RECORDNO`. If both are used, they must belong to the same record:

```
<update>
    <COMPLIANCEDEFINITION>
        <COMPLIANCEDEFINITIONID>LW124</COMPLIANCEDEFINITIONID>
        <PAYMENTNOTIFICATION>Warning</PAYMENTNOTIFICATION>
        <MINLIENWAIVERAMOUNT>35000</MINLIENWAIVERAMOUNT>
        <MINPRIMARYDOCAMOUNT>350000</MINPRIMARYDOCAMOUNT>
        <COMPDEFENTRIES>
            <DOCPARID>PO-105535</DOCPARID>
        </COMPDEFENTRIES>
    </COMPLIANCEDEFINITION>
</update>
```

> Update a vendor compliance definition record that does not allow lien waivers with negative amounts.

```
<update>
    <COMPLIANCEDEFINITION>
        <COMPLIANCEDEFINITIONID>LW124</COMPLIANCEDEFINITIONID>
        <ALLOWNEGATIVELIENWAIVERS>false</ALLOWNEGATIVELIENWAIVERS>
    </COMPLIANCEDEFINITION>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCEDEFINITION | Required | object | Type of object to update |

`COMPLIANCEDEFINITION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | `RECORDNO` of the compliance definition to update. Required if not using `COMPLIANCEDEFINITIONID`. |
| COMPLIANCEDEFINITIONID | Optional | string | ID of the compliance definition to update. Required if not using `RECORDNO`. |
| NAME | Required | string | The compliance definition name. |
| VALIDATIONRULE | Required | string | How compliance will be validated. Options depend on the `CATEGORY` value:
*   `Expiration date` - For `Insurance` and `Miscellaneous` categories.
*   `Document received` - For `Miscellaneous` and `Lien waiver` categories.

 |
| PAYMENTNOTIFICATION | Required | string | Action to take when a vendor is out of compliance with this definition and a payment is attempted:

*   `Ignore` - no error returned and payments to the vendor are allowed (default)
*   `Warning` - a warning is returned and payments to the vendor are still allowed
*   `Error` - an error is returned and payments to the vendor are blocked.

 |
| DESCRIPTION | Optional | string | Description of the compliance definition. |
| STATUS | Optional | string | Status of compliance definition.

*   `active` - the compliance record can be assigned to compliance types, and compliance records are validated against the definition. (default)
*   `inactive` - The compliance definition is not used in compliance validation, and cannot be used to create a new compliance type.

 |
| GENERATERULE | Optional | string | Indicates whether to automatically generate compliance records and how to do so. For example, users can select which vendor types automatically generate compliance records.

*   `Do not generate` - Compliance records are not generated automatically. (default)
*   `Automatic by type` - Generate compliance records based on the list of types in `COMPDEFENTRIES`.

 |
| COMPDEFENTRIES | Optional | array | List of vendor types or primary document IDs for which to generate compliance records when `GENERATERULE` is set to `Automatic by type`. Options are:

*   `VENDTYPENAME` - The name of a vendor type. Used when `TRACKBY` is set to `Vendor`.
*   `DOCPARID` - The ID of a purchasing transaction definition that has `PRIMARYDOCUMENT` set to `true`. Used when `TRACKBY` is set to `Primarydoc`.

 |
| MINLIENWAIVERAMOUNT | Optional | currency | When `CATEGORY` is set to `Lien waiver`, sets a minimum amount required for a lien waiver to be generated. For example, users might want orders of less than $10,000, which might be partial orders, to not require a lien waiver. Use `0` or a null value for no minimum. |
| MINPRIMARYDOCAMOUNT | Optional | currency | When `CATEGORY` is set to `Lien waiver`, sets a minimum amount required for a lien waiver to be generated based on the primary document. For example, users might want orders of less than $10,000, which might be partial orders, to not require a lien waiver. Use `0` or a null value for no minimum. |
| ALLOWNEGATIVELIENWAIVERS | Optional | boolean | Use `true` (default) to indicate that lien waivers can be generated with negative amounts, otherwise use `false`. Applies only when `CATEGORY` is set to `Lien waiver`. If `CATEGORY` is not `Lien waiver` and a value is supplied, an error is returned. This value only affects the generation of future lien waiver compliance records. |

* * *

Delete a Vendor Compliance Definition
-------------------------------------

#### `delete`

> Delete a vendor compliance definition. Note that you can only delete definitions not in use by vendor compliance records or types.

```
<delete>
    <object>COMPLIANCEDEFINITION</object>
    <keys>148</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCEDEFINITION` |
| keys | Required | string | Comma-separated list of compliance definition `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

