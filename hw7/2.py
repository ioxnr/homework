from abc import ABC, abstractmethod


class Textile(ABC):

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def consumption(self):
        pass


class Coat(Textile):

    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    @property
    def consumption(self):
        return f'Расход ткани для пальто равен {self._size / 6.5 + 0.5}'


class Suit(Textile):

    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    @property
    def consumption(self):
        return f'Расход ткани для костюма равен {2 * self._height + 0.3}'


coat = Coat('Пальто', 5)
suit = Suit('Костюм', 10)
print(coat.consumption)
print(suit.consumption)
