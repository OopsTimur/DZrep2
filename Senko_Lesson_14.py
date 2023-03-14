# Senko_Timur group_208
# DZ



# 1. Создайте класс Person, который имеет атрибуты name и age,
# а также метод greet() (выводит приветствие на экран с именем персоны).
class person:
    name = 'Timur'
    age = 25
    def greet(self):
        print(f'Hello {self.name}')


timur = person()
timur.greet()


# 2. Создайте класс Car, который имеет атрибуты make, model и year,
# а также метод get_info() (возвращает строку, содержащую информацию о машине).

class Car:
    make = "Tesla"
    model = "Tesla_X"
    year = 2008
    def get_info(self):
        return f'Make: {self.make}. Year of release: {self.year}. Model: {self.model}'


Tesla_Car = Car()
print(Tesla_Car.get_info())