import math


class Coordinates:

    class Theta(float):
        def __init__(self, phi: float):
            self.__phi = float(phi)

        @property
        def degrees(self) -> float:
            return round(math.degrees(self.__phi), 3)

    def __init__(self, x: float | int, y: float | int, is_polar=False, to_round=3):

        self.__is_polar = is_polar

        if self.__is_polar:
            self.__r = float(x)
            self.__theta = self.Theta(y)
        else:
            self.__x = float(x)
            self.__y = float(y)

        self.__to_round = to_round

    def get(self) -> (float, float):
        """
        (x, y)
        (radius, theta) theta in radians
        """
        if self.__is_polar:
            return self.__r, self.__theta
        else:
            return self.__x, self.__y

    def __get__(self, instance, owner):
        return self.get()

    def __iter__(self):
        return iter(self.get())

    def __getitem__(self, key) -> float:
        return self.get()[key]

    def __cart2pol(self, x: float, y: float) -> (float, float):

        phi = round(math.atan2(y, x), self.__to_round)
        if phi < 0:
            phi = math.pi * 2 + phi
        return round(math.sqrt(x * x + y * y), self.__to_round), round(phi, self.__to_round)

    def __pol2cart(self, rho: float, phi: float) -> (float, float):
        return round(rho * math.cos(phi), self.__to_round), round(rho * math.sin(phi), self.__to_round)

    def polar(self) -> "Coordinates":
        if not self.__is_polar:
            return self.__class__(*self.__cart2pol(self.__x, self.__y), is_polar=True)
        return self

    def cartesian(self) -> "Coordinates":
        if self.__is_polar:
            return self.__class__(*self.__pol2cart(self.__r, self.__theta))
        return self

    def __str__(self):
        if self.__is_polar:
            return f"{self.__class__.__name__}<(r={self.__r}, theta={self.__theta})>"
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
    def theta(self) -> Theta:
        if self.__is_polar:
            return self.__theta


if __name__ == '__main__':
    c = Coordinates(2, 3).polar()
    print(c.get())
    print("Radius:", c.r)
    print("Degrees:", c.theta.degrees)
