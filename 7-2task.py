from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, cost):
        self.cost = cost

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.cost / 6.5) + 0.5

class Costume(Clothes):
    @property
    def consumption(self):
        return (2 * self.cost + 0.3) / 100

coat_param = Coat(40)
costume_param = Costume(130)
print(costume_param + coat_param)

