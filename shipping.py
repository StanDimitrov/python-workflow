#
students = ["Stanimir","Leo","Artur","Fernando",["Peter","Solomon","Jonathan","Alex","Armstrong","Paco"]]
#
# for student in students:
#     print(student)
#
# s = students[-1][:5:2] # [-1] the last element in the list and then [start:stop:step]
# print(s)
# y = s[0]
# print(y)
# print(type(y), y)
#
# students[-1][0] = "Python"
# print(students)

# students.append("Tina") # using append method
# print(students)

students_list_1 = ["Tina", "John","Rambo"]
# students.extend(students_list_1) # using extend method
# print(students)
students_list_1.insert(0,"Bob") # using inter method we can say the position exact and the value of the element (position 0, "element")
print(students_list_1)
stud = students_list_1.copy()
print(stud)
students_list_1.clear()
print(students_list_1)