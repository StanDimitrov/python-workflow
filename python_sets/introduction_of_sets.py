# sets is unordered collection of immutable elements

python_set = {1,2,3,4,5,6,7,8,9}
print(len(python_set))
print(type(python_set))

python_set.add(88)
print(python_set)

python_set.remove(2) # if the number is not exist in the set the remove method will rise an error
print(python_set)

python_set.discard(200) # if the number is not exist in the set so discard method will not produced an error
print(python_set)

python_set.clear()
print(python_set) # the clear method will delete the entire set