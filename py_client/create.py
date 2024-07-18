import requests
import json
from getpass import getpass

# from bs4 import BeautifulSoup
if __name__ == '__main__':
    auth_endpoint = "http://localhost:8000/api/auth/"
    # Define the authentication endpoint URL

    # Prompt for username and password
    username = input("Enter your username: ")
    print(username)
    password = input("Enter your password: ")
    print(password)
    auth_response = requests.post(auth_endpoint, data={'username': username, 'password': password})
    print(auth_response.status_code)
    if auth_response.status_code == 200:
        token = auth_response.json()['token']
        headers = {
            "Authorization": f"Token {token}"
        }
        endpoint = "http://127.0.0.1:8000/api/v2/books-api/"
        data = {
            "title": "aaa CIty", 'price': 10.22,
            "author": {"name": "MonGOL", "birth_date": "1996-01-05"}
        }
        res2 = requests.post(endpoint, json=data, headers=headers)

        # Prettify the JSON response using json.dumps()
        # print(res2.json())
        prettified_json = json.dumps(res2.json(), indent=8)
        print(prettified_json)
