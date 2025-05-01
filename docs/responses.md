Title: XML Responses

URL Source: https://developer.intacct.com/web-services/responses/

Markdown Content:
*   [status](https://developer.intacct.com/web-services/responses/#status)
*   [result](https://developer.intacct.com/web-services/responses/#result)
*   [errormessage](https://developer.intacct.com/web-services/responses/#errormessage)

* * *

When working with Web Services, responses are provided in XML.

The high level structure of a response is very similar to that of a request—both have `control` and `operation` elements organizing the main content.

The following example shows the basic structure of a response.

![Image 1: sample XML response with session lifespan](https://developer.intacct.com/images/web-services/xml_response.png)

The `control`, `operation`, and `authentication` elements are parallel elements that reflect the contents of the request. The following descriptions highlight items that are unique to a response.

* * *

status
------

Indicates status with either `success` or `failure`. An error message is provided in case of a failure (see below).

Note that there are three levels for status messages. If the `control` and `authentication` blocks succeed, then `results` are available. Individual `function` calls can succeed or fail independently (unless the `operation` element in the request had the `transaction` attribute set to `true`).

* * *

result
------

Depending on the type of function you requested, the structure of the result will vary. For example, when using the `create` function for multiple objects (as shown in the figure), the result provides a `data` element with `listtype` and `count` attributes as well as child elements representing each object. Other functions, such as `delete`, return only a status of `success` or errors. See the reference documentation for the function of interest for specifics about the return values.

* * *

errormessage
------------

For every error triggered during request execution, the XML response document provides an `errormessage` element. The error can occur at the control level, in which case no operation is executed. Errors can also occur for individual functions. For example, the following shows an error for a problem at the function level:

![Image 2: example of errormessage element](https://developer.intacct.com/images/web-services/xml-error-result.png)

* * *

What’s next?
------------

*   Learn about [handling errors](https://developer.intacct.com/web-services/error-handling/).

[Provide feedback](https://forms.office.com/Pages/ResponsePage.aspx?id=fN0yPvZBLUmho8WOsCz0-Gj_lksFLzJAg2QKkx1lkvZUMkxMVDYxSzhHQzlNTjBNR1IwOVNETDNEMiQlQCN0PWcu)

