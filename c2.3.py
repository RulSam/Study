class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # создадим свойство human_age, которое будет переводить возраст животного в человеческий
    @property  # тот самый магический декоратор
    def human_age(self):
        return self.age * 7.3


jane = Dog("jane", 4)
# т.к. метод помечен декоратором property, то нам не надо вызывать этот метод, чтобы получить результат
print(jane.human_age)

В этом куске кода мы пометили декоратором @property метод human_age. В итоге мы смогли получить результат работы метода, не вызывая его явно (без декоратора нам бы пришлось дописать в конец его вызов). Как правило, на этом объяснение этого потрясающего декоратора и заканчивается, а очень даже зря. Ведь помимо неявного вызова метода, мы можем похожим образом устанавливать значение в поле. Давайте же дополним наш код ещё одним свойством — шкалой счастья.

Для этого поля мы создадим геттер и сеттер. Из темы инкапсуляция (модуль C1) вы должны помнить, что:

геттеры — это специальные методы для получения значения поля класса;
сеттеры — это специальные методы для установки значений в поле класса.
class Dog:
    _happiness = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def human_age(self):
        return self.age * 7.3

    # добавим новое поле — шкала счастья
    @property
    def happiness(self):
        return self._happiness

    # с помощью декоратора setter мы можем неявно передать во второй
    # аргумент значение, находящееся справа от равно, а не закидывать это
    # значение в скобки, как мы это делали в модуле C1, когда не знали о
    # декораторах класса
    @happiness.setter
    # допустим, мы хотим, чтобы счастье питомца измерялось шкалой от 0 до 100
    def happiness(self, value):
        if value <= 100 and value >= 0:
            self._happiness = value
        else:
            raise ValueError("Happiness must be between 0 ... 100")


jane = Dog("jane", 4)
jane.happiness = 100  # осчастливим нашу собаку < :
print(jane.happiness)


Создать вычисляемое свойство для класса Square. Сделайте метод по вычислению площади свойством. Сделайте сторону квадрата свойством, которое можно установить только через сеттер. В сеттере добавьте проверку условия, что сторона должна быть неотрицательной.

Ответ
class Square:
    _a = None
    def __init__(self, a):
        self.a = a
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
    @property
    def area(self):
        return self.a**2