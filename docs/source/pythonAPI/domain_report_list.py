import requests
from pprint import pprint
from config import BASEURL, TOKEN

'''Get a detailed list from the domain report:
This function will query the domain and return only the information you want via the parameters:
d= string, the domain name to be analyzed
s=y/n include screenshots Default: y
w=y/n include whois information Default: y
n=y/n include DNS information Default: y
c=y/n include certificate information Default: y
st= string, start date for the report
en= string, end date for the report'''

def get_domain_report_list():
    url = BASEURL + "report/list"
    headers = { "Authorization": f"Bearer {TOKEN}" }
    params = {
        "d": "bfore.ai",
        "s": "n",
        "w": "n",
        "n": "n",
        "c": "y"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pprint(response.json(), indent=4)
    else: print("Error: ", response.status_code)
    return response.json()

get_domain_report_list() # test the function