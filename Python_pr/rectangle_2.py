
from rectangle import Rectangle

#далее создаём два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
#вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

from rectangle import Rectangle, Square

# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

# Запустите
# программу
# и
# посмотрите
# ожидаемый
# результат
# в
# консоли: площадь
# прямоугольника
# и
# квадрата.Можно
# более
# лаконично
# выводить
# два
# квадрата: через
# запятую(см.
# 14
# строчку).
#
# Теперь
# мы
# хотим
# в
# нашей
# программе
# все
# объекты
# перенести
# в
# единую
# коллекцию.Назовём
# фигуры(figures).Коллекция
# содержит
# список, в
# который
# и
# помещаем
# наш
# первый
# прямоугольник, квадрат
# и
# т.д.(см.
# 17
# строчку).Работаем
# в
# файле
# rectangle_2.py:

from rectangle import Rectangle, Square, Circle

# далее создаём два прямоугольника

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
# вывод площади наших двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

figures = [rect_1, rect_2, square_1, square_2]

# Далееп ройдёмся поциклу for:

print(square_1.get_area_square(),
      square_2.get_area_square())



figures = [rect_1, rect_2, square_1, square_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    else:
        print(figure.get_area())

rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)
square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(1)
circle_2 = Circle(2)

figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_circle())