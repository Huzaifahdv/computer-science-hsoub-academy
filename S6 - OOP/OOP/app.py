from Employee import Employee
from Manager import Manager
from Programmer import Programmer, FreelancerProgrammer
from Roles import *
from Payments import *
from Designer import *
from Profile import Profile

# __name__ المتغير
# هو أحد المتغيرات الخاصة التي ينشئها مفسر لغة بايثون عند تشغيله يحمل هذا المتغير اسم الوحدة الحالية التي يجري تنفيذها
# عندما تنفذ شيفرة بايثون مباشرا أي من سطر الأوامر __main__ ولكن تصبح قيمته
if __name__ == '__main__':
    # Ahmed = Programmer('Ahmed', 'Jameel', 3000, 'PHP', ['Website', 'Blog'])
    # Sara = FreelancerProgrammer('Sara', 'Mazin', 200, 18, 'PHP', ['Website', 'Customer Service'])
    # print(Ahmed.info())
    # print(Sara.info())

    jawad = Programmer('Jawad', 'Kareem', 'Python', 'HR System', 4000)
    maha = FreelancerProgrammer('Maha', 'Ali', 50, 30, 'PHP', ['Website'])
    ahmed = Manager('Ahmed', 'Saeed', 5000, [jawad, maha])
    kalid = Designer('kalid', 'ahmed', 'Photoshop', 3000, ['l1', 'l2'])
    print(kalid.calculate_salary())
    khalid = Profile('BD', '01600', 'miau@gmail.com', False)
    print(khalid)

    # jawadProfile = Profile('Iraq, Baghdad', '39488', 'jawad@gmail.com', True)
    # print(jawadProfile)

    # for employee in (jawad, maha, ahmed):
    #     print(f'{employee.first_name} {employee.last_name} is paied: ')
    #     print(employee.calculate_salary())
    #     print('-'*20)
