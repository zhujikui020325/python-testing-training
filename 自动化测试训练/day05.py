# 1.第一个类：定义类 Case，__init__ 接收 name 和 api 存为属性；方法 info() 返回 f"用例 {self.name}：接口 {self.api}"。造两个对象——「登录 / /api/login」和「下单 / /api/order」，分别打印 info() 的返回值。
class Case:
    def __init__(self, name, api):
        self.name = name
        self.api = api

    def info(self):
        return f"用例 {self.name}：接口 {self.api}"


c1 = Case("登录", "/api/login")
c2 = Case("下单", "/api/order")
print(c1.info())
print(c2.info())


# 2.
class Result:
    def __init__(self, name, status="pass"):
        self.name = name
        self.status = status

    def is_passed(self):
        return self.status == "pass"


r1 = Result("登录")
print(r1.is_passed())
print(Result("支付", "fail").is_passed())
print(Result("查询", "pass").is_passed())


# 3.捕获 KeyError：字典 data = {"code": 0}。把 print(data["msg"]) 包进 try，except KeyError 打印「字段缺失，已兜底」；try/except 的外面再打印一行「脚本还活着」，证明程序没崩。
data = {"code": 0}

try:
    print(data["msg"])
except KeyError:
    print("字段缺失，已兜底")

print("脚本还活着")


# 4.安全转换函数：定义函数 safe_int(text)，内部用 try 尝试 return int(text)，except ValueError 时 return None。打印 safe_int("100") 和 safe_int("abc")。
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return None


print(safe_int("100"))
print(safe_int("abc"))


# 5.raise 与捕获：定义函数 check_status(code)，code 不等于 200 就 raise ValueError(f"状态码异常：{code}")，等于 200 就返回「接口正常」。分别用 500 和 200 调用，每次都用 try 包住、except ValueError as e 打印 f"捕获到断言失败：{e}"。
def check_status(code):
    if code != 200:
        raise ValueError(f"状态码异常：{code}")
    return "接口正常"


try:
    print(check_status(500))
except ValueError as e:
    print(f"捕获到断言失败：{e}")

try:
    print(check_status(200))
except ValueError as e:
    print(f"捕获到断言失败：{e}")
