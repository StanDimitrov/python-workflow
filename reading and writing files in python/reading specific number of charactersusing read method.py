with open('students.txt', 'r') as file_object:
    content = file_object.read(8) # with this method .read(we can put the number of characters that we want to print)
    print(content)