Title: Dunning Level Definitions

URL Source: https://developer.intacct.com/api/accounts-receivable/dunning/

Markdown Content:
*   [Get Dunning Definition Object Definition](https://developer.intacct.com/api/accounts-receivable/dunning/#get-dunning-definition-object-definition)
*   [Get a Dunning Definition](https://developer.intacct.com/api/accounts-receivable/dunning/#get-a-dunning-definition)
*   [Create Dunning Definition](https://developer.intacct.com/api/accounts-receivable/dunning/#create-dunning-definition)
*   [Update Dunning Definition](https://developer.intacct.com/api/accounts-receivable/dunning/#update-dunning-definition)
*   [Delete Dunning Definition](https://developer.intacct.com/api/accounts-receivable/dunning/#delete-dunning-definition)

* * *

**About Dunning Notices**

Dunning is the process of communicating with customers to collect overdue balances.

These communications can progress from gentle reminders to more aggressive letters as accounts become more overdue.

Use dunning levels to establish your company’s collection process. The dunning level defines the range for days overdue and commensurate invoice amounts and acts as a filter when you go to print or email dunning notices.

You can assign different printed document templates for each level using `PRINTTEMPLATENAME` or email templates using `EMAILTEMPLATEKEY`. This allows you to alter the tone of the letter based on how overdue the customer is or how much they owe.

Printing of dunning notices is done through the Intacct application.

* * *

Get Dunning Definition Object Definition
----------------------------------------

#### `lookup`

> List all the fields and relationships for the dunning object:

```
<lookup>
    <object>DUNNINGDEFINITION</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DUNNINGDEFINITION` |

* * *

Get a Dunning Definition
------------------------

#### `read`

```
        <read>
            <object>DUNNINGDEFINITION</object>
            <keys>150</keys>
            <fields>*</fields>
            <returnFormat>xml</returnFormat>
            <docparid></docparid>
        </read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DUNNINGDEFINITION` |

* * *

Create Dunning Definition
-------------------------

#### `create`

> Create a dunning definition:

```
        <create>
            <DUNNINGDEFINITION>
                <DUNNINGDEFINITIONID>Level-2</DUNNINGDEFINITIONID>
                <CURRENCY>USD</CURRENCY>
                <PRINTTEMPLATENAME>AR Dunning Notice - Standard</PRINTTEMPLATENAME>
                <EMAILTEMPLATEKEY>2</EMAILTEMPLATEKEY>
                <NOTICESEQUENCE>AA</NOTICESEQUENCE>
                <MINDAYS>1</MINDAYS>
                <MAXDAYS></MAXDAYS>
                <MINAMOUNT></MINAMOUNT>
                <MAXAMOUNT></MAXAMOUNT>
            </DUNNINGDEFINITION>
        </create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `DUNNINGDEFINITION` | Required | object | Object to create |

`DUNNINGDEFINITION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DUNNINGDEFINITIONID | Required | string | The title to use for the dunning level being created |
| CURRENCY | Optional | string | Currency filter for dunning notice |
| PRINTTEMPLATENAME | Required | string | Print template for dunning notice |
| EMAILTEMPLATEKEY | Optional | number | Email template for dunning notice |
| NOTICESEQUENCE | Required | string | Document sequence for dunning notice |
| MINDAYS | Optional | number | Minimum number of days overdue for a dunning notice to be sent by the system |
| MAXDAYS | Optional | number | Maximum number of overdue days for a dunning notice to be sent by the system |
| MINAMOUNT | Optional | number | Minimum overdue amount for a dunning notice to be sent by the system |
| MAXAMOUNT | Optional | number | Maximum overdue amount for a dunning notice to be sent by the system |

To find what email or print templates are available to assign to a particular dunning level, use the [Email template API](https://developer.intacct.com/api/accounts-receivable/customers/#query-and-list-customer-email-templates)

* * *

Update Dunning Definition
-------------------------

#### `update`

```
        <update>
            <DUNNINGDEFINITION>
                <RECORDNO>150</RECORDNO>
                <DUNNINGDEFINITIONID>Level5</DUNNINGDEFINITIONID>
                <CURRENCY>USD</CURRENCY>
                <PRINTTEMPLATENAME>AR Dunning Notice - Standard</PRINTTEMPLATENAME>
                <EMAILTEMPLATEKEY>2</EMAILTEMPLATEKEY>
                <MINDAYS>1</MINDAYS>
                <MAXDAYS></MAXDAYS>
                <MINAMOUNT></MINAMOUNT>
                <MAXAMOUNT></MAXAMOUNT>
                <NOTICESEQUENCE>AA</NOTICESEQUENCE>
            </DUNNINGDEFINITION>
        </update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `DUNNINGDEFINITION` | Required | object | Object to create |

`DUNNINGDEFINITION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CURRENCY | Optional | string | Currency filter for dunning notice |
| PRINTTEMPLATENAME | Required | string | Print template for dunning notice |
| EMAILTEMPLATEKEY | Optional | number | Email template for dunning notice |
| NOTICESEQUENCE | Required | string | Document sequence for dunning notice |
| MINDAYS | Optional | number | Minimum number of days overdue for a dunning notice to be sent by the system |
| MAXDAYS | Optional | number | Maximum number of overdue days for a dunning notice to be sent by the system |
| MINAMOUNT | Optional | number | Minimum overdue amount for a dunning notice to be sent by the system |
| MAXAMOUNT | Optional | number | Maximum overdue amount for a dunning notice to be sent by the system |

To find what email or print templates are available to assign to a particular dunning level, use the [Email template API](https://developer.intacct.com/api/accounts-receivable/customers/#query-and-list-customer-email-templates)

* * *

Delete Dunning Definition
-------------------------

#### `delete`

```
        <delete>
            <object>DUNNINGDEFINITION</object>
            <keys>151</keys>
        </delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `DUNNINGDEFINITION` |
| key | Required | string | Record number of dunning definitionx\` to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

