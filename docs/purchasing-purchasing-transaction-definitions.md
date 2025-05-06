Title: Purchasing Transaction Definitions

URL Source: https://developer.intacct.com/api/purchasing/purchasing-transaction-definitions/

Markdown Content:
Blog
Guides 
API Reference
Tools & Libraries
Support
  API  Purchasing  Purchasing Transaction Definitions
Purchasing Transaction Definitions
Get Purchasing Transaction Definition Object Definition
Query and List Purchasing Transaction Definitions
Query and List Purchasing Transaction Definitions (Legacy)
Get Purchasing Transaction Definition
Create Purchasing Transaction Definition
Update Purchasing Transaction Definition
Delete Purchasing Transaction Definition

A transaction definition contains the accounting rules, workflow settings, security settings, and other characteristics for a transaction.

If your company has enabled advanced workflows, you can add new transaction definitions or edit existing ones.

This page provides some examples that create and update Purchasing transaction definitions that are for demonstration purposes only. Your requirements will be different.

Get Purchasing Transaction Definition Object Definition
lookup

List all the fields and relationships for the Purchasing transaction definition object:

<lookup>
    <object>PODOCUMENTPARAMS</object>
</lookup>
Parameters
Name	Required	Type	Description
object	Required	string	Use PODOCUMENTPARAMS
Query and List Purchasing Transaction Definitions
query

List the template name and template type for each transaction definition:

<query>
    <object>PODOCUMENTPARAMS</object>
    <select>
        <field>DOCID</field>
        <field>DOCCLASS</field>
    </select>
</query>
Parameters
Name	Required	Type	Description
object	Required	string	Use PODOCUMENTPARAMS
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
Query and List Purchasing Transaction Definitions (Legacy)
readByQuery
<readByQuery>
    <object>PODOCUMENTPARAMS</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
Parameters
Name	Required	Type	Description
object	Required	string	Use PODOCUMENTPARAMS
fields	Optional	string	Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide * for the value.
query	Required	string	SQL-like query based on fields on the object. The following operators are supported: <, >, >=, <=, =, like, not like, in, not in, IS NOT NULL, IS NULL, AND, OR. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes ('Jane\'s Deli'). Joins are not supported.
pagesize	Optional	integer	Custom page size between 1 and 1000 items (Default: 100)

query Fields

Name	Required	Type	Description
DOCCLASS	Optional	string	Template type for the transaction. Use QUOTE, ORDER, LIST, INVOICE, ADJ, or OTHER.
CATEGORY	Optional	string	Workflow category. Use Q for Quote, O for Order, S for Shipping, I for Invoice, or R for Return.
IN_OUT	Optional	string	Increases/decreases inventory and billings. Use I for Increase or D for Decrease.
EDITTYPE	Optional	string	Edit policy for the transaction type in the Security Configuration. Use N for No Edit, P for Before Printing, or H for All.
DELTYPE	Optional	string	Delete policy for the transaction type in the Security Configuration. Use N for No Edit, P for Before Printing, or H for All.
CREATETYPE	Optional	string	Create policy for the transaction type in the Security Configuration. Use N for New document or Convert or C for Convert only.
Get Purchasing Transaction Definition
read
<read>
    <object>PODOCUMENTPARAMS</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
Parameters
Name	Required	Type	Description
object	Required	string	Use PODOCUMENTPARAMS
keys	Required	string	Comma-separated list of object RECORDNO to get
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Create Purchasing Transaction Definition

History

create

Creates a transaction definition for vendor bills for office supplies:

<create>
    <PODOCUMENTPARAMS>
        <!-- General Properties -->
        <DOCID>Vendor Bill</DOCID>
        <DESCRIPTION>Vendor bill for office supplies with AP posting</DESCRIPTION>
        <DOCCLASS>Invoice</DOCCLASS>
        <CATEGORY>Invoice</CATEGORY>
        <SEQUENCE>Vendor Bill</SEQUENCE>
        <PRESERVE_SEQNUM>true</PRESERVE_SEQNUM>
        <INHERIT_SOURCE_DOCNO>false</INHERIT_SOURCE_DOCNO>

        <!-- Accounting Properties -->
        <SHOW_TOTALS>false</SHOW_TOTALS>
        <LINELEVELSIMPLETAX>false</LINELEVELSIMPLETAX>
        <SHOWEXPANDEDTOTALS>false</SHOWEXPANDEDTOTALS>
        <ENABLEOVERRIDETAX>false</ENABLEOVERRIDETAX>
        <OVERRIDE_PRICE>true</OVERRIDE_PRICE>
        <UPDATES_GL>A</UPDATES_GL>  <!-- Sets transaction posting for AP -->
        <POSTTOGL>false</POSTTOGL>

        <!-- Posting Configuration for AP -->
        <AR_ACCOUNTS> <!-- AR_ACCOUNT is shared across applications including AP -->
            <AR_ACCOUNT>
                <GLACCOUNT>2000--Accounts Payable</GLACCOUNT>
                <ISOFFSET>true</ISOFFSET>
                <DEBIT_CREDIT>Debit</DEBIT_CREDIT>
            </AR_ACCOUNT>
            <AR_ACCOUNT>
                <ITEM_GLGROUP>Expenses</ITEM_GLGROUP>
                <GLACCOUNT>6215--Office Supplies</GLACCOUNT>
                <ISOFFSET>false</ISOFFSET>
                <DEBIT_CREDIT>Credit</DEBIT_CREDIT>
            </AR_ACCOUNT>
        </AR_ACCOUNTS>

        <!-- Workflow Properties -->
        <RECALLS>
            <RECALL>
                <RECDOCPAR>PO Receiver</RECDOCPAR>
            </RECALL>
        </RECALLS>
        <CONVTYPE>Leave Transaction Open</CONVTYPE>
        <CREDITLIMITCHECK>false</CREDITLIMITCHECK>

        <!-- Printing Properties -->
        <CONTACTTITLE1>Pay to</CONTACTTITLE1>
        <SHOWTITLE1>true</SHOWTITLE1>
        <ALLOWEDITBILLTO>false</ALLOWEDITBILLTO>
        <CONTACTTITLE2>Return to</CONTACTTITLE2>
        <SHOWTITLE2>true</SHOWTITLE2>
        <ALLOWEDITSHIPTO>false</ALLOWEDITSHIPTO>
        <CONTACTTITLE3>Deliver to</CONTACTTITLE3>
        <SHOWTITLE3>false</SHOWTITLE3>
        <ALLOWEDITDELIVERTO>false</ALLOWEDITDELIVERTO>

        <!-- Security Configuration -->
        <EDITTYPE>All</EDITTYPE>
        <DELTYPE>Before Printing</DELTYPE>
        <CREATETYPE>New document or Convert</CREATETYPE>
        <TD_CREATION_RULE>Top level or Entity</TD_CREATION_RULE>
    </PODOCUMENTPARAMS>
</create>

Creates the same type of transaction definition but adds subtotals, reversals, and multi-entity settings:

<create>
    <PODOCUMENTPARAMS>
        <!-- General Properties -->
        <DOCID>Vendor Bill Subtotals</DOCID>
        <DESCRIPTION>Vendor bill with subtotals and numbering for entities</DESCRIPTION>
        <DOCCLASS>Invoice</DOCCLASS>
        <CATEGORY>Invoice</CATEGORY>
        <SEQUENCE>Vendor Bill</SEQUENCE>
        <PRESERVE_SEQNUM>false</PRESERVE_SEQNUM>
        <INHERIT_SOURCE_DOCNO>false</INHERIT_SOURCE_DOCNO>

        <!-- Accounting Properties -->
        <SHOW_TOTALS>true</SHOW_TOTALS>
        <LINELEVELSIMPLETAX>false</LINELEVELSIMPLETAX>
        <SUBTOTALS>
            <SUBTOTAL>
                <DESCRIPTION>Vendor Bill Percent Discount</DESCRIPTION>
                <DISC_CHARGE>Discount</DISC_CHARGE>
                <AMT_PERC>Percent</AMT_PERC>
                <VALUE></VALUE>
                <DEBIT_CREDIT>Debit</DEBIT_CREDIT>
                <GLACCOUNT>4200--Discounts</GLACCOUNT>
                <GLOFFSETACCOUNT></GLOFFSETACCOUNT>
                <APPORTIONED>false</APPORTIONED>
                <ISTAX>false</ISTAX>
            </SUBTOTAL>
        </SUBTOTALS>
        <SHOWEXPANDEDTOTALS>false</SHOWEXPANDEDTOTALS>
        <ENABLEOVERRIDETAX>false</ENABLEOVERRIDETAX>
        <OVERRIDE_PRICE>true</OVERRIDE_PRICE>
        <OVERRIDE_EXCH_RATE_TYPE>true</OVERRIDE_EXCH_RATE_TYPE>
        <DISPLAY_BASECURRENCY>false</DISPLAY_BASECURRENCY>
        <UPDATES_GL>A</UPDATES_GL>  <!-- Sets transaction posting for AP -->
        <POSTTOGL>false</POSTTOGL>

        <!-- Posting Configuration for AP -->
        <AR_ACCOUNTS> <!-- AR_ACCOUNT is shared across applications including AP -->
            <AR_ACCOUNT>
                <GLACCOUNT>2100--Accounts Payable</GLACCOUNT>
                <ISOFFSET>true</ISOFFSET>
                <DEBIT_CREDIT>Debit</DEBIT_CREDIT>
            </AR_ACCOUNT>
            <AR_ACCOUNT>
                <ITEM_GLGROUP>Office Supplies</ITEM_GLGROUP>
                <GLACCOUNT>6215--Office Supplies</GLACCOUNT>
                <ISOFFSET>false</ISOFFSET>
                <DEBIT_CREDIT>Credit</DEBIT_CREDIT>
            </AR_ACCOUNT>
        </AR_ACCOUNTS>

        <!-- Workflow Properties -->
        <RECALLS>
            <RECALL>
                <RECDOCPAR>PO Receiver</RECDOCPAR>
            </RECALL>
        </RECALLS>
        <CONVTYPE>Leave Transaction Open</CONVTYPE>
        <CREDITLIMITCHECK>false</CREDITLIMITCHECK>

        <!-- Printing Properties -->
        <CONTACTTITLE1>Pay to</CONTACTTITLE1>
        <SHOWTITLE1>true</SHOWTITLE1>
        <ALLOWEDITBILLTO>false</ALLOWEDITBILLTO>
        <CONTACTTITLE2>Return to</CONTACTTITLE2>
        <SHOWTITLE2>true</SHOWTITLE2>
        <ALLOWEDITSHIPTO>false</ALLOWEDITSHIPTO>
        <CONTACTTITLE3>Deliver to</CONTACTTITLE3>
        <SHOWTITLE3>false</SHOWTITLE3>
        <ALLOWEDITDELIVERTO>false</ALLOWEDITDELIVERTO>

        <!-- Security Configuration -->
        <EDITTYPE>All</EDITTYPE>
        <DELTYPE>Before Printing</DELTYPE>
        <CREATETYPE>New document or Convert</CREATETYPE>
        <TD_CREATION_RULE>Top level or Entity</TD_CREATION_RULE>

        <!-- Entity Settings -->
        <ENTITY_PROPS>
            <ENTITY_PROP>
                <ENTITY_NAME>200</ENTITY_NAME>
                <SEQUENCE>VendBill Canadian</SEQUENCE>
                <PRESERVE_SEQNUM>true</PRESERVE_SEQNUM>
                <INHERIT_SOURCE_DOCNO>false</INHERIT_SOURCE_DOCNO>
                <ENABLEOVERRIDETAX>false</ENABLEOVERRIDETAX>
                <LINELEVELSIMPLETAX>false</LINELEVELSIMPLETAX>
            </ENTITY_PROP>
            <ENTITY_PROP>
                <ENTITY_NAME>100</ENTITY_NAME>
                <SEQUENCE>VendBill USA</SEQUENCE>
                <PRESERVE_SEQNUM>true</PRESERVE_SEQNUM>
                <INHERIT_SOURCE_DOCNO>false</INHERIT_SOURCE_DOCNO>
                <ENABLEOVERRIDETAX>false</ENABLEOVERRIDETAX>
                <LINELEVELSIMPLETAX>false</LINELEVELSIMPLETAX>
            </ENTITY_PROP>
        </ENTITY_PROPS>
    </PODOCUMENTPARAMS>
</create>
Parameters
Name	Required	Type	Description
PODOCUMENTPARAMS	Required	object	Type of object to create.

PODOCUMENTPARAMS

General Properties
Name	Required	Type	Description
DOCID	Required	string	Template name for the transaction definition. Use 30 characters or fewer. Once you save a transaction definition, you can’t change the template name.
DESCRIPTION	Optional	string	Meaningful description for the transaction definition. Use 100 characters or fewer.
DOCCLASS	Optional	string	Template type for the transaction. The type determines whether certain fields appear on the transaction (for example, Expiration Date vs. Ship Date). Use Quote, Order, List, Invoice, Adjustment, or Other. (Default: Quote)
CATEGORY	Optional	string	Workflow category. Use Quote, Order, Shipping, Invoice, or Return. (Default: Quote)
REPORTINGCATEGORY	Optional	string	Standard reporting categories for Construction projects. Use one of the following or a null value: Bids and Quotes, Purchase Orders, Purchase Order Change Orders, Purchase Receivers, Purchase Order Invoices, Purchase Returns, Purchase Credits, Purchase Debits, Purchase Clearing Receivers, Subcontract Bids, Subcontracts, Subcontract Change Orders, Subcontract Invoices, Internal Supply Requisitions, Purchase Requisitions, Blanket POs or Vendor Contracts, Grant Requests, or Grant Awards.
STATUS	Optional	string	Status for the transaction definition. Use Active or Inactive. (Default: Active)
ENABLEDOCCHANGE	Optional	string	Enable change management for transactions. Use Enable Change for source transactions that can accept change orders, use Change Order for transactions that are themselves change orders, or No Change for transactions that do not use change management. (Default value: No Change)
SEQUENCE	Optional	string	Numbering sequence for the transaction. If not provided, transactions must be numbered manually. Can be overridden in the Entity Settings.
PRESERVE_SEQNUM	Optional	boolean	Preserve sequence numbers so that numbers are not skipped. Use true to preserve sequences, false otherwise. Can be overridden in the Entity Settings. (Default: false)
INHERIT_SOURCE_DOCNO	Optional	boolean	Inherit the source document number from the transaction from which this transaction is converted. Use true to inherit the numbering, false otherwise. Can be overridden in the Entity Settings. (Default: false)
PRIMARYDOC	Optional	boolean	Enables the primary document feature within a workflow. Use true to enable, false otherwise. When set to true, all documents created using the purchasing transaction definition are marked as primary documents, and all documents that result from conversions or change orders from a primary document have links back to the primary document. Available in companies with a Construction subscription. When you set PRIMARYDOC to true, you can’t disable it. (Default: false)
Inventory Control Properties
Name	Required	Type	Description
TOTALS	Optional	TOTAL[1…n]	Inventory Control totals. Your company must subscribe to Inventory Control.
WARNONLOWQTY	Optional	boolean	Warn user if item ONHAND quantity falls below zero. Use true to warn, false otherwise. (Default: true)
IN_OUT	Optional	string	Increases/decreases inventory and billings. Use Increase or Decrease. (Default: Increase)
WAREHOUSESELMETHOD	Optional	string	Warehouse selection method. Use Sort by ID, Sort by Name, Warehouse with Available Inventory, or Use the default warehouse. (Default: Sort by ID)
DEFAULT_WAREHOUSE	Optional	string	Default warehouse. Only applicable if warehouse selection method is set to Use the default warehouse. A user’s Default warehouse setting overrides this selection.

TOTAL

Name	Required	Type	Description
TOTALID	Required	string	Inventory total ID. Use DAMAGED, ONHAND, ONHOLD, ONORDER, REQUISITIONED, SCRAP OR SPOILAGE or a custom inventory total.
Q_QV	Required	string	Maintain inventory. Use Quantity, Value, or Quantity &amp; Value.
SIGN	Required	string	Add/Subtract. Use Add or Subtract.
Accounting Properties
Name	Required	Type	Description
SHOW_TOTALS	Optional	boolean	Enable subtotals. Use true to enable subtotals, false otherwise. (Default: false)
LINELEVELSIMPLETAX	Optional	boolean	Enable line level Simple Tax. Use true to enable line level Simple Tax, false otherwise. (Default: false)
SUBTOTALS	Optional	SUBTOTAL[1..n]	Transaction subtotals. Only applicable when subtotals are enabled (via SHOW_TOTALS).
ENABLEOVERRIDETAX	Optional	string	Line item tax. Specifies whether the user can override whether an item is taxable. Only applicable when subtotals are enabled (via SHOW_TOTALS).
SHOWEXPANDEDTOTALS	Optional	string	Show expanded tax details in the transaction user interface and in the printed output. Only applicable when subtotals are enabled (via SHOW_TOTALS) for companies that use Avalara tax or Intacct Advanced Tax.(Default: false)
OVERRIDE_PRICE	Optional	boolean	Override suggested price. Specifies whether the user can override the price proposed by the system. Use true if you want to allow this, false otherwise. (Default: true)
OVERRIDE_EXCH_RATE_TYPE	Optional	boolean	Exchange rate and exchange rate type. Specifies whether the user can edit the Exchange rate and/or Exchange rate type fields on the transaction. Use true if you want to allow this, false otherwise. (Default: true)
EXCHRATETYPES	Optional	string	Exchange rate type for custom exchange rate. Only applicable for multi-currency companies.
DISPLAY_BASECURRENCY	Optional	boolean	Display base currency as well as transaction currency for multi-currency. Use true to display both, false otherwise. Only applicable for multi-currency companies. (Default: false)
UPDATES_GL	Optional	string	Transaction posting. Use A for Accounts Payable, G for General Ledger, or N for Don’t Post. If you specify Accounts Payable or General Ledger, you must supply the Transaction posting account mapping (via AR_ACCOUNTS) in the Posting Configuration.
AR_ACCOUNTS	Optional	AR_ACCOUNT[2]	Transaction posting account mapping for either Accounts Payable or General Ledger transaction posting. There must be one credit and one debit account. Note: AR_ACCOUNT is shared across applications, which is why there isn’t an AP_ACCOUNT mapping parameter as you might expect.
POSTTOGL	Optional	boolean	Enable reversal posting, which can be any additional posting, not just for reversals. Use true to enable, false otherwise. If set to true, you must supply the Reversal GL entry account mapping in the Posting Configuration. (Default: false)
DISABLEVAT	Optional	boolean	For a VAT enabled company, disables tax capture for the general ledger. (Default: false) (AU, GB, ZA only)
INVGL_ACCOUNTS	Optional	INVGL_ACCOUNT[2]	Reversal GL entry account mapping in the Posting Configuration. There must be one credit and one debit account.
ALLOW_ALLOCATIONS	Optional	boolean	Enable transaction allocations. Set to true to allow line-level transaction allocations for non-inventory items.
ENABLE_RETAINAGE	Optional	boolean	Enable retainage for transactions. Set to true to allow retainages (Construction or Projects subscription).

SUBTOTAL

Name	Required	Type	Description
DESCRIPTION	Optional	string	Description for the transaction subtotal
DISC_CHARGE	Optional	string	Subtotal type. Use Discount or Charge.
BASELINE	Optional	integer	Applied to line
AMT_PERC	Optional	string	Value type. Use Amount or Percent.
VALUE	Optional	integer	Value
DEBIT_CREDIT	Optional	string	Debit/Credit. Use Debit or Credit.
GLACCOUNT	Optional	string	GL Account
GLOFFSETACCOUNT	Optional	string	GL Offset Account
APPORTIONED	Optional	boolean	Apportioned. Use true for apportioned, false otherwise. (Default: false)
ISTAX	Optional	boolean	Is Tax. Use true to flag the subtotal as a tax, false otherwise. If your organization uses Simple Tax, Advanced Tax, or Avalara Tax, set this option to true. (Default: false)
Posting Configuration

AR_ACCOUNT

Details for AP account mapping or Transaction posting GL account mapping. Accounts Payable or General Ledger must be specified as the transaction posting option (via UPDATES_GL) for this to apply. There must be one credit and one debit account, and there must be one offset account.

Note: AR_ACCOUNT is shared across applications, which is why there isn’t an AP_ACCOUNT mapping parameter as you might expect.

Name	Required	Type	Description
ITEM_GLGROUP	Optional	string	Item GL Group
WAREHOUSE	Optional	string	Warehouse
ENT_GLGROUP	Optional	string	Vendor GL Group.
DEBIT_CREDIT	Optional	string	Debit/Credit. Use Debit or Credit.
GLACCOUNT	Optional	string	GL Account
ISOFFSET	Optional	boolean	Is Offset? Use true to indicate this is an offset account, false otherwise. (Default: false)

INVGL_ACCOUNT

Details for Reversal GL entry account mapping. Reversal posting must be enabled (viaPOSTTOGL) for this to apply. There must be one credit and one debit account, and there must be one offset account.

Name	Required	Type	Description
ITEM_GLGROUP	Optional	string	Item GL Group
WAREHOUSE	Optional	string	Warehouse
DEBIT_CREDIT	Optional	string	Debit/Credit. Use Debit or Credit.
GLACCOUNT	Optional	string	GL Account
ISOFFSET	Optional	boolean	Is Offset? Use true to indicate this is an offset account, false otherwise. (Default: false)
Workflow Properties
Name	Required	Type	Description
RECALLS	Optional	RECALL[1..n]	Transaction definitions from which this transaction can be converted. If this transaction definition is the first step in your workflow, omit this parameter.
CONVTYPE	Optional	string	Partial conversion handling. Use Close Transaction, Leave Transaction Open, or Close Original and Create Back Order. (Default: Close Transaction)
PRICELISTID	Optional	string	Initial price list. If you are using layered price lists, this indicates the first price list the system will evaluate when determining a suggested transaction price.
SPECIAL_PRICELISTID	Optional	string	Special price list. If you are using layered price lists, this indicates a special price list (for example, a discounted price list or seasonal price list).
UPDATES_PRICELISTID	Optional	string	Price list to update. If you are using layered price lists, this indicates a special price list such as a seasonal one (typically not used).
CREDITLIMITCHECK	Optional	boolean	Enforce credit limit. Specifies whether to enforce customer credit limit restrictions in transactions created from this template. Use true for needing a credit check, false otherwise. (Default: false)
TERM_NAME	Optional	string	Default AP term. If selected, the system auto-populates the Expiration date for quotes and the Date due for invoices based on the selected term.

RECALL

RECDOCPAR	Optional	string	Transaction definition from which this transaction can be converted from as part of a workflow.
Printing Properties
Name	Required	Type	Description
XSLTEMPLATE	Optional	string	Custom document template for printing.
FIXED_MESG	Optional	string	Optional default text. Only applicable if a custom document template for printing is not used. Use 4000 or fewer characters.
CONTACTTITLE1	Optional	string	Contact Title label change for Pay to label. Use 20 or fewer characters.
SHOWTTITLE1	Optional	boolean	Show on Print for Pay to label for CONTACTTITLE1. Use true to show the title, false otherwise.
ALLOWEDITBILLTO	Optional	boolean	Allow Editing for Pay to label for CONTACTTITLE1. Use true to allow the user to select a contact other than the default, false otherwise.
CONTACTTITLE2	Optional	string	Contact Title label change for Return to label. Use 20 or fewer characters.
SHOWTTITLE2	Optional	boolean	Enable Show on Print for the Return to label for CONTACTTITLE2. Use true to show the title, false otherwise.
ALLOWEDITSHIPTO	Optional	boolean	Enable Allow Editing for the Return to label for CONTACTTITLE2. Use true to allow the user to select a contact other than the default, false otherwise.
CONTACTTITLE3	Optional	string	Contact Title label change for Deliver to label. Use 20 or fewer characters.
SHOWTTITLE3	Optional	boolean	Enable Show on Print for Deliver to label for CONTACTTITLE3. Use true to show the title, false otherwise.
ALLOWEDITDELIVERTO	Optional	boolean	Enable Allow Editing for the Deliver to label for CONTACTTITLE3. Use true to allow the user to select a contact other than the default, false otherwise.
Additional Information Properties

Details related to Construction projects, useful for working with subcontractors.

Name	Required	Type	Description
ENABLEADDINFOSCOPE	Optional	boolean	Enables Scope parameters. This includes SCOPE, INCLUSIONS, EXCLUSIONS, and TERMS.
ENABLEADDINFOSCHEDULE	Optional	boolean	Enables Schedule parameters for Construction projects
ENABLEADDINFOINTERNALREF	Optional	boolean	Enables Internal Reference parameters. This includes all parameters prefixed with INTERNAL.
ENABLEADDINFOEXTERNALREF	Optional	boolean	Enables External Reference parameters. This includes all parameters prefixed with EXTERNAL.
ENABLEADDINFOBOND	Optional	boolean	Enables Bond parameters
Security Configuration
Name	Required	Type	Description
EDITTYPE	Optional	string	Edit policy for the transaction type in the Security Configuration. Use No Edit to specify that the user cannot edit this transaction after it is created, Before Printing to specify that the user can edit this transaction until it has been printed to PDF, or All to specify that the user can edit this transaction as allowed by the transaction’s condition. (Default: No Edit)
DELTYPE	Optional	string	Delete policy for the transaction type in the Security Configuration. Use No Edit to specify that the user cannot delete this transaction after it is created, Before Printing to specify that the user can delete this transaction until it has been printed to PDF, or All to specify that the user can delete this transaction as allowed by the transaction’s condition. (Default: No Edit)
CREATETYPE	Optional	string	Create policy for the transaction type in the Security Configuration. Use New document or Convert to specify that the user can create this transaction as a standalone transaction or by converting the previous transaction in the workflow, or use Convert only to specify that the user can create this transaction only by converting the previous transaction in the workflow. (Default: New document or Convert)
TD_CREATION_RULE	Optional	string	Create-transactions-in policy for the transaction type in the Security Configuration. Use Top level or Entity, Top level only, or Entity only. (Default: Top level or Entity)
Entity Settings
Name	Required	Type	Description
ENTITY_PROPS	Optional	ENTITY_PROP[1..n]	Entity settings. Available only if the Create-transactions-in policy in the Security Configuration is set to Top level or entity or Entity only. If you omit this array, all entities use the defaults set in the General tab.

ENTITY_PROP

These settings are only applicable when a transaction is created from the entity, not the top level.

Name	Required	Type	Description
ENTITY_NAME	Optional	string	Entity ID
SEQUENCE	Optional	string	Numbering sequence for the transaction within this entity. If not provided, transactions need to be numbered manually.
PRESERVE_SEQNUM	Optional	boolean	Preserve sequence numbers so that numbers are not skipped. Use true to preserve sequences, false otherwise. (Default: false)
INHERIT_SOURCE_DOCNO	Optional	boolean	Inherit the source document number from the transaction from which this transaction is converted. Use true to inherit the numbering, false otherwise. (Default: false)
XSLTEMPLATE	Optional	string	Custom document template for printing.
ENABLEOVERRIDETAX	Optional	string	Line item tax
Update Purchasing Transaction Definition

History

If your transaction definition has entity properties, you need to include the entity ID (via ENTITY_NAME in theENTITY_PROPS) for each such entity for every update call regardless of other parameters you are providing. See Entity Settings below for more information.

update

Updates the description of a transaction definition:

<update>
    <PODOCUMENTPARAMS>
        <RECORDNO>105</RECORDNO>
        <DESCRIPTION>New description</DESCRIPTION>
    </PODOCUMENTPARAMS>
</update>

Adds subtotals to the transaction definition:

<update>
    <PODOCUMENTPARAMS>
        <RECORDNO>108</RECORDNO>
        <SHOW_TOTALS>true</SHOW_TOTALS>
        <SUBTOTALS>
            <SUBTOTAL>
                <DESCRIPTION>Vendor Bill Percent Discount</DESCRIPTION>
                <DISC_CHARGE>Discount</DISC_CHARGE>
                <AMT_PERC>Percent</AMT_PERC>
                <VALUE></VALUE>
                <DEBIT_CREDIT>Debit</DEBIT_CREDIT>
                <GLACCOUNT>4200--Discounts</GLACCOUNT>
                <GLOFFSETACCOUNT></GLOFFSETACCOUNT>
                <APPORTIONED>false</APPORTIONED>
                <ISTAX>false</ISTAX>
            </SUBTOTAL>
        </SUBTOTALS>
    </PODOCUMENTPARAMS>
</update>
Parameters
Name	Required	Type	Description
PODOCUMENTPARAMS	Optional	object	Object to update

PODOCUMENTPARAMS

Name	Required	Type	Description
RECORDNO	Required	integer	Transaction definition RECORDNO to update

General Properties

Name	Required	Type	Description
DESCRIPTION	Optional	string	Meaningful description for the transaction definition. Use 100 characters or fewer.
DOCCLASS	Optional	string	Template type for the transaction. The type determines whether certain fields appear on the transaction (for example, Expiration Date vs. Ship Date). Use Quote, Order, List, Invoice, Adjustment, or Other. (Default: Quote)
CATEGORY	Optional	string	Workflow category. Use Quote, Order, Shipping, Invoice, or Return. (Default: Quote)
REPORTINGCATEGORY	Optional	string	Standard reporting categories for Construction projects. Use one of the following or a null value: Bids and Quotes, Purchase Orders, Purchase Order Change Orders, Purchase Receivers, Purchase Order Invoices, Purchase Returns, Purchase Credits, Purchase Debits, Purchase Clearing Receivers, Subcontract Bids, Subcontracts, Subcontract Change Orders, Subcontract Invoices, Internal Supply Requisitions, Purchase Requisitions, Blanket POs or Vendor Contracts, Grant Requests, or Grant Awards.
STATUS	Optional	string	Status for the transaction definition. Use Active or Inactive. (Default: Active)
ENABLEDOCCHANGE	Optional	string	Enable change management for transactions. Use Enable Change for source transactions that can accept change orders, use Change Order for transactions that are themselves change orders, or No Change for transactions that do not use change management. You can modify an existing transaction definition to be a source. You can modify an existing transaction definition without any transactions to be a change order. You can modify an existing source transaction definition to prevent change orders if there aren’t already existing change orders. Finally, you can modify an existing change transaction definition without any transactions to remove change management.
SEQUENCE	Optional	string	Numbering sequence for the transaction. If not provided, transactions must be numbered manually.
PRESERVE_SEQNUM	Optional	boolean	Preserve sequence numbers so that numbers are not skipped. Use true to preserve sequences, false otherwise. (Default: false)
INHERIT_SOURCE_DOCNO	Optional	boolean	Inherit the source document number from the transaction from which this transaction is converted. Use true to inherit the numbering, false otherwise. (Default: false)
PRIMARYDOC	Optional	boolean	Enables the primary document feature within a workflow. Use true to enable, false otherwise. When set to true, all documents created using the purchasing transaction definition are marked as primary documents, and all documents that result from conversions or change orders from a primary document have links back to the primary document. Available in companies with a Construction subscription. When you set PRIMARYDOC to true, you can’t disable it. (Default: false)
Inventory Control Properties
Name	Required	Type	Description
TOTALS	Optional	TOTAL[1…n]	Inventory Control totals. Your company must subscribe to Inventory Control.
WARNONLOWQTY	Optional	boolean	Warn user if item ONHAND quantity falls below zero. Use true to warn, false otherwise. (Default: true)
IN_OUT	Optional	string	Increases/decreases inventory and billings. Use Increase or Decrease. (Default: Increase)
WAREHOUSESELMETHOD	Optional	string	Warehouse selection method. Use Sort by ID, Sort by Name, Warehouse with Available Inventory, or Use the default warehouse. (Default: Sort by ID)
DEFAULT_WAREHOUSE	Optional	string	Default warehouse. Only applicable if warehouse selection method is set to Use the default warehouse. A user’s Default warehouse setting overrides this selection.

TOTAL

To add inventory totals using the API, provide a complete set with both the existing ones and the new ones. To delete a an inventory total, use the UI.

Name	Required	Type	Description
TOTALID	Optional	string	Inventory total ID. Use DAMAGED, ONHAND, ONHOLD, ONORDER, REQUISITIONED, SCRAP OR SPOILAGE or a custom inventory total.
Q_QV	Optional	string	Maintain inventory. Use Quantity, Value, or Quantity &amp; Value.
SIGN	Optional	string	Add/Subtract. Use Add or Subtract.
Accounting Properties
Name	Required	Type	Description
SHOW_TOTALS	Optional	boolean	Enable subtotals. Use true to enable subtotals, false otherwise. (Default: false)
LINELEVELSIMPLETAX	Optional	boolean	Enable line level Simple Tax. Use true to enable line level Simple Tax, false otherwise. (Default: false)
SUBTOTALS	Optional	SUBTOTAL[1..n]	Transaction subtotals. Only applicable when subtotals are enabled (via SHOW_TOTALS).
ENABLEOVERRIDETAX	Optional	string	Line item tax. Specifies whether the user can override whether an item is taxable. Only applicable when subtotals are enabled (via SHOW_TOTALS).
SHOWEXPANDEDTOTALS	Optional	string	Show expanded tax details in the transaction user interface and in the printed output. Only applicable when subtotals are enabled (via SHOW_TOTALS) for companies that use Avalara tax or Intacct Advanced Tax.(Default: false)
OVERRIDE_PRICE	Optional	boolean	Override suggested price. Specifies whether the user can override the price proposed by the system. Use true if you want to allow this, false otherwise. (Default: true)
OVERRIDE_EXCH_RATE_TYPE	Optional	boolean	Exchange rate and exchange rate type. Specifies whether the user can edit the Exchange rate and/or Exchange rate type fields on the transaction. Use true if you want to allow this, false otherwise. (Default: true)
EXCHRATETYPES	Optional	string	Exchange rate type for custom exchange rate. Only applicable for multi-currency companies.
DISPLAY_BASECURRENCY	Optional	boolean	Display base currency as well as transaction currency for multi-currency. Use true to display both, false otherwise. Only applicable for multi-currency companies. (Default: false)
UPDATES_GL	Optional	string	Transaction posting. Use A for Accounts Payable, G for General Ledger, or N for Don’t Post. If you specify Accounts Payable or General Ledger, you must supply the Transaction posting account mapping (via AR_ACCOUNTS) in the Posting Configuration.
AR_ACCOUNTS	Optional	AR_ACCOUNT[2]	Transaction posting account mapping for either Accounts Payable or General Ledger transaction posting. There must be one credit and one debit account. Note: AR_ACCOUNT is shared across applications, which is why there isn’t an AP_ACCOUNT mapping parameter as you might expect.
POSTTOGL	Optional	boolean	Enable reversal posting, which can be any additional posting, not just for reversals. Use true to enable, false otherwise. If set to true, you must supply the Reversal GL entry account mapping in the Posting Configuration. (Default: false)
DISABLEVAT	Optional	boolean	For a VAT enabled company, disables tax capture for the general ledger. (Default: false) (AU, GB, ZA only)
INVGL_ACCOUNTS	Optional	INVGL_ACCOUNT[2]	Reversal GL entry account mapping in the Posting Configuration. There must be one credit and one debit account.
ALLOW_ALLOCATIONS	Optional	boolean	Enable transaction allocations. Set to true to allow line-level transaction allocations for non-inventory items.
ENABLE_RETAINAGE	Optional	boolean	Enable retainage for transactions for Construction projects. Set to true to allow retainages. (Construction or Projects subscription).

SUBTOTAL

You can overwrite existing subtotals. If you want to add new subtotals, provide a complete set with both the existing ones and the new ones. To delete subtotals, use the UI.

Name	Required	Type	Description
DESCRIPTION	Optional	string	Description for the transaction subtotal
DISC_CHARGE	Optional	string	Subtotal type. Use Discount or Charge.
BASELINE	Optional	integer	Applied to line
AMT_PERC	Optional	string	Value type. Use Amount or Percent.
VALUE	Optional	integer	Value
DEBIT_CREDIT	Optional	string	Debit/Credit. Use Debit or Credit.
GLACCOUNT	Optional	string	GL Account
GLOFFSETACCOUNT	Optional	string	GL Offset Account
APPORTIONED	Optional	boolean	Apportioned. Use true for apportioned, false otherwise. (Default: false)
ISTAX	Optional	boolean	Is Tax. Use true to flag the subtotal as a tax, false otherwise. If your organization uses Simple Tax, Advanced Tax, or Avalara Tax, set this option to true. (Default: false)
Posting Configuration

AR_ACCOUNT

Details for AP account mapping or Transaction posting GL account mapping. Accounts Payable or General Ledger must be specified as the transaction posting option (via UPDATES_GL) for this to apply. There must be one credit and one debit account, and there must be one offset account.

Note: AR_ACCOUNT is shared across applications, which is why there isn’t an AP_ACCOUNT mapping parameter as you might expect.

You can overwrite existing mappings. If you want to add new mappings, provide a complete set with both the existing ones and the new ones. To delete mappings, use the UI.

Name	Required	Type	Description
ITEM_GLGROUP	Optional	string	Item GL Group
WAREHOUSE	Optional	string	Warehouse
ENT_GLGROUP	Optional	string	Vendor GL Group.
DEBIT_CREDIT	Optional	string	Debit/Credit. Use Debit or Credit.
GLACCOUNT	Optional	string	GL Account
ISOFFSET	Optional	boolean	Is Offset? Use true to indicate this is an offset account, false otherwise. (Default: false)

INVGL_ACCOUNT

Details for Reversal GL entry account mapping. Reversal posting must be enabled (viaPOSTTOGL) for this to apply. There must be one credit and one debit account, and there must be one offset account.

You can overwrite existing mappings. If you want to add new mappings, provide a complete set with both the existing ones and the new ones. To delete mappings, use the UI.

Name	Required	Type	Description
ITEM_GLGROUP	Optional	string	Item GL Group
WAREHOUSE	Optional	string	Warehouse
DEBIT_CREDIT	Optional	string	Debit/Credit. Use Debit or Credit.
GLACCOUNT	Optional	string	GL Account
ISOFFSET	Optional	boolean	Is Offset? Use true to indicate this is an offset account, false otherwise. (Default: false)
Workflow Properties
Name	Required	Type	Description
RECALLS	Optional	RECALL[1..n]	Transaction definitions from which this transaction can be converted. If this transaction definition is the first step in your workflow, omit this parameter.
CONVTYPE	Optional	string	Partial conversion handling. Use Close Transaction, Leave Transaction Open, or Close Original and Create Back Order. (Default: Close Transaction)
PRICELISTID	Optional	string	Initial price list. If you are using layered price lists, this indicates the first price list the system will evaluate when determining a suggested transaction price.
SPECIAL_PRICELISTID	Optional	string	Special price list. If you are using layered price lists, this indicates a special price list (for example, a discounted price list or seasonal price list).
UPDATES_PRICELISTID	Optional	string	Price list to update. If you are using layered price lists, this indicates a special price list such as a seasonal one (typically not used).
CREDITLIMITCHECK	Optional	boolean	Enforce credit limit. Specifies whether to enforce customer credit limit restrictions in transactions created from this template. Use true for needing a credit check, false otherwise. (Default: false)
TERM_NAME	Optional	string	Default AP term. If selected, the system auto-populates the Expiration date for quotes and the Date due for invoices based on the selected term.

RECALL

You can overwrite existing definitions. If you want to add new definitions, provide a complete set with both the existing ones and the new ones. To delete definitions, use the UI.

RECDOCPAR	Optional	string	Transaction definition from which this transaction can be converted from as part of a workflow.
Printing Properties
Name	Required	Type	Description
XSLTEMPLATE	Optional	string	Custom document template for printing.
FIXED_MESG	Optional	string	Optional default text. Only applicable if a custom document template for printing is not used. Use 4000 or fewer characters.
CONTACTTITLE1	Optional	string	Contact Title label change for Pay to label. Use 20 or fewer characters.
SHOWTTITLE1	Optional	boolean	Show on Print for Pay to label for CONTACTTITLE1. Use true to show the title, false otherwise.
ALLOWEDITBILLTO	Optional	boolean	Allow Editing for Pay to label for CONTACTTITLE1. Use true to allow the user to select a contact other than the default, false otherwise.
CONTACTTITLE2	Optional	string	Contact Title label change for Return to label. Use 20 or fewer characters.
SHOWTTITLE2	Optional	boolean	Enable Show on Print for the Return to label for CONTACTTITLE2. Use true to show the title, false otherwise.
ALLOWEDITSHIPTO	Optional	boolean	Enable Allow Editing for the Return to label for CONTACTTITLE2. Use true to allow the user to select a contact other than the default, false otherwise.
CONTACTTITLE3	Optional	string	Contact Title label change for Deliver to label. Use 20 or fewer characters.
SHOWTTITLE3	Optional	boolean	Enable Show on Print for Deliver to label for CONTACTTITLE3. Use true to show the title, false otherwise.
ALLOWEDITDELIVERTO	Optional	boolean	Enable Allow Editing for the Deliver to label for CONTACTTITLE3. Use true to allow the user to select a contact other than the default, false otherwise.
Additional Information Properties

Details related to Construction projects, useful for working with subcontractors.

Name	Required	Type	Description
ENABLEADDINFOSCOPE	Optional	boolean	Enables Scope parameters. This includes SCOPE, INCLUSIONS, EXCLUSIONS, and TERMS
ENABLEADDINFOSCHEDULE	Optional	boolean	Enables Schedule parameters. This includes SCHEDULESTARTDATE, ACTUALSTARTDATE, SCHEDULEDCOMPLETIONDATE, REVISEDCOMPLETIONDATE, SUBSTANTIALCOMPLETIONDATE, ACTUALCOMPLETIONDATE, NOTICETOPROCEED, RESPONSEDUE, EXECUTEDON, and SCHEDULEDIMPACT.
ENABLEADDINFOINTERNALREF	Optional	boolean	Enables Internal Reference parameters. This includes all parameters prefixed with INTERNAL
ENABLEADDINFOEXTERNALREF	Optional	boolean	Enables External Reference parameters. This includes all parameters prefixed with EXTERNAL
ENABLEADDINFOBOND	Optional	boolean	Enables Bond parameters. This includes PERFORMANCEBONDREQUIRED, PERFORMANCEBONDRECEIVED, PERFORMANCEBONDAMOUNT, PERFORMANCESURETYCOMPANYKEY, PERFORMANCESURETYCOMPANY, PAYMENTBONDREQUIRED, PAYMENTBONDRECEIVED, PAYMENTBONDAMOUNT, PAYMENTSURETYCOMPANYKEY, and PAYMENTSURETYCOMPANY.
Security Configuration
Name	Required	Type	Description
EDITTYPE	Optional	string	Edit policy for the transaction type in the Security Configuration. Use No Edit to specify that the user cannot edit this transaction after it is created, Before Printing to specify that the user can edit this transaction until it has been printed to PDF, or All to specify that the user can edit this transaction as allowed by the transaction’s condition. (Default: No Edit)
DELTYPE	Optional	string	Delete policy for the transaction type in the Security Configuration. Use No Edit to specify that the user cannot delete this transaction after it is created, Before Printing to specify that the user can delete this transaction until it has been printed to PDF, or All to specify that the user can delete this transaction as allowed by the transaction’s condition. (Default: No Edit)
CREATETYPE	Optional	string	Create policy for the transaction type in the Security Configuration. Use New document or Convert to specify that the user can create this transaction as a standalone transaction or by converting the previous transaction in the workflow, or use Convert only to specify that the user can create this transaction only by converting the previous transaction in the workflow. (Default: New document or Convert)
TD_CREATION_RULE	Optional	string	Create-transactions-in policy for the transaction type in the Security Configuration. Use Top level or Entity, Top level only, or Entity only. (Default: Top level or Entity)
Entity Settings
Name	Required	Type	Description
ENTITY_PROPS	Optional	ENTITY_PROP[1..n]	Entity settings. Available only if the Create-transactions-in policy in the Security Configuration is set to Top level or entity or Entity only. If you omit this array, all entities use the defaults set in the General tab.

ENTITY_PROP

These settings are only applicable when a transaction is created from the entity, not the top level.

If your transaction definition has entity properties, you need to include the entity ID (via ENTITY_NAME) for each entity for every update call regardless of other parameters you are providing. This includes unrelated parameters such as the description or the status. Providing only the entity ID inside the ENTITY_PROP array means that any previously specified entity settings will be retained. You can also provide only those parameters that you want modified along with the entity ID.

Name	Required	Type	Description
ENTITY_NAME	Optional	string	Entity ID
SEQUENCE	Optional	string	Numbering sequence for the transaction within this entity. If not provided, transactions need to be numbered manually.
PRESERVE_SEQNUM	Optional	boolean	Preserve sequence numbers so that numbers are not skipped. Use true to preserve sequences, false otherwise. (Default: false)
INHERIT_SOURCE_DOCNO	Optional	boolean	Inherit the source document number from the transaction from which this transaction is converted. Use true to inherit the numbering, false otherwise. (Default: false)
XSLTEMPLATE	Optional	string	Custom document template for printing.
ENABLEOVERRIDETAX	Optional	string	Line item tax
Delete Purchasing Transaction Definition
delete
<delete>
    <object>PODOCUMENTPARAMS</object>
    <keys>106</keys>
</delete>
Parameters
Name	Required	Type	Description
object	Required	string	Use PODOCUMENTPARAMS
keys	Required	string	Comma-separated list of purchasing Transaction definition RECORDNO to delete

 PROVIDE FEEDBACK

Page content licensed under Creative Commons Attribution 4.0. Code samples licensed under Apache v2.0.
© 2025 The Sage Group plc or its affiliates or licensors ("Sage"). All trademarks mentioned are the property of their respective owners. Use of non-Sage trademarks is not an endorsement of any person or product.

