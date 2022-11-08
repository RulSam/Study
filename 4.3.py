#Написать функцию, которая будет перемножать любое количество переданных ей аргументов.

# def mul(*nums):
#     p = 1
#     for n in nums:
#         p *= n
#
#     return p
#
# pass
#
# print(mul(3,5))

# С помощью рекурсивной функции найдите сумму чисел от 1 до n.
#
# Решение
# def rec_sum(n):
#    if n == 1:  # терминальный случай
#        return 1
#    return n + rec_sum(n - 1)  # рекурсивный вызов

# С помощью рекурсивной функции разверните строку.
#
# Решение
# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')  # tset

#
# Дано натуральное число N. Вычислите сумму его цифр.
#
# При решении этой задачи нельзя использовать строки, списки, массивы (ну и циклы, разумеется).
#
# Решение
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# sum_digit(123)  # 6