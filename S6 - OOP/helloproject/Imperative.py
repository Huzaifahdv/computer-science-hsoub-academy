# U2 lesson2: Imperative programming
# sum = 1
# sum = sum + 2
# sum = sum + 3
# sum = sum + 4
# sum = sum + 5
# sum = sum + 6
# sum = sum + 7
# sum = sum + 8
# sum = sum + 9
# sum = sum + 10
# print(sum)
# # لا لا لا سواليف كثيرة انشرح بالدرس وفهمته


# lesson 4 : Declaring classes and objects
# class Employees: #تعريف صنف جديد
#     def __init__(self, first_name, last_name, title, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.title = title
#         self.salary = salary
#     def info(self):
#         return f'Name: {self.first_name} {self.last_name}, Job title: {self.title}, Salary: {self.salary}'
#     def change_salary(self, addition):
#         self.salary = self.salary + addition
#         return self.salary
# #Instantiation #إنشاء نسخة من صنف ما
# ahmed = Employees('ahmed', 'miau', 'miau', 3245)
# kalid = Employees('kalid','miau', 'miau', 3924423)
# print(ahmed.info())
# ahmed.change_salary(300)
# print(ahmed.info())


# # تمرين
# class product:
#     def __init__(self, name, color, description, price, weight):
#         self.name = name
#         self.color = color
#         self.description = description
#         self.price = price
#         self.weight = weight
#
#     def info(self):
#         return f'Name:{self.name}, color:{self.color},  description:{self.description},  price:{self.price}, weight:{self.weight}'
#
#     def change_price(self, addition):
#         self.price = self.price + addition
#         return print('تم تعديل سعر المنتج')
#
#     def change_description(self, addition):
#         self.description = addition
#         return print('تم تعديل وصف المنتج')
#
# orange = product('orange', 'red', 'fruit', 200, 1024)
# print(orange.info())
# orange.change_price(-50)
# orange.change_description(' Healthy fruit')
# print(orange.info())


# lesson 5 : class properties and methods
# import datetime
# class Employee:
#     total = 0 # class properties خصائص الصنف
#     salary_raise = 1.1
#     def __init__(self, first_name, last_name, title, salary): # object method تابع الكائن
#         self.first_name = first_name  # object properties خصائص الكائن
#         self.last_name = last_name
#         self.title = title
#         self.salary = salary
#         Employee.total +=1
#     def info(self):
#         return f'Name:{self.first_name}{self.last_name},Job:{self.title}, salary:{self.salary}'
#     @classmethod # class methods توابع الأصناف
#     def change_raise(cls, amount):
#         cls.salary_raise = amount
#     @classmethod
#     def from_string(cls, string):
#         first_name, last_name, title, salary = string.split('-')
#         salary = int(salary)
#         return cls(first_name, last_name, title, salary)
#     # lesson 6: static methods
#     @staticmethod   # تعريف تابع ساكن
#     def is_workday(day):  # تابع ساكن
#         if day.weekday() == 4 or day.weekday() == 5:
#             return False
#         return True

# ali = Employee('ali','hamad', 'programmer', 12000)
# kalid = Employee("kalid",'ali','accountent',3200)
# ahmed = Employee.from_string('miau- miau-miau-23423')
# print(Employee.salary_raise)
# print(kalid.salary)

# lesson 7: Object deletion
# print(ahmed)
# del ahmed
# print(ahmed)
# print(Employee.total)
# data = datetime.date(2025,5,27)
# print(Employee.is_workday(data)) #يمكن استدعاء الكائن الساكن من خلال الصنف أو من خلال الكائن
# print(ali.is_workday(data))
