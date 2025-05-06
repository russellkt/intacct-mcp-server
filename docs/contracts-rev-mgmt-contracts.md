Title: Contracts

URL Source: https://developer.intacct.com/api/contracts-rev-mgmt/contracts/

Markdown Content:
*   [Get Contract Object Definition](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#get-contract-object-definition)
*   [Query and List Contracts](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#query-and-list-contracts)
*   [Query and List Contracts (Legacy)](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#query-and-list-contracts-legacy)
*   [Get a Contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#get-a-contract)
*   [Get a Contract by ID](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#get-a-contract-by-id)
*   [Create Contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#create-contract)
*   [Update Contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#update-contract)
*   [Post Contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#post-contract)
*   [Renew Contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#renew-contract)
*   [Clear All MEA Allocations](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#clear-all-mea-allocations)
*   [Clear Individual MEA Allocations](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#clear-individual-mea-allocations)
*   [Delete Contract](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#delete-contract)

* * *

Contract is a dimension that can be defined by the company and set on transactions to expand report functionality and insight.

* * *

Get Contract Object Definition
------------------------------

#### `lookup`

> List all the fields and relationships for the contract object:

```
<lookup>
    <object>CONTRACT</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |

* * *

Query and List Contracts
------------------------

#### `query`

> List the record number and description for each contract:

```
<query>
    <object>CONTRACT</object>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
    </select>
</query>
```

> List the Evergreen template in use for each Evergreen contract:

```
<query>
    <object>CONTRACT</object>
    <filter>
        <equalto>
            <field>TERMTYPE</field>
            <value>Evergreen</value>
        </equalto>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>CONTRACTID</field>
        <field>EVERGREENMACRO</field>
    </select>
</query>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |
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

Query and List Contracts (Legacy)
---------------------------------

#### `readByQuery`

```
<readByQuery>
    <object>CONTRACT</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATE | Optional | string | Contract state.
*   `I` - In progress
*   `R` - Renewed
*   `C` - Canceled
*   `N` - Not Renewed

 |
| BILLINGFREQUENCY | Optional | string | Billing frequency.

*   `M` - Monthly
*   `Q` -- Quarterly
*   `A` - Annually

 |
| RENEWTERMPERIOD | Optional | string | Renewal term period.

*   `Y` - Years
*   `M` - Months
*   `D` - Days

 |

* * *

Get a Contract
--------------

#### `read`

```
<read>
    <object>CONTRACT</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |
| keys | Required | string | Comma-separated list of contract `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get a Contract by ID
--------------------

#### `readByName`

```
<readByName>
    <object>CONTRACT</object>
    <keys>C1000</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |
| keys | Required | string | Comma-separated list of contract `CONTRACTID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Contract
---------------

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#history-create-contract)

| Release | Changes |
| --- | --- |
| 2024 Release 4 | Added APPLICATION and ADDITIONALCONTACTNAME |
| 2022 Release 2 | Added TERMTYPE and EVERGREENMACRO |
| 2021 Release 1 | BILLINGFREQUENCY is now optional |
| 2020 Release 1 | Added STATE |
| 2019 Release 2 | Added CONTRACTTYPE, Added value of Annually for BILLINGFREQUENCY |
| 2018 Release 2 | Added RENEWALADVBILLBY and RENEWALADVBILLBYTYPE |
| 2018 Release 1 | Added ADVBILLBY and ADVBILLBYTYPE |

#### `create`

```
<create>
    <CONTRACT>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <CUSTOMERID>C-103</CUSTOMERID>
        <NAME>North central contract</NAME>
        <BEGINDATE>04/01/2017</BEGINDATE>
        <ENDDATE>12/31/2017</ENDDATE>
        <BILLINGFREQUENCY>Monthly</BILLINGFREQUENCY>
        <TERMNAME>Net 30</TERMNAME>
        <LOCATIONID>US</LOCATIONID>
        <CURRENCY>USD</CURRENCY>
        <EXCHRATETYPE>Intacct Daily Rate</EXCHRATETYPE>
    </CONTRACT>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACT | Required | object | Object type to create |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Optional | string | Unique ID for the contract. Required if company does not use document sequencing, or you can provide a value to use instead of the document sequence value. |
| CUSTOMERID | Required | string | Customer ID |
| NAME | Required | string | Contract name |
| STATE | Optional | string | State in which to create the contract.
*   `In progress` (default)
*   `Draft` - The contract that will not yet post to the general ledger.

Use the [post](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#post-contract) function to move a contract from `Draft` to `In progress`. |
| CONTRACTTYPE | Optional | string | [Contract type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/) |
| BILLTOCONTACTNAME | Optional | string | Bill to contact name. Leave blank to use customer’s default. |
| DESCRIPTION | Optional | string | Description |
| SHIPTOCONTACTNAME | Optional | string | Ship to contact name. Leave blank to use customer’s default. |
| BEGINDATE | Required | string | Start date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy`. Required when the term type is Termed. |
| BILLINGFREQUENCY | Optional | string | Billing frequency.

*   `Monthly`
*   `Quarterly`
*   `Annually`

 |
| TERMNAME | Required | string | Payment term |
| TERMTYPE | Required | string | Indicates the term type for the contract.

*   `Termed` - a traditional payment term such as Net 30 (default)
*   `Evergreen` - perpetual contract

 |
| APPLICATION | Required | string | Indicates whether the contract is a full contract (`C`) or a dimension-only contract (`O`). The contract dimension is used to categorize Order Entry transactions without a subscription to the Contracts application. Default is full contract (`C`). |
| ADDITIONALCONTACTNAME | Optional | string | Name of an additional contact. |
| EVERGREENMACRO | Optional | string | Perpetual (Evergreen) template. Required for an `Evergreen` term type. |
| PRCLIST | Optional | string | Billing price list |
| MEAPRCLIST | Optional | string | Fair value price list |
| ADVBILLBY | Optional | integer | Bill in advance. Number of months or days before the start date. Overrides bill-in-advance settings on the customer. |
| ADVBILLBYTYPE | Optional | string | Bill-in-advance time period. Required if using bill in advance.

*   `days`
*   `months`

 |
| RENEWALADVBILLBY | Optional | integer | Bill in advance for renewals. Number of months or days before the start date. |
| RENEWALADVBILLBYTYPE | Optional | string | Bill-in-advance time period for renewals. Required if using bill in advance for renewals.

*   `days`
*   `months`

 |
| SUPDOCID | Optional | string | Attachments ID |
| LOCATIONID | Required | string | Location ID |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CLASSID | Optional | string | Class ID |
| CURRENCY | Optional | string | Transaction currency. Required if company is configured for multi-currency. |
| EXCHRATETYPE | Optional | string | Exchange rate type. Required if company is configured for multi-currency (Leave blank to use `Intacct Daily Rate`) |
| RENEWAL | Optional | boolean | Renewal.

*   `false` - No (default)
*   `true` - Yes

Applicable only for termed contracts. |
| RENEWALMACRO | Optional | string | Renewal template. Only used if `RENEWAL` is `true`. |
| RENEWTERMLENGTH | Optional | integer | Term length. Only used if `RENEWAL` is `true`. |
| RENEWTERMPERIOD | Optional | string | Period. Only used if `RENEWAL` is `true`.

*   `Years`
*   `Months` (default)
*   `Days`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Contract
---------------

[History](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#history-update-contract)

| Release | Changes |
| --- | --- |
| 2022 Release 2 | Added TERMTYPE and EVERGREENMACRO |
| 2019 Release 2 | Added CONTRACTTYPE, Added value of Annually for BILLINGFREQUENCY |
| 2018 Release 2 | Added RENEWALADVBILLBY and RENEWALADVBILLBYTYPE |
| 2018 Release 1 | Added ADVBILLBY and ADVBILLBYTYPE |

#### `update`

```
<update>
    <CONTRACT>
        <CONTRACTID>CTRC-003</CONTRACTID>
        <NAME>North central contract for services</NAME>
        <DEPARTMENTID>300</DEPARTMENTID>
    </CONTRACT>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACT | Create | object | Object type to update. |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of contract. Required if not using `CONTRACTID`. |
| CONTRACTID | Optional | string | Contract ID to update. Required if not using `RECORDNO`. |
| CUSTOMERID | Optional | string | Customer ID |
| NAME | Optional | string | Contract name |
| CONTRACTTYPE | Optional | string | [Contract type](https://developer.intacct.com/api/contracts-rev-mgmt/contract-types/) |
| BILLTOCONTACTNAME | Optional | string | Bill to contact name. Leave blank to use customer’s default. |
| DESCRIPTION | Optional | string | Description |
| SHIPTOCONTACTNAME | Optional | string | Ship to contact name. Leave blank to use customer’s default. |
| BEGINDATE | Required | string | Start date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy`. Required when the term type is Termed. |
| BILLINGFREQUENCY | Optional | string | Billing frequency.
*   `Monthly`
*   `Quarterly`
*   `Annually`

 |
| TERMNAME | Required | string | Payment term |
| TERMTYPE | Optional | string | Indicates the term type for the contract.

*   `Termed` - a traditional payment term such as Net 30 (default)
*   `Evergreen` - perpetual contract

 |
| APPLICATION | Required | string | Indicates whether the contract is a full contract (`C`) or a dimension-only contract (`O`). The contract dimension is used to categorize Order Entry transactions without a subscription to the Contracts application. Default is full contract (`C`). |
| ADDITIONALCONTACTNAME | Optional | string | Name of an additional contact. |
| EVERGREENMACRO | Optional | string | Perpetual (Evergreen) template. Required for an `Evergreen` term type. |
| PRCLIST | Optional | string | Billing price list |
| MEAPRCLIST | Optional | string | Fair value price list |
| ADVBILLBY | Optional | integer | Bill in advance. Number of months or days before the start date. Overrides bill-in-advance settings on the customer. |
| ADVBILLBYTYPE | Optional | string | Bill-in-advance time period. Required if using bill in advance.

*   `days`
*   `months`

 |
| RENEWALADVBILLBY | Optional | integer | Bill in advance for renewals. Number of months or days before the start date. |
| RENEWALADVBILLBYTYPE | Optional | string | Bill-in-advance time period for renewals. Required if using bill in advance for renewals.

*   `days`
*   `months`

 |
| SUPDOCID | Optional | string | Attachments ID |
| LOCATIONID | Required | string | Location ID |
| DEPARTMENTID | Optional | string | Department ID |
| PROJECTID | Optional | string | Project ID |
| VENDORID | Optional | string | Vendor ID |
| EMPLOYEEID | Optional | string | Employee ID |
| CLASSID | Optional | string | Class ID |
| CURRENCY | Optional | string | Transaction currency. Required if company is configured for multi-currency. |
| EXCHRATETYPE | Optional | string | Exchange rate type. Required if company is configured for multi-currency (Leave blank to use `Intacct Daily Rate`) |
| RENEWAL | Optional | boolean | Renewal.

*   `false` - No (default)
*   `true` - Yes

Applicable only for termed contracts. |
| RENEWALMACRO | Optional | string | Renewal template. Only used if `RENEWAL` is `true`. |
| RENEWTERMLENGTH | Optional | integer | Term length. Only used if `RENEWAL` is `true`. |
| RENEWTERMPERIOD | Optional | string | Period. Only used if `RENEWAL` is `true`.

*   `Years`
*   `Months` (default)
*   `Days`

 |
| _Custom field name_ | varies | varies | Custom field names and values as defined for this object.  
For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Post Contract
-------------

You can post a contract that is in `Draft` state so that it is fully validated and posted to the GL. The state of a posted contract is changed from `Draft` to `In progress`.

If your draft contract is missing required parameter values, check the error messages from the `post` response and use the [update](https://developer.intacct.com/api/contracts-rev-mgmt/contracts/#update-contract) function to correct any issues before trying to post again.

#### `post`

```
<post>
    <CONTRACT>
        <RECORDNO>127</RECORDNO>
        <GLPOSTINGDATE>01/01/2020</GLPOSTINGDATE>
        <POSTMEMO>Contract has been finalized</POSTMEMO>
    </CONTRACT>
</post>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | object | Use `CONTRACT` |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number of the contract to post |
| GLPOSTDATE | Required | string | GL posting date in format `mm/dd/yyyy` |
| POSTMEMO | Optional | string | Memo about the post |

* * *

Renew Contract
--------------

Forces the renewal of a contract that failed to renew at the scheduled time. This can be useful if you uploaded multiple contracts as part of an integration and want to avoid manually renewing them in the Sage Intacct UI. (A contract must have )

#### `renew`

```
<renew>
    <CONTRACT>
        <CONTRACTID>CTRC-003</CONTRACTID>
    </CONTRACT>
</renew>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACT | Required | object | Object type to renew. |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Required | string | ID of the contract to renew. The contract’s state must be `In progress`, and there must be at least one contract line. |

* * *

Clear All MEA Allocations
-------------------------

You can clear MEA allocations to reset the applicable revenue schedules to the amounts that existed prior to the allocations. Clearing MEA allocations unposts previously posted revenue, so the applicable reporting periods must be open.

#### `clearallmea`

```
<clearallmea>
    <CONTRACT>
        <CONTRACTID>CTRC-003</CONTRACTID>
    </CONTRACT>
</clearallmea>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Required | string | Contract ID for which to clear all MEA allocations. |

* * *

Clear Individual MEA Allocations
--------------------------------

You can clear individual MEA allocations one at a time, starting with the current one and working back in time.

#### `clearlastactivemea`

```
<clearlastactivemea>
    <CONTRACT>
        <CONTRACTID>CTRC-003</CONTRACTID>
    </CONTRACT>
</clearlastactivemea>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |

`CONTRACT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTRACTID | Required | string | Contract ID for which to clear the current MEA allocation. |

* * *

Delete Contract
---------------

#### `delete`

```
<delete>
    <object>CONTRACT</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `CONTRACT` |
| keys | Required | string | Comma-separated list of contract `RECORDNO` to delete. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

