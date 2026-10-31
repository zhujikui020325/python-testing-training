import json
import requests

# 1.写报告文件：用 with open 以写模式创建 report.txt（必带 encoding="utf-8"），写入两行：「登录用例：通过」和「下单用例：通过」（每行末尾带 \n）。再以读模式读回全部内容并打印。期望输出末尾多一个空行是正常现象——读回的内容自带换行符，print 又补了一个。
with open("report.txt", "w", encoding="utf-8") as f:
    f.write("登录用例：通过\n")
    f.write("下单用例：通过\n")

with open("report.txt", "r", encoding="UTF-8") as f:
    print(f.read())


# 2.json 互转：字典 case = {"name": "登录", "status": "pass"}。用 json.dumps(case, ensure_ascii=False) 转成字符串打印；打印它的 type()；再用 json.loads 变回字典，打印其中的 name。
case = {"name": "登录", "status": "pass"}
jcase = json.dumps(case, ensure_ascii=False)
print(jcase)
print(type(jcase))
dcase = json.loads(jcase)
print(dcase["name"])


# 3.第一个 GET：用 requests.get("https://jsonplaceholder.typicode.com/todos/1") 发请求。打印状态码；用 resp.json() 拿到字典后，取出 title 和 completed 分别打印。
resp = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(resp.status_code)
jresp = resp.json()
print(jresp["title"])
print(jresp["completed"])


# 4.第一个 POST：用 requests.post 访问 https://jsonplaceholder.typicode.com/posts，json= 参数传 {"title": "自动化测试", "body": "由脚本创建", "userId": 1}。打印状态码和返回 JSON 里的 id。
resp2 = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "自动化测试", "body": "由脚本创建", "userId": 1},
)
print(resp2.status_code)
print(resp2.json()["id"])
