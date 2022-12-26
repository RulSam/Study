import redis

red = redis.Redis(
    host='redis-15266.c89.us-east-1-3.ec2.cloud.redislabs.com',
    port=15266,
    password=''
)



Теперь давайте попробуем записать данные в кеш. Для этого используется метод: .set(<название переменной для хеширования>, <значение переменной в виде строки>).
import redis

red = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

red.set('var1', 'value1')  # записываем в кеш строку "value1"
print(red.get('var1'))  # считываем из кеша данные




авайте теперь удалим некоторые строчки и убедимся, что данные, которые мы записывали в предыдущей сессии, сохранились

import redis

red = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

print(red.get('var1'))  # считываем из кеша данные



Как видим, строки хранятся отлично. И получать их можно оттуда так же легко. Давайте теперь попробуем записать в кеш что-нибудь посложнее, например, словарь.

import redis
import \
    json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?

red = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(
    red.get('dict1'))  # с помощью знакомой нам функции превращаем данные, полученные из кеша обратно в словарь
print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
print(converted_dict)  # ну и выводим его содержание


Наконец, давайте научимся удалять данные из кеша по ключу. Это делается совсем просто.

import redis
import json

red = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

red.delete('dict1')  # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))






Задание 5.5.4
Напишите программу, которая будет записывать и кешировать номера телефонов ваших друзей.

Программа должна уметь воспринимать несколько команд:

записать номер;
показать номер друга в консоли при вводе имени;
удалить номер друга по имени.
Кеширование надо производить с помощью Redis. Ввод и вывод информации должен быть реализован через консоль (с помощью функций input() и print()).
red = redis.Redis(
    host='ваш хост',
    port=ваш
порт,
password = пароль
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break