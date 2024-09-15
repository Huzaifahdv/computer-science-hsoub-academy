# lesson 8: Encapsulation
import datetime


class Employee:
    total = 0
    __salary_raise = 1.1

    def __init__(self, first_name, last_name, title, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.__salary = salary  # لإخبار بايثون أن هذه البيانات حساسة نضع شرطتين سفليتين قبل اسم الخاصية عند تعريفها ، وعند وضعها لن يمكن استدعاء هذه البيانات
        Employee.total += 1

    def info(self):
        return f'name: {self.first_name}{self.last_name} Job title: {self.title}'

    # تتيح جميع لغات البرمجة التي تدعم البرمجة الكائنية إضافة دوال الحصول ودوال التعيين للبيانات الحساسة بهذه الطريقة
    def set_salary(self, salary):
        if salary <=0:   # يمكن الإضافة هنا بعض الشروط الذي نريده مثلا: أن الذي يريد الاستدعاء قد سجل الدخول إلى النظام أو أنه يملك الصلاحيات المطلوبة لرؤية البيانات الحساسة
            raise ValueError
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    # تقدم بايثون طريقة أخرى لتنفيذ ذلك حيث يجب أن يكون دالة الحصول قبل دالة التعيين بهذه الطريقة

    @property   # يتم تعريف دالة الحصول هكذا
    def salary(self):
        return self.__salary

    @salary.setter  # يتم تعريف دالة التعيين هكذا
    def salary(self, salary):
        if salary <= 0:
            raise ValueError
        self.__salary = salary
    # وهذه الطريقة تجعل البيانات يمكن استدعائها كما يستدعى الخاصية
    # وطبعا ما الفائدة ولماذا لا أدري !! لأنه يمكن استدعاء البيانات أصلا مثل الخاصية حتى بدون دوال التعيين ودوال الحصول إلا أنه ينفذ الأكواد الموجودة في الدوال ، يجب أن أبحث أكثر..
    """
    ينطبق مفهوم التغليف على التوابع أيضًا، تكون التوابع 
    عامة بصورة افتراضية ويمكن تحويلها إلى توابع خاصة 
    بإضافة شرطتين سفليتين قبل اسم التابع عند تعريفه 
    مثل هذه التابع التي في الأعلى 
    salary_raise = 1.1
    وكذلك الدالة التي في الأسفل 
    change_raise()
    والآن لن يكون بالإمكان استدعاء هذا التابع خارج الصنف
    ولا تغيير مرتبات الزيادة على الموظفين من خارج الصنف أيضا
    """

    @classmethod
    def __change_raise(cls, amount):
        cls.salary_raise = amount

    @classmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, title, salary)

    @staticmethod
    def is_workday(day):
        if day.workday() == 4 or day.workday() == 5:
            return False
        return True


ahmed = Employee('Ahmed', 'Kareem', 33, 3000)
print(ahmed.get_salary())
ahmed.set_salary(4000)
print(ahmed.get_salary())
print(ahmed.salary)
