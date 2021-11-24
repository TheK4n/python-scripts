import math


class Coordinates:

    class Phi(float):
        def __init__(self, phi: float):
            self.__phi = phi

        @property
        def degrees(self):
            return math.degrees(self.__phi)

    def __init__(self, x: float | int, y: float | int, is_polar=False, to_round=3):

        if is_polar:
            self.__r = float(x)
            self.__phi = self.Phi(y)
        else:
            self.__x = float(x)
            self.__y = float(y)

        self.__to_round = to_round
        self.__is_polar = is_polar

    def get(self) -> (float, float):
        if self.__is_polar:
            return self.__r, self.__phi
        else:
            return self.__x, self.__y

    def __get__(self, instance, owner):
        return self.get()

    def __iter__(self):
        return iter(self.get())

    def __getitem__(self, key):
        return self.get()[key]

    def __cart2pol(self, x: float, y: float):
        return round(math.sqrt(x * x + y * y), self.__to_round), round(math.atan2(y, x), self.__to_round)

    def __pol2cart(self, rho: float, phi: float):
        return round(rho * math.cos(phi), self.__to_round), round(rho * math.sin(phi), self.__to_round)

    def polar(self):
        if self.__is_polar:
            return self

        polar_cords = self.__cart2pol(self.__x, self.__y)
        self.__r = polar_cords[0]
        self.__phi = self.Phi(polar_cords[1])
        self.__is_polar = True
        return self

    def cartesian(self):
        if not self.__is_polar:
            return self
        self.__x, self.__y = self.__pol2cart(self.__r, self.__phi)
        self.__is_polar = False
        return self

    def __str__(self):
        if self.__is_polar:
            return f"{self.__class__.__name__}<(r={self.__r}, phi={self.__phi})>"
        else:
            return f"{self.__class__.__name__}<(x={self.__x}, y={self.__y})>"

    @property
    def x(self) -> float:
        if not self.__is_polar:
            return self.__x

    @property
    def y(self) -> float:
        if not self.__is_polar:
            return self.__y

    @property
    def r(self) -> float:
        if self.__is_polar:
            return self.__r

    @property
    def phi(self) -> Phi:
        if self.__is_polar:
            return self.__phi


if __name__ == '__main__':
    c = Coordinates(1, -1)
    print(c.cartesian())
    print(c.polar())
    print("Degrees:", c.polar().phi.degrees)
