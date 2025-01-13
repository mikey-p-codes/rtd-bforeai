import requests
from config import BASEURL, CHANGE_PASSWORD

"""Change the password for the user:
The function takes the following parameters:
changePassword = {
    "username":"michael@bfore.ai",
    "old": "VrKSS1FPRYYFK12Ryfzhc0OYkuQ5tBQD",
    "new": "VrKSS1FPRYYFK12Ryfzhc0OYkuQ5tBQD",
    "confirm": "VrKSS1FPRYYFK12Ryfzhc0OYkuQ5tBQD"
}"""

def changePassword():
    url = BASEURL + "user/password"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=CHANGE_PASSWORD)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error: ", response.status_code)
    return response.json()