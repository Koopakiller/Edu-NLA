# Author: Tom Lambert
# Content: UnitTests for Sum-class

import unittest
from StringIO import StringIO
from fraction import Fraction


class FractionTests(unittest.TestCase):
    """Contains Tests for the Fraction-class."""

    a = Fraction(1, 2)
    a2 = Fraction(5, 10)
    b = Fraction(2, 1)
    c = Fraction(2 * 3, 3 * 5)
    d = Fraction(2 * 7, 7 * 5)

    def test_init(self):
        x = Fraction(2, 4)
        self.assertEqual(x.numerator, 1)
        self.assertEqual(x.denominator, 2)

    def test_operator_eq(self):
        self.assertEqual(self.a == self.a, True)
        self.assertEqual(self.a == self.b, False)
        self.assertEqual(self.a == self.a2, True)
        self.assertEqual(Fraction(0, 3) == Fraction(0, 1), True)
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
        self.assertTrue(Fraction(1, -2) < Fraction(1, 2))

        self.assertTrue(self.a > 0)
        self.assertFalse(self.a > 0.5)
        self.assertTrue(self.a >= 0.5)
        self.assertFalse(self.a >= 0.6)
        self.assertTrue(self.b >= 1)
        self.assertTrue(self.b >= 2)
        self.assertFalse(self.a >= 3)
        self.assertTrue(Fraction(-1, -2) > Fraction(-1, 2))

    def test_operator_basic_ops(self):
        self.assertEqual(self.a * self.b, Fraction(1, 1))
        self.assertEqual(self.c * self.d, Fraction(2 * 3 * 2 * 7, 3 * 5 * 5 * 7))
        self.assertEqual(self.c / self.d, Fraction(2 * 3 * 5 * 7, 3 * 5 * 2 * 7))
        self.assertEqual(self.c + self.d, Fraction(2 * 3 * 7 * 5 + 3 * 5 * 2 * 7, 3 * 5 * 7 * 5))
        self.assertEqual(self.c - self.d, Fraction(2 * 3 * 7 * 5 - 3 * 5 * 2 * 7, 3 * 5 * 7 * 5))
        self.assertEqual(-self.a, Fraction(-1, 2))
        self.assertEqual(-self.a, Fraction(1, -2))
        self.assertEqual(self.a + 1, Fraction(3, 2))
        self.assertEqual(1 + self.a, Fraction(3, 2))
        self.assertEqual(self.a * 3, Fraction(3, 2))
        self.assertEqual(3 * self.a, Fraction(3, 2))
        self.assertEqual(1 / self.a, self.b)
        self.assertEqual(self.a / 4, Fraction(1, 8))
        self.assertEqual(self.a - 1, Fraction(-1, 2))
        self.assertEqual(1 - self.a, self.a)

    def test_str(self):
        self.assertEqual(str(self.a), "1 / 2")
        self.assertEqual(str(self.a2), "1 / 2")
        self.assertEqual(str(self.c), "2 / 5")
        self.assertEqual(str(self.b), "2")
        self.assertEqual(str(Fraction(0, 1)), "0")
        self.assertEqual(str(Fraction(1, 0)), "NaN")

    def test_float(self):
        self.assertEqual(float(self.a), 0.5)


def test_fraction():
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(unittest.makeSuite(FractionTests))
    return result
