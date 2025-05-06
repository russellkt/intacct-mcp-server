Title: Customers

URL Source: https://developer.intacct.com/api/accounts-receivable/customers/

Markdown Content:
Blog
Guides 
API Reference
Tools & Libraries
Support
  API  Accounts Receivable  Customers
Customers
Customers
Get Customer Object Definition
Query and List Customers
Query and List Customers (Legacy)
Get Customer
Get Customer by ID
Create Customer
Create Customer (Legacy)
Update Customer
Update Customer (Legacy)
Delete Customer
Delete Customer (Legacy)
Customer Email Templates
Get Customer Email Template Object Definition
Query and List Customer Email Templates
Query and List Customer Email Templates (Legacy)
Get Customer Email Template
Get Customer Email Template by ID
Customer Visibility
Get Customer Visibility Object Definition
Get Customer Visibility

A Customer is any company to which you sell goods and services.

Other Sage Intacct applications use customer information—not only for record-keeping purposes, but also for printing names and addresses on forms, such as invoices, and for determining the location of the Ship To contact so that sales can be computed correctly.

You can associate existing custom email templates with customers to tailor communications about transactions.

Customers
Get Customer Object Definition
lookup

List all the fields and relationships for the customer object:

<lookup>
    <object>CUSTOMER</object>
</lookup>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMER
Query and List Customers
query

List the record number, shipto contact name, and total amount due for all customers with total due > 100:

<query>
    <object>CUSTOMER</object>
    <filter>
        <greaterthan>
            <field>TOTALDUE</field>
            <value>100</value>
        </greaterthan>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>SHIPTOCONTACT.CONTACTNAME</field>
        <field>TOTALDUE</field>
    </select>
</query>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMER
filter	Optional	object	Filter expression to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, VENDOR.CREDITLIMIT on APBILL).
select	Required	sequence	The names of the fields that you want included in the response, and an optional aggregate function such as count or sum. Returning all fields is not supported.
orderby	Optional	object	Provide an order element with a field name and choose an ascending or descending sort order, for example:
<order>
  <field>RECORDNO</field>
  <descending/>
</order>
options	Optional	object	Query options:
Set the caseinsensitive element to true for a case-insensitive query
 <caseinsensitive>true</caseinsensitive>
In a multi-entity company, set the showprivate element to true to query data in private entities:
 <showprivate>true</showprivate>
Specify the returnformat for the response: xml (default), json, or csv
 <returnformat>json</returnformat>

pagesize	Optional	integer	Maximum number of matching objects to return in the response, between 1 and 2000 items (Default: 100)
offset	Optional	integer	Point at which to start indexing into records (Default: 0)
Query and List Customers (Legacy)
readByQuery
<readByQuery>
    <object>CUSTOMER</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMER
fields	Optional	string	Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide * for the value.
query	Required	string	SQL-like query based on fields on the object. The following operators are supported: <, >, >=, <=, =, like, not like, in, not in, IS NOT NULL, IS NULL, AND, OR. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes ('Jane\'s Deli'). Joins are not supported.
pagesize	Optional	integer	Custom page size between 1 and 1000 items (Default: 100)
Get Customer
read
<read>
    <object>CUSTOMER</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMER
keys	Required	string	Comma-separated list of customer RECORDNO to get
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Get Customer by ID
readByName
<readByName>
    <object>CUSTOMER</object>
    <keys>C1234</keys>
    <fields>*</fields>
</readByName>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMER
keys	Required	string	Comma-separated list of customer CUSTOMERID to get
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Create Customer

History

create

Creates a customer and specifies a display contact and a contact list (provided via customer contacts):

<create>
    <CUSTOMER>
        <CUSTOMERID>C1234</CUSTOMERID>
        <NAME>SaaS Company Inc</NAME>
        <DISPLAYCONTACT>
            <PRINTAS>SaaS Company Inc</PRINTAS>
            <COMPANYNAME>SaaS Co</COMPANYNAME>
            <TAXABLE>true</TAXABLE>
            <TAXGROUP>CA</TAXGROUP>
            <TAXSOLUTIONID>US Sales Tax - SYS</TAXSOLUTIONID>
            <TAXSCHEDULE>US Purchase Goods Standard</TAXSCHEDULE>
            <PREFIX>Mr</PREFIX>
            <FIRSTNAME>Bill</FIRSTNAME>
            <LASTNAME>Smith</LASTNAME>
            <INITIAL>G</INITIAL>
            <PHONE1>12</PHONE1>
            <PHONE2>34</PHONE2>
            <CELLPHONE>56</CELLPHONE>
            <PAGER>78</PAGER>
            <FAX>90</FAX>
            <EMAIL1></EMAIL1>
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
        <CUSTTYPE>SaaS</CUSTTYPE>
        <PARENTID>C5678</PARENTID>
        <GLGROUP>Group</GLGROUP>
        <TERRITORYID>NE</TERRITORYID>
        <SUPDOCID>A1234</SUPDOCID>
        <TERMNAME>N30</TERMNAME>
        <OFFSETGLACCOUNTNO>1200</OFFSETGLACCOUNTNO>
        <ARACCOUNT>4000</ARACCOUNT>
        <SHIPPINGMETHOD>USPS</SHIPPINGMETHOD>
        <RESALENO>123</RESALENO>
        <TAXID>12-3456789</TAXID>
        <CREDITLIMIT>1234.56</CREDITLIMIT>
        <ONHOLD>false</ONHOLD>
        <DELIVERY_OPTIONS>Print</DELIVERY_OPTIONS>
        <CUSTMESSAGEID>hello</CUSTMESSAGEID>
        <COMMENTS>my comment</COMMENTS>
        <CURRENCY>USD</CURRENCY>
        <ARINVOICEPRINTTEMPLATEID>temp1</ARINVOICEPRINTTEMPLATEID>
        <OEQUOTEPRINTTEMPLATEID>temp2</OEQUOTEPRINTTEMPLATEID>
        <OEORDERPRINTTEMPLATEID>temp3</OEORDERPRINTTEMPLATEID>
        <OELISTPRINTTEMPLATEID>temp4</OELISTPRINTTEMPLATEID>
        <OEINVOICEPRINTTEMPLATEID>temp5</OEINVOICEPRINTTEMPLATEID>
        <OEADJPRINTTEMPLATEID>temp6</OEADJPRINTTEMPLATEID>
        <OEOTHERPRINTTEMPLATEID>temp7</OEOTHERPRINTTEMPLATEID>
        <CONTACTINFO>
            <CONTACTNAME>primary</CONTACTNAME>
        </CONTACTINFO>
        <BILLTO>
            <CONTACTNAME>bill to</CONTACTNAME>
        </BILLTO>
        <SHIPTO>
            <CONTACTNAME>ship to</CONTACTNAME>
        </SHIPTO>
        <OBJECTRESTRICTION>Restricted</OBJECTRESTRICTION>
        <RESTRICTEDLOCATIONS>100#~#200</RESTRICTEDLOCATIONS>
        <RESTRICTEDDEPARTMENTS>D100#~#D200</RESTRICTEDDEPARTMENTS>
        <CUSTOMFIELD1>Hello</CUSTOMFIELD1>
    </CUSTOMER>
</create>

Creates a customer and specifies a display contact and a contact list (provided via customer contacts):

<create>
    <CUSTOMER>
        <CUSTOMERID>C378</CUSTOMERID>
        <NAME>ACME Widget Company Inc.</NAME>
        <DISPLAYCONTACT>
            <PRINTAS>ACME Widget Company Inc</PRINTAS>
            <COMPANYNAME>ACME Widget Company</COMPANYNAME>
        </DISPLAYCONTACT>
        <CUSTOMERCONTACTS>
            <CUSTOMERENTITYCONTACTS>
                <CATEGORYNAME>Mobile</CATEGORYNAME>
                <CONTACT>
                    <NAME>Kristensen, Linda</NAME>
                </CONTACT>
            </CUSTOMERENTITYCONTACTS>
            <CUSTOMERENTITYCONTACTS>
                <CATEGORYNAME>Fax</CATEGORYNAME>
                <CONTACT>
                    <NAME>Kristensen, Linda</NAME>
                </CONTACT>
            </CUSTOMERENTITYCONTACTS>
        </CUSTOMERCONTACTS>
    </CUSTOMER>
</create>
Parameters
Name	Required	Type	Description
CUSTOMER	Required	object	Object to create

CUSTOMER

Name	Required	Type	Description
CUSTOMERID	Optional	string	Unique ID for the customer. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value.
NAME	Required	string	Name
DISPLAYCONTACT	Required	object	Contact info
STATUS	Optional	string	Status. Use active for Active or inactive for Inactive (Default: active)
ONETIME	Optional	boolean	One time. Use false for No, true for Yes. (Default: false)
HIDEDISPLAYCONTACT	Optional	boolean	Exclude from contact list. Use false for No, true for Yes. (Default: false)
CUSTTYPE	Optional	string	Customer type ID
CUSTREPID	Optional	string	Sales rep employee ID
PARENTID	Optional	string	Parent customer ID
GLGROUP	Optional	string	GL group name
TERRITORYID	Optional	string	Territory ID
SUPDOCID	Optional	string	Attachments ID
TERMNAME	Optional	string	Payment term
OFFSETGLACCOUNTNO	Optional	string	Offset AR GL account number
ARACCOUNT	Optional	string	Default AR GL account number
SHIPPINGMETHOD	Optional	string	Shipping method
RESALENO	Optional	string	Resale number
TAXID	Optional	string	Tax ID
CREDITLIMIT	Optional	currency	Credit limit
RETAINAGEPERCENTAGE	Optional	numeric	Default retainage percentage for customers (Construction or Projects subscription).
ONHOLD	Optional	boolean	On hold. Use false for No, true for Yes. (Default: false)
DELIVERY_OPTIONS	Optional	string	Delivery method. Use either Print, E-Mail, or Print#~#E-Mail for both. If using E-Mail, the customer contact must have a valid e-mail address.
CUSTMESSAGEID	Optional	string	Default invoice message
EMAILOPTIN	Optional	boolean	Accept emailed invoices option. Use false for No, true for Yes. Applicable only for companies configured for South Africa (ZA) VAT.
COMMENTS	Optional	string	Comments
CURRENCY	Optional	string	Default currency code
ADVBILLBY	Optional	integer	Bill in advance. Number of months or days before the start date. Use 0 through 9.
ADVBILLBYTYPE	Optional	string	Bill-in-advance time period. Required if using bill in advance. Use days or months.
ARINVOICEPRINTTEMPLATEID	Optional	string	Print option - AR invoice template name
OEQUOTEPRINTTEMPLATEID	Optional	string	Print option - OE quote template name
OEORDERPRINTTEMPLATEID	Optional	string	Print option - OE order template name
OELISTPRINTTEMPLATEID	Optional	string	Print option - OE list template name
OEINVOICEPRINTTEMPLATEID	Optional	string	Print option - OE invoice template name
OEADJPRINTTEMPLATEID	Optional	string	Print option - OE adjustment template name
OEOTHERPRINTTEMPLATEID	Optional	string	Print option - OE other template name
CONTACTINFO	Optional	object	Primary contact. If blank system will use DISPLAYCONTACT.
BILLTO	Optional	object	Bill to contact. If blank system will use DISPLAYCONTACT.
SHIPTO	Optional	object	Ship to contact. If blank system will use DISPLAYCONTACT.
CONTACT_LIST_INFO	Optional	CONTACT_LIST_INFO[]	Contact list (alternative to CUSTOMERCONTACTS). Multiple individual CONTACT_LIST_INFO elements may be passed. If this parameter and CUSTOMERCONTACTS are both provided, CUSTOMERCONTACTS is used. If neither are provided, any values supplied for other contacts (Primary, Bill to, or Ship to) are used to create a contact list.
CUSTOMERCONTACTS	Optional	CUSTOMERNTITYCONTACTS[0…n]	Contact list (alternative to CONTACT_LIST_INFO). If this parameter and CONTACT_LIST_INFO are both provided, CUSTOMERCONTACTS is used. If neither are provided, any values supplied for other contacts (Primary, Bill to, or Ship to) are used to create a contact list.
OBJECTRESTRICTION	Optional	object	Restriction type. Use Unrestricted, RootOnly, or Restricted. (Default Unrestricted)
RESTRICTEDLOCATIONS	Optional	string	Restricted location IDs. Use if OBJECTRESTRICTION is Restricted. Implode multiple IDs with #~#.
RESTRICTEDDEPARTMENTS	Optional	string	Restricted department IDs. Use if OBJECTRESTRICTION is Restricted. Implode multiple IDs with #~#.
CUSTOMEREMAILTEMPLATES	Optional	CUSTOMEREMAILTEMPLATE[1..n]	Custom email templates to override the default email templates associated with transaction definitions. You choose existing custom email templates to use for this customer, optionally specifying the transactions to which they apply.
Custom field name	varies	varies	Custom field names and values as defined for this object.
For a multi-pick-list custom field, implode multiple field values with #~#.

DISPLAYCONTACT

Name	Required	Type	Description
PRINTAS	Required	string	Print as
CONTACTNAME	Optional	string	If left blank, system will create the name as [NAME](C[CUSTOMERID])
COMPANYNAME	Optional	string	Company name
TAXABLE	Optional	boolean	Taxable. Use false for No, true for Yes. (Default: true)
TAXGROUP	Optional	string	Contact tax group name
PREFIX	Optional	string	Prefix
FIRSTNAME	Optional	string	First name
LASTNAME	Optional	string	Last name
INITIAL	Optional	string	Middle name
TAXSCHEDULE	Optional	string	You can assign a default tax schedule for a customer contact. When you create an AR transaction, the tax details from the assigned schedule are used as the default for the AR line entry. The tax details can be overridden through the UI
TAXSOLUTIONID	Optional	string	Tax solution. Required if providing Tax Schedule
Optional	string	Primary phone number	 
PHONE2	Optional	string	Secondary phone number
CELLPHONE	Optional	string	Cellular phone number
PAGER	Optional	string	Pager number
FAX	Optional	string	Fax number
EMAIL1	Optional	string	Primary email address
EMAIL2	Optional	string	Secondary email address
URL1	Optional	string	Primary URL
URL2	Optional	string	Secondary URL
MAILADDRESS	Optional	object	Mail address

MAILADDRESS

Name	Required	Type	Description
ADDRESS1	Optional	string	Address line 1
ADDRESS2	Optional	string	Address line 2
ADDRESS3	Optional	string	Address line 3
CITY	Optional	string	City
STATE	Optional	string	State/province
ZIP	Optional	string	Zip/postal code
COUNTRY	Optional	string	Country
ISOCOUNTRYCODE	Optional	string	ISO country code. When ISO country codes are enabled in a company, both COUNTRY and ISOCOUNTRYCODE must be provided.

CONTACTINFO

Name	Required	Type	Description
CONTACTNAME	Required	string	Primary contact name

BILLTO

Name	Required	Type	Description
CONTACTNAME	Required	string	Bill to contact name

SHIPTO

Name	Required	Type	Description
CONTACTNAME	Required	string	Ship to contact name

CONTACT_LIST_INFO

Name	Required	Type	Description
CATEGORYNAME	Required	string	Contact category, such as work, home, and so forth.
CONTACT	Optional	object	Category

CUSTOMERENTITYCONTACTS

If the category and contact name you provide for a contact matches one already in the contact list, your entry is skipped.

Name	Required	Type	Description
CATEGORYNAME	Required	string	Contact category, such as work, home, and so forth.
CONTACT	Required	object	Contact

CONTACT

Name	Required	Type	Description
NAME	Required	string	Contact name

CUSTOMEREMAILTEMPLATE

Name	Required	Type	Description
DOCPARID	Optional	string	Transaction definition that will use this email template. Applicable only for Order Entry, Purchasing, and Contract email templates.
EMAILTEMPLATENAME	Required	string	Name of the email template
Create Customer (Legacy)

History

create_customer
<create_customer>
    <customerid>C1234</customerid>
    <name>Volume Reseller</name>
    <primary>
        <contactname>Bill Jones</contactname>
    </primary>
    <contactinfo>
        <contact>
            <contactname>Volume Reseller(CC1234)</contactname>
            <printas>Volume Reseller</printas>
        </contact>
    </contactinfo>
</create_customer>
Parameters
Name	Required	Type	Description
customerid	Required	string	Unique ID for the customer. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value.
name	Required	string	Name
parentid	Optional	string	Parent customer ID
termname	Optional	string	Payment term
custrepid	Optional	string	Sales rep employee ID
shippingmethod	Optional	string	Shipping method
custtype	Optional	string	Customer type ID
taxid	Optional	string	Tax ID
creditlimit	Optional	currency	Credit limit
retainagepercentage	Optional	numeric	Default retainage percentage for customers (Construction or Projects subscription).
territoryid	Optional	string	Territory ID
resaleno	Optional	string	Resale number
deliveryoptions	Optional	object	Delivery method
accountlabel	Optional	string	GL account label
glaccountno	Optional	string	Default AR GL account number
glgroup	Optional	string	GL group name
onhold	Optional	boolean	On hold. Use false for No, true for Yes. (Default: false)
comments	Optional	string	Comments
status	Optional	string	Status. Use active for Active or inactive for Inactive (Default: active)
currency	Optional	string	Default currency code
primary	Optional	object	Primary contact. If blank system will use the corresponding contactinfo.
billto	Optional	object	Ship to contact. If blank system will use the corresponding contactinfo.
shipto	Optional	object	Return to contact. If blank system will use the corresponding contactinfo.
contactinfo	Optional	object	Contact info.
contactlist	Optional	contactitem[0...n]	Contact list
vsoepricelist	Optional	String	Name of a vendor-specific Order Entry price list
customfields	Optional	customfield[0...n]	Custom fields
visibility	Optional	object	Restrictions
supdocid	Optional	string	Attachments ID
offsetglaccountno	Optional	string	Offset AR GL account number

deliveryoptions

Name	Required	Type	Description
deliveryoption	Required	string	Delivery method. Use either print, email, or both. If using E-Mail, the customer contact must have a valid e-mail address.

primary

Name	Required	Type	Description
contactname	Required	string	Contact name of an existing contact

billto

Name	Required	Type	Description
contactname	Required	string	Contact name of an existing contact

shipto

Name	Required	Type	Description
contactname	Required	string	Contact name of an existing contact

contactinfo

Name	Required	Type	Description
contact	Required	object	New contact to create corresponding with the customer

contact

Name	Required	Type	Description
contactname	Required	string	Contact name
printas	Required	string	Print as
taxable	Optional	boolean	Taxable. Use false for No, true for Yes. (Default: true)
companyname	Optional	string	Company name
taxgroup	Optional	string	Contact tax group name
prefix	Optional	string	Prefix
firstname	Optional	string	First name
lastname	Optional	string	Last name
initial	Optional	string	Middle name
phone1	Optional	string	Primary phone number
phone2	Optional	string	Secondary phone number
cellphone	Optional	string	Cellular phone number
pager	Optional	string	Pager number
fax	Optional	string	Fax number
email1	Optional	string	Primary email address
email2	Optional	string	Secondary email address
url1	Optional	string	Primary URL
url2	Optional	string	Secondary URL
status	Optional	string	Status. Use active for Active or inactive for Inactive (Default: active)
mailaddress	Optional	object	Mail address
taxid	Optional	string	Tax ID
taxsolutionid	Optional	string	Tax solution. Required if providing Tax Schedule
taxschedule	Optional	string	You can assign a default tax schedule for a customer contact. When you create an AR transaction, the tax details from the assigned schedule are used as the default for the AR line entry. The tax details can be overridden through the UI

mailaddress

Name	Required	Type	Description
address1	Optional	string	Address line 1
address2	Optional	string	Address line 2
address3	Optional	string	Address line 3
city	Optional	string	City
state	Optional	string	State/province
zip	Optional	string	Zip/postal code
country	Optional	string	Country
isocountrycode	Optional	string	ISO country code. When ISO country codes are enabled in a company, both country and isocountrycode must be provided.
latitude	Optional	string	Latitude
longitude	Optional	string	Longitude

customfield

Name	Required	Type	Description
customfieldname	Optional	string	Custom field ID
customfieldvalue	Optional	varies	Custom field value. For a multi-pick-list custom field, implode multiple field values with #~#.

contactitem

Name	Required	Type	Description
category	Required	string	Contact category, such as work, home, and so forth.
contactname	Required	string	Contact name of an existing contact

customfield

Name	Required	Type	Description
customfieldname	Optional	string	Custom field ID
customfieldvalue	Optional	varies	Custom field value. For a multi-pick-list custom field, implode multiple field values with #~#.

visibility

visibility_type	Required	string	Restriction type. Use Unrestricted, RootOnly, or Restricted. (Default Unrestricted)
restricted_locs	Optional	locationid[0...n]	Restricted location IDs
restricted_depts	Optional	departmentid[0...n]	Restricted department IDs
Update Customer

History

update

Add a comment to a customer:

<update>
    <CUSTOMER>
        <RECORDNO>12</RECORDNO>
        <NAME>SaaS Company Inc</NAME>
        <DISPLAYCONTACT>
            <PRINTAS>SaaS Company Inc</PRINTAS>
            <COMPANYNAME>SaaS Co</COMPANYNAME>
            <TAXABLE>true</TAXABLE>
            <TAXGROUP>CA</TAXGROUP>
            <TAXSOLUTIONID>US Sales Tax - SYS</TAXSOLUTIONID>
            <TAXSCHEDULE>US Purchase Goods Standard</TAXSCHEDULE>
            <PREFIX>Mr</PREFIX>
            <FIRSTNAME>Bill</FIRSTNAME>
            <LASTNAME>Smith</LASTNAME>
            <INITIAL>G</INITIAL>
            <PHONE1>12</PHONE1>
            <PHONE2>34</PHONE2>
            <CELLPHONE>56</CELLPHONE>
            <PAGER>78</PAGER>
            <FAX>90</FAX>
            <EMAIL1></EMAIL1>
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
        <CUSTTYPE>SaaS</CUSTTYPE>
        <PARENTID>C5678</PARENTID>
        <GLGROUP>Group</GLGROUP>
        <TERRITORYID>NE</TERRITORYID>
        <SUPDOCID>A1234</SUPDOCID>
        <TERMNAME>N30</TERMNAME>
        <OFFSETGLACCOUNTNO>1200</OFFSETGLACCOUNTNO>
        <ARACCOUNT>4000</ARACCOUNT>
        <SHIPPINGMETHOD>USPS</SHIPPINGMETHOD>
        <RESALENO>123</RESALENO>
        <TAXID>12-3456789</TAXID>
        <CREDITLIMIT>1234.56</CREDITLIMIT>
        <ONHOLD>false</ONHOLD>
        <DELIVERY_OPTIONS>Print#~#E-Mail</DELIVERY_OPTIONS>
        <CUSTMESSAGEID>hello</CUSTMESSAGEID>
        <COMMENTS>my comment</COMMENTS>
        <CURRENCY>USD</CURRENCY>
        <ARINVOICEPRINTTEMPLATEID>temp1</ARINVOICEPRINTTEMPLATEID>
        <OEQUOTEPRINTTEMPLATEID>temp2</OEQUOTEPRINTTEMPLATEID>
        <OEORDERPRINTTEMPLATEID>temp3</OEORDERPRINTTEMPLATEID>
        <OELISTPRINTTEMPLATEID>temp4</OELISTPRINTTEMPLATEID>
        <OEINVOICEPRINTTEMPLATEID>temp5</OEINVOICEPRINTTEMPLATEID>
        <OEADJPRINTTEMPLATEID>temp6</OEADJPRINTTEMPLATEID>
        <OEOTHERPRINTTEMPLATEID>temp7</OEOTHERPRINTTEMPLATEID>
        <CONTACTINFO>
            <CONTACTNAME>primary</CONTACTNAME>
        </CONTACTINFO>
        <BILLTO>
            <CONTACTNAME>bill to</CONTACTNAME>
        </BILLTO>
        <SHIPTO>
            <CONTACTNAME>ship to</CONTACTNAME>
        </SHIPTO>
        <OBJECTRESTRICTION>Restricted</OBJECTRESTRICTION>
        <RESTRICTEDLOCATIONS>100#~#200</RESTRICTEDLOCATIONS>
        <RESTRICTEDDEPARTMENTS>D100#~#D200</RESTRICTEDDEPARTMENTS>
        <CUSTOMFIELD1>Hello</CUSTOMFIELD1>
    </CUSTOMER>
</update>

Replace a previous email template selection by providing a different email template name for the given record number. Also add a new email template to the set:

<update>
    <CUSTOMER>
        <CUSTOMERID>C1234</CUSTOMERID>
        ...
        <CUSTOMEREMAILTEMPLATES>
            <customeremailtemplate>
                <RECORDNO>170</RECORDNO>
                <EMAILTEMPLATENAME>ARInvEmailTemplate</EMAILTEMPLATENAME>
            </customeremailtemplate>
            <customeremailtemplate>
                <EMAILTEMPLATENAME>ARStmtEmailTemplate</EMAILTEMPLATENAME>
            </customeremailtemplate>
        </CUSTOMEREMAILTEMPLATES>
    </CUSTOMER>
</update>

Update a customer to delete the existing contact list:

<update>
    <CUSTOMER>
        <RECORDNO>1</RECORDNO>
        <CUSTOMERCONTACTS></CUSTOMERCONTACTS>
    </CUSTOMER>
</update>
Parameters
Name	Required	Type	Description
CUSTOMER	Required	object	Object to update

CUSTOMER

Name	Required	Type	Description
RECORDNO	Optional	integer	Record number of customer to update. Required if not using customer ID.
CUSTOMERID	Optional	string	Customer ID. Required if not using RECORDNO.
NAME	Optional	string	Name
DISPLAYCONTACT	Optional	object	Contact info
STATUS	Optional	string	Status. Use active for Active or inactive for Inactive (Default: active)
ONETIME	Optional	boolean	One time customer. Use false for No, true for Yes. (Default: false)
HIDEDISPLAYCONTACT	Optional	boolean	Exclude from contact list. Use false for No, true for Yes. (Default: false)
CUSTTYPE	Optional	string	Customer type ID
CUSTREPID	Optional	string	Sales rep employee ID
PARENTID	Optional	string	Parent customer ID
GLGROUP	Optional	string	GL group name
TERRITORYID	Optional	string	Territory ID
SUPDOCID	Optional	string	Attachments ID
TERMNAME	Optional	string	Payment term
OFFSETGLACCOUNTNO	Optional	string	Offset AR GL account number
ARACCOUNT	Optional	string	Default AR GL account number
SHIPPINGMETHOD	Optional	string	Shipping method
RESALENO	Optional	string	Resale number
TAXID	Optional	string	Tax ID
CREDITLIMIT	Optional	currency	Credit limit
RETAINAGEPERCENTAGE	Optional	numeric	Default retainage percentage for customers (Construction or Projects subscription).
ONHOLD	Optional	boolean	On hold. Use false for No, true for Yes. (Default: false)
DELIVERY_OPTIONS	Optional	string	Delivery method. Use either Print, E-Mail, or Print#~#E-Mail for both. If using E-Mail, the customer contact must have a valid e-mail address.
CUSTMESSAGEID	Optional	string	Default invoice message
EMAILOPTIN	Optional	boolean	Accept emailed invoices option. Use false for No, true for Yes. Applicable only for companies configured for South Africa (ZA) VAT.
COMMENTS	Optional	string	Comments
CURRENCY	Optional	string	Default currency code
ADVBILLBY	Optional	integer	Bill in advance. Number of months or days before the start date. Use 0 through 9.
ADVBILLBYTYPE	Optional	string	Bill-in-advance time period. Required if using bill in advance. Use days or months.
ARINVOICEPRINTTEMPLATEID	Optional	string	Print option - AR invoice template name
OEQUOTEPRINTTEMPLATEID	Optional	string	Print option - OE quote template name
OEORDERPRINTTEMPLATEID	Optional	string	Print option - OE order template name
OELISTPRINTTEMPLATEID	Optional	string	Print option - OE list template name
OEINVOICEPRINTTEMPLATEID	Optional	string	Print option - OE invoice template name
OEADJPRINTTEMPLATEID	Optional	string	Print option - OE adjustment template name
OEOTHERPRINTTEMPLATEID	Optional	string	Print option - OE other template name
CONTACTINFO	Optional	object	Primary contact
BILLTO	Optional	object	Bill to contact. The system automatically appends a corresponding Bill to Contact to the contact list.
SHIPTO	Optional	object	Ship to contact. The system automatically appends a corresponding Ship to Contact to the contact list.
CONTACT_LIST_INFO	Optional	CONTACT_LIST_INFO[]	Contact list (alternative to CUSTOMERCONTACTS). Multiple individual CONTACT_LIST_INFO elements may be passed. If this parameter is omitted, the original contact list remains intact. If you supply new elements, these are appended to the list. Passing an empty CONTACT_LIST_INFO element deletes the contact list. If this parameter and CUSTOMERCONTACTS are both provided, CUSTOMERCONTACTS is used. If not provided and not already existing, any values supplied for other contacts (Primary, Bill to, or Ship to) are used to create a contact list.
CUSTOMERCONTACTS	Optional	CUSTOMERENTITYCONTACTS[0…n]	Contact list (alternative to CONTACT_LIST_INFO). If this parameter is omitted, the original contact list remains intact. If you supply new elements, these are appended to the list. Passing an empty CUSTOMERCONTACTS element deletes the contact list. If this parameter and CONTACT_LIST_INFO are both provided, CUSTOMERCONTACTS is used. If not provided and not already existing, any values supplied for other contacts (Primary, Bill to, or Ship to) are used to create a contact list.
OBJECTRESTRICTION	Optional	object	Restriction type. Use Unrestricted, RootOnly, or Restricted. (Default Unrestricted)
RESTRICTEDLOCATIONS	Optional	string	Restricted location IDs. Use if OBJECTRESTRICTION is Restricted. Implode multiple IDs with #~#.
RESTRICTEDDEPARTMENTS	Optional	string	Restricted department IDs. Use if OBJECTRESTRICTION is Restricted. Implode multiple IDs with #~#.
CUSTOMEREMAILTEMPLATES	Optional	CUSTOMEREMAILTEMPLATE[1..n]	Custom email templates to override the default email templates associated with transaction definitions. You choose existing custom email templates to use for this customer, optionally specifying the transactions to which they apply.
Custom field name	varies	varies	Custom field names and values as defined for this object.
For a multi-pick-list custom field, implode multiple field values with #~#.

DISPLAYCONTACT

Name	Required	Type	Description
PRINTAS	Optional	string	Print as
COMPANYNAME	Optional	string	Company name
TAXABLE	Optional	boolean	Taxable. Use false for No, true for Yes. (Default: true)
TAXGROUP	Optional	string	Contact tax group name
TAXSCHEDULE	Optional	string	You can assign a default tax schedule for a customer contact. When you create an AR transaction, the tax details from the assigned schedule are used as the default for the AR line entry. The tax details can be overridden through the UI
TAXSOLUTIONID	Optional	string	Tax solution. Required if providing Tax Schedule
PREFIX	Optional	string	Prefix
FIRSTNAME	Optional	string	First name
LASTNAME	Optional	string	Last name
INITIAL	Optional	string	Middle name
PHONE1	Optional	string	Primary phone number
PHONE2	Optional	string	Secondary phone number
CELLPHONE	Optional	string	Cellular phone number
PAGER	Optional	string	Pager number
FAX	Optional	string	Fax number
EMAIL1	Optional	string	Primary email address
EMAIL2	Optional	string	Secondary email address
URL1	Optional	string	Primary URL
URL2	Optional	string	Secondary URL
MAILADDRESS	Optional	object	Mail address

MAILADDRESS

Name	Required	Type	Description
ADDRESS1	Optional	string	Address line 1
ADDRESS2	Optional	string	Address line 2
ADDRESS3	Optional	string	Address line 3
CITY	Optional	string	City
STATE	Optional	string	State/province
ZIP	Optional	string	Zip/postal code
COUNTRY	Optional	string	Country
ISOCOUNTRYCODE	Optional	string	ISO country code. When ISO country codes are enabled in a company, both COUNTRY and ISOCOUNTRYCODE must be provided.

CONTACTINFO

Name	Required	Type	Description
CONTACTNAME	Required	string	Primary contact name

BILLTO

Name	Required	Type	Description
CONTACTNAME	Required	string	Bill to contact name

SHIPTO

Name	Required	Type	Description
CONTACTNAME	Required	string	Ship to contact name

CONTACT_LIST_INFO

Name	Required	Type	Description
CATEGORYNAME	Required	string	Contact category, such as work, home, and so forth.
CONTACT	Optional	object	Category

CUSTOMERENTITYCONTACTS

If the category and contact name you provide for a contact matches one already in the contact list, your entry is skipped.

Name	Required	Type	Description
CATEGORYNAME	Required	string	Contact category, such as work, home, and so forth.
CONTACT	Required	object	Contact

CONTACT

Name	Required	Type	Description
NAME	Required	string	Contact name

CUSTOMEREMAILTEMPLATE

Name	Required	Type	Description
RECORDNO	Optional	numeric	Required if updating an existing customer email template selection (a custom email template and optional corresponding transaction definition previously designated for this customer). You can specify a different email template by name, or you can specify a different transaction definition for the current email template, or both. The record number remains unchanged.
EMAILTEMPLATENAME	Optional	string	Required if not providing a record number. Name of an email template.
DOCPARID	Optional	string	Transaction definition that will use this email template. Applicable only for Order Entry, Purchasing, and Contract email templates.
Update Customer (Legacy)

History

update_customer
<update_customer customerid="C1234">
    <name>Volume Reseller(CC1234)</name>
    <termname>N15</termname>
</update_customer>
Parameters
Name	Required	Type	Description
customerid	Required	string	Customer ID to update
name	Optional	string	Name
parentid	Optional	string	Parent customer ID
termname	Optional	string	Payment term
custrepid	Optional	string	Sales rep employee ID
shippingmethod	Optional	string	Shipping method
custtype	Optional	string	Customer type ID
taxid	Optional	string	Tax ID
creditlimit	Optional	currency	Credit limit
retainagepercentage	Optional	numeric	Default retainage percentage for customers (Construction or Projects subscription).
territoryid	Optional	string	Territory ID
resaleno	Optional	string	Resale number
deliveryoptions	Optional	object	Delivery method
accountlabel	Optional	string	GL account label
glaccountno	Optional	string	Default AR GL account number
glgroup	Optional	string	GL group name
onhold	Optional	boolean	On hold. Use false for No, true for Yes.
comments	Optional	string	Comments
status	Optional	string	Status. Use active for Active or inactive for Inactive.
currency	Optional	string	Default currency code
primary	Optional	object	Primary contact. If blank system will use the corresponding contactinfo.
billto	Optional	object	Bill to contact. If blank system will use the corresponding contactinfo.
shipto	Optional	object	Return to contact. If blank system will use the corresponding contactinfo.
contactinfo	Optional	object	Contact info.
contactlist	Optional	contactitem[0...n]	Contact list. If not provided and not already existing, any values supplied for other contacts (Primary, Bill to, or Ship to) are used to create a contact list.
vsoepricelist	Optional	String	Name of a vendor-specific Order Entry price list
customfields	Optional	varies	Custom fields
visibility	Optional	object	Restrictions
supdocid	Optional	string	Attachments ID
offsetglaccountno	Optional	string	Offset AR GL account number

deliveryoptions

Name	Required	Type	Description
deliveryoption	Required	string	Delivery method. Use either print, email, or both. If using E-Mail, the customer contact must have a valid e-mail address.

primary

Name	Required	Type	Description
contactname	Required	string	Contact name of an existing contact. The system automatically provides a corresponding Primary Contact in the first row of the Contact list, overwriting existing data (if present).

billto

Name	Required	Type	Description
contactname	Required	string	Contact name of an existing contact. The system automatically appends a corresponding Bill to Contact to the contact list.

shipto

Name	Required	Type	Description
contactname	Required	string	Contact name of an existing contact. The system automatically appends a corresponding Ship to Contact to the contact list.

contactinfo

Name	Required	Type	Description
contact	Required	object	New contact to create corresponding with the customer

contact

Name	Required	Type	Description
contactname	Required	string	Contact name
printas	Required	string	Print as
taxable	Optional	boolean	Taxable. Use false for No, true for Yes. (Default: true)
companyname	Optional	string	Company name
taxgroup	Optional	string	Contact tax group name
prefix	Optional	string	Prefix
firstname	Optional	string	First name
lastname	Optional	string	Last name
initial	Optional	string	Middle name
phone1	Optional	string	Primary phone number
phone2	Optional	string	Secondary phone number
cellphone	Optional	string	Cellular phone number
pager	Optional	string	Pager number
fax	Optional	string	Fax number
email1	Optional	string	Primary email address
email2	Optional	string	Secondary email address
url1	Optional	string	Primary URL
url2	Optional	string	Secondary URL
status	Optional	string	Status. Use active for Active or inactive for Inactive (Default: active)
mailaddress	Optional	object	Mail address
taxid	Optional	string	Tax ID
taxsolutionid	Optional	string	Tax solution. Required if providing Tax Schedule
taxschedule	Optional	string	You can assign a default tax schedule for a customer contact. When you create an AR transaction, the tax details from the assigned schedule are used as the default for the AR line entry. The tax details can be overridden through the UI

mailaddress

Name	Required	Type	Description
address1	Optional	string	Address line 1
address2	Optional	string	Address line 2
address3	Optional	string	Address line 3
city	Optional	string	City
state	Optional	string	State/province
zip	Optional	string	Zip/postal code
country	Optional	string	Country
isocountrycode	Optional	string	ISO country code. When ISO country codes are enabled in a company, both country and isocountrycode must be provided.
latitude	Optional	string	Latitude
longitude	Optional	string	Longitude

contactitem

Name	Required	Type	Description
category	Required	string	Contact category, such as work, home, and so forth.
contactname	Required	string	Contact name of an existing contact

customfield

Name	Required	Type	Description
customfieldname	Optional	string	Custom field ID
customfieldvalue	Optional	varies	Custom field value. For a multi-pick-list custom field, implode multiple field values with #~#.

visibility

visibility_type	Required	string	Restriction type. Use Unrestricted, RootOnly, or Restricted. (Default Unrestricted)
restricted_locs	Optional	locationid[0...n]	Restricted location IDs
restricted_depts	Optional	departmentid[0...n]	Restricted department IDs
Delete Customer
delete
<delete>
    <object>CUSTOMER</object>
    <keys>112</keys>
</delete>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMER
keys	Required	string	Comma-separated list of customer RECORDNO to delete
Delete Customer (Legacy)
delete_customer
<delete_customer customerid="C1234"></delete_customer>
Parameters
Name	Required	Type	Description
customerid	Required	string	Customer ID to delete

–

Customer Email Templates
Get Customer Email Template Object Definition
lookup

List all the fields and relationships for the customer email template object:

<lookup>
    <object>CUSTOMEREMAILTEMPLATE</object>
</lookup>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMEREMAILTEMPLATE
Query and List Customer Email Templates
query

List the template name and customer ID for each customer email template:

<query>
    <object>CUSTOMEREMAILTEMPLATE</object>
    <select>
        <field>EMAILTEMPLATENAME</field>
        <field>CUSTOMERID</field>
    </select>
</query>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMEREMAILTEMPLATE
filter	Optional	object	Filter expression to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, VENDOR.CREDITLIMIT on APBILL).
select	Required	sequence	The names of the fields that you want included in the response, and an optional aggregate function such as count or sum. Returning all fields is not supported.
orderby	Optional	object	Provide an order element with a field name and choose an ascending or descending sort order, for example:
<order>
  <field>RECORDNO</field>
  <descending/>
</order>
options	Optional	object	Query options:
Set the caseinsensitive element to true for a case-insensitive query
 <caseinsensitive>true</caseinsensitive>
In a multi-entity company, set the showprivate element to true to query data in private entities:
 <showprivate>true</showprivate>
Specify the returnformat for the response: xml (default), json, or csv
 <returnformat>json</returnformat>

pagesize	Optional	integer	Maximum number of matching objects to return in the response, between 1 and 2000 items (Default: 100)
offset	Optional	integer	Point at which to start indexing into records (Default: 0)
Query and List Customer Email Templates (Legacy)
readByQuery
<readByQuery>
    <object>CUSTOMEREMAILTEMPLATE</object>
    <fields>*</fields>
    <query/>
    <pagesize>100</pagesize>
</readByQuery>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMEREMAILTEMPLATE
fields	Optional	string	Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide * for the value.
query	Required	string	SQL-like query based on fields on the object. The following operators are supported: <, >, >=, <=, =, like, not like, in, not in, IS NOT NULL, IS NULL, AND, OR. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes ('Jane\'s Deli'). Joins are not supported.
pagesize	Optional	integer	Custom page size between 1 and 1000 items (Default: 100)
Get Customer Email Template
read
<read>
    <object>CUSTOMEREMAILTEMPLATE</object>
    <keys>21</keys>
    <fields>*</fields>
</read>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMEREMAILTEMPLATE
keys	Required	string	Comma-separated list of customer email template RECORDNO to get.
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Get Customer Email Template by ID
readByName
<readByName>
    <object>CUSTOMEREMAILTEMPLATE</object>
    <keys>21</keys>
    <fields>*</fields>
</readByName>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMEREMAILTEMPLATE
keys	Required	string	Comma-separated list of customer email template RECORDNO to get.
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Customer Visibility
Get Customer Visibility Object Definition
lookup

List all the fields and relationships for the customer visibility object:

<lookup>
    <object>CUSTOMERVISIBILITY</object>
</lookup>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMERVISIBILITY
Get Customer Visibility
read
<read>
    <object>CUSTOMERVISIBILITY</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
Parameters
Name	Required	Type	Description
object	Required	string	Use CUSTOMERVISIBILITY
keys	Required	string	Comma-separated list of customer visibility RECORDNO to get
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv

 PROVIDE FEEDBACK

Page content licensed under Creative Commons Attribution 4.0. Code samples licensed under Apache v2.0.
© 2025 The Sage Group plc or its affiliates or licensors ("Sage"). All trademarks mentioned are the property of their respective owners. Use of non-Sage trademarks is not an endorsement of any person or product.

