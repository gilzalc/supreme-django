import requests
import json

endpoint = "http://127.0.0.1:8000/api/books/3/update/"

data = {
     "author": {"name":"Jorge jesus","birth_date": "2030-01-01"}}

if __name__ == '__main__':
    # response = requests.post(endpoint, json=data)
    res2 = requests.patch(endpoint, json=data)
    # Prettify the JSON response using json.dumps()
    prettified_json = json.dumps(res2.json(), indent=8)
    print(prettified_json)
