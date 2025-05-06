Title: Locations

URL Source: https://developer.intacct.com/api/company-console/locations/

Markdown Content:
*   [Get Location Object Definition](https://developer.intacct.com/api/company-console/locations/#get-location-object-definition)
*   [Query and List Locations](https://developer.intacct.com/api/company-console/locations/#query-and-list-locations)
*   [Get Location](https://developer.intacct.com/api/company-console/locations/#get-location)
*   [Get Location by ID](https://developer.intacct.com/api/company-console/locations/#get-location-by-id)
*   [Create Location](https://developer.intacct.com/api/company-console/locations/#create-location)
*   [Create Location (Legacy)](https://developer.intacct.com/api/company-console/locations/#create-location-legacy)
*   [Update Location](https://developer.intacct.com/api/company-console/locations/#update-location)
*   [Update Location (Legacy)](https://developer.intacct.com/api/company-console/locations/#update-location-legacy)
*   [Delete Location](https://developer.intacct.com/api/company-console/locations/#delete-location)
*   [Delete Location (Legacy)](https://developer.intacct.com/api/company-console/locations/#delete-location-legacy)

* * *

Location is a dimension that can be defined by the company and set on transactions to expand report functionality and insight.

* * *

Get Location Object Definition
------------------------------

#### `lookup`

> List all the fields and relationships for the location object:

```
<lookup>
    <object>LOCATION</object>
</lookup>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATION` |

* * *

Query and List Locations
------------------------

#### `readByQuery`

```
<readByQuery>
    <object>LOCATION</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATION` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

`query` Fields

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STATUS | Optional | string | Status. Use `T` for Active and `F` for Inactive. |

* * *

Get Location
------------

#### `read`

```
<read>
    <object>LOCATION</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATION` |
| keys | Required | string | Comma-separated list of location `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Get Location by ID
------------------

#### `readByName`

```
<readByName>
    <object>LOCATION</object>
    <keys>110-SJC</keys>
    <fields>*</fields>
</readByName>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATION` |
| keys | Required | string | Comma-separated list of location `LOCATIONID` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

Create Location
---------------

#### `create`

```
<create>
    <LOCATION>
        <LOCATIONID>110-SJC</LOCATIONID>
        <NAME>San Jose CA</NAME>
        <PARENTID>100-US</PARENTID>
        <SUPERVISORID>E1010</SUPERVISORID>
        <CONTACTINFO>
            <CONTACTNAME>Smith, John</CONTACTNAME>
        </CONTACTINFO>
        <SHIPTO>
            <CONTACTNAME>Smith, Jane</CONTACTNAME>
        </SHIPTO>
        <STARTDATE>01/01/2000</STARTDATE>
        <ENDDATE></ENDDATE>
        <CUSTTITLE></CUSTTITLE>
        <STATUS>active</STATUS>
    </LOCATION>
</create>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATION | Required | object | Object to create |

`LOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATIONID | Required | string | Location ID to create |
| NAME | Required | string | Location name |
| PARENTID | Optional | string | Parent location ID |
| SUPERVISORID | Optional | string | Manager employee ID |
| CONTACTINFO | Optional | object | Primary contact info |
| SHIPTO | Optional | object | Ship to contact info |
| STARTDATE | Optional | string | Start date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy` |
| CUSTTITLE | Optional | string | Location title for reporting |
| STATUS | Optional | string | Location status. Use `active` for Active otherwise use `inactive` for Inactive (Default: `active`) |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Contact name |

`SHIPTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Contact name |

* * *

Create Location (Legacy)
------------------------

#### `create_location`

```
<create_location>
    <locationid>110-SJC</locationid>
    <name>San Jose CA</name>
</create_location>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| locationid | Required | string | Location ID to create |
| name | Required | string | Location name |
| parentid | Optional | string | Parent location ID |
| supervisorid | Optional | string | Manager employee ID |
| startdate | Optional | object | Start date |
| enddate | Optional | object | End date |
| status | Optional | string | Location status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |
| primary | Optional | object | Primary contact info |
| shipto | Optional | object | Ship to contact info |
| customfields | Optional | array of `customfield` | Custom fields |
| custtitle | Optional | string | Location title for reporting |

`startdate`  
`enddate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`primary`  
`shipto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Update Location
---------------

#### `update`

```
<update>
    <LOCATION>
        <RECORDNO>212</RECORDNO>
        <NAME>San Jose CA</NAME>
        <PARENTID></PARENTID>
        <SUPERVISORID></SUPERVISORID>
        <CONTACTINFO>
            <CONTACTNAME></CONTACTNAME>
        </CONTACTINFO>
        <SHIPTO>
            <CONTACTNAME></CONTACTNAME>
        </SHIPTO>
        <STARTDATE></STARTDATE>
        <ENDDATE></ENDDATE>
        <CUSTTITLE></CUSTTITLE>
        <STATUS>active</STATUS>
    </LOCATION>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| LOCATION | Required | object | Object to update |

`LOCATION`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Record number of location to update. Required if not using `LOCATIONID`. |
| LOCATIONID | Optional | string | Location ID. Required if not using `RECORDNO`. |
| NAME | Required | string | Location name |
| PARENTID | Optional | string | Parent location ID |
| SUPERVISORID | Optional | string | Manager employee ID |
| CONTACTINFO | Optional | object | Primary contact info |
| SHIPTO | Optional | object | Ship to contact info |
| STARTDATE | Optional | string | Start date in format `mm/dd/yyyy` |
| ENDDATE | Optional | string | End date in format `mm/dd/yyyy` |
| CUSTTITLE | Optional | string | Location title for reporting |
| STATUS | Optional | string | Location status. Use `active` for Active otherwise use `inactive` for Inactive. (Default: `active`) |

`CONTACTINFO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Contact name |

`SHIPTO`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| CONTACTNAME | Required | string | Contact name |

* * *

Update Location (Legacy)
------------------------

#### `update_location`

```
<update_location locationid="110-SJC">
    <name>San Jose California</name>
</update_location>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| locationid | Required | string | Location ID to update |
| name | Optional | string | Location name |
| parentid | Optional | string | Parent location ID |
| supervisorid | Optional | string | Manager employee ID |
| startdate | Optional | object | Start date |
| enddate | Optional | object | End date |
| status | Optional | string | Location status. Use `active` for Active otherwise use `inactive` for Inactive. |
| primary | Optional | object | Primary contact info |
| shipto | Optional | object | Ship to contact info |
| customfields | Optional | array of `customfield` | Custom fields |
| custtitle | Optional | string | Location title for reporting |

`enddate`  
`startdate`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| year | Required | string | Year `yyyy` |
| month | Required | string | Month `mm` |
| day | Required | string | Day `dd` |

`primary`  
`shipto`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| contactname | Required | string | Contact name of an existing contact |

`customfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| customfieldname | Optional | string | Custom field ID |
| customfieldvalue | Optional | varies | Custom field value. For a multi-pick-list custom field, implode multiple field values with `#~#`. |

* * *

Delete Location
---------------

#### `delete`

```
<delete>
    <object>LOCATION</object>
    <keys>112</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `LOCATION` |
| keys | Required | string | Comma-separated list of location `RECORDNO` to delete |

* * *

Delete Location (Legacy)
------------------------

#### `delete_location`

```
<delete_location locationid="110-SJC"></delete_location>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| locationid | Required | string | Location ID to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

