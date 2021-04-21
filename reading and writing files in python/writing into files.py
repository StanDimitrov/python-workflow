

names = ['Stan','John','Peter','Bob','James']

with open('students.txt', 'w') as file_object:
    file_object.writelines("\n".join(names)) #this .join function will join each of the elements with aa new line there in between

# we can do the same thing using a loop like this :
    for name in names:
        file_object.write(name)
        file_object.write('\n')
