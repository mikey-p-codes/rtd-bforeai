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

The following code snippet will login a user and return details about that user.  For simplicity we are just printing the response, but you can use the response to store the token in an environment variable.

To properly build the request you will need the following

+------------------------+-----------------------------------+
| Endpoint               | https://api.bfore.ai/user/login   |                        
+========================+===================================+
| JSON Request           | .. code-block:: json              |
|                        |                                   |
|                        |    {                              |
|                        |        "Username":"<username>",   |
|                        |        "Password":"<password>"    |
|                        |    }                              |
|                        |                                   |
+------------------------+-----------------------------------+

.. code-block:: python

    import requests
    from config import BASEURL, AUTH

    def login():
    url = BASEURL + "user/login"
    response = requests.post(url, json=AUTH)
    if response.status_code == 200:
        response_data = response.json()
        print("Username:", response_data.get("Username"))
        print("Token:", response_data.get("Token"))
    else:
        print("Error: ", response.status_code)
    return response.json()

.. code-block:: bash

    $ python3 login.py
    Username: michael@bfore.ai
    Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9[....snip....]8OabCHwHjSIymw

.. _test_secure:

Testing Secure Endpoint Availability
------------------------------------

You can confirm that your token is being accpeted by the platform by sending a request with your token as a bearer token in the header.  

+------------------------+-----------------------------------------+
| Endpoint               | https://api.bfore.ai/test/secure        |                        
+------------------------+-----------------------------------------+
| Request Header         | .. code-block:: json                    |
|                        |                                         |
|                        |    {                                    |
|                        |        "Authorization":f"Bearer {TOKEN}"|
|                        |    }                                    |
|                        |                                         |
+------------------------+-----------------------------------------+

.. code-block:: python

    import requests
    from config import BASEURL, TOKEN

    def test_secure():
    url = BASEURL + "test/secure"
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error: ", response.status_code)
    return response.json()

.. code-block:: bash

    $ python3 test_secure.py
    {'message': 'Hi michael@bfore.ai'}


.. _expire_security_token:

Expire Security Token and Logout
---------------------------------

To expire a security token and logout, you can use the following code snippet.  This will invalidate the token and require the user to log in again to retrieve a new token.

+------------------------+-----------------------------------------+
| Endpoint               | https://api.bfore.ai/user/logout        |
+------------------------+-----------------------------------------+
| Request Header         | .. code-block:: json                    |
|                        |                                         |
|                        |    {                                    |
|                        |        "Authorization":f"Bearer {TOKEN}"|
|                        |    }                                    |
|                        |                                         |
+------------------------+-----------------------------------------+

.. code-block:: python

    import requests
    from config import BASEURL, TOKEN

    def expire_security_token():
      headers = {
            "Authorization": f"Bearer {TOKEN}"
      }
      url = BASEURL + "user/logout"
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
            print(response.json())
      else:
            print("Error: ", response.status_code)
      return response.json()

.. code-block:: bash

    $ python3 expire_security_token.py
    {'message': 'User logged out'}

.. _request_new_token:

Request New Security Token
---------------------------

To request a new security token, you can use the following code snippet.  This will invalidate the current token and return a new token.

+------------------------+-----------------------------------------+
| Endpoint               | https://api.bfore.ai/user/token         |
+------------------------+-----------------------------------------+
| Request Header         | .. code-block:: json                    |
|                        |                                         |
|                        |    {                                    |
|                        |        "Authorization":f"Bearer {TOKEN}"|
|                        |    }                                    |
|                        |                                         |
+------------------------+-----------------------------------------+
|Parameters              + .. code-block:: json		               |
|                        |                                         |
|                        |    {                                    |
|                        |        "m":int,		                   |
|                        |        "d":int    		               |
|                        |    }                                    |
|                        |                                         |
+------------------------+-----------------------------------------+

.. code-block:: python
    import requests
    from config import BASEURL, TOKEN

    def request_new_token():
    url = BASEURL + "user/token"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        "m": "int", # number of minutes before the token expires
        #or
        "d": "int"  # number of days before the token expires
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        response_data = response.json()
        print("Token:", response_data.get("Token"))
    else: 
        print("Error: ", response.status_code)
    return response.json()

.. code-block:: bash
    
    $ python3 request_new_token.py
    Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9[....snip....]8OabCHwHjSIymw


.. _renew_security_token:

Renewing Security Token
-----------------------

You can use the following code snippet to renew a security token.  This will extend the expiration time of the token.

+------------------------+-----------------------------------------+
| Endpoint               | https://api.bfore.ai/user/renew         |
+------------------------+-----------------------------------------+
| Request Header         | .. code-block:: json                    |
|                        |                                         |
|                        |    {                                    |
|                        |        "Authorization":f"Bearer {TOKEN}"|
|                        |    }                                    |
|                        |                                         |
+------------------------+-----------------------------------------+

.. code-block:: python

    import requests
    from config import BASEURL, TOKEN

    def renew_security_token():
    url = BASEURL + "user/renew"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else: 
        print("Error: ", response.status_code)
    return response.json()

.. code-block:: bash
    
    $ python3 renew_security_token.py
    {   'Authorizations': [   {   'Company': {   'Created': '0001-01-01T00:00:00',
                                             'Deleted': '0001-01-01T00:00:00',
                                             'Id': 1,
                                             'Name': 'Bfore',
                                             'Parent': {   'Created': '0001-01-01T00:00:00',
                                                           'Deleted': '0001-01-01T00:00:00',
                                                           'Id': 4}},
                              'Roles': [{'Id': 1, 'Name': 'user'}]}],
    'Created': '1999-09-09T14:56:14',
    'Email': 'michael@bfore.ai',
    'Firstname': 'Dreamcast',
    'Id': '0',
    'Lastname': '',
    'PasswordExpiration': '0001-01-01T00:00:00',
    'Properties': {},
    'Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.[...snip...]F4qvRMLU80GRISwNlAbFApiJujVIg',
    'Username': 'michael@bfore.ai',
    'access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.[....snip....]8OabCHwHjSIymw',
    'expires_in': 0,
    'token_type': 'bearer'}


.. _change_password:

Changing Password
-----------------

This function will let a user login and change their password. The user will need to provide their old password, and the new password they would like to use.  The user will also need to confirm the new password.

+------------------------+------------------------------------------+
| Endpoint               | https://api.bfore.ai/user/password       |                        
+========================+==========================================+
| JSON Request           | .. code-block:: json                     |
|                        |                                          |
|                        |    {                                     |
|                        |        "Username":"<username>",          |
|                        |        "old":"<YOUR_OLD_PASSWORD>" ,     |
|                        |        "new":"<YOUR  NEW_PASSWORD>" ,    |
|                        |        "confirm":"<CONFIRM_NEW_PASSWORD>"|
|                        |    }                                     |
|                        |                                          |
+------------------------+------------------------------------------+

.. code-block:: python

    import requests
    from config import BASEURL, CHANGE_PASSWORD

    def change_password():
    url = BASEURL + "user/password"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=CHANGE_PASSWORD)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error: ", response.status_code)
    return response.json()