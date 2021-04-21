
def process(fixed, *args, **kwargs): # variable length arguments we can have fixed, *args for tuples and ** for dict
    print(fixed)
    print(args)
    print(kwargs)

process(10,20,30,40,50,'Stan', k1 ='Football', k2='Basketball', k3 = 2020)

# if we want to have fixed arguments after *args we have to mention the name of args like this:

def process1(*args, fixed, **kwargs): # we have to mention the name of our argument to the value that we want to passing
    print(fixed) # we cannot passing fixed arguments after **kwargs its not accepted in python
    print(args)
    print(kwargs)

process1(100,10, fixed="Hi from Python Function", f1='This is amazing')