# Завдання 4
# Створіть базовий клас Clock, який містить атрибути
# години та хвилини. Від цього базового класу
# успадковуйте два класи: AnalogClock та DigitalClock.
# Клас AnalogClock повинен мати метод display_time,
# який виводить поточний час у форматі
# "години:хвилини". Клас DigitalClock повинен мати
# метод display_time, який виводить поточний час у
# цифровому форматі "гг:хх".
# Створіть об'єкти кожного класу та виведіть
# поточний час за допомогою методу display_time.

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


class AnalogClock(Clock):
    def display_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}")


class DigitalClock(Clock):
    def display_time(self):
        print(f"{self.hour:02d}:{self.minute:02d}")

analog_clock = AnalogClock(10, 30)
analog_clock.display_time()  # Виведе "10:30"

digital_clock = DigitalClock(14, 45)
digital_clock.display_time()  # Виведе "14:45"



