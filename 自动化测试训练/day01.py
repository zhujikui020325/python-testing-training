# name = 100.0
# print(type(name))
# name = "allure"
# case = 100
# print(f"报告={name},用例有{case}条")
# price = "19.9"
# price1 = float(price)
# price2 = int(price1)
# print(price2)
# 1.商品信息：用变量保存 goods_name = "无线鼠标"、price = 89.9、stock = 120，用一条 f-string 打印出下面这句话。
goods_name = "无线鼠标"
price = 89.9
stock = 120
print(f"商品：{goods_name} 单价：{price}元 库存：{stock}件")
# 2.购物车小计：单价 89.9、数量 3，打印小计金额；再单独一行打印小计的 type()。想一想：为什么不是整数？答案写在注释里。
price_single = 89.9
num = 3
total = num * price_single
print(
    f"小计金额：{total}"
)  # float 参与运算，结果就是 float——num 是 int，price_single 是 float，两者相乘，float 会把结果的类型「传染」成 float
# 误差原因：计算机用二进制存小数，89.9 存进去的那一刻就有亿分之一级别的误差，乘 3 之后误差现形了。这就是为什么支付、对账系统里金额绝不能直接用 float
print(f"小计金额的类型：{type(total)}")
# 3.接口联调预演：库存数量从接口拿到的是字符串 "50"。把它转成整数，加上补货量 10，打印结果和它的类型。
total1 = "50"
total2 = int(total1) + 10
print(f"库存数量：{total1}，类型：{type(total1)}")
print(f"库存数量：{total2}，类型：{type(total2)}")
# 4.类型探查：分别打印 type(100)、type(99.9)、type("100")、type(True)，一行一个。
print(type(100))
print(type(99.9))
print(type("100"))
print(type(True))
# 5.故意踩坑：执行 price = "19.9" 然后 int(price)。运行之前，先把你猜会发生的事写进注释；然后运行，把完整报错贴给我，并用一句注释写出报错原因。
# 猜测：这里会报错，因为 int() 读不懂带小数点的字符串
price5 = "19.9"
print(int(price5))
# 原因：ValueError —— int() 只接受长得像整数的字符串，"19.9" 要先 float() 再 int()
