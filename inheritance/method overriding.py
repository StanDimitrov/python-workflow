
class Human:
    def __init__(self,name):
        self.name = name

    def smile(self):
        print(self.name, 'is smiling - Ha ha ha')

    def walking(self):
        print(self.name, ' is walking')

class Student(Human):
    def __init__(self,roll_no,name):
        super().__init__(name)
        self.roll_no =roll_no

    def smile(self): # we override the method smile from our parent class Human
        print(self.name, 'is smiling - hi hi hi') # we define in the same way this function and we change the print

    def study(self):
        print('Student: ', self.name, 'Roll: ', self.roll_no, 'is preparing for exam')

class Teacher(Human):
    def __init__(self,dept_name, name):
        super().__init__(name)
        self.dept_name = dept_name

    def take_class(self):
        print('Teacher: ',self.name, 'taking class for departament:',self.dept_name)

s1 = Student(1,'Stanimir')
t1 = Teacher('Programming','John')

s1.smile()
t1.smile()

s1.study()
t1.take_class()