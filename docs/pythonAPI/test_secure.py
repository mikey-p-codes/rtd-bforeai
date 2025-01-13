import requests
from config import BASEURL, TOKEN

"""Test service with token
Returns a greeting message and use the security token to get the username of the
logged user, it’s useful to check the availability of the system and the status of the
token."""

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

test_secure() # test the function