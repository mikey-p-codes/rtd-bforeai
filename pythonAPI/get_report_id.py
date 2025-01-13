import requests
from config import BASEURL, TOKEN
from pprint import pprint

''' Retrieve a report from a previously run domain report with the report ID passed as paramater 
d= string, the report ID to be analyzed'''

def get_report_id():
    url = BASEURL + "report/get"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    params = { "d": "670e3292-582b-11ec-89e8-06a568c1d9e7" }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pprint(response.json(), indent=4)
    else: print("Error: ", response.status_code)

get_report_id() # test the function