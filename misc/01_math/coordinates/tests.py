import unittest
from azimuth import az2clock, clock2az
from coordinate_system import Cylindrical, Spherical, Cartesian3D, Cartesian2D, Polar


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

        self.cart2polar_values = self.cartesian.create_polar().get()
        self.pol2cart_values = self.polar.create_cartesian().get()

    def testInstance(self):
        self.assertIsInstance(self.cartesian.create_polar(), Polar)
        self.assertIsInstance(self.polar.create_cartesian(), Cartesian2D)

    def testEquals(self):
        self.assertEqual(self.cartesian.create_polar().get(), (2, 3))


if __name__ == '__main__':
    unittest.main()
