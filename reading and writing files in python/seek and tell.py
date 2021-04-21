
with open('students.txt', 'r') as file_objects:
    position = file_objects.tell()
    print('Position = ', position)
    read_content = file_objects.read(5) # we will read the first 5 characters here
    position1 = file_objects.tell() # we can see in witch position in out text file using .tell() method
    print('Position = ', position1)
    # we can relocate the file marker within the file
    # 0 for begining the file, 1 to the current position, 2 end of file