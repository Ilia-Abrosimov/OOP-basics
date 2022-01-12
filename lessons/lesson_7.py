class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Prop:
    """Родительский класс для классов Line и Rect"""
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width
        print("Инициализатор базового класса Prop")

    def getWidth(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):  # сначала вызывается конструктор дочернего класса
        print("Переопределенный инициализатор Line")
        super().__init__(*args)  # вызов конструктора родительской класса через метод super
        self.__width = 5  # приватная переменная класса Line к ней можно обратиться внутри класса line

    def drawLine(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, width класса Prop: {self.getWidth()}, локальная width: {self.__width}")  # для обращения к приватной переменной родительского класса необходимо использовать метод


class Rect(Prop):
    def __init__(self, *args):
        print("Переопределенный инициализатор Rect")
        super().__init__(*args)

    def drawReact(self):
        print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}")


line = Line(Point(1, 2), Point(10, 20))
line.drawLine()
rectangle = Rect(Point(3, 4), Point(30, 40))
rectangle.drawReact()
