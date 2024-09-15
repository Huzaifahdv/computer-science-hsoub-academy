# lesson 10: Abstraction.
import datetime
from math import floor
from abc import ABC, abstractmethod  # لتعريف أصناف وتوابع مجرد abc من الوحدة abstractmethod و المزخرف ABC يتم جلب الصنف


# قبل الصنف abstract في لغات البرمجة الأخرى يتم تعريف الصنف المجرد بوضع
# لتعريف الصنف المجرد  ABC يوضع اسم الصنف
class Employee(ABC):
    total = 0
    __salary_raise = 1.1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total += 1

    @abstractmethod  # طريقة تعريف تابع مجرد
    def info(self):
        return f'name: {self.first_name} {self.last_name}'

    @abstractmethod
    def calculate_salary(self):
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, string):
        first_name, last_name, title, salary = string.split('-')
        return cls(first_name, last_name)

    @staticmethod
    def is_workday(day):
        if day.workday() == 4 or day.workday() == 5:
            return False
        return True


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):  # هذه القيمة تجعل الخاصية اختيارية
        super().__init__(first_name, last_name)
        self.__salary = salary
        if employees is None:
            employees = []
        self.employees = employees

    def get_employees(self):
        print("Employees:")
        print("="*10)
        employees_list = []
        for number, employee in enumerate(self.employees):
            employees_list.append(f"{number + 1}. {employee.info()}")
        return '\n'.join(employees_list)

    def info(self):
        return f'name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}'

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary)


class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}'

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary, lang = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary, lang)

    def assign_project(self, project):
        self.projects.append(project)


# تمرين أنشئ صنف يرث من الصنف المجرد وأضف إليه خصائص وتوابع جديدة ولا تنس إنشاء التوابع الموروثة
class Accountant(Employee):
    def __init__(self, first_name, last_name, salary, projects=None):
        super().__init__(first_name, last_name)
        self.__salary = salary
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'name: {self.first_name} {self.last_name}; Job Title: {self.__class__.__name__}, project: {self.projects}'

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        first_name, last_name, salary = string.split('-')
        salary = int(salary)
        return cls(first_name, last_name, salary)

    def assign_project(self, project):
        self.projects.append(project)


ahmed = Accountant.from_string('ahmed-muhammad-3200')
print(ahmed.info())
ahmed.assign_project('A1')
ahmed.assign_project('A2')
print(ahmed.info())
