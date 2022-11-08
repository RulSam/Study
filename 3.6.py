# S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
# N = 5
# #
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# p = 1
# n = 5
# for i in range(1, n + 1):
#     p *= i
#     print(p)

# n = 3
# for i in range(1, n + 1):
#    print("*" * i)
#
# S = 0  # заводим переменную-счётчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счётчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n-1)

# Напишите цикл while, который находит максимальное натуральное число, квадрат которого меньше 1000.
#
# Решение
# n = 1
# while n**2 < 1000:
#     n += 1
# print("Искомое число", n - 1)

# n = 1
# while True:
#     if n**2 >= 1000:
#
#         print("Искомое число", n - 1)
#         break
#     n += 1
#
# N = 2
# M = 3
# # заполнили матрицу последовательными числами
# matrix = [
#     [0, 1, 2],
#     [3, 4, 5],
# ]
#
#
# for i in range(N):  # цикл, отвечающий за строки
#     for j in range(M):  # цикл, отвечающий за столбцы
#         print(matrix[i][j], end=" ")
# # 0 1 2 3 4 5
# a = 3
# b = 3
# ranrandom_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
#
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
#
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print("Минимальные элементы:", min_value_rows)
# print("Их индексы:", min_index_rows)
# print("Максимальные элементы:", max_value_rows)
# print("Их индексы:", max_index_rows)