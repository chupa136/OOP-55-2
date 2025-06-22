# Магические методыAdd commentMore actions
# (или dunder-методы, от "double underscore")

# class Hero:
#
#     def __init__(self, name, hp, lvl=None):
#         self.name = name
#         self.lvl = lvl
#
#     def __str__(self):
#         return "Наш текс"
#
# hero = Hero(name="Name", hp=123, lvl=100)
#
# test = 12
# test2 = 12
#
# test3 = test2 + test
#
# print(int)


class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print(f"{self.x}")
        print(f"{other.x}")
        return "Наш текст"

    def __eq__(self, other):
        return "не равен"

    def __gt__(self, other):
        return "Правильно"

    def __lt__(self, other):
        return "Правильно"

v1 = Vector(10, 20)
v2 = Vector(5, 1)

v3 = v1 < v2

# print(f"{v3}")

class CustomList:

    def __init__(self, items):
        self.items = items

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        return print("Не удалю")

    # def __call__(self, *args, **kwargs):

    # def __exit__(self, exc_type, exc_val, exc_tb):
    # def __dir__(self):


my_list = CustomList([1,23,123,4,32,321,423,4,12])

# print(dir(my_list))

# my_list[1] = 25
#
# print(my_list.items)
# del my_list[5]


# Модули - main.py все файлы с расширением .py
# from lesson3 import BankAccount
#
# user1 = BankAccount('user',123,123)
#
# print(user1)

# Пакеты - это папка которая содержит несколько модулей



from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')