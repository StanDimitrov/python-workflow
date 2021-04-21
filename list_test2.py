
my_list = [10,80,80,40,80,60,70,90,90]

# if 20 in my_list:
#     print("Hello Python")
# else:
#     print("the number was not found")
#
# count = my_list.count(10)
# print(count)

# my_list.reverse()
# print(my_list)

# x = my_list.pop(2) # we will delete the 2 element in the my_list -- request index that we want to delete
# print(my_list, "\n" "The pop method was deleted the value of :",x)
# rem = my_list.remove(30) # the remove method request a value of the number that we need to delete !!
# print(my_list)

# index = my_list.index(80,1,9) # this method ask us the value for witch we want to find it's index position in the list
# print(index) # we can also say the start and the stop positions (80- value, 1-start,9-stop) for the value we search

target = 80
c = my_list.count(target)
start = 0
i = 1
while i <= c:
    index = my_list.index(target, start)
    print(index)
    start = index + 1
    i = i + 1
