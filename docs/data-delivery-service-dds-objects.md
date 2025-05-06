Title: DDS Objects

URL Source: https://developer.intacct.com/api/data-delivery-service/dds-objects/

Markdown Content:
*   [List DDS Objects](https://developer.intacct.com/api/data-delivery-service/dds-objects/#list-dds-objects)
*   [Get DDS Object Data Definition Language](https://developer.intacct.com/api/data-delivery-service/dds-objects/#get-dds-object-data-definition-language)

* * *

DDS objects are selected as part of setting up an automated DDS run or processing a manual run.

* * *

List DDS Objects
----------------

Lists all objects, both standard and custom, available for use in a DDS job.

#### `getDdsObjects`

```
<getDdsObjects/>
```

#### Parameters

No parameters

* * *

Get DDS Object Data Definition Language
---------------------------------------

The Data Definition Language (DDL) returned is currently compatible with PostgreSQL databases.

#### `getDdsDdl`

```
<getDdsDdl>
    <object>CUSTOMER</object>
</getDdsDdl>
```

#### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Object type to get. |

> The above function returns data structured like this:

```
<DdsDdl>
    <Ddl>
        create table CUSTOMER (
        RECORDNO integer,
        CUSTOMERID varchar,
        NAME varchar,
        ENTITY varchar,
        TERMNAME varchar,
        RESALENO varchar,
        ...
        MODIFIEDBY integer,
        MEGAENTITYKEY integer,
        MEGAENTITYID varchar,
        MEGAENTITYNAME varchar,
        WEBSITE varchar,
        ddsReadTime timestamp);
        
        alter table CUSTOMER add constraint PK_CUSTOMER primary key(CUSTOMERID);
        -- Link column PARENTKEY to CUSTOMER.RECORDNO;
        -- Link column SHIPTOKEY to CONTACT.RECORDNO;
        -- Link column BILLTOKEY to CONTACT.RECORDNO;
        -- Link column DISPLAYCONTACTKEY to CONTACT.RECORDNO;
        -- Link column CONTACTKEY to CONTACT.RECORDNO;
        -- Link column ACCOUNTKEY to GLACCOUNT.RECORDNO;
        -- Link column CUSTTYPEKEY to CUSTTYPE.RECORDNO;
        -- Link column MEGAENTITYKEY to LOCATION.RECORDNO;
        
    </Ddl>
</DdsDdl>
```

**Note:** You can also access the DDL for an object from the UI. Choose **Platform Services \> Objects \> _object_** and look at the bottom of the page.

* * *

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

