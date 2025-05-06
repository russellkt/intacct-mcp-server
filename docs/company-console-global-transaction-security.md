Title: Global Transaction Security Setup

URL Source: https://developer.intacct.com/api/company-console/global-transaction-security/

Markdown Content:
*   [Get Global Transaction Security Setup Object Definition](https://developer.intacct.com/api/company-console/global-transaction-security/#get-global-transaction-security-setup-object-definition)
*   [Get Global Transaction Security Setup](https://developer.intacct.com/api/company-console/global-transaction-security/#get-global-transaction-security-setup)
*   [Create Global Transaction Security Setup](https://developer.intacct.com/api/company-console/global-transaction-security/#create-global-transaction-security-setup)
*   [Update Global Transaction Security Setup](https://developer.intacct.com/api/company-console/global-transaction-security/#update-global-transaction-security-setup)

* * *

The Intacct transaction security controls help to prevent fraud by disabling certain types of changes to posted transactions. You can have different settings at the company level and in entities; entity level configurations override company level.

Users can still edit, delete, and reclassify transactions that have not been posted to the General Ledger, including transactions in draft, submitted, and partially approved states.

**Note:** Global Transaction Security settings will block API attempts to edit or delete transactions that have been posted to the General Ledger, which may interfere with 3rd party integrations.

* * *

Get Global Transaction Security Setup Object Definition
-------------------------------------------------------

### lookup

> List all the fields and relationships for the AFRSETUP object:

```
<lookup>
    <object>AFRSETUP</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `AFRSETUP` |

* * *

### read

```
<read>
    <object>AFRSETUP</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `AFRSETUP` |
| keys | Required | string | no value required |
| fields | Optional | string | Comma-separated list of fields on the object to get. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |

* * *

Create Global Transaction Security Setup
----------------------------------------

Create can only be used for the initial configuration of Global Transaction Security at the top level of the company.

### create

```
<create>
    <AFRSETUP>
        <DISABLEEDIT>true</DISABLEEDIT>
        <DISABLEDELETE>true</DISABLEDELETE>
        <DISABLERECLASS>true</DISABLERECLASS>
    </AFRSETUP>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `AFRSETUP` | Required | object | Type of object to create |

`AFRSETUP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| MODULEKEY | Required | string |   |
| DISABLEEDIT | Optional | boolean | Set to `true` to disallow edit on transactions posted to the General Ledger. |
| DISABLEDELETE | Optional | boolean | Set to `true` to disallow deleting transactions posted to the General Ledger. |
| DISABLERECLASS | Optional | boolean | Set to `true` to disallow reclassification of transactions posted to subledgers or to the General Ledger. |

* * *

Update Global Transaction Security Setup
----------------------------------------

### update

```
<update>
    <AFRSETUP>
        <DISABLEDELETE>false</DISABLEDELETE>
    </AFRSETUP>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `AFRSETUP` | Required | object | Object to update |

`AFRSETUP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| MODULEKEY | Required | string |   |
| DISABLEEDIT | Optional | boolean | Set to `true` to disallow edit on transactions posted to the General Ledger. |
| DISABLEDELETE | Optional | boolean | Set to `true` to disallow deleting transactions posted to the General Ledger. |
| DISABLERECLASS | Optional | boolean | Set to `true` to disallow reclassification of transactions posted to subledgers or to the General Ledger. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

