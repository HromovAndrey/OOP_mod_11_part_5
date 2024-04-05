# class Animal:
#     def sound(self):
#         print("Some sound: hrrr")
#
#     def make_noise(self):
#         self.sound()
#         self.sound()
#         self.sound()
#
# class Dog(Animal):
#     def run(self):
#         print("Dog is running")
#
#     def sound(self):
#          print("Hav-hav")
#
# class Cat(Animal):
#     def sound(self):
#          print("Miau")
#
# obj = Dog
# obj.sound()
# obj.make_noise()


# class Animal:
#     def make_sound(self):
#         print("Гучно оре")
#
# class Dog(Animal):
#     def make_sound(self):
#         #super().make_sound() #Викликаємо метод батьківського класу
#         print("Woof!")
#
# #творення обьєкта класу Dog
# dog = Dog("Buddy", "Golden Retriever")
#
# #  Виклик медоду make_sound бьєкта класу Dog
# dog.make_sound()


# class Animal:
#     def sound(self):
#         print("Some sound: hrrr")
#
#     def make_sound(self):
#         self.sound()
#         self.sound()
#         self.sound()
# class Cat(Animal):
#     def sound(self):
#         super().sound()
#         print("Miau")
#
#     def get_super(self):
#         print(super())
#
# cat = Cat()
# cat.get_super()
# cat.sound()

# class Figure:
#     def __init__(self, area):
#         self._area = area
#         print("init from Figure")
#
# class Circle(Figure):
#     def __init__(self, area, radius):
#         super().__init__(area)
#         self._radius = radius
#         print("init from Circle")
#
#
#     def print_info(self):
#         print(f"{self._area=}")
#         print(f"{self._radius=}")
#
# obj = Circle(20, 3)
# obj.print_info()
#
# class Person:
#     def __init__(self, name, surname, place_of_birth, year_of_birth):
#         self.name = name
#         self.surname = surname
#         self.place_of_birth = place_of_birth
#         self.year_of_birth = year_of_birth
#
#     def print_info(self, n):
#         for i in range(n):
#             print(f"name: {self.name}, surname: {self.surname}, Place of birth:{self.place_of_birth}, year_of_birth:{self.year_of_birth}")
#
#
#     def get_age(self, current_yaer):
#         return current_yaer - self.year_of_birth
#
# p1 = Person("Elon", "Musk", "UAR", 1971)
# p2 = Person("Sergii", "Korolev", "Russia", 1907)
# p3 = Person("Albert", "Einstein", "Germany", 1879)
#
# p1.print_info(1)
# p2.print_info(1)
# p3.print_info(1)


# class Cat:
#     breed = "pars"
#
#     def set_value(self, value, age=0):
#         self.name = name
#         self.age = age
#
#     def __init__(self):
#        print("Hello new object", self)
#
# Jerry = Cat

class Person:
     age = 18
     def __init__(self, x, y):
         self.height = x
         self.age = y
p = Person(179, "Andrii")
print(p.__dict__)




