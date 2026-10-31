# 练习1：登录校验预演：变量 username = "admin"、password = "123456"。如果账号是 admin 且密码是 123456，打印「登录成功，开始测试」；否则打印「账号或密码错误」。写完后把 username 改成别的值再跑一次，验证另一个分支也通，两种输出都要贴。
username = "admin"
password = "123456"
if username == "admin" and password == "123456":
    print("登录成功，开始测试")
else:
    print("账号或密码错误")
username = "user"
if username == "admin" and password == "123456":
    print("登录成功，开始测试")
else:
    print("账号或密码错误")
# 练习2：状态码分类：变量 status = 503。500 到 599 打印 f"状态码 {status}：服务器错误"；400 到 499 打印「客户端错误」；200 到 299 打印「成功」；其余打印「未知状态码」。只用今天学的 if/elif/else 和比较、逻辑运算。
status = 503
if status >= 500 and status <= 599:
    print(f"状态码 {status}：服务器错误")
elif status >= 400 and status <= 499:
    print(f"状态码 {status}：客户端错误")
elif status >= 200 and status <= 299:
    print(f"状态码 {status}：成功")
else:
    print(f"状态码 {status}：未知状态码")

# 练习3：批量执行用例：用 for 加 range，打印「正在执行用例 1」到「正在执行用例 5」共 5 行，循环结束后再打印一行「本轮共执行 5 条用例」。
i = 1
for i in range(1, 6):
    print(f"正在执行用例 {i}")
print(f"本轮共执行 {i} 条用例")

# 练习4：超时重试预演：变量 retry = 0。用 while 循环，retry 小于 3 时打印 f"第 {retry + 1} 次请求接口……"，并让 retry 每圈加 1；循环结束后打印「3 次请求全部超时，标记用例失败」。
retry = 0
while retry < 3:
    print(f"第 {retry + 1} 次请求接口……")
    retry += 1
print("3 次请求全部超时，标记用例失败")

# 练习5：跳过与终止：用 for 加 range 遍历用例编号 1 到 8。编号等于 3 的是失败用例，跳过它（不打印任何内容）；编号等于 6 时假设遇到致命错误，直接终止整个循环；其余编号打印 f"用例 {i} 通过"。想清楚：判断致命错误的 if 必须放在打印之前。
i = 1
for i in range(1, 9):
    if i == 3:
        continue
    if i == 6:
        break
    print(f"用例 {i} 通过")
