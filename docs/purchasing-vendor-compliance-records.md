Title: Vendor Compliance Records

URL Source: https://developer.intacct.com/api/purchasing/vendor-compliance-records/

Markdown Content:
*   [Get Vendor Compliance Record Object Definition](https://developer.intacct.com/api/purchasing/vendor-compliance-records/#get-vendor-compliance-record-object-definition)
*   [Query and List Vendor Compliance Records](https://developer.intacct.com/api/purchasing/vendor-compliance-records/#query-and-list-vendor-compliance-records)
*   [Get Vendor Compliance Records](https://developer.intacct.com/api/purchasing/vendor-compliance-records/#get-vendor-compliance-records)
*   [Get Vendor Compliance Records by ID](https://developer.intacct.com/api/purchasing/vendor-compliance-records/#get-vendor-compliance-records-by-id)
*   [Create Vendor Compliance Records](https://developer.intacct.com/api/purchasing/vendor-compliance-records/#create-vendor-compliance-records)
*   [Update Vendor Compliance Record](https://developer.intacct.com/api/purchasing/vendor-compliance-records/#update-vendor-compliance-record)
*   [Delete Vendor Compliance Records](https://developer.intacct.com/api/purchasing/vendor-compliance-records/#delete-vendor-compliance-records)

* * *

Vendor compliance is the validation that a subcontractor or vendor has provided documents required for a job. For example, the vendor might need to supply proof of insurance, certified reports, lien waivers, or other misc documents like permits, licenses, and so forth.

A **compliance record** applies a compliance type to a specified vendor or primary document so that you can track dates, amounts, and documents that show compliance.

NOTE: To enable the Vendor Compliance subscription, first enable Accounts Payable, Purchasing, and Construction. Vendor compliance is available only for Construction at this time.

### Out-of-compliance error messages

If the vendor specified in a compliance record is out of compliance with the compliance definition (for example, the insurance policy has expired), and the `PAYMENTNOTIFICATION` is set to `error`, payments to that vendor will be blocked and an error message will be returned like the example shown to the right.

```
<error>
    <errorno>CRE-3211</errorno>
    <description></description>
    <description2>Expiration date compliance error CR.01091--General liability insurance</description2>
    <correction></correction>
</error>
```

where:

*   `Expiration date` is the validation rule, either `Expiration date` or `Document received`
*   `error` or `warning` based on the `PAYMENTNOTIFICATION` setting
*   `CR.01091` is the `COMPLIANCERECORDID` from the compliance record
*   `General liability insurance` is the `NAME` from the compliance record

* * *

Get Vendor Compliance Record Object Definition
----------------------------------------------

#### `lookup`

> List all the fields and relationships for the vendor compliance record object:

```
<lookup>
    <object>COMPLIANCERECORD</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCERECORD` |

* * *

Query and List Vendor Compliance Records
----------------------------------------

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the specified fields for each vendor compliance record that has a specified `COMPLIANCERECORDID`.

```
<query>
    <object>COMPLIANCERECORD</object>
          <select>
            <field>RECORDNO</field>
            <field>COMPLIANCERECORDID</field>
            <field>NAME</field>
            <field>VENDORKEY</field>
            <field>VENDORID</field>
            <field>VENDORNAME</field>
            <field>PROJECTKEY</field>
            <field>PROJECTID</field>
            <field>PROJECTNAME</field>
            <field>NOTES</field>
          </select>
          <filter>
            <equalto>
              <field>COMPLIANCEDEFINITIONID</field>
              <value>CD-15-LW-ALLOW-NEG</value>
            </equalto>
          </filter>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCERECORD` |
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

#### `read`

> Get all vendor compliance record fields for the specified keys:

```
<read>
    <object>COMPLIANCERECORD</object>
    <fields>*</fields>
    <keys>42</keys>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCERECORD` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the `COMPLIANCERECORD` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Vendor Compliance Records by ID
-----------------------------------

#### `readByName`

```
<readByName>
    <object>compliancerecord</object>
    <fields>*</fields>
    <keys>GL-Insurance</keys>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCERECORD` |
| keys | Required | string | Comma-separated list of `COMPLIANCERECORDID` of the compliance record to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Vendor Compliance Records
--------------------------------

#### `create`

> Create a vendor compliance record using the required values:

```
<create>
    <COMPLIANCERECORD>
        <COMPLIANCETYPEID>GL-Insurance</COMPLIANCETYPEID>
        <NAME>Seamless Cement GL Insurance</NAME>
        <VENDORID>1099 Int</VENDORID>  
        <PROJECTID>120</PROJECTID>
        <NOTES>New GM in San Jose office.</NOTES>
    </COMPLIANCERECORD>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCERECORD | Required | object | Type of object to create. |

`COMPLIANCERECORD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCETYPEID | Required | string | ID of the [compliance type](https://developer.intacct.com/api/purchasing/vendor-compliance-types/) to use to create the compliance record. The `COMPLIANCERECORDID` for the new compliance record will be generated by the system using the document sequence specified in the compliance type. |
| NAME | Required | string | Name for the compliance record. |
| VENDORID | Required | string | ID of the [vendor](https://developer.intacct.com/api/accounts-payable/vendors/) that this compliance record applies to. |
| DESCRIPTION | Optional | string | Description of the compliance record. |
| STATUS | Optional | string | Status of compliance record:
*   `active` - the compliance record is used for compliance validation. (default)
*   `inactive` - The compliance record is not counted in compliance validation.

 |
| CONTACTNAME | Optional | string | The name of a [contact](https://developer.intacct.com/api/company-console/contacts/) to associate with this compliance record. |
| POLICYNUMBER | Optional | string | The policy or document number for this record. |
| EFFECTIVEDATE | Optional | string | Date when policy or document becomes effective. Used for reporting. |
| EXPIRATIONDATE | Optional | string | Date when the policy or document expires. If the `VALIDATIONRULE` in the applicable [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) is set to `Expiration date`, this value is checked when payment to the vendor is initiated. |
| AMOUNT | Optional | currency | The amount of insurance coverage provided, for capturing insurance liability limitation. Used for reporting. |
| ADDITIONALINSURED | Optional | boolean | Use `true` to indicate that the contractor is listed as an additional insured on the policy, otherwise use `false`. (Default: `false`) |
| REFERENCENUMBER | Optional | string | Document reference number. |
| SUBROGATIONWAIVER | Optional | boolean | Use `true` to indicate that the policy includes a subrogation waiver, otherwise use `false`. (Default: `false`) |
| DOCUMENTRECEIVED | Optional | boolean | Use `true` to indicate that the required compliance document has been received, otherwise use `false`. If the `VALIDATIONRULE` in the applicable [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) is set to `Document received`, this value is used to determine compliance. (Default: `false`) |
| PROJECTID | Optional | string | Unique user-defined project identifier. Should refer to an existing, active project record. The project is retrieved from the primary document header. |
| NOTES | Optional | string | Text field for user-added notes. Use 4000 or fewer characters. |
| RECEIVEDDATE | Optional | string | The date that the compliance document was received. |
| RECEIVEDBYID | Optional | string | The ID of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who received the compliance document. |
| NOTIFICATIONOVERRIDE | Optional | Boolean | Use `true` to override the `PAYMENTNOTIFICATION` setting defined in the [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) so that the vendor can be paid even if out-of-compliance, otherwise use `false`. (Default: `false`) |
| SUPDOCID | Optional | string | The reference number of any supporting documentation. |
| SENDTOCONTACTNAME | Optional | string | The name of the contact to whom the lien waiver will be sent. Applies only when `CATEGORY` is `Lien waiver`. If `CATEGORY` is not set to Lien waiver and a value is supplied, then an error is returned. |

* * *

Update Vendor Compliance Record
-------------------------------

#### `update`

> Update a vendor compliance record’s description using `recordno`:

```
<update>
    <COMPLIANCERECORD>
        <RECORDNO>42</RECORDNO>
        <DESCRIPTION>These compliance docs apply to FY25</DESCRIPTION>
        <PROJECTID>122</PROJECTID>
        <NOTES>Updated docs in Q1.</NOTES>
    </COMPLIANCERECORD>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| COMPLIANCERECORD | Required | object | Object type to update |

`COMPLIANCERECORD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | `RECORDNO` of the compliance record to update. |
| NAME | Optional | string | Name for the compliance record. |
| VENDORID | Optional | string | ID of the [vendor](https://developer.intacct.com/api/accounts-payable/vendors/) that this compliance record applies to. |
| DESCRIPTION | Optional | string | Description of the compliance record. |
| STATUS | Optional | string | Status of compliance record:
*   `active` - the compliance record is used for compliance validation.
*   `inactive` - The compliance record is not counted in compliance validation.

 |
| CONTACTNAME | Optional | string | The name of a [contact](https://developer.intacct.com/api/company-console/contacts/) to associate with this compliance record. |
| POLICYNUMBER | Optional | string | The policy or document number for this record. |
| EFFECTIVEDATE | Optional | string | Date when policy or document becomes effective. Used for reporting. |
| EXPIRATIONDATE | Optional | string | Date when the policy or document expires. If the `VALIDATIONRULE` in the applicable [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) is set to `Expiration date`, this value is checked when payment to the vendor is initiated. |
| AMOUNT | Optional | currency | The amount of insurance coverage provided, for capturing insurance liability limitation. Used for reporting. |
| ADDITIONALINSURED | Optional | boolean | Use `true` to indicate that the contractor is listed as an additional insured on the policy, otherwise use `false`. |
| REFERENCENUMBER | Optional | string | Document reference number. |
| SUBROGATIONWAIVER | Optional | boolean | Use `true` to indicate that the policy includes a subrogation waiver, otherwise use `false`. |
| DOCUMENTRECEIVED | Optional | boolean | Use `true` to indicate that the required compliance document has been received, otherwise use `false`. If the `VALIDATIONRULE` in the applicable [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) is set to `Document received`, this value is used to determine compliance. |
| PROJECTID | Optional | string | Unique user-defined project identifier. Should refer to an existing, active or inactive project record. The project is retrieved from the primary document header. |
| NOTES | Optional | string | Text field for user-added notes. Use 4000 or fewer characters. |
| RECEIVEDDATE | Optional | string | The date that the compliance document was received. |
| RECEIVEDBYID | Optional | string | The ID of the [employee](https://developer.intacct.com/api/employee-expenses/employees/) who received the compliance document. |
| NOTIFICATIONOVERRIDE | Optional | Boolean | Use `true` to override the `PAYMENTNOTIFICATION` setting defined in the [compliance definition](https://developer.intacct.com/api/purchasing/vendor-compliance-definitions/) so that the vendor can be paid even if out-of-compliance, otherwise use `false`. |
| SUPDOCID | Optional | string | The reference number of any supporting documentation. |
| FINALCOMPLIANCE | Optional | boolean | Applicable only when the Category is ‘Lien waiver’. Indictes whether the compliance record is finalized. Options are `true` or `false` (default). If `CATEGORY` is not set to Lien waiver and a value is supplied, then an error is returned. |
| SENDTOCONTACTNAME | Optional | string | The name of the contact to whom the lien waiver will be sent. Applies only when `CATEGORY` is `Lien waiver`. If `CATEGORY` is not set to Lien waiver and a value is supplied, then an error is returned. |

* * *

Delete Vendor Compliance Records
--------------------------------

#### `delete`

```
<delete>
    <object>compliancerecord</object>
    <keys>42</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `COMPLIANCERECORD` |
| keys | Required | string | Comma-separated list of compliance record `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

