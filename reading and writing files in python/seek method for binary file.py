
with open('students1.txt', 'rb') as file_object:
    file_object.seek(10)
    position = file_object.tell()
    print('Position = ', position)
    file_object.seek(-5,1) # we will move the file marker with -5 position from our current position so we use -5, 1
    position = file_object.tell()
    print('Position = ', position)
    file_object.seek(0, 2) # we will take the entire file from the end till the beginning of file
    position = file_object.tell()
    print('Position = ', position) # we will get the size of the file - the bytes of the file up to file marker
    file_object.seek(-4, 2)
    content = file_object.read(4)
    print(content) # in the result we will recived b'... this b' indicate that this string is actually a binary string
    print(content.decode('ascii')) # using . decode('ascii') we can reformat our binary code to ascii code