Title: Run Global or Domestic Consolidation

URL Source: https://developer.intacct.com/api/consolidations/global-consolidations/

Markdown Content:
*   [Run Global Consolidation](https://developer.intacct.com/api/consolidations/global-consolidations/#run-global-consolidation)
*   [Run Global Consolidation (Legacy)](https://developer.intacct.com/api/consolidations/global-consolidations/#run-global-consolidation-legacy)

* * *

Consolidation books contain entities with different operating currencies that must be converted into a single currency for reporting and budgeting.

You can run a global or domestic consolidation to accomplish this.

Usage information for [running consolidations](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=Consolidating_Subsidiary_Data) is available in the Sage Intacct product help. https://www.intacct.com/ia/docs/en\_US/help\_action/Default.htm#cshid=Consolidating\_Subsidiary\_Data

**Note:** Most consolidation object names start with `GC` and are called “Global Coonsolidation,” but you can use them for domestic or global consolidations.

* * *

#### `consolidate`

```
<consolidate>
    <bookid>gc_book</bookid>
    <offline>F</offline>
    <updatesucceedingperiods>F</updatesucceedingperiods>
    <changesonly>true</changesonly>
    <email>noreply@intacct.com</email>
    <reportingperiodname>Month Ended January 2017</reportingperiodname>
    <entities>
        <csnentity>
            <entityid>100-US</entityid>
            <bsrate></bsrate>
            <warate></warate>
        </csnentity>
        <csnentity>
            <entityid>200-MX</entityid>
            <bsrate></bsrate>
            <warate></warate>
        </csnentity>
    </entities>
</consolidate>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bookid | Required | string | Consolidation book ID |
| offline | Optional | boolean | Run consolidation offline. Use `F` for No, `T` for Yes. (Default: `F`) |
| updatesucceedingperiods | Optional | boolean | Consolidate succeeding periods. Use `false` for No, `true` for Yes. (Default: `false`) |
| changesonly | Required | boolean | Only consolidate changes since last consolidation. Use `T` to consolidate changes only, `F` otherwise. |
| email | Optional | string | Email consolidation results to this address |
| reportingperiodname | Required | string | Report period name to consolidate |
| entities | Optional | `csnentity[0...n]` | Entities to consolidate in addition to any entities already set up for the book |

`csnentity`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| entityid | Required | string | Entity ID |
| bsrate | Optional | currency | Balance sheet rate |
| warate | Optional | currency | Weighted average rate |

* * *

Run Global Consolidation (Legacy)
---------------------------------

#### `create_consolidation`

```
<create_consolidation>
    <bookid>USCON</bookid>
    <offline>false</offline>
    <updatesucceedingperiods>false</updatesucceedingperiods>
    <changesonly>true</changesonly>
    <email>noreply@intacct.com</email>
    <reportingperiodname>Month Ended January 2017</reportingperiodname>
    <entities>
        <csnentity>
            <entityid>100-US</entityid>
            <bsrate></bsrate>
            <warate></warate>
        </csnentity>
        <csnentity>
            <entityid>200-MX</entityid>
            <bsrate></bsrate>
            <warate></warate>
        </csnentity>
    </entities>
</create_consolidation>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| bookid | Required | string | Consolidation book ID |
| offline | Optional | boolean | Run consolidation offline. Use `false` for No, `true` for Yes. (Default: `false`) |
| updatesucceedingperiods | Optional | boolean | Consolidate succeeding periods. Use `false` for No, `true` for Yes. (Default: `false`) |
| changesonly | Optional | boolean | Only consolidate changes since last consolidation. Use `T` to consolidate changes only, `F` otherwise. (Default: `T`) |
| email | Optional | string | Email consolidation results to this address |
| reportingperiodname | Required | string | Report period name to consolidate |
| entities | Optional | `csnentity[0...n]` | Entities to consolidate in addition to any entities already set up for the book |

`csnentity`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| entityid | Required | string | Entity ID |
| bsrate | Optional | currency | Balance sheet rate |
| warate | Optional | currency | Weighted average rate |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

