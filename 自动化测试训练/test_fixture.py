import pytest
import requests


# 1.返回值的魔法：定义 fixture base_url 返回 jsonplaceholder 地址；写一条测试用它 GET f"{base_url}/todos/1"，断言状态码 200。
@pytest.fixture
def api_base():
    return "https://jsonplaceholder.typicode.com"


def test_get_posts(api_base):
    resp = requests.get(f"{api_base}/posts")
    assert resp.status_code == 200


# 2.yield 前置与后置：模块级列表 cleanup_log = []；fixture resource 在 yield 前 cleanup_log.append("打开资源")、yield "资源就绪"、yield 后 cleanup_log.append("关闭资源")。写两条测试使用它（各断言 resource 的值），再写一条不使用 fixture 的测试 test_cleanup_happened，断言 cleanup_log == ["打开资源", "关闭资源", "打开资源", "关闭资源"]——用它证明每条用例都走了一轮「前置 + 后置」。
cleanup_log = []


@pytest.fixture
def resource():
    cleanup_log.append("打开资源")
    yield "资源就绪"
    cleanup_log.append("关闭资源")


def test_resource(resource):
    assert resource == "资源就绪"


def test_resource2(resource):
    assert resource == "资源就绪"


def test_cleanup_happened():
    assert cleanup_log == ["打开资源", "关闭资源", "打开资源", "关闭资源"]


# 3.登录前置 fixture：fixture api_token 向 httpbin.org/post 发登录请求（第 7 课的写法），返回回显里的 username 当作 Token；写一条测试断言拿到的 Token 等于 "admin"。
@pytest.fixture
def token():
    resp = requests.post(
        "https://httpbin.org/post", json={"username": "admin", "password": "123456"}
    )
    return resp.json()["json"]["username"]


def test_get_token(token):
    assert token == "admin"


# 4.fixture + parametrize 同台：parametrize todo_id 为 [1, 2, 3]，测试参数是 (base_url, todo_id)——base_url 来自你第 1 题的 fixture，断言状态码 200 且返回 id 等于传入的 todo_id。
@pytest.mark.parametrize(
    "todo_id",
    [1, 2, 3],
)
def test_get_todo_by_id(api_base, todo_id):
    resp = requests.get(f"{api_base}/todos/{todo_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == todo_id
