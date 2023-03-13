# Senko_Timur 208_group
# DZ
import self as self


# 1. Создайте класс Person, который имеет атрибуты name и age,
# а также метод greet() (выводит приветствие на экран с именем персоны).
class person:
    name = 'Timur'
    age = 25

    @staticmethod  # Нажал alt + enter, выбило автоматом staticmethod, я так понял, он нужен, если в функции не нужны аргументы
    def greet():
        print(f'Hello {person.name}')


person.greet()


# 2. Создайте класс Car, который имеет атрибуты make, model и year,
# а также метод get_info() (возвращает строку, содержащую информацию о машине).

class Car:
    make = "Tesla"
    model = "Tesla_X"
    year = 2008

    @staticmethod
    def get_info():
        return f'Make: {Car.make}. Year of release: {Car.year}. Model: {Car.model}'


print(Car.get_info())
