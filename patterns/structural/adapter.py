import math


class RoundHole:

    def __init__(self, radius: int):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg: "RoundPeg"):
        if not isinstance(peg, RoundPeg):
            raise ValueError("Wrong peg!")
        return peg.get_radius() < self.get_radius()


class RoundPeg:
    def __init__(self, radius: float):
        self.radius = radius

    def get_radius(self):
        return self.radius


class SquarePeg:

    def __init__(self, width: float):
        self.width = width

    def get_width(self):
        return self.width


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: "SquarePeg"):
        self.peg = peg

    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2) / 2


if __name__ == '__main__':
    hole = RoundHole(5)
    rpeg = RoundPeg(5)
    hole.fits(rpeg)

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    try:
        hole.fits(small_sqpeg)
    except ValueError as e:
        print(repr(e))

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
    assert hole.fits(small_sqpeg_adapter)
    assert not hole.fits(large_sqpeg_adapter)
