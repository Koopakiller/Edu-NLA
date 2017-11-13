import numpy


class Sum:

    def __init__(self):
        pass

    def sum_indices(self, values):
        result = 0
        for value in values:
            result += value
        return result

    def sum_ordered_ascendends(self, values):
        result = 0
        for value in sorted(values):
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
    pass


if __name__ == "__main__":
    main()
