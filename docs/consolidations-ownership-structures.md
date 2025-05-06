Title: Ownership Structures

URL Source: https://developer.intacct.com/api/consolidations/ownership-structures/

Markdown Content:
*   [Ownership Structure Object](https://developer.intacct.com/api/consolidations/ownership-structures/#ownership-structure-object)
    *   [Get Ownership Structure Object Definition](https://developer.intacct.com/api/consolidations/ownership-structures/#get-ownership-structure-object-definition)
    *   [Query and List Ownership Structures](https://developer.intacct.com/api/consolidations/ownership-structures/#query-and-list-ownership-structures)
    *   [Get an Ownership Structure](https://developer.intacct.com/api/consolidations/ownership-structures/#get-an-ownership-structure)
    *   [Get Ownership Structure by ID](https://developer.intacct.com/api/consolidations/ownership-structures/#get-ownership-structure-by-id)
    *   [Create Ownership Structure](https://developer.intacct.com/api/consolidations/ownership-structures/#create-ownership-structure)
    *   [Update Ownership Structure](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-structure)
    *   [Delete Ownership Structure](https://developer.intacct.com/api/consolidations/ownership-structures/#delete-ownership-structure)
*   [Ownership Structure Detail Object](https://developer.intacct.com/api/consolidations/ownership-structures/#ownership-structure-detail-object)
    *   [Query and List Ownership Structure Details](https://developer.intacct.com/api/consolidations/ownership-structures/#query-and-list-ownership-structure-details)
    *   [Get Ownership Structure Detail](https://developer.intacct.com/api/consolidations/ownership-structures/#get-ownership-structure-detail)
    *   [Create Ownership Structure Detail](https://developer.intacct.com/api/consolidations/ownership-structures/#create-ownership-structure-detail)
    *   [Update Ownership Structure Detail](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-structure-detail)
    *   [Delete Ownership Structure Detail](https://developer.intacct.com/api/consolidations/ownership-structures/#delete-ownership-structure-detail)
*   [Ownership Entity Object](https://developer.intacct.com/api/consolidations/ownership-structures/#ownership-entity-object)
    *   [Query and List Ownership Entities](https://developer.intacct.com/api/consolidations/ownership-structures/#query-and-list-ownership-entities)
    *   [Get an Ownership Entity](https://developer.intacct.com/api/consolidations/ownership-structures/#get-an-ownership-entity)
    *   [Create Ownership Entities](https://developer.intacct.com/api/consolidations/ownership-structures/#create-ownership-entities)
    *   [Update Ownership Entities](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-entities)
    *   [Delete Ownership Entity](https://developer.intacct.com/api/consolidations/ownership-structures/#delete-ownership-entity)
*   [Ownership Child Entity Object](https://developer.intacct.com/api/consolidations/ownership-structures/#ownership-child-entity-object)
    *   [Query and List Ownership Child Entities](https://developer.intacct.com/api/consolidations/ownership-structures/#query-and-list-ownership-child-entities)
    *   [Get an Ownership Child Entity](https://developer.intacct.com/api/consolidations/ownership-structures/#get-an-ownership-child-entity)
    *   [Create Child Ownership Entities](https://developer.intacct.com/api/consolidations/ownership-structures/#create-child-ownership-entities)
    *   [Update Ownership Entities](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-entities-1)
    *   [Delete Ownership Child Entity](https://developer.intacct.com/api/consolidations/ownership-structures/#delete-ownership-child-entity)

* * *

Use an ownership structure to define the relationships among entities in your multi-entity company during a given period. For example, suppose your multi-entity company includes entity E100, which owns entities E200 and E300. Entity E400 is 60% owned by the company. You can define all of these entities and their relationships using ownership structures.

*   The `GCOWNERSHIPSTRUCTURE` object defines the name of the structure and its accounting method. The structure is used in [ownership structure consolidation](https://developer.intacct.com/api/consolidations/ownership-structure-consolidations/).

*   The `GCOWNERSHIPSTRUCTUREDETAIL` object sets the start period of the ownership structure and contains an array of owned `GCOWNERSHIPENTITY` objects.
    *   Each `GCOWNERSHIPENTITY` object defines the parent entities and books of an ownership structure, and contains an array of `GCOWNERSHIPCHILDENTITY` objects.
        *   A `GCOWNERSHIPCHILDENTITY` object defines a single subsidiary (“child”) entity and its ownership percentage.

Note that a parent entity can also be a child of another entity.

* * *

Ownership Structure Object
--------------------------

The `GCOWNERSHIPSTRUCTURE` object defines the name of the structure, its accounting method, and its status. The makeup of the structure is defined in `GCOWNERSHIPSTRUCTUREDETAIL` objects.

### Get Ownership Structure Object Definition

#### `lookup`

> List all the fields and relationships for the Ownership Structure object:

```
<lookup>
    <object>GCOWNERSHIPSTRUCTURE</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTURE` |

* * *

### Query and List Ownership Structures

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, structure name, description, and source book ID for each ownership structure:

```
<query>
  <object>GCOWNERSHIPSTRUCTURE</object>
  <select>
    <field>RECORDNO</field>
    <field>STRUCTURENAME</field>
    <field>DESCRIPTION</field>
    <field>SOURCEBOOKID</field>
  </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTURE` |
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

### Get an Ownership Structure

Returns the details of a single ownership structure that is specified by a `RECORDNO`.

#### `read`

```
<read>
    <object>GCOWNERSHIPSTRUCTURE</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTURE` |
| keys | Required | string | The `RECORDNO` of the ownership structure to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |

* * *

### Get Ownership Structure by ID

Returns the details of a single ownership structure that is specified by its structure name.

#### `readByName`

```
<readByName>
    <object>GCOWNERSHIPSTRUCTURE</object>
    <keys>tier 2</keys>
    <fields>*</fields>
</readByName>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTURE` |
| keys | Required | string | Name of the ownership structure. 20 character limit. |
| fields | Optional | string | Comma-separated list of fields on the object to get. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |

* * *

### Create Ownership Structure

#### `create`

```
<create>
  <GCOWNERSHIPSTRUCTURE>
    <STRUCTURENAME>North American Entities</STRUCTURENAME>
    <DESCRIPTION>All entities in North America</DESCRIPTION>
    <AUTOELIMINATION>true</AUTOELIMINATION>
    <SOURCEBOOKID>ACCRUAL</SOURCEBOOKID>
    <STATUS>active</STATUS>
  </GCOWNERSHIPSTRUCTURE>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCOWNERSHIPSTRUCTURE | Required | object | Object to create |

`GCOWNERSHIPSTRUCTURE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STRUCTURENAME | Required | string | Name of the ownership structure. Use 20 characters or fewer. |
| DESCRIPTION | Optional | string | Description |
| AUTOELIMINATION | Optional | boolean | Use `true` to indicate that the consolidation books of the structure should automatically clear inter-entity balances. Automatically clearing inter-entity balances means that transactions between entities do not affect reporting in the consolidated book. Otherwise, use `false` (default). |
| SOURCEBOOKID | Optional | enum | Accounting method of the consolidation books.
*   `ACCRUAL` (default)
*   `CASH`

If company is not operating multi-book, the value defaults to the company’s default book. |
| STATUS | Optional | string | Status of the ownership structure. Options are:

*   `active` (default)
*   `inactive`

Consolidations cannot be run on inactive structures. |

* * *

### Update Ownership Structure

#### `update`

```
<update>
    <GCOWNERSHIPSTRUCTURE>
        <RECORDNO>21</RECORDNO>
        <DESCRIPTION>Europe Group 2</DESCRIPTION>
    </GCOWNERSHIPSTRUCTURE>
 </update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCOWNERSHIPSTRUCTURE | Required | object | Object to update |

`GCOWNERSHIPSTRUCTURE`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| RECORDNO | Required | integer | ID of the ownership structure to update. |
| STRUCTURENAME | Required | string | Name of the ownership structure. Use 20 characters or fewer. |
| DESCRIPTION | Optional | string | Description. |
| AUTOELIMINATION | Optional | boolean | Use `true` to indicate that the consolidation books of the structure should automatically clear inter-entity balances. Automatically clearing inter-entity balances means that transactions between entities do not affect reporting in the consolidated book. Otherwise, use `false` (default). |
| SOURCEBOOKID | Optional | enum | Accounting method of the consolidation books.
*   `ACCRUAL` (default)
*   `CASH`

If company is not operating multi-book, the value defaults to the company’s default book. |
| STATUS | Optional | string | Status of the ownership structure. Options are:

*   `active` (default)
*   `inactive`

Consolidations cannot be run on inactive structures. |

* * *

### Delete Ownership Structure

#### `delete`

```
<delete>
    <object>GCOWNERSHIPSTRUCTURE</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTURE`. |
| keys | Required | string | `RECORDNO` of the ownership structure to delete. |

* * *

Ownership Structure Detail Object
---------------------------------

The `GCOWNERSHIPSTRUCTUREDETAIL` object sets the start period of the consolidation and contains an array of owned [`GCOWNERSHIPENTITY`](https://developer.intacct.com/api/consolidations/ownership-structures/#create-GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITY) objects that define the parent entities and associated books of the structure.

#### Get Ownership Structure Detail Object Definition

#### `lookup`

> List all the fields and relationships for the Ownership Structure Detail object:

```
<lookup>
    <object>GCOWNERSHIPSTRUCTUREDETAIL</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTUREDETAIL` |

* * *

### Query and List Ownership Structure Details

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, structure name, from period, status, and state for each ownership structure detail:

```
<query>
  <object>GCOWNERSHIPSTRUCTUREDETAIL</object>
  <select>
    <field>RECORDNO</field>
    <field>STRUCTURENAME</field>
    <field>FROMPERIOD</field>
    <field>STATUS</field>
    <field>STATE</field>
  </select>
</query>
```

> Find all ownership structure details objects that link to a specific ownership structure:

```
<query>
  <object>GCOWNERSHIPSTRUCTUREDETAIL</object>
  <filter>
    <equalto>
      <field>STRUCTURENAME</field>
      <value>My Structure Name</value>
    </equalto>
  </filter>
  <select>
    <field>RECORDNO</field>
    <field>STRUCTURENAME</field>
    <field>FROMPERIOD</field>
    <field>STATUS</field>
    <field>STATE</field>
  </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTUREDETAIL` |
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

### Get Ownership Structure Detail

Returns all information about a single ownership structure detail object that is specified by `RECORDNO`.

#### `read`

```
<read>
    <object>GCOWNERSHIPSTRUCTUREDETAIL</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTUREDETAIL` |
| keys | Required | string | Ownership structure detail `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |

* * *

### Create Ownership Structure Detail

#### `create`

```
<create>
  <GCOWNERSHIPSTRUCTUREDETAIL>
    <STRUCTURENAME>Strucutre 1</STRUCTURENAME>
    <STATE>Draft</STATE>
    <FROMPERIOD>01/01/2022</FROMPERIOD>
    <GCOWNERSHIPENTITIES>
      <GCOWNERSHIPENTITY>
        <PARENTENTITYID>1</PARENTENTITYID>
        <BOOK>
            <BOOKID>BOOK_1</BOOKID>
            <BOOKDESCRIPTION>Parent entity : 1 book</BOOKDESCRIPTION>
            <CURRENCY>USD</CURRENCY>
            <CTANETASSETACCOUNTNO>1001</CTANETASSETACCOUNTNO>
            <CTANETINCOMEACCOUNTNO>1000</CTANETINCOMEACCOUNTNO>
            <BOOKSTATJOURNALSYMBOL>BOOK_1_SJ</BOOKSTATJOURNALSYMBOL>
            <BOOKSTATJOURNALTITLE>BOOK_1 statistical journal</BOOKSTATJOURNALTITLE>
            <BSTRANMETHOD>Ending spot rate</BSTRANMETHOD>
            <ISTRANMETHOD>Weighted average rate</ISTRANMETHOD>
            <EENAME>USDE</EENAME>
            <ELIMINATIONADJACCT></ELIMINATIONADJACCT>
            <BOOKJOURNALSYMBOL>BOOK_1</BOOKJOURNALSYMBOL>
            <BOOKJOURNALTITLE>BOOK_1</BOOKJOURNALTITLE>
          </BOOK>
        <GCOWNERSHIPCHILDENTITIES>
          <GCOWNERSHIPCHILDENTITY>
            <ENTITYID>2</ENTITYID>
            <OWNERSHIPPERCENTAGE>50</OWNERSHIPPERCENTAGE>
          </GCOWNERSHIPCHILDENTITY>
          <GCOWNERSHIPCHILDENTITY>
            <ENTITYID>3</ENTITYID>
            <OWNERSHIPPERCENTAGE>20</OWNERSHIPPERCENTAGE>
          </GCOWNERSHIPCHILDENTITY>
        </GCOWNERSHIPCHILDENTITIES>
      </GCOWNERSHIPENTITY>
    </GCOWNERSHIPENTITIES>
  </GCOWNERSHIPSTRUCTUREDETAIL>
</create>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCOWNERSHIPSTRUCTUREDETAIL | Required | object | Object to create |

`GCOWNERSHIPSTRUCTUREDETAIL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STRUCTURENAME | Required | string | Name of the ownership structure. Use 20 characters or fewer. |
| FROMPERIOD | Required | string | Date that this ownership structure took effect. |
| COMMENT | Optional | string | Description of the structure detail. |
| STATE | Optional | string | The state of the period.
*   `draft` (default)
*   `activated`
*   `review`

 |
| STATUS | Optional | string | Status of the ownership structure. Options are:

*   `active` (default)
*   `inactive`

Consolidations cannot be run on inactive structures. |
| GCOWNERSHIPENTITIES | Required | array of [`GCOWNERSHIPENTITY`](https://developer.intacct.com/api/consolidations/ownership-structures/#create-GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITY) | Defines the parent entities and associated books of the structure. |

* * *

`GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| PARENTENTITYID | Required | string | The ID of the parent [entity](https://developer.intacct.com/api/company-console/entities/) in an ownership structure. |
| BOOK | Required | [BOOK object](https://developer.intacct.com/api/consolidations/ownership-structures/#create-GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITY.BOOK) | Use 12 characters or fewer. |
| GCOWNERSHIPCHILDENTITIES | Required | array of [`GCOWNERSHIPCHILDENTITY`](https://developer.intacct.com/api/consolidations/ownership-structures/#create-GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITY.GCOWNERSHIPCHILDENTITY) | Child entities of a parent entity. |

`GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.BOOK`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| BOOKID | Required | string | Tier consolidation book ID. |
| CTANETASSETACCOUNTNO | Required | string | Net income account number for currency exchange gain/loss. |
| CTANETINCOMEACCOUNTNO | Required | string | Net assets account number for currency exchange gain/loss. |
| EENAME | Required | string | Elimination entity name. |
| ELIMINATIONADJACCT | Required | string | Elimination adjustment account. |
| BOOKDESCRIPTION | Optional | string | Description of the tier consolidation book. |
| CURRENCY | Optional | string | Currency code to use in reporting. (Default: Parent entity base currency.) |
| BOOKSTATJOURNALSYMBOL | Optional | string | Statistical journal symbol. Use 16 characters or fewer. (Default value is Book ID.) |
| BOOKSTATJOURNALTITLE | Optional | string | Statistical journal title. Use 40 characters or fewer. (Default value is Book ID.) |
| BSTRANMETHOD | Optional | string | Translation method for balance sheet accounts. (Default: `Ending spot rate`.) |
| ISTRANMETHOD | Optional | string | Translation method for income statement. (Default: `weighted average`.) |
| BOOKJOURNALSYMBOL | Optional | string | Default statistical journal symbol. Use 16 characters or fewer. (Default value is Book ID.) |
| BOOKJOURNALTITLE | Optional | string | Statistical journal title. Use 40 characters or fewer. (Default value is Book ID.) |

`GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITIES.GCOWNERSHIPENTITY.GCOWNERSHIPCHILDENTITY`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| ENTITYID | Required | string | The ID of an [entity](https://developer.intacct.com/api/company-console/entities/). |
| OWNERSHIPPERCENTAGE | Required | decimal | The percentage of the child entity that is owned by the parent entity. |
| CONSOLIDATIONMETHOD | Required | Enum | The consolidation method to use for the entity.
*   `CONSOLIDATION`: If selected then the ownership accounts must be selected.
*   `PROPORTIONAL`: If selected, then indicate the percentage to apply in `OWNERSHIPPERCENTAGE`.
*   `FULL CONSOLIDATION`: Default when `OWNERSHIPPERCENTAGE` is 100.
.

 |

### Update Ownership Structure Detail

Use the `update` request for `GCOWNERSHIPSTRUCTUREDETAIL` objects to update the object itself and to add or update owned `GCOWNERSHIPENTITY` and `GCOWNERSHIPCHILDENTITY` objects.

*   To update an existing `GCOWNERSHIPENTITY` or `GCOWNERSHIPCHILDENTITY` object, include its `RECORDNO` in the request along with the updated field values.
*   To add a new `GCOWNERSHIPENTITY` or `GCOWNERSHIPCHILDENTITY` object, include entity fields in the request without a `RECORDNO`.
*   Any `GCOWNERSHIPENTITY` or `GCOWNERSHIPCHILDENTITY` that are not included in the request are not updated or deleted.

NOTE: Child objects (`GCOWNERSHIPENTITY` and `GCOWNERSHIPCHILDENTITY`) can only be updated from `GCOWNERSHIPSTRUCTUREDETAIL`. Individual update calls on child objects not supported.

You cannot update a `GCOWNERSHIPSTRUCTUREDETAIL` object that has STATE==`activated`. Note that after _running_ a consolidation, the ability to change book setup is largely limited to adding new data, such as a completely new account. You can also modify which dimensions are included.

#### `update`

```
<update>
    <gcownershipstructuredetail>
    <RECORDNO>68</RECORDNO>
    <STRUCTUREKEY>42</STRUCTUREKEY>
    <FROMPERIOD>01/01/2020</FROMPERIOD>
    <COMMENT>update to active</COMMENT>
    <STATE>draft</STATE>
    <STATUS>active</STATUS>
    </gcownershipstructuredetail>
</update>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| GCOWNERSHIPSTRUCTUREDETAIL | Required | object | Object to update |

`GCOWNERSHIPSTRUCTUREDETAIL`

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| STRUCTURENAME | Required | string | Name of the ownership structure. Use 20 characters or fewer. |
| FROMPERIOD | Optional | string | Date that this ownership structure took effect. |
| COMMENT | Optional | string | Description of the structure detail. |
| STATE | Optional | string | The state of the period.
*   `draft` (default)
*   `activated`
*   `review`

 |
| STATUS | Optional | string | Status of the ownership structure. Options are:

*   `active` (default)
*   `inactive`

Consolidations cannot be run on inactive structures. |
| GCOWNERSHIPENTITIES | Required | array of [`GCOWNERSHIPENTITY`](https://developer.intacct.com/api/consolidations/ownership-structures/#create-GCOWNERSHIPSTRUCTUREDETAIL.GCOWNERSHIPENTITY) | Defines the parent entities and associated books of the structure. |

* * *

### Delete Ownership Structure Detail

Deleting the parent object will also deletes the child objects under it.

*   Individual delete calls on child objects are supported.
*   Deleting the parent object deletes the associated book.

#### `delete`

```
<delete>
    <object>GCOWNERSHIPSTRUCTURE</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSTRUCTUREDETAIL` |
| keys | Required | string | `GCOWNERSHIPSTRUCTUREDETAIL` `RECORDNO` to delete. |

* * *

Ownership Entity Object
-----------------------

A `GCOWNERSHIPENTITY` object is owned by a `GCOWNERSHIPSTRUCTUREDETAIL` object and defines the parent entities and associated books of an ownership structure. Each `GCOWNERSHIPENTITY` object contains an array of owned `GCOWNERSHIPCHILDENTITY` objects that define child entities and ownership percentages.

#### Get Ownership Entity Object Definition

#### `lookup`

> List all the fields and relationships for the Ownership Entity object:

```
<lookup>
    <object>GCOWNERSHIPENTITY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPENTITY` |

* * *

### Query and List Ownership Entities

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number and name for each ownership structure:

```
<query>
  <object>GCOWNERSHIPENTITY</object>
  <select>
    <field>RECORDNO</field>
    <field>STRUCTURENAME</field>
  </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSENTITY` |
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

### Get an Ownership Entity

Returns all information about a single ownership entity object that is specified by `RECORDNO`.

#### `read`

```
<read>
    <object>GCOWNERSHIPENTITY</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPSENTITY` |
| keys | Required | string | Ownership entity `RECORDNO` to get |
| fields | Optional | string | Comma-separated list of fields on the object to get. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |

* * *

### Create Ownership Entities

Ownership entity objects can only be created by [creating](https://developer.intacct.com/api/consolidations/ownership-structures/#create-ownership-structure-detail) or [updating an ownership detail object](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-structure-detail).

### Update Ownership Entities

Ownership entity objects can only be updated by [updating the ownership detail object](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-structure-detail).

* * *

### Delete Ownership Entity

Deleting an ownership entity object will also delete all ownership entity child objects beneath it and the associated book. It will also delete the associated book.

#### `delete`

```
<delete>
    <object>GCOWNERSHIPENTITY</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPENTITY` |
| keys | Required | string | Ownership entity `RECORDNO` to delete |

Ownership Child Entity Object
-----------------------------

A `GCOWNERSHIPCHILDENTITY` object is owned by a `GCOWNERSHIPENTITY` object and defines a single child entity and its ownership percentage.

#### Get Ownership Child Entity Object Definition

#### `lookup`

> List all the fields and relationships for the ownership child entity object:

```
<lookup>
    <object>GCOWNERSHIPCHILDENTITY</object>
</lookup>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPCHILDENTITY` |

* * *

### Query and List Ownership Child Entities

#### [`query`](https://developer.intacct.com/web-services/queries/)

> List the record number, structure name, description, and source book ID for each ownership child entity:

```
<query>
  <object>GCOWNERSHIPCHILDENTITY</object>
  <select>
    <field>RECORDNO</field>
    <field>STRUCTURENAME</field>
    <field>FROMPERIOD</field>
    <field>STATUS</field>
    <field>STATE</field>
  </select>
</query>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPCHILDENTITY` |
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

### Get an Ownership Child Entity

Returns all information about a single ownership child entity object that is specified by `RECORDNO`.

#### `read`

```
<read>
    <object>GCOWNERSHIPCHILDENTITY</object>
    <keys>5</keys>
    <fields>*</fields>
</read>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPCHILDENTITY` |
| keys | Required | string | `RECORDNO` of ownership child entity to get. |
| fields | Optional | string | Comma-separated list of fields on the object to get. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide `*` for the value. |

* * *

### Create Child Ownership Entities

Ownership child entity objects can only be created by [creating](https://developer.intacct.com/api/consolidations/ownership-structures/#create-ownership-structure-detail) or [updating an ownership detail object](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-structure-detail).

### Update Ownership Entities

Ownership child entity objects can only be updated by [updating the ownership detail object](https://developer.intacct.com/api/consolidations/ownership-structures/#update-ownership-structure-detail).

* * *

### Delete Ownership Child Entity

*   #### `delete`
    

```
<delete>
    <object>GCOWNERSHIPCHILDENTITY</object>
    <keys>112</keys>
</delete>
```

##### Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| object | Required | string | Use `GCOWNERSHIPCHILDENTITY` |
| keys | Required | string | `RECORDNO` of ownership child entity to delete. |

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

