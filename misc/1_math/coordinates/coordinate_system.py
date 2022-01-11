import math
from abc import ABC


class Coordinate(float):
    def __str__(self):
        return str(round(self, 3))


class Phi(Coordinate):

    def __init__(self, value: int | float):
        self.__phi = Coordinate(value)

    @property
    def degrees(self) -> Coordinate:
        return Coordinate(math.degrees(self.__phi) % 360)


class CoordinatesBase(ABC):
    attr_names = "", ""

    def __init__(self, x: float | int, y: float | int):
        self.set(x, y)

    def set(self, x: float | int, y: float | int):
        self._xx, self._yy = Coordinate(x), Coordinate(y)

    def get(self) -> (Coordinate, Coordinate):
        return self._xx, self._yy

    def __str__(self):
        x, y = attr_names
        return f"{self.__class__.__name__}<({x}={self._xx}, {y}={self._yy})>"


class Cartesian(CoordinatesBase):
    attr_names = "x", "y"

    def create_polar(self) -> "Polar":
        return Polar(*self.__convert_to_polar())

    def __convert_to_polar(self) -> (float, float):
        x, y = self._xx, self._yy
        phi = math.atan2(y, x)
        phi = math.pi * 2 + phi if phi < 0 else phi
        return math.sqrt(x * x + y * y), phi

    @property
    def x(self) -> Coordinate:
        return self._xx

    @property
    def y(self) -> Coordinate:
        return self._yy


class Polar(CoordinatesBase):
    attr_name = "rho", "phi"

    def create_cartesian(self) -> "Cartesian":
        return Cartesian(*self.__convert_to_cart())

    def __convert_to_cart(self) -> (float, float):
        rho, phi = self._xx, self._yy
        return rho * math.cos(phi), rho * math.sin(phi)

    def set(self, x: float | int, y: float | int):
        self._xx, self._yy = Coordinate(x), Phi(y)

    @property
    def rho(self) -> Coordinate:
        return self._xx

    @property
    def phi(self) -> Phi:
        return self._yy


if __name__ == '__main__':
    p = Cartesian(2, 3).create_polar()
    c = p.create_cartesian()
    print("Radius:", p.rho)
    print("Degrees:", p.phi.degrees)

