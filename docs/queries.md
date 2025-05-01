Title: Queries

URL Source: https://developer.intacct.com/web-services/queries/

Markdown Content:
*   [Overview](https://developer.intacct.com/web-services/queries/#overview)
*   [Advantages of query](https://developer.intacct.com/web-services/queries/#advantages-of-query)
*   [Using query](https://developer.intacct.com/web-services/queries/#using-query)
    *   [Building more complex queries](https://developer.intacct.com/web-services/queries/#building-more-complex-queries)
    *   [Finding an object’s queryable fields and values](https://developer.intacct.com/web-services/queries/#finding-an-objects-queryable-fields-and-values)
    *   [Query on a field value](https://developer.intacct.com/web-services/queries/#query-on-a-field-value)
    *   [Query on a field value of a related object](https://developer.intacct.com/web-services/queries/#query-on-a-field-value-of-a-related-object)
    *   [Support for custom objects and relationships](https://developer.intacct.com/web-services/queries/#support-for-custom-objects-and-relationships)
    *   [Query capabilities](https://developer.intacct.com/web-services/queries/#query-capabilities)
    *   [Examples](https://developer.intacct.com/web-services/queries/#examples)
    *   [Schema definition](https://developer.intacct.com/web-services/queries/#schema-definition)
    *   [Elements of the query](https://developer.intacct.com/web-services/queries/#elements-of-the-query)
    *   [Tips](https://developer.intacct.com/web-services/queries/#query-tips)
*   [Using readByQuery (legacy)](https://developer.intacct.com/web-services/queries/#using-readbyquery-legacy)
    *   [Limit fields returned to improve performance](https://developer.intacct.com/web-services/queries/#limit-fields-returned-to-improve-performance)
    *   [Use rownum to specify the rows that readByQuery returns](https://developer.intacct.com/web-services/queries/#use-rownum-to-specify-the-rows-that-readbyquery-returns)
    *   [Paginate results](https://developer.intacct.com/web-services/queries/#paginate-results)
    *   [Supported operators](https://developer.intacct.com/web-services/queries/#supported-operators)
    *   [Operands](https://developer.intacct.com/web-services/queries/#operands)
    *   [Illegal characters in XML](https://developer.intacct.com/web-services/queries/#illegal-characters-in-xml)
    *   [Examples](https://developer.intacct.com/web-services/queries/#examples-1)
    *   [Tips](https://developer.intacct.com/web-services/queries/#readByQuery-tips)

* * *

You can query the data in a Sage Intacct company to return a list of objects that match given conditions.

Overview
--------

There are two functions for performing queries on standard and custom objects:

*   `query` is a newer function that accepts query and filter expressions composed of XML elements with a well-defined [schema](https://developer.intacct.com/web-services/queries/#schema-definition). This function supports complex queries with multiple conditions.
*   `readByQuery` is a legacy function that accepts a simple string for the query definition.

Here’s a comparison of the two functions performing the same query to find all bills for a vendor that is specified by name:

![Image 1: side-by-side comparision of query and readByQuery functions](https://developer.intacct.com/images/web-services/queryFunctionComparison.png)

* * *

Advantages of query
-------------------

The `query` function provides several advantages over the `readByQuery` function:

*   More operators are supported.
*   You can get the values for fields on related objects and/or use them in filters.
*   You can return the queryable fields and relationships with the `lookup` function.
*   You can perform case-insensitive queries.
*   Building complex query statements is less error-prone and error checking is more robust.
*   You can sort results.
*   You can perform aggregate operations such as sum or average.
*   You can get more objects in a response.

* * *

Using query
-----------

Let’s take a closer look at the query that lists AP bills where the vendor name is `Regal Services`.

```
<query>
    <object>APBILL</object>
    <filter>
        <equalto>
            <field>VENDORNAME</field>
            <value>Regal Services</value>
        </equalto>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
    </select>
</query>
```

*   The type of object that you’re looking for is specified by the `object` element, which is `APBILL` in this example.
*   The values that you want to find are listed in the `filter` element. This example uses `equalto` to find all APBILL objects in which the `VENDORNAME` field is equal to `Regal Services`.
*   The fields to include in the response are specified in the `select` element.

The response might look like this:

```
<data listtype="APBILL" totalcount="2" offset="0" count="2" numremaining="0">
    <APBILL>
        <RECORDNO>208</RECORDNO>
        <VENDORNAME>Regal Services</VENDORNAME>
    </APBILL>
    <APBILL>
        <RECORDNO>227</RECORDNO>
        <VENDORNAME>Regal Services</VENDORNAME>
    </APBILL>
</data>
```

### Building more complex queries

While simple queries like the one shown above are useful, you can use the `query` and `lookup` functions to create more complex queries based on field values and [object relationships](https://developer.intacct.com/web-services/queries/#query-on-a-field-value-of-a-related-object).

### Finding an object’s queryable fields and values

Use the `lookup` function to find all of an object’s queryable fields, their data types, valid values (for enums) and relationships to other objects. You can use any of those within the `select` and/or `filter` elements of a query. `lookup` works with both standard and custom objects.

The following shows an excerpt from the response of a `lookup` on the journal entry object, GLBATCH. Note all the information provided for the fields, including any valid values for enum fields. [Relationships that can be queried](https://developer.intacct.com/web-services/queries/#query-on-a-field-value-of-a-related-object) are listed after the fields.

```
<lookup>
    <object>GLBATCH</object>
</lookup>
```

Response:

```
<Type Name="GLBATCH" DocumentType="">
    <Fields>
        <Field>
            <ID>RECORDNO</ID>
            <LABEL>Record number</LABEL>
            <DESCRIPTION>Record Number</DESCRIPTION>
            <REQUIRED>false</REQUIRED>
            <READONLY>false</READONLY>
            <DATATYPE>INTEGER</DATATYPE>
            <ISCUSTOM>false</ISCUSTOM>
        </Field>
        ...
        <Field>
            <ID>STATE</ID>
            <LABEL>State</LABEL>
            <DESCRIPTION></DESCRIPTION>
            <REQUIRED>true</REQUIRED>
            <READONLY>false</READONLY>
            <DATATYPE>TEXT</DATATYPE>
            <VALIDVALUES>
                <VALIDVALUE>Draft</VALIDVALUE>
                <VALIDVALUE>Submitted</VALIDVALUE>
                <VALIDVALUE>Partially Approved</VALIDVALUE>
                <VALIDVALUE>Approved</VALIDVALUE>
                <VALIDVALUE>Posted</VALIDVALUE>
                <VALIDVALUE>Declined</VALIDVALUE>
                <VALIDVALUE>Reversal pending</VALIDVALUE>
                <VALIDVALUE>Reversed</VALIDVALUE>
            </VALIDVALUES>
            <ISCUSTOM>false</ISCUSTOM>
        </Field>
        ...
    </Fields>
 ...
    <Relationships>
        <Relationship>
            <OBJECTPATH>JOURNAL</OBJECTPATH>
            <OBJECTNAME>JOURNAL</OBJECTNAME>
            <LABEL></LABEL>
            <RELATIONSHIPTYPE>MANY2ONE</RELATIONSHIPTYPE>
            <RELATEDBY>JOURNAL</RELATEDBY>
        </Relationship>
        ...
    </Relationships>
</Type>
```

### Query on a field value

After using lookup, you can easily compose a query based on the output. Continuing with the example, you can now query for posted entries using one of the valid values for the `STATE` field:

```
<query>
    <object>GLBATCH</object>
    <filter>
        <equalto>
            <field>STATE</field>
            <value>Posted</value>
        </equalto>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
</query>
```

You can access the value of a field on a many-to-one related object that was returned by `lookup`.

Continuing with the example, assume you want to know the journal symbol for each listed journal entry. After running a separate `lookup` on the JOURNAL object, you learn that one of its queryable fields is `SYMBOL`.

To access the value of the journal’s `SYMBOL` field from within the `GLBATCH` query, provide the `OBJECTPATH` value of the related object (from the GLBATCH `lookup` output above), followed by the dot operator (.), then the name of the field. In our example, this is `JOURNAL.SYMBOL`:

```
<query>
    <object>GLBATCH</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
        <field>JOURNAL.SYMBOL</field>
    </select>
    <filter>
        <equalto>
            <field>JOURNAL.SYMBOL</field>
            <value>APJ</value>
        </equalto>
    </filter>
</query>
```

Response:

```
<data listtype="GLBATCH" totalcount="97" offset="0" count="97" numremaining="0">
   <GLBATCH>
        <RECORDNO>2624</RECORDNO>
        <STATE>Posted</STATE>
        <JOURNAL.SYMBOL>APJ</JOURNAL.SYMBOL>
    </GLBATCH>
    <GLBATCH>
        <RECORDNO>2625</RECORDNO>
        <STATE>Posted</STATE>
        <JOURNAL.SYMBOL>APJ</JOURNAL.SYMBOL>
    </GLBATCH>
    ...
</data>
```

You can query across multiple relationships using multiple dot operators in many cases. For example, the following expression resolves correctly when querying a vendor object:

```
<field>PAYTOCONTACT.MAILADDRESS.ZIP</field>
```

For hierarchical relationships, such as a customer to a parent customer, you can query across one relationship:

```
<field>CUSTOMER.PARENT.NAME</field>
```

Querying across more than one hierarchical relationship is not allowed. The following results in an error:

```
<field>CUSTOMER.PARENT.PARENT.NAME</field>
```

### Support for custom objects and relationships

You can query across custom relationships:

*   Between two custom objects
*   Between one custom and one standard object, or vice versa

Querying across a custom relationship between two standard objects is not supported.

### Query capabilities

Let’s look at the top-level elements of a query to get an idea of everything you can do with this function.

![Image 2: diagram showing high-level schema of query](https://developer.intacct.com/images/web-services/querySchemaSkeletal.png)

* * *

### Examples

The following examples range from simple queries to complex ones that combine multiple queries. Click to view the individual examples or expand them all.

[Expand All](https://developer.intacct.com/web-services/queries/#expAll)

**Lists paid bills, returning the record number, vendor name, and state for each.**

```
<query>
    <object>APBILL</object>
    <filter>
        <equalto>
            <field>STATE</field>
            <value>Paid</value>
        </equalto>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
        <field>STATE</field>
    </select>
</query>
```

**Lists bills where the total due is greater than 500 and sort the results from the highest amount to the lowest.**

```
<query>
    <object>APBILL</object>
    <filter>
        <greaterthan>
            <field>TOTALDUE</field>
            <value>500</value>
        </greaterthan>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>TOTALDUE</field>
    </select>
    <orderby>
        <order>
            <field>TOTALDUE</field>
            <descending />
        </order>
    </orderby>
</query>
```

**Lists bills where the related vendor's credit limit is greater than 50,000. Note the use of the dot operator (`.`) to access the related field.**

```
<query>
    <object>APBILL</object>
    <filter>
        <greaterthan>
            <field>VENDOR.CREDITLIMIT</field>
            <value>50000</value>
        </greaterthan>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
        <field>VENDOR.CREDITLIMIT</field>
    </select>
</query>
```

**Lists bills, showing the due dates for the terms for the related vendors:**

```
<query>
    <object>APBILL</object>
    <select>
        <field>RECORDNO</field>
        <field>VENDOR.TERM.DUEDATE</field>
    </select>
</query>
```

**Lists bill lines where the department ID is in the given set.**

```
<query>
    <object>APBILLITEM</object>
    <filter>
        <in>
            <field>DEPARTMENTID</field>
            <value>04</value>
            <value>05</value>
            <value>06</value>
            <value>07</value>
        </in>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>DEPARTMENTID</field>
    </select>
</query>
```

**Lists bills where the vendor name is `Acme Supply` and the bills were created after 04/26/2021.**

```
<query>
    <object>APBILL</object>
    <filter>
        <and>
            <greaterthanorequalto>
                <field>WHENCREATED</field>
                <value>04/26/2021</value>
            </greaterthanorequalto>
            <notequalto>
                <field>VENDORNAME</field>
                <value>Acme Supply</value>
            </notequalto>
        </and>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORID</field>
        <field>WHENCREATED</field>
    </select>
</query>
```

**Lists bills where the vendor name starts with the letter `B`.**

```
<query>
    <object>APBILL</object>
    <filter>
        <like>
            <field>VENDORNAME</field>
            <value>B%</value>
        </like>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
    </select>
</query>
```

**Lists bills that are due between the given dates. Note that the first date value must be the earlier date:**

```
<query>
    <object>APBILL</object>
    <filter>
        <between>
            <field>WHENDUE</field>
            <value>01/24/2022</value>
            <value>02/24/2022</value>
        </between>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>WHENDUE</field>
    </select>
</query>
```

**Lists bills where the third letter of the vendor name is `n` (note the two underscores before the `n`).**

```
<query>
    <object>APBILL</object>
    <filter>
        <like>
            <field>VENDORNAME</field>
            <value>__n%</value>
        </like>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
    </select>
</query>
```

**Lists bills with empty descriptions.**

```
<query>
    <object>APBILL</object>
    <filter>
        <isnull>
            <field>DESCRIPTION</field>
        </isnull>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
</query>
```

**Lists bills with empty descriptions, skipping the first five results.**

```
<query>
    <object>APBILL</object>
    <filter>
        <isnull>
            <field>DESCRIPTION</field>
        </isnull>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>DESCRIPTION</field>
    </select>
    <offset>5</offset>
</query>
```

**Lists bills where the total due is between 10 and 500 dollars, inclusive.**

```
<query>
    <object>APBILL</object>
    <filter>
        <between>
            <field>TOTALDUE</field>
            <value>10</value>
            <value>500</value>
        </between>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
        <field>TOTALDUE</field>
    </select>
</query>
```

**Lists bills with empty descriptions where either the total due is over 5000 or the payment priority is urgent (or both).**

```
<query>
    <object>APBILL</object>
    <filter>
        <and>
            <isnull>
                <field>DESCRIPTION</field>
            </isnull>
            <or>
                <greaterthan>
                    <field>TOTALDUE</field>
                    <value>5000</value>
                </greaterthan>
                <equalto>
                    <field>PAYMENTPRIORITY</field>
                    <value>urgent</value>
                </equalto>
            </or>
        </and>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>VENDORNAME</field>
        <field>TOTALDUE</field>
        <field>PAYMENTPRIORITY</field>
    </select>
</query>
```

**Lists customers where the value of the `CUSTOM_HEALTH` custom field is `Good`.**

```
<query>
    <object>CUSTOMER</object>
    <filter>
        <equalto>
            <field>CUSTOMER_HEALTH</field>
            <value>Good</value>
        </equalto>
    </filter>
    <select>
        <field>NAME</field>
        <field>CUSTOMER_HEALTH</field>
    </select>
</query>
```

**Lists invoices where the customer ID starts with the letter `c` or `C` and provides a sum of the total due by customer ID. Results are grouped by the first two fields.**

```
<query>
    <object>ARINVOICE</object>
    <filter>
        <like>
            <field>CUSTOMERID</field>
            <value>c%</value>
        </like>
    </filter>
    <select>
        <field>CUSTOMERID</field>
        <field>CUSTOMERNAME</field>
        <sum>TOTALDUE</sum>
    </select>
    <options>
        <caseinsensitive>true</caseinsensitive>
    </options>
</query>

Each entry in the response provides the total due on all invoices for the given customer, for example:

<result>
    <status>success</status>
    ...
    <data listtype="ARINVOICE" totalcount="29" offset="0" count="29" numremaining="0">
        <ARINVOICE>
            <CUSTOMERID>C-00003</CUSTOMERID>
            <CUSTOMERNAME>Burlington Textiles Corp of America</CUSTOMERNAME>
            <TOTALDUE>1679615.93</TOTALDUE>
        </ARINVOICE>
        <ARINVOICE>
            <CUSTOMERID>c-1102</CUSTOMERID>
            <CUSTOMERNAME>Sharpe Interiors</CUSTOMERNAME>
            <TOTALDUE>205375</TOTALDUE>
        </ARINVOICE>
        ...
    </data>
</result>
```

**Lists Order Entry transactions where the transaction definition (`docparid`) is `Sales Order`.**

```
<query>
    <object>SODOCUMENT</object>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
    <docparid>Sales Order</docparid>
</query>
```

**Lists the number of bill records for each vendor.**

```
<query>
    <object>APBILL</object>
    <select>
        <field>VENDORNAME</field>
        <count>RECORDNO</count>
    </select>
</query>

Each entry in the response provides the count of the total number of bill records for the given vendor.
    In this example, there are 5 bill records for Acme Co.


<result>
    <status>success</status>
    ...
    <data listtype="APBILL" totalcount="8" offset="0" count="8" numremaining="0">
        <APBILL>
            <VENDORNAME>Acme Co.</VENDORNAME>
            <COUNT.RECORDNO>5</COUNT.RECORDNO>
        </APBILL>
        <APBILL>
            <VENDORNAME>MYDESK CORPORATION</VENDORNAME>
            <COUNT.RECORDNO>2</COUNT.RECORDNO>
        </APBILL>
        ...
    </data>
</result>
```

**Lists the task ID as well as related field values for each task where the parent project's end date is in the given range.**

```
<query>
    <object>TASK</object>
    <filter>
        <between>
            <field>PROJECT.ENDDATE</field>
            <value>01/01/2018</value>
            <value>01/01/2021</value>
        </between>
    </filter>
    <select>
        <field>TASKID</field>
        <field>NAME</field>
        <field>PROJECT.PROJECTID</field>
        <field>PROJECT.NAME</field>
        <field>PROJECT.CUSTOMER.CUSTOMERID</field>
    </select>
</query>

Sample output:

...
<data listtype="TASK" totalcount="19" offset="0" count="19" numremaining="0">
    <TASK>
        <TASKID>32</TASKID>
        <NAME>Prototyping</NAME>
        <PROJECT.PROJECTID>13</PROJECT.PROJECTID>
        <PROJECT.NAME>Widget Development</PROJECT.NAME>
        <PROJECT.CUSTOMER.CUSTOMERID>A13</PROJECT.CUSTOMER.CUSTOMERID>
        <PROJECT.CUSTOMER.NAME>Acme Electronics Co.</PROJECT.CUSTOMER.NAME>
    </TASK>
    <TASK>
        <TASKID>2</TASKID>
        <NAME>Requirements gathering</NAME>
        <PROJECT.PROJECTID>19</PROJECT.PROJECTID>
        <PROJECT.NAME>Special tools</PROJECT.NAME>
        <PROJECT.CUSTOMER.CUSTOMERID>A17</PROJECT.CUSTOMER.CUSTOMERID>
        <PROJECT.CUSTOMER.NAME>Johnson MFG, Inc.</PROJECT.CUSTOMER.NAME>
    </TASK>
    ...
</data>
```

**Lists AR invoice items where the item ID starts with the letter `B` and the customer has a credit limit within the given range.**

```
<query>
    <object>ARINVOICEITEM</object>
    <filter>
        <and>
            <between>
                <field>ARINVOICE.CUSTOMER.CREDITLIMIT</field>
                <value>500</value>
                <value>10000</value>
            </between>
            <like>
                <field>ITEMID</field>
                <value>B%</value>
            </like>
        </and>
    </filter>
    <select>
        <field>RECORDNO</field>
        <field>ITEMID</field>
        <field>ARINVOICE.CUSTOMERID</field>
        <field>ARINVOICE.CUSTOMER.CREDITLIMIT</field>
    </select>
</query>

Sample output:
...
<data listtype="TASK" totalcount="19" offset="0" count="19" numremaining="0">
    <ARINVOICEITEM>
        <RECORDNO>135</RECORDNO>
        <ITEMID>B02-12</ITEMID>
        <ARINVOICE.CUSTOMERID>C-00003</ARINVOICE.CUSTOMERID>
        <ARINVOICE.CUSTOMER.CREDITLIMIT>5000</ARINVOICE.CUSTOMER.CREDITLIMIT>
    </ARINVOICEITEM>
    <ARINVOICEITEM>
        <RECORDNO>2201</RECORDNO>
        <ITEMID>BB02-14</ITEMID>
        <ARINVOICE.CUSTOMERID>C-00008</ARINVOICE.CUSTOMERID>
        <ARINVOICE.CUSTOMER.CREDITLIMIT>900</ARINVOICE.CUSTOMER.CREDITLIMIT>
    </ARINVOICEITEM>
    ...
</data>
```

**Lists MCA\_attendee custom objects where the related customer (via R\_attendee\_customer relationship) owes more than 5,000.**

```
<query>
    <object>MCA_attendee</object>
    <filter>
        <greaterthan>
            <field>R_attendee_customer.TOTALDUE</field>
            <value>5000</value>
        </greaterthan>
    </filter>
    <select>
        <field>NAME</field>
        <field>R_attendee_customer.CUSTOMERID</field>
    </select>
</query>
```

### Schema definition

The following shows a graphical representation of the schema for the `query` function. The actual XSD in provided after that.

Under the `filter` element, only one top-level operator is allowed. For complex queries, use an `and`/`or` operator at the top level to build expressions with as many conditions as you need.

![Image 3: diagram showing schema of query](https://developer.intacct.com/images/web-services/querySchema.png)

**Complete schema (XSD file)**

```
<xs:element name='query'>
    <xs:complexType>
        <xs:all>
            <xs:element name="select" minOccurs="1" maxOccurs="1">
                <xs:complexType>
                    <xs:choice minOccurs="1" maxOccurs="unbounded">
                        <xs:element name="field"/>
                        <xs:element name="count" />
                        <xs:element name="avg" />
                        <xs:element name="min" />
                        <xs:element name="max" />
                        <xs:element name="sum" />
                    </xs:choice>
                </xs:complexType>
            </xs:element>
            <xs:element name="object" minOccurs="1" maxOccurs="1" type='xs:string'/>
            <xs:element name="docparid" minOccurs="0" maxOccurs="1" type='xs:string'/>
            <xs:element name="pagesize" minOccurs="0" maxOccurs="1" type='xs:integer' />
            <xs:element name="orderby" minOccurs="0" maxOccurs="1">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="order" minOccurs="1" maxOccurs="unbounded">
                            <xs:complexType>
                                <xs:sequence>
                                    <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
                                    <xs:choice minOccurs="0" maxOccurs="1">
                                        <xs:element name="ascending"/>
                                        <xs:element name="descending"/>
                                    </xs:choice>
                                </xs:sequence>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="options" minOccurs="0" maxOccurs="1">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="caseinsensitive" minOccurs="0" maxOccurs="1" default="false" type="xs:boolean" />
                        <xs:element name="showprivate" minOccurs="0" maxOccurs="1" default="false" type="xs:boolean" />
                        <xs:element name="returnformat" minOccurs="0" type='xs:string'/>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="pagesize" minOccurs="0" maxOccurs="1" default="100">
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="1"/>
                        <xs:maxInclusive value="2000"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="offset" minOccurs="0" maxOccurs="1" default="0">
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="0"/>
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="filter" minOccurs="0" maxOccurs="1" type="filteroption"/>
        </xs:all>
    </xs:complexType>
</xs:element>
<xs:complexType name="filteroption">
    <xs:choice minOccurs="1" maxOccurs="1">
         <xs:group ref="andor"/>
         <xs:group ref="operators"/>
    </xs:choice>
</xs:complexType>
 
<xs:group name="andor">
    <xs:choice>
        <xs:element ref="and"/>
        <xs:element ref="or"/>
    </xs:choice>
</xs:group>
 
<xs:group name="operators">
    <xs:choice>
        <xs:element ref="equalto"/>
        <xs:element ref="notequalto"/>
        <xs:element ref="lessthan"/>
        <xs:element ref="lessthanorequalto"/>
        <xs:element ref="greaterthan"/>
        <xs:element ref="greaterthanorequalto"/>
        <xs:element ref="between"/>
        <xs:element ref="in"/>
        <xs:element ref="notin"/>
        <xs:element ref="like"/>
        <xs:element ref="notlike"/>
        <xs:element ref="isnull"/>
        <xs:element ref="isnotnull"/>
    </xs:choice>
</xs:group>

<xs:element name="and">
    <xs:complexType>
        <xs:choice minOccurs="2" maxOccurs="unbounded">
            <xs:group ref="andor"/>
            <xs:group ref="operators"/>
        </xs:choice>
    </xs:complexType>
</xs:element>

<xs:element name="or">
    <xs:complexType>
        <xs:choice minOccurs="2" maxOccurs="unbounded">
            <xs:group ref="andor"/>
            <xs:group ref="operators"/>
        </xs:choice>
    </xs:complexType>
</xs:element>
 
<xs:element name="equalto">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="notequalto">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="lessthan">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="lessthanorequalto">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="greaterthan">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="greaterthanorequalto">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="between">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="2" maxOccurs="2"/>
        </xs:sequence>
   </xs:complexType>
</xs:element>

<xs:element name="in">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1000"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="notin">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1000"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="like">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="notlike">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
            <xs:element name="value" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="isnull">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>

<xs:element name="isnotnull">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="field" type="xs:string" minOccurs="1" maxOccurs="1"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

### Elements of the query

*   [Object](https://developer.intacct.com/web-services/queries/#object)
*   [Select](https://developer.intacct.com/web-services/queries/#select)
*   [Filter](https://developer.intacct.com/web-services/queries/#filter)
*   [Order by](https://developer.intacct.com/web-services/queries/#order-by)
*   [Options](https://developer.intacct.com/web-services/queries/#options)
*   [Page size](https://developer.intacct.com/web-services/queries/#page-size)
*   [Transaction type (docparid)](https://developer.intacct.com/web-services/queries/#transaction-type-docparid)

#### Object

Use `object` to specify which object to query, for example, `APBILL`. Both standard and custom objects are supported.

```
 <object>APBILL</object>
```

#### Select

Use `select` to specify the fields to return as well as any aggregate functions to use.

##### Fields

Use `field` to specify each field on the object to return in the results.

```
<select>
    <field>RECORDNO</field>
    <field>VENDORNAME</field>
    <field>STATE</field>
</select>
```

The dot operator (`.`) lets you access the values of fields on a related object that has a many-to-one relationship to the object being queried. You can use the dot operator in fields you supply in the `select` or `filter` tags.

The Nexus section of the Platform/Customization Services catalog can help you identify the related objects whose fields can be queried. For example, the Nexus section for AP bill shows that the related vendor object has a many-to-one relationship to AP bills.

![Image 4: UI section showing related objects](https://developer.intacct.com/images/web-services/queryRelatedField.png)

Accordingly, you can access fields on the related vendor from the AP bill, for example:

```
<field>VENDOR.CREDITLIMIT</field>
```

##### Aggregate functions

Aggregate functions perform operations on the values of fields. When using aggregate functions, the fields in the `select` element are used to group the results.

| Operator | Description |
| --- | --- |
| count | Return the number of fields |
| avg | Return the average of fields |
| min | Return the smallest value |
| max | Return the largest value |
| sum | Return the sum of the fields |

For example, the following provides the total number of `ARINVOICE` records for the given `CUSTOMERID`:

```
<query>
    <select>
        <field>CUSTOMERID</field>
        <count>RECORDNO</count>
    </select>
    <object>ARINVOICE</object>
</query>
```

Results such as the following are returned:

```
    <ARINVOICE>
        <CUSTOMERID>C-00004</CUSTOMERID>
        <COUNT.RECORDNO>18</COUNT.RECORDNO>
    </ARINVOICE>
    <ARINVOICE>
        <CUSTOMERID>C-00023</CUSTOMERID>
        <COUNT.RECORDNO>20</COUNT.RECORDNO>
    </ARINVOICE>
```

See the [tip](https://developer.intacct.com/web-services/queries/#query-tips) for using aggregate functions.

#### Filter

**Note:** Use of custom field filters on large datasets may slow query execution. This is because custom fields are not indexed. Using standard, indexed fields for queries ensures better query performance over time. To ensure the best possible query performance, follow these recommendations for filters:

*   Prioritize standard fields in filters.
*   Incorporate custom fields only as supplemental filters.

* * *

Qualifies the records to return based on their field values. You use operators and conditions to build your filter.

```
<filter>
    <greaterthan>
        <field>TOTALDUE</field>
        <value>500</value>
    </greaterthan>
</filter>
```

##### Comparison operators

| Operator | Description |
| --- | --- |
| `equalto` | Equal to |
| `notequalto` | Not equal to |
| `lessthan` | Less than |
| `lessthanorequalto` | Less than or equal to |
| `greaterthan` | Greater than |
| `greaterthanorequalto` | Greater than or equal to |
| `isnull` | Is a null value |
| `isnotnull` | Is not a null value |

```
<filter>
    <equalto>
        <field>STATE</field>
        <value>Paid</value>
    </equalto>
</filter>
```

##### Logical operators

| Operator | Description |
| --- | --- |
| `between` | Value is within the given range |
| `in` | Value is one of the given values |
| `notin` | Value is not one of the given values |
| `like` | Value matches a given pattern |
| `notlike` | Value does not match a given pattern |

The `like` and `notlike` operators support wildcards:

*   Percent sign (`%`) to match zero, one, or multiple characters
*   Underscore (`_`) to match a single character

The following example matches any name that begins with the letter `B`:

```
<filter>
    <like>
        <field>VENDORNAME</field>
        <value>B%</value>
    </like>
</filter>
```

##### Conditions

Conditions let you combine operator statements for complex queries.

| Condition | Description |
| --- | --- |
| `and` | All conditions must be true |
| `or` | One or more conditions must be true |

```
<filter>
    <and>
        <greaterthanorequalto>
            <field>WHENCREATED</field>
            <value>04/19/2023</value>
        </greaterthanorequalto>
        <lessthanorequalto>
            <field>WHENCREATED</field>
            <value>04/26/2023</value>
        </lessthanorequalto>
        <equalto>
            <field>VENDORNAME</field>
            <value>Acme Supply</value>
        </equalto>
    </and>
</filter>
```

#### Order by

Specifies the order for results based on the chosen field.

Values: `ascending`, `descending`

```
<orderby>
    <order>
        <field>TOTALDUE</field>
        <descending />
    </order>
</orderby>
```

If not specified, there is no default and the order of results is undefined.

#### Options

##### Response data format

The default format for query responses is XML, but you can use the `returnformat` option to have data returned in CSV or JSON format.

```
<options>
    <returnformat>csv</returnformat>
</options>
```

Valid values are `xml`, `csv`, and `json`. Note that CSV and JSON responses do not include any surrounding XML elements such as `<control>` and `<authentication>`; they only include the response data.

Here is a sample response containing two vendor objects with three fields each in all three formats:

###### XML

```
<?xml version="1.0" encoding="UTF-8"?>
<response>
    <control>
        <status>success</status>
        <senderid>*******</senderid>
        <controlid>1234567890</controlid>
        <uniqueid>false</uniqueid>
        <dtdversion>3.0</dtdversion>
    </control>
    <operation>
        <authentication>
            <status>success</status>
            <userid>joe.user</userid>
            <companyid>Goliath Corp</companyid>
            <locationid></locationid>
            <sessiontimestamp>2022-02-07T20:21:01+00:00</sessiontimestamp>
            <sessiontimeout>2022-02-08T20:21:01+00:00</sessiontimeout>
        </authentication>
        <result>
            <status>success</status>
            <function>query</function>
            <controlid>a92cb391-6647-494d-bfca-c52d677be181</controlid>
            <data listtype="VENDOR" totalcount="18" offset="0" count="18" numremaining="0">
                <VENDOR>
                    <RECORDNO>1010</RECORDNO>
                    <PAYTOCONTACT.CONTACTNAME>Ackman, Alice</PAYTOCONTACT.CONTACTNAME>
                    <TOTALDUE>3797</TOTALDUE>
                </VENDOR>
                <VENDOR>
                    <RECORDNO>1009</RECORDNO>
                    <PAYTOCONTACT.CONTACTNAME>Halpert, Jim</PAYTOCONTACT.CONTACTNAME>
                    <TOTALDUE>2987</TOTALDUE>
                </VENDOR>
            </data>
        </result>
    </operation>
</response>
```

###### CSV

```
RECORDNO,PAYTOCONTACT.CONTACTNAME,TOTALDUE
1010,"Ackman, Alice",3797
1009,"Halpert, Jim",2987
```

###### JSON

```
[
    {
        "RECORDNO": "1010",
        "PAYTOCONTACT.CONTACTNAME": "Ackman, Alice",
        "TOTALDUE": "3797"
    },
    {
        "RECORDNO": "1009",
        "PAYTOCONTACT.CONTACTNAME": "Halpert, Jim",
        "TOTALDUE": "2987"
    }
]
```

##### Case sensitivity

Queries are case sensitive by default, but you can choose a case-insensitive query with the `options` element.

Values: `true`, `false`

```
<options>
    <caseinsensitive>true</caseinsensitive>
</options>
```

##### Query into private entities

By default, in a multi-entity company, queries from the top-level entity do not access data in private entities. You can set the `showprivate` option to `true` if you want to query data in private entities.

Values: `true`, `false`

```
<options>
    <showprivate>true</showprivate>
</options>
```

#### Page size

Specifies the number of results per returned set.

Default value: 100

Maximum value: 2000

```
 <pagesize>200</pagesize>
```

If you have more than 2000 total records, see offsets below.

#### Offset

If you have more than 2000 total records (which is the maximum page size), use offsets to return sets of results until there are no more.

**Note:** Each call with a different offset is a new query and not a continuation of any previous query. Any changes to the underlying data that happen between calls may affect query results. For example, if there is a query that returns 2000 records, and then new records are added, and then there is another query request with an offset of 2000, records may be missed due to the new records changing the result set.

For example, the following skips the first 10 results.

```
 <offset>10</offset>
```

#### Transaction type (docparid)

Specifies the transaction definition type (or document type) for `SODOCUMENT`, `PODOCUMENT`, or `INVDOCUMENT` records. You must use this to take advantage of any custom fields on the transaction definition.

```
<query>
    <select>
        <field>RECORDNO</field>
        <field>STATE</field>
    </select>
    <object>SODOCUMENT</object>
    <docparid>Sales Order</docparid>
</query>
```

### Tips

When using aggregate functions, avoid using record number in the `select` element. For example, consider the following query:

```
    ...
    <query>
        <select>
            <field>CUSTOMERID</field>
            <field>RECORDNO</field>
            <count>RECORDNO</count>
        </select>
        <object>ARINVOICE</object>
    </query>
```

The results will provide a separate entry for each record in order to include its record number, so your count does not work as expected. (Each record has an entry with a count of 1):

```
    <ARINVOICE>
        <CUSTOMERID>C-00019</CUSTOMERID>
        <RECORDNO>122</RECORDNO>
        <COUNT.RECORDNO>1</COUNT.RECORDNO>
    </ARINVOICE>
    <ARINVOICE>
        <CUSTOMERID>C-00019</CUSTOMERID>
        <RECORDNO>128</RECORDNO>
        <COUNT.RECORDNO>1</COUNT.RECORDNO>
    </ARINVOICE>
```

* * *

Using readByQuery (legacy)
--------------------------

Let’s look at a simple `readByQuery` example. The following matches `APBILL` objects with the given `VENDORNAME`.

![Image 5: example of query on vendor name](https://developer.intacct.com/images/web-services/query.png)

Queries are interpreted as part of a `readyByQuery` function call in the `content` element of an XML request:

```
<content>
    <function>
        <readByQuery>
            <object>APBILL</object>
            <fields>*</fields>
            <query>VENDORNAME = 'Regal Services'</query>
            <pagesize>100</pagesize>
        </readByQuery>
    </function>
</content>
```

You can provide an empty `query` element to return all `APBILL` objects (up to the limit specified with `pagesize`). See [Paginate results](https://developer.intacct.com/web-services/queries/#paginate-results) to access results beyond the specified limit.

### Limit fields returned to improve performance

If you are querying for many objects, you can improve performance by limiting the fields returned to only those you care about:

```
<readByQuery>
   <object>APBILL</object>
   <fields>RECORDNO,RECORDTYPE</fields>
   <query></query>
   <pagesize>25</pagesize>
</readByQuery>
```

### Use rownum to specify the rows that readByQuery returns

When querying custom objects, you might want to limit your query to rows that you specify. The `rownum` condition returns a number for each row that `readByQuery` returns, so you can reduce the amount of data returned to just what you need. For example, use `rownum` to verify if a query result will contain expected data by returning a set of 5 rows instead of all rows. Or you might want to target rows in your query that were added later; if so, you can select rows greater than a specified `rownum`.

In the following example, four fields of the `depreciation_schedule` object are queried using the specified criteria; `rownum` is used to limit the query to the first row found.

```
<function controlid="2194e274-ceca-4779-bffa-779166f52122_204175">
    <readByQuery>
        <object>depreciation_schedule</object>
        <fields>Rasset,Rasset_class,posting_date,depreciation_amount</fields>
        <pagesize>10</pagesize>
        <query>id in (347839,347840,347841,347842) and (status = 'posted' OR status = 'summary_posted') and rownum = 1 </query>
    </readByQuery>
</function>
```

The following filter conditions return only the rows specified:

*   rownum = 1 returns row 1
*   rownum < 5 returns rows 1 - 4
*   rownum \> 5 returns rows 6 and greater.

### Paginate results

You might want to get query results in batches instead of all at once. Note that the query in the previous example provided a `pagesize` of 25. Assuming there are more than 25 results, you can get the next batch of 25 with `readMore`. Provide either the object name or the result ID (from the `readByQuery` response) for the child element as shown. Using the result ID ensures that your paged results are from the same originating `readByQuery` call, which is important if there might be multiple `readByQuery` calls on the same object or data changing behind the scenes.

When you get to the last set of results, `numremaining="0"` is shown in the `listtype` attribute of the `data` element.

```
<readMore>
    <object>APBILL</object>
</readMore>
```

```
<readMore>
   <resultId>7765623332WU1hh8CoA4QAAHxI9i8AAAAA5</resultId>
</readMore>
```

### Supported operators

Sage Intacct queries support a subset of operators available for the standard SQL `WHERE` clause, as follows:

`<`, `>`, `>=`, `<=`, `=`, `like`, `not like`, `in`, `not in`

When doing NULL comparisons, you can use `IS NOT NULL` or `IS NULL`.

You can combine conditions using `AND` and `OR` operators, and you can query for an untrue condition by prefixing it with `NOT`.

**Note:** You cannot query on a field that is a join by foreign key.

The `like` operator supports wildcards:

*   Percent sign (`%`) to match zero, one, or multiple characters
*   Underscore (`_`) to match a single character

### Operands

The operands are the integration name of a field and a corresponding target value (or values) for that field.

String operands are case-sensitive.

### Illegal characters in XML

When composing your queries, be aware that the less than (`<`) and ampersand (`&`) characters are illegal in XML. The greater than (`>`) character is legal, but it is a good practice to replace it with the XML entity reference.

| Character | Entity reference |
| --- | --- |
| Less than (`<` ) | `&lt;` |
| Greater than (`>` ) | `&gt;` |
| Ampersand (`&` ) | `&amp;` |

### Examples

The following shows examples of queries on both standard and custom objects.

| Object | Query | Purpose |
| --- | --- | --- |
| `VENDOR` | `STATUS = 'F' AND ONETIME = 'T'` | List inactive and one-time vendors (by querying on boolean values). |
| `DEPARTMENT` | `DEPARTMENTID IN ('10','20','15','11','12','8','3','4','100','99')` | List departments with any of these IDs. |
| `CONTACT` | `CONTACTNAME = 'Erin\'s Software'` | List contacts with the given name. Note the escaped apostrophe. |
| `ACTIVITYLOG` | `OBJ_ID &gt; 2000 AND CREATED_AT &gt;= '04/19/2021 12:00:00' AND CREATED_AT &lt; '04/20/2021 12:00:00'` | List audit trail logs for all records on April 19, 2021. When working with dates, the greater than operator means _more recent than_. Note the use of the entity references for the greater than and less than operators. |
| `GLBATCH` | `JOURNAL = 'GJ'` | List Journal Entries. |
| `APBILL` | `STATE='A'` | List bills whose state is set to posted. |
| `GLACCOUNTBALANCE` | `PERIOD = 'Month Ended June 2021'` | List account balances for the given period. |
| `GLACCOUNTBALANCE` | `PERIOD = 'Month Ended June 2021' AND NOT (TOTDEBIT = 0 AND TOTCREDIT = 0 AND TOTADJDEBIT = 0 AND TOTADJCREDIT = 0 AND FORBAL = 0 AND ENDBAL = 0)` | List account balances, excluding entries with the specified zero balances. |
| `USERINFO` | `usertype = 'B'` | List user information records of the _business_ user type. |
| `depreciation_schedule` | `depreciation_amount &lt;= 50 AND Rasset = 'Thinkpad T61' AND posting_date &gt;= '02/01/2022'` | List custom `deprecation_schedule` objects that meet the conditions. Note the use of the entity references for the less than and greater than operators. |
| `depreciation_schedule` | `STATUS IS NULL` | List custom `deprecation_schedule` objects whose status is set to NULL. |
| `VENDOR` | `NOT VENDORID = 'V1234'` | List vendors with vendor IDs other than `V1234`. |
| `EMPLOYEE` | `EMPLOYEEID like 'b%'` | List employees whose IDs start with the letter `b`. |
| `EMPLOYEE` | `EMPLOYEEID like '%b%'` | List employees whose IDs include the letter `b` at any position. |
| `EMPLOYEE` | `EMPLOYEEID like '_b%'` | List employees whose IDs have the letter `b` as the second character. |

### Tips

*   If you create a new boolean field on existing records, those fields will not yet have a value. Even though a `read` request will show the value as `false` to reflect the value in the Sage Intacct UI, when you attempt to return these with a `readByQuery` request, you need to query on the NULL value.
    
*   If you are querying a validated list that stores single characters in place of terms, you need to use the database character. For example, `usertype = 'B'` queries for records of the _business_ user type from [USERINFO](https://developer.intacct.com/api/company-console/users/#query-and-list-users). See the query tables in the API documentation for details about such such database characters.
    
*   If you need information about available fields for an object, there are several places with helpful information:
    
    *   Consult the [API documentation](https://developer.intacct.com/api/) for the object of interest. Look under the `readByQuery` heading and consult a secondary query table (if present). See [Account Balances](https://developer.intacct.com/api/general-ledger/account-balances/) for an example.
        
    *   Use the Sage Intacct GUI to look up object field integration names through **Object Definition** pages.
        
    *   Use the `inspect` function to return many fields names and types for an object, for example:
        
        ```
         <inspect detail = "1">
            <object>APBILL</object>
         </inspect>
        ```
        
*   If you need to get information about related or owned objects, see the relevant [FAQ](https://developer.intacct.com/support/faq/#how-do-you-get-information-about-related-or-owned-objects).
    
*   If you need to query for an object based on a joined field, see the relevant [FAQ](https://developer.intacct.com/support/faq/#how-do-i-query-for-an-object-based-on-a-joined-field-or-how-do-i-query-for-an-employee-by-name).
    

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

