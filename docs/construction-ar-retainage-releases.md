Title: AR Retainage Releases

URL Source: https://developer.intacct.com/api/construction/ar-retainage-releases/

Markdown Content:
*   [AR Retainage Releases](https://developer.intacct.com/api/construction/ar-retainage-releases/#ar-retainage-releases)
    *   [Get AR Retainage Release Object Definition](https://developer.intacct.com/api/construction/ar-retainage-releases/#get-ar-retainage-release-object-definition)
    *   [Query and List AR Retainage Releases](https://developer.intacct.com/api/construction/ar-retainage-releases/#query-and-list-ar-retainage-releases)
    *   [Query and List AR Invoice Lines with Retainages](https://developer.intacct.com/api/construction/ar-retainage-releases/#query-and-list-ar-invoice-lines-with-retainages)
    *   [Query and List AR Retainage Release Entries (Legacy)](https://developer.intacct.com/api/construction/ar-retainage-releases/#query-and-list-ar-retainage-release-entries-legacy)
    *   [Get AR Retainage Release](https://developer.intacct.com/api/construction/ar-retainage-releases/#get-ar-retainage-release)
    *   [Create AR Retainage Release](https://developer.intacct.com/api/construction/ar-retainage-releases/#create-ar-retainage-release)
    *   [Update AR Retainage Release](https://developer.intacct.com/api/construction/ar-retainage-releases/#update-ar-retainage-release)
    *   [Delete AR Retainage Release](https://developer.intacct.com/api/construction/ar-retainage-releases/#delete-ar-retainage-release)
*   [AR Retainage Release Entries](https://developer.intacct.com/api/construction/ar-retainage-releases/#ar-retainage-release-entries)
    *   [Get AR Retainage Release Entry Object Definition](https://developer.intacct.com/api/construction/ar-retainage-releases/#get-ar-retainage-release-entry-object-definition)
    *   [Query and List AR Retainage Release Entries](https://developer.intacct.com/api/construction/ar-retainage-releases/#query-and-list-ar-retainage-release-entries)
    *   [Get AR Retainage Release Entry](https://developer.intacct.com/api/construction/ar-retainage-releases/#get-ar-retainage-release-entry)

* * *

This object lets you release amounts retained on invoices until completion of a construction project.

After the details have been satisfactorily addressed by both the project owner and the construction company, you create a retainage release for the amount still due from the customer. You can release some or all of the retainages due if there are still outstanding issues.

You must [configure retainage](https://www.intacct.com/ia/docs/en_US/help_action/Default.htm#cshid=configure_retainage) in your company as described in the Sage Intacct product help.

* * *

### Get AR Retainage Release Object Definition

#### `lookup`

> List all the fields and relationships for the AR retainage release object:

```
<lookup>
    <object>APRETAINAGERELEASE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRETAINAGERELEASE` |

* * *

### Query and List AR Retainage Releases

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, description, and release date for each retainage release where the release date is between the given dates:

```
<query>
    <object>ARRETAINAGERELEASE</object>
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
| object | Required | string | Use `ARRETAINAGERELEASE` |
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

### Query and List AR Invoice Lines with Retainages

#### [`query`](https://developer.intacct.com/web-services/queries/)

> For each AR invoice line for the given customer, provide its record number, the record number of the owning invoice, and the amount released and retained for that line.

```
<query>
    <object>ARINVOICEITEM</object>
    <select>
        <field>RECORDNO</field>
        <field>ARINVOICE.RECORDNO</field>
        <field>CUSTOMERID</field>
        <field>TRX_AMOUNTRETAINED</field>
        <field>TRX_AMOUNTRELEASED</field>
    </select>
    <filter>
        <isnotnull>
            <field>TRX_AMOUNTRETAINED</field>
        </isnotnull>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARINVOICEITEM` |
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
<data listtype="ARINVOICEITEM" totalcount="48" offset="0" count="48" numremaining="0">
    <ARINVOICEITEM>
        <RECORDNO>19</RECORDNO>
        <ARINVOICE.RECORDNO>4</ARINVOICE.RECORDNO>
        <CUSTOMERID>C101</CUSTOMERID>
        <TRX_AMOUNTRETAINED>500</TRX_AMOUNTRETAINED>
        <TRX_AMOUNTRELEASED>450</TRX_AMOUNTRELEASED>
    </ARINVOICEITEM>
    <ARINVOICEITEM>
        <RECORDNO>50</RECORDNO>
        <ARINVOICE.RECORDNO>11</ARINVOICE.RECORDNO>
        <CUSTOMERID>C102</CUSTOMERID>
        <TRX_AMOUNTRETAINED>3000</TRX_AMOUNTRETAINED>
        <TRX_AMOUNTRELEASED>3000</TRX_AMOUNTRELEASED>
    </ARINVOICEITEM>
    ...
 </data>
```

* * *

### Query and List AR Retainage Release Entries (Legacy)

#### `readByQuery`

```
<readByQuery>
    <object>ARRETAINAGERELEASEENTRY</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRETAINAGERELEASEENTRY` |
| fields | Optional | string | Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |
| query | Required | string | SQL-like query based on fields on the object. The following operators are supported: `<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`, `IS NOT NULL`, `IS NULL`, `AND`, `OR`. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes (`'Jane\'s Deli'`). Joins are not supported. |
| pagesize | Optional | integer | Custom page size between `1` and `1000` items (Default: `100`) |

* * *

### Get AR Retainage Release

#### `read`

```
<read>
    <object>ARRETAINAGERELEASE</object>
    <keys>29</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRETAINAGERELEASE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the AR retainage release to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

### Create AR Retainage Release

#### `create`

> Create an AR retainage release for two invoice line items:

```
<create>
    <ARRETAINAGERELEASE>
        <DESCRIPTION>Release for Customer C101</DESCRIPTION>
        <RELEASEDATE>03/15/2020</RELEASEDATE>
        <ARRETAINAGERELEASEENTRIES>
            <ARRETAINAGERELEASEENTRY>
                <RETAINAGEINVOICEKEY>4</RETAINAGEINVOICEKEY>
                <RETAINAGEINVOICEITEMKEY>19</RETAINAGEINVOICEITEMKEY>
                <TRX_AMOUNTRELEASED>50.00</TRX_AMOUNTRELEASED>
            </ARRETAINAGERELEASEENTRY>
        </ARRETAINAGERELEASEENTRIES>
    </ARRETAINAGERELEASE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `ARRETAINAGERELEASE` | Required | object | Object to create |

`ARRETAINAGERELEASE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| DESCRIPTION | Required | string | Description for the AR retainage release |
| RELEASEDATE | Optional | string | Release date in format `mm/dd/yyyy` (Default: Today’s date) |
| GLPOSTINGDATE | Optional | string | GL posting date in format `mm/dd/yyyy` (Default: Release date) |
| STATE | Optional | string | State for the retainage release. Use `Draft` or `Released` (Default: `Draft`) |
| ARRETAINAGERELEASEENTRIES | Optional | `ARRETAINAGERELEASEENTRY[0 .. n]` | Array of retainage release entries, each of which corresponds with an invoice line with retainages |

`ARRETAINAGERELEASEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RETAINAGEINVOICEKEY | Required | string | Invoice record number with retainages to be released |
| RETAINAGEINVOICEITEMKEY | Required | string | Invoice line record number |
| TRX\_AMOUNTRELEASED | Required | currency | Amount to release |

* * *

### Update AR Retainage Release

When updating an AR retainage release to modify the entries, be aware that it is a complete replacement of the existing set. So, to add an entry, supply all the original ones and the new one. To delete an entry, supply only the ones you want to keep.

#### `update`

```
<update>
    <ARRETAINAGERELEASE>
        <RECORDNO>29</RECORDNO>
        <ARRETAINAGERELEASEENTRIES>
            <ARRETAINAGERELEASEENTRY>
                <RETAINAGEINVOICEKEY>44</RETAINAGEINVOICEKEY>
                <RETAINAGEINVOICEITEMKEY>146</RETAINAGEINVOICEITEMKEY>
                <TRX_AMOUNTRELEASED>200</TRX_AMOUNTRELEASED>
            </ARRETAINAGERELEASEENTRY>
            <ARRETAINAGERELEASEENTRY>
                <RETAINAGEINVOICEKEY>44</RETAINAGEINVOICEKEY>
                <RETAINAGEINVOICEITEMKEY>148</RETAINAGEINVOICEITEMKEY>
                <TRX_AMOUNTRELEASED>300</TRX_AMOUNTRELEASED>
            </ARRETAINAGERELEASEENTRY>
        </ARRETAINAGERELEASEENTRIES>
    </ARRETAINAGERELEASE>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `ARRETAINAGERELEASE` | Required | object | Object to update |

`ARRETAINAGERELEASE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | string | Record number for the AR retainage release to update |
| RELEASEDATE | Optional | string | Release date in format `mm/dd/yyyy` |
| GLPOSTINGDATE | Optional | string | GL posting date in format `mm/dd/yyyy` |
| STATE | Optional | string | State for the retainage release. Use `Draft` or `Released` |
| ARRETAINAGERELEASEENTRIES | Optional | `ARETAINAGERELEASEENTRY[0 .. n]` | Array of retainage release entries, each of which corresponds with an invoice line with retainages. This a complete replacement of the existing set. |

`ARRETAINAGERELEASEENTRY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RETAINAGEINVOICEKEY | Required | string | Invoice record number with retainages to be released |
| RETAINAGEINVOICEITEMKEY | Required | string | Invoice line record number |
| TRX\_AMOUNTRELEASED | Required | currency | Amount to release |

* * *

### Delete AR Retainage Release

You can delete an AR retainage release that is in `Draft` state.

#### `delete`

```
<delete>
    <object>ARRETAINAGERELEASE</object>
    <keys>29</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRETAINAGERELEASE` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the ARRETAINAGERELEASE to delete |

* * *

AR Retainage Release Entries
----------------------------

### Get AR Retainage Release Entry Object Definition

#### `lookup`

> List all the fields and relationships for the AR retainage release entry object:

```
<lookup>
    <object>ARRETAINAGERELEASEENTRY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRETAINAGERELEASEENTRY` |

* * *

### Query and List AR Retainage Release Entries

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and transaction amount released for each AR retainage release entry for the invoice with record number 19:

```
<query>
    <object>ARRETAINAGERELEASEENTRY</object>
    <select>
        <field>RECORDNO</field>
        <field>TRX_AMOUNTRELEASED</field>
        <field>RETAINAGEINVOICEKEY</field>
    </select>
    <filter>
        <equalto>
            <field>RETAINAGEINVOICEKEY</field>
            <value>19</value>
        </equalto>
    </filter>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRETAINAGERELEASEENTRY` |
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

### Get AR Retainage Release Entry

#### `read`

```
<read>
    <object>ARRETAINAGERELEASEENTRY</object>
    <keys>8</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ARRETAINAGERELEASEENTRY` |
| keys | Required | string | Comma-separated list of `RECORDNO` of the AR retainage release entry to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

