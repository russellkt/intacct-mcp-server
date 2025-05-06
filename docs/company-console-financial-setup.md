Title: Financial Setup

URL Source: https://developer.intacct.com/api/company-console/financial-setup/

Markdown Content:
*   [Get Financial Setup](https://developer.intacct.com/api/company-console/financial-setup/#get-financial-setup)

* * *

Provides basic financial setup information for a company such as its base currency, first fiscal month, multi-currency setting, and so forth.

* * *

Get financial setup of a company.

#### `getFinancialSetup`

```
<getFinancialSetup/>
```

#### Parameters

No parameters

#### `Response`

```
<financialSetup>
    <baseCurrency>USD</baseCurrency>
    <defaultBook>ACCRUAL</defaultBook>
    <firstFiscalMonth>1</firstFiscalMonth>
    <multiBaseCurrency>false</multiBaseCurrency>
    <multiBook>false</multiBook>
    <multiCurrency>true</multiCurrency>
    <multiEntityShared>true</multiEntityShared>
</financialSetup>
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| defaultBook | string | Company’s default book can be either `ACCRUAL` or `CASH`. |
| multiBook | boolean | This is `true` if a company is enabled for multiple books (Cash and Accrual). |
| firstFiscalMonth | string | First fiscal month (1-12) |
| multiEntityShared | boolean | This is `true` if a company is enabled for multiple shared entities. |
| multiCurrency | boolean | This is `true` if a company is enabled for multiple currencies. |
| multiBaseCurrency | boolean | This is `true` if a company is enabled for multiple base currencies. |
| baseCurrency | string | Company’s base currency. This will be empty if `multiBaseCurrency` is `true`. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

