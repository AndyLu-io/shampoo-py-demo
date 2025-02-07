class Person:
    num=1
    def sayHello(self):
        print("Hello")

    def __init__(self):
        print("init")
        self.name="tom"
        self.age=10

    def printName(self):
        print(self.name)
        print(self.age)





p=Person()
p.sayHello()
print(Person.num)
p.printName()


class Student(Person):

    def __init__(self, color):
        super().__init__()
        self.__color=color

    def printName(self):
        print(self.name)
        print(self.age)
        print(self.__color)


s=Student("red")
s.sayHello()
s.printName()





