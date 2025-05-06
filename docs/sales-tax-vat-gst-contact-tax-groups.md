Title: Contact Tax Groups

URL Source: https://developer.intacct.com/api/sales-tax-vat-gst/contact-tax-groups/

Markdown Content:
*   [Create Contact Tax Group (Legacy)](https://developer.intacct.com/api/sales-tax-vat-gst/contact-tax-groups/#create-contact-tax-group-legacy)
*   [Delete Contact Tax Group (Legacy)](https://developer.intacct.com/api/sales-tax-vat-gst/contact-tax-groups/#delete-contact-tax-group-legacy)

* * *

Contact tax groups enable you to apply different taxes to customers, vendors, and their contacts, according to their jurisdictions. You associate customers, vendors, and their contacts with contact tax groups. Then, you use tax schedule maps to apply different tax schedules to your contact tax groups.

* * *

#### `create_contacttaxgroup`

```
<create_contacttaxgroup>
    <name>TN-19</name>
</create_contacttaxgroup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Name |

* * *

#### `delete_contacttaxgroup`

```
<delete_contacttaxgroup name="TN-14"></delete_contacttaxgroup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| name | Required | string | Contact tax group name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

