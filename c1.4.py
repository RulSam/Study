# user_peter = {
#     "name": "Peter",
#     "email": "peterrobertson@mail.com",
#     "created_at": "2019-05-05",
#     "is_email_verified": True,
#     "purchases": ["Egg", "Spam", "Hat", "Knife", "Shield", "Book of Knight secrets"],
# }
#
# user_julia = {
#     "name": "Julia Donaldson",
#     "email": "juliadonaldson@mail.com",
#     "created_at": "2019-06-13",
#     "is_email_verified": True,
#     "purchases": ["Egg", "Spam", "Magic Brush"],
# }
#
# product_eggs = {
#     "name": "Egg",
#     "category": "food",
#     "is_available": False,
#     "quantity_in_stock": 0,
#     "vendor": "Dark Knight LTD",
#     "manager": "William The Conqueror",
# }
#
#
# def is_product_available(product):
#     return True if product["quantity_in_stock"] > 0 else False

# class User:
#     pass
# peter = User()
# peter.name = "Peter Robertson"
# peter.email = "peterrobertson@mail.com"
#
# julia = User()
# julia.name = "Julia Donaldson"
#
# print(peter.email)
# print('\n')
# print(julia.email)

# Мы можем задавать атрибуты, которые будут доступны из любого объекта, причём без дополнительных действий. Для этого их надо объявлять прямо внутри класса:

# class User:
#     number_of_fingers = 5
#     number_of_eyes = 2
#
# lancelot = User()
# print(lancelot.number_of_fingers)
# array = [[0, 1, 2, 3, 4],
#          [10, 11, 12, 13, 14],
#          [20, 21, 22, 23, 24],
#          [30, 31, 32, 33, 34]]
#
#
# def to_csv_text(array):
#     for i in array: print("\n".join(list(map(str, array))))
# a = [[0, 1, 2, 3, 4],
#          [10, 11, 12, 13, 14],
#          [20, 21, 22, 23, 24],
#          [30, 31, 32, 33, 34]]
#
# to_Csv_Text=a=a.join("\n")

def say_hello(name):
    print('Hello,', name)
