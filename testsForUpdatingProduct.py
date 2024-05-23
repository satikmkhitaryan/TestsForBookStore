import requests

url = 'https://jsonplaceholder.typicode.com/posts/2'
response = requests.get(url)


# /  Response  item's  body is changed
# // Response  item's  title is changed

def test_is_item_body_changed():
    assert response.json()["body"] == "bar"


def test_is_item_title_changed():
    assert response.json()["title"] == "foo"
