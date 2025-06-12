class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} , я живу в {self.city}"

    def is_adult(self):
        if self.age >= "18":
            return True
        else:
            return False

Me = Person("Damir","16","Bishkek")
person1 = Person("Amir","26","Talas")

print(Me.introduce())
print(Me.is_adult())
print(person1.introduce())
print(person1.is_adult())