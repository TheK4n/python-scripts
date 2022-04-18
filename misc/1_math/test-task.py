import math


class sum(int):
    def __call__(self, x=0):
        return sum(self + x)


assert sum(5) == 5
assert sum(5)() == 5
assert sum(5)()(2) == 7
assert sum(5)(2) == 7
assert sum(5)(2)(1) == 8
assert sum(5)(100)(-10) == 95

assert 1 + sum(5) == 6
assert sum(5)(2) - 10 == -3
assert 2 * sum(5)(95) == 200
assert math.sin(sum(10)) == -0.5440211108893698

