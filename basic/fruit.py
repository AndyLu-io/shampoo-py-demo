class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"
        self.__city = "shanghai"

    def __outPutColor(self):
        print(self.__color)

    def __outPutCity(self):
        print(self.__city)

    def outPut(self):
        self.__outPutColor()
        self.__outPutCity()


    @staticmethod
    def printPrice():
        print(Fruit.price)

    @staticmethod
    def setPrice(p):
        Fruit.price = p

apple=Fruit()
apple.outPut()
Fruit.printPrice()
Fruit.setPrice(10)
Fruit.printPrice()