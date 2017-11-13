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

    def sum_ordered_ascendends(self, addends):
        result = 0
        for addend in sorted(addends):
            result += addend
        return result


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

    print("Partial sum of harmonic series")

    for k in map(lambda x: 2**x, range(1, 20)):
        start = time.clock()
        addends = get_harmonic_series_addends(Decimal(k))
        print("k = " + str(k))
        r1 = s.sum_indices(addends)
        print("   added by indices: " + str(r1))
        r2 = s.sum_ordered_ascendends(addends)
        print("   added by size:    " + str(r2))
        print(" > elapsed time: " + str(time.clock() - start) + "s")

    print()
    print("==================================================================")
    print()



if __name__ == "__main__":
    main()
