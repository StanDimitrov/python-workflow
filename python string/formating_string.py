name1 = "Stanimir"
name2 = "Dimitrov"
age = 29
education_score = 97.5689
#str = name1 + " and " + name2 + " is my name"
#print(str)

# str = "{} {} is my name".format(name1,name2)
# print(str)

# str = "{0:>10} {1:>10} is my name and i am {2:^15} year old and your education score is {3:.2f}".format(name1,name2,age, education_score)
# print(str) # we can use :, :>, :< :^ or .2f for setting any number of white spaces for left,right and center the placeholder .2f to formating a value to second parameter

str = "{0:->10} {1:->10} is {2:.>10} years old and his final education score of python is {3:.^15.2f}".format(name1,name2,age,education_score)
print(str) # we can also set the :characters and position as :.>10 or :->10 or :.^15.2f

# str = ("%s %s is my name"%(name1,name2))
# print(str)

