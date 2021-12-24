class Point:
    """Класс для описания координат точки на плоскости"""

    def __init__(self, x=0, y=0):  # инициализатор класса
        self.x = x
        self.y = y

    def __del__(self):  # финализатор вызывается при уничтожении экземпляра класса сборщиком мусора
        print("Удаление экземпляра: " + self.__str__())


pt = Point()   # без передачи аргументов устанавливаются значения указанные в инициализаторе
pt2 = Point(5)
pt3 = Point(5, 10)
print(pt.__dict__, pt2.__dict__, pt3.__dict__, sep="\n")