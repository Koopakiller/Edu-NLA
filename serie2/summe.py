# coding=utf-8
# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


from __future__ import print_function
import time
import numpy as np
import Console as Console
import Sum as Sum
import warnings


warnings.filterwarnings("ignore")


class AddendGenerator:
    """Provides algorithms to generate addends for series."""

    def __init__(self, delegate):
        """
        Initializes a new instance of this class.

        :param delegate: A function which creates a numeric type to use in the calculation from a given value x.
        """
        self.delegate = delegate

    def factorial(self, k):
        """
        Calculates the factorial of k.

        :param k: An integer or long to calculate its factorial.
        :return: The factorial of Parameter k.
        """
        result = self.delegate(1)
        for i in range(2, k + 1):
            result *= self.delegate(i)
        return result

    def get_harmonic_series_addends(self, k):
        """
        Calculates addends for an harmonic series.

        :param k: The number of addends to generate.
        :return: An array of all generated addends.
        """
        result = []
        for i in range(1, k + 1):
            result.append(self.delegate(1) / self.delegate(i))
        return result

    def get_e_taylor_series_1_addends(self, x, k):
        """
        Calculates addends for a Taylor series to calculate e^x.

        :param x: The x to use to calculate e^x.
        :param k: The number of addends to generate.
        :return: An array of all generated addends.
        """
        result = []
        for i in range(0, k + 1):
            result.append((self.delegate(x) ** self.delegate(i)) / self.factorial(i))
        return result

    def get_e_taylor_series_2_addends(self, x, k):
        """
        Calculates addends for a Taylor series to calculate e^x. The sum of the result-array is the reciprocal of e^x.

        :param x: The x to use to calculate e^x.
        :param k: The number of addends to generate.
        :return: An array of all generated addends.
        """
        result = []
        for i in range(0, k + 1):
            numerator = self.delegate(1 if i % 2 == 0 else -1) * (self.delegate(x) ** self.delegate(i))
            denominator = self.delegate(self.factorial(i))
            result.append(0 if np.isinf(denominator) else (numerator / denominator))
        return result


def main():
    """Executes the main program including user-interaction"""

    while True:

        print("This program calculates sums.")
        print(" [0] Exit")
        print(" [1] Calculate partial sum of harmonic series")
        print(" [2] Calculate Taylor series for e^x")

        kind = Console.read_integer_interval("Please Choose: ", "Please input 1 or 2", 0, 2)

        if kind == 0:
            return

        addend_counts = []
        print("")
        print("How many addends do you like to sum? You can specify multiple values separated by commas (,).")
        if kind == 1:
            print("Press [Enter] to use 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
            addend_counts = Console.read_integer_list_in_range("", 1, None, [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
                                                                             2048, 4096, 8192])
        if kind == 2:
            print("Press [Enter] to use 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
            addend_counts = Console.read_integer_list_in_range("", 1, None, [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
                                                                             2048, 4096, 8192])

        x_values = []
        if kind == 2:
            print()
            print("For which x in e^x do you want to calculate?"
                  "You can specify multiple values separated by commas (,)")
            print("Press [Enter] to use -20,-1,1,20")
            x_values = Console.read_integer_list_in_range("", None, None, [-20, -1, 1, 20])

        print()
        print("Which data type do you like to use for the calculation? You can specify multiple values separated by"
              " commas" "(,)")
        print(" [1] Numpy.float16")
        print(" [2] Numpy.float32")
        print(" [3] Numpy.float64")
        print("Press [Enter] to use all.")
        types = Console.read_integer_list_in_range("", 1, 3, [1, 2, 3])

        Console.print_separator1()

        for type in types:
            delegate = [lambda y: np.float16(y), lambda y: np.float32(y), lambda y: np.float64(y)][type - 1]
            type_name = ["float16", "float32", "float64"][type - 1]

            for addend_count in addend_counts:

                ag = AddendGenerator(delegate)

                if kind == 1:
                    print("Type: {0}; Addend Count: {1}".format(type_name, addend_count))

                    start = time.clock()

                    addends = ag.get_harmonic_series_addends(addend_count)

                    problems = []
                    r1 = Sum.sum_indices(addends, problems)
                    print("   added by indices: " + str(r1) + (" (an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                    problems = []
                    r2 = Sum.sum_ordered(addends, problems)
                    print("   added by size:    " + str(r2) + (" (an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                    problems = []
                    r3 = Sum.sum_ordered_grouped_by_sign(addends, problems)
                    print("   added by sign:    " + str(r3) + (" (an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                    print(" > elapsed time: " + str(time.clock() - start) + "s")
                    print()

                if kind == 2:
                    for x in x_values:
                        print("Type: {0}; Addend Count: {1}; x = {2}".format(type_name, addend_count, x))

                        start = time.clock()

                        print("Algorithm 1:")
                        addends = ag.get_e_taylor_series_1_addends(x, addend_count)

                        problems = []
                        r1 = Sum.sum_indices(addends, problems)
                        print("   added by indices: " + str(r1) + (" (an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                        problems = []
                        r2 = Sum.sum_ordered(addends, problems)
                        print("   added by size:    " + str(r2) + (" (an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                        problems = []
                        r3 = Sum.sum_ordered_grouped_by_sign(addends, problems)
                        print("   added by sign:    " + str(r3) + (" (an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                        print(" > elapsed time: " + str(time.clock() - start) + "s")
                        print()

                        start = time.clock()

                        print("Algorithm 2:")
                        addends = ag.get_e_taylor_series_2_addends(x, addend_count)

                        problems = []
                        s = Sum.sum_indices(addends, problems)
                        r1 = "1 / ±infinity = 0" if np.isinf(s) else str(delegate(1) / s)
                        print("   added by indices: " + r1 + (" ( an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                        problems = []
                        s = Sum.sum_ordered(addends, problems)
                        r2 = "1 / ±infinity = 0" if np.isnan(s) else str(delegate(1) / s)
                        print("   added by size:    " + r2 + (" ( an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                        problems = []
                        s = Sum.sum_ordered_grouped_by_sign(addends, problems)
                        r3 = "1 / ±infinity = 0" if np.isnan(s) else str(delegate(1) / s)
                        print("   added by sign:    " + r3 + (" ( an addend was " + problems[0] + ")" if len(problems) > 0 else ""))

                        print(" > elapsed time: " + str(time.clock() - start) + "s")
                        print()
                    Console.print_separator3()

            Console.print_separator2()

        Console.print_separator1()


if __name__ == "__main__":

    main()
