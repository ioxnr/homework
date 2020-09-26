from abc import ABC, abstractmethod


class Textile(ABC):

    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def consumption(self):
        pass

    @property
    def full_consumption(self):
        return f'Общая расход ткани равен {(self.size / 6.5 + 0.5) + (2 * self.height + 0.3)}'


class Coat(Textile):

    def __init__(self, size, height):
        super().__init__(size, height)

    def consumption(self):
        return f'Расход ткани для пальто равен {self.size / 6.5 + 0.5}'


class Suit(Textile):

    def __init__(self, size, height):
        super().__init__(size, height)

    def consumption(self):
        return f'Расход ткани для костюма равен {2 * self.height + 0.3}'


coat = Coat(6, 5)
suit = Suit(5, 10)
print(coat.consumption())
print(suit.consumption())
print(coat.full_consumption)
