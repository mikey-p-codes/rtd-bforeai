import requests
from config import BASEURL, TOKEN
from pprint import pprint

'''Renew the token
This function renews the security token with an expire time starting from now'''

def renew_security_token():
    url = BASEURL + "user/renew"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        pprint(response.json(), indent=4)
    else: 
        print("Error: ", response.status_code)
    return response.json()
renew_security_token()