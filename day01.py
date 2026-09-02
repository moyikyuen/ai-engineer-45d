# print("Hello World")
# 第一部分：基础数据类型
# Python 里最常见的 5 种基础数据类型是：
age = 30
salary = 15000.5
job = "AI Engineer"
is_learning = True
result = None

# print(type(age))
# print(type(salary))
# print(type(job))
# print(type(is_learning))
# print(type(result))
#
# amount = "2500"
# print(type(amount))
#
# amount = float(amount)
# print(type(amount))
# print(amount + 500)

fruits = ["apple", "banana", "orange"]
# print(fruits)
# print(type(fruits))
# print(fruits[0])


# for item in data:
#     if 条件:
#         做事情
scores = [68, 92, 55, 81, 76]
# 把所有大于等于 80 的分数打印出来。
# for score in scores:
#     if score > 80:
#         print(score)

# total_score = 0
# for score in scores:
#     if score >= 80:
#         total_score += score
# print(total_score)

# append() 是 list 的方法，往列表末尾添加 一个元素。
# high_scores = []
# for score in scores:
#     if score >= 80:
#         high_scores.append(score)
# print(high_scores)

# names = ["Amy", "Bob", "Christopher", "Leo", "Jennifer"]
# #把名字长度大于 4 的名字收集进一个新列表。
# new_names = []
# for name in names:
#     if len(name) > 4:
#         new_names.append(name)
# print(new_names)

#set 去重
# names = ["Amy", "Bob", "Amy", "Leo", "Bob"]
# unique_names = set(names)
# print(unique_names)
# #从这个列表里取第 2 个到第 4 个元素。Python 切片是 左闭右开。左包括，右不包括
# #要返回 ['Bob', 'Leo', 'Jennifer']
# print(names[1:4])
# #如果想取最后一个,"Bob"
# print(names[-1])

# if 和 多条件
# score = 85
#
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")

# age = 25
# has_ticket = True
# if age >= 18 and has_ticket:
#     print("可以进入")

# payment = "wechat"
# if payment == "wechat" or payment == "alipay":
#     print("支持该支付方式")

# is_paid = False
# if not is_paid:
#     print("尚未付款")

#practice
# amount = 2500
# transaction_type = "expense"
# if transaction_type == "expense" and amount >= 2000:
#     print("大额支出")
# elif transaction_type == "expense" and amount < 2000:
#     print("普通支出")
# else:
#     print("非支出交易")

#break 和 continue 学习
# 作用是：直接结束整个循环。

# names = ["Amy", "Bob", "Amy", "Leo", "Bob"]
# for name in names:
#     if name == "Leo":
#         break    #相当于stop all
#     print(name)
#
# for name in names:
#     if name == "Amy":
#         continue #相当于skip
#     print(name)

# # practice
# numbers = [10, 20, 30, 40, 50]
# #用 break：打印数字，但遇到 30 就停止。
# number1= []
# for number in numbers:
#     if number == 30:
#         break
#     number1.append(number)
# print(number1)
#
# # 用 continue：打印数字，但跳过 30。
# number2= []
# for number in numbers:
#     if number == 30:
#         continue
#     number2.append(number)
# print(number2)

# range() #：生成一段数字
# for number in range(5):
#     print(number)
# for number in range(1, 5):
#     print(number)
# # range(开始, 结束, 步长step),也就是每次加 2。
# for number in range(0, 10, 2):
#     print(number)
# # 练习
# for number in range(1, 6):
#     print(number)

# enumerate()：同时拿到“序号 + 内容” 相当于map-index
# names = ["Amy", "Bob", "Amy", "Leo", "Bob"]
# for index, name in enumerate(names):
#     print(index, name)
# for index, name in enumerate(names, start=1): #序号从1开始
#     print(index, name)
# #使用场景：
# # for index, file in enumerate(files, start=1):
# #     print(f"正在处理第 {index} 个文件：{file}")
#
# # zip()：把两组数据一一配对
# names = ["Amy", "Bob", "Leo"]
# scores = [90, 80, 70]
# for name, score in zip(names, scores):
#     print(name, score)

#练习1
# 用 range() 打印：
# 1
# 2
# 3
# 4
# 5

# for a in range(1,6):
#     print(a)
#
# # 第二题：
# # 用：
# names = ["Amy", "Bob", "Amy", "Leo", "Bob"]
# # 和 enumerate() 输出：
# # 1 Amy
# # 2 Bob
# # 3 Amy
# # 4 Leo
# # 5 Bob
#
# for index, n in enumerate(names):
#     print(index,n)
#
# # 第三题：
# names = ["Amy", "Bob", "Leo"]
# scores = [95, 80, 88]
# # 用 zip() 输出：
# # Amy 95
# # Bob 80
# # Leo 88
#
# for n,s in zip(names,scores):
#     print(n,s)

# while 循环
# for 适合：我知道要遍历一组数据。
# while 适合：只要某个条件还成立，就一直重复。
# # while 会不断检查条件，只要条件为 True，就继续执行。
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# # 字符串学习
# text = "  hello python  "
# print(text.strip()) #去掉首尾空格
# print(text.replace("python", "AI"))
# print(text.strip().startswith("hello")) #startswith()：判断是不是以某内容开头，返回布尔值
# print(text.strip().endswith("python")) #判断结尾，返回布尔值
#
# # split = 字符串 → list
# # join  = list → 字符串
# text = "Amy,Bob,Leo"
# names = text.split(",") #按照某个分隔符，把一个字符串拆成 list。
# print(names)
#
# names = ["Amy", "Bob", "Leo"]
# text = ",".join(names)
# print(text)
# print(type(text))
#
# name = "Amy"
# score = 95
# print(f"{name} 的分数是 {score}")
#
# amount = 4000
# print(f"金额：¥{amount:,.2f}") #,：千位分隔  .2f：保留两位小数

# # # 你做一个小练习：
# text = "Amy|Bob|Leo"
# # 要求：
# # 用 split() 变成 list
# split_sample=text.split("|")
# print(split_sample)
# # 再用 join() 变成：
# # Amy, Bob, Leo
# join_sample=",".join(split_sample)
# print(join_sample)
# # 最后用 f-string 输出：
# # 一共有 3 个名字：Amy, Bob, Leo
# print(f"一共有 {len(split_sample)} 个名字：{text.replace('|',',')}")

# # 切片
# text = "Python"
# print(text[:3])
# print(text[::2]) #数据[start:end:step]
# 练习
# text = "AIEngineer"
# # 请分别写出：
# # 取前两个字符
# print(text[:2])
# # 取最后 3 个字符
# print(text[-3:])
# # 每隔 2 个字符取一次
# print(text[::2])
# # 笔记
# # text[2] → 取一个
# # text[2:5] → 取一段

# # 容器类型
# point = (100, 200)
# print(type(point))
#
# print(point[0])   # 100
# print(point[1])   # 200
#
# # list 可以修改，tuple 通常不能修改。
# # list  = 一组可以改的数据
# # tuple = 一组不希望被改的数据
# names = ["Amy", "Bob"]
# names[0] = "Leo"
# # point[0] = 300  会报错
# transaction = {
#     "counterparty": "深圳A科技有限公司",
#     "amount": 2500,
#     "type": "expense"
# }
# print(transaction["amount"])
# transaction["amount"] = 3000
# transaction["currency"] = "CNY"
#
# print(transaction)
# print(transaction.get("amount"))
# print(transaction["amount"])
# # transaction["date"] #没有的值会报错KeyError: 'date'
# print(transaction.get("date")) #返回none

# #练习
# user = {
#     "name": "Amy",
#     "age": 25
# }
# # 请你自己写代码完成：
# # 把 age 改成 26
# user["age"] =26
# # 新增 "job": "AI Engineer"
# user["job"] = "AI Engineer"
#
# # 用 .get() 读取 "email"，如果没有就返回 "暂无邮箱"
# if user.get("email") is None:
#     print("暂无邮箱")
# print(user.get("email", "暂无邮箱")) #推荐写法
#
# # 最后打印整个 user
# print(user)

# user = {
#     "name": "Amy",
#     "age": 26,
#     "job": "AI Engineer"
# }
# #
# # print(user.keys())
# # print(user.values())
# print(user.items())
# for key, value in user.items():
#     print(key, value)

# #练习
# product = {
#     "name": "MacBook",
#     "price": 9999,
#     "stock": 5
# }
#
# # 要求打印成：
# # name MacBook
# # price 9999
# # stock 5
#
# for key,value in product.items():
#     print(key, value)

# user = {
#     "name": "Amy",
#     "job": {
#         "title": "AI Engineer",
#         "salary": 25000
#     }
# }
#
# print(user["job"]["salary"])
#
# data = {
#     "users": [
#         {
#             "name": "Amy",
#             "age": 25
#         },
#         {
#             "name": "Bob",
#             "age": 30
#         }
#     ]
# }
#
# # 如果要拿 Bob：
# print(data["users"][1]["name"])

#练习
# data = {
#     "company": "OpenAI",
#     "employees": [
#         {
#             "name": "Amy",
#             "skills": ["Python", "SQL"]
#         },
#         {
#             "name": "Bob",
#             "skills": ["Java", "Docker"]
#         }
#     ]
# }
# # 请你写两行代码：
# # 打印 "Bob"
# print(data["employees"][1]["name"])
# # 打印 Bob 的 "Docker"
# print(data["employees"][1]["skills"][1])


#函数学习
# def say_hello(name): #say_hello是函数名
#     print(f"Hello，{name}")
# say_hello("luna")
#
# def add(a, b):
#     result = a + b
#     return result
#
# print(add(1,2))
#练习
# 写一个函数：calculate_total
# 接收两个参数：price quantity
# 返回：price * quantity
# 然后调用：calculate_total(100, 3)
#
# def calculate_total(price,quantity):
#     return price * quantity
#
# result = calculate_total(100, 3)
# print(result)
#
# def calculate_discount(price, discount):
#     # 这里自己完成
#     return price * discount
# result = calculate_discount(1000, 0.8)
# print(result)

# def greet(name, language="zh"):
#     if language == "zh":
#         return f"你好，{name}"
#     else:
#         return f"Hello, {name}"
#
# language="zh"
# print(greet("Amy"))
# print(greet("Amy", "en"))
# print(greet(name="Amy", language="en"))
#
# def calculate_price(price, quantity=1):
#     return price * quantity
#
# print(calculate_price(price=100))
# print(calculate_price(price=100, quantity=3))

# 学习：作用域 scope
# x = 100
# def test():
#     x = 20 #这个x，只在这个def里生效，函数里的变量，默认只在函数里面有效。这就是局部作用域。
#     print(x)
#
# test()
# print(x)

# 学习*args 和 **kwargs
# 所以最简单记法：
# *args → 多个值 → tuple
# **kwargs → 多个 key=value → dict
# def add_numbers(*args): #*args = 把多个传进来的值收进一个 tuple。
#     total = 0
#     for number in args:
#         total += number
#     return total
#
# print(add_numbers(1, 2))
# print(add_numbers(1, 2, 3, 4))
# #
# def test(*args):
#     print(args)
# #
# test("Amy", 20, True)
#
# def show_user(**kwargs): #**kwargs 用来接收不确定数量的关键字参数：
#     print(kwargs)
#
# show_user(name="Amy", age=25, job="AI Engineer")
#
#
# #练习
# def show_info(**kwargs):
#     # 遍历 kwargs，把 key 和 value 打印出来
#     for key, value in kwargs.items():
#         print(key, value)
#
# show_info(name="Amy", age=25, job="AI Engineer")

# 学习：条件运算：or 和 not
# payment = "wechat"
# if payment == "wechat" or payment == "alipay":
#     print("支持该支付方式")
#
# is_paid = False
# if not is_paid:
#     print("尚未付款")
#
# #练习
# email = ""
# phone = "13800000000"
# # 要求：
# # 如果 email 或 phone 至少有一个有值，打印 "存在联系方式"；
# # 如果两个都没有，打印 "没有联系方式"。
#
# if email or phone:
#     print("存在联系方式")
# else:
#     print("没有联系方式")


# 测试一
#假设我们现在有一组银行交易：
# transactions = [
#     {
#         "counterparty": "深圳A科技有限公司",
#         "amount": 2500.00,
#         "type": "expense",
#         "currency": "CNY"
#     },
#     {
#         "counterparty": "广州B贸易有限公司",
#         "amount": 800.00,
#         "type": "expense",
#         "currency": "CNY"
#     },
#     {
#         "counterparty": "深圳A科技有限公司",
#         "amount": 3200.00,
#         "type": "income",
#         "currency": "CNY"
#     },
#     {
#         "counterparty": "上海C咨询有限公司",
#         "amount": 1500.00,
#         "type": "expense",
#         "currency": "CNY"
#     },
#     {
#         "counterparty": "广州B贸易有限公司",
#         "amount": 5000.00,
#         "type": "income",
#         "currency": "CNY"
#     }
# ]
#
# big_expenses = []
# #Task 1：筛选 找出：type == "expense" 并且 amount >= 1500
# for transaction in transactions:
#     if transaction["type"] == "expense" and transaction["amount"] >= 1500:
#         big_expenses.append(transaction)
#
# print(big_expenses)
#
# # Task 2：计算总额 计算这些符合条件的支出总额。预期：4000.0
# total = 0
# for expense in big_expenses:
#     total += expense["amount"]
# print(total)
#
# # Task 3：去重 找出整个交易列表中所有不同的交易对手方。 要求使用：set
# # # 结果应该包含：深圳A科技有限公司 广州B贸易有限公司 上海C咨询有限公司
# companies = []
# for company in transactions:
#     companies.append(company["counterparty"])
# a = set(companies)
# print(a)
#
# # Task 4：切片, 取：前 3 条记录。必须使用：[:]
# print(transactions[:3])
#
# # Task 5：格式化输出，“共发现 2 笔大额支出，总金额为 ¥4,000.00” （大于1000）
# print(f"共发现 {len(big_expenses)} 笔大额支出，总金额为 ¥{total:,.2f}")
#
# # Task 6：封装成函数
# def valid_records(minimum_amount, all_transactions):
#     records = []
#     for transaction in all_transactions:
#         if transaction["amount"] >= minimum_amount and transaction["type"] == "expense":
#             records.append(transaction)
#     return records
#
# def add_up(records):
#     total = 0
#     for record in records:
#         total += record["amount"]
#     return total
#
# def get_big_expenses(all_transactions, minimum_amount):
#     records = valid_records(minimum_amount,all_transactions)
#     count = len(records)
#     total = add_up(records)
#     text = f"共发现 {count} 笔大额支出，总金额为 ¥{total:,.2f}"
#     return text
#
#
# result = get_big_expenses(
#         transactions,
#         minimum_amount=1500
#     )
#
# print(result)

# 测试二
# orders = [
#     {"customer": "Amy", "amount": 1200, "status": "paid"},
#     {"customer": "Bob", "amount": 800, "status": "unpaid"},
#     {"customer": "Leo", "amount": 2600, "status": "paid"},
#     {"customer": "Amy", "amount": 500, "status": "paid"},
#     {"customer": "Bob", "amount": 1800, "status": "paid"}
# ]
# # 你完成 5 题，
# # 1. 找出所有 status == "paid" 且 amount >= 1000 的订单，放进新列表 valid_orders。
# # 2. 计算这些订单的总金额。
# # 3. 找出所有不同客户名，要求用 set()。
# # 4. 写一个函数：返回所有“已付款且金额达到最低值”的订单
# #     --->共发现 3 笔有效订单，总金额为 ¥5,600.00
# def valid_orders(all_orders,minimim_amount):
#     "过滤出符合条件的订单"
#     records = []
#     for order in all_orders:
#         if order["status"] == "paid" and order["amount"] >= minimim_amount:
#             records.append(order)
#     return records
#
# def amount_add_up(valid_records):
#     "加总符合条件的金额"
#     total = 0
#     for record in valid_records:
#         total += record["amount"]
#     return total
#
# def unique_customers(all_orders):
#     "所有用户名，去重返回set"
#     customers = []
#     for order in all_orders:
#         customers.append(order["customer"])
#     unique_c = set(customers)
#     return unique_c
#
# def text_respond(count,total):
#     text = f"共发现 {count} 笔有效订单，总金额为 ¥{total:,.2f}"
#     return text
#
# def filter_orders(all_orders, minimum_amount):
#     valid_records = valid_orders(all_orders, minimum_amount)
#     total = amount_add_up(valid_records)
#     count = len(valid_records)
#     text = text_respond(count,total)
#     return text
#
# result = filter_orders(orders, minimum_amount=1000)
#
# print(result)
# print(unique_customers(orders))
#
#
#
# # 复习：
# orders = [
#     {"customer": "Amy", "amount": 1200, "status": "paid"},
#     {"customer": "Bob", "amount": 800, "status": "unpaid"},
#     {"customer": "Leo", "amount": 2600, "status": "paid"},
#     {"customer": "Amy", "amount": 500, "status": "paid"},
# ]
#
# # 1.
# # 打印所有 status == "paid" 的 customer
# valid_customers = []
# for order in orders:
#     if order["status"] == "paid":
#         valid_customers.append(order["customer"])
# print(set(valid_customers))
#
# # 2.
# # 把 amount >= 1000 的订单放进一个新 list：big_orders
# big_orders = []
# for order in orders:
#     if order["amount"] >= 1000:
#         big_orders.append(order)
# print(big_orders)
#
# # 3.
# # 写一个函数 calculate_total(records)
# # 返回 records 中所有 amount 的总和
# def calculate_total(records):
#     total = 0
#     for order in records:
#         total += order["amount"]
#     return total
#
# # 4.
# # 调用 calculate_total(big_orders)
# # 最后输出：
# # 大额订单共 2 笔，总金额为 ¥3,800.00
# count = len(big_orders)
# total = calculate_total(big_orders)
#
# print(f"大额订单共 {count} 笔，总金额为 ¥{total:,.2f}")

# ""
