from prime import Prime


class Bruch:
    def __init__(self, zaehler, nenner):
        self.numerator = zaehler
        self.denominator = nenner
        self.reduce()

    # Reduce and Clone this object

    def reduce(self):
        q = Prime.get_greatest_common_divisor(self.numerator, self.denominator)
        self.numerator = self.numerator / q
        self.denominator = self.denominator / q

    def clone(self):
        return Bruch(self.numerator, self.denominator)

    # Calculation Operators

    def __add__(self, other):
        if isinstance(other, Bruch):
            return Bruch(self.numerator * other.denominator + other.numerator * self.denominator,
                         self.denominator * other.denominator)
        if isinstance(other, int) or isinstance(other, long):
            return self.__add__(Bruch(other, 1))
        raise TypeError()

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        if isinstance(other, Bruch):
            return Bruch(self.numerator * other.numerator, self.denominator * other.denominator)
        if isinstance(other, int) or isinstance(other, long):
            return self.__mul__(Bruch(other, 1))
        raise TypeError()

    def __div__(self, other):
        if isinstance(other, Bruch):
            return self.__mul__(Bruch(other.denominator, other.numerator))
        if isinstance(other, int) or isinstance(other, long):
            return self.__div__(Bruch(1, other))
        raise TypeError()

    def __neg__(self):
        return Bruch(-self.numerator, self.denominator)

    # Equality Operators

    def __eq__(self, other):
        if isinstance(other, float):
            return self.__float__() == other
        if isinstance(other, int) or isinstance(other, long):
            other = Bruch(other, 1)
        if not isinstance(other, Bruch):
            raise ValueError()

        a = self - other
        return a.numerator == 0 and a.denominator != 0

    def __cmp__(self, other):
        return self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, float):
            return self.__float__() < other
        if isinstance(other, int) or isinstance(other, long):
            other = Bruch(other, 1)
        if not isinstance(other, Bruch):
            raise ValueError()

        return self.numerator * other.denominator < other.denominator * self.denominator

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    # Type conversation

    def __str__(self):
        if self.numerator == 0:
            return "0"
        if self.denominator == 0:
            return "NaN"
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + " / " + str(self.denominator)

    def __float__(self):
        return float(self.numerator) / float(self.denominator)
