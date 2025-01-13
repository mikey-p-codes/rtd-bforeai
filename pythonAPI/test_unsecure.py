import requests
from config import BASEURL
"""Test service without token
Returns a greeting message, it’s useful to check the availability of the system. This
endpoint does not require token so anyone can invoke it."""

def test_unsecure():
    url = BASEURL + "test/unsecure"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json())  
    else:
        print("Error: ", response.status_code)
    return response.json()

test_unsecure() # test the function