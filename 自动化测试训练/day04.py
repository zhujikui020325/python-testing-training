import time


# 1.第一个函数：定义 say_hello(name)，用 return 返回 f"你好，{name}"（函数里不要 print）。调用两次，分别传「小明」和「Claude」，打印两次的返回值。
def say_hello(name):
    return f"你好，{name}"


print(say_hello("小明"))
print(say_hello("Claude"))


# 2.登录函数：定义 login(username, password)，账号是 admin 且密码是 123456 时返回 True，否则返回 False。打印 login("admin", "123456") 和 login("admin", "000000") 的返回值。
def login(username, password):
    if username == "admin" and password == "123456":
        return True
    else:
        return False


print(login("admin", "123456"))
print(login("admin", "000000"))


# 3.统计函数：定义 count_pass(statuses)，接收一个结果列表，函数内部用 for 加 if 数出 "pass" 的条数并 return。调用它，传入 ["pass", "fail", "pass", "pass", "fail"]，把返回值存变量后打印总结行。
def count_pass(statuses):
    count = 0
    for status in statuses:
        if status == "pass":
            count += 1
    return count


print(f"通过 {count_pass(['pass', 'fail', 'pass', 'pass', 'fail'])} 条")


# 4.默认参数：定义 check_api(url, timeout=5)，返回 f"请求 {url}，超时 {timeout} 秒"。打印 check_api("https://api.test.com") 和 check_api("https://slow.test.com", 30)。
def check_api(url, timeout=5):
    return f"请求 {url}，超时 {timeout} 秒"


print(check_api("https://api.test.com"))
print(check_api("https://slow.test.com", 30))


# 5.时间戳函数：在文件顶部 import time。定义 now()，返回 time.strftime("%H:%M:%S")；打印 f"用例开始执行，时间：{now()}"。
def now():
    return time.strftime("%H:%M:%S")


print(f"用例开始执行，时间：{now()}")


# github账号名称：zhujk_tester
