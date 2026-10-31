import requests


resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "自动化测试", "body": "由脚本创建", "userId": 1},
)
print(resp.status_code)
print(resp.json()["id"])
