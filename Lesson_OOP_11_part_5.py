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

class Figure:
    def __init__(self, area):
        self._area = area
        print("init from Figure")

class Circle(Figure):
    def __init__(self, area, radius):
        super().__init__(area)
        self._radius = radius
        print("init from Circle")


    def print_info(self):
        print(f"{self._area=}")
        print(f"{self._radius=}")

obj = Circle(20, 3)
obj.print_info()

