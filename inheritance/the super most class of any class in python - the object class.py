# Whenever we write a class in Python that is by default extended from the inbuilt Object class
# any object class contains the general implementaation of dunder __str__ method and dunder __repr__
class Rectangle: # Rectangle(object)
    def __init__(self, width,height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Rectangle object width: {self.width}, height: {self.height}, area: {self.get_area()}, '  \
        f'Peremeter: {self.get_perimeter()}'
r = Rectangle(4,10)
print(r.__str__())
print(issubclass(Rectangle, object)) # we can chek wheter a class is subclass of another class or not with issubclass functuon

