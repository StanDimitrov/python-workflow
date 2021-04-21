
class Student:
    pass_score = 40.0
    #from_string_counter = 0

    def __init__(self, roll, first_name, last_name, score):
        self.roll = roll
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.email = first_name.lower() + "." + last_name.lower() + "@gmail.com"

    def name(self):
        return self.first_name + " " + self.last_name

    def pass_of_fail(self):
        if self.score >= Student.pass_score:
            return "Passed"
        else:
            return "Failed"

    @classmethod
    def update_score(cls, new_score):
        cls.pass_score = new_score

    @staticmethod # if we do not need the class reference in our method for accessing any class members then we can declare this method as staticmethod
    def from_string(str_student): # staticmethod does now receive the class references and also it does not receive object references either
        str_roll, str_first_name, str_last_name, str_score = str_student.split(",")
        s = Student(int(str_roll), str_first_name, str_last_name, float(str_score))
        #cls.from_string_counter += 1
        return s

str1 = "1,Stanimir,Dimitrov,98.2"
str2 = "2,John,Rambo, 77.5"
str3 = "3, Peter,Smith, 82.1"

s1 = Student.from_string(str1)
s2 = Student.from_string(str2)

print(s1.email)
print(s2.email)
#print(Student.from_string_counter)