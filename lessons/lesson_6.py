class Point:
    """Описан класс singleton для которого можно создать только один экземпляр"""
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):  # выполняется перед созданием экземпляра класса
        if not isinstance(cls.__instance, cls):  # проверяет что экземпляров класса не существует
            cls.__instance = super(Point, cls).__new__(cls)
        else:
            print("Экземпляр класса Point уже создан!")
        return cls.__instance

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.coordX = x
        self.coordY = y

    @staticmethod  # декоратор указывается при объявлении метода статическим
    def getCount():  # для статического метода в параметре self нет необходимости
        return Point.__count


pt = Point()
pt1 = Point()
pt2 = Point()
print(id(pt), id(pt1), id(pt2), sep="\n")  # доступ к статическому методу осуществляется из класса
print(Point.getCount())
