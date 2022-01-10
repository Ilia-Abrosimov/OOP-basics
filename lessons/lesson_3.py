class Point:
    WIDTH = 5
    __slots__ = ["__x", "__y"]  # контроль за локальными свойствами экземпляров классов

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setCoords(self, x, y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print("Coordinates should be is digit")

    def getCoords(self):
        return self.__x, self.__y

    def __checkValue(x):
        """Проверка корректности переменных"""
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    # def __getattribute__(self, item):
    #     """Автоматически вызывается при получении свойства класса с именем item"""
    #
    #     if item == "_Point__x":
    #         return "Private attribute"
    #     else:
    #         return object.__getattribute__(self, item)
    #
    # def __setattr__(self, key, value):
    #     """Автоматически вызывается при изменении свойства key класса"""
    #
    #     if key == "WIDTH":
    #         raise AttributeError
    #     else:
    #         self.__dict__[key] = value
    #
    # def __getattr__(self, item):
    #     """Автоматически вызывается при получении несуществующего свойства item класса"""
    #
    #     print("__getattr__: " + item)

    def __delattr__(self, item):
        """Автоматически вызывается при удалении свойства item (не важно: существует оно или нет)"""

        print("__delattr__: " + item)


pt = Point()
pt.setCoords(10, 20)
print(pt.getCoords())
pt._Point__x = 100  # Доступ к приватной переменной
print(pt.getCoords())
print(Point._Point__checkValue("4"))  # Доступ к приватному методу
