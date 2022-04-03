from abc import ABC, abstractmethod

class Clouthes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clouthes):

    @property
    def calculate(self):
        return round((self.param / 6.5) + 0.5)

class Suit(Clouthes):

    @property
    def calculate(self):
        return round((2 * self.param) + 0.3)

coat = Coat(10)
suit = Suit(20)
print(coat.calculate)
print(suit.calculate)
