class Point:
    """Класс для описания координат точки на плоскости"""
    x = 1
    y = 1


class_description = Point.__doc__
print(class_description)  # вывод строки документации класса

class_name = Point.__name__
print(class_name)  # вывод имени класса

class_data = dir(Point)
print(class_data)  # вывод данных класса

pt = Point()  # экземпляр класса Point
print(pt.x, pt.y)
Point.x = 100  # изменяем переменную х класса Point
print(pt.x, pt.y)  # изменяется и переменная экземпляра
print(id(pt.x), id(Point.x), sep='\n')  # переменная x экземпляра pt является атрибутом класса Point - это один объект
pt.x = 5  # переопределяем переменную x экземпляра pt
print(pt.x, pt.y)
print(id(pt.x), id(Point.x), sep='\n')  # переменная x экземпляра pt не является атрибутом класса Point - это разные объекты
pt2 = Point()  # Создам новый экземпляр класса Point
local_dict = pt2.__dict__  # словарь локальных переменных экземпляра класса
print(local_dict)  # локальных переменных x и y нет, т.к. они являются атрибутами класса Point
pt2.x = 10  # объявляем локальную переменную x экземпляра pt2
pt2.y = 20  # объявляем локальную переменную y экземпляра pt2
print(local_dict)  # локальные переменные записаны
print(getattr(pt2, 'x'))  # getattr возвращает значение атрибута объекта
print(hasattr(pt2, 'x'))  # hasattr проверяет на наличие атрибута у объекта
setattr(pt2, "z", 30)  # задает значение атрибута (если атрибут не существует, то он создается)
print(local_dict)
delattr(pt2, "z")  # delattr удаляет атрибут
print(local_dict)
print(isinstance(pt2, Point))  # isinstance определяет принадлежность экземпляра к тому или иному классу
print(isinstance(pt2.x, int))