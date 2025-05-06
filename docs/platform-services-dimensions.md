Title: Dimensions

URL Source: https://developer.intacct.com/api/platform-services/dimensions/

Markdown Content:
*   [List Dimensions](https://developer.intacct.com/api/platform-services/dimensions/#list-dimensions)
*   [List Dimension Relationships](https://developer.intacct.com/api/platform-services/dimensions/#list-dimension-relationships)
*   [List Dimension Auto-fill Details](https://developer.intacct.com/api/platform-services/dimensions/#list-dimension-auto-fill-details)
*   [List Dimension Restrictions](https://developer.intacct.com/api/platform-services/dimensions/#list-dimension-restrictions)
*   [List Dimension(s) Restricted Data](https://developer.intacct.com/api/platform-services/dimensions/#list-dimensions-restricted-data)

* * *

A dimension is a classification used to organize, sort, and report on company information.

Standard dimensions such as Location and Department are provided by the system, or you can create user-defined dimensions (UDDs) with Platform Services. A UDD is simply a custom object that is enabled as a **user defined GL dimension**. Dimensions are available on reports and transaction entry pages.

A relationship between dimensions lets you populate a dimension value in a transaction based on the value of another dimension. Consider the following example, which shows the relationships for three UDDs.

![Image 1: relationships between UDDs](https://developer.intacct.com/images/api/platform-services/dimensions/relationship-model.png)

Given that the relationship from `PARTNER` to `PARTNER_TYPE` is to one, the system can be set up to auto-fill the value for `PARTNER_TYPE` when a specific partner is chosen on a transaction entry page. For example, choosing the Sarderra Partner on a transaction entry page can result in the prepopulated value of Full Service for Partner Type. In addition, since `PARTNER_TYPE` has a to-one relationship to `LINE_OF_BUSINESS`, providing the Full Service Partner Type can prepopulate the Line of Business field. Note that such fields can be set up as read only, as is the case for Line of Business, or available to override, as is the case for Partner Type.

![Image 2: autofill UI example](https://developer.intacct.com/images/api/platform-services/dimensions/autofill.png)

* * *

List Dimensions
---------------

Lists all standard dimensions and UDDs in a company along with helpful integration information about the object.

#### `getDimensions`

```
<getDimensions/>
```

#### Parameters

No parameters

#### `Response`

> The above function returns data structured like this:

```
<dimensions>
    <dimension>
        <objectName>DEPARTMENT</objectName>
        <objectLabel>Department</objectLabel>
        <termLabel>Department</termLabel>
        <userDefinedDimension>false</userDefinedDimension>
        <enabledInGL>true</enabledInGL>
    </dimension>
    <dimension>
        <objectName>LOCATION</objectName>
        <objectLabel>Location</objectLabel>
        <termLabel>Location</termLabel>
        <userDefinedDimension>false</userDefinedDimension>
        <enabledInGL>true</enabledInGL>
    </dimension>
    <!-- ... -->
    <dimension>
        <objectName>LINE_OF_BUSINESS</objectName>
        <objectLabel>Line of Business</objectLabel>
        <termLabel>Line of Business</termLabel>
        <userDefinedDimension>true</userDefinedDimension>
        <enabledInGL>true</enabledInGL>
    </dimension>
</dimensions>
```

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| objectName | string | Object integration name |
| objectLabel | string | Object label |
| termLabel | string | Terminology label, if renamed in company terminology |
| userDefinedDimension | boolean | This is `true` if the dimension is setup as a user defined dimension |
| enabledInGL | boolean | This is `true` if the dimension is enabled in the General Ledger module |

* * *

List Dimension Relationships
----------------------------

Lists all standard dimensions and UDDs and provides information about their to-one and to-many relationships to other dimensions.

#### `getDimensionRelationships`

```
<getDimensionRelationships/>
```

#### Parameters

No parameters

#### `Response`

> In this sample response, the `LOCATION` standard dimension has no relationships, but the UDDs do. For example, `LINE_OF_BUSINESS` has a one-to-many relationship to `PARTNER_TYPE`. Further down, you see that the `PARTNER_TYPE` has a many-to-one relationship back to `LINE_OF_BUSINESS`.

```
<relationship>
    <dimension>LOCATION</dimension>
    <object_id>5003</object_id>
    <autofillrelated>false</autofillrelated>
    <enableoverride>false</enableoverride>
</relationship>
...
<relationship>
    <dimension>LINE_OF_BUSINESS</dimension>
    <object_id>10002</object_id>
    <autofillrelated>true</autofillrelated>
    <enableoverride>true</enableoverride>
    <related>
        <dimension>PARTNER_TYPE</dimension>
        <object_id>10003</object_id>
        <relationship_id>10123</relationship_id>
        <source_side>One</source_side>
        <related_side>Many</related_side>
    </related>
</relationship>
<relationship>
    <dimension>PARTNER_TYPE</dimension>
    <object_id>10003</object_id>
    <autofillrelated>true</autofillrelated>
    <enableoverride>false</enableoverride>
    <related>
        <dimension>LINE_OF_BUSINESS</dimension>
        <object_id>10002</object_id>
        <relationship_id>10123</relationship_id>
        <source_side>Many</source_side>
        <related_side>One</related_side>
    </related>
    <related>
        <dimension>PARTNER</dimension>
        <object_id>10004</object_id>
        <relationship_id>10124</relationship_id>
        <source_side>One</source_side>
        <related_side>Many</related_side>
    </related>
</relationship>
<relationship>
    <dimension>PARTNER</dimension>
    <object_id>10004</object_id>
    <autofillrelated>true</autofillrelated>
    <enableoverride>true</enableoverride>
    <related>
        <dimension>PARTNER_TYPE</dimension>
        <object_id>10003</object_id>
        <relationship_id>10124</relationship_id>
        <source_side>Many</source_side>
        <related_side>One</related_side>
    </related>
</relationship>
```

`relationship[0...n]`

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dimension | string | Name of the standard dimension or UDD |
| object\_id | string | Dimension ID |
| autofillrelated | string | Indicates whether the values for related dimensions can be auto-filled |
| enableoverride | string | Indicates whether the auto-filled relationship values can be overriden |
| related | `related[0...n]` | Related dimensions |

`related[0...n]`

| Name | Type | Description |
| --- | --- | --- |
| dimension | string | Name of the related standard dimension or UDD |
| object\_id | string | Dimension ID |
| relationship\_id | string | Relationship ID |
| source\_side | string | Cardinality of the relationship from the source dimension |
| related\_side | string | Cardinality of the relationship to the target (`related`) dimension |

* * *

List Dimension Auto-fill Details
--------------------------------

Provides information about auto-fill settings for to-one relationships between dimensions. (If the relationship is to-many, auto-fill is not available.)

#### `getDimensionAutofillDetails`

```
<getDimensionAutofillDetails/>
```

#### Parameters

No parameters

#### `Response`

> This sample response shows that the `PARTNER_TYPE` dimension has a relationship to `LINE_OF_BUSINESS` where the value is auto-filled and cannot be overriden. The `PARTNER` dimension has a relationship to the `PARTNER_TYPE` dimension in which the relationship value is auto-filled but can be overriden.

```
<relationship>
    <dimension>LOCATION</dimension>
    <object_id>5003</object_id>
    <enableoverride>true</enableoverride>
</relationship>
<relationship>
    <dimension>LINE_OF_BUSINESS</dimension>
    <object_id>10002</object_id>
    <enableoverride>false</enableoverride>
</relationship>
<relationship>
    <dimension>PARTNER_TYPE</dimension>
    <object_id>10003</object_id>
    <enableoverride>false</enableoverride>
    <autofill>
        <dimension>LINE_OF_BUSINESS</dimension>
        <object_id>10002</object_id>
        <relationship_id>10123</relationship_id>
        <type>Many-to-One</type>
    </autofill>
</relationship>
<relationship>
    <dimension>PARTNER</dimension>
    <object_id>10004</object_id>
    <enableoverride>true</enableoverride>
    <autofill>
        <dimension>PARTNER_TYPE</dimension>
        <object_id>10003</object_id>
        <relationship_id>10124</relationship_id>
        <type>Many-to-One</type>
    </autofill>
</relationship>
```

`relationship[0...n]`

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dimension | string | Name of the standard dimension or UDD |
| object\_id | string | Dimension ID |
| enableoverride | string | Indicates whether auto-filled relationship values can be overriden for this dimension |
| autofill | `autofill[0...n]` | Dimension relationship with auto-fill enabled. Only to-one relationships can be auto-filled. |

`autofill[0...n]`

| Name | Type | Description |
| --- | --- | --- |
| dimension | string | Name of the standard dimension or UDD for the related dimension |
| object\_id | string | Dimension ID |
| relationship\_id | string | Relationship ID |
| type | string | Cardinality of the relationship from the perspective of the source dimension. |

* * *

List Dimension Restrictions
---------------------------

Provides information about dimensions with to-one restrictions.

#### `getDimensionRestrictions`

```
<getDimensionRestrictions/>
```

#### Parameters

No parameters

#### `Response`

> The response shows the to-one restrictions for each dimension, for example:

```
...
<restriction>
    <dimension>PARTNER_TYPE</dimension>
    <object_id>10003</object_id>
    <restrictedby>
        <dimension>LINE_OF_BUSINESS</dimension>
        <object_id>10002</object_id>
        <relationship_id>10123</relationship_id>
    </restrictedby>
</restriction>
<restriction>
    <dimension>PARTNER</dimension>
    <object_id>10004</object_id>
    <restrictedby>
        <dimension>PARTNER_TYPE</dimension>
        <object_id>10003</object_id>
        <relationship_id>10124</relationship_id>
    </restrictedby>
</restriction>
...
```

* * *

List Dimension(s) Restricted Data
---------------------------------

Lists the IDs of related dimensions that are the target(s) of to-many relationships from a single source dimension.

**Note:** To get to-one relationship values, list the dimension object and look for related fields (r_fields_) in the output. For more information, see the [FAQ](https://developer.intacct.com/support/faq/#how-do-i-get-the-targets-of-to-one-relationships-when-working-with-dimension-restrictions).

#### `getDimensionRestrictedData`

```
<getDimensionRestrictedData>
    <DimensionValue>
        <dimension>PARTNER_TYPE</dimension>
        <value>Full Service</value>
    </DimensionValue>
</getDimensionRestrictedData>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DimensionValue | Required | object | Dimension value to list. Provide only 1. |

`DimensionValue`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| dimension | Required | string | Dimension to list |
| value | Required | string | Value either Name/ID of dimension |

#### `Response`

> The sample response provides the IDs of the two related `PARTNER` records that are the targets of to-many relationships from the `PARTNER_TYPE` dimension. Nothing can be returned for the `LINE_OF_BUSINESS` dimension as it is the target of a to-one relationship from `PARTNER_TYPE`.

```
<RestrictedData>
    <dimension>PARTNER</dimension>
    <value>10008</value>
    <value>10009</value>
</RestrictedData>
```

`RestrictedData[0...n]`

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dimension | string | Name of the related standard dimension or UDD that is the target of a to-many relationship |
| value | ` value[0...n]` | IDs for the related dimension values that are the targets of to-many relationships |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

