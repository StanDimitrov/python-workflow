
student = {'name':'Rambo','gpa':9.1,'grade':'0'}

fmt_string = 'Name of the student : {}, GPA : {}, and Grade: {}'.format(student["name"],student["gpa"],student["grade"])
print(fmt_string)

format_string = 'Name of student : {0[name]}, GPA : {1[gpa]} and GRADE {2[grade]}'.format(student,student,student)
print(format_string)

another_formating_string = 'Name of student : {0[name]}, GPA : {0[gpa]} and grade {0[grade]}'.format(student)
print(another_formating_string)

another_formating_string1 = f'Name of student : {student["name"]}, GPA : {student["gpa"]} and GRADE : {student["grade"]}'
print(another_formating_string1)