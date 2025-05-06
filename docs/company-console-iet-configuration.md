Title: Inter-Entity Transaction Configuration

URL Source: https://developer.intacct.com/api/company-console/iet-configuration/

Markdown Content:
*   [Get the Inter-Entity Configuration](https://developer.intacct.com/api/company-console/iet-configuration/#get-the-inter-entity-configuration)
*   [Update the Inter-Entity Configuration](https://developer.intacct.com/api/company-console/iet-configuration/#update-the-inter-entity-configuration)
*   [Delete Inter-Entity Account Default](https://developer.intacct.com/api/company-console/iet-configuration/#delete-inter-entity-account-default)
*   [Delete Inter-Entity Account Override](https://developer.intacct.com/api/company-console/iet-configuration/#delete-inter-entity-account-override)

* * *

The inter-entity configuration object lets you designate payable and receivable accounts for inter-entity transactions in a multi-entity shared company.

There is only one inter-entity configuration object (INTERENTITYSETUP) for a company, and the record number is always 1.

Two types of inter-entity configuration are available:

*   With the basic configuration, you provide one default inter-entity receivable (IER) account and one default inter-entity payable (IEP) account for each entity.
*   With the advanced configuration, you create a relationship between two entities and provide the IER and IEP accounts for each side of the relationship.

Your company will use one type of configuration or the other—they cannot be used together.

* * *

When you get an inter-entity configuration, the type of configuration (`ADVANCED` or `BASIC`) is returned via the `IEMAPPLAN` parameter in the response.

#### `read`

> Get the inter-entity configuration object using the record number, which is always 1.

```
<read>
    <object>INTERENTITYSETUP</object>
    <keys>1</keys>
    <fields>*</fields>
</read>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use INTERENTITYSETUP |
| keys | Required | string | Use 1 |
| fields | Optional | string | Comma-separated list of fields on the object to get. To return all fields, omit the element or provide `*` for the value.  
For best performance and predictability, limit the number of fields. |
| returnFormat | Optional | string | Data format for the response body:
*   `xml` (default)
*   `json`
*   `csv`

 |

#### `Response`

`INTERENTITYSETUP`

> The above function returns the following for a basic configuration:

```
<INTERENTITYSETUP>
    <RECORDNO>1</RECORDNO>
    <IEMAPPLAN>BASIC</IEMAPPLAN>
    <ENTITYACCTDEFAULTS>
        <entityacctdefault>
            <RECORDNO>4</RECORDNO>
            <ENTITYID>Central Region</ENTITYID>
            <ENTITYKEY>4</ENTITYKEY>
            <ENTITYNAME>Central Region</ENTITYNAME>
            <ENTITYSTATUS>T</ENTITYSTATUS>
            <IEPAYABLEACCTKEY>44</IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO>2000</IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME>Accounts Payable</IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY>3</IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO>1000</IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME>Cash in Bank</IERECEIVABLEACCTNAME>
        </entityacctdefault>
        <entityacctdefault>
            <RECORDNO>5</RECORDNO>
            <ENTITYID>Eastern Region</ENTITYID>
            <ENTITYKEY>5</ENTITYKEY>
            <ENTITYNAME>Eastern Region</ENTITYNAME>
            <ENTITYSTATUS>T</ENTITYSTATUS>
            <IEPAYABLEACCTKEY>163</IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO>2008</IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME>Checking - Western Region</IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY>163</IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO>1006</IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME>Checking - Western Region</IERECEIVABLEACCTNAME>
        </entityacctdefault>
        <entityacctdefault>
            <RECORDNO>3</RECORDNO>
            <ENTITYID>Mountain Region</ENTITYID>
            <ENTITYKEY>3</ENTITYKEY>
            <ENTITYNAME>Mountain Region</ENTITYNAME>
            <ENTITYSTATUS>T</ENTITYSTATUS>
            <IEPAYABLEACCTKEY></IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO></IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME></IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY></IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO></IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME></IERECEIVABLEACCTNAME>
        </entityacctdefault>
        <entityacctdefault>
            <RECORDNO>2</RECORDNO>
            <ENTITYID>Western Region</ENTITYID>
            <ENTITYKEY>2</ENTITYKEY>
            <ENTITYNAME>Western Region</ENTITYNAME>
            <ENTITYSTATUS>T</ENTITYSTATUS>
            <IEPAYABLEACCTKEY></IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO></IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME></IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY></IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO></IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME></IERECEIVABLEACCTNAME>
        </entityacctdefault>
    </ENTITYACCTDEFAULTS>
</INTERENTITYSETUP>
```

> The above function returns the following for an advanced configuration:

```
<INTERENTITYSETUP>
    <RECORDNO>1</RECORDNO>
    <IEMAPPLAN>ADVANCED</IEMAPPLAN>
    <ENTITYACCTOVERRIDES>
        <entityacctoverride>
            <RECORDNO>2</RECORDNO>
            <SOURCEENTITYID>Central Region</SOURCEENTITYID>
            <SOURCEENTITYKEY>4</SOURCEENTITYKEY>
            <SOURCEENTITYNAME>Central Region</SOURCEENTITYNAME>
            <SOURCEENTITYSTATUS>T</SOURCEENTITYSTATUS>          
            <TARGETENTITYID>Mountain Region</TARGETENTITYID>
            <TARGETENTITYKEY>3</TARGETENTITYKEY>
            <TARGETENTITYNAME>Mountain Region</TARGETENTITYNAME>
            <TARGETENTITYSTATUS>T</TARGETENTITYSTATUS>
            <IEPAYABLEACCTKEY>162</IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO>2000</IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME>Checking - Eastern Region</IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY>163</IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO>1000</IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME>Checking - Western Region</IERECEIVABLEACCTNAME>
        </entityacctoverride>
        <entityacctoverride>
            <RECORDNO>6</RECORDNO>
            <SOURCEENTITYID>Central Region</SOURCEENTITYID>
            <SOURCEENTITYKEY>4</SOURCEENTITYKEY>
            <SOURCEENTITYNAME>Central Region</SOURCEENTITYNAME>
            <SOURCEENTITYSTATUS>T</SOURCEENTITYSTATUS>
            <TARGETENTITYID>Western Region</TARGETENTITYID>
            <TARGETENTITYKEY>2</TARGETENTITYKEY>
            <TARGETENTITYNAME>Western Region</TARGETENTITYNAME>
            <TARGETENTITYSTATUS>T</TARGETENTITYSTATUS>
            <IEPAYABLEACCTKEY>164</IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO>2044</IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME>Checking - Mountain Region</IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY>161</IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO>1044</IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME>Checking - Central Region</IERECEIVABLEACCTNAME>
        </entityacctoverride>
        <entityacctoverride>
            <RECORDNO>1</RECORDNO>
            <SOURCEENTITYID>Mountain Region</SOURCEENTITYID>
            <SOURCEENTITYKEY>3</SOURCEENTITYKEY>
            <SOURCEENTITYNAME>Mountain Region</SOURCEENTITYNAME>
            <SOURCEENTITYSTATUS>T</SOURCEENTITYSTATUS>
            <TARGETENTITYID>Central Region</TARGETENTITYID>
            <TARGETENTITYKEY>4</TARGETENTITYKEY>
            <TARGETENTITYNAME>Central Region</TARGETENTITYNAME>
            <TARGETENTITYSTATUS>T</TARGETENTITYSTATUS>
            <IEPAYABLEACCTKEY>163</IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO>2040</IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME>Checking - Western Region</IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY>164</IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO>1040</IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME>Checking - Mountain Region</IERECEIVABLEACCTNAME>
        </entityacctoverride>
        <entityacctoverride>
            <RECORDNO>5</RECORDNO>
            <SOURCEENTITYID>Western Region</SOURCEENTITYID>
            <SOURCEENTITYKEY>2</SOURCEENTITYKEY>
            <SOURCEENTITYNAME>Western Region</SOURCEENTITYNAME>
            <SOURCEENTITYSTATUS>T</SOURCEENTITYSTATUS>
            <TARGETENTITYID>Central Region</TARGETENTITYID>
            <TARGETENTITYKEY>4</TARGETENTITYKEY>
            <TARGETENTITYNAME>Central Region</TARGETENTITYNAME>
            <TARGETENTITYSTATUS>T</TARGETENTITYSTATUS>
            <IEPAYABLEACCTKEY>63</IEPAYABLEACCTKEY>
            <IEPAYABLEACCTNO>3000</IEPAYABLEACCTNO>
            <IEPAYABLEACCTNAME>Capital Stock</IEPAYABLEACCTNAME>
            <IERECEIVABLEACCTKEY>160</IERECEIVABLEACCTKEY>
            <IERECEIVABLEACCTNO>1040</IERECEIVABLEACCTNO>
            <IERECEIVABLEACCTNAME>Checking - Corporate (San Jose)</IERECEIVABLEACCTNAME>
        </entityacctoverride>
    </ENTITYACCTOVERRIDES>
</INTERENTITYSETUP>
```

* * *

Update the Inter-Entity Configuration
-------------------------------------

How you designate payable and receivable accounts for inter-entity transactions depends on your inter-entity configuration.

### Basic Configuration

With basic configuration, you provide one default inter-entity receivable (IER) account and one default inter-entity payable (IEP) account for each entity in a single ENTITYACCTDEFAULT object.

*   To create a new pair of default accounts, provide an ENTITYACCTDEFAULT for an entity ID that doesn’t currently have default accounts.
*   To update an existing pair of default accounts, provide the record numbers of the existing ENTITYACCTDEFAULT objects and the entity IDs, but with different IER and IEP accounts. You must provide two accounts, so if you only want to change one, include the changed one and the one you want to keep. Any existing defaults not specified in the update remain untouched.
*   To delete a default pair of accounts, provide the record number of the existing ENTITYACCTDEFAULT objects with null values for both accounts in the ENTITYACCTDEFAULT object. Alternatively, you can use the [delete](https://developer.intacct.com/api/company-console/iet-configuration/#delete-inter-entity-account-default) function.

### Advanced Configuration

With advanced configuration, you create a relationship between two entities using a pair of ENTITYACCTOVERRIDE objects. Each ENTITYACCOVERRIDE object provides the IER and IEP account for the entity on one side of the relationship. The accounts will be used when transferring back and forth between these two entities.

*   To create a relationship, provide an ENTITYACCTOVERRIDE for each side of a new relationship between two entities. Two ENTITYACCTOVERRIDE objects must be supplied when creating a new relationship.
*   To update an existing relationship, supply both sides of the relationship as ENTITYACCTOVERRIDE objects and include their record numbers and the other fields. You must provide two ENTITYACCTOVERRIDE objects, so if you only want to change one, include the changed one and the one you want to keep. Any existing relationships not specified in the update remain untouched.
*   To delete an existing relationship, provide both involved ENTITYACCTOVERRIDE objects by record number and provide null values for both accounts for either one of these two objects (it doesn’t matter which one—the entire relationship will be delted).

#### `update`

> Provides a new default account and updates an existing default account for a company with basic configuration:

```
<update>
    <INTERENTITYSETUP>
        <RECORDNO>1</RECORDNO>
        <ENTITYACCTDEFAULTS>
            <ENTITYACCTDEFAULT>
                <ENTITYID>Central Region, South</ENTITYID>
                <IEPAYABLEACCTNO>2030</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1027</IERECEIVABLEACCTNO>
            </ENTITYACCTDEFAULT>
            <ENTITYACCTDEFAULT>
                <RECORDNO>5</RECORDNO>
                <ENTITYID>Eastern Region</ENTITYID>
                <IEPAYABLEACCTNO>2010</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1010</IERECEIVABLEACCTNO>
            </ENTITYACCTDEFAULT>
        </ENTITYACCTDEFAULTS>
    </INTERENTITYSETUP>
</update>
```

> Creates a relationship between two entities for a company with advanced configuration:

```
<update>
    <INTERENTITYSETUP>
        <RECORDNO>1</RECORDNO>
        <ENTITYACCTOVERRIDES>
            <ENTITYACCTOVERRIDE>
                <SOURCEENTITYID>Central Region</SOURCEENTITYID>
                <TARGETENTITYID>Mountain Region</TARGETENTITYID>
                <IEPAYABLEACCTNO>2000</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1000</IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
            <ENTITYACCTOVERRIDE>
                <SOURCEENTITYID>Mountain Region</SOURCEENTITYID>
                <TARGETENTITYID>Central Region</TARGETENTITYID>
                <IEPAYABLEACCTNO>2010</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1010</IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
        </ENTITYACCTOVERRIDES>
    </INTERENTITYSETUP>
</update>
```

> Adds a new relationship and updates an existing relationship for a company with advanced configuration:

```
<update>
    <INTERENTITYSETUP>
        <RECORDNO>1</RECORDNO>
        <ENTITYACCTOVERRIDES>
            <ENTITYACCTOVERRIDE>
                <SOURCEENTITYID>Central Region 2</SOURCEENTITYID>
                <TARGETENTITYID>Western Region 2</TARGETENTITYID>
                <IEPAYABLEACCTNO>2007</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1003</IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
            <ENTITYACCTOVERRIDE>
                <SOURCEENTITYID>Western Region 2</SOURCEENTITYID>
                <TARGETENTITYID>Central Region 2</TARGETENTITYID>
                <IEPAYABLEACCTNO>2010</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1010</IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
            <ENTITYACCTOVERRIDE>
                <RECORDNO>2</RECORDNO>
                <SOURCEENTITYID>Central Region</SOURCEENTITYID>
                <TARGETENTITYID>Mountain Region</TARGETENTITYID>
                <IEPAYABLEACCTNO>2000</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1005</IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
            <ENTITYACCTOVERRIDE>
                <RECORDNO>1</RECORDNO>
                <SOURCEENTITYID>Mountain Region</SOURCEENTITYID>
                <TARGETENTITYID>Central Region</TARGETENTITYID>
                <IEPAYABLEACCTNO>2020</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1010</IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
        </ENTITYACCTOVERRIDES>
    </INTERENTITYSETUP>
</update>
```

> Deletes a relationship between two entities for a company with advanced configuration:

```
<update>
    <INTERENTITYSETUP>
        <RECORDNO>1</RECORDNO>
        <ENTITYACCTOVERRIDES>
            <ENTITYACCTOVERRIDE>
                <RECORDNO>2</RECORDNO>
                <SOURCEENTITYID>Central Region</SOURCEENTITYID>
                <TARGETENTITYID>Mountain Region</TARGETENTITYID>
                <IEPAYABLEACCTNO></IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO></IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
            <ENTITYACCTOVERRIDE>
                <RECORDNO>1</RECORDNO>
                <SOURCEENTITYID>Mountain Region</SOURCEENTITYID>
                <TARGETENTITYID>Central Region</TARGETENTITYID>
                <IEPAYABLEACCTNO>2010</IEPAYABLEACCTNO>
                <IERECEIVABLEACCTNO>1010</IERECEIVABLEACCTNO>
            </ENTITYACCTOVERRIDE>
        </ENTITYACCTOVERRIDES>
    </INTERENTITYSETUP>
</update>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| `INTERENTITYSETUP` | Required | object | Object to update |

`INTERENTITYSETUP`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | Use 1 |
| ENTITYACCTDEFAULTS | Optional | `ENTITYACCTDEFAULT[0..n]` | Basic inter-entity default accounts. Required if using basic configuration. |
| ENTITYACCTOVERRIDES | Optional | `ENTITYACCTOVERRIDE[0..n]` | Advanced inter-entity relationships between entities. Required if using advanced configuration. |

`ENTITYACCTDEFAULT`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Required if updating an existing entity account default |
| ENTITYID | Required | string | ID of the entity |
| IEPAYABLEACCTNO | Required | string | Account number for the IE payable account |
| IERECEIVABLEACCTNO | Required | string | Account number for the IE receivable account |

`ENTITYACCTOVERRIDE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Optional | integer | Required if updating an existing entity account override |
| SOURCEENTITYID | Required | string | ID of the source entity |
| TARGETENTITYID | Required | string | ID of the target entity |
| IEPAYABLEACCTNO | Required | string | Account number for the IE payable account for the source entity. Provide an empty value to delete the relationship on both sides. |
| IERECEIVABLEACCTNO | Required | string | Account number for the IE receivable account for the source entity. Provide an empty value to delete the relationship on both sides. |

* * *

Delete Inter-Entity Account Default
-----------------------------------

#### `delete`

```
<delete>
    <object>ENTITYACCTDEFAULT</object>
    <keys>9</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ENTITYACCTDEFAULT` |
| keys | Required | string | Comma-separated list of entity account default to delete |

* * *

Delete Inter-Entity Account Override
------------------------------------

#### `delete`

```
<delete>
    <object>ENTITYACCTOVERRIDE</object>
    <keys>10</keys>
</delete>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `ENTITYACCTOVERRIDE` |
| keys | Required | string | Comma-separated list of entity account override to delete |

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

