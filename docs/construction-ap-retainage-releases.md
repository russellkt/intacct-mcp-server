Title: AP Retainage Releases

URL Source: https://developer.intacct.com/api/construction/ap-retainage-releases/

Markdown Content:
*   [AP Retainage Releases](https://developer.intacct.com/api/construction/ap-retainage-releases/#ap-retainage-releases)
    *   [Get AP Retainage Release Object Definition](https://developer.intacct.com/api/construction/ap-retainage-releases/#get-ap-retainage-release-object-definition)
    *   [Query and List AP Retainage Releases](https://developer.intacct.com/api/construction/ap-retainage-releases/#query-and-list-ap-retainage-releases)
    *   [Query and List AP Bill Lines with Retainages](https://developer.intacct.com/api/construction/ap-retainage-releases/#query-and-list-ap-bill-lines-with-retainages)
    *   [Query and List AP Retainage Releases (Legacy)](https://developer.intacct.com/api/construction/ap-retainage-releases/#query-and-list-ap-retainage-releases-legacy)
    *   [Get AP Retainage Release](https://developer.intacct.com/api/construction/ap-retainage-releases/#get-ap-retainage-release)
    *   [Create AP Retainage Release](https://developer.intacct.com/api/construction/ap-retainage-releases/#create-ap-retainage-release)
    *   [Update AP Retainage Release](https://developer.intacct.com/api/construction/ap-retainage-releases/#update-ap-retainage-release)
    *   [Delete AP Retainage Release](https://developer.intacct.com/api/construction/ap-retainage-releases/#delete-ap-retainage-release)
*   [AP Retainage Release Entries](https://developer.intacct.com/api/construction/ap-retainage-releases/#ap-retainage-release-entries)
    *   [Get AP Retainage Release Entry Object Definition](https://developer.intacct.com/api/construction/ap-retainage-releases/#get-ap-retainage-release-entry-object-definition)
    *   [Query and List AP Retainage Release Entries](https://developer.intacct.com/api/construction/ap-retainage-releases/#query-and-list-ap-retainage-release-entries)
    *   [Query and List AP Retainage Release Entries (Legacy)](https://developer.intacct.com/api/construction/ap-retainage-releases/#query-and-list-ap-retainage-release-entries-legacy)
    *   [Get AP Retainage Release Entry](https://developer.intacct.com/api/construction/ap-retainage-releases/#get-ap-retainage-release-entry)

* * *

This object lets you release amounts retained on AP bills until completion of a construction project.

After the details have been satisfactorily addressed by both the project owner and the construction company, you create a retainage release for the amount still owed to the vendor/subcontractor. You can release some or all of the owed retainages if there are still outstanding issues.

You must [configure retainage](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=configure_retainage) in your company as described in the Sage Intacct product help.

* * *

### Get AP Retainage Release Object Definition

#### `lookup`

> List all the fields and relationships for the AP retainage release object:

```
<lookup>
    <object>APRETAINAGERELEASE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASE` |

* * *

### Query and List AP Retainage Releases

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, description, and release date for each retainage release where the release date is between the given dates:

```
<query>
    <object>APRETAINAGERELEASE</object>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
        <field>RELEASEDATE</field>
    </select>
    <filter>
        <between>
            <field>RELEASEDATE</field>
            <value>01/01/2020</value>
            <value>03/01/2020</value>
        </between>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASE` |
| filter | Optional | object | [Filter expression](https://developer.intacct.com/web-services/queries/#filter) to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, `VENDOR.CREDITLIMIT` on APBILL). |
| select | Required | sequence | The names of the fields that you want included in the response, and an optional [aggregate function](https://developer.intacct.com/web-services/queries/#aggregate-functions) such as `count` or `sum`. Returning all fields is not supported. |
| orderby | Optional | object | Provide an `order` element with a field name and choose an ascending or descending [sort order](https://developer.intacct.com/web-services/queries/#order-by), for example:  
```
<order>  
   <field>RECORDNO</field>   
   <descending/>   
</order>
``` |
| options | Optional | object | [Query options](https://developer.intacct.com/web-services/queries/#options):
*   Set the `caseinsensitive` element to `true` for a case-insensitive query  
     `<caseinsensitive>true</caseinsensitive>`
*   In a multi-entity company, set the `showprivate` element to `true` to query data in private entities:  
     `<showprivate>true</showprivate>`
*   Specify the `returnformat` for the response: `xml` (default), `json`, or `csv`  
     `<returnformat>json</returnformat>`

 |
| pagesize | Optional | integer | Maximum number of matching objects to return in the response, between `1` and `2000` items (Default: `100`) |
| offset | Optional | integer | Point at which to start indexing into records (Default: `0`) |

* * *

### Query and List AP Bill Lines with Retainages

#### [`query`](https://developer.intacct.com/web-services/queries/)

> For each AP bill line for the given vendor, provide its record number, the record number of the owning bill, and the amount released and retained for that line.

```
<query>
    <object>APBILLITEM</object>
    <select>
        <field>RECORDNO</field>
        <field>APBILL.RECORDNO</field>
        <field>VENDORID</field>
        <field>TRX_AMOUNTRETAINED</field>
        <field>TRX_AMOUNTRELEASED</field>
    </select>
    <filter>
        <and>
            <isnotnull>
                <field>TRX_AMOUNTRETAINED</field>
            </isnotnull>
            <notequalto>
                <field>TRX_AMOUNTRETAINED</field>
                <value>0</value>
            </notequalto>
        </and>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APBILLENTRY` |
| filter | Optional | object | [Filter expression](https://developer.intacct.com/web-services/queries/#filter) to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, `VENDOR.CREDITLIMIT` on APBILL). |
| select | Required | sequence | The names of the fields that you want included in the response, and an optional [aggregate function](https://developer.intacct.com/web-services/queries/#aggregate-functions) such as `count` or `sum`. Returning all fields is not supported. |
| orderby | Optional | object | Provide an `order` element with a field name and choose an ascending or descending [sort order](https://developer.intacct.com/web-services/queries/#order-by), for example:  
```
<order>  
   <field>RECORDNO</field>   
   <descending/>   
</order>
``` |
| options | Optional | object | [Query options](https://developer.intacct.com/web-services/queries/#options):
*   Set the `caseinsensitive` element to `true` for a case-insensitive query  
     `<caseinsensitive>true</caseinsensitive>`
*   In a multi-entity company, set the `showprivate` element to `true` to query data in private entities:  
     `<showprivate>true</showprivate>`
*   Specify the `returnformat` for the response: `xml` (default), `json`, or `csv`  
     `<returnformat>json</returnformat>`

 |
| pagesize | Optional | integer | Maximum number of matching objects to return in the response, between `1` and `2000` items (Default: `100`) |
| offset | Optional | integer | Point at which to start indexing into records (Default: `0`) |

#### `Response`

> The above function returns data structured like this:

```
<data listtype="APBILLITEM" totalcount="45" offset="0" count="45" numremaining="0">
    <APBILLITEM>
        <RECORDNO>134</RECORDNO>
        <APBILL.RECORDNO>40</APBILL.RECORDNO>
        <VENDORID>V100</VENDORID>
        <TRX_AMOUNTRETAINED>500</TRX_AMOUNTRETAINED>
        <TRX_AMOUNTRELEASED>375</TRX_AMOUNTRELEASED>
    </APBILLITEM>
    <APBILLITEM>
        <RECORDNO>1</RECORDNO>
        <APBILL.RECORDNO>1</APBILL.RECORDNO>
        <VENDORID>V100</VENDORID>
        <TRX_AMOUNTRETAINED>2000</TRX_AMOUNTRETAINED>
        <TRX_AMOUNTRELEASED>2000</TRX_AMOUNTRELEASED>
    </APBILLITEM>
 </data>
```

* * *

### Query and List AP Retainage Releases (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APRETAINAGERELEASE</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AP Retainage Release

#### `read`

```
<read>
    <object>APRETAINAGERELEASE</object>
    <keys>26</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the AP retainage release to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create AP Retainage Release

#### `create`

> Create an AP retainage release for two bill line items:

```
<create>
    <APRETAINAGERELEASE>
        <DESCRIPTION>Release for Vendor V100</DESCRIPTION>
        <RELEASEDATE>03/15/2020</RELEASEDATE>
        <APRETAINAGERELEASEENTRIES>
            <APRETAINAGERELEASEENTRY>
                <RETAINAGEBILLKEY>40</RETAINAGEBILLKEY>
                <RETAINAGEBILLITEMKEY>134</RETAINAGEBILLITEMKEY>
                <TRX_AMOUNTRELEASED>125.00</TRX_AMOUNTRELEASED>
            </APRETAINAGERELEASEENTRY>
        </APRETAINAGERELEASEENTRIES>
    </APRETAINAGERELEASE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `APRETAINAGERELEASE` | Required | object | Object to create |

`APRETAINAGERELEASE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DESCRIPTION | Required | string | Description for the AP retainage release |
| RELEASEDATE | Optional | string | Release date in format `mm/dd/yyyy` (Default: Today’s date) |
| GLPOSTINGDATE | Optional | string | GL posting date in format `mm/dd/yyyy` (Default: Release date) |
| STATE | Optional | string | State for the retainage release. Use `Draft` or `Released` (Default: `Draft`) |
| APRETAINAGERELEASEENTRIES | Optional | `APRETAINAGERELEASEENTRY[0 .. n]` | Array of retainage release entries, each of which corresponds with a bill line with retainages |

`APRETAINAGERELEASEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RETAINAGEBILLKEY | Required | string | Bill record number with retainages to be released |
| RETAINAGEBILLITEMKEY | Required | string | Bill line record number |
| TRX\_AMOUNTRELEASED | Required | currency | Amount to release |

* * *

### Update AP Retainage Release

When updating an AP retainage release to modify the entries, be aware that it is a complete replacement of the existing set. So, to add an entry, supply all the original ones and the new one. To delete an entry, supply only the ones you want to keep.

#### `update`

```
<update>
    <APRETAINAGERELEASE>
        <RECORDNO>26</RECORDNO>
        <APRETAINAGERELEASEENTRIES>
            <APRETAINAGERELEASEENTRY>
                <RETAINAGEINVOICEKEY>44</RETAINAGEINVOICEKEY>
                <RETAINAGEINVOICEITEMKEY>146</RETAINAGEINVOICEITEMKEY>
                <TRX_AMOUNTRELEASED>200</TRX_AMOUNTRELEASED>
            </APRETAINAGERELEASEENTRY>
            <APRETAINAGERELEASEENTRY>
                <RETAINAGEINVOICEKEY>44</RETAINAGEINVOICEKEY>
                <RETAINAGEINVOICEITEMKEY>148</RETAINAGEINVOICEITEMKEY>
                <TRX_AMOUNTRELEASED>300</TRX_AMOUNTRELEASED>
            </APRETAINAGERELEASEENTRY>
        </APRETAINAGERELEASEENTRIES>
    </APRETAINAGERELEASE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `APRETAINAGERELEASE` | Required | object | Object to update |

`APRETAINAGERELEASE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number for the AP retainage release to update |
| RELEASEDATE | Optional | string | Release date in format `mm/dd/yyyy` |
| GLPOSTINGDATE | Optional | string | GL posting date in format `mm/dd/yyyy` |
| STATE | Optional | string | State for the retainage release. Use `Draft` or `Released` |
| APRETAINAGERELEASEENTRIES | Optional | `APRETAINAGERELEASEENTRY[0 .. n]` | Array of retainage release entries, each of which corresponds with a bill line with retainages. This a complete replacement of the existing set. |

`APRETAINAGERELEASEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RETAINAGEBILLKEY | Required | string | Bill record number with retainages to be released |
| RETAINAGEBILLITEMKEY | Required | string | Bill line record number |
| TRX\_AMOUNTRELEASED | Required | currency | Amount to release |

* * *

### Delete AP Retainage Release

You can delete an AP retainage release that is in `Draft` state.

#### `delete`

```
<delete>
    <object>APRETAINAGERELEASE</object>
    <keys>26</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the APRETAINAGERELEASE to delete |

* * *

AP Retainage Release Entries
----------------------------

### Get AP Retainage Release Entry Object Definition

#### `lookup`

> List all the fields and relationships for the AP retainage release entry object:

```
<lookup>
    <object>APRETAINAGERELEASEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASEENTRY` |

* * *

### Query and List AP Retainage Release Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and transaction amount released for each AP retainage release entry for the bill with record number 15:

```
<query>
    <object>APRETAINAGERELEASEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>TRX_AMOUNTRELEASED</field>
        <field>RETAINAGEBILLKEY</field>
    </select>
    <filter>
        <equalto>
            <field>RETAINAGEBILLKEY</field>
            <value>15</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASEENTRY` |
| filter | Optional | object | [Filter expression](https://developer.intacct.com/web-services/queries/#filter) to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, `VENDOR.CREDITLIMIT` on APBILL). |
| select | Required | sequence | The names of the fields that you want included in the response, and an optional [aggregate function](https://developer.intacct.com/web-services/queries/#aggregate-functions) such as `count` or `sum`. Returning all fields is not supported. |
| orderby | Optional | object | Provide an `order` element with a field name and choose an ascending or descending [sort order](https://developer.intacct.com/web-services/queries/#order-by), for example:  
```
<order>  
   <field>RECORDNO</field>   
   <descending/>   
</order>
``` |
| options | Optional | object | [Query options](https://developer.intacct.com/web-services/queries/#options):
*   Set the `caseinsensitive` element to `true` for a case-insensitive query  
     `<caseinsensitive>true</caseinsensitive>`
*   In a multi-entity company, set the `showprivate` element to `true` to query data in private entities:  
     `<showprivate>true</showprivate>`
*   Specify the `returnformat` for the response: `xml` (default), `json`, or `csv`  
     `<returnformat>json</returnformat>`

 |
| pagesize | Optional | integer | Maximum number of matching objects to return in the response, between `1` and `2000` items (Default: `100`) |
| offset | Optional | integer | Point at which to start indexing into records (Default: `0`) |

* * *

### Query and List AP Retainage Release Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>APRETAINAGERELEASEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AP Retainage Release Entry

#### `read`

```
<read>
    <object>APRETAINAGERELEASEENTRY</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `APRETAINAGERELEASEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the AP retainage release entry to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

