import requests
import json

# from bs4 import BeautifulSoup
if __name__ == '__main__':
    endpoint = "http://127.0.0.1:8000/detail/7/delete"

    response = requests.post(endpoint, data={'title': 'Noam moss'})

    # Prettify the JSON response using json.dumps()
    print(response.text)
    # prettified_json = json.dumps(res.json(), indent=8)
    # print(prettified_json)
