from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def method(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def method(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def method(self):
        return self.height * 2 + 0.3


coat = Coat(5)
print(f'Расход ткани для пальто составит: {coat.method:.2f}')

costume = Costume(6)
print(f'Расход ткани для костюма составит: {costume.method:.2f}')

print(f'Общий расход ткани составит: {coat.method + costume.method:.2f}')
