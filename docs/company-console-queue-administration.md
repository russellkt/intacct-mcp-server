Title: Queue Administration

URL Source: https://developer.intacct.com/api/company-console/queue-administration/

Markdown Content:
Blog
Guides 
API Reference
Tools & Libraries
Support
  API  Company and Console  Queue Administration
Queue Administration
Get Offline Job Object Definition
Query and List Offline Jobs
Query and List Offline Jobs (Legacy)
Get Offline Job
Prioritize a Job
Cancel a Job

Queue administration lets you get a list of all offline jobs queued to run in your company.

You can also see a history of jobs to determine if an important offline job has been completed or if there were complications. If you have the right subscription (Premium Level of Service at Silver level or higher) you can cancel offline jobs or prioritize important jobs to the top of the queue.

An offline job refers to any sort of data action that you choose to process offline in the background while you continue working. Offline jobs can include CSV imports, reports, contract invoices, check runs, Data Delivery Service jobs, and more. Smart Events are not currently supported.

Usage information for queue administration is available in the Sage Intacct product help.

Get Offline Job Object Definition
lookup

List all the fields and relationships for the offline job object:

<lookup>
    <object>JOBQUEUERECORD</object>
</lookup>
Parameters
Name	Required	Type	Description
object	Required	string	Use JOBQUEUERECORD
Query and List Offline Jobs
query

List the job ID, job type, and time queued for each offline job:

<query>
    <object>JOBQUEUERECORD</object>
    <select>
        <field>JOBID</field>
        <field>JOBTYPE</field>
        <field>TIMEQUEUED</field>
    </select>
</query>
Parameters
Name	Required	Type	Description
object	Required	string	Use JOBQUEUERECORD
filter	Optional	object	Filter expression to limit the response to only objects that match the expression. Check the value of a single field using operators such as equalto/like, or multiple fields using and/or. Query fields on related objects using the dot operator (for example, VENDOR.CREDITLIMIT on APBILL).
select	Required	sequence	The names of the fields that you want included in the response, and an optional aggregate function such as count or sum. Returning all fields is not supported.
orderby	Optional	object	Provide an order element with a field name and choose an ascending or descending sort order, for example:
<order>
  <field>RECORDNO</field>
  <descending/>
</order>
options	Optional	object	Query options:
Set the caseinsensitive element to true for a case-insensitive query
 <caseinsensitive>true</caseinsensitive>
In a multi-entity company, set the showprivate element to true to query data in private entities:
 <showprivate>true</showprivate>
Specify the returnformat for the response: xml (default), json, or csv
 <returnformat>json</returnformat>

pagesize	Optional	integer	Maximum number of matching objects to return in the response, between 1 and 2000 items (Default: 100)
offset	Optional	integer	Point at which to start indexing into records (Default: 0)

filter Fields

Name	Required	Type	Description
TIMEQUEUED	Optional	string	Date that the job was queued in format mm/dd/yyyy
STATE	Optional	string	Status of the job. For active jobs, use Q for Queued or T for In progress/In Transit. For processed jobs, use S for Delivered, D for Failed, R for Deferred, or C for Cancelled.
JOBTYPE	Optional	string	Job type. Use DDS job, Asynchronous API requests, CSV import, Scheduled memorized report, Scheduled financial report, Update report, Process & store report, Scheduled report, Email report, Process & store report group, Scheduled report group, Recurring consolidation, Offline consolidation, Run action, Contract invoices, Project invoices, Check run, Confirm check run, Void check run, or Wells Fargo payments. For more information about these, see queue administration in the Sage Intacct product help.
Response

JOBQUEUERECORD

The above function returns data structured like this:

<JOBQUEUERECORD>
    <JOBID>6465763130WyzaiwriEQoAAEvnxBQAAAxxx</JOBID>
    <JOBTYPE>DDS job</JOBTYPE>
    <TIMEQUEUED>2018-06-22T11:21:48Z</TIMEQUEUED>
</JOBQUEUERECORD>
Parameters
JOBID	string	Unique identifier for the job.
TIMEQUEUED	string	Date that the job was queued in ISO 8601 date time format.
JOBTYPE	string	Job type. One of DDS job, Asynchronous API requests, CSV import, Scheduled memorized report, Scheduled financial report, Update report, Process & store report, Scheduled report, Email report, Process & store report group, Scheduled report group, Recurring consolidation, Offline consolidation, Run action, Contract invoices, Project invoices, Check run, Confirm check run, Void check run, or Wells Fargo payments. For more information about these, see queue administration in the Sage Intacct product help.
ACTION	string	Either the name of the report or record affected by the job, or the action performed by the job.
DETAILS	string	Additional details of the job, which might include the record information, report information, send-to email address, or more.
USERS	string	User who submitted the job.
STATE	string	Status of the job. For active jobs, Queued or In Progress. For processed jobs, Delivered, Failed, Deferred, or Cancelled.
ACTIVETIME	string	Total time the job took from the start of processing to completion of processing in HH:mm:ss format (called active time in the UI).
WAITINQUEUE	string	Time that the job has been waiting in the queue in HH:mm:ss format.
TIMESTARTED	string	Date and time the job started processing in ISO 8601 date time format.
Query and List Offline Jobs (Legacy)
readByQuery
<readByQuery>
    <object>JOBQUEUERECORD</object>
    <fields>*</fields>
    <query></query>
    <pagesize>100</pagesize>
</readByQuery>
Parameters
Name	Required	Type	Description
object	Required	string	Use JOBQUEUERECORD
fields	Optional	string	Comma-separated list of fields on the object to list. For best performance and predictability, limit the number of fields. To return all fields, omit the element or provide * for the value.
query	Required	string	SQL-like query based on fields on the object. The following operators are supported: <, >, >=, <=, =, like, not like, in, not in, IS NOT NULL, IS NULL, AND, OR. Illegal XML characters must be properly encoded, and single quotes must be escaped with backslashes ('Jane\'s Deli'). Joins are not supported. Note: like, not like, IS NOT NULL, and IS NULL are not supported for OBJECTTYPE and OBJECTKEY.
pagesize	Optional	integer	Custom page size between 1 and 1000 items (Default: 100)

query Fields

Name	Required	Type	Description
TIMEQUEUED	Optional	string	Date that the job was queued in format mm/dd/yyyy
STATE	Optional	string	Status of the job. For active jobs, use Q for Queued or T for In progress/In Transit. For processed jobs, use S for Delivered, D for Failed, R for Deferred, or C for Cancelled.
JOBTYPE	Optional	string	Job type. Use DDS job, Asynchronous API requests, CSV import, Scheduled memorized report, Scheduled financial report, Update report, Process & store report, Scheduled report, Email report, Process & store report group, Scheduled report group, Recurring consolidation, Offline consolidation, Run action, Contract invoices, Project invoices, Check run, Confirm check run, Void check run, or Wells Fargo payments. For more information about these, see queue administration in the Sage Intacct product help.
Response

jobqueuerecord

The above function returns data structured like this:

<jobqueuerecord>
    <JOBID>6465763130WyzaiwriEQoAAEvnxBQAAAxxx</JOBID>
    <TIMEQUEUED>2018-06-22T11:21:48Z</TIMEQUEUED>
    <JOBTYPE>DDS job</JOBTYPE>
    <ACTION>Sales Document Detail</ACTION>
    <DETAILS>All data</DETAILS>
    <USERS>tjmalloney</USERS>
    <STATE>Delivered</STATE>
    <ACTIVETIME>0:05:02</ACTIVETIME>
    <WAITINQUEUE>0:49:39</WAITINQUEUE>
    <TIMESTARTED>2018-06-22T12:11:27Z</TIMESTARTED>
</jobqueuerecord>
Parameters
JOBID	string	Unique identifier for the job.
TIMEQUEUED	string	Date that the job was queued in ISO 8601 date time format.
JOBTYPE	string	Job type. One of DDS job, Asynchronous API requests, CSV import, Scheduled memorized report, Scheduled financial report, Update report, Process & store report, Scheduled report, Email report, Process & store report group, Scheduled report group, Recurring consolidation, Offline consolidation, Run action, Contract invoices, Project invoices, Check run, Confirm check run, Void check run, or Wells Fargo payments. For more information about these, see queue administration in the Sage Intacct product help.
ACTION	string	Either the name of the report or record affected by the job, or the action performed by the job.
DETAILS	string	Additional details of the job, which might include the record information, report information, send-to email address, or more.
USERS	string	User who submitted the job.
STATE	string	Status of the job. For active jobs, Queued or In Progress. For processed jobs, Delivered, Failed, Deferred, or Cancelled.
ACTIVETIME	string	Total time the job took from the start of processing to completion of processing in HH:mm:ss format (called active time in the UI).
WAITINQUEUE	string	Time that the job has been waiting in the queue in HH:mm:ss format.
TIMESTARTED	string	Date and time the job started processing in ISO 8601 date time format.
Get Offline Job
read
<read>
    <object>JOBQUEUERECORD</object>
    <keys>6465762230WuhjPAriEFQAAG91x@AAAAAK7</keys>
    <fields>*</fields>
</read>
Parameters
Name	Required	Type	Description
object	Required	string	Use JOBQUEUERECORD
keys	Required	string	Comma-separated list of job JOBID to get
fields	Optional	string	Comma-separated list of fields on the object to get. To return all fields, omit the element or provide * for the value.
For best performance and predictability, limit the number of fields.
returnFormat	Optional	string	Data format for the response body:
xml (default)
json
csv
Prioritize a Job
promote
<promote>
    <JOBQUEUERECORD>
        <JOBID>6465762230WuhjPAriEFQAAG91x@AAAAAK7</JOBID>
    </JOBQUEUERECORD>
</promote>
Parameters
Name	Required	Type	Description
object	Required	string	Use JOBQUEUERECORD
keys	Required	string	Comma-separated list of job JOBID to move to the top of the queue
Cancel a Job
cancel
<cancel>
    <JOBQUEUERECORD>
        <JOBID>6465762230WuhjPAriEFQAAG91x@AAAAAK7</JOBID>
    </JOBQUEUERECORD>
</cancel>
Parameters
Name	Required	Type	Description
object	Required	string	Use JOBQUEUERECORD
keys	Required	string	Comma-separated list of job JOBID to cancel

 PROVIDE FEEDBACK

Page content licensed under Creative Commons Attribution 4.0. Code samples licensed under Apache v2.0.
© 2025 The Sage Group plc or its affiliates or licensors ("Sage"). All trademarks mentioned are the property of their respective owners. Use of non-Sage trademarks is not an endorsement of any person or product.

