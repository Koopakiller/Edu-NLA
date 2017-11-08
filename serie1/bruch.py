# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


from __future__ import print_function
from pprint import pprint

from fraction_tests import test_fraction
from prime_tests import test_prime
from fraction import Fraction


class Bruch(Fraction):
    """A derivative of the Fraction-class without other implementations.
    For UnitTests see FractionTests.
    """

    def __init__(self, zaehler, nenner):
        """Initializes a  new instance.

        :param zaehler: The numerator of the instance to crate.
        :param nenner: The denominator of the instance to create.
        """
        Fraction.__init__(zaehler, nenner)


def run_test(class_name, fx):
    """Runs a given unit-test and prints the result.

    :param class_name: The class name which will be tested. It will be printed ith the results.
    :param fx: The test-function to execute.
    :return: A result-object with the result of the tests.
    """
    print("Testing " + class_name + " class:")
    r = fx()
    print("Number of run tests: " + str(r.testsRun))
    if len(r.errors) > 0:
        print("Errors :")
        print(r.errors)
    else:
        print("No errors occurred.")
    if len(r.failures) > 0:
        print("Failures :")
        pprint(r.failures)
    else:
        print("No failures occurred.")


def main():
    """The main program. It runs unittests to test the main-modules."""
    print("The implemented unit tests will be executed.")
    print
    run_test("Fraction", test_fraction)
    print
    run_test("Prime", test_prime)
    print
    print("All tests run.")


if __name__ == "__main__":
    main()
