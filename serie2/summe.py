from __future__ import print_function
import time
import numpy as np


# Helper Methods for an unique style

def separator1():
    print()
    print("-----------------------------------------------------------")
    print()


def separator2():
    print()
    print()
    print("===========================================================")
    print()
    print()


# Implementation

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


class TestRunner:

    def __init__(self, delegate):
        self.delegate = delegate

    def get_harmonic_series_addends(self, k):
        result = []
        for i in range(1, k + 1):
            result.append(self.delegate(1) / self.delegate(i))
        return result

    def factorial(self, k):
        result = self.delegate(1)
        for i in range(2, k + 1):
            result *= k
        return result

    def get_e_taylor_series_addends(self, x, k):
        result = []
        for i in range(1, k + 1):
            result.append((x ** self.delegate(i)) / self.factorial(i))
        return result

    def get_e_taylor_series_2_addends(self, x, k):
        result = []
        for i in range(1, k + 1):
            result.append((1 if i % 2 == 0 else -1)
                          * (x ** i)
                          / self.factorial(i))
        return result

    def run_test(self):

        s = Sum()
        k_set = map(lambda y: 2**y, range(1, 21))

        print("Partial sum of harmonic series")
        print()

        for k in k_set:
            start = time.clock()
            addends = self.get_harmonic_series_addends(k)
            print("k = " + str(k))
            r1 = s.sum_indices(addends)
            print("   added by indices: " + str(r1))
            r2 = s.sum_ordered(addends)
            print("   added by size:    " + str(r2))
            print(" > elapsed time: " + str(time.clock() - start) + "s")
            print()

        separator1()

        k_set = map(lambda y: 2**y, range(1, 13))

        print("First Taylor series to approximate e^x")
        print()

        for x in [-20, -1, 1, 20]:
            for k in k_set:
                start = time.clock()
                addends = self.get_e_taylor_series_addends(self.delegate(x), k)
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

        separator1()

        print("Second Taylor series to approximate e^x")
        print()

        for x in [-20, -1, 1, 20]:
            for k in k_set:
                start = time.clock()
                addends = self.get_e_taylor_series_2_addends(self.delegate(x), k)
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


def main():
    print("Test with numpy.float16")
    print()
    runner = TestRunner(lambda x: np.float16(x))
    runner.run_test()

    separator2()

    print("Test with numpy.float32")
    print()
    runner = TestRunner(lambda x: np.float32(x))
    runner.run_test()

    separator2()

    print("Test with numpy.float64")
    print()
    runner = TestRunner(lambda x: np.float64(x))
    runner.run_test()

if __name__ == "__main__":
    main()
