# Завдання 2
# Створіть клас Passport (паспорт), який міститиме
# паспортну інформацію про громадянина заданої країни.
# За допомогою механізму успадкування реалізуйте
# клас ForeignPassport (закордонний паспорт), похідний
# від Passport.
# Нагадаємо, що закордонний паспорт містить, крім
# паспортних даних, дані про візи і номер закордонного
# паспорта.
# Кожен із класів має містити необхідні методи.
class Passport:
    def __init__(self, name, passport_number, age, country):
        self.name = name
        self.passport_number = passport_number
        self.age = age
        self.country = country


class ForeignPassport(Passport):
    def __init__(self, name, passport_number, age, country, visas):
        super().__init__(name, passport_number, age, country)
        self.passport_number = passport_number
        self._visas = visas

    def show_info(self):
        super().show_info()
        print(f"Foreign Passport Number: {self.foreign_passport_number}")
        print("Visa Information:")
        for visa in self.visa_info:
            print(f"- {visa}")


passport = Passport("John Doe", "AB123456", "USA")
passport.show_info()
print()
foreign_passport = ForeignPassport("Alice Smith", "CD789012", "UK", ["USA", "Canada"], "XYZ987654")
foreign_passport.show_info()



