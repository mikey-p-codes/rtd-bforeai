import requests
from config import BASEURL, TOKEN
from pprint import pprint

'''This function retrieves details about a monitored domain with the domain ID passed as parameter d= string,'''

def get_domain_info():
    url = BASEURL + "domain/info"
    headers = { "Authorization": f"Bearer {TOKEN}" }
    params = { "d": "domain" }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pprint(response.json(), indent=4)
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return response.json()

   
    
    