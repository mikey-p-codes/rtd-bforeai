import requests
from config import BASEURL, TOKEN 
from pprint import pprint

'''Retrieve the details of a process with the process ID passed as parameter p= string, the process ID to be analyzed
This function can return an empty list even if the response is 200 OK'''

def get_process_details():
    url = BASEURL + "process/get"
    headers = { "Authorization": f"Bearer {TOKEN}" }
    params = { "p": "290460" }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print(f"Status: {response.status_code}")
        pprint(response.json(), indent=4)
    else:
        print(f"Error: {response.status_code} - {response.text}")
    return response.json()
get_process_details() # test the function