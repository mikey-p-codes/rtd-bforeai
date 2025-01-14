.. _Domain Information:

================================
Gathering Domain Information and Generating Reports
================================

API calls to gather information on domains and gather detail information on domains.

.. _introduction:

Introduction
------------
This section details gathering information on domains.  Gathering importation information like Whois data important for determining the legitimacy of a given domain. 

.. _get_domain_report:

Generating a Domain Report
--------------------------
This endpoint will generate and return a report with information about a specific domain. 
This function requires a parameter ?d= string, the domain name to be analyzed
This call can take some time to complete based on the size of the organization and the number of records to be analyzed.
The response will return a Screenshot, since we are viewing only data we have removed it from the response.
Finally we have printed the data in a pretty format using pprint

.. _get_domain_info:

Gathering Domain Information
----------------------------

This function retrieves details about a monitored domain with the domain ID passed as parameter d= string.

.. _domain_report_list:

Domain Report List
------------------

Get a detailed list from the domain report:
This function will query the domain and return only the information you want via the parameters:
d= string, the domain name to be analyzed
s=y/n include screenshots Default: y
w=y/n include whois information Default: y
n=y/n include DNS information Default: y
c=y/n include certificate information Default: y
st= string, start date for the report
en= string, end date for the report

.. _get_report_id:

Get Report ID
-------------

Retrieve a report from a previously run domain report with the report ID passed as paramater 
d= string, the report ID to be analyzed

.. _get_domain_scores:

Domain Scores
-------------

Retrieve a list of domains processed and scored starting from a specific start and end date.
Time is represented as linux epoch time.

Note: The Linux epoch time for Jan 1, 1970, is 0.
Today's date in Linux Epoch time is: 1736804009 (for example, if today is January 13 2025)
.. note: It appears that if you attempt to go too far back you will get an internal server error.

