
class test_python_class:
    def __init__(self):
        print("Constructor invoked")

test1 = test_python_class()
test2 = test_python_class()

class person:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0

p1 = person()
print(p1.name)
print(p1.age)

p1 = person()
p1.name = "Bill"
p1.age = 25
print(p1.name, p1.age)

class person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person1("Bill", 25)
p2 = person1("Stan", 29)
print(p1.name,p1.age)
print(p2.name,p2.age)

class person2:
    def __init__(self, name="Python", age=1991):
        self.name = name
        self.age = age

p1 = person2()
print(p1.name)
print(p1.age)


class person3:
    greet = "Hello"

p1 = person3()
print(p1.greet)
p1.greet = "How are you doing?"
print(p1.greet)
print(person3.greet)
p2 = person3()
print(p2.greet)


class peprson4:
    totalObjects = 0
    def __init__(self):
        peprson4.totalObjects = peprson4.totalObjects + 1

p1 = peprson4()
print(p1.totalObjects)
p2 = peprson4()
print(p2.totalObjects)


class new_person:
    def __init__(self):
        self.name = "unknown"
        self.age = 0
    def displayInfoo(self):
        print(self.name, self.age)
p1 = new_person()
p1.displayInfoo()

class employee:
    def __init__(self, name, sal):
        self._name = name
        self._salary = sal

e1 = employee("Stanimir", 10000)
print(e1._name)
e1._salary = 20000
print(e1._salary)
e1._name = "Python"
print(e1._name)

class employee1:
    def __init__(self, name, sal):
        self.__name = name
        self.__salary = sal

e1 = employee1("Accedia", 10000)
print(e1._employee1__name)
e1._employee1__salary = 2000
print(e1._employee1__salary)