from abc import ABC, abstractmethod

class Human(ABC): # abstract class
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def smile(self):
        pass

    def walking(self):
        print(self.name, 'is walking')

class Student(Human):
    def __init__(self,roll_no,name):
        super().__init__(name)
        self.roll_no = roll_no

    def smile(self):
        print(self.name, 'is smiling hi hi hi')

    def study(self):
        print('Student: ',self.name, 'is preparing for exam')

class Teacher(Human):
    def __init__(self,dept_name,name):
        super().__init__(name)
        self.dept_name = dept_name

    def take_class(self):
        print('Teacher: ',self.name, 'is taking his class of :', self.dept_name)

    def smile(self):
        print(self.name, 'is smiling xoxoxox')

s1 = Student(1,'Stanimir')
t1 = Teacher('Maths','John Rambo')

s1.study()
t1.take_class()

s1.smile()
t1.smile()