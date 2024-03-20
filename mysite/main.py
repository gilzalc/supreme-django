import json
import requests


def get_news_from_api(api_key, topic):
    base_url = 'https://newsapi.org/v2/everything?q=JohnCena&from=2024-03-11&to=2024-03-11&sortBy=popularity&apiKey=e4b99ccda2554eb3bde8bce8a4eb1b12'
    # params = {
    #     'apiKey': api_key,
    #     'category': topic,
    #     'country': 'uk'  # You can adjust the country parameter based on your preference
    # }

    response = requests.get(base_url)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        # print(articles)
        # Specify the file path
        file_path = "output.txt"
        text = articles[1].get('content', '')

        # Write the text to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        # Print a message indicating the file path
        print(f"Text has been written to '{file_path}'")
        print(articles[1].get('content', ''))
        for article in articles:
            print(article)

    else:
        print(
            f"Failed to retrieve news from API. Status code: {response.status_code}")


def get_books_api():
    """
    Funcion to get Json format of The books API using requests
    :return:books_data, Error if code different than 200
    """
    # Specify the URL of your API endpoint
    api_url = 'http://127.0.0.1:8000/api/books/'

    try:
        # Make a GET request to the API endpoint
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            books_data = response.json()
            return books_data
        else:
            # Print an error message if the request was not successful
            print(
                f"Error: Unable to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        print(f"Error: {e}")


if __name__ == '__main__':
    # Call the function and print the result

    books_data = get_books_api()
    pretty_books_data = json.dumps(books_data, indent=2)

    print(pretty_books_data)
    for x in books_data:
        print(x['id'])

    # get_news_from_api('e4b99ccda2554eb3bde8bce8a4eb1b12', 'Biden')
