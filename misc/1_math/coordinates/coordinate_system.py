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
        x, y = self.attr_names
        return f"{self.__class__.__name__}<({x}={self._xx}, {y}={self._yy})>"


class Cartesian2D(CoordinatesBase):
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

    def create_cartesian(self) -> "Cartesian2D":
        return Cartesian2D(*self.__convert_to_cart())

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


class Coordinates3DBase(CoordinatesBase):
    attr_names = "", "", ""

    def __init__(self, x: float | int, y: float | int, z: float | int):
        self.set(x, y, z)

    def set(self, x: float | int, y: float | int, z: float | int):
        self._xx, self._yy, self._zz = Coordinate(x), Coordinate(y), Coordinate(z)

    def get(self) -> (Coordinate, Coordinate, Coordinate):
        return self._xx, self._yy, self._zz

    def __str__(self):
        x, y, z = self.attr_names
        return f"{self.__class__.__name__}<({x}={self._xx}, {y}={self._yy}, {z}={self._zz})>"


class Cartesian3D(Coordinates3DBase):
    attr_names = "x", "y", "z"

    def __convert_to_spherical(self) -> (float, float, float):
        x, y, z = self._xx, self._yy, self._zz
        return math.sqrt(x*x + y*y + z*z), math.atan(math.sqrt(x*x + y*y) / z), math.atan2(y, x)

    def create_spherical(self) -> "Spherical":
        return Spherical(*self.__convert_to_spherical())

    def __convert_to_cylindrical(self) -> (float, float, float):
        x, y, z = self._xx, self._yy, self._zz
        return math.sqrt(x*x + y*y), math.atan2(y, x), z

    def create_cylindrical(self) -> "Cylindrical":
        return Cylindrical(*self.__convert_to_cylindrical())

    @property
    def x(self) -> Coordinate:
        return self._xx

    @property
    def y(self) -> Coordinate:
        return self._yy

    @property
    def z(self) -> Coordinate:
        return self._zz


class Spherical(Coordinates3DBase):
    attr_names = "rho", "theta", "phi"

    def set(self, x: float | int, y: float | int, z: float | int):
        self._xx, self._yy, self._zz = Coordinate(x), Phi(y), Phi(z)

    def __convert_to_cartesian3d(self) -> (float, float, float):
        rho, theta, phi = self._xx, self._yy, self._zz
        return rho * math.sin(theta) * math.cos(phi), rho * math.sin(theta) * math.sin(phi), rho * math.cos(theta)

    def create_cartesian3d(self) -> "Cartesian3D":
        return Cartesian3D(*self.__convert_to_cartesian3d())

    def __convert_to_cylindrical(self) -> (float, float, float):
        rho, theta, phi = self._xx, self._yy, self._zz
        return rho * math.sin(theta), theta, rho * math.cos(theta)

    def create_cylindrical(self) -> "Cylindrical":
        return Cylindrical(*self.__convert_to_cylindrical())

    @property
    def rho(self) -> Coordinate:
        return self._xx

    @property
    def theta(self) -> Phi:
        return self._yy

    @property
    def phi(self) -> Phi:
        return self._zz


class Cylindrical(Coordinates3DBase):
    attr_names = "rho", "phi", "z"

    def set(self, x: float | int, y: float | int, z: float | int):
        self._xx, self._yy, self._zz = Coordinate(x), Phi(y), Coordinate(z)

    def __convert_to_cartesian3d(self) -> (float, float, float):
        rho, phi, z = self._xx, self._yy, self._zz
        return rho * math.cos(phi), rho * math.sin(phi), z

    def create_cartesian3d(self) -> "Cartesian3D":
        return Cartesian3D(*self.__convert_to_cartesian3d())

    def __convert_to_spherical(self) -> (float, float, float):
        rho, phi, z = self._xx, self._yy, self._zz
        return math.sqrt(rho*rho + z*z), phi, math.atan2(z, rho)

    def create_spherical(self) -> "Spherical":
        return Spherical(*self.__convert_to_spherical())

    @property
    def rho(self) -> Coordinate:
        return self._xx

    @property
    def phi(self) -> Phi:
        return self._yy

    @property
    def z(self) -> Coordinate:
        return self._zz



if __name__ == '__main__':
    p = Cartesian2D(2, 3).create_polar()
    c = p.create_cartesian()
    print("Radius:", p.rho)
    print("Degrees:", p.phi.degrees)

    c3d = Cartesian3D(2, 3, 1)
    print(c3d.create_cylindrical())
    print(c3d.create_spherical())
    print(c3d.create_spherical())

