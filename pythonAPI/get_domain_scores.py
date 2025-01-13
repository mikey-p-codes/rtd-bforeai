import requests
from config import BASEURL, TOKEN
from pprint import pprint

''' Retrieve a list of domains processed and scored starting from a specific start and end date.
Time is represented as linux epoch time.

Note: The Linux epoch time for Jan 1, 1970, is 0.
Today's date in Linux Epoch time is: 1736804009 (for example, if today is January 13 2025)
It appears that if you attempt to go too far back you will get an internal server error'''

def get_domain_scores():
    url = BASEURL + "process/domains"
    headers = { "Authorization": f"Bearer {TOKEN}" }
    params = { "s": 1736800000, 
               "e": 1736890409 
              }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pprint(response.json(), indent=4)
    else: print("Error: ", response.status_code)
    return response.json()

get_domain_scores() # test the function