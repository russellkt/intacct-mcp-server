Title: Attachments

URL Source: https://developer.intacct.com/api/company-console/attachments/

Markdown Content:
*   [Attachments](https://developer.intacct.com/api/company-console/attachments/#attachments)
    *   [List Attachments (Legacy)](https://developer.intacct.com/api/company-console/attachments/#list-attachments-legacy)
    *   [Get Attachment by ID (Legacy)](https://developer.intacct.com/api/company-console/attachments/#get-attachment-by-id-legacy)
    *   [Create Attachment (Legacy)](https://developer.intacct.com/api/company-console/attachments/#create-attachment-legacy)
    *   [Update Attachment (Legacy)](https://developer.intacct.com/api/company-console/attachments/#update-attachment-legacy)
    *   [Delete Attachment (Legacy)](https://developer.intacct.com/api/company-console/attachments/#delete-attachment-legacy)
*   [Attachment Folders](https://developer.intacct.com/api/company-console/attachments/#attachment-folders)
    *   [List Attachment Folders (Legacy)](https://developer.intacct.com/api/company-console/attachments/#list-attachment-folders-legacy)
    *   [Get Attachment Folder by Name (Legacy)](https://developer.intacct.com/api/company-console/attachments/#get-attachment-folder-by-name-legacy)
    *   [Create Attachment Folder (Legacy)](https://developer.intacct.com/api/company-console/attachments/#create-attachment-folder-legacy)
    *   [Update Attachment Folder (Legacy)](https://developer.intacct.com/api/company-console/attachments/#update-attachment-folder-legacy)
    *   [Delete Attachment Folder (Legacy)](https://developer.intacct.com/api/company-console/attachments/#delete-attachment-folder-legacy)

* * *

An attachment can be any document, such as a bill, spreadsheet, or tax form, that provides tangible, historical, and auditable information in support of a transaction or financial record.

* * *

### List Attachments (Legacy)

Consider limiting the fields and `maxitems` returned because attachment data, which can be very large, is also sent.

#### `get_list`

```
<get_list object="supdoc" maxitems="1">
</get_list>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string attribute | Use `supdoc` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/company-console/attachments/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/company-console/attachments/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/company-console/attachments/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/company-console/attachments/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/company-console/attachments/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

`get_list.filter.expression`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| field | Required | string | Name of the field to be compared. |
| operator | Required | string | Comparison operator. Valid operators are
*   `=`
*   `!=`
*   `<`
*   `<=`
*   `>`
*   `>=`
*   `like`
*   `is null`

 |
| value | Required | string | Comparison value. |

`get_list.sort.sortfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order (attribute) | Required | string | Sort order for this named field. Use either `asc` or `desc`. |

* * *

### Get Attachment by ID (Legacy)

Consider limiting the fields and `maxitems` returned because attachment data, which can be very large, is also sent.

#### `get`

```
<get object="supdoc" key="A1234">
</get>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `supdoc` |
| key | Required | string | Object `supdocid` to get |
| fields | Optional | `field[0...n]` | Field(s) to return in response |

* * *

### Create Attachment (Legacy)

#### `create_supdoc`

```
<create_supdoc>
    <supdocid>newSupDocID</supdocid>
    <supdocfoldername>mySupFolder</supdocfoldername>
    <supdocdescription>Blah blah</supdocdescription>
    <attachments>
        <attachment>
            <attachmentname>My Attachment1</attachmentname>
            <attachmenttype>txt</attachmenttype>
            <attachmentdata>aGVsbG8gd29ybGQhIHRoaXMgaXMgYmFzZTY0IGVuY29kZWQgZGF0YQ==</attachmentdata>
        </attachment>
    </attachments>
</create_supdoc>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| supdocid | Optional | string | Attachment ID. Required if company does not have attachment autonumbering configured. |
| supdocname | Required | string | Name of attachment |
| supdocfoldername | Required | string | Attachments folder to create in |
| supdocdescription | Optional | string | Description |
| attachments | Optional | `attachment[0...n]` | Zero to many attachments |

`attachment`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| attachmentname | Required | string | File name, no period or extension |
| attachmenttype | Required | string | File extension, no period |
| attachmentdata | Required | string | Base64 encode the file’s binary data |

* * *

### Update Attachment (Legacy)

You can update the header information for the attachment, and you can provide additional attachment files using update.

You cannot use update to modify the contents of an existing attachment file directly. To work around this, [delete](https://developer.intacct.com/api/company-console/attachments/#delete-attachment-legacy) the existing attachment and start over, providing the new attachment file in the [create](https://developer.intacct.com/api/company-console/attachments/#create-attachment-legacy) call.

#### `update_supdoc`

> Update the header information and provide an additional attachment file.

```
<update_supdoc>
    <supdocid>oldSupDocID</supdocid>
    <supdocfoldername>A Different Folder</supdocfoldername>
    <supdocdescription>Update!</supdocdescription>
    <attachments>
        <attachment>
            <attachmentname>My Attachment1</attachmentname>
            <attachmenttype>txt</attachmenttype>
            <attachmentdata>aGVsbG8gd29ybGQhIHRoaXMgaXMgYmFzZTY0IGVuY29kZWQgZGF0YQ==</attachmentdata>
        </attachment>
    </attachments>
</update_supdoc>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| supdocid | Required | string | Attachment ID to update |
| supdocname | Optional | string | Name of attachment |
| supdocfoldername | Optional | string | Attachments folder to create in |
| supdocdescription | Optional | string | Description |
| attachments | Optional | `attachment[0...n]` |   |

`attachment`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| attachmentname | Required | string | File name for a new attachment, no period or extension. |
| attachmenttype | Required | string | File extension, no period |
| attachmentdata | Required | string | Base64 encode the file’s binary data |

* * *

### Delete Attachment (Legacy)

#### `delete_supdoc`

```
<delete_supdoc key="A1234"></delete_supdoc>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Attachment ID to delete |

* * *

Attachment Folders
------------------

### List Attachment Folders (Legacy)

#### `get_list`

```
<get_list object="supdocfolder">
</get_list>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `supdocfolder` |
| maxitems | Optional | integer attribute | Maximum number of items to return. |
| start | Optional | integer attribute | First item from total result set to include in response, zero-based integer. |
| showprivate | Optional | boolean attribute | Show entity private records if running this at top level. Use either `true` or `false`. (Default: `false`) |
| fields | Optional | array of `field` | List of fields to return in response. |
| filter | Optional | [object](https://developer.intacct.com/api/company-console/attachments/#get_list.filter) | Limits the objects to return based on their field values. |
| sorts | Optional | array of [`sortfield`](https://developer.intacct.com/api/company-console/attachments/#get_list.sort.sortfield) | Sets the order of results based on the values of specified fields. |

`get_list.filter`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| expression | Optional | [object](https://developer.intacct.com/api/company-console/attachments/#get_list.filter.expression) | A single filter expression made up of a field name, an operator, and a value. Required if not using `logical`. |
| logical | Optional | [object](https://developer.intacct.com/api/company-console/attachments/#get_list.filter.logical) | Multiple filter expressions that should be evaluated with `and` or `or`. Logical filters can be nested to create complex and/or logic. Required if not using `expression`. |

`get_list.filter.logical`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| logical\_operator | Required | string attribute | Operator. Use either `and` or `or`. |
| expression or logical | Required | `logical` or array of [`expression`](https://developer.intacct.com/api/company-console/attachments/#get_list.filter.expression) | Expressions to be evaluated as filters, and optionally additional logical evaluations. |

`get_list.filter.expression`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| field | Required | string | Name of the field to be compared. |
| operator | Required | string | Comparison operator. Valid operators are
*   `=`
*   `!=`
*   `<`
*   `<=`
*   `>`
*   `>=`
*   `like`
*   `is null`

 |
| value | Required | string | Comparison value. |

`get_list.sort.sortfield`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| order (attribute) | Required | string | Sort order for this named field. Use either `asc` or `desc`. |

* * *

### Get Attachment Folder by Name (Legacy)

#### `get`

```
<get object="supdocfolder" key="Bills">
</get>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `supdocfolder` |
| key | Required | string | Object `supdocfoldername` to get |
| fields | Optional | `field[0...n]` | Field(s) to return in response |

* * *

### Create Attachment Folder (Legacy)

#### `create_supdocfolder`

```
<create_supdocfolder>
    <supdocfoldername>MyTestFolder</supdocfoldername>
    <supdocfolderdescription></supdocfolderdescription>
    <supdocparentfoldername></supdocparentfoldername>
</create_supdocfolder>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| supdocfoldername | Required | string | Attachment folder name to create |
| supdocfolderdescription | Optional | string | Description |
| supdocparentfoldername | Optional | string | Parent attachment folder |

* * *

### Update Attachment Folder (Legacy)

#### `update_supdocfolder`

```
<update_supdocfolder>
    <supdocfoldername>MyTestFolder</supdocfoldername>
    <supdocfolderdescription>hello world!</supdocfolderdescription>
    <supdocparentfoldername></supdocparentfoldername>
</update_supdocfolder>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| supdocfoldername | Required | string | Attachment folder name to update |
| supdocfolderdescription | Optional | string | Description |
| supdocparentfoldername | Optional | string | Parent attachment folder |

* * *

### Delete Attachment Folder (Legacy)

#### `delete_supdocfolder`

```
<delete_supdocfolder key="MyFolder"></delete_supdocfolder>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| key | Required | string | Attachment folder name to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

