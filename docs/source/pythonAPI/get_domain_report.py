import requests
from config import BASEURL, TOKEN
from pprint import pprint

'''This endpoint will generate and return a report with information about a specific domain. 
This function requires a parameter ?d= string, the domain name to be analyzed
This call can take some time to complete based on the size of the organization and the number of records to be analyzed.
The response will return a Screenshot, since we are viewing only data we have removed it from the response.
Finally we have printed the data in a pretty format using pprint'''

def get_domain_report():
    url = BASEURL + "report/domain"
    headers = { "Authorization": f"Bearer {TOKEN}" }
    params = { "d": "bfore.ai" }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if "Screenshot" in data:
            del data["Screenshot"]
        pprint(data, indent=2)
    else: print("Error: ", response.status_code)
    return response.json()

get_domain_report()