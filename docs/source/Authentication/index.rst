.. _authentication:

================================
Authentication and Token Management
================================

BforeAi User and Token Managment

.. toctree::
   :maxdepth: 5
   :caption: Contents:
    introduction
    environment_variables

.. _introduction:

Introduction
------------

The BforeAi API uses a Username and Password authentication scheme to log in and retrieve a Java Web Token (JWT).  This token is used to authenticate all subsequent requests to the API.  The token can be passed in the header of the request as a Bearer token.  The token can be set to expire after a certain amount of time, and the user will need to log in again to retrieve a new token.  A user may also log out and expire thier own token.

.. _config:

Environment Variables
---------------------

.. _test_unsecure:

Testing Endpoint Availability
-----------------------------

.. _login:

User Authentication
-------------------

.. _test_secure:

Testing Secure Endpoint Availability
------------------------------------

.. _expire_security_token:

Expire Security Token and Logout
---------------------------------

.. _request_new_token:

Request New Security Token
---------------------------

.. _renew_security_token:

Renewing Security Token
-----------------------

.. _change_password:

Changing Password
-----------------
