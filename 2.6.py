# s = []
# s = [0, 'hello', (1, 'a')]
# letters = ['a', 'b', 'c', 'd']
# letters.append('e')
# print(letters)
# # ['a', 'b', 'c', 'd', 'e']
# print(letters[1])
# print(letters[0])
# print(len(letters))
# print(letters[len(letters)-1])
#
# [:]	Возвращает элементы полностью	[‘a’, ‘b’, ‘c’, ‘d’, ‘e’, ‘f’, ‘g’]
# [2:]	Возвращает элементы списка, начиная с элемента индекса 2 и до конца списка	[‘c’, ‘d’, ‘e’, ‘f’, ‘g’]
# [:3]	Возвращает элементы списка от его начала до элемента с индексом 3, не включая его	[‘a’, ‘b’, ‘c’]
# [1:4]	Объединяя предыдущие два способа, можно получить элементы из середины. В данном случае начиная с индекса 1 до индекса 4, не включительно. Иными словами, элементы с индексами 1,2 и 3	[‘b’, ‘c’, ‘d’]
# [::2]	Задает шаг, через который извлекаются элементы	[‘a’, ‘c’, ‘e’, ‘g’]
# [::-1]	Используя отрицательный шаг, можно развернуть массив	[‘g’, ‘f’, ‘e’, ‘d’, ‘c’, ‘b’, ‘a’]
#
# L = ["а", "б", "в", 1, 2, 3, 4]
# print(L[1:4])
# print(L[::3])
# print(L[3::-1])
# print(L[-1:-4:-1])
#
# # имеем список с числами с плавающей точкой
# L = [3.3, 4.4, 5.5, 6.6]
#
# # печатаем сам объект map
# print(map(round, L)) # к каждому элементу применяем функцию округления
# # <map object at 0x7fd7e86eb6a0>
#
# # и результат его преобразования в список
# print(list(map(round, L)))
# # # [3, 4, 6, 7]
# L = ['3.3', '4.4', '5.5', '6.6']
# # print(map(int, L))
# # print (list (map ( float ,  L)))
#
# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # cписок чисел
#
# print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка
#
# string = input("Введите числа через пробел:")
# list_of_strings = string.split()
# L = list(map(float, list_of_strings))
# L[0], L[-1] = L[-1], L[0]
# print(sum(L))
#
# person = {} # с помощью фигурных скобок можно создать словарь
#
# # словарь заполняется по принципу — ключ:объект (через двоеточие)
# person = {'name' : 'Ivan Petrov'}
#
# # в него можно также добавлять новые объекты по ключу
# person['age'] = 25
# person['email'] = 'ivan_petrov@example.com'
# person['phone'] = '8(800)555-35-35'
#
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
# # print(person['address'])
# # KeyError: 'address'
# # Можно отдельно получить список ключей:
#
# print(person.keys())
# # dict_keys(['name', 'age', 'email', 'phone'])
# # Или список значений:
#
# print(person.values())
# # dict_values(['Ivan Petrov', 25, 'ivan_petrov@example.com', '8(800)555-35-35'])
#
# # Из словаря аналогично спискам можно удалить объект по его ключу. Словарь является упорядоченным. В функцию pop() всегда нужно передавать ключ удаляемого объекта:
#
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
#
# person.pop('phone')
#
# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com'}
#
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))
# title = input("write title:")
# author = input("write author:")
# year = int(input("write year:"))
# Book={'title': title, 'author': author, 'year': year}
# print(Book)
# title = input("write title:")
# author = input("write author:")
# year = input("write year:")
# Book={'title': title, 'author': author, 'year': year}
# print(Book)
#
# abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
# abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
# abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}
# abits = [abit1, abit2, abit3]
# print(abits)
#
# a = {'a', 'b', 'c', 'd'}
# L = {1, 1, 2, 3, 2}
# b= set(L)
# print(b)
# b_list=list(b)
# print(b_list)
# ля краткостти можно написать см ниж
# c = list(set(L))
#
# print(c)
# # [1,2,3]
#
# text = input("Введите текст")
# unique = list(set(text))
# print("Уникальные символы", len(unique))
#
# set.union(other)	Объединение	Возвращает множество, состоящее из элементов set и other.
# set.intersection(other)	Пересечение	Возвращает множество, состоящее из элементов, которые встречаются и в set, и в other.
# set.difference(other)	Разность	Возвращает множество элементов set, которые не встречаются в other.
# set.symmetric_difference(other)	Симметричная разность	Возвращает множество элементов, встречающиеся в одном из множеств, но не в обоих одновременно.
#
#
# abons = {"Иванов", "Петров", "Васильев", "Антонов"}
#
# debtors = {"Петров", "Антонов"}
#
# non_debtors = abons.difference(debtors)
#
# print(non_debtors)
# # {'Васильев', 'Иванов'}
#
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# a_set, b_set = set(a), set(b)
# a_and_b = a_set.intersection(b_set)
# print(a_and_b)
#
# a = input("Превое число")
# b = input("вторе число")
# a_set, b_set = set(a), set(b)
# a_and_b = a_set.symmetric_difference(b_set)
# print(a_and_b)
#
