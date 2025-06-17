class Animal:
    def make_sound(self):
        return f"Издает звук"
class Flyable:
    def move(self):
        return f"Летит"

class Swimable:
    def move(self):
        return f"Плавает"

class Duck(Animal, Flyable, Swimable):
        pass

donald = Duck()
print(donald.move())

class A:
    def test_method(self):
        return "Class A"

class B(A):
    def test_method(self):
        return super().test_method()

class C(A):
    def test_method(self):
        return super().test_method()

class D(B,C):
    pass

obj = B()

print(B.__mro__)

#import logging

class Math:
    sum = print("123")

    def __init__(self, test):
        self.test = test

    @staticmethod
    def add(a,b):
        return a + b

    @classmethod
    def get_sum(cls):
        return cls.sum

    def just_method(self):
        return None

print(Math.sum)

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def get_radius(self):
        return self.__radius

    @property
    def area(self):
        return 3.14 * self.__radius

def my_decorator(func):
    def wrapper():
        print('Перед выполнением функции')
        func()
        print('После выполнения функции')
    return wrapper

@my_decorator
def hello():
    print('hello world!!')

@my_decorator
def test():
    print("test")

hello()
test()

def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator

@repeat(5)
def hello():
    print("Hello")

hello()

def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            return "Новый метод!!!"
    return NewClass

@class_decorator
class MyClass:
    def old_method(self):
        return "Старый метод"

obj = MyClass()

print(obj)

class A:
    def a(self):
        return 'a'

class B(A):
    def b(self):
        return "b"

class C(A):
    def b(self):
        return "b"