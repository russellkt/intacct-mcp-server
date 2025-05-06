Title: Run Ownership Structure Consolidation

URL Source: https://developer.intacct.com/api/consolidations/ownership-structure-consolidations/

Markdown Content:
*   [Run Ownership Structure Consolidation](https://developer.intacct.com/api/consolidations/ownership-structure-consolidations/#run-ownership-structure-consolidation)

* * *

Consolidate entities that have multi-level tier structures and/or entities with partial ownership.

Advanced ownership consolidation uses a defined [ownership structure](https://developer.intacct.com/api/consolidations/ownership-structures/) to create consolidated financial statements by period.

Usage information for [running a consolidation](https://www.intacct.com/ia/docs/en_US/help_action/Consolidations/Global_Consolidations/Consolidations/run-a-consolidation.htm) is available in the Sage Intacct product help.

* * *

#### `consolidatebytier`

> Run a consolidation:

```
<consolidatebytier>
    <structurename>NA Operations</structurename>
    <reportingperiodname>Month Ended January 2022</reportingperiodname>
    <email>noreply@sage.com</email>
</consolidatebytier>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| reportingperiodname | Required | string | Report period to consolidate |
| structurename | Required | string | Name of the [ownership structure](https://developer.intacct.com/api/consolidations/ownership-structures/) to consolidate. Use 20 characters or fewer. |
| email | Optional | string | Email address to send consolidation results to. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

