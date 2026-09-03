# #day 02｜文件、JSON、路径
# from pathlib import Path
# import json
# # 今天的目标是让你理解并能自己完成：
# # Python 内存里的数据 → 写入文件 → 从文件读回来 → JSON 保存/读取 → 用 pathlib 管理文件路径
# # with open("hello.txt", "w", encoding="utf-8") as file:
# #     file.write("Hello Python")
# # 练习
# # 用 Python 创建：day2_note.txt
# # 内容写：今天开始学习 Python 文件处理
#
# # with open("day2_note.txt","w",encoding="utf-8") as file:
# #     file.write("今天开始学习 Python 文件处理")
#
# # with open("day2_note.txt", "r", encoding="utf-8") as file:
# #     content = file.read()
#
# # with open("day2_note.txt", "a", encoding="utf-8") as file:
# #    file.write("\n下一步学习 JSON")
# #
# # with open("day2_note.txt", "r", encoding="utf-8") as file:
# #     content = file.read()
# #
# # print(content)
#
# import json
# from sys import path
#
# # user = {"name": "Amy",
# #         "age": 25,
# #         "skills": ["Python", "SQL"]}
# # with open("user.json", "w", encoding="utf-8") as file:
# #     json.dump(user, file, ensure_ascii=False, indent=2)
# #
# # with open("user.json", "r", encoding="utf-8") as file:
# #         data = json.load(file)
# # print(data)
# # print(type(data))
#
# product = {
#     "name": "MacBook",
#     "price": 9999,
#     "stock": 5
# }
# #
# # with open("products.json", "w",encoding= "utf-8") as file:
# #     json.dump(product, file, ensure_ascii=False, indent=2)
# #
# # with open("products.json", "r", encoding="utf-8") as file:
# #     data = json.load(file)
# # print(data)
# # print(data["price"])
#
# # user = {
# #     "name": "Amy",
# #     "age": 25
# # }
# #
# # # Python → JSON 文件
# # with open("users.json", "w", encoding="utf-8") as file:
# #     json.dump(user, file, ensure_ascii=False, indent=2)
# #
# # # JSON 文件 → Python
# # with open("users.json", "r", encoding="utf-8") as file:
# #     users = json.load(file)
# #
# # print(users)
# # print(type(users))
#
# # # Python → JSON 字符串
# # json_text = json.dumps(
# #     user,
# #     ensure_ascii=False,
# #     indent=2
# # )
# #
# # print(json_text)
# # print(type(json_text))
# #
# # # JSON 字符串 → Python
# # users = json.loads(json_text)
# #
# # print(users)
# # print(type(users))
#
#
#
# from day01 import result
#
# # file_path = Path("products.json")
#
# # print(file_path)              #路径本身：products.json
# # print(file_path.exists())     #这个路径对应的文件/文件夹是否存在
# # print(file_path.name)         #完整文件名：products.json
# # print(file_path.stem)         #去掉后缀后的文件名：products
# # print(file_path.suffix)       #文件扩展名：.json
# # print(file_path.parent)       # parent：父级目录，这里 . 表示当前目录
#
# # base = Path("data")             # 创建一个路径对象：data
# # folder = base / "users"         # 拼接路径：data/users
# # file_path = folder / "user.json"  # 拼接文件路径：data/users/user.json
# # print(file_path)                # 输出：data/users/user.json
#
# # folder = Path("data/users")     # 表示 data/users 这个目录路径
# # # print(folder.exists())        # 判断这个路径是否存在，返回 True / False
# # # print(folder.is_dir())        # 判断这个路径是否是文件夹，返回 True / False
# #
# # folder.mkdir(
# #     parents=True,               # 如果上级目录 data 不存在，也一起创建
# #     exist_ok=True               # 如果文件夹已经存在，不报错
# # )
# #
# # print(folder.exists())          # 创建后通常输出 True
# # print(folder.is_dir())          # 是文件夹，输出 True
#
# # # 题 1：拼路径
# # base = Path("data")
# # folder_path = base / "orders"
# # path = folder_path / "orders.json"
# # print(path)
# #
# # # 题 2：创建文件夹
# # folder = Path(path)
# # print(folder.exists())
# # folder.mkdir(parents=True, exist_ok=True)
# # print(folder.exists())
# #
# # # 题 3：综合题
# # product = {
# #     "name": "MacBook",
# #     "price": 9999
# # }
# #
# # folder1 = base / "products"
# # products_path = folder1 / "product.json"
# # print(products_path)
# #
# # folder1.mkdir(parents=True, exist_ok=True) #创建文件夹
# # print(folder1.exists())
# #
# # with open(products_path,"w",encoding="utf-8") as file:
# #  json.dump(product,file, ensure_ascii=False, indent=2)
# #
# # print(products_path.exists())                 # 判断 product.json 是否存在
# # print(products_path.is_file())                # 判断 product.json 是否是文件
# #
# # with open(products_path,"r",encoding="utf-8") as file:
# #     results = json.load(file)
# #     print(results["price"])
#
#
# # file_path = Path("data/products/product.json")   # 相对路径：从当前运行目录开始找
# # print(Path.cwd())                                # 当前工作目录：程序当前从哪里运行
# # print(file_path)                                 # 相对路径:从当前工作目录出发,输出：data/products/product.json
# # print(file_path.resolve())                       # 转成绝对路径：从根目录开始算->当前文件
# #
# # print(file_path.exists())
# # print(file_path.is_dir())
# # print(file_path.is_file())
#
# # base = Path("data")
# # folder = base / "reports"
# # folder.mkdir(parents=True, exist_ok=True)
# # file_path = folder/"summary.json"
# # print(folder.exists())
# # print(folder.is_dir())
# # print(file_path.exists())
# # print(file_path.suffix)
#
# # base = Path("data")
# # folder = base / "reports"
# # file_path = folder / "summary.json"
# #
# # report = {
# #     "total": 3800,
# #     "count": 3
# # }
# #
# # print(folder.exists())
# # with open(file_path, "w",encoding="utf-8") as file:
# #     json.dump(report, file, ensure_ascii=False, indent=4)
# #
# # with open(file_path, "r",encoding="utf-8") as file:
# #     report_data = json.load(file)
# #
# # print(report_data["total"])
# # print(file_path.is_file())
#
#
# # file_path = Path("note.txt")
# # file_path.write_text("今天继续学习 Python", encoding="utf-8")   # 直接写入文本文件
# # content = file_path.read_text(encoding="utf-8")               # 直接读取整个文本文件
# #
# # print(content)
#
# # file_path = Path("hello.txt")
# # file_path.write_text("Hello Python", encoding="utf-8") #什么时候要encoding="utf-8"？
# # content = file_path.read_text(encoding="utf-8")
# # print(content)
# # print(type(content))
#
# folder = Path("data")
# # json_files = list(folder.glob("*.json"))  # 找 data 目录下所有 .json 文件.只找 当前这一层目录，不会自动深入子文件夹。
# # # folder.glob("*.json")    # 查找当前目录下所有 .json 文件
# # # *                        # 通配符，表示“任意文件名”
# # # list(...)                # 把查找结果转换成 list
# # print(json_files)
#
# # excel_file = list(folder.rglob("*.xlsx"))
# # print(excel_file)
#
# # from pathlib import Path
# #
# # folder = Path("data")                       # 要扫描的目录
# # json_files = list(folder.rglob("*.json"))  # 找到所有 json 文件
# #
# # for file_path in json_files:               # 一个一个拿出文件路径
# #     print(file_path)                        # 打印当前正在处理的文件
#
#
#
# # folder = Path("data")
# # json_files = list(folder.rglob("*.json"))
# # path = Path("data/orders/orders.json")
# # print(path.exists())
# # print(path.is_file())
# # print(path.is_dir())
#
# # with open(path,"w",encoding="utf-8") as f:
# #     json.dump(product,f,ensure_ascii=False,indent=4)
#
# # for file_path in json_files:
# #     if not file_path.is_file():
# #         continue
# #     with open(file_path, "r", encoding="utf-8") as file:
# #         data = json.load(file)                  # 当前 JSON 文件 → Python 数据
# #
# #     print(file_path.name)                       # 当前文件名
# #     print(data)                                 # 当前文件里的内容
#
# # total_price = 0
# # for file_path in json_files:
# #     if not file_path.is_file():
# #         continue
# #     with open(file_path,"r",encoding="utf-8") as file:
# #         record = json.load(file)
# #         total_price += record["price"]
# #         print(total_price)
#
# # summary = {
# #     "total_price" : 3800,
# #     "file_count" : 3
# # }
# #
# # base = Path("data1")
# # mid_path = base / "reports"
# # file_path =mid_path / "summary.json"
# # print(file_path)
# # mid_path.mkdir(parents=True, exist_ok=True)      # 创建文件夹，不存在则创建
# #
# # def input_data(py_json):
# #     with open(file_path,"w",encoding="utf-8") as f:
# #         json.dump(py_json,f,ensure_ascii=False,indent=4)
# #
# # input_data(summary)
# # print(file_path.is_file())
# #
# # def read_json(f_path):
# #     with open(f_path,"r",encoding="utf-8") as f:
# #         data = json.load(f)
# #     return data
# #
# # summary_data=read_json(file_path)
# # print(summary_data["total_price"],summary_data["file_count"])
#
#
# # ## 综合测试
# # orders = [
# #     {"customer": "Amy", "amount": 1200},
# #     {"customer": "Bob", "amount": 800},
# #     {"customer": "Leo", "amount": 2600}
# # ]
# #
# # # 1. 创建 data2/orders 文件夹
# # base = Path("data2")
# # file_path = base/"orders"
# # file_path.mkdir(parents=True, exist_ok=True)
# #
# # # 2. 把 orders 保存成 orders.json
# # with open(file_path/"orders.json","w",encoding="utf-8") as f:
# #     json.dump(orders,f,ensure_ascii=False,indent=2)
# #
# # # 3. 再把 orders.json 读取回来
# # with open(file_path/"orders.json","r",encoding="utf-8") as f:
# #     orders_data = json.load(f)
# # print(orders_data)
# #
# # # 4. 计算所有 amount 的总和
# # total = 0
# # for order in orders_data:
# #     total += order["amount"]
# # print(total)
# # # 5. 计算订单数量
# # count = len(orders_data)
# # print(count)
# #
# # # 6. 创建 summary 字典：
# # #    {
# # #        "total_amount": ...,
# # #        "order_count": ...
# # #    }
# # summary = {"total_amount": total, "order_count": count}
# # # 7. 保存为 data2/reports/summary.json
# # summary_path = base/"reports"
# # print(summary_path.resolve())
# # summary_path.mkdir(parents=True, exist_ok=True)
# # with open(summary_path/"summary.json","w",encoding="utf-8") as f:
# #     json.dump(summary,f,ensure_ascii=False,indent=2)
# #
# # # 8. 再读取 summary.json
# # with open(summary_path/"summary.json","r",encoding="utf-8") as f:
# #     summary_data = json.load(f)
# # # 9. 最后打印：
# # #    总金额：4600
# # #    订单数量：3
# # print(f"总金额：{summary_data['total_amount']}\n订单数量：{summary_data['order_count']}")
#
#
# #复习
# # 复习1:JSON 方向
# data = {
#     "name": "Amy",
#     "age": 25
# }
#
# base = Path("data3")
# folder_path = base /"reports"
# folder_path.mkdir(exist_ok=True, parents=True)
#
# file_path = folder_path / "reports.json"
#
# # 复习 2：读取 JSON
# with open(file_path,"w",encoding="utf-8") as f:
#     json.dump(data,f,ensure_ascii=False,indent=2)
#
# print(file_path.resolve()) #=> /Users/wuyiyuan/Documents/GitHub/ai-engineer-45d/data3/reports/reports.json
# # file_path.name  #=> reports.json
# # file_path.stem  #=> reports
# # file_path.suffix #=> .json
# # file_path.parent #=> data/reports
#
# orders = [
#     {"amount": 1200},
#     {"amount": 800},
#     {"amount": 2600}
# ]
#
# total = 0
# for order in orders:
#     total += order["amount"]
#
# print(total)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
