Title: Budgets

URL Source: https://developer.intacct.com/api/general-ledger/budgets/

Markdown Content:
*   [Budgets](https://developer.intacct.com/api/general-ledger/budgets/#budgets)
    *   [Get Budget Object Definition](https://developer.intacct.com/api/general-ledger/budgets/#get-budget-object-definition)
    *   [Query and List Budgets](https://developer.intacct.com/api/general-ledger/budgets/#query-and-list-budgets)
    *   [Query and List Budgets (Legacy Query)](https://developer.intacct.com/api/general-ledger/budgets/#query-and-list-budgets-legacy-query)
    *   [Get Budget](https://developer.intacct.com/api/general-ledger/budgets/#get-budget)
    *   [Get Budget by ID](https://developer.intacct.com/api/general-ledger/budgets/#get-budget-by-id)
    *   [Create Budget](https://developer.intacct.com/api/general-ledger/budgets/#create-budget)
    *   [Update Budget](https://developer.intacct.com/api/general-ledger/budgets/#update-budget)
    *   [Delete Budget](https://developer.intacct.com/api/general-ledger/budgets/#delete-budget)
*   [Budget Details](https://developer.intacct.com/api/general-ledger/budgets/#budget-details)
    *   [Get Budget Detail Object Definition](https://developer.intacct.com/api/general-ledger/budgets/#get-budget-detail-object-definition)
    *   [Query and List Budget Details](https://developer.intacct.com/api/general-ledger/budgets/#query-and-list-budget-details)
    *   [Query and List Budget Details (Legacy Query)](https://developer.intacct.com/api/general-ledger/budgets/#query-and-list-budget-details-legacy-query)
    *   [Get Budget Detail](https://developer.intacct.com/api/general-ledger/budgets/#get-budget-detail)
    *   [Delete Budget Detail](https://developer.intacct.com/api/general-ledger/budgets/#delete-budget-detail)

* * *

A budget is a plan to help estimate revenue and expenses for operations.

Budget amounts are uploaded early in the cycle (month or quarter), and then are used at the end of the cycle to compare against actuals.

You create a budget and its details by creating a GLBUDGETHEADER object with owned GLBUDGETITEMS. You can use update to add more budget details, and you can delete budget details using the [delete](https://developer.intacct.com/api/general-ledger/budgets/#delete-budget-detail) function.

* * *

### Get Budget Object Definition

#### `lookup`

> List all the fields and relationships for the budget object:

```
<lookup>
    <object>GLBUDGETHEADER</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETHEADER` |

* * *

### Query and List Budgets

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and budget ID for each budget:

```
<query>
    <object>GLBUDGETHEADER</object>
    <select>
        <field>RECORDNO</field>
        <field>BUDGETID</field>
    </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETHEADER` |
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

### Query and List Budgets (Legacy Query)

[History](https://developer.intacct.com/api/general-ledger/budgets/#history-list-budgets)

| Release | Changes |
| --- | --- |
| 2019 Release 3 | Added support for GLBUDGETHEADER |

#### `readByQuery`

```
<readByQuery>
    <object>GLBUDGETHEADER</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETHEADER` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Budget

#### `read`

```
<read>
    <object>GLBUDGETHEADER</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETHEADER` |
| keys | Required | string | Comma-separated list of budget `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Get Budget by ID

#### `readByName`

```
<readByName>
    <object>GLBUDGETHEADER</object>
    <keys>2019 Annual Plan</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETHEADER` |
| keys | Required | string | Comma-separated list of budget `BUDGETID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create Budget

#### `create`

```
<create>
    <GLBUDGETHEADER>
        <BUDGETID>2019 Annual Plan</BUDGETID>
        <DESCRIPTION>2019 Annual Plan</DESCRIPTION>
        <DEFAULT_BUDGET>true</DEFAULT_BUDGET>
        <GLBUDGETITEMS>
            <GLBUDGETITEM>
                <ACCT_NO>1000</ACCT_NO>
                <PERIODNAME>Month Ended January 2019</PERIODNAME>
                <DEPT_NO>20</DEPT_NO>
                <LOCATION_NO>30</LOCATION_NO>
                <AMOUNT>20000</AMOUNT>
            </GLBUDGETITEM>
            <GLBUDGETITEM>
                <ACCT_NO>1001</ACCT_NO>
                <PERIODNAME>Month Ended February 2019</PERIODNAME>
                <DEPT_NO>10</DEPT_NO>
                <LOCATION_NO>30</LOCATION_NO>
                <AMOUNT>10000</AMOUNT>
            </GLBUDGETITEM>
        </GLBUDGETITEMS>
    </GLBUDGETHEADER>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLBUDGETHEADER | Required | object | Type of object to create. |

`GLBUDGETHEADER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BUDGETID | Required | string | Budget ID |
| DESCRIPTION | Required | string | Description of the budget. |
| DEFAULT\_BUDGET | Optional | boolean | Use `true` to designate this as the company’s default budget, otherwise use `false` |
| ISCONSOLIDATED | Optional | boolean | Use `true` to make this a consolidated budget, otherwise use `false` |
| CURRENCY | Optional | string | Consolidation currency code. Required if `ISCONSOLIDATED` is set to `true` |
| ISPCNBUDGET | Optional | Boolean | Set to `true` to restrict the budget to be used with project contracts. All budget details will be generated from project contracts. |
| GLBDUGETITEMS | Optional | array of `GLBUDGETITEM[` | Zero or more budget details. |

`GLBUDGETITEM`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ACCT\_NO | Required | string | Account number |
| PERIODNAME | Required | string | Name of a budgetable reporting period |
| LOCATION\_NO | Optional | string | Location number |
| DEPT\_NO | Optional | string | Department number |
| AMOUNT | Required | currency | Amount |

* * *

### Update Budget

Use this function to add new budget details or modify existing budget details. To delete existing budget details, use the [delete](https://developer.intacct.com/api/general-ledger/budgets/#delete-budget-detail) function.

#### `update`

> Add one new budget detail and modify an existing one:

```
<update>
    <GLBUDGETHEADER>
        <RECORDNO>20</RECORDNO>
        <GLBUDGETITEMS>
            <GLBUDGETITEM>
                <PERIODNAME>Month Ended April 2019</PERIODNAME>
                <ACCT_NO>1000</ACCT_NO>
                <DEPT_NO>20</DEPT_NO>
                <LOCATION_NO>10</LOCATION_NO>
                <AMOUNT>16000</AMOUNT>
            </GLBUDGETITEM>
            <GLBUDGETITEM>
                <RECORDNO>3679</RECORDNO>
                <PERIODNAME>Month Ended March 2019</PERIODNAME>
                <ACCT_NO>1000</ACCT_NO>
                <DEPT_NO>20</DEPT_NO>
                <LOCATION_NO>10</LOCATION_NO>
                <AMOUNT>15750</AMOUNT>
            </GLBUDGETITEM>
        </GLBUDGETITEMS>
    </GLBUDGETHEADER>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GLBUDGETHEADER | Required | object | Type of object to update. |

`GLBUDGETHEADER`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Record number of the budget |
| DESCRIPTION | Optional | string | Description of budget |
| DEFAULT\_BUDGET | Optional | boolean | Use `true` to designate this as the company’s default budget, otherwise use `false` |
| ISCONSOLIDATED | Optional | boolean | Use `true` to make this a consolidated budget, otherwise use `false` |
| CURRENCY | Optional | string | Consolidation currency code. Required if `ISCONSOLIDATED` is set to `true` |
| ISPCNBUDGET | Optional | Boolean | Set to `true` to restrict the budget to use with project contracts. This value cannot be changed for budgets that have any GLBUDGETITEMs. |
| GLBDUGETITEMS | Optional | array of `GLBUDGETITEM` | Budget details. |

`GLBUDGETITEM`

You can add new details or modify fields on existing details.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of a budget detail to modify. Omit this parameter to create a new budget detail. |
| ACCT\_NO | Required | string | Account number |
| PERIODNAME | Required | string | Name of a budgetable reporting period |
| LOCATION\_NO | Optional | string | Location number |
| DEPT\_NO | Optional | string | Department number |
| AMOUNT | Required | currency | Amount |

* * *

### Delete Budget

#### `delete`

```
<delete>
    <object>GLBUDGETHEADER</object>
    <keys>1</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETHEADER` |
| keys | Required | string | Comma-separated list of budget `RECORDNO` to delete |

* * *

Budget Details
--------------

### Get Budget Detail Object Definition

#### `lookup`

> List all the fields and relationships for the budget detail object:

```
<lookup>
    <object>GLBUDGETITEM</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETITEM` |

* * *

### Query and List Budget Details

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and budget ID for each budget detail for the `Proj-05-Budget` budget:

```
<query>
    <object>GLBUDGETITEM</object>
    <select>
        <field>RECORDNO</field>
        <field>BUDGETID</field>
    </select>
    <filter>
        <equalto>
            <field>BUDGETID</field>
            <value>Proj-05-Budget</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETITEM` |
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

### Query and List Budget Details (Legacy Query)

#### `readByQuery`

```
<readByQuery>
    <object>GLBUDGETITEM</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETITEM` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get Budget Detail

#### `read`

```
<read>
    <object>GLBUDGETITEM</object>
    <keys>2</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETITEM` |
| keys | Required | string | Comma-separated list of budget detail `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Delete Budget Detail

If deleting a budget detail will result in an empty period, that budget detail will not be deleted. Instead, its value is set to zero (and its record number is retained).

#### `delete`

```
<delete>
    <object>GLBUDGETITEM</object>
    <keys>40</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GLBUDGETITEM` |
| keys | Required | string | Comma-separated list of budget detail `RECORDNO` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

