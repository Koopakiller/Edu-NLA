# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import numpy
from prime import Prime


class Fraction:
    """Represents a fraction with two integers."""

    def __init__(self, numerator, denominator):
        """Initializes a new Fraction-Instance with a value.

        :param numerator: The numerator in the instance to created.
        :param denominator: The denominator in the instance to create.
        """
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    # Reduce and Clone this object

    def reduce(self):
        """Reduces the fraction by removing all common prime factors."""
        if self.denominator == 0:
            self.numerator = 1
        else:
            q = Prime.get_greatest_common_divisor(self.numerator, self.denominator)
            self.numerator = self.numerator / q
            self.denominator = self.denominator / q

    def clone(self):
        """Creates a copy of this instance.

        :return: A new instance with the same value as this fraction.
        """
        return Fraction(self.numerator, self.denominator)

    # Calculation Operators

    def __add__(self, other):
        """Adds an integer or another fraction to this instance and returns the result.

        :param other: The other value to add; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the addition.
        """
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        if isinstance(other, int) or isinstance(other, long):
            return self.__add__(Fraction(other, 1))
        raise TypeError()

    def __radd__(self, other):
        """Adds an integer or another fraction to this instance and returns the result.

        :param other: The other value to add; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the addition.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Subtracts an integer or another fraction from this instance and returns the result.

        :param other: The other value to subtract; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the subtraction.
        """
        return self.__add__(-other)

    def __rsub__(self, other):
        """Subtracts this instance from an integer or another fraction and returns the result.

        :param other: The other value to subtract from; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the subtraction.
        """
        return -self + other

    def __mul__(self, other):
        """Multiplies an integer or another fraction with this instance and returns the result.

        :param other: The other value to multiply with; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the multiplication.
        """
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        if isinstance(other, int) or isinstance(other, long):
            return self.__mul__(Fraction(other, 1))
        raise TypeError()

    def __rmul__(self, other):
        """Multiplies an integer or another fraction with this instance and returns the result.

        :param other: The other value to multiply with; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the multiplication.
        """
        return self.__mul__(other)

    def __div__(self, other):
        """Divides this instance by an integer or another fraction and returns the result.

        :param other: The other value to divide with; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the division.
        """
        if isinstance(other, Fraction):
            return self.__mul__(Fraction(other.denominator, other.numerator))
        if isinstance(other, int) or isinstance(other, long):
            return self.__div__(Fraction(other, 1))
        raise TypeError()

    def __rdiv__(self, other):
        """Divides an integer or another fraction with this instance and returns the result.

        :param other: The other value to divide; it can be a Fraction, int or long.
        :return: A new Fraction instance with the result of the division.
        """
        if isinstance(other, Fraction):
            return other.__mul__(Fraction(self.denominator, self.numerator))
        if isinstance(other, int) or isinstance(other, long):
            return Fraction(other, 1).__div__(self)
        raise TypeError()

    def __neg__(self):
        """Negates the value of this instance and returns it.

        :return: A new Fraction instance with the negated value of this instance
        """
        return Fraction(-self.numerator, self.denominator)

    # Equality Operators

    def __eq__(self, other):
        """Compares this Fraction with another Fraction, float, int or long for value-equality.

        :param other: The other value to compare with; it can be another Fraction, float, int or long
        :return: True, if the values are equal; otherwise False.
        """
        if isinstance(other, float):
            return self.__float__() == other
        if isinstance(other, int) or isinstance(other, long):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise ValueError()

        a = self - other
        return a.numerator == 0 and a.denominator != 0

    def __ne__(self, other):
        """Compares this Fraction with another Fraction, float, int or long for value-inequality.

        :param other: The other value to compare with; it can be another Fraction, float, int or long
        :return: False, if the values are equal; otherwise True.
        """
        return not self.__eq__(other) and self.denominator != 0 and (not isinstance(other, Fraction) or other.denominator != 0)

    def __lt__(self, other):
        """Checks if the value of this instance is less then another value.

        :param other: The other value to compare with; it can be another Fraction float, int or long
        :return: True if this instances value is less then the other value; otherwise False.
        """
        if isinstance(other, float):
            return self.__float__() < other
        if isinstance(other, int) or isinstance(other, long):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise ValueError()

        return self.numerator * numpy.abs(other.denominator) * numpy.sign(self.denominator) \
               < other.numerator * numpy.abs(self.denominator) * numpy.sign(other.denominator)

    def __le__(self, other):
        """Checks if the value of this instance is less or equal than another value.

        :param other: The other value to compare with; it can be another Fraction float, int or long
        :return: True if this instances value is less or equal then the other value; otherwise False.
        """
        return (self.__lt__(other) or self.__eq__(other)) and self.denominator != 0 and (not isinstance(other, Fraction) or other.denominator != 0)

    def __gt__(self, other):
        """Checks if the value of this instance is greater than another value.

        :param other: The other value to compare with; it can be another Fraction float, int or long
        :return: True if this instances value is greater then the other value; otherwise False.
        """
        return not self.__le__(other) and self.denominator != 0 and (not isinstance(other, Fraction) or other.denominator != 0)

    def __ge__(self, other):
        """Checks if the value of this instance is greater or equal than another value.

        :param other: The other value to compare with; it can be another Fraction float, int or long
        :return: True if this instances value is greater or equal then the other value; otherwise False.
        """
        return not self.__lt__(other) and self.denominator != 0 and (not isinstance(other, Fraction) or other.denominator != 0)

    # Type conversation

    def __str__(self):
        """Creates a string representation for this instance.

        :return: * "NaN" if the denominator is 0;
                 * "0" if the denominator is 0;
                 * the numerator-value as a string if the denominator is 1;
                 * otherwise "numerator / denominator"
        """
        if self.numerator == 0:
            return "0"
        if self.denominator == 0:
            return "NaN"
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + " / " + str(self.denominator)

    def __float__(self):
        """Converts the value of this instance into a float-value. The result must not be exact.

        :return: A approximated float-value of this instances value.
        """
        return float(self.numerator) / float(self.denominator)
