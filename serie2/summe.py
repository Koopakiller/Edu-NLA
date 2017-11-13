from __future__ import print_function
from decimal import *
import time

class Sum:

    def __init__(self):
        pass

    def sum_indices(self, addends):
        result = 0
        for addend in addends:
            result += addend
        return result

    def sum_ordered(self, addends):
        result = 0
        for addend in sorted(addends):
            result += addend
        return result

    def sum_ordered_grouped_by_sign(self, addends):
        pos = 0
        neg = 0
        for addend in sorted(addends):
            if addend > 0:
                pos += addend
            if addend < 0:
                neg += addend
        return pos + neg


def get_harmonic_series_addends(k):
    result = []
    for i in range(1, k + 1):
        result.append(Decimal(1) / Decimal(i))
    return result


def factorial(k):
    result = Decimal(1)
    for i in range(2, k + 1):
        result *= k
    return result


def get_e_taylor_series_addends(x, k):
    result = []
    for i in range(1, k + 1):
        result.append((x ** Decimal(i)) / factorial(i))
    return result


def get_e_taylor_series_2_addends(x, k):
    result = []
    for i in range(1, k + 1):
        result.append((1 if i % 2 == 0 else -1)
                      * (x ** i)
                      / factorial(i))
    return result


def main():

    s = Sum()
    k_set = map(lambda y: 2**y, range(1, 21))

    print("Partial sum of harmonic series")

    for k in k_set:
        start = time.clock()
        addends = get_harmonic_series_addends(Decimal(k))
        print("k = " + str(k))
        r1 = s.sum_indices(addends)
        print("   added by indices: " + str(r1))
        r2 = s.sum_ordered(addends)
        print("   added by size:    " + str(r2))
        print(" > elapsed time: " + str(time.clock() - start) + "s")
        print()

    print()
    print("==================================================================")
    print()

    k_set = map(lambda y: 2**y, range(1, 13))

    print("First Taylor series to approximate e^x")

    for x in [-20, -1, 1, 20]:
        for k in k_set:
            start = time.clock()
            addends = get_e_taylor_series_addends(Decimal(x), Decimal(k))
            print("x = " + str(x) + ", k = " + str(k))
            r1 = s.sum_indices(addends)
            print("   added by indices: " + str(r1))
            r2 = s.sum_ordered(addends)
            print("   added by size:    " + str(r2))
            r3 = s.sum_ordered_grouped_by_sign(addends)
            print("   added by sign:    " + str(r3))
            print(" > elapsed time: " + str(time.clock() - start) + "s")
            print()
        print()

    print()
    print("==================================================================")
    print()

    print("Second Taylor series to approximate e^x")

    for x in [-20, -1, 1, 20]:
        for k in k_set:
            start = time.clock()
            addends = get_e_taylor_series_2_addends(Decimal(x), Decimal(k))
            print("x = " + str(x) + ", k = " + str(k))
            r1 = s.sum_indices(addends)
            print("   added by indices: " + str(r1))
            r2 = s.sum_ordered(addends)
            print("   added by size:    " + str(r2))
            r3 = s.sum_ordered_grouped_by_sign(addends)
            print("   added by sign:    " + str(r3))
            print(" > elapsed time: " + str(time.clock() - start) + "s")
            print()
        print()



if __name__ == "__main__":
    main()
