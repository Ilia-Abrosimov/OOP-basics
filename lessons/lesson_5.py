class CoordValue:
    """Дескриптор с методами get и set"""
    def __set_name__(self, owner, name):
        self.__name = name  # c версии Python 3.6 метод вызывается автоматически при создании дескриптора в параметре name хранится имя экземпляра класса

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]  # instance ccылается на экземпляр класса для которого был вызван дескриптор

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class Point:
    coordX = CoordValue()  # Дескриптор класса Point для переменной описывающей координату х
    coordY = CoordValue()  # Дескриптор класса Point для переменной описывающей координату y

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt = Point(1, 2)
pt2 = Point(10, 20)
print(pt.coordX, pt.coordY)
print(pt2.coordX, pt2.coordY)
