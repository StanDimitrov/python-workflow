#
# class Human:
#     def __init__(self,name):
#         self.name = name
#
#     def smile(self):
#         print(self.name, 'is smiling - Ha ha ha')
#
#     def walking(self):
#         print(self.name, 'is walking')
#
# class Student(Human): # Human becomes the super type of Student type # when we construct object of student all the features of Human are going to be there for the Student
#     def __init__(self, roll_no, name):
#         super().__init__(name) # we can also write Human.__init__(self, name)
#         self.roll_no = roll_no
#
#     def study(self):
#         print('Student :', self.name,'Roll: ', self.roll_no, 'is preparing for the exam')
#
# class Teacher(Human):
#     def __init__(self, department_no, name):
#         super().__init__(name)
#         self.department_no = department_no
#
#     def take_class(self):
#         print('Teacher', self.name, 'taking class for ', self.department_no)
#
# s1 = Student(1,'Stanimir')
# t1 = Teacher('Programming','Malik')
#
# s1.smile()
# t1.smile()
#
# s1.study()
# t1.take_class()


class Employee:
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary

    def personal_tasks(self, production_no):
        self.production_no = production_no
        print(self.name, 'was produced :', self.production_no, 'elements this month')

class Training_employee(Employee):
    def __init__(self, half_shifts, name, address, salary):
        super().__init__(name,address,salary)
        self.half_shifts = half_shifts
        print('Employee on training', self.name, 'with adress',self.address, 'had', self.half_shifts, 'falf_shifts and he earned', self.salary,'during his training period')

    def check_in(self):
        print('Employee', self.name, 'have to made his checkpoint at 9h00.')

e1 = Training_employee(4,'Stanimir','54 bul Belomorski','500,BGLV')

e1.check_in()
e1.personal_tasks(20)
