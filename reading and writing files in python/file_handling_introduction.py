#1 - Text files
#2 - Binary files

file_object = open('names.txt.txt', 'r') # 1 read - 'r' 2 write - 'w' 3 append - 'a'
# lines = file_object.read() # we can print a single line using readline
# print(lines, type(lines))
# file_object.close()

# another way to print all the elements in our file is with a loop
for line in file_object:
    print(line[:-1]) # we have an additional new line in the end of each element in our file
file_object.close() # so if we want to print out list content without 1 new line we need to use [:-1] i nout print statement

