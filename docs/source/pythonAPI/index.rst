.. _login_get_token_py:

===============================
Execute login and get the token
===============================

Introduction!
-------------

Checks the user credential and return an object containing the logged user
information (user data, authorizations, active company, etc.) and the security
token!

.. _subtopic_section_1_label:

Authenticate and Get Token
--------------------------

+------------------------+-----------------------------------+
| Endpoint               | https://api.bfore.ai/user/login   |                        
+------------------------+-----------------------------------+
| JSON Request           | .. code-block:: json              |
|                        |                                   |
|                        |    {                              |
|                        |        "Username":"<username>",   |
|                        |        "Password":"<password>"    |
|                        |    }                              |
|                        |                                   |
+------------------------+-----------------------------------+