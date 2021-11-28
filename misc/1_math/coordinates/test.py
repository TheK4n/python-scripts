import unittest
from .azimuth import *


class MyTestCase(unittest.TestCase):
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

    def test_phi2az(self):
        self.assertEqual(phi2az(0), 90)
        self.assertEqual(phi2az(45), 45)
        self.assertEqual(phi2az(90), 0)
        self.assertEqual(phi2az(91), 359)
        self.assertEqual(phi2az(135), 315)
        self.assertEqual(phi2az(180), 270)
        self.assertEqual(phi2az(-180), 270)
        self.assertEqual(phi2az(-135), 225)
        self.assertEqual(phi2az(-91), 181)
        self.assertEqual(phi2az(-90), 180)
        self.assertEqual(phi2az(-45), 135)


if __name__ == '__main__':
    unittest.main()
