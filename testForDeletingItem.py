import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)


def test_is_first_product_deleted():
    assert response.json()["id"] == 1
