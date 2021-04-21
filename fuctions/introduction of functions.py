# # # # # function help us to medernize our programs
# # # #
# # # # def say_hello(name, age):
# # # #     if age <= 20:
# # # #         print("Hello", name, age, "from my first function")
# # # #     else:
# # # #         print("hi", name, age, "from my first function")
# # # # say_hello("World",2020) # colling of the function
# # # # say_hello("Programing",11)
# # #
# # # def sum_digits(num):
# # #     sum = 0
# # #     num = abs(num)
# # #     while num > 0:
# # #         sum += num % 10
# # #         num //= 10
# # #     return sum
# # #
# # # s = sum_digits(123)
# # # print(s)
# #
# # def sub_of_and_b(name, age):
# #     return name + age
# #
# # def main():
# #     print('Welcome in Python function')
# #
# # if __name__ == '__main__':
# #     main()
# #
# # v = sub_of_and_b("Stanimir", str(29))
# # print(v)
# #
# # #parameter passing in functions
# #
# # def parameter(x):
# #     print('x =', x, 'from function before')
# #     x = x + 1
# #     print('x=', x, 'from function after update')
# #
# # x = 10
# # print('x=', x, 'Befor calling function parameter')
# # parameter(x)
# # print('x=', x, 'After calling function parameter')
#
# def dog_function(name):
#     for dog in range(len(name)):
#         return name[dog]
#
# dogs = ['Sani','Lucky','Simba']
# dog_function(dogs)
# print(dogs)

#default parameters
#def process(name, age, major = 'Physics'): # we put it the default parameter for major argument
    #print('Name : ', name, 'Age : ', age, 'Major : ', major)

#process('Stanimir', 2020, 'Mathematics')
# if we want to overwrite our function we can put any value to major 'Mathematics' and it will be printed
# if we have any default parameter so it have to be after the non-default parameters name, age, then major = 'Physics'

# we cannot write our function like this def process(major='Physics, name, age) its not possible

#---------------------------------------------------------------------------------------------------------------

# Keyword based parameters

def process1(name, age, major='Physics'): # name, age, major are the FORMAL AGRUMENTS
    print('Name:', name, 'Age:', age, 'Major:', major)

process1('Stan', 1991, 'Zoology') # 'Stan', 1991, 'Zoology are the ACTUAL ARGUMENTS


process1(major='Programming', age=2020, name='Python')
# since we mention the name of each argument befor passing the parameters we don't need to remember the order of parameters.

# !!!!!!!!!!!!!!!!! #
# We can not doing mentioning of non keyword based arguments after keyword based arguments like :

def process2(name,school,age,mention= 'Zoology'):
    print('Name:', name, 'School:', school, 'Age:', age, 'Mention:', mention)

#process2(school='Hristo Botev',age=2020, mention='Physics', 'Stan')

# we should put the non keyword arguments in the begining of our function like this :
process2('Stan',school='Hristo Botev', age=29,mention='Programing')

#Syntax
#lambda arguments : expression
l = (lambda x: (x % 2 and 'odd' or 'even'))(300)
print(l)

lf = (lambda x:x*x)(3)
print(lf)