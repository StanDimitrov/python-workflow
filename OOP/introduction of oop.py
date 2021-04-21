#
# class human:
#     pass
#
# h1 = human()
# h2 = human()
#
# h1.name = 'Stanimir'
# h1.last_name = 'Dimitrov'
#
# h2.name = 'John'
# h2.last_name = 'Rambo'
#
# print(h1.name, h1.last_name)
# print(h2.name, h2.last_name)

# The __init__ method------------------------------

class Student:
    def __init__(self, roll, fname, lname):
        self.roll = roll
        self.fname = fname
        self.lname = lname
        self.email = fname.lower() + "." + lname.lower() + "@gmail.com"

    def full_name(self):
        return self.fname + " " + self.lname

s1 = Student(1, 'Stanimir','Dimitrov')
s2 = Student(2, 'John', 'Rambo')
# We can also use Student.name(s1 or s2) when we want to use full_name method
print(s1.roll, s1.full_name(),s2.roll,s2.full_name())
print(s1. fname,s1.lname,s1.email, type(s1))
print(s2.fname,s2.lname,s2.email,  type(s2))