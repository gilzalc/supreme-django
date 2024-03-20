import requests
import json

# from bs4 import BeautifulSoup
if __name__ == '__main__':
    endpoint = "http://127.0.0.1:8000/api/"
    res = requests.post(endpoint, json={'title': 'Hello Noam',
                                        'author': {'name': 'Noam'}})
    # Prettify the JSON response using json.dumps()
    prettified_json = json.dumps(res.json(), indent=8)
    print(prettified_json)
