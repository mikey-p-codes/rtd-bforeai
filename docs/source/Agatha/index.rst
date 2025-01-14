.. _process_execution:

===============
Process Execution
===============

.. _introduction:

Introduction
------------

This section details listing processes executed by the BforeAi API.  You can leverage this API to see a list of scored domains, drill down on a process that was exuted and get information regarding a monitored domain.

.. _get_process_list:

Get Process List
----------------

This function retrieves a list of processes executed by the BforeAi API.

.. _get_process_details:

Get Process Details
-------------------

Retrieve the details of a process with the process ID passed as parameter p= string, the process ID to be analyzed

.. note: This function can return an empty list even if the HTTP response is 200 OK

.. _get_domain_scores:

Get Domain Scores
-----------------

''' Retrieve a list of domains processed and scored starting from a specific start and end date.
Time is represented as linux epoch time.

Note: The Linux epoch time for Jan 1, 1970, is 0.
Today's date in Linux Epoch time is: 1736804009 (for example, if today is January 13 2025)
.. note: It appears that if you attempt to go too far back you will get an internal server error

