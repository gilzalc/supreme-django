import requests
import json

# from bs4 import BeautifulSoup
if __name__ == '__main__':
    token = '77893ce174c9787fa220b5f230d981fa5ff3af7c'
    headers = {'Authorization': f'Token {token}'}
    auth_endpoint = "http://localhost:8000/api/v2/books-api/"
    get_response = requests.get(auth_endpoint, headers=headers)
    print(get_response.json(

    ))

    # Prettify the JSON response using json.dumps()
    # prettified_json = json.dumps(get_response.json(), indent=8)
    # print(prettified_json)
