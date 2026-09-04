# 继承
import json
from itertools import product
from typing import final
from unicodedata import category


# 子类自己没有某个 method
# Python 会继续去父类里找
# class Employee:
#     def work(self):
#         return "working"
#
# class Manager(Employee):
#     def hold_meeting(self):
#         return "meeting"
#
# # Manager 继承 Employee
# # 所以 Manager 的实例可以使用 Employee 的 method
# manager = Manager()
# print(manager.work())

# class User:
#     def __init__(self, name):
#         self.name = name
#
# class Admin(User):
#     def __init__(self, name, level):
#         super().__init__(name)      #直接执行了User里init的代码，得到name的赋值
#         self.level = level
#
# admin = Admin("Amy", 5)
# print(admin.name)                  #Amy
# print(admin.level)                 #5

# 组合，composition
# class Model:
#     def predict(self, text):
#         return f"分析结果：{text}"
#
# class InvoiceParser:
#     def __init__(self, model):
#         self.model = model
#
#     def parse(self, file):
#         return self.model.predict(file)          #把model.predict(file)保存成自己的属性
#
# model = Model()
# parser = InvoiceParser(model)
#
# print(parser.parse("invoice.pdf"))

# class Phone:
#     def call(self):
#         return "正在打电话"
#
# class Person:
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#     def make_call(self):
#         return self.phone.call()   # 把传进来的 Phone 对象保存下来
#
# phone = Phone()                   # phone 变量里装的是一个 Phone 对象
# amy = Person("Amy", phone)  # 把这个 Phone 对象传进去
#
# print(amy.make_call())

# class Product:
#     category = "Electronics"
#
#     def __init__(self, name):
#         self.name = name
#
#     def show_name(self):
#         return self.name
#
#     @classmethod
#     def show_category(cls):
#         return cls.category
#
# product1 = Product("MacBook")
#
# print(product1.show_name())       # self = product1, 输出MacBook
# print(Product.show_category())    # cls = Product，输出Electronics

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def from_string(cls, text):
#         name, age = text.split(",")
#         return cls(name, int(age))
#
# user1 = User("Amy", 25)
# user2 = User.from_string("Bob,30")

# class Employee:
#     company = "OpenAI"
#
#     @classmethod
#     def show_company(cls):
#        return cls.company
#
# print(Employee.show_company())

# class Product:
#     @staticmethod
#     def is_valid_price(price):
#         return price > 0
#
# print(Product.is_valid_price(100))
# print(Product.is_valid_price(-5))

# class User:
#     @staticmethod
#     def is_adult(age):
#         return age >= 18
#
# print(User.is_adult(20))
# print(User.is_adult(16))

# class User:
#     def __init__(self):
#         self.first_name = "Amy"
#         self.last_name = "Yao"
#         self.age = 25
#
#     @property
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#     def __str__(self):
#          return f"{self.full_name} - {self.age}"
#
#
# user = User()
# print(user.full_name)
# print(user)
#
# class Phone:
#     def __init__(self,brand):
#         self.brand = brand
#
#     def call(self):
#         return f"{self.brand} calling"
#
# class User:
#     def __init__(self,name,phone,age):
#         self.name = name
#         self.age = age
#         self.phone = phone
#
#     def role(self):
#         return "user"
#
#     @classmethod
#     def from_str(cls,text):
#         name,age = text.split(",")
#         return cls(name,phone,int(age))
#
# class Admin(User):
#     def __init__(self,name,phone,level):
#         super().__init__(name,phone,level)
#         self.level = level
#
#     def role(self):
#         parent_role = super().role()
#         return f"{parent_role} + admin"
#
# phone = Phone("iPhone")
# # user = User("Amy", phone,10)
# admin = Admin("Leo", phone,1)
# user = User.from_str("Amy,251111")
#
# # print(admin.role(),admin.level)
# # print(user.role())
# print(user.name)     # Amy
# print(user.age)      # 25
# # print(user.name)
# # print(user.phone.brand)
# # print(user.phone.call())
# #
#
# # print(admin.name)
# # print(admin.phone.brand)
# # print(admin.phone.call())
# #

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     @classmethod
#     def from_str(cls, str):
#         name,price = str.split(",")
#         return cls(name,int(price))
#
# product1 = Product.from_str("abcdef,11")
# print(product1.name,product1.price)
#
# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department
#
#     @classmethod
#     def from_str(cls,text):
#         name,salary,department = text.split(",")
#         return cls(name,int(salary),department)
#
# employee = Employee.from_str("Amy,20000,AI")
# print(employee.name)
# print(employee.salary)
# print(employee.department)

# class Product:
#     def __init__(self,name,price,category) :
#         self.name = name
#         self.price = price
#         self.category = category
#
#     def final_price(self):
#         return self.price
#
#     @classmethod
#     def from_str(cls,text):
#         name,price,category = text.split(",")
#         return cls(name, int(price), category)  #易错
#
#     @staticmethod
#     def is_expensive(price):
#         return price  >= 5000
#
#     @property
#     def display_name(self):
#         return f"{self.category} - {self.name}"
#
#     def __str__(self):
#         return f"{self.category} - {self.name}: {self.price}元"
#
# class SaleProduct(Product):
#     def __init__(self,name,price,category,discount):
#         super().__init__(name,price,category)
#         self.discount = discount
#
#     def final_price(self):
#         return  super().final_price()* self.discount
#
#
# product = Product.from_str("MacBook,9999,电脑")
# # print(product)
#
# sale_product = SaleProduct(
#     "iPhone",
#     6999,
#     "手机",
#     0.9
# )
#
# # print(sale_product.final_price())
#
# print(product.name)
# print(product.price)
# print(product.display_name)
# print(product)
# print(Product.is_expensive(product.price))
#
# print(sale_product.name)
# print(sale_product.final_price())
# print(SaleProduct.is_expensive(sale_product.price))

# class Member:
#     platform_name = "AI学习营"
#     def __init__(self,name,age,points):
#         self.name = name
#         self.age = age
#         self.points = points
#
#     def introduce(self):
#         return f"我是 {self.name}，{self.age}岁，当前积分 {self.points}"
#
#     def add_points(self,amount):
#         self.points += amount     #需要返回东西吗？-- 不一定
#
#     @classmethod
#     def change_platform(cls,new_name):
#         cls.platform_name = new_name
#
#     @staticmethod
#     def is_adult(age): #没用到cls，所以不需要classmethod
#         return age >= 18
#
#     @classmethod
#     def from_str(cls,text):
#         name,age,points = text.split(",") #需要返回东西吗？需要，因为反向建了新的object
#         return cls(name,int(age),int(points))
#
#     @property
#     def display_name (self):
#         return f"{self.platform_name} - {self.name}"
#
#     def __str__(self):
#         return f"{self.name}|{self.age}|{self.points}积分"
#
# class VipMember(Member):
#     def __init__(self,name,age,points,level,discount):
#         super().__init__(name,age,points)
#         self.level = level
#         self.discount = discount

#     def introduce(self):
#         return f"{super().introduce()} VIP等级：{self.level}"
#
#
# vip = VipMember("Leo", 30, 5000, 3, 0.9)
# print(vip.introduce())

class Player:
    def __init__(self,nickname,level,coins):
        self.nickname = nickname
        self.level = level
        self.coins = coins

    server_name = "亚洲一区"
    def introduce(self):
        return f"我是{self.nickname}，等级{self.level}，金币{self.coins}"

    @classmethod
    def change_server(cls,new_name):
        cls.server_name = new_name

    @staticmethod
    def is_high_level(level):
        return level > 30       #不确定

    @classmethod
    def from_str(cls,text):
        nickname,level,coins = text.split(",")
        return cls(nickname,int(level),int(coins))

    @property
    def display_name (self):
        return f"{self.server_name} - {self.nickname}"

    def __str__(self):
        return f"{self.nickname} | {self.level}| {self.coins}金币"



player = Player("luna",99,8000)

print(player.introduce())
player.change_server("欧区")
print(player.server_name)
print(player.is_high_level(10))

playerAmy = Player.from_str("Amy,20,5000")
print(playerAmy.introduce())
print(playerAmy.display_name)

print(playerAmy)
print(player)
