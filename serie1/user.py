from fraction import Fraction
import Console


def print_operation(a, operator, b, result):
    str_a = "({0})" if isinstance(a, Fraction) else "{0}"
    str_b = "({2})" if isinstance(b, Fraction) else "{2}"
    print(("( " + str_a + " {1} " + str_b + " ) = {3}").format(a, operator, b, result))


def print_intro():
    print("This program is the implementation of Series 1. "
          "This program was written to test and use the Fraction class. "
          "A ready-made set of inputs will be processed if the user chooses the appropriate option.")


def get_test_values_from_user():
    if Console.read_yesno("Is the first operand a fraction? [Y/n] ", default_input=True):
        x1 = Console.read_integer("Please enter the numerator of the first fraction: ")
        x2 = Console.read_integer("Next, enter the denominator of the first fraction: ")
        a = Fraction(x1, x2)
    else:
        a = Console.read_float("Please enter a float or integer value: ")
        if long(a) == a:
            a = long(a)

    if Console.read_yesno("Is the second operand a fraction? [Y/n] ", default_input=True):
        x1 = Console.read_integer("Please enter the numerator of the second fraction: ")
        x2 = Console.read_integer("Lastly, enter the denominator of the second fraction: ")
        b = Fraction(x1, x2)
    else:
        b = Console.read_float("Please enter a float or integer value: ")
        if long(b) == b:
            b = long(b)

    return a, b


def main():
    print_intro()
    print("")

    tests = []
    if Console.read_yesno("Do you want to test your own values? [y/N]", default_input=False):
        tests.append(get_test_values_from_user())
    else:
        tests.append((Fraction(1, 2), Fraction(1, 3)))
        tests.append((Fraction(1, 2), Fraction(1, 2)))
        tests.append((Fraction(1, 2), Fraction(0, 1)))
        tests.append((Fraction(1, 0), Fraction(1, 2)))
        tests.append((Fraction(1, 2), Fraction(1, 0)))

        tests.append((Fraction(1, 2), 2))
        tests.append((Fraction(1, 2), 1.5))
        tests.append((2, Fraction(1, 2)))
        tests.append((1.5, Fraction(1, 2)))

    for test in tests:
        a, b = test

        print("")
        print("Test for {2}{0} and {3}{1}".format(a, b,
                                                  "fraction " if isinstance(a, Fraction) else "number ",
                                                  "fraction " if isinstance(b, Fraction) else "number "))

        if not isinstance(a, Fraction) and not isinstance(b, Fraction):
            print("Neither the first nor the second operator is a fraction...")

        if not isinstance(a, float) and not isinstance(b, float):
            print_operation(a, " +", b, a + b)
            print_operation(a, " -", b, a - b)
            print_operation(a, " *", b, a * b)
            print_operation(a, " /", b, a / b)

        print_operation(a, " <", b, a < b)
        print_operation(a, " >", b, a > b)
        print_operation(a, "==", b, a == b)
        print_operation(a, "<=", b, a <= b)
        print_operation(a, ">=", b, a >= b)
        print_operation(a, "!=", b, a != b)


if __name__ == "__main__":
    main()
