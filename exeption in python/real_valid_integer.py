
def real_valid_integer():
    value = 0
    is_valid = False

    while not is_valid: # not False is True
        is_valid = True
        try:
            value = int(input('Input an integer:'))
        except Exception as e:
            print("Invalid formated integer")
            is_valid = False
    return value

def main():
    age = real_valid_integer()
    print('You age is:', age)

    id = real_valid_integer()
    print('Your id is:', id)

if __name__=='__main__':
    main()