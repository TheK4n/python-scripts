import unittest
from azimuth import az2clock, clock2az
from coordinate_system import Cartesian2D, Polar


class TestClock(unittest.TestCase):
    def test_hours(self):
        self.assertEqual(az2clock(0), 12)
        self.assertEqual(az2clock(360), 12)
        self.assertEqual(az2clock(180), 6)
        self.assertEqual(az2clock(90), 3)
        self.assertEqual(az2clock(270), 9)

    def test_hours2(self):
        self.assertEqual(clock2az(12), 0)
        self.assertEqual(clock2az(1), 30)
        self.assertEqual(clock2az(6), 180)
        self.assertEqual(clock2az(3), 90)
        self.assertEqual(clock2az(9), 270)


class TestCoordinateSystem2D(unittest.TestCase):
    def setUp(self) -> None:
        self.cartesian = Cartesian2D(2, 3)
        self.polar = Polar(2, 3)

        self.cart2polar = self.polar.from_cartesian(self.cartesian)
        self.pol2cart_values = self.cartesian.from_polar(self.polar)

    def testEquals(self):
        self.assertEqual(self.cartesian.from_polar(self.polar.from_cartesian(self.cartesian)), (2, 3))


if __name__ == '__main__':
    unittest.main()
