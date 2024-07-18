import requests

pk_to_delete = 1  # Replace with the ID of the book you want to delete

if __name__ == '__main__':

    endpoint = "http://127.0.0.1:8000/api/v2/books-api/10/"

    token = '77893ce174c9787fa220b5f230d981fa5ff3af7c'
    headers = {'Authorization': f'Token {token}'}

    response = requests.delete(endpoint, headers=headers)
    print(response.status_code)