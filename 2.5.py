# s1 = 'hello'
# s2 = "hola"
# s3 = """Привет!Хорошего дня!"""
# s4 = s3[0:5:2]
# print(s4)
# s = "Hello"
# print(s[0])
# print(s[4])
# print(s[1:4])

# print(len(s))
# print(s.find('e'))
# print(s.find('o'))
# print(s.isdigit())
# print(s.isalpha())
# print(s.isalnum())

# print(s.upper())
# print(s.lower())

# # Practice
# colors = 'red blue green'
# # print(colors.split())
# # path = '/home/user/documents/file.txt'
# # print(path.split('/'))
# colors_split = colors.split()
# colors_joined = ' '.join(colors_split)
# print(colors_joined)

# data = '1 2 3 4 5 6 7'
# print(data.split())

# numbers = '1 2 3 4 5 6 7'
# numbers_split = numbers.split()
# numbers_joined = "\n".join(numbers_split)
# print(numbers_joined)

# int_num = int(input("Введите целое число"))
# print(int_num)
# print(type(int_num))

# age = 25
# my_age = "i'm " + str(age)
# print(my_age)

# age = int(input ("Введите ваш возраст"))
# my_age = "i'm " + str(age)
# print(my_age)

# age = 25
#
# my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d
#
# print(my_age)
# # I'm 25 years old

# %d, %i	Целое число
# %5d, %12d	Выделяет пространство 5 (или любое другое число) символов под это число. Выравнивание вправо, остальное пространство остаётся пустым
# %05d	Также выделяется пространство в 5 символов, но свободное пространство слева заполняется нулями
# %o	Число в восьмеричной системе счисления
# %x	Число в шестнадцатеричной системе счисления
# %f	Число с плавающей точкой
# %10.2f	Число с плавающей точкой, для которого зарезервировано пространство из 10 символов и стоит ограничение на количество знаков после запятой — 2
# %e	Также число с плавающей точкой, но в экспоненциальной записи
# %c	Код символа
# %s	Другая строка
# %%	Знак процента, если его необходимо использовать просто как символ в строке
#
# pi = 31.4159265
# print ("%.4e" % (pi))
# HH = 1
# MM = 2
# SS = 3
# print("%02d.%02d.%02d" % (HH, MM, SS))
