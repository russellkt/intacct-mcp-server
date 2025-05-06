Title: Views

URL Source: https://developer.intacct.com/api/platform-services/views/

Markdown Content:
*   [List View Records](https://developer.intacct.com/api/platform-services/views/#list-view-records)

* * *

Custom list views let you display list items the way you need to see them by applying filters and sorting.

For example, the vendor object definition has an **All Vendors** view with an original ID that uniquely identifies the view in your company. You can use `readView` to list a subset of the vendors in that view based on your filtering.

* * *

List View Records
-----------------

> Filters an existing vendor view to list vendors where the total due is greater than 30,000 and the credit limit is less than 25,000.

#### `readView`

```
<readView>
    <view>VENDOR#135422@10051</view>
    <pagesize>100</pagesize>
    <filters>
        <filterCondition>AND</filterCondition>
        <filterExpression>
            <field>totaldue</field>
            <operator>greater than</operator>
            <value>30000</value>
        </filterExpression>
        <filterExpression>
            <field>creditlimit</field>
            <operator>less than</operator>
            <value>25000</value>
        </filterExpression>
    </filters>
</readView>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| view | Required | string | Object and original ID for an existing view in the format `object#originalId`, for example, `VENDOR#135422@10051`. A view is assigned an original ID at creation time and this ID never changes. To find the original ID of a view, go to **Platform Services \> Objects**, click on the object you want, and go to the **Views** section where the **Original ID**s are listed. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |
| filters | Optional | string | Accepts a filter condition such as `AND` or `OR`, and individual filter expressions based on field values. The individual expressions include a field name, and operator, and a value. For help building expressions, see [list views](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=List_views) in the Sage Intacct product help. |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

