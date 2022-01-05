import math


class Coord(float):
    def __str__(self):
        return str(round(self, 3))


class Phi(Coord):

    def __init__(self, value: int | float):
        self.__phi = Coord(value)

    @property
    def degrees(self) -> Coord:
        return Coord(math.degrees(self.__phi) % 360)


class Cartesian:

    def __init__(self, x: float | int, y: float | int):
        self.set(x, y)

    def set(self, x: float | int, y: float | int):
        self.__x, self.__y = Coord(x), Coord(y)

    def get(self) -> (Coord, Coord):
        return self.__x, self.__y

    def create_polar(self) -> "Polar":
        return Polar(*self.__cart2pol())

    def __cart2pol(self) -> (float, float):
        x, y = self.__x, self.__y
        phi = math.atan2(y, x)
        phi = math.pi * 2 + phi if phi < 0 else phi
        return math.sqrt(x * x + y * y), phi

    def __str__(self):
        return f"{self.__class__.__name__}<(x={self.__x}, y={self.__y})>"

    @property
    def x(self) -> Coord:
        return self.__x

    @property
    def y(self) -> Coord:
        return self.__y


class Polar:
    def __init__(self, rho: float | int, phi: float | int):
        self.set(rho, phi)

    def set(self, rho: float | int, phi: float | int):
        self.__rho, self.__phi = Coord(rho), Phi(phi)

    def get(self) -> (Coord, Phi):
        return self.__rho, self.__phi

    def create_cartesian(self) -> "Cartesian":
        return Cartesian(*self.__pol2cart())

    def __pol2cart(self) -> (float, float):
        rho, phi = self.__rho, self.__phi
        return rho * math.cos(phi), rho * math.sin(phi)

    def __str__(self):
        return f"{self.__class__.__name__}<(rho={self.__rho}, phi={self.__phi})>"

    @property
    def rho(self) -> Coord:
        return self.__rho

    @property
    def phi(self) -> Phi:
        return self.__phi


if __name__ == '__main__':
    c = Cartesian(2, 3).create_polar()
    p = Polar(3, 1).create_cartesian()
    print("Radius:", c.rho)
    print("Degrees:", c.phi.degrees)

