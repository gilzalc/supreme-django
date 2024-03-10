import json
import requests


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
