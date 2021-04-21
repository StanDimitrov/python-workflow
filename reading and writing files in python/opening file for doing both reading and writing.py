
with open('test_file.txt.txt', 'r+') as file_object: # we can use 'r+' = read and write, 'w+' = write and read or 'a+' = append and read from file
    position = file_object.tell()
    print('Position =', position)
    position = file_object.seek(0) # we put the start position of our text file
    print('Position = ', position)
    take_text_from_file = file_object.read(6) # we want to select the first 6 characters
    print('Your selected text is: ', take_text_from_file)