from fraction import Fraction
from prime_tests import test_prime
from fraction_tests import test_fraction
from pprint import pprint


class Bruch(Fraction):

    def __init__(self, zaehler, nenner):
        Fraction.__init__(zaehler, nenner)


def run_test(class_name, fx):
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
    print("The implemented unit tests will be executed.")
    print
    run_test("Fraction", test_fraction)
    print
    run_test("Prime", test_prime)
    print
    print("All tests run.")


if __name__ == "__main__":
    main()
