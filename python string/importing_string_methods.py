# line = "Hello World! This is a Python string"
# # c = line.count("!")
# # print(c)
#
# #target = "is"
# #idnex = line.find(target) # this method finde will find thhe index of the first letter that we search "is"
# #print(idnex) # the position of "is" is 15 it will match first i and will send to us the its position
#
# # targeet = "Python"
# # index = line.find(targeet,10,20) # we can pass start0 and stop points using .find method
# # print(index) # if the searching element is not in range that we passed then the result will be -1
# target = "is"
# start = 0
# index = line.find(target,start)
# while index != -1:
#     print("Index of target :", index)
#     start = index + 1
#     index = line.find(target,start)
#
#
# line1 = 'Hello Python'
# print(line.startswith("Hello"))
# print(line.endswith(""))
#
# '''When we use .finde method and when we came out of range the output result will be -1.
# When we use the .index method and when we came out of range the output result will be error '''
#

names = "Stan,John,Sarah,Peter,Bob"
list = names.split(",")
print(list)

upper_method = names.upper()
print(upper_method)
print(upper_method.lower())

string_title = upper_method.title() # this will capitalyze only the title letters of each string
print(string_title)

print(string_title.capitalize()) # only the first title ot the entire string will be printed with a capital letter
string_title= string_title.upper()
print(string_title.isupper())