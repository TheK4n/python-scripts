import math
from typing import NamedTuple


class Cartesian2D(NamedTuple):
    x: float
    y: float

    @classmethod
    def from_polar(cls, p: "Polar") -> "Cartesian2D":
        x = p.rho * math.cos(p.theta)
        y = p.rho * math.sin(p.theta)
        return cls(x, y)


class Polar(NamedTuple):
    rho: float
    theta: float

    @classmethod
    def from_cartesian(cls, c: Cartesian2D) -> "Polar":
        theta = math.atan2(c.y, c.x)
        theta = math.pi * 2 + theta if theta < 0 else theta
        rho, theta = math.sqrt(c.x * c.x + c.y * c.y), theta
        return cls(rho, theta)


class Cartesian3D(NamedTuple):
    x: float
    y: float
    z: float

    @classmethod
    def from_spherical(cls, s: "Spherical") -> "Cartesian3D":
        x = s.rho * math.sin(s.theta) * math.cos(s.phi)
        y = s.rho * math.sin(s.theta) * math.sin(s.phi)
        z = s.rho * math.cos(s.theta)
        return cls(x, y, z)

    @classmethod
    def from_cylindrical(cls, cy: "Cylindrical") -> "Cartesian3D":
        x = cy.rho * math.cos(cy.phi)
        y = cy.rho * math.sin(cy.phi)
        z = cy.z
        return cls(x, y, z)


class Spherical(NamedTuple):
    rho: float
    theta: float
    phi: float

    @classmethod
    def from_cartesian(cls, c: Cartesian3D) -> "Spherical":
        rho = math.sqrt(c.x*c.x + c.y*c.y + c.z*c.z)
        theta = math.atan2(c.y, c.x)
        phi = math.atan(math.sqrt(c.x*c.x + c.y*c.y) / c.z)
        return cls(rho, theta, phi)

    @classmethod
    def from_cylindrical(cls, cy: "Cylindrical") -> "Spherical":
        rho = math.sqrt(cy.rho*cy.rho + cy.z*cy.z)
        theta = math.atan2(cy.z, cy.rho)
        phi = cy.phi
        return cls(rho, theta, phi)


class Cylindrical(NamedTuple):
    rho: float
    phi: float
    z: float

    @classmethod
    def from_cartesian(cls, c: Cartesian3D) -> "Cylindrical":
        rho = math.sqrt(c.x*c.x + c.y*c.y)
        phi = math.atan2(c.y, c.x)
        z = c.z
        return cls(rho, phi, z)

    @classmethod
    def from_spherical(cls, s: Spherical) -> "Cylindrical":
        rho = s.rho * math.sin(s.theta)
        phi = s.theta
        z = s.rho * math.cos(s.theta)
        return cls(rho, phi, z)


if __name__ == '__main__':
    c = Cartesian2D(2, 3)
    p = Polar.from_cartesian(c)
    print(p)
    print(Cartesian2D.from_polar(p))

    print()

    c3d = Cartesian3D(2, 3, 1)
    print(c3d)
    print(Cylindrical.from_cartesian(c3d))
    print(Spherical.from_cartesian(c3d))
