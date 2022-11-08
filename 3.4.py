# A = int(input("Bведите число 1:"))
# B = int(input("Bведите число 2:"))
# are_both_odd = ("A", "B")
# if A % 2 == 1 and B % 2 == 1:
#     print(1)
# else:
#     print(0)
# x = int(input("введите число:"))
# y = int(input("введите число:"))
# if x > 0 and y > 0:
#     print("Первая четверть")
# if x > 0 and y < 0:
#          print("Четвертая четверть")
# if x < 0 and y > 0:
#          print("Вторая четверть")
# if x < 0 and y < 0:
#          print("Третья четверть")

# mount = int(input())
#
# if mount in [3, 4, 5]:
#     print("Весна")
# elif mount in [6, 7, 8]:
#     print("Лето")
# elif mount in [9, 10, 11]:
#     print("Осень")
# elif mount in [12, 1, 2]:
#     print("Зима")

# def get_wind_class(speed):  # Объявление функции
#  if 1 <= speed <= 4:
#     return ("weak [1]")
#  elif 5 <= speed <= 10:
#     return ("moderate [2]")
#  elif 11 <= speed <= 18:
#     return ("strong [3]")
#  elif 19 <= speed:
#     return ("hurricane [4]")
# print(get_wind_class(3))

# user_database = {
#     'user': 'password',
#     # 'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }

# def check_user(username, password):
#     if username in user_database:
#         if password == user_database [username]:
#             return True
#         else: return False
#     else: return False


# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# Записать логические выражения, которые определяют, что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
#
# Решение
# A = int(input('Введите число\n'))
#
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
#     print("Число принадлежит интервалу")


# Дано двузначное число. Определить: входит ли в него цифра 5. Попробуйте решить её с использованием целочисленного деления и деления с остатком.
# a = int(input("Введите число"))
# check_number = '5' in str(a)
# print(check_number)
#
# или
#
# n = 15
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# Проверить, все ли элементы в списке являются уникальными.
#
# Подсказка
# Решение
# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# print(len(list_) == len(set(list_)))

# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково слева направо и справа налево).
#
# Подсказка
# Использовать целочисленное деление и деление с остатком не нужно. Попробуйте преобразовать число к строке, а потом перевернуть эту строку. См. материал прошлого модуля.
# Решение
# num = 12345678
#
# print(str(num) == str(num)[::-1])