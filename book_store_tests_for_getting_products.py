import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)


# 1 / Status code is equal to 200
def test_is_requests_status_code_equal_to_200():
    assert response.status_code == 200


# 3/response list length is > 1
def test_is_response_list_length_greeter_then_1():
    assert len(response.content) > 1


# // 4/ Response each item contains userId
def test_does_each_item_contain_userId():
    # assert response.json()[0]["userId"] is not None
    assert "userId" in response.json()[0].keys()


# // 5/ Response each item contains Id
def test_does_each_item_contain_id():
    # assert response.json()[0]["id"] is not None
    assert "id" in response.json()[0].keys()


# // 6/ Response each item contains title
def test_does_each_item_contain_title():
    # assert response.json()[0]["title"] is not None
    assert "title" in response.json()[0].keys()


# // 7/ Response each item contains body
def test_does_each_item_contain_body():
    # assert response.json()[0]["body"] is not None
    assert "body" in response.json()[0].keys()
