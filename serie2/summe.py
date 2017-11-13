import numpy


class Sum:

    def __init__(self):
        pass

    def sum_indices(self, addends):
        result = 0
        for value in addends:
            result += value
        return result

    def sum_ordered_ascendends(self, addends):
        result = 0
        for value in sorted(addends):
            result += value
        return result


def get_harmonic_series_addends(k):
    result = []
    for i in range(1, k + 1):
        result.append(1 / k)
    return result


def get_e_taylor_series_addends(x, k):
    result = []
    for i in range(1, k + 1):
        result.append(numpy.power(x, i) / numpy.math.factorial(i))
    return result


def get_e_taylor_series_2_addends(x, k):
    result = []
    for i in range(1, k + 1):
        result.append((1 if i % 2 == 0 else -1)
                      * numpy.power(x, i)
                      / numpy.math.factorial(i))
    return result


def main():

    sum = Sum()

    print("Partial sum of harmonic series")

    for k in map(lambda x: 2**x, range(1, 20)):
        addends = get_harmonic_series_addends(k)
        print("k = " + str(k))
        r1 = sum.sum_indices(addends)
        print("  added by indices: " + str(r1))
        r2 = sum.sum_ordered_ascendends(addends)
        print("  added by size:    " + str(r2))

    pass


if __name__ == "__main__":
    main()
