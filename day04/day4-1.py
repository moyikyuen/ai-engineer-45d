# Day 4 - 1：Class 和 Object
from ctypes.wintypes import BOOL


# User  = class 类
# user1 = object 对象 / instance 实例
# user2 = object 对象 / instance 实例

# 创建一个 Product 类。
# 然后根据 Product 创建两个对象：
# class Product:
#     pass
#
# product1 = Product()
# product2 = Product()
#
# # product1 和 product2 都属于 Product
# # 但它们是两个不同的实例
# print(product1)
# print(product2)
# print(product1 == product2)
#
# class Product:
#     def __init__(self, name, price):       # 创建对象时，当前这个对象会自动传给 self
#         self.name = name                   # 这些是属性 attribute
#         self.price = price
#
#     def show_info(self):                   # 一个方法method
#         print(self.name, self.price)
#
#     def discount(self,pct):
#         return f"{self.price * pct:.2f}"
#
#     def rename(self,new_name):
#         self.name = new_name
#
# # product1 = Product("MacBook", 9999)
# # product2 = Product("iPhone", 6999)
# # product3 = Product("iPad", 4999)
# #
# # products = [product1, product2, product3]     # list 里面可以放 object
# # total = 0
# # for product in products:
# #     total += product.price
# # print(total)
#
# products_data = [
#     {"name": "MacBook", "price": 9999},
#     {"name": "iPhone", "price": 6999},
#     {"name": "iPad", "price": 4999}
# ]
#
# products = []
# for item in products_data:
#     product = Product(item["name"], item["price"])
#     products.append(product)
#     print(product.name,product.price)
#
# class Order:
#     def __init__(self,customer,amount,count):
#         self.customer = customer
#         self.amount = amount
#         self.status = "pending"
#         self.count = count
#
#     def is_large(self):
#         return self.amount >= 2000
#
#     def complete(self):
#         self.status = "completed"
#
#     def sell(self):
#         if self.count > 0:
#            self.count -= 1
#            return True
#         else: self.count = 0
#         return False
#
#
# order1 = Order("Amy", 1200,  3)
# order2 = Order("Bob", 800, 5)
# order3 = Order("Leo", 2600, 0)
#
# orders = [order1,order2,order3]

# for order in orders:
#     print(order.customer,order.amount)

# for order in orders:
#     print(order.customer,order.is_large())

# print(order1.status)
# order1.complete()
# print(order1.status)

# for order in orders:
#  print(order.customer,order.amount,order.count)
# # print(order1.sell())
# order1.sell()
# order1.sell()
# print("---------")
# for order in orders:
#  print(order.customer,order.amount,order.count)
#
# print(order1.sell())
# print(order3.sell())
#
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self,amount):
#         self.balance += amount
#
#     def withdraw(self,amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         else: return False
#
#
# account_list =[{"owner": "Amy",
#                 "balance":1000},
#                {"owner": "Bob",
#                 "balance":500}]
#
#
#
# def open_account (accounts):
#     bank_account_list = []
#     for account in accounts:
#         bank_account_list.append(BankAccount(account["owner"],
#                                  account["balance"]))
#     return bank_account_list
#
#
# if __name__ == "__main__":
#     all_accounts = open_account(account_list)
#     all_accounts[0].deposit(500)
#     amy = all_accounts[0].withdraw(1200)
#     bob = all_accounts[1].withdraw(800)
#     print(all_accounts[0].owner, all_accounts[0].balance)
#     print(all_accounts[1].owner, all_accounts[1].balance)
#     print(amy)
#     print(bob)

class Task:
    def __init__(self,title,priority,status = "todo"):
        self.title = title
        self.priority = priority
        self.status = status

    def complete(self):
        self.status = "done"

    def is_important(self):
        return self.priority >= 2

tasks = [{"title":"学习 Python",
          "priority":3},
         {"title": "整理简历",
          "priority":2},
         {"title": "买牛奶",
          "priority":1}
         ]

def set_up (task_list):
    all_tasks = []
    for t in task_list:
      all_tasks.append(Task(t["title"],t["priority"]))
    return all_tasks


if __name__ == "__main__":
   all_task = set_up(tasks)
   all_task[0].complete()
   all_task[1].complete()
   for task in all_task:
       print(task.title,task.status,task.is_important())

