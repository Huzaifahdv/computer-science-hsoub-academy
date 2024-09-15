# lesson no 6: conditions:
# الطريقة العادية
# name = input('Enter your name: ')
# if len(name)>0:
#     print('Hello, '+ name + ', Welcome to our program.')
# else:print('sorry, you did not write your name.')
# age = int(input('Enter your age: '))
# if age < 14:
#     print('You are too young ')
# elif 14 < age < 18:
#     print("You need your parents' permission .")
# else:
#     print("You do not need permission. ")
# الطريقة المختصرة (التعبير الشرطي او العامل الثلاثي) conditional expression
# age = int(input('Enter your age: '))
# if age >18:
#     allowed=True
# else:
#     allowed=False
# اختصار هذه
# allowed = True if age > 18 else False


# lesson 7 lists:
# cars = ['BMW', 'Marcedes', 'Toyota', 'Kia', 'Renault']
# squares = [1,4,9,16,25]
# راجع الحلقة وموسوعة حسوب للمزيد من التفاصيل حول القوائم


# lesson 8 Tuples:
# grades = 98, 80, 85, 70, 90, 88
# print(grades)
# #انشاء صف فارغ
# lesson = ()
# print(lesson)
# #انشاء صف يحتوي على عنصر واحد
# lessons ='miau',
# print(lessons)
# #يمكن تنفيذ نفس العمليات التي يمكن فعلها في القوائم
# #ويمكن الوصول للعنصر في الصف بنفس الطريقة المتبعة في القوائم
# print(grades[2])
# print(grades[2:5])
# print(65 in grades)
# print(80 in grades)


# lesson 9: Dictionaries
# employees = {'Mohammed': 3000, 'Ahmed': 3200, 'Ali': 3100}
# # لإضافة عنصر في القاموس
# employees['Kareem']=3250
# print(employees)
# # لحذف عنصر من القاموس
# del employees['Ahmed']
# print(employees)
# # للحصول على مفاتيح القاموس
# print(list(employees))
# # للتحقق من وجود مفتاح في القاموس
# print('mohammed'in employees)
# print('Mohammed' in employees)
# # للحصول على القيمة المرتبطة بمفتاح معين
# print(employees.get('Ali'))


# lesson 10: loops
# rivers = ['Tigris', 'Nile', 'Barada', 'Euphrates']
# for river in rivers:
#     print(river)
# #يستخدم الدالة
# #range()
# #للمرور على تسلسل من الأرقام وللمزيد عنه راجع موسوعة حسوب
# #الدالة whlie تعمل بنفس التي في جافاسكربت
# x=5
# while (x>0):
#     print(x)
#     x-=1


# lesson 11: List Comprehension
# numbers = [2, 9, 11, 24, 30, 33, 56,79, 85, 103]
# newNumbers= [number for number in numbers]
# print(newNumbers)
#
# newNumbers =[]
# for number in numbers:
#     if number >30:
#         newNumbers.append(number)
# print(newNumbers)
# newNumbers = [number for number in numbers if number>30]
# print(newNumbers)
# #الصيغة العامة لليست كوبريهنشن هي
# # newlist = [expression for item in iterable if condition == True]
# divideby = [number for number in numbers if number % 2 == 0]
# print(divideby)
#
# Numbers = []
# for x in range(11):
#     Numbers.append(x)
# print(Numbers)
# Numbers = [x for x in range(11)]
# print(Numbers)
# #التابع
# #title()
# #يحول الحرف الأول في السلسلة النصية إلى حرف كبير
# fruits = ['apple', 'orange', 'grapes', 'banana', 'apricot']
# Fruits = []
# for fruit in fruits:
#     Fruits.append(fruit.title())
# print(Fruits)
# Fruits = [fruit.title() for fruit in fruits]
# print(Fruits)
# #تمرين انشاء قائمة عناصرها هي حاصل تربيع عناصر الأولى
# nmb = [2, 4, 5, 8, 9, 21, 23, 54, 75, 88, 89, 73]
# nmbs = []
# for n in nmb:
#     nmbs.append(n*n)
# print(nmbs)
# nmbs = [n*n for n in nmb ]
# print(nmbs)
# #يوجد نفس التمرين من خلال while
# # راجع تعليقات الدرس


# lesson 12: Functions
# pass  # لا تؤدي هذه الكلمة المفتاحية أي وظيفة ولكنها تخبر المفسر بتجاوز هذا السطر ويمكن استخدامه لتجنب ظهور خطأ عند تعريف دالة فارغة
# def odd_number(end, start = 0):
#     """Calculate Odd Numbers"""
#     for number in range(start, end):
#         if number % 2 == 0:
#             continue
#         print(number, sep=',')
# odd_number(10)
# def get_info(name,age,married):l
#     print("name:",name,"age:",age,"married:",married)
# get_info(True,'miau',32)
# def divide(x,y):
#     if y==0:
#         print('you can not divide by zero!')
#         return
#     return x/y
# print(divide(2,4))


# lesson 13: Function Annotations
# PI = 3.13
# def area(redios: float)->float:
#     return PI * redios**2
# print(area('5'))
# #يجب تنزيل جزمة خاصة راجع الجزء الأخير من الدرس وراجع التعليقات للفهم بشكل أكبر


# lesson 14: Decorators part1
# def increase(x):
#     return x + 1
# def decrease(x):
#     return x - 1
# def calculate(operation, x):
#     return operation(x)
# print(calculate(increase,5))
# print(calculate(decrease,5))
#
# def parent():
#     print("This is the parent function")
#     def child1():
#         print("This is child 1 function")
#     def child2():
#         print("This is child 2 function")
#     child2()
#     child1()
# parent()
#
# def vot(age):
#     def allow():
#         print("You are allowed to vote")
#     def not_allow():
#         print("You are not allowed to vote")
#     if age>18:
#         return allow
#     else:
#         return not_allow
# person1 = vot(19)
# person2 = vot(12)
# person1()
# person2()


# lesson 15: Decorators part2
# الدالة المُزَخرِفة
# def decorator(function):
#     def inner(*args, **kwargs):
#         print('='*20)
#         function(*args, **kwargs)
#         print('='*20)
#     return inner
# def write():
#     print('Hello World')
# #يوجد طريقتان لاستدعاء الدالة المزخرفة
# write = decorator(write)
# write()
# #or
# @decorator
# def write1():
#     print('miau miauu')
# write1()
# #سيتسبب الكود التالي إلى ظهور خطأ وذلك بسبب عدم تعريف المعامل عند استدعاء الدالة في الدالة المزخرفة
# @decorator
# def write2(name):
#     print(name)
# write2('miau')
# #تقدم بايثون الكلمات المفتاحية
# #*args والتي تمثل قائمة بجميع المعاملات الموقعية الممررة إلى الدالة
# #**kwargs والتي تمثل قاموسًا يضم جميع المعاملات المفتاحية الممررة إلى الدالة على هيئة زوج مفتاح يساوي قيمة
# #ولكن لو كانت القيمة معادة
# def decorator(function):
#     def inner(*args, **kwargs):
#         print('='*20)
#         return function(*args, **kwargs)
#     return inner
# @decorator
# def write(name):
#     return name #هنا؟؟!
# print(write('miau'))
# #شرح السبب الطريقة في الدرس من الدقيقة سبعة ونصف تقريبًا
# #مثال حقيقي لاستخدام المزخرفات للتحقق من أن المستخدم الذي يطلب معلومات الحساب قد سجل الدخول في حسابه بادخال المعلومات الصحيحة
# name = input("Enter you name: ")
# password = input("Enter you password: ")
# def logged_in(function):
#     def inner():
#         if name == "Ahmad" and password == '123456':
#             function()
#         else:
#             print('please log in !')
#             return
#     return inner
# @logged_in
# def get_account():
#     print('you are logged in. user name:', name, 'password: ', password)
# get_account()


# lesson 16: Modules
# import fibo
# fibo.fib(100)
