import requests
from config import BASEURL, TOKEN

'''
Get a new JWT for the current user
the function requires one of two parameters:
m: int, number of minutes before the token expires
d: int, number of days before the token expires
'''

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
        print(response.json())
    else: print("Error: ", response.status_code)