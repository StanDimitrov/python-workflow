# #
# # # list comprehension
# #
# # lst = []
# #
# # for i in range(10):
# #     lst.append(1)
# # print(lst)
# #
# # # we can do this exactly the same using list comprehension
# #
# # lst_comp = [i for i in range(10) if i % 2 == 0]
# # print(lst_comp)
# #
# # # There are three parts in list comprehension
# # # first - expression that you need to evaluate
# # # second - then the iteration with a for statement
# # # three - the condition that do you want to impose on the expression
#
# # a_list = [101,55,40,24,78,200,75,19,16,43]
# # b_list = [i * 3 for i in a_list if i % 2 != 0]
# # print(b_list)
#
# students = {"Jonh":9.99,"Peter":8.87,"Stan":9.00}
# grade_student = [name for name, graduation_score in students.items() if graduation_score >= 9.0 and name.startswith("S")]
# print(grade_student)
#
# # how we can make a set and setting a value to the selected element
# grade_student = {name:"Hello from Python" for name, graduation_score in students.items() if graduation_score >= 9.0}
# print(grade_student)

# More list comprehension examples
a_list = [1,2,3,4,5]
b_list = [10,20,30,40,50]

c_list = [i * j for i in a_list for j in b_list]
print(c_list)
#if we want to add more additional conditions for example print only the values up to 100
c_list = [i*j for i in a_list for j in b_list if i*j <= 100]
print(c_list)

# this list comprehension is exactly the same as:
for i in a_list:
    for j in b_list:
        print(i*j, end=' ')


cartesian_product = [(i,j) for i in a_list for j in b_list]
print(cartesian_product) # we can make () tuples or {} since we create our expression