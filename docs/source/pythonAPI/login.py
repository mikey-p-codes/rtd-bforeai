import requests
from config import BASEURL, AUTH

"""Execute the login and get the token
Checks the user credential and returns an object containing the logged in user
information (user data, authorizations, active company, etc.) and the security
token. This token is required to access the other endpoints."""

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

login()