import pytest
import requests


# 1.登录检查参数化：定义函数 login(username, password)，返回「账号是 admin 且密码是 123456」的布尔结果（第 0004 课的写法）。用 parametrize 写一条测试函数，3 组数据：("admin", "123456", True)、("admin", "000000", False)、("guest", "123456", False)，断言 login 的返回值等于 expected。
@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin", "123456", True),
        ("admin", "000000", False),
        ("guest", "123456", False),
    ],
)
def test_login(username, password, expected):
    result = username == "admin" and password == "123456"
    assert result == expected


# 2.状态码分类参数化：定义函数 classify(status)，按第 0002 课练习 2 的规则返回分类文本（5xx→「服务器错误」、4xx→「客户端错误」、2xx→「成功」、其余→「未知状态码」）。参数化 4 组：(503, "服务器错误")、(404, "客户端错误")、(200, "成功")、(302, "未知状态码")，断言分类结果与期望一致。
def classify(status):
    if 500 <= status < 600:
        return "服务器错误"
    elif 400 <= status < 500:
        return "客户端错误"
    elif 200 <= status < 300:
        return "成功"
    else:
        return "未知状态码"


@pytest.mark.parametrize(
    "code,expected",
    [(503, "服务器错误"), (404, "客户端错误"), (200, "成功"), (302, "未知状态码")],
)
def test_classify(code, expected):
    assert classify(code) == expected


# 3.大模型响应形状：把课上第五节的 LLM_RESP 抄进你的文件。写两条测试：test_llm_keys 用 parametrize 遍历 ["choices", "usage"]，断言每个键都 in LLM_RESP；test_llm_content 精确断言嵌套取出的 content 等于「你好，我是助手」（精确值，不是 is not None——第 7 课立的规矩）。
LLM_RESP = {
    "choices": [{"message": {"role": "assistant", "content": "你好，我是助手"}}],
    "usage": {"total_tokens": 42},
}


@pytest.mark.parametrize(
    "key",
    [
        "choices",
        "usage",
    ],
)
def test_llm_keys(key):
    assert key in LLM_RESP


def test_llm_content():
    assert LLM_RESP["choices"][0]["message"]["content"] == "你好，我是助手"


# 4.
@pytest.mark.parametrize(
    "todo_id",
    [1, 2, 3],
)
def test_todo(todo_id):
    resp = requests.get(f"https://jsonplaceholder.typicode.com/todos/{todo_id}")
    assert resp.status_code == 200
    assert resp.json()["id"] == todo_id
