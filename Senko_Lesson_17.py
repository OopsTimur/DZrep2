# Senko_Timur group_208
# DZ

from abc import ABC, abstractmethod


class Zoo_animals:
    @abstractmethod
    def drink(self, water_use):
        pass

    @abstractmethod
    def eat(self, food_use):
        pass

    @abstractmethod
    def sleep(self, energy):
        pass

    @abstractmethod
    def posing(self, meal):
        pass

    @abstractmethod
    def info(self):
        pass


class Fish(Zoo_animals):
    __food = 500
    __water = 500
    __Sleepy_energy = 0
    __meal = 0
    scales = 'чешуя по всему телу'
    gills = 'у каждой рыбы есть жарбы.'

    def drink(self, water_use):
        self.__water -= water_use
        print(self.__water)

    def eat(self, food_use):
        self.__food -= food_use
        print(self.__food)

    def sleep(self, energy):
        self.__Sleepy_energy += energy
        print(self.__Sleepy_energy)

    def posing(self, meal):
        print('Рыбки не позируют!')

    def info(self):
        print(f'У рыб - {self.scales} и {self.gills}')


fish_1 = Fish()
fish_1.info()


class Animals(Zoo_animals):
    __food = 500
    __water = 500
    __Sleepy_energy = 0
    __meal = 100
    wool = 'шерсть по всему телу'
    ears = 2
    tail = 1

    def drink(self, water_use):
        self.__water -= water_use
        print(self.__water)

    def eat(self, food_use):
        self.__food -= food_use
        print(self.__food)

    def sleep(self, energy):
        self.__Sleepy_energy += energy
        print(self.__Sleepy_energy)

    def posing(self, meal):
        self.__meal -= meal
        print(f'Животное позирует')
        print(f'У вас было 100 гр. еды, вы потратили {meal}')

    def info(self):
        print(f'У животных - {self.wool}, при этом они имеют {self.ears} уха и {self.tail} хвост.')


Animal_dog = Animals()
Animal_dog.info()


class Birds(Zoo_animals):
    __food = 500
    __water = 500
    __Sleepy_energy = 0
    __meal = 100
    beak = 1
    feathers = "перья по всему телу"
    wings = 2

    def drink(self, water_use):
        self.__water -= water_use
        print(self.__water)

    def eat(self, food_use):
        self.__food -= food_use
        print(self.__food)

    def sleep(self, energy):
        self.__Sleepy_energy += energy
        print(self.__Sleepy_energy)

    def posing(self, meal):
        self.__meal -= meal
        print(f'Птица позирует позирует')
        print(f'У вас было 100 гр. еды, вы потратили {meal}')

    def info(self):
        print(f'У птиц {self.feathers} и {self.wings} крыла.')


Birds_parrot = Birds()
Birds_parrot.info()


class Amphibians(Zoo_animals):
    __food = 500
    __water = 500
    __Sleepy_energy = 0
    __meal = 100
    slippery_skyn = "У амфибий скользкая кожа"
    three_chamber_heart = "амфибии имеют трёхкамерное сердце."

    def drink(self, water_use):
        self.__water -= water_use
        print(self.__water)

    def eat(self, food_use):
        self.__food -= food_use
        print(self.__food)

    def sleep(self, energy):
        self.__Sleepy_energy += energy
        print(self.__Sleepy_energy)

    def posing(self, meal):
        self.__meal -= meal
        print(f'Амфибия позирует')
        print(f'У вас было 100 гр. еды, вы потратили {meal}')

    def info(self):
        print(f'{self.slippery_skyn} и {self.three_chamber_heart}')


Amphibians_lizard = Amphibians()
Amphibians_lizard.info()
