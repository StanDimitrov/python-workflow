#from real_valid_integer import real_valid_integer
def factiorial(n):
    if n < 0:
        ve = ValueError('Unable to calculate factorial of negavite number')
        raise ve
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

def main():
    valid = False
    while not valid:
        valid = True
        try:
            usr_inp = int(input("Enter any integer"))
            f = factiorial(usr_inp)
            print(f)
        except ValueError as v:
            print(v.args)
            valid = False

if __name__=='__main__':
    main()

