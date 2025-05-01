Title: XML Functions

URL Source: https://developer.intacct.com/web-services/functions/

Markdown Content:
*   [Generic versus object-specific functions](https://developer.intacct.com/web-services/functions/#generic-versus-object-specific-functions)
*   [Working with transaction lines and legacy functions](https://developer.intacct.com/web-services/functions/#working-with-transaction-lines-and-legacy-functions)

* * *

Generic versus object-specific functions
----------------------------------------

The XML API provides two types of functions:

*   _Generic functions_ provide basic CRUD (`create`, `read`, `update`, and `delete`) operations. You supply the target objects with their appropriate parameters (in any order) as sub-elements of the function. One function call can operate on multiple objects.
    
*   _Object-specific functions_ provide a set of CRUD functions for each object type—for example, `create_customer`, `update_customer`, `create_vendor`, `update_vendor`, and so forth. Each object-specific function has a unique body structure and the sub-elements must be in the correct order. You must use a separate call for each object.
    

The following table shows examples of both types of functions. Note the difference in how multiple objects are created.

| Generic functions | Object-specific functions |
| --- | --- |
| ![Image 1: example of generic create function](https://developer.intacct.com/images/web-services/3.0_xml.png) | ![Image 2: examples of explicit functions](https://developer.intacct.com/images/web-services/2.1_xml.png) |

By convention, uppercase letters are used for object elements when showing examples of generic functions, and lowercase letters are used for object elements when using object-specific functions.

**Note:** When implementing new APIs, Intacct provides generic functions. The object-specific functions are labeled as _legacy_ in the API documentation, which simply means they will not be enhanced. There are no plans to deprecate legacy functions, and in fact, there are cases in which they are the only functions available.

* * *

Working with transaction lines and legacy functions
---------------------------------------------------

When using a combination of generic and object-specific functions in your work, be aware that there can be a difference in the way transaction lines are indexed.

For example, consider order entry transactions. For this object, the generic `read` function uses a zero-based index for entries returned in the response. However, the object-specific update function uses a one-based index for entries you supply in the request.

So, when you perform a `read` on SODCUMENT, the response identifies the first entry as `LINE_NO` 0.

```
...
<SODOCUMENTENTRIES>
    <sodocumententry>
        <RECORDNO>44</RECORDNO>
        <DOCHDRNO>25</DOCHDRNO>
        <DOCHDRID>Sales Order-SO-00029</DOCHDRID>
        <SALE_PUR_TRANS>S</SALE_PUR_TRANS>
        <BUNDLENUMBER></BUNDLENUMBER>
        <LINE_NO>0</LINE_NO>  <!-- First entry is zero -->
        <MEMO>First line</MEMO>
```

When using the object-specific `update_sotransaction` function to modify that first line, you need to add one to the line number from the `read` response.

```
<update_sotransaction key='Sales Order-SO-00029'>
      <updatesotransitems>
            <updatesotransitem line_num='1'>  <!-- First entry is one -->
                <memo>First line: updated!</memo>
            </updatesotransitem>
      </updatesotransitems>
</update_sotransaction>
```

The same math must be performed when using `read` in combination with:

*   `update_potransaction` in Purchasing
*   `update_ictransaction` in Inventory Control

When working with other transactions, the `read` response typically returns entries using a one-based index.

**Warning:** Before doing any large scale update operations using object-specific functions, always perform a test to make sure you are modifying the correct lines.

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

