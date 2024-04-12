import requests
import json

endpoint = "http://127.0.0.1:8000/api/books/2/update/"

data = {'title': 'mossssss', 'price': 10.22,
        'author': {'name': 'aaaadfssaf', "birth_date": "1942-01-07"}}

if __name__ == '__main__':
    # response = requests.post(endpoint, json=data)
    res2 = requests.patch(endpoint, json=data)
    # Prettify the JSON response using json.dumps()
    prettified_json = json.dumps(res2.json(), indent=8)
    print(prettified_json)
