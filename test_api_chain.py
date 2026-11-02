import requests


def test_login():
    resp = requests.post(
        "https://httpbin.org/post", json={"username": "admin", "password": "123456"}
    )
    assert resp.status_code == 200
    assert resp.json()["json"]["username"] == "admin"


def test_get_token():
    resp = requests.get(
        "https://httpbin.org/bearer", headers={"Authorization": "Bearer test-token-123"}
    )
    assert resp.status_code == 200
    assert resp.json()["authenticated"] == True


def test_query():
    resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert resp.status_code == 200
    assert resp.json()["title"] is not None


def test_order():
    resp = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "自动化测试", "body": "由脚本创建", "userId": 1},
    )
    assert resp.status_code == 201
    assert resp.json()["id"] == 101
