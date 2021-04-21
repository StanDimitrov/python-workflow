# Special methods - Dunders
# difference between repr and str
# what is a complex number - it have two parts one is a real part and another is imaginable part

#complex_number = a + ib

class Complex:

    def __init__(self, real=1,imaginary=1):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + i {self.imaginary}'

    def __repr__(self):
        return f'Complex({self.real}, {self.imaginary})'

    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        z = Complex(r, i)
        return z

print(int.__add__(5,15))
print(str.__add__('Hello, ', 'World'))
z1 = Complex(5,6)
z2 = Complex(7,8)

z3 = z1 + z2 # Complex.__add__(z1,z2) z1 = self in def __add__ and z2 = other
print(z3)
#print(z1)
#print(str(z1)) # we can also write print(z1.__str__)
#print(repr(z1)) # or print(z1.__repr__) and the print will be exactly the same