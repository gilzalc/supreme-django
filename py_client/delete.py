import requests
import json

endpoint = "http://127.0.0.1:8000/api/books/33/delete/"

if __name__ == '__main__':
    # response = requests.post(endpoint, json=data)
    res2 = requests.delete(endpoint)
    print(res2.status_code)
