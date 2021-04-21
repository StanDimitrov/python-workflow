my_str = "3 Python"

my_str = my_str.split()
print(my_str)

my_str[0] = int(my_str[0])
print(my_str)
n = my_str[0]
print(n)
pos = 1

if pos == 1:
    my_str = my_str[1][0:n]
    print(my_str)
else:
    my_str = my_str[1][n:]
    print(my_str)