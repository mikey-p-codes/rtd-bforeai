import requests
from config import BASEURL, TOKEN
from pprint import pprint

''' List of Agatha process executions;
This function returns a list of all process executions within a specific time frame. 
the last ID of the process to be analyzed.  
Additional parameters are:
st= string, start date
en= string, end date

start and end date are formatted as YYYY-MM-DDTHH:MM:SS'''

def agatha_process_list():
    url = BASEURL + "process/list"
    headers = { "Authorization": f"Bearer {TOKEN}" }
    params = { "st": "2025-01-12T:00:00:00",
               "en": "2025-01-13T:23:59:59" }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pprint(response.json(), indent=4)
    else: print("Error: ", response.status_code)
    return response.json()
agatha_process_list() # test the function