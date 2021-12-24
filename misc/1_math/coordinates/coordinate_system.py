import math


class Coord(float):
    def __str__(self):
        return str(round(self, 3))


class Phi(Coord):

    def __init__(self, value: int | float):
        self.__phi = Coord(value)

    @property
    def degrees(self) -> float:
        return Coord(math.degrees(self.__phi) % 360)


class Coordinates:

    def __init__(self, x: float | int, y: float | int, is_polar=False, to_round=3):

        if is_polar is None:
            raise TypeError("Attribute 'is_polar' can`t be NoneType")
        self.set(x, y, is_polar)
        self.__to_round = to_round

    def set(self, x: float | int, y: float | int, is_polar=None):

        self.__is_polar = is_polar if is_polar is not None else self.__is_polar

        if self.__is_polar:
            self.__rho = Coord(x)
            self.__phi = Phi(y)
        else:
            self.__x = Coord(x)
            self.__y = Coord(y)

    def get(self) -> (Coord, Coord):
        """
        (x, y)
        (rho, phi(rad))
        """
        if self.__is_polar:
            return tuple(map(self.__round(self.__rho, self.__phi)))
        return self.__x, self.__y

    def __cart2pol(self, x: float, y: float) -> (float, float):
        phi = math.atan2(y, x)
        phi = math.pi * 2 + phi if phi < 0 else phi
        return math.sqrt(x * x + y * y), phi

    def __pol2cart(self, rho: float, phi: float) -> (float, float):
        return rho * math.cos(phi), rho * math.sin(phi)

    def create_polar(self) -> "Coordinates":
        if not self.__is_polar:
            return self.__class__(*self.__cart2pol(self.__x, self.__y), is_polar=True)
        return self

    def create_cartesian(self) -> "Coordinates":
        if self.__is_polar:
            return self.__class__(*self.__pol2cart(self.__rho, self.__phi))
        return self

    def __str__(self):
        if self.__is_polar:
            return f"{self.__class__.__name__}<(rho={self.__rho}, phi={self.__phi})>"
        return f"{self.__class__.__name__}<(x={self.__x}, y={self.__y})>"

    def __raise_attribute_error(self, attr: str):
        status = "polar" if self.__is_polar else "cartesian"
        msg = f"'{self.__class__.__name__} object has no attribute '{attr}'. Seems it in {status} system"
        raise AttributeError(msg)

    @property
    def x(self) -> float:
        if not self.__is_polar:
            return self.__x
        self.__raise_attribute_error("x")

    @property
    def y(self) -> float:
        if not self.__is_polar:
            return self.__y
        self.__raise_attribute_error("y")

    @property
    def rho(self) -> float:
        if self.__is_polar:
            return self.__rho
        self.__raise_attribute_error("rho")

    @property
    def phi(self) -> Phi:
        if self.__is_polar:
            return self.__phi
        self.__raise_attribute_error("phi")


if __name__ == '__main__':
    c = Coordinates(2, 3).create_polar()
    print("Radius:", c.rho)
    print("Degrees:", c.phi.degrees)

