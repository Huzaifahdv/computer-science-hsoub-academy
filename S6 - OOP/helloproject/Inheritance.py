# lesson 9: Inheritance.
import datetime


class Employee:
    total = 0
    __salary_raise = 1.1

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.__salary = salary
        Employee.total += 1

    def info(self):
        return f'name: {self.first_name} {self.last_name}'

    def get_salary(self):
        return self.__salary * self.__salary_raise

    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError
        self.__salary = salary

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


class Manager(Employee):    # في بايثون يكفي تمرير اسم الصنف الأساس في سطر تعريف الصنف المشتق للتعبير عن علاقة الوراثة بين الصنفين هكذا
    def __init__(self, first_name, last_name, salary, employees):
        super().__init__(first_name, last_name, salary)     # هذه الدالة تحضر تابع او معاملاته او شي زي كذا من الصنف الأب
        self.employees = employees

    def get_employees(self):        # دالة لعرض قائمة الموظفين التابع لكائن المدير
        print("Employees:")
        print("="*10)
        employees_list = []
        for number, employee in enumerate(self.employees):
            employees_list.append(f"{number + 1}. {employee.info()}")
        return '\n'.join(employees_list)
    """
    __init__()
    يمكننا الاستغناء عن وضع هذا التابع إذا اردنا استخدام نفس معاملات هذا التابع من الصنف الأساسي
    إذا اردنا إضافة معاملات إضافية للصنف المشتق نضيف نفس التابع مع معاملات الصنف الأساسي ثم إضافة المعاملات الإضافية
    لأنه لو أضفنا المعاملات الإضافية فقط سيلغى المعاملات الموروثة من الصنف الأساسي ويبقى فقط المعاملات الإضافية وسيظهر خطأ
    :ويمكننا إضافة جميع معاملات الصنف الأساسي باختصار وذلك بوضع هذه الدالة
    super()
    """
# ahmed = Employee('Ahmed', 'Kamal', 3000)
# ali = Employee('Ali', 'Zaher', 3000)
# najwa = Employee('Najwa', 'Adeeb',3000)
# anwar = Manager('Anwar', 'Khaled', 5000, [ahmed, ali, najwa])
# print(anwar.get_employees())


class Accountant(Employee):
    pass


# تمرين
class Programmer(Employee):
    def __init__(self, first_name, last_name, salary, lang, projects):
        super().__init__(first_name, last_name, salary)
        self.lang = lang
        self.projects = projects

    def get_projects(self):
        print('_' * 50)
        print('Projects in which he participated or is currently working: ')
        projects_list = []
        for number, projects in enumerate(self.projects):
            projects_list.append(f"{number + 1}. {projects.info()}")
        return '\n'.join(projects_list)


class Project:
    def __init__(self, name, description, days, done):
        self.name = name
        self.description = description
        self.days = days
        self.done = done

    def info(self):
        return f"Project: {self.name} \n Description: {self.description} \n Project duration: {self.days} \n Project state: {self.done}"


project1 = Project('Website', 'Airline', 14, False)
project2 = Project('website', 'Hotel', 5, True)
project3 = Project('Application', 'Game', 130, False)
zoro = Programmer('Roronoa', 'Zoro', 4000, 'js', [project1, project2])
nami = Programmer('Cat Burglar', 'Nami', 10000, ['js', 'py'], [project1, project3])
akai = Programmer('Akai', 'Shuichi', 8000, ['py', 'js'], [project3])
print(nami.info())
print(nami.get_projects())
