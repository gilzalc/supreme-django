import requests
import json

# from bs4 import BeautifulSoup
if __name__ == '__main__':
    endpoint = "http://127.0.0.1:8000/api/books/"
    data = {
        "title": "ABCD",
        "author": {"name": "Yotam the jew"}
    }
    # response = requests.post(endpoint, json=data)
    res2 = requests.post(endpoint,json=data)
    # Prettify the JSON response using json.dumps()
    # print(res2.json())
    prettified_json = json.dumps(res2.json(), indent=8)
    print(prettified_json)
