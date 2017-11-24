# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


from __future__ import print_function
import time
import numpy as np
import Console as Console
import Sum as Sum


class AddendGenerator:

    def __init__(self, delegate):
        self.delegate = delegate


    def factorial(self, k):
        result = self.delegate(1)
        for i in range(2, k + 1):
            result *= i
        return result


    def get_harmonic_series_addends(self, k):
        result = []
        for i in range(1, k + 1):
            result.append(self.delegate(1) / self.delegate(i))
        return result

    def get_e_taylor_series_1_addends(self, x, k):
        result = []
        for i in range(1, k + 1):
            result.append((self.delegate(x) ** self.delegate(i)) / self.factorial(i))
        return result

    def get_e_taylor_series_2_addends(self, x, k):
        result = []
        for i in range(1, k + 1):
            result.append(self.delegate(1 if i % 2 == 0 else -1)
                          * (self.delegate(x) ** self.delegate(i))
                          / self.delegate(self.factorial(i)))
        return result


def main():

    while True:

        print("This program calculates sums.")
        print(" [0] Exit")
        print(" [1] Calculate partial sum of harmonic series")
        print(" [2] Calculate Taylor series for e^x")

        kind = Console.read_integer_interval("Your Choose: ", "Please input 1 or 2", 0, 2)

        if kind==0:
            return

        print("")
        print("How many addends do you like to sum? You can specify multiple values separated by comma (,)")
        addend_counts = Console.read_integer_list_in_range("", 1, None)

        x_values = []
        if kind == 2:
            print()
            print("Which x in e^x do you want to calculate? You can specify multiple values separated by comma (,)")
            x_values = Console.read_integer_list_in_range("", None, None)

        print()
        print("Which type do you like to use for the calculation? You can specify multiple values separated by comma (,)")
        print(" [1] Numpy.float16")
        print(" [2] Numpy.float32")
        print(" [3] Numpy.float64")
        types = Console.read_integer_list_in_range("", 1, 3)


        Console.print_separator1()


        for type in types:
            delegate = [lambda y: np.float16(y), lambda y: np.float32(y), lambda y: np.float64(y)][type - 1]
            type_name = ["float16", "float32", "float64"][type - 1]

            for addend_count in addend_counts:

                ag = AddendGenerator(delegate)

                if kind==1:
                    print("Type: {0}; Addend Count: {1}".format(type_name, addend_count))

                    start = time.clock()

                    addends = ag.get_harmonic_series_addends(addend_count)
                    r1 = Sum.sum_indices(addends)
                    print("   added by indices: " + str(r1))
                    r2 = Sum.sum_ordered(addends)
                    print("   added by size:    " + str(r2))
                    r3 = Sum.sum_ordered_grouped_by_sign(addends)
                    print("   added by sign:    " + str(r3))

                    print(" > elapsed time: " + str(time.clock() - start) + "s")
                    print()

                if kind==2:
                    for x in x_values:
                        print("Type: {0}; Addend Count: {1}; x = {2}".format(type_name, addend_count, x))

                        start = time.clock()

                        print("Algorithm 1:")
                        addends = ag.get_e_taylor_series_1_addends(x, addend_count)
                        r1 = Sum.sum_indices(addends)
                        print("   added by indices: " + str(r1))
                        r2 = Sum.sum_ordered(addends)
                        print("   added by size:    " + str(r2))
                        r3 = Sum.sum_ordered_grouped_by_sign(addends)
                        print("   added by sign:    " + str(r3))

                        print(" > elapsed time: " + str(time.clock() - start) + "s")
                        print()

                        start = time.clock()

                        print("Algorithm 2:")
                        addends = ag.get_e_taylor_series_2_addends(x, addend_count)
                        r1 = delegate(1) / Sum.sum_indices(addends)
                        print("   added by indices: " + str(r1))
                        r2 = delegate(1) / Sum.sum_ordered(addends)
                        print("   added by size:    " + str(r2))
                        r3 = delegate(1) / Sum.sum_ordered_grouped_by_sign(addends)
                        print("   added by sign:    " + str(r3))

                        print(" > elapsed time: " + str(time.clock() - start) + "s")
                        print()
                    Console.print_separator3()

            Console.print_separator2()

        Console.print_separator1()

if __name__ == "__main__":
    main()
