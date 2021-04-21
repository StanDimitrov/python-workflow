with open('names.txt.txt', 'r') as file_object:
    for line in file_object:
        print(line[:-1])
print('Is the  file closed? ', file_object.closed)