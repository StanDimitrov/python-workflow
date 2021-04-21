
#Syntax errors
#Logical mistakes
#Runtime exceptions

try:
    my_list = [1,2,3,4,5,6]
    my_list.remove(3)
    print(my_list)
    my_list.remove(100)
    print(my_list)
except ValueError as ve:
    print('Something wrong in your program')
    print(ve.args) # is going to print the details of the exception there ve = value error for example

print('In the main flow of the program...')