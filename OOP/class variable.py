
class Student:
    pass_score = 40.0 # variable of class, we can access this using the class name Student.pass_score

    def __init__(self,roll,first_name, last_name,score):
        self.roll = roll
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.email = first_name.lower() + " " + last_name.lower() + '@gmail.com'


    def name(self):
        return self.first_name + " " + self.last_name

    def pass_or_fail(self):
        if self.score >= Student.pass_score:
            return "Passed"
        else:
            return "Failed"

s1 = Student(1,'Stanimir', 'Dimitrov',75.0)
s2 = Student(2,"John", "Rambo",85.0)

# print('Pass score is : ', Student.pass_score)
# print('Content of s1 - ',s1.__dict__)
# print('Content of s2 - ',s2.__dict__)
# print('Using s1: ',s1.pass_score)
print(s1.roll, s1.name(),s1.email, s1.score,type(s1))
print(s2.roll,s2.name(),s2.email,s2.score,type(s2))

print(s1.pass_or_fail())
print(s2.pass_or_fail())