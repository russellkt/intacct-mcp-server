Title: Vendors

URL Source: https://developer.intacct.com/api/accounts-payable/vendors/

Markdown Content:
*   [Vendors](https://developer.intacct.com/api/accounts-payable/vendors/#vendors)
    *   [Get Vendor Object Definition](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor-object-definition)
    *   [Query and List Vendors](https://developer.intacct.com/api/accounts-payable/vendors/#query-and-list-vendors)
    *   [Query and List Vendors (Legacy)](https://developer.intacct.com/api/accounts-payable/vendors/#query-and-list-vendors-legacy)
    *   [Get Vendor](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor)
    *   [Get Vendor by ID](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor-by-id)
    *   [Create Vendor](https://developer.intacct.com/api/accounts-payable/vendors/#create-vendor)
    *   [Create Vendor (Legacy)](https://developer.intacct.com/api/accounts-payable/vendors/#create-vendor-legacy)
    *   [Update Vendor](https://developer.intacct.com/api/accounts-payable/vendors/#update-vendor)
    *   [Update Vendor (Legacy)](https://developer.intacct.com/api/accounts-payable/vendors/#update-vendor-legacy)
    *   [Delete Vendor](https://developer.intacct.com/api/accounts-payable/vendors/#delete-vendor)
    *   [Delete Vendor (Legacy)](https://developer.intacct.com/api/accounts-payable/vendors/#delete-vendor-legacy)
    *   [Create Location Specific Vendor Account Number (Legacy)](https://developer.intacct.com/api/accounts-payable/vendors/#create-location-specific-vendor-account-number-legacy)
*   [Vendor Approvals](https://developer.intacct.com/api/accounts-payable/vendors/#vendor-approvals)
    *   [Get Vendors to Approve](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendors-to-approve)
    *   [Approve Vendors](https://developer.intacct.com/api/accounts-payable/vendors/#approve-vendors)
    *   [Decline Vendors](https://developer.intacct.com/api/accounts-payable/vendors/#decline-vendors)
    *   [Get Vendor Approval History](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor-approval-history)
*   [Vendor Email Templates](https://developer.intacct.com/api/accounts-payable/vendors/#vendor-email-templates)
    *   [Get Vendor Email Template Object Definition](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor-email-template-object-definition)
    *   [Query and List Vendor Email Templates](https://developer.intacct.com/api/accounts-payable/vendors/#query-and-list-vendor-email-templates)
    *   [Query and List Vendor Email Templates (Legacy)](https://developer.intacct.com/api/accounts-payable/vendors/#query-and-list-vendor-email-templates-legacy)
    *   [Get Vendor Email Template](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor-email-template)
*   [Vendor Visibility](https://developer.intacct.com/api/accounts-payable/vendors/#vendor-visibility)
    *   [Get Vendor Visibility Object Definition](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor-visibility-object-definition)
    *   [Get Vendor Visibility](https://developer.intacct.com/api/accounts-payable/vendors/#get-vendor-visibility)

* * *

Vendors are companies or individuals that are paid for goods and services.

* * *

### Get Vendor Object Definition

#### `lookup`

> List all the fields and relationships for the vendor object:

```
<lookup>
    <object>VENDOR</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOR` |

* * *

### Query and List Vendors

#### [`query`](https://developer.intacct.com/web-services/queries/)

> For each vendor owed more than 100.00, list the record number, pay-to contact name, and total due:

```
<query>
    <object>VENDOR</object>
    <select>
        <field>RECORDNO</field>
        <field>PAYTOCONTACT.CONTACTNAME</field>
        <field>TOTALDUE</field>
    </select>
    <filter>
        <greaterthan>
            <field>TOTALDUE</field>
            <value>100</value>
        </greaterthan>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOR` |
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

### Query and List Vendors (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>VENDOR</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOR` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active and `F` for Inactive. |
| ONETIME | Optional | string | One-time use. Use `T` for one-time use or `F` otherwise. |

* * *

### Get Vendor

#### `read`

```
<read>
    <object>VENDOR</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOR` |
| keys | Required | string | Comma-separated list of vendor `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Vendor by ID

#### `readByName`

```
<readByName>
    <object>VENDOR</object>
    <keys>V1234</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOR` |
| keys | Required | string | Comma-separated list of vendor `VENDORID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Vendor

[History](https://developer.intacct.com/api/accounts-payable/vendors/#history-create-vendor)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added TAXSOLUTIONID, TAXSCHEDULE to Create/Update |
| 2021 Release 4 | Added PROVIDERVENDORS |
| 2021 Release 3 | Added VENDORCONTACTS, VENDOREMAILTEMPLATES, VENDORACCTNOLOCATIONS, FILEPAYMENTSERVICE, PYMTCOUNTRYCODE, VENDORBANKFILEDETAILS, and ISINDIVIDUAL |
| 2020 Release 2 | Added RETAINAGEPERCENTAGE |
| 2018 Release 4 | Added DEFAULT\_LEAD\_TIME |
|  | Updated note about RETAINAGEPERCENTAGE |

#### `create`

> Creates a vendor and specifies a display contact:

```
<create>
    <VENDOR>
        <VENDORID>V1234</VENDORID>
        <NAME>SaaS Company Inc</NAME>
        <DISPLAYCONTACT>
            <PRINTAS>SaaS Company Inc</PRINTAS>
            <COMPANYNAME>SaaS Co</COMPANYNAME>
            <TAXABLE>true</TAXABLE>
            <TAXGROUP>CA</TAXGROUP>
            <TAXSOLUTIONID>US Sales Tax - SYS</TAXSOLUTIONID>
            <TAXSCHEDULE>US Sold Goods Standard</TAXSCHEDULE>
            <PREFIX>Mr</PREFIX>
            <FIRSTNAME>Bill</FIRSTNAME>
            <LASTNAME>Smith</LASTNAME>
            <INITIAL>G</INITIAL>
            <PHONE1>12</PHONE1>
            <PHONE2>34</PHONE2>
            <CELLPHONE>56</CELLPHONE>
            <PAGER>78</PAGER>
            <FAX>90</FAX>
            <EMAIL1>noreply@intacct.com</EMAIL1>
            <EMAIL2></EMAIL2>
            <URL1></URL1>
            <URL2></URL2>
            <MAILADDRESS>
                <ADDRESS1>300 Park Ave</ADDRESS1>
                <ADDRESS2>Ste 1400</ADDRESS2>
                <CITY>San Jose</CITY>
                <STATE>CA</STATE>
                <ZIP>95110</ZIP>
                <COUNTRY>United States</COUNTRY>
            </MAILADDRESS>
        </DISPLAYCONTACT>
        <ONETIME>false</ONETIME>
        <STATUS>active</STATUS>
        <HIDEDISPLAYCONTACT>false</HIDEDISPLAYCONTACT>
        <VENDTYPE>SaaS</VENDTYPE>
        <PARENTID>V5678</PARENTID>
        <GLGROUP>Group</GLGROUP>
        <TAXID>12-3456789</TAXID>
        <NAME1099>SAAS CO INC</NAME1099>
        <FORM1099TYPE>MISC</FORM1099TYPE>
        <FORM1099BOX>3</FORM1099BOX>
        <SUPDOCID>A1234</SUPDOCID>
        <APACCOUNT>2000</APACCOUNT>
        <CREDITLIMIT>1234.56</CREDITLIMIT>
        <ONHOLD>false</ONHOLD>
        <DONOTCUTCHECK>false</DONOTCUTCHECK>
        <COMMENTS>my comment</COMMENTS>
        <CURRENCY>USD</CURRENCY>
        <CONTACTINFO>
            <CONTACTNAME>primary</CONTACTNAME>
        </CONTACTINFO>
        <PAYTO>
            <CONTACTNAME>pay to</CONTACTNAME>
        </PAYTO>
        <RETURNTO>
            <CONTACTNAME>return to</CONTACTNAME>
        </RETURNTO>
        <PAYMETHODKEY>Printed Check</PAYMETHODKEY>
        <MERGEPAYMENTREQ>true</MERGEPAYMENTREQ>
        <PAYMENTNOTIFY>true</PAYMENTNOTIFY>
        <BILLINGTYPE>openitem</BILLINGTYPE>
        <PAYMENTPRIORITY>Normal</PAYMENTPRIORITY>
        <TERMNAME>N30</TERMNAME>
        <DISPLAYTERMDISCOUNT>false</DISPLAYTERMDISCOUNT>
        <ACHENABLED>true</ACHENABLED>
        <ACHBANKROUTINGNUMBER>123456789</ACHBANKROUTINGNUMBER>
        <ACHACCOUNTNUMBER>1111222233334444</ACHACCOUNTNUMBER>
        <ACHACCOUNTTYPE>Checking Account</ACHACCOUNTTYPE>
        <ACHREMITTANCETYPE>CTX</ACHREMITTANCETYPE>
        <VENDORACCOUNTNO>9999999</VENDORACCOUNTNO>
        <DISPLAYACCTNOCHECK>false</DISPLAYACCTNOCHECK>
        <OBJECTRESTRICTION>Restricted</OBJECTRESTRICTION>
        <RESTRICTEDLOCATIONS>100#~#200</RESTRICTEDLOCATIONS>
        <RESTRICTEDDEPARTMENTS>D100#~#D200</RESTRICTEDDEPARTMENTS>
        <CUSTOMFIELD1>Hello</CUSTOMFIELD1>
    </VENDOR>
</create>
```

> Creates a vendor and specifies a display contact and a contact list (provided via vendor contacts):

```
<create>
    <VENDOR>
        <VENDORID>V378</VENDORID>
        <NAME>ACME Widget Company Inc.</NAME>
        <DISPLAYCONTACT>
            <PRINTAS>ACME Widget Company Inc</PRINTAS>
            <COMPANYNAME>ACME Widget Company</COMPANYNAME>
        </DISPLAYCONTACT>
        <VENDORCONTACTS>
            <VENDORENTITYCONTACTS>
                <CATEGORYNAME>Mobile</CATEGORYNAME>
                <CONTACT>
                    <NAME>Despereaux, Pierre</NAME>
                </CONTACT>
            </VENDORENTITYCONTACTS>
            <VENDORENTITYCONTACTS>
                <CATEGORYNAME>Fax</CATEGORYNAME>
                <CONTACT>
                    <NAME>Despereaux, Pierre</NAME>
                </CONTACT>
            </VENDORENTITYCONTACTS>
        </VENDORCONTACTS>
    </VENDOR>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDOR | Required | object | Object to create |

`VENDOR`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDORID | Optional | string | Unique ID for the vendor. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value. |
| NAME | Required | string | Name |
| DISPLAYCONTACT | Required | object | Contact info |
| STATUS | Optional | string | Status. Use `active` for Active or `inactive` for Inactive (Default: `active`) |
| ONETIME | Optional | boolean | One time. Use `false` for No, `true` for Yes. (Default: `false`) |
| HIDEDISPLAYCONTACT | Optional | boolean | Exclude from contact list. Use `false` for No, `true` for Yes. (Default: `false`) |
| VENDTYPE | Optional | string | Vendor type ID |
| PARENTID | Optional | string | Parent vendor ID |
| GLGROUP | Optional | string | GL group name |
| DEFAULT\_LEAD\_TIME | Optional | integer | Default lead time in days for replenishment purposes. Can be overridden by lead time specified on an item with that vendor, or lead time specified for on an item with a warehouse/vendor combination with that vendor. (Default: 1) |
| TAXID | Optional | string | Tax ID |
| NAME1099 | Optional | string | Form 1099 name |
| FORM1099TYPE | Optional | string | Form 1099 type |
| FORM1099BOX | Optional | string | Form 1099 box |
| SUPDOCID | Optional | string | Attachments ID |
| APACCOUNT | Optional | string | Default expense GL account number |
| OFFSETGLACCOUNTNO | Optional | string | AP account number |
| CREDITLIMIT | Optional | currency | Credit limit |
| RETAINAGEPERCENTAGE | Optional | numeric | Default retainage percentage for vendors (Construction or Projects subscription). |
| ONHOLD | Optional | boolean | On hold. Use `false` for No, `true` for Yes. (Default: `false`) |
| DONOTCUTCHECK | Optional | boolean | Do not pay. Use `false` for No, `true` for Yes. (Default: `false`) |
| COMMENTS | Optional | string | Comments |
| CURRENCY | Optional | string | Default currency code |
| CONTACTINFO | Optional | object | Primary contact. If blank system will use DISPLAYCONTACT. |
| PAYTO | Optional | object | Pay to contact. If blank system will use DISPLAYCONTACT. |
| RETURNTO | Optional | object | Return to contact. If blank system will use DISPLAYCONTACT. |
| CONTACT\_LIST\_INFO | Optional | `CONTACT_LIST_INFO`\[\] | Contact list (alternative to `VENDORCONTACTS`). Multiple individual `CONTACT_LIST_INFO` elements may be passed. If this parameter and `VENDORCONTACTS` are both provided, `VENDORCONTACTS` is used. If neither are provided, any values supplied for other contacts (Primary, Pay to, or Return to) are used to create a contact list. |
| VENDORCONTACTS | Optional | `VENDORENTITYCONTACTS`\[0…n\] | Contact list (alternative to `CONTACT_LIST_INFO`). If this parameter and `CONTACT_LIST_INFO` are both provided, `VENDORCONTACTS` is used. If neither are provided, any values supplied for other contacts (Primary, Pay to, or Return to) are used to create a contact list. |
| VENDOREMAILTEMPLATES | Optional | `VENDOREMAILTEMPLATE`\[0…n\] | Vendor email templates. |
| VENDORACCTNOLOCATIONS | Optional | `VENDORACCTNOLOCHEAD`\[0…n\] | Vendor location assigned account numbers (alternative to `VENDOR_ACCTNO_LOC_HEAD `). If this parameter and `VENDOR_ACCTNO_LOC_HEAD` are both provided, `VENDORACCTNOLOCATIONS` is used. |
| VENDOR\_ACCTNO\_LOC\_HEAD | Optional | `VENDOR_ACCTNO_LOC_HEAD`\[\] | Vendor location assigned account numbers (alternative to `VENDORACCTNOLOCATIONS `). Multiple individual `VENDOR_ACCTNO_LOC_HEAD` elements may be passed. If this parameter and `VENDORACCTNOLOCATIONS` are both provided, `VENDORACCTNOLOCATIONS` is used. |
| FILEPAYMENTSERVICE | Optional | string | Enable direct payments to this vendor using a bank file. Choose `ACH`, `BANKFILE`, or `NONE`. (Default: `NONE`) |
| PYMTCOUNTRYCODE | Optional | string | Country code for a vendor. Required if the vendor is to receive bank file payments. Choose `AU`, `ZA`, or `GB`. (AU, GB, ZA only) |
| VENDORBANKFILEDETAILS | Optional | VENDORBANKFILEDETAIL\[\] | Vendor bank file payment details. The values you provide are validated if `FILEPAYMENTSERVICE` is set to `BANKFILE`. (AU, GB, ZA only) |
| PROVIDERVENDORS | Optional | PROVIDERVENDOR\[\] | Electronic payment providers to link to this vendor. You can also create a [PROVIDERVENDOR](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#create-payment-provider-vendor) object directly. (Early Adopter program) |
| PAYMETHODKEY | Optional | string | Preferred payment method |
| MERGEPAYMENTREQ | Optional | boolean | Merge payment requests. Use `false` for No, `true` for Yes. (Default: `true`) |
| PAYMENTNOTIFY | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. (Default: `false`) |
| BILLINGTYPE | Optional | string | Vendor billing type |
| PAYMENTPRIORITY | Optional | string | Payment priority |
| TERMNAME | Optional | string | Payment term |
| DISPLAYTERMDISCOUNT | Optional | boolean | Display term discount on check stub. Use `false` for No, `true` for Yes. (Default: `true`) |
| ACHENABLED | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. (Default: `false`) |
| ACHBANKROUTINGNUMBER | Optional | string | ACH bank routing number |
| ACHACCOUNTNUMBER | Optional | string | ACH bank account number |
| ACHACCOUNTTYPE | Optional | string | ACH bank account type |
| ACHREMITTANCETYPE | Optional | string | ACH bank account class |
| VENDORACCOUNTNO | Optional | string | Vendor account number |
| DISPLOCACCTNOCHECK | Optional | boolean | Display location assigned account number on check stub. Use `false` for No, `true` for Yes. (Default: `false`) |
| OBJECTRESTRICTION | Optional | string | Restriction type. Use `Unrestricted`, `RootOnly`, or `Restricted`. (Default `Unrestricted`) |
| RESTRICTEDLOCATIONS | Optional | string | Restricted location IDs. Use if OBJECTRESTRICTION is `Restricted`. Implode multiple IDs with `#~#`. |
| RESTRICTEDDEPARTMENTS | Optional | string | Restricted department IDs. Use if OBJECTRESTRICTION is `Restricted`. Implode multiple IDs with `#~#`. |
| ISINDIVIDUAL | Optional | boolean | Specifies whether to mark the vendor as an individual person so that personally identifiable information (PII) can be masked. Use `false` for No, `true` for Yes. (Default: `false`) (Vendor Payments powered by CSI) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`DISPLAYCONTACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PRINTAS | Required | string | Print as |
| CONTACTNAME | Optional | string | If left blank, system will create the name as `[NAME](V[VENDORID])` |
| COMPANYNAME | Optional | string | Company name |
| TAXABLE | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
| TAXGROUP | Optional | string | Contact tax group name |
| TAXSCHEDULE | Optional | string | You can assign a default tax schedule for a vendor contact. When you create an AP transaction, the tax details from the assigned schedule are used as the default for the AP line entry. The tax details can be overridden through the UI |
| TAXSOLUTIONID | Optional | string | Tax solution. Required if providing Tax Schedule |
| PREFIX | Optional | string | Prefix |
| FIRSTNAME | Optional | string | First name |
| LASTNAME | Optional | string | Last name |
| INITIAL | Optional | string | Middle name |
| PHONE1 | Optional | string | Primary phone number |
| PHONE2 | Optional | string | Secondary phone number |
| CELLPHONE | Optional | string | Cellular phone number |
| PAGER | Optional | string | Pager number |
| FAX | Optional | string | Fax number |
| EMAIL1 | Optional | string | Primary email address |
| EMAIL2 | Optional | string | Secondary email address |
| URL1 | Optional | string | Primary URL |
| URL2 | Optional | string | Secondary URL |
| MAILADDRESS | Optional | object | Mail address |

`MAILADDRESS`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ADDRESS1 | Optional | string | Address line 1 |
| ADDRESS2 | Optional | string | Address line 2 |
| ADDRESS3 | Optional | string | Address line 3 |
| CITY | Optional | string | City |
| STATE | Optional | string | State/province |
| ZIP | Optional | string | Zip/postal code |
| COUNTRY | Optional | string | Country |
| ISOCOUNTRYCODE | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `COUNTRY` and `ISOCOUNTRYCODE` must be provided. |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Primary contact name |

`PAYTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Pay to contact name |

`RETURNTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Return to contact name |

`VENDORENTITYCONTACTS`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CATEGORYNAME | Required | string | Contact category, such as work, home, and so forth. |
| CONTACT | Required | object | Contact |

`CONTACT_LIST_INFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CATEGORYNAME | Required | string | Contact category, such as work, home, and so forth. |
| CONTACT | Optional | object | Contact |

`CONTACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Contact name |

`VENDOREMAILTEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EMAILTEMPLATENAME | Required | string | Name of the email template |
| DOCPARID | Required | string | Document type, such as Purchase Order |

`VENDORACCTNOLOCHEAD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATION | Required | string | Location ID |
| ACCOUNTNO | Required | string | Account number |

`VENDOR_ACCTNO_LOC_HEAD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATION | Required | string | Location ID |
| ACCOUNTNO | Required | string | Account number |

`VENDORBANKFILEDETAIL`

Available for Australia (AU), South Africa (ZA), or the United Kingdom (GB).

**AU**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BANKACCOUNTNUMBER | Required | string | Creditor account number. Use 9 or fewer digits, including hyphens and spaces. |
| ACCOUNTNAME | Required | string | Creditor account name. Use 16 or fewer alphanumeric characters. |
| BSBNUMBER | Required | string | Creditor BSB number, which is the 6-digit hyphenated branch number of the vendor bank account. For example, `123-456`. |
| PYMTREFERENCE | Required | string | Meaningful reference number to connect the bank file and the bills to be paid, enabling payments to be tracked. Use 18 or fewer alphanumeric characters. |

**ZA**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCOUNTNAME | Optional | string | Homing account name for the vendor bank account to which payments are made. Use 30 or fewer digits. |
| BANKACCOUNTNUMBER | Required | string | Homing account number for the vendor bank account to which payments are made. Use 31 or fewer digits. |
| BRANCHCODE | Required | string | Homing branch, which is the 6-digit branch number of the vendor bank |
| ACCOUNTTYPE | Optional | string | Account type for the vendor bank account to which payments are made. Use `1` for cheque account, `2` for savings account, `3` for transmission account, or `4` for bond account. |
| ACCOUNTCODE | Optional | string | Beneficiary account code. Use 20 or fewer characters. |
| PROOFOFPYMT | Optional | boolean | Proof of payment flag, which specifies whether to print the proof of payment when the bank file payment is authorized. Use `false` for No, `true` for Yes. |
| PYMTREFERENCE | Required | string | User reference, which is a meaningful reference number to connect the bank file and the bills to be paid, enabling payments to be tracked. Use 20 or fewer alphanumeric characters. |

**GB**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BANKACCOUNTNUMBER | Required | string | Beneficiary account number. Use 8 or fewer digits, including hyphens and spaces. |
| ACCOUNTNAME | Required | string | Beneficiary name. Use 18 or fewer characters. |
| SORTCODE | Required | string | Beneficiary sort code, which is the 6-digit branch number of the vendor bank |

`PROVIDERVENDOR`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PROVIDERID | Required | string | ID of the payment provider |
| STATUS | Required | string | Status. Use `active` or `inactive`. |

* * *

### Create Vendor (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/vendors/#history-create-vendor-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Behavior changes (see the release notes) |
| 2020 Release 2 | Added retainagepercentage |
|  | Updated note about RETAINAGEPERCENTAGE |

#### `create_vendor`

```
<create_vendor>
    <vendorid>V1234</vendorid>
    <name>SaaS Company Inc</name>
    <contactinfo>
        <contact>
            <contactname>SaaS Company Inc(VV1234)</contactname>
            <printas>SaaS Company Inc</printas>
        </contact>
    </contactinfo>
</create_vendor>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| vendorid | Optional | string | Unique ID for the vendor. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value. |
| name | Required | string | Name |
| parentid | Optional | string | Parent vendor ID |
| termname | Optional | string | Payment term |
| glaccountno | Optional | string | Default expense GL account number |
| vendtype | Optional | string | Vendor type ID |
| taxid | Optional | string | Tax ID |
| taxsolutionid | Optional | string | Tax solution |
| taxschedule | Optional | string | You can assign a default tax schedule for a vendor contact. When you create an AP transaction, the tax details from the assigned schedule are used as the default for the AP line entry. The tax details can be overridden through the UI |
| creditlimit | Optional | currency | Credit limit |
| retainagepercentage | Optional | numeric | Default retainage percentage for vendors (Construction or Projects subscription). |
| paymethod | Optional | string | Preferred payment method |
| billingtype | Optional | string | Vendor billing type |
| vendoraccountno | Optional | string | Vendor account number |
| displocacctnocheck | Optional | boolean | Display location assigned account number on check stub. Use `false` for No, `true` for Yes. (Default: `false`) |
| onhold | Optional | boolean | On hold. Use `false` for No, `true` for Yes. (Default: `false`) |
| donotcutcheck | Optional | boolean | Do not pay. Use `false` for No, `true` for Yes. (Default: `false`) |
| comments | Optional | string | Comments |
| status | Optional | string | Status. Use `active` for Active or `inactive` for Inactive (Default: `active`) |
| currency | Optional | string | Default currency code |
| onetime | Optional | boolean | One time. Use `false` for No, `true` for Yes. (Default: `false`) |
| primary | Optional | object | Primary contact. If blank system will use the corresponding `contactinfo`. |
| returnto | Optional | object | Return to contact. If blank system will use the corresponding `contactinfo`. |
| payto | Optional | object | Pay to contact. If blank system will use the corresponding `contactinfo`. |
| contactinfo | Optional | object | Contact info |
| contactto1099 | Optional | object | 1099 contact. If blank system will use the corresponding `contactinfo`. |
| contactlist | Optional | `contactitem[0...n]` | Contact list. If not provided, any values supplied for other contacts (Primary, Pay to, or Return to) are used to create a contact list. |
| name1099 | Optional | string | Form 1099 name |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| customfields | Optional | `customfield[0...n]` | Custom fields |
| paymentnotify | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. (Default: `false`) |
| achenabled | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. (Default: `false`) |
| achbankroutingnumber | Optional | string | ACH bank routing number |
| achaccountnumber | Optional | string | ACH bank account number |
| achaccounttype | Optional | string | ACH bank account type |
| achremittancetype | Optional | string | ACH bank account class |
| displaytermdiscount | Optional | boolean | Display term discount on check stub. Use `false` for No, `true` for Yes. (Default: `true`) |
| visibility | Optional | object | Restrictions |
| supdocid | Optional | string | Attachments ID |
| mergepaymentreq | Optional | boolean | Merge payment requests. Use `false` for No, `true` for Yes. (Default: `true`) |
| offsetglaccountno | Optional | string | AP account number |

`primary`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`returnto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`payto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`contactinfo`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contact | Required | object | New contact to create corresponding with the vendor |

`contact`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name |
| printas | Required | string | Print as |
| taxable | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
| companyname | Optional | string | Company name |
| taxgroup | Optional | string | Contact tax group name |
| prefix | Optional | string | Prefix |
| firstname | Optional | string | First name |
| lastname | Optional | string | Last name |
| initial | Optional | string | Middle name |
| phone1 | Optional | string | Primary phone number |
| phone2 | Optional | string | Secondary phone number |
| cellphone | Optional | string | Cellular phone number |
| pager | Optional | string | Pager number |
| fax | Optional | string | Fax number |
| email1 | Optional | string | Primary email address |
| email2 | Optional | string | Secondary email address |
| url1 | Optional | string | Primary URL |
| url2 | Optional | string | Secondary URL |
| status | Optional | string | Status. Use `active` for Active or `inactive` for Inactive (Default: `active`) |
| mailaddress | Optional | object | Mail address |
| taxid | Optional | string | Tax ID |

`mailaddress`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| address1 | Optional | string | Address line 1 |
| address2 | Optional | string | Address line 2 |
| address3 | Optional | string | Address line 3 |
| city | Optional | string | City |
| state | Optional | string | State/province |
| zip | Optional | string | Zip/postal code |
| country | Optional | string | Country |
| isocountrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `isocountrycode` must be provided. |
| latitude | Optional | string | Latitude |
| longitude | Optional | string | Longitude |

`contactto1099`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`contactitem`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| category | Required | string | Contact category, such as work, home, and so forth. |
| contactname | Required | string | Contact name of an existing contact |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`visibility`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| visibility\_type | Required | string | Restriction type. Use `Unrestricted`, `RootOnly`, or `Restricted`. (Default `Unrestricted`) |
| restricted\_locs | Optional | `locationid[0...n]` | Restricted location IDs |
| restricted\_depts | Optional | `departmentid[0...n]` | Restricted department IDs |

* * *

### Update Vendor

[History](https://developer.intacct.com/api/accounts-payable/vendors/#history-update-vendor)

| Release | Changes |
| --- | --- |
| 2021 Release 4 | Added PROVIDERVENDORS |
| 2021 Release 3 | Added VENDORCONTACTS, VENDOREMAILTEMPLATES, VENDORACCTNOLOCATIONS, FILEPAYMENTSERVICE, PYMTCOUNTRYCODE, VENDORBANKFILEDETAILS, and ISINDIVIDUAL |
| 2020 Release 2 | Added RETAINAGEPERCENTAGE |
| 2018 Release 4 | Added DEFAULT\_LEAD\_TIME |
|  | Updated note about RETAINAGEPERCENTAGE |

#### `update`

> Updates a vendor with a new payment term:

```
<update>
    <VENDOR>
        <RECORDNO>59</RECORDNO>
        <TERMNAME>NET15</TERMNAME>
    </VENDOR>
</update>
```

> Updates a vendor to delete the existing contact list and email templates:

```
<update>
    <VENDOR>
        <RECORDNO>59</RECORDNO>
        <VENDORCONTACTS></VENDORCONTACTS>
        <VENDOREMAILTEMPLATES></VENDOREMAILTEMPLATES>
    </VENDOR>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| VENDOR | Required | object | Object to update |

`VENDOR`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of vendor to update. Required if not using `VENDORID`. |
| VENDORID | Optional | string | Vendor ID. Required if not using `RECORDNO`. |
| NAME | Optional | string | Name |
| DISPLAYCONTACT | Optional | object | Contact info |
| STATUS | Optional | string | Status. Use `active` for Active or `inactive` for Inactive (Default: `active`) |
| ONETIME | Optional | boolean | One time. Use `false` for No, `true` for Yes. (Default: `false`) |
| HIDEDISPLAYCONTACT | Optional | boolean | Exclude from contact list. Use `false` for No, `true` for Yes. (Default: `false`) |
| VENDTYPE | Optional | string | Vendor type ID |
| PARENTID | Optional | string | Parent vendor ID |
| GLGROUP | Optional | string | GL group name |
| DEFAULT\_LEAD\_TIME | Optional | integer | Default lead time in days for inventory replenishment purposes. (Default: 1) |
| TAXID | Optional | string | Tax ID |
| TAXSCHEDULE | Optional | string | You can assign a default tax schedule for a vendor contact. When you create an AP transaction, the tax details from the assigned schedule are used as the default for the AP line entry. The tax details can be overridden through the UI |
| TAXSOLUTIONID | Optional | string | Tax solution. Required if providing Tax Schedule |
| NAME1099 | Optional | string | Form 1099 name |
| FORM1099TYPE | Optional | string | Form 1099 type |
| FORM1099BOX | Optional | string | Form 1099 box |
| SUPDOCID | Optional | string | Attachments ID |
| APACCOUNT | Optional | string | Default expense GL account number |
| OFFSETGLACCOUNTNO | Optional | string | AP account number |
| CREDITLIMIT | Optional | currency | Credit limit |
| RETAINAGEPERCENTAGE | Optional | numeric | Default retainage percentage (Construction or Projects subscription). |
| ONHOLD | Optional | boolean | On hold. Use `false` for No, `true` for Yes. (Default: `false`) |
| DONOTCUTCHECK | Optional | boolean | Do not pay. Use `false` for No, `true` for Yes. (Default: `false`) |
| COMMENTS | Optional | string | Comments |
| CURRENCY | Optional | string | Default currency code |
| CONTACTINFO | Optional | object | Primary contact. If blank system will use DISPLAYCONTACT. |
| PAYTO | Optional | object | Pay to contact. The system automatically appends a corresponding `Pay to Contact` to the contact list. If blank system will use DISPLAYCONTACT. |
| RETURNTO | Optional | object | Return to contact. The system automatically appends a corresponding `Return to Contact` to the contact list. If blank system will use DISPLAYCONTACT. |
| CONTACT\_LIST\_INFO | Optional | `CONTACT_LIST_INFO`\[\] | Contact list (alternative to `VENDORCONTACTS`). Multiple individual `CONTACT_LIST_INFO` elements may be passed. If this parameter is omitted, the original contact list remains intact. If you supply new elements, these are **appended** to the list. Passing an empty `CONTACT_LIST_INFO` element deletes the contact list. If this parameter and `VENDORCONTACTS` are both provided, `VENDORCONTACTS` is used. If there is not an existing contact list, any values supplied for other contacts (Primary, Pay to, or Return to) are used to create a contact list. |
| VENDORCONTACTS | Optional | `VENDORENTITYCONTACTS`\[0…n\] | Contact list (alternative to `CONTACT_LIST_INFO`). If this parameter is omitted, the original contact list remains intact. If you supply new elements, these are **appended** to the list. Passing an empty `VENDORCONTACTS` element deletes the contact list. If this parameter and `CONTACT_LIST_INFO` are both provided, `VENDORCONTACTS` is used. If there is not an existing contact list, any values supplied for other contacts (Primary, Pay to, or Return to) are used to create a contact list. |
| VENDOREMAILTEMPLATES | Optional | `VENDOREMAILTEMPLATE`\[0…n\] | Vendor email templates. If this parameter is omitted, the original vendor email templates remain intact. If you supply new elements, these **replace** the set of templates. Passing an empty `VENDOREMAILTEMPLATES` element deletes the set of templates. |
| VENDORACCTNOLOCATIONS | Optional | `VENDORACCTNOLOCHEAD`\[0…n\] | Vendor location assigned account numbers (alternative to `VENDOR_ACCTNO_LOC_HEAD`). If this parameter is omitted, the original set remains intact. If you supply new elements, these **replace** the original set. Passing an empty `VENDORACCTNOLOCATIONS` element deletes the set. If this parameter and `VENDOR_ACCTNO_LOC_HEAD` are both provided, `VENDORACCTNOLOCATIONS` is used. |
| VENDOR\_ACCTNO\_LOC\_HEAD | Optional | `VENDOR_ACCTNO_LOC_HEAD`\[\] | Vendor location assigned account numbers (alternative to `VENDORACCTNOLOCATIONS`). If this parameter is omitted, the original set remains intact. Multiple individual `VENDOR_ACCTNO_LOC_HEAD` elements may be passed. If this parameter and `VENDORACCTNOLOCATIONS` are both provided, `VENDORACCTNOLOCATIONS` is used. |
| FILEPAYMENTSERVICE | Optional | string | Enable direct payments to this vendor using a bank file. Choose `ACH`, `BANKFILE`, or `NONE`. (Default: `NONE`) |
| PYMTCOUNTRYCODE | Optional | string | Country code for a vendor. Required if the vendor is to receive bank file payments. Choose `AU`, `ZA`, or `GB`. (AU, GB, ZA only) |
| VENDORBANKFILEDETAILS | Optional | VENDORBANKFILEDETAIL\[\] | Vendor bank file payment details. The values you provide are validated if `FILEPAYMENTSERVICE` is set to `BANKFILE`. (AU, GB, ZA only) |
| PROVIDERVENDORS | Optional | PROVIDERVENDOR\[\] | Electronic payment providers to link to this vendor. If this parameter is omitted, the original set remains intact. If you supply new elements, these **replace** the original set. You can also update a [PROVIDERVENDOR](https://developer.intacct.com/api/accounts-payable/payment-provider-vendor/#update-payment-provider-vendor) object directly, but you cannot delete a `PROVIDERVENDOR` object. (Early Adopter program) |
| PAYMETHODKEY | Optional | string | Preferred payment method |
| MERGEPAYMENTREQ | Optional | boolean | Merge payment requests. Use `false` for No, `true` for Yes. (Default: `true`) |
| PAYMENTNOTIFY | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. (Default: `false`) |
| BILLINGTYPE | Optional | string | Vendor billing type |
| PAYMENTPRIORITY | Optional | string | Payment priority |
| TERMNAME | Optional | string | Payment term |
| DISPLAYTERMDISCOUNT | Optional | boolean | Display term discount on check stub. Use `false` for No, `true` for Yes. (Default: `true`) |
| ACHENABLED | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. (Default: `false`) |
| ACHBANKROUTINGNUMBER | Optional | string | ACH bank routing number |
| ACHACCOUNTNUMBER | Optional | string | ACH bank account number |
| ACHACCOUNTTYPE | Optional | string | ACH bank account type |
| ACHREMITTANCETYPE | Optional | string | ACH bank account class |
| VENDORACCOUNTNO | Optional | string | Vendor account number |
| DISPLOCACCTNOCHECK | Optional | boolean | Display location assigned account number on check stub. Use `false` for No, `true` for Yes. (Default: `false`) |
| OBJECTRESTRICTION | Optional | string | Restriction type. Use `Unrestricted`, `RootOnly`, or `Restricted`. (Default `Unrestricted`) |
| RESTRICTEDLOCATIONS | Optional | string | Restricted location IDs. Use if OBJECTRESTRICTION is `Restricted`. Implode multiple IDs with `#~#`. |
| RESTRICTEDDEPARTMENTS | Optional | string | Restricted department IDs. Use if OBJECTRESTRICTION is `Restricted`. Implode multiple IDs with `#~#`. |
| ISINDIVIDUAL | Optional | boolean | Specifies whether to mark the vendor as an individual person so that personally identifiable information (PII) can be masked. Use `false` for No, `true` for Yes. (Vendor Payments powered by CSI) |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`DISPLAYCONTACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PRINTAS | Optional | string | Print as |
| COMPANYNAME | Optional | string | Company name |
| TAXABLE | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
| TAXGROUP | Optional | string | Contact tax group name |
| TAXSCHEDULE | Optional | string | You can assign a default tax schedule for a vendor contact. When you create an AP transaction, the tax details from the assigned schedule are used as the default for the AP line entry. The tax details can be overridden through the UI |
| TAXSOLUTIONID | Optional | string | Tax solution. Required if providing Tax Schedule |
| PREFIX | Optional | string | Prefix |
| FIRSTNAME | Optional | string | First name |
| LASTNAME | Optional | string | Last name |
| INITIAL | Optional | string | Middle name |
| PHONE1 | Optional | string | Primary phone number |
| PHONE2 | Optional | string | Secondary phone number |
| CELLPHONE | Optional | string | Cellular phone number |
| PAGER | Optional | string | Pager number |
| FAX | Optional | string | Fax number |
| EMAIL1 | Optional | string | Primary email address |
| EMAIL2 | Optional | string | Secondary email address |
| URL1 | Optional | string | Primary URL |
| URL2 | Optional | string | Secondary URL |
| MAILADDRESS | Optional | object | Mail address |

`MAILADDRESS`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ADDRESS1 | Optional | string | Address line 1 |
| ADDRESS2 | Optional | string | Address line 2 |
| ADDRESS3 | Optional | string | Address line 3 |
| CITY | Optional | string | City |
| STATE | Optional | string | State/province |
| ZIP | Optional | string | Zip/postal code |
| COUNTRY | Optional | string | Country |
| ISOCOUNTRYCODE | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `COUNTRY` and `ISOCOUNTRYCODE` must be provided. |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Primary contact name |

`PAYTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Pay to contact name |

`RETURNTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Return to contact name |

`CONTACT_LIST_INFO`

If the category and contact name you provide for a contact matches one already in the contact list, your entry is skipped.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CATEGORYNAME | Required | string | Contact category, such as work, home, and so forth. |
| CONTACT | Optional | object | Category |

`VENDORENTITYCONTACTS`

If the category and contact name you provide for a contact matches one already in the contact list, your entry is skipped.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CATEGORYNAME | Required | string | Contact category, such as work, home, and so forth. |
| CONTACT | Required | object | Contact |

`CONTACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| NAME | Required | string | Contact name |

`VENDOREMAILTEMPLATE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| EMAILTEMPLATENAME | Required | string | Name of the email template |
| DOCPARID | Required | string | Document type, such as Purchase Order |

`VENDORACCTNOLOCHEAD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATION | Required | string | Location ID |
| ACCOUNTNO | Required | string | Account number |

`VENDOR_ACCTNO_LOC_HEAD`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATION | Required | string | Location ID |
| ACCOUNTNO | Required | string | Account number |

`VENDORBANKFILEDETAIL`

Available for Australia (AU), South Africa (ZA), or the United Kingdom (GB).

**AU**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of bank file details to update. |
| BANKACCOUNTNUMBER | Required | string | Creditor account number. Use 9 or fewer digits, including hyphens and spaces. |
| ACCOUNTNAME | Required | string | Creditor account name. Use 16 or fewer alphanumeric characters. |
| BSBNUMBER | Required | string | Creditor BSB number, which is the 6-digit hyphenated branch number of the vendor bank account. For example, `123-456`. |
| PYMTREFERENCE | Required | string | Meaningful reference number to connect the bank file and the bills to be paid, enabling payments to be tracked. Use 18 or fewer alphanumeric characters. |

**ZA**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of bank file details to update. |
| ACCOUNTNAME | Optional | string | Homing account name for the vendor bank account to which payments are made. Use 30 or fewer digits. |
| BANKACCOUNTNUMBER | Required | string | Homing account number for the vendor bank account to which payments are made. Use 31 or fewer digits. |
| BRANCHCODE | Required | string | Homing branch, which is the 6-digit branch number of the vendor bank |
| ACCOUNTTYPE | Optional | string | Account type for the vendor bank account to which payments are made. Use `1` for cheque account, `2` for savings account, `3` for transmission account, or `4` for bond account. |
| ACCOUNTCODE | Optional | string | Beneficiary account code. Use 20 or fewer characters. |
| PROOFOFPYMT | Optional | boolean | Proof of payment flag, which specifies whether to print the proof of payment when the bank file payment is authorized. Use `false` for No, `true` for Yes. |
| PYMTREFERENCE | Required | string | User reference, which is a meaningful reference number to connect the bank file and the bills to be paid, enabling payments to be tracked. Use 20 or fewer alphanumeric characters. |

**GB**

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of bank file details to update. |
| BANKACCOUNTNUMBER | Required | string | Beneficiary account number. Use 8 or fewer digits, including hyphens and spaces. |
| ACCOUNTNAME | Required | string | Beneficiary name. Use 18 or fewer characters. |
| SORTCODE | Required | string | Beneficiary sort code, which is the 6-digit branch number of the vendor bank |

`PROVIDERVENDOR`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the provider vendor object to update |
| PROVIDERID | Optional | string | ID of the payment provider |
| STATUS | Required | string | Status. Use `active` or `inactive`. |

* * *

### Update Vendor (Legacy)

[History](https://developer.intacct.com/api/accounts-payable/vendors/#history-update-vendor-legacy)

| Release | Changes |
| --- | --- |
| 2021 Release 3 | Behavior changes (see the release notes) |
| 2020 Release 2 | Added retainagepercentage |
|  | Updated note about RETAINAGEPERCENTAGE |

#### `update_vendor`

```
<update_vendor vendorid="V1234">
    <name>SaaS Company Inc</name>
    <termname>N15</termname>
</update_vendor>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| vendorid | Required | string | Vendor ID to update |
| name | Optional | string | Name |
| parentid | Optional | string | Parent vendor ID |
| termname | Optional | string | Payment term |
| glaccountno | Optional | string | Default expense GL account number |
| vendtype | Optional | string | Vendor type ID |
| taxid | Optional | string | Tax ID |
| taxsolutionid | Optional | string | Tax solution. Required if providing Tax Schedule |
| taxschedule | Optional | string | You can assign a default tax schedule for a vendor contact. When you create an AP transaction, the tax details from the assigned schedule are used as the default for the AP line entry. The tax details can be overridden through the UI |
| creditlimit | Optional | currency | Credit limit |
| retainagepercentage | Optional | numeric | Default retainage percentage for vendors (Construction or Projects subscription). |
| paymethod | Optional | string | Preferred payment method |
| billingtype | Optional | string | Vendor billing type |
| vendoraccountno | Optional | string | Vendor account number |
| displocacctnocheck | Optional | boolean | Display location assigned account number on check stub. Use `false` for No, `true` for Yes. |
| onhold | Optional | boolean | On hold. Use `false` for No, `true` for Yes. |
| donotcutcheck | Optional | boolean | Do not pay. Use `false` for No, `true` for Yes. |
| comments | Optional | string | Comments |
| status | Optional | string | Status. Use `active` for Active or `inactive` for Inactive. |
| currency | Optional | string | Default currency code |
| primary | Optional | object | Primary contact. If blank system will use the corresponding `contactinfo`. |
| returnto | Optional | object | Return to contact. The system automatically appends a corresponding `Return to Contact` to the contact list. If blank system will use the corresponding `contactinfo`. |
| payto | Optional | object | Pay to contact. The system automatically appends a corresponding `Pay to Contact` to the contact list. If blank system will use the corresponding `contactinfo`. |
| contactinfo | Optional | object | Contact info |
| contactto1099 | Optional | object | 1099 contact. If blank system will use the corresponding `contactinfo`. |
| contactlist | Optional | `contactitem[0...n]` | Contact list. If not provided and not already existing, any values supplied for other contacts (Primary, Pay to, or Return to) are used to create a contact list. |
| name1099 | Optional | string | Form 1099 name |
| form1099type | Optional | string | Form 1099 type |
| form1099box | Optional | string | Form 1099 box |
| customfields | Optional | `customfield[0...n]` | Custom fields |
| paymentnotify | Optional | boolean | Send automatic payment notification. Use `false` for No, `true` for Yes. |
| achenabled | Optional | boolean | ACH enabled. Use `false` for No, `true` for Yes. |
| achbankroutingnumber | Optional | string | ACH bank routing number |
| achaccountnumber | Optional | string | ACH bank account number |
| achaccounttype | Optional | string | ACH bank account type |
| achremittancetype | Optional | string | ACH bank account class |
| displaytermdiscount | Optional | boolean | Display term discount on check stub. Use `false` for No, `true` for Yes. |
| visibility | Optional | object | Restrictions |
| supdocid | Optional | string | Attachments ID |
| mergepaymentreq | Optional | boolean | Merge payment requests. Use `false` for No, `true` for Yes. |
| offsetglaccountno | Optional | string | AP account number |

`primary`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`returnto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`payto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`contactinfo`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contact | Required | object | New contact to create corresponding with the vendor |

`contact`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name |
| printas | Required | string | Print as |
| taxable | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
| companyname | Optional | string | Company name |
| taxgroup | Optional | string | Contact tax group name |
| prefix | Optional | string | Prefix |
| firstname | Optional | string | First name |
| lastname | Optional | string | Last name |
| initial | Optional | string | Middle name |
| phone1 | Optional | string | Primary phone number |
| phone2 | Optional | string | Secondary phone number |
| cellphone | Optional | string | Cellular phone number |
| pager | Optional | string | Pager number |
| fax | Optional | string | Fax number |
| email1 | Optional | string | Primary email address |
| email2 | Optional | string | Secondary email address |
| url1 | Optional | string | Primary URL |
| url2 | Optional | string | Secondary URL |
| status | Optional | string | Status. Use `active` for Active or `inactive` for Inactive (Default: `active`) |
| mailaddress | Optional | object | Mail address |
| taxid | Optional | string | Tax ID |

`mailaddress`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| address1 | Optional | string | Address line 1 |
| address2 | Optional | string | Address line 2 |
| address3 | Optional | string | Address line 3 |
| city | Optional | string | City |
| state | Optional | string | State/province |
| zip | Optional | string | Zip/postal code |
| country | Optional | string | Country |
| isocountrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `isocountrycode` must be provided. |
| latitude | Optional | string | Latitude |
| longitude | Optional | string | Longitude |

`contactto1099`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`contactitem`

If the category and contact name you provide matches one already in the contact list, your entry is skipped.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| category | Required | string | Contact category, such as work, home, and so forth. |
| contactname | Required | string | Contact name of an existing contact |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

`visibility`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| visibility\_type | Required | string | Restriction type. Use `Unrestricted`, `RootOnly`, or `Restricted`. (Default `Unrestricted`) |
| restricted\_locs | Optional | `locationid[0...n]` | Restricted location IDs |
| restricted\_depts | Optional | `departmentid[0...n]` | Restricted department IDs |

* * *

### Delete Vendor

#### `delete`

```
<delete>
    <object>VENDOR</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOR` |
| keys | Required | string | Comma-separated list of vendor `RECORDNO` to delete |

* * *

### Delete Vendor (Legacy)

#### `delete_vendor`

```
<delete_vendor vendorid="V1234"></delete_vendor>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| vendorid | Required | string | Vendor ID to delete |

* * *

### Create Location Specific Vendor Account Number (Legacy)

#### `create_vendorentityaccountno`

```
<create_vendorentityaccountno>
    <vendorid>V1234</vendorid>
    <accountno>9876543210</accountno>
    <locationid>100</locationid>
</create_vendorentityaccountno>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| vendorid | Required | string | Vendor ID |
| accountno | Required | string | Vendor account number |
| locationid | Required | string | Location ID |

* * *

Vendor Approvals
----------------

[History](https://developer.intacct.com/api/accounts-payable/vendors/#history-approve-vendor)

| Release | Changes |
| --- | --- |
| 2023 Release 4 | Added getVendorsToApprove, approveVendor, declineVendor, and getVendorApprovalHistory |

When vendor approval is enabled, new and recently edited vendors are automatically submitted to an approval queue. Designated approvers review those vendors and either approve or decline them. For more information, see [About vendor approvals](https://www.intacct.com/ia/docs/en_US/help_action/Accounts_Payable/Approvals/Vendor_approvals/about-vendor-approvals.htm?TocPath=Applications%7CAccounts%20Payable%7CSetup%7CApprovals%7CVendor%20approval%7C_____1).

### Get Vendors to Approve

#### `getVendorsToApprove`

```
<getVendorsToApprove/>
```

* * *

### Approve Vendors

#### `approveVendor`

```
<approveVendor>
     <recordno>583</recordno>
     <reviewcomments>Approved by purchasing director</reviewcomments>
</approveVendor> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | integer | Record number of vendor to approve. |
| reviewcomments | Optional | string | Reviewer comments |

* * *

### Decline Vendors

#### `declineVendor`

```
<declineVendor>
     <recordno>590</recordno>
     <reviewcomments>Declined by purchasing director</reviewcomments>
</declineVendor> 
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | integer | Record number of vendor to decline. |
| reviewcomments | Optional | string | Reviewer comments |

* * *

### Get Vendor Approval History

#### `getVendorApprovalHistory`

```
<getVendorApprovalHistory>
     <recordno>576</recordno>
</getVendorApprovalHistory>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| recordno | Required | integer | Record number of vendor to get approval history for. |

* * *

Vendor Email Templates
----------------------

### Get Vendor Email Template Object Definition

#### `lookup`

> List all the fields and relationships for the vendor email template object:

```
<lookup>
    <object>VENDOREMAILTEMPLATE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOREMAILTEMPLATE` |

* * *

### Query and List Vendor Email Templates

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the template name and vendor ID for each vendor email template:

```
<query>
    <object>VENDOREMAILTEMPLATE</object>
    <select>
        <field>EMAILTEMPLATENAME</field>
        <field>VENDORID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOREMAILTEMPLATE` |
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

### Query and List Vendor Email Templates (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>VENDOREMAILTEMPLATE</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOREMAILTEMPLATE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Vendor Email Template

#### `read`

```
<read>
    <object>VENDOREMAILTEMPLATE</object>
    <keys>8</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDOREMAILTEMPLATE` |
| keys | Required | string | Comma-separated list of vendor email template `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Vendor Visibility
-----------------

### Get Vendor Visibility Object Definition

#### `lookup`

> List all the fields and relationships for the vendor visibility object:

```
<lookup>
    <object>VENDORVISIBILITY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDORVISIBILITY` |

### Get Vendor Visibility

#### `read`

```
<read>
    <object>VENDORVISIBILITY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `VENDORVISIBILITY` |
| keys | Required | string | Comma-separated list of vendor visibility `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

