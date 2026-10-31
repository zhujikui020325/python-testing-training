# 1.用例清单管理：列表 cases = ["登录", "查询商品", "下单"]。打印用例总数和第一条用例；往队尾追加「支付」；再打印追加后的总数和最后一条用例。
cases = ["登录", "查询商品", "下单"]
print(f"共 {len(cases)} 条用例")
print(f"第一条用例：{cases[0]}")
cases.append("支付")
print(f"共 {len(cases)} 条用例")
print(f"最后一条用例：{cases[-1]}")

# 2.列表 statuses = ["pass", "fail", "pass", "pass", "fail"]。用 for 遍历，配合 if 统计两种结果各多少条，最后打印一行总结。提示：两个计数器都从 0 起步。
statuses = ["pass", "fail", "pass", "pass", "fail"]
pass1 = 0
fail = 0
for i in statuses:
    if i == "pass":
        pass1 += 1
    else:
        fail += 1
print(f"通过 {pass1} 条，失败 {fail} 条")


# 3.接口数据探查：字典 user = {"id": 1001, "name": "小明", "vip": True}。把 name 和 vip 的值取出来存变量，分别打印；再用 in 判断 "email" 这个键在不在，不在就打印「缺少邮箱字段」。
user = {"id": 1001, "name": "小明", "vip": True}
name = user["name"]
vip = user["vip"]
print(f"用户名：{name}")
print(f"VIP：{vip}")
if "email" not in user:
    print("缺少邮箱字段")


# get() 防坑：继续用上面的 user 字典。打印 user.get("email") 和 user.get("email", "未填写")；然后用自己的话写一句注释：为什么取可能不存在的字段时，.get() 比方括号安全。
print(user.get("email"))
print(user.get("email", "未填写"))
# 注意：使用get()方法取值时，如果键不存在，返回None；如果指定了默认值，则返回默认值。不使用get()方法取值时，如果键不存在，会报错KeyError。


# 5.
resp = {
    "code": 0,
    "data": {
        "list": [
            {"name": "无线鼠标", "price": 89.9},
            {"name": "机械键盘", "price": 199.0},
        ]
    },
}
if resp["code"] == 0:
    print("接口返回正常")
resp_data = resp["data"]
print(
    f"第一件商品：{resp_data['list'][0]['name']}，价格：{resp_data['list'][0]['price']}元"
)
for i in resp_data["list"]:
    print(f"商品：{i['name']}，价格：{i['price']}元")
