import requests
import json
from getpass import getpass

# from bs4 import BeautifulSoup
if __name__ == '__main__':
    auth_endpoint = "http://localhost:8000/api/auth/"
    username = input("what is your username?\n")
    password = getpass()
    auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
    print(auth_response.json())
    if auth_response.status_code == 200:
        token = auth_response.json()['token']
        headers = {
            "Authorization": f"Bearer {token}"
        }

        endpoint = "http://localhost:8000/api/books/"
        get_response = requests.get(endpoint, headers=headers)
        print(get_response.json())


    # Prettify the JSON response using json.dumps()
    # prettified_json = json.dumps(res.json(), indent=8)
    # print(prettified_json)
