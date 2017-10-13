from fraction import Fraction
from prime_tests import test_prime
from fraction_tests import test_fraction


class Bruch(Fraction):

    def __init__(self, zaehler, nenner):
        Fraction.__init__(zaehler, nenner)


if __name__ == "__main__":
    print("The implemented unit tests will be executed. Only errors will be shown.")

    print("Running tests for prime.py")
    test_prime()
    print("tests finished")

    print("Running tests for prime.py")
    test_fraction()
    print("tests finished")

    print("Execution completed")
