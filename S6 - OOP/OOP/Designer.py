# تمرين
from Employee import Employee
from Roles import DesignerRole
from Payments import *


class Designer(Employee, DesignerRole, Salary):
    def __init__(self, first_name, last_name, app, salary, projects=None):
        Employee.__init__(self, first_name, last_name)
        DesignerRole.__init__(self, app, projects)
        Salary.__init__(self, salary)
        if projects is None:
            projects = []
        self.projects = projects

    def info(self):
        return f'name: {self.first_name} {self.last_name}, Job Title: {self.__class__.__name__}'

    def calculate_salary(self):
        return Salary.calculate_salary(self)
