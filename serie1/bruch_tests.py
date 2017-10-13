# Author: Tom Lambert
# Content: UnitTests for Sum-class

import unittest

from bruch import Bruch


class BruchTests(unittest.TestCase):

    a = Bruch(1, 2)
    a2 = Bruch(5, 10)
    b = Bruch(2, 1)
    c = Bruch(2*3, 3*5)
    d = Bruch(2*7, 7*5)

    def test_init(self):
        x = Bruch(2, 4)
        self.assertEqual(x.numerator, 1)
        self.assertEqual(x.denominator, 2)

    def test_operator_eq(self):
        self.assertEqual(self.a == self.a, True)
        self.assertEqual(self.a == self.b, False)
        self.assertEqual(self.a == self.a2, True)
        self.assertEqual(Bruch(0, 3) == Bruch(0, 1), True)
        self.assertEqual(self.a != self.a, False)
        self.assertEqual(self.a != self.b, True)
        self.assertEqual(self.a != self.a2, False)
        self.assertEqual(self.a, 0.5)
        self.assertEqual(self.b, 2)

        self.assertFalse(self.a < 0.4)
        self.assertFalse(self.a < 0.5)
        self.assertTrue(self.a <= 0.5)
        self.assertTrue(self.a <= 0.6)
        self.assertFalse(self.b <= 1)
        self.assertTrue(self.b <= 2)
        self.assertTrue(self.a <= 3)
        self.assertTrue(Bruch(1, -2) < Bruch(1, 2))

        self.assertTrue(self.a > 0)
        self.assertFalse(self.a > 0.5)
        self.assertTrue(self.a >= 0.5)
        self.assertFalse(self.a >= 0.6)
        self.assertTrue(self.b >= 1)
        self.assertTrue(self.b >= 2)
        self.assertFalse(self.a >= 3)
        self.assertTrue(Bruch(-1, -2) > Bruch(-1, 2))

    def test_operator_basic_ops(self):
        self.assertEqual(self.a * self.b, Bruch(1, 1))
        self.assertEqual(self.c * self.d, Bruch(2*3*2*7, 3*5*5*7))
        self.assertEqual(self.c / self.d, Bruch(2*3*5*7, 3*5*2*7))
        self.assertEqual(self.c + self.d, Bruch(2*3*7*5 + 3*5*2*7, 3*5*7*5))
        self.assertEqual(self.c - self.d, Bruch(2*3*7*5 - 3*5*2*7, 3*5*7*5))
        self.assertEqual(-self.a, Bruch(-1, 2))
        self.assertEqual(-self.a, Bruch(1, -2))
        self.assertEqual(self.a + 1, Bruch(3, 2))
        self.assertEqual(1 + self.a, Bruch(3, 2))
        self.assertEqual(self.a * 3, Bruch(3, 2))
        self.assertEqual(3 * self.a, Bruch(3, 2))
        self.assertEqual(1/self.a, self.b)
        self.assertEqual(self.a / 4, Bruch(1, 8))
        self.assertEqual(self.a - 1, Bruch(-1, 2))
        self.assertEqual(1 - self.a, self.a)

    def test_str(self):
        self.assertEqual(str(self.a), "1 / 2")
        self.assertEqual(str(self.a2), "1 / 2")
        self.assertEqual(str(self.c), "2 / 5")
        self.assertEqual(str(self.b), "2")
        self.assertEqual(str(Bruch(0, 1)), "0")
        self.assertEqual(str(Bruch(1, 0)), "NaN")

    def test_float(self):
        self.assertEqual(float(self.a), 0.5)

if __name__ == '__main__':
    unittest.main()
