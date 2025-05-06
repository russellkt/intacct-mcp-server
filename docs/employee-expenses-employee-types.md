Title: Employee Types

URL Source: https://developer.intacct.com/api/employee-expenses/employee-types/

Markdown Content:
*   [Get Employee Type Object Definition](https://developer.intacct.com/api/employee-expenses/employee-types/#get-employee-type-object-definition)
*   [Query and List Employee Types](https://developer.intacct.com/api/employee-expenses/employee-types/#query-and-list-employee-types)
*   [Get Employee Type](https://developer.intacct.com/api/employee-expenses/employee-types/#get-employee-type)
*   [Get Employee Type by ID](https://developer.intacct.com/api/employee-expenses/employee-types/#get-employee-type-by-id)

* * *

An employee type is a user-defined or default type for an employee, usually related to payroll requirements.

Examples include full time, part time, intern, and so forth.

* * *

Get Employee Type Object Definition
-----------------------------------

#### `lookup`

> List all the fields and relationships for the employee type object:

```
<lookup>
    <object>EMPLOYEETYPE</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEETYPE` |

* * *

Query and List Employee Types
-----------------------------

#### `readByQuery`

> List employee types:

```
<readByQuery>
    <object>EMPLOYEETYPE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

> List employee types with dividend plans:

```
<readByQuery>
    <object>EMPLOYEETYPE</object>
    <fields>*</fields>
    <query>FORM1099TYPE = 'DIV'</query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEETYPE` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099TYPE | Optional | string | Form 1099 types. Use:  
• `DIV` for dividend Income (Form 1099-DIV)  
• `INT` for interest income (Form 1099-INT)  
• `MISC` for miscellaneous income (Form 1099-MISC)  
• `R` for distributions from pensions, annuities …(Form 1099-R)  
• `S` for proceeds from real estate transactions (Form 1099-S)  
• `PATR` for taxable distributions received (Form 1099-PATR)  
• `G` for certain government payments (Form 1099-G)  
• `W-2G` for certain gambling winnings (Form W-2G) |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form 1099-DIV box values. Use:  
• `1A` for 1a - Total Ordinary dividends  
• `1B` for 1b - Qualified dividends  
• `2A` for 2a - Total capital gain distr  
•`2B` for 2b - Unrecap. sec. 1250 gain  
• `2C` for 2c - Section 1202 gain  
• `2D` for 2d - Collectibles (28%) gain  
• `3` for 3 - Nontaxable distributions  
• `4` for 4 - Federal income tax withheld  
• `5` for 5 - Investment expenses  
• `6` for 6 - Foreign tax paid  
• `8` for 8 - Cash liquidation distr  
• `9` for 9 - Noncash liquidation distr  
• `10` for 10 - Exempt-interest dividends  
• `11` for 11 - Specified private activity bond interest dividends  
• `14` for 14 - State tax withheld |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form 1099-INV box values. Use:  
• `1` for 1 - Interest income  
• `2` for 2 - Early withdrawal penalty  
• `3` for 3 - Interest on U.S. Savings Bonds and Treasury obligations  
• `4` for 4 - Federal income tax withheld  
• `5` for 5 - Investment expenses  
• `6` for 6 - Foreign tax paid  
• `8` for 8 - Tax-exempt interest  
• `9` for 9 - Specified private activity bond interest  
• `10` for 10 - Market Discount  
• `11` for 11 - Bond premium  
• `15` for 15 - State tax withheld |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form 1099-MISC box values. Use:  
• `1` for 1 - Rents  
• `2` for 2 - Royalties  
• `3` for 3 - Other income  
• `4` for 4 - Federal income tax withheld  
• `5` for 5 - Fishing boat proceeds  
• `6` for 6 - Medical and health care payments  
• `7` for 7 - Nonemployee compensation  
• `8` for 8 - Substitute payments in lieu of dividends or interest  
• `10` for 10 - Crop insurance proceeds  
• `13` for 13 - Excess golden parachute payments  
• `14` for 14 - Gross proceeds paid to an attorney  
• `15A` for 15a - Section 409A deferrals  
• `15B` for 15b - Section 409A income  
• `16` for 16 - State tax withheld  
• `18` for 18 - State income |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form 1099-R box values. Use:  
• `1` for 1 - Gross distribution  
• `2A` for 2a - Taxable amount  
• `3` for 3 - Capital gain (included in box 2a)  
• `4` for 4 - Federal income tax withheld  
• `5` for 5 - Employee contributions or insurance premiums  
• `6` for 6 - Net unrealized appreciation in employer’s securities  
• `8` for 8 - Other  
• `9B` for 9b - Total employee contributions  
• `10` for 10 - Amount allocable to IRR within 5 years  
• `12` for 12 - State tax withheld  
• `14` for 14 - State distribution  
• `15` for 15 - Local tax withheld  
• `17` for17 - Local distribution |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form 1099-S box values. Use:  
• `2` for 2 - Gross proceeds  
• `5` for 5 - Buyer’s part of real estate tax |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form 1099-PATR box values. Use:  
• `1` for 1 - Patronage dividends  
• `2` for 2 - NonPatronage dividends  
• `3` for 3 - Per-unit retain allocations  
• `4` for 4 - Federal income tax withheld  
• `5` for 5 - Redemptions of nonqualified notices and retain allocations  
• `6` for 6 - Domestic production activities deduction  
• `7` for 7 - Investment credit  
• `8` for 8 - Work opportunity credit  
• `9` for 9 - Patron’s AMT adjustments  
• `10` for 10 - Other credits and deductions |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form 1099-G box values. Use:  
• `1` for 1- Unemployment compensation  
• `2` for 2 - State or local income tax refunds, credits or offsets  
• `4` for 4 - Federal income tax withheld  
• `5` for 5 - ATAA payments  
• `6` for 6 - Taxable grant  
• `7` for 7 - Agricultural payments  
• `9` for 9 - Market Gain |

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| FORM1099BOX | Optional | string | Form W-2G box values. Use:  
• `1` for 1 - Gross Winnings  
• `4` for 4 - Federal income tax withheld  
• `7` for 7 - Winnings from identical wagers  
• `14` for 14 - State winnings  
• `15` for 15 - State income tax withheld  
• `16` for 16 - Local winnings  
• `17` for 17 - Local income tax withheld |

Get Employee Type
-----------------

#### `read`

```
<read>
    <object>EMPLOYEETYPE</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEETYPE` |
| keys | Required | string | Comma-separated list of object `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Employee Type by ID
-----------------------

#### `readByName`

```
<readByName>
    <object>EMPLOYEETYPE</object>
    <keys>Full Time</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `EMPLOYEETYPE` |
| keys | Required | string | Comma-separated list of object `NAME` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

