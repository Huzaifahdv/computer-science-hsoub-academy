# شرح للوحدات من ChatGPT
# import time
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"الوقت المستغرق لتنفيذ {func.__name__} هو {end_time - start_time} ثواني")
#         return result
#     return wrapper
# @timer_decorator
# def my_function(n):
#     sum = 0
#     for i in range(n):
#         sum += i
#     return sum
# my_function(1000000)
# print(time.asctime())

# Encapsulation with ChatGPT
class Car:
    def __init__(self, color, make):
        # السمات (المتغيرات) الخاصة بالسيارة
        self._color = color
        self._make = make

    # دالة الحصول (Getter) للسمة اللون
    def get_color(self):
        return self._color

    # دالة التعيين (Setter) للسمة اللون
    def set_color(self, new_color):
        self._color = new_color

    # دالة للحصول على تفاصيل السيارة
    def get_details(self):
        return f"Car Color: {self._color}, Make: {self._make}"


# إنشاء كائن من السيارة
my_car = Car('أحمر', 'تويوتا')

# استخدام دالة الحصول للحصول على تفاصيل السيارة
print(my_car.get_details())

# محاولة تحديث لون السيارة باستخدام دالة التعيين
my_car.set_color('أزرق')
print(f"New Car Color: {my_car.get_color()}")
print(my_car)
