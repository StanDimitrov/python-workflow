
class person:
    def __init__(self, name="Guest"):
        self.__name = name

    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

p1 = person()
print(p1.getname())
p1.setname("Bill")
print(p1.getname())


class person1:
    def __init__(self):
        self.__name = ''
    def setname(self,name):
        print('setname() called')
        self.__name = name
    def getname(self):
        print('getname() called')
        return self.__name
    name = property(getname, setname)

p1 = person1()
p1.name = "Steve"
print(p1.name)

class person2:
    def __init__(self, name):
        self.__name = name
    def setname(self,name):
        print('setname() called')
        self.__name = name
    def getname(self):
        print('getname() called')
        return self.__name
    def delname(self):
        print('defname() called')
        del self.__name
    name = property(getname,setname,delname)

p1 = person2("")
p1.name = "Steve"
print(p1.name)


class Alien:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.greeting = "Hello i came from Mars.... \n My name is {} and i am {} years old!". format(name,age)

    def __repr__(self):
        return "age {}, name {}m greeting{}".format(self.name, self.age,self.greeting)

alien = Alien("CrazyPython", 100)
alien.age = alien.age + 1
print(alien)