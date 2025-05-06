Title: Contacts

URL Source: https://developer.intacct.com/api/company-console/contacts/

Markdown Content:
*   [Get Contact Object Definition](https://developer.intacct.com/api/company-console/contacts/#get-contact-object-definition)
*   [Query and List Contacts](https://developer.intacct.com/api/company-console/contacts/#query-and-list-contacts)
*   [Query and List Contacts (Legacy)](https://developer.intacct.com/api/company-console/contacts/#query-and-list-contacts-legacy)
*   [Get Contact](https://developer.intacct.com/api/company-console/contacts/#get-contact)
*   [Get Contact by ID](https://developer.intacct.com/api/company-console/contacts/#get-contact-by-id)
*   [Create Contact](https://developer.intacct.com/api/company-console/contacts/#create-contact)
*   [Create Contact (Legacy)](https://developer.intacct.com/api/company-console/contacts/#create-contact-legacy)
*   [Update Contact](https://developer.intacct.com/api/company-console/contacts/#update-contact)
*   [Update Contact (Legacy)](https://developer.intacct.com/api/company-console/contacts/#update-contact-legacy)
*   [Delete Contact](https://developer.intacct.com/api/company-console/contacts/#delete-contact)
*   [Delete Contact (Legacy)](https://developer.intacct.com/api/company-console/contacts/#delete-contact-legacy)

* * *

Contacts are shared across the entire system and are used to send event notifications, to determine ship-to/bill-to, pay-to/return-to addresses in Order Entry and Purchasing transactions, and to determine tax on transactions.

* * *

#### `lookup`

> List all the fields and relationships for the contact object:

```
<lookup>
    <object>CONTACT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTACT` |

* * *

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each contact:

```
<query>
    <object>CONTACT</object>
    <select>
        <field>RECORDNO</field>
        <field>CONTACTNAME</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTACT` |
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

#### `readByQuery`

```
<readByQuery>
    <object>CONTACT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTACT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

#### `read`

```
<read>
    <object>CONTACT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTACT` |
| keys | Required | string | Comma-separated list of contact `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

#### `readByName`

```
<readByName>
    <object>CONTACT</object>
    <keys>TEST</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTACT` |
| keys | Required | string | Comma-separated list of `CONTACTNAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

#### `create`

```
<create>
    <CONTACT>
        <CONTACTNAME>hello</CONTACTNAME>
        <PRINTAS>world</PRINTAS>
    </CONTACT>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACT | Required | object | Object to create |

`CONTACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Contact name to create |
| PRINTAS | Required | string | Print as |
| COMPANYNAME | Optional | string | Company name |
| TAXABLE | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
| TAXGROUP | Optional | string | Contact tax group name |
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
| STATUS | Optional | string | Status. Use `active` for Active or `inactive` for Inactive (Default: `active`) |
| MAILADDRESS | Optional | object | Mail address |
| TAXSCHEDULE | Optional | object | You can assign a default tax schedule for a contact. When you create an AP or AR transaction, the tax details from the assigned schedule are used as the default for the AP or AR line entry. The tax details can be overridden through the UI |
| TAXSOLUTIONID | Optional | string | Tax solution. Required if providing Tax Schedule |

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
| COUNTRYCODE | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `COUNTRY` and `COUNTRYCODE` must be provided. |

* * *

#### `create_contact`

```
<create_contact>
    <contactname>Hello</contactname>
    <printas>World</printas>
</create_contact>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name to create |
| printas | Required | string | Print as |
| companyname | Optional | string | Company name |
| taxable | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
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
| taxschedule | Optional | string | You can assign a default tax schedule for a contact. When you create an AP or AR transaction, the tax details from the assigned schedule are used as the default for the AP or AR line entry. The tax details can be overridden through the UI |
| taxsolutionid | Optional | string | Tax solution. Required if providing Tax Schedule |

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
| countrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `countrycode` must be provided. |
| latitude | Optional | string | Latitude |
| longitude | Optional | string | Longitude |

* * *

#### `update`

```
<update>
    <CONTACT>
        <RECORDNO>11</RECORDNO>
        <PRINTAS>hello world</PRINTAS>
    </CONTACT>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACT | Optional | object | Object to update |

`CONTACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of contact to update. Required if not using `CONTACTNAME`. |
| CONTACTNAME | Optional | string | Contact name. Required if not using `RECORDNO`. |
| PRINTAS | Optional | string | Print as |
| COMPANYNAME | Optional | string | Company name |
| TAXABLE | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
| TAXGROUP | Optional | string | Contact tax group name |
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
| STATUS | Optional | string | Status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |
| MAILADDRESS | Optional | object | Mail address |
| TAXSCHEDULE | Optional | object | You can assign a default tax schedule for a contact. When you create an AP or AR transaction, the tax details from the assigned schedule are used as the default for the AP or AR line entry. The tax details can be overridden through the UI |
| TAXSOLUTIONID | Optional | string | Tax solution. Required if providing Tax Schedule |

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
| COUNTRYCODE | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `COUNTRY` and `COUNTRYCODE` must be provided. |

* * *

#### `update_contact`

```
<update_contact contactname="Hello">
    <printas>World</printas>
</update_contact>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name to update |
| printas | Required | string | Print as |
| companyname | Optional | string | Company name |
| taxable | Optional | boolean | Taxable. Use `false` for No, `true` for Yes. (Default: `true`) |
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
| taxsolutionid | Optional | string | Tax solution. Required if providing Tax Schedule |
| taxschedule | Optional | string | You can assign a default tax schedule for a contact. When you create an AP or AR transaction, the tax details from the assigned schedule are used as the default for the AP or AR line entry. The tax details can be overridden through the UI |

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
| countrycode | Optional | string | ISO country code. When ISO country codes are enabled in a company, both `country` and `countrycode` must be provided. |
| latitude | Optional | string | Latitude |
| longitude | Optional | string | Longitude |

* * *

#### `delete`

```
<delete>
    <object>CONTACT</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTACT` |
| keys | Required | string | Comma-separated list of contact `RECORDNO` to delete |

* * *

#### `delete_contact`

```
<delete_contact contactname="hello"></delete_contact>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

