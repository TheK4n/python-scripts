import abc
import math
from abc import ABC


class Coord(ABC):

    def __init__(self):
        self._x = self._y = 0

    def __str__(self):
        return f"<{self.__class__.__name__}(x={self._x}, y={self._y})>"

    @property
    def x(self) -> int | float:
        return self._x

    @property
    def y(self) -> int | float:
        return self._y

    def get(self) -> (int | float, int | float):
        return self._x, self._y

    @staticmethod
    def _check_value(*args) -> bool:
        return all(map(lambda x: isinstance(x, (int, float)), args))

    @abc.abstractmethod
    def set(self, *args):
        pass


class Cartesian(Coord):

    def set(self, *args):
        if isinstance(args[0], Polar):
            self._x, self._y = self.__from_polar_to_cart(*args[0].get())
            return self
        else:
            if self._check_value(*args):
                self._x = args[0]
                self._y = args[1]
            else:
                raise ValueError("Coord must be int or float or Polar")

    @staticmethod
    def __from_polar_to_cart(x, y, to_round=3):
        return round(x * math.cos(y), to_round), round(x * math.sin(y), to_round)


class Polar(Coord):

    def set(self, *args):
        if isinstance(args[0], Cartesian):
            self._x, self._y = self.__from_cart_to_polar(*args[0].get())
            return self
        else:
            if self._check_value(*args):
                self._x = args[0]
                self._y = args[1]
            else:
                raise ValueError("coord must be int or float or Cartesian")

    @staticmethod
    def __from_cart_to_polar(x, y, to_round=3):

        radius = math.sqrt(x * x + y * y)

        if x == 0 and y == 0:
            f = 0
        elif x == 0 and y < 0:
            f = 3 * math.pi / 2
        elif x == 0 and y > 0:
            f = math.pi / 2
        elif x < 0:
            f = math.atan(y / x) + math.pi
        elif y < 0:
            f = math.pi * 1.5 - math.atan(y / x)
        else:
            f = math.atan(y / x)

        return round(radius, to_round), round(f, to_round)


def pelingator(a, b, delta_dist=25):
    a = (a + 360) % 360
    b = (b + 360) % 360

    if a < b:
        delta = abs(360 + a - b)
    else:
        delta = abs(b - a)
    return abs(round(delta_dist / math.sin(math.radians(delta)), 2))


if __name__ == '__main__':
    cart = Cartesian()
    cart.set(1, 2)

    polar = Polar()
    print(polar.set(cart).get())

    cart1 = Cartesian()
    print(cart1.set(polar).get())
