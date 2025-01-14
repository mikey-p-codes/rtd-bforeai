.. _authentication:

================================
Authentication and Token Management
================================

BforeAi User and Token Managment

.. _introduction:

Introduction
------------

The BforeAi API uses a Username and Password authentication scheme to log in and retrieve a Java Web Token (JWT).  This token is used to authenticate all subsequent requests to the API.  The token can be passed in the header of the request as a Bearer token.  The token can be set to expire after a certain amount of time, and the user will need to log in again to retrieve a new token.  A user may also log out and expire thier own token.

.. _config:

Environment Variables
---------------------

To simplify setup, the use of environment variables is recommended.  You will be sending the token information in the header of the request many times, having it in an environment variable will make it easier to manage.

.. code-block:: python

    BASEURL = "https://api.bfore.ai/"

    AUTH = {
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD"
    }

    TOKEN ="YOUR_TOKEN"

    CHANGE_PASSWORD = {
        "username":"YOUR_USERNAME",
        "old": "YOUR_OLD_PASSWORD",
        "new": "YOUR_NEW_PASSWORD",
        "confirm": "CONFIRM_NEW_PASSWORD"
    }


.. note: These variables are just an example, you can set them to whatever works best for you and your development environment.

.. _test_unsecure:

Testing Endpoint Availability
-----------------------------

To test the availability of the API, you can use the following code snippet:



.. code-block:: python

    import requests
    from config import BASEURL

    def test_unsecure():
    url = BASEURL + "test/unsecure"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())  
    else:
        print("Error: ", response.status_code)
    return response.json()

.. code-block:: powershell

    PS C:\patti\bforeai> python3.exe test_unsecure.py
    {'message': 'Hi anonymous'}

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
