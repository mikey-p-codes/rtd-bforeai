import requests
from config import BASEURL, TOKEN   

"""Logout the user and expire the token"""

def expire_security_token():
      headers = {
            "Authorization": f"Bearer {TOKEN}"
      }
      url = BASEURL + "user/logout"
      response = requests.get(url, headers=headers)
      if response.status_code == 200:
            print(response.json())
      else:
            print("Error: ", response.status_code)
      return response.json()

## Test the function
expire_security_token()