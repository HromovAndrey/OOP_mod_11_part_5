

# Завдання 3
# Створіть базовий клас «Тварина» та похідні класи:
# «Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
# конструктора ім’я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, "Tiger")

    def move(self):
        return "Running"

    def sound(self):
        return "Roar"


class Crocodile(Animal):
    def __init__(self, name):
        super().__init__(name, "Crocodile")

    def move(self):
        return "Swimming"

    def sound(self):
        return "Growl"


class Kangaroo(Animal):
    def __init__(self, name):
        super().__init__(name, "Kangaroo")

    def move(self):
        return "Hopping"

    def sound(self):
        return "Clicking"


tiger = Tiger("Shere Khan")
print(f"{tiger.name} the {tiger.species} is {tiger.move()} and makes a {tiger.sound()} sound.")

crocodile = Crocodile("Snappy")
print(f"{crocodile.name} the {crocodile.species} is {crocodile.move()} and makes a {crocodile.sound()} sound.")

kangaroo = Kangaroo("Joey")
print(f"{kangaroo.name} the {kangaroo.species} is {kangaroo.move()} and makes a {kangaroo.sound()} sound.")