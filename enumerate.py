names = ["John","Stan","Lucy","Peter","Mike"]

#index = 0
for index, name in enumerate(names, start=1): # with enumerate method we can access the values of our elements in the list
    print(index, name) # enumerate method will auto increment each element with + 1 in the list we can give a start position
