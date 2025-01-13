.. _login_get_token:

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



To authenticate you can use the following Go code:

.. code-block:: go

	package main

	import (
		"bytes"
		"encoding/json"
		"fmt"
		"log"
		"net/http"
	)


	type Auth struct {
		Username string `json:"username"`
		Password string `json:"password"`
		Token    string `json:"token"`
	}

	func main() {
		auth := Auth{
			Username: "API_USERNAME",
			Password: "API_PASSWORD",
		}

		jsonData, err := json.Marshal(auth)
		if err != nil {
			log.Fatalln(err)
		}

		res, err := http.Post("https://api.bfore.ai/user/login", "application/json", bytes.NewBuffer(jsonData))
		if err != nil {
			log.Fatalln(err)
		}
		defer res.Body.Close()
		var responseAuth Auth
		if err := json.NewDecoder(res.Body).Decode(&responseAuth); err != nil {
			log.Fatalln(err)
		}

		fmt.Printf("Username: %s\nToken: %s\n", responseAuth.Username, responseAuth.Token)
	}

The code sends a request to the API and recieves a response in JSON.  You can parse the response and print the username and the token.