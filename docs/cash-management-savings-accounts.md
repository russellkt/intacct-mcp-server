Title: Savings Accounts

URL Source: https://developer.intacct.com/api/cash-management/savings-accounts/

Markdown Content:
Blog
Guides 
API Reference
Tools & Libraries
Support
  API  Cash Management  Savings Accounts
Savings Accounts
Get Savings Account Object Definition
Query and List Savings Accounts
Query and List Savings Accounts (Legacy)
Get Savings Account
Get Savings Account by ID
Create Savings Account (Legacy)
Update Savings Account (Legacy)
Delete Savings Account (Legacy)
Reconcile Savings Account

Provides the relevant information for a savings account, such as the account ID, account number, associated GL account, and so forth.

Get Savings Account Object Definition
lookup

List all the fields and relationships for the savings account object:

<lookup>
    <object>SAVINGSACCOUNT</object>
</lookup>
Parameters
Name	Required	Type	Description
object	Required	string	Use SAVINGSACCOUNT
Query and List Savings Accounts
query

List the record number and account ID for each savings account:

<query>
    <object>SAVINGSACCOUNT</object>
    <select>
        <field>RECORDNO</field>
        <field>BANKACCOUNTID</field>
    </select>
</query>
Parameters
Name	Required	Type	Description
object	Required	string	Use SAVINGSACCOUNT
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
Query and List Savings Accounts (Legacy)
readByQuery
<readByQuery>
    <object>SAVINGSACCOUNT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
Parameters
Name	Required	Type	Description
object	Required	string	Use SAVINGSACCOUNT
fields	Optional	string	Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide * for the value.
query	Required	string	SQL-like query based on fields on the object. The following operators are supported: <, >, >=, <=, =, like, not like, in, not in, IS NOT NULL, IS NULL, AND, OR. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes ('Jane\'s Deli'). Joins are not supported.
pagesize	Optional	integer	Custom page size between 1 and 1000 items (Default: 100)
Get Savings Account
read
<read>
    <object>SAVINGSACCOUNT</object>
    <keys>40</keys>
    <fields>*</fields>
</read>
Parameters
Name	Required	Type	Description
object	Required	string	Use SAVINGSACCOUNT
keys	Required	string	Comma-separated list of object RECORDNO to get
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Get Savings Account by ID
readByName
<readByName>
    <object>SAVINGSACCOUNT</object>
    <keys>SBB</keys>
    <fields>*</fields>
</readByName>
Parameters
Name	Required	Type	Description
object	Required	string	Use SAVINGSACCOUNT
keys	Required	string	Comma-separated list of account BANKACCOUNTID to get
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Create Savings Account (Legacy)
create_savingsaccount
<create_savingsaccount>
    <bankaccountid>SBB</bankaccountid>
    <bankaccountno>100-768</bankaccountno>
    <bankname>Savings Bank of Braunville</bankname>
    <currency>USD</currency>
</create_savingsaccount>
Parameters
Name	Required	Type	Description
bankaccountid	Required	string	Bank account ID
bankaccountno	Optional	string	Bank account number
Optional	string	LOCATIONID of an active location. Required if company is multi-entity enabled.	 
bankname	Required	string	Bank name
routingno	Optional	string	Routing number
branchid	Optional	string	Branch ID
phone	Optional	string	Bank phone number
currency	Optional	string	Currency code if multi-currency is enabled.
mailaddress	Optional	object	Mail address
status	Optional	string	Status. Use active for Active or inactive for Inactive. (Default: active)
disableiet	Optional	boolean	Disable inter-entity transfers. Use true to disable transfers, false to enable. (Default: false)
financialdata	Optional	object	Default financial settings
glaccountno	Optional	string	GL account number
servicechargeglaccount	Optional	string	GL account for service charges. Do not provide if using servicechargeaccountlabel.
servicechargeaccountlabel	Optional	string	GL account label for service charges. Do not provide if using servicechargeglaccount.
interestearnedglaccount	Optional	string	GL account for earned interest. Do not provide if using interestearnedaccountlabel.
interestearnedaccountlabel	Optional	string	GL account label for earned interest. Do not provide if using interestearnedglaccount.
departmentid	Optional	string	Department ID
visibility	Optional	object	Restrictions

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

financialdata

Name	Required	Type	Description
reconmode	Optional	string	Reconciliation mode. Use Manual, Automatch or AutomatchReview. (Default is Manual)
apjournal	Optional	string	Default Accounts Payable journal
arjournal	Optional	string	Default Accounts Receivable journal

visibility

visibility_type	Required	string	Restriction type. Use Unrestricted, RootOnly, or Restricted.
restricted_locs	Optional	locationid[0...n]	Restricted location IDs
restricted_depts	Optional	departmentid[0...n]	Restricted department IDs
Update Savings Account (Legacy)
update_savingsaccount
<update_savingsaccount bankaccountid="SBB">
    <phone>1(408)123-1234</phone>
</update_savingsaccount>
Parameters
Name	Required	Type	Description
bankaccountid	Required	string	Bank account ID to update
bankaccountno	Optional	string	Bank account number
Optional	string	LOCATIONID of an active location. Required if company is multi-entity enabled.	 
bankname	Optional	string	Bank name
routingno	Optional	string	Routing number
branchid	Optional	string	Branch ID
phone	Optional	string	Bank phone number
currency	Optional	string	Currency code if multi-currency is enabled.
mailaddress	Optional	object	Mail address
status	Optional	string	Status. Use active for Active or inactive for Inactive. (Default: active)
disableiet	Optional	boolean	Disable inter-entity transfers. Use true to disable transfers, false to enable. (Default: false)
financialdata	Optional	object	Default journal settings
glaccountno	Optional	string	GL account number
servicechargeglaccount	Optional	string	GL account for service charges. Do not provide if using servicechargeaccountlabel.
servicechargeaccountlabel	Optional	string	GL account label for service charges. Do not provide if using servicechargeglaccount.
interestearnedglaccount	Optional	string	GL account for earned interest. Do not provide if using interestearnedaccountlabel.
interestearnedaccountlabel	Optional	string	GL account label for earned interest. Do not provide if using interestearnedglaccount.
departmentid	Optional	string	Department ID
visibility	Optional	object	Restrictions

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

financialdata

Name	Required	Type	Description
reconmode	Optional	string	Reconciliation mode. Use Manual, Automatch or AutomatchReview. (Default is Manual)
apjournal	Optional	string	Default Accounts Payable journal
arjournal	Optional	string	Default Accounts Receivable journal

visibility

visibility_type	Required	string	Restriction type. Use Unrestricted, RootOnly, or Restricted.
restricted_locs	Optional	locationid[0...n]	Restricted location IDs
restricted_depts	Optional	departmentid[0...n]	Restricted department IDs
Delete Savings Account (Legacy)
delete_savingsaccount
<delete_savingsaccount bankaccountid="SBB"></delete_savingsaccount>
Parameters
Name	Required	Type	Description
key	Required	string	Savings bank account ID to delete
Reconcile Savings Account
reconcile_bank
<reconcile_bank>
    <bankaccountid>SBB</bankaccountid>
    <cutoffdate>
        <year>2013</year>
        <month>06</month>
        <day>30</day>
    </cutoffdate>
    <statementendingdate>
        <year>2013</year>
        <month>07</month>
        <day>31</day>
    </statementendingdate>
    <reconmode>AutomatchReview</reconmode>
    <statementendingbalance>1000</statementendingbalance>
    <banktxns>
        <banktxn>
            <postingdate>
                <year>2013</year>
                <month>07</month>
                <day>15</day>
            </postingdate>
            <txntype></txntype>
            <doctype></doctype>
            <document>1234</document>
            <payee>Payee</payee>
            <amount>10.99</amount>
            <description>description</description>
        </banktxn>
    </banktxns>
</reconcile_bank>
Parameters
Name	Required	Type	Description
bankaccountid	Required	string	Account BANKACCOUNTID to reconcile
cutoffdate	Optional	object	Beginning balance cut off date
statementendingdate	Required	object	Statement ending date
reconmode	Required	string	Reconciliation mode. Use Automatch or AutomatchReview. Default depends on mode set on checking account. If Automatch, then the entire reconciliation must clear otherwise you will get an error. Recommended to use Automatch with review. When user reviewing in UI, they must check the “Use previous uploaded file” to see this.
statementendingbalance	Required	currency	Statement ending balance
banktxns	Required	banktxn[1...n]	Bank statement transactions to reconcile with

cutoffdate

Name	Required	Type	Description
year	Required	string	Year yyyy
month	Required	string	Month mm
day	Required	string	Day dd

banktxn

Name	Required	Type	Description
postingdate	Required	object	Posting date
txntype	Required	string	Transaction type. Use withdrawal or deposit. If blank, the system will determine this based on the Amount being positive or negative.
doctype	Required	string	Document type. Use check, card, ach, or leave blank.
document	Required	string	Document number, like the check number or electronic transaction ID.
payee	Required	string(80)	Name of payee
amount	Required	currency	Amount. Must be non-zero.
description	Optional	string(80)	Memo

postingdate

Name	Required	Type	Description
year	Required	string	Year yyyy
month	Required	string	Month mm
day	Required	string	Day dd

 PROVIDE FEEDBACK

Page content licensed under Creative Commons Attribution 4.0. Code samples licensed under Apache v2.0.
© 2025 The Sage Group plc or its affiliates or licensors ("Sage"). All trademarks mentioned are the property of their respective owners. Use of non-Sage trademarks is not an endorsement of any person or product.

