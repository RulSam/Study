# map
# Функция map пришла из функционального программирования. Она позволяет применять некую функцию к каждому элементу итерируемого объекта (строки, списки, кортежи, словари).
#
# Вот псевдокод, по которому работает map. Псевдокод — компактный, зачастую неформальный, способ описания алгоритмов, использующий ключевые слова языков программирования, но опускающий несущественные для понимания алгоритма подробности и специфический синтаксис.
#
# def map_(func, some_list):
#     # some_list объект, над которым будет производиться преобразование
#     # func функция, которая должна выполняться над каждым объектом
#     outp = []
#     for i in range(len(some_list)):
#         outp.append(func(some_list[i]))
#     return outp
# Чтобы не использовать такую конструкцию каждый раз, введена встроенная функция:
#
# map(function, iter1, iter2, ...)
# iter1, iter2, ... — может быть 1 и более итерируемых объектов, однако на вход функции должно приходить такое же количество аргументов.
# function — ссылка на функцию.
#
# Но особенность функции map в том, что она возвращает результат вычислений не сразу, а в виде итератора, который в дальнейшем производит «ленивые» вычисления. Чтобы получить список значений, нужно в явном виде привести к нужному типу либо воспользоваться циклом for:
#
# print(list(map(pow_, a_list)))  # [1, 4, 9]
#
# for i in map(pow_, a_list):
#    pass
# Задание 5.5.1
# Задание на самопроверку.
#
# С помощью метода строки str.lower перевести все элементы списка в нижний регистр.
#
# L = ['THIS', 'IS', 'LOWER', 'STRING']
# Ответ
# print(list(map(str.lower, L)))
# # ['this', 'is', 'lower', 'string']


# Задание 5.5.2
# Задание на самопроверку.
#
# Отфильтровать из заданного списка только чётные элементы.
# def even_numbers(x):
#     return x % 2 == 0
# result = filter(even_numbers, [-2, -1, 0, 1, -3, 2, -3])
# print(list(result))


#
# В каких случаях стоит использовать map и filter?
# Чаще всего генераторы списков более читаемы, чем map и filter, особенно в простых конструкциях.
#
# # map + filter
# some_list = [i - 10 for i in range(20)]
# def pow2(x): return x**2
# def positive(x): return x > 0
#
# print(some_list)
# print(list(map(pow2, filter(positive, some_list))))
# То же самое через list comprehension.
#
# [i**2 for i in some_list if i > 0]
# Возникает вопрос, когда использовать map, а когда list comprehension? Как оговаривалось ранее, map работает по принципу ленивых вычислений, а list comprehension возвращает результат вычислений сразу.
#
# map(func, list1)  # итератор, но никаких вычислений не будет произведено
# list(map(...))  # только здесь появляется объект
#
# [func(i) for i in list1]  # сразу готовый объект
#
#
# [func(i) for i in list1] == list(map(func, list1))  # результат один и тот же

#
# Lambda функции
# Функции map и filter принимают в виде первого аргумента другую функцию, которая должна применяться к каждому элементу. Иногда встроенных функций не хватает, и приходится объявлять функцию, которая зачастую будет применена всего один раз. Но при этом она будет загромождать исходный код.
#
# Специально для таких одноразовых функций были сделаны анонимные функции. Объявляются они по ключевому слову lambda.
#
# # эти две функции выполняют одно и то же, складывают два числа
# def my_function(x1, x2):  # Обычная функция
#    return x2 + x1
#
# lambda x1, x2: x2 + x1  # Анонимная функция
# Анонимные функции могут содержать в себе только одну инструкцию (выражение), которую они выполняют.
#
# # Возвести первые 10 натуральных чисел в квадрат
# list(map(lambda x: x ** 2, range(1, 11)))  # правильно
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# list(map(lambda x: x ** 2; x + 1, range(1, 11)))  #  неправильно, так как lambda содержит две конструкции


# Предположим, мы хотим отсортировать словарь по значениям. Вообще говоря, словарь (его ещё называют ассоциативным массивом) является неупорядоченной структурой данных. Иными словами, порядок хранения пар ключ-значение в памяти может быть произвольным. Однако создатели языка Python, начиная с версии 3.6, изменили реализацию словарей таким образом, что порядок ключей «запоминается». И потому упорядочивание словаря в Python становится осмысленным. По умолчанию словарь сортируется по ключам.
#
# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
#
# # Чтобы отсортировать его по ключам, нужно сделать так
# print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
# А вот, чтобы отсортировать словарь по значениям, необходимо указать, что сортировать нужно по второму элементу кортежа ключ-значение. Тут на помощь приходят lambda-функции. У встроенной функции sortred() можно задать аргумент key, который укажет, по какому ключу нужно производить сортировку.
#
# sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря
# Итог по lambda-функциям:
#
# используются один раз;
# не загромождают код программы;
# после выполнения сразу удаляются;


# a = ["asd", "bbd", "ddfa", "mcsa"]
# print(list( map(len,  a)))

# a = ["это", "маленький", "текст", "обидно"]
# print(list(map(str.capitalize, a)))
#
# X = 'X'
# O = '0'
# RAZMER_DOSKI = 9
# HODI = ' '
# NICHYA = 'Ничья'
#
#
# def instrukciya():
#     print('''
# Привет! Это игра "Крестики-нолики".
# Чтобы сделать ход, введи номер клетки,
# куда хочешь поставить свой символ:
#
# 0 | 1 | 2
# +++++++++
# 3 | 4 | 5
# +++++++++
# 6 | 7 | 8
#
#
# ''')
#
#
# def nachalo(vopros):
#     otvet = None
#     while otvet not in ('да', 'нет'):
#         otvet = input(vopros).lower()
#     return otvet
#
#
# def fishki():
#     perviy_hod = nachalo("Вы хотите быть первым, кто сделает ход \
# (играть крестиками)?  ")
#     if perviy_hod == 'да':
#         print('Окей, ты играешь крестиками!')
#         human = X
#         comp = O
#     else:
#         print('ОК, я делаю первый ход крестиками')
#         human = O
#         comp = X
#     return comp, human
#
#
# def hod_number(low, high):
#     otvet = None
#     while otvet not in range(low, high):
#         otvet = int(input("Делай свой ход - напиши номер поля (0-8): "))
#     return otvet
#
#
# def new_doska():
#     doska = []
#     for i in range(RAZMER_DOSKI):
#         doska.append(HODI)
#     return doska
#
#
# def pokaz_doski(doska):
#     print('\n', doska[0], '|', doska[1], '|', doska[2])
#     print('+++++++++')
#     print('\n'
#           , doska[3], '|', doska[4], '|', doska[5])
#     print('+++++++++')
#     print('\n', doska[6], '|', doska[7], '|', doska[8], '\n')
#
#
# def dostupnie_hodi(doska):
#     dostupnie_hodi = []
#     for i in range(RAZMER_DOSKI):
#         if doska[i] == HODI:
#             dostupnie_hodi.append(i)
#     return dostupnie_hodi
#
#
# def winner(doska):
#     VAR_POBED = ((0, 1, 2),
#                  (3, 4, 5),
#                  (6, 7, 8),
#                  (0, 3, 6),
#                  (1, 4, 7),
#                  (2, 5, 8),
#                  (0, 4, 8),
#                  (2, 4, 6))
#     for i in VAR_POBED:
#         if doska[i[0]] == doska[i[1]] == doska[i[2]] != HODI:
#             winner = doska[i[0]]
#             return winner
#         if HODI not in doska:
#             return NICHYA
#     return None
#
#
# def human_hod(doska, human):
#     dostupnie = dostupnie_hodi(doska)
#     hod = None
#     while hod not in dostupnie:
#         hod = hod_number(0, RAZMER_DOSKI)
#         if hod not in dostupnie:
#             print('Поле занято. Напиши другой номер: ')
#     print('Супер!')
#     return hod
#
#
# def comp_hod(doska, comp, human):
#     doska = doska[:]
#     BEST_HODI = (4, 0, 2, 6, 8, 1, 3, 5, 7)
#     print('Мой ход: ')
#     for i in dostupnie_hodi(doska):
#         doska[i] = comp
#         if winner(doska) == comp:
#             print(i)
#             return i
#         doska[i] = HODI
#     for j in dostupnie_hodi(doska):
#         doska[j] = human
#         if winner(doska) == human:
#             print(j)
#             return j
#         doska[j] = HODI
#     for k in dostupnie_hodi(doska):
#         print(k)
#         return k
#
#
# def next_ochered(ochered):
#     if ochered == X:
#         return O
#     else:
#         return X
#
#
# def pozdrav_pobeditela(pobeditel, comp, human):
#     if pobeditel != NICHYA:
#         print('Собрана линия ', pobeditel)
#     else:
#         print(NICHYA)
#     if pobeditel == comp:
#         print('Компьютер выиграл!')
#     elif pobeditel == human:
#         print('Ты победил!')
#     elif pobeditel == NICHYA:
#         print(NICHYA)
#
#
# def main():
#     instrukciya()
#     comp, human = fishki()
#     ochered = X
#     doska = new_doska()
#     pokaz_doski(doska)
#     while not winner(doska):
#         if ochered == human:
#             hod = human_hod(doska, human)
#             doska[hod] = human
#         else:
#             hod = comp_hod(doska, comp, human)
#             doska[hod] = comp
#         pokaz_doski(doska)
#         ochered = next_ochered(ochered)
#     pobeditel = winner(doska)
#     pozdrav_pobeditela(pobeditel, comp, human)
#
#
# main()
# input('\n Нажми Entr, чтобы выйти')



# a = ("How can mirrors be real  our eyes aren real")
# def to_jaden_case(string):
#     a = string.title()
#     return a
# def invert(list):
#     empty = []
#     for num in list:
#         num = num * -1
#     empty.append(num)
#     return empty


# def sale_hotdogs(n):
#     if n < 5:
#         sum_ = n
#         sum_ *= 100
#         return sum_
#     if n >=5 and n < 10:
#         sum_ = n
#         sum_ *= 95
#         return sum_
#         sum_ = n
#     if n >=10:
#         sum_ *= 90
#         return sum_