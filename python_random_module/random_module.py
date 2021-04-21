import random
#
# v = random.random() # take 0.0 to 0.9999999
# print(v)
#
# v1 = random.uniform(5,3) # takes the float numbers fromm 3.0 to 4.999999
# print(v1)
#
# v2 = random.randint(1,5) # takes int numbers from 1 to 5 inclus
# print(v2)
#
# v3 = random.randrange(1,10,2)
# print(v3) # takes start, stop and step parameters
# i = 1

# USA_states = ('Alabama',  'Hawaii', 'Massachusetts', 'New Mexico', 'South Dakota')
# print(USA_states)
# for state in USA_states:
#     print(i, "This is : ",state)
#     i += 1
# for i in range(10):
#     contact = f'{random.randint(100,999)}-555-{random.randint(1000,9999)}'
#     print(contact)

first_name = ['Stanimir','John','Rambo','Python','Bob']
last_name = ['Dimitrov','Smith','Cobra','Monty','Parker']
f_name = random.choice(first_name)
print(f_name)
