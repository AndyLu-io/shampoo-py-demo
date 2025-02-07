class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__color = "red"

    def sayHello(self):
        print("Hello person")


class Student(Person):

    def __int__(self):
        self.__grade = 10

    def sayHello(self):
        print("Hello student")

    def printName(self):
        print(self.name)
        print(self.age)

    def printGrade(self):
        print(self.__grade)


s = Student("tom", 10, "male")
s.sayHello()
s.printName()
s.printGrade()
