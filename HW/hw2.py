import random
class Heroes:
    def __init__ (self, name, hp,):
        self.name = name
        self.hp = hp

    def action(self):
        return(f"{self.name} ready!")

    def attack(self):
        return(f"{self.name} attack!")


class Archer(Heroes):
    def __init__(self, name, hp, arrows=None, precision=None):
        super().__init__(name,hp)
        self.arrows = arrows
        self.precision = precision


    def attack (self):
        self.arrows -= 1
        if random.random() < self.precision: #0-1
            print(f'Sucsess!')
        else:
            print(f'Fail!')
        return (f"You have {self.arrows} arrow")

    def rest(self):
        self.arrows += 5
        return (f"Replenished 5 arrows ")

    def status(self):
        return (f"Name: {self.name}, HP: {self.hp},"
                f" Arrows: {self.arrows}, Precision: {self.precision*100}%")


#write precision 0-1 | 0.5 = 50%
damir =(Archer("Damir", 100, 10, 0.5))
print(damir.status())
print(damir.action())
print(damir.rest())
print(damir.status())
damir.attack()
damir.attack()
print(damir.status())

