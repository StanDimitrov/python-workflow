
# Different types of inheritance - number one is multi level inheritance, number two is multiple inheritance
# Multi level inheritance - a class can have at most one class as its parent
# Multiple inheritance - we can have more than one parent for a class, a class can be extended from multiple parents
class X:
    def fun_x(self):
        print('Fun of base class X')

class A(X):
    def fun_a(self):
        print('Fun of class A')
    def fun_x(self):
        print('Overrided method Fun X in class A')

class B(X):
    def fun_b(self):
        print('Fun of class B')
    def fun_x(self):
        print('Orverrided method Fun X in class B')

class C(A, B): # child class of A, B
    def fun_c(self):
        print('Fun of class C')

c = C()
c.fun_a()
c.fun_b()
c.fun_c()
c.fun_x() # this method will take the print of class A its because the inheritance start from left to right class C(A,B)
# Method resolution order - __mro__
print(C.__mro__)# this will print the order of the method resolution
