import requests
import json
from bs4 import BeautifulSoup

# from bs4 import BeautifulSoup
if __name__ == '__main__':
    endpoint = "https://www.transfermarkt.com/copa-libertadores/marktwerte/pokalwettbewerb/CLI"

    response = requests.get(endpoint)

    # Prettify the JSON response using json.dumps()
    # print(response.text)
    # prettified_json = json.dumps(response.json(), indent=8)
    # print(prettified_json)

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

    page = "https://www.transfermarkt.com/copa-libertadores/marktwerte/pokalwettbewerb/CLI"

    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    pageSoup = pageSoup.prettify()
    print(pageSoup)
