from fraction import Fraction
import Console


def print_operation(a, operator, b, result):
    str_a = "({0})" if isinstance(a, Fraction) else "{0}"
    str_b = "({2})" if isinstance(b, Fraction) else "{2}"
    print(("( " + str_a + " {1} " + str_b + " ) = {3}").format(a, operator, b, result))


def main():
    show_comparison = True
    show_basic_ops = True

    if Console.read_yesno("Is the first operand a fraction? [Y/n] ", default_input=True):
        x1 = Console.read_integer("Please enter the numerator of the first fraction: ")
        x2 = Console.read_integer("Next, enter the denominator of the first fraction: ")
        a = Fraction(x1, x2)
    else:
        a = Console.read_float("Please enter a float or integer value: ")
        if long(a) != a:
            show_basic_ops = False
        else:
            a = long(a)

    if Console.read_yesno("Is the second operand a fraction? [Y/n] ", default_input=True):
        x1 = Console.read_integer("Please enter the numerator of the second fraction: ")
        x2 = Console.read_integer("Lastly, enter the denominator of the second fraction: ")
        b = Fraction(x1, x2)
    else:
        b = Console.read_float("Please enter a float or integer value: ")
        if long(b) != b:
            show_basic_ops = False
        else:
            b = long(b)

    print("")
    if not isinstance(a, Fraction) and not isinstance(b, Fraction):
        print("Neither the first nor the second operator is a fraction...")

    if show_basic_ops:
        print_operation(a, " +", b, a + b)
        print_operation(a, " -", b, a - b)
        print_operation(a, " *", b, a * b)
        print_operation(a, " /", b, a / b)

    if show_comparison:
        print_operation(a, " <", b, a < b)
        print_operation(a, " >", b, a > b)
        print_operation(a, "==", b, a == b)
        print_operation(a, "<=", b, a <= b)
        print_operation(a, ">=", b, a >= b)
        print_operation(a, "!=", b, a != b)


if __name__ == "__main__":
    main()
