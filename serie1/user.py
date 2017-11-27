import fraction
import decimal

def start():
    a = int(raw_input("Pleae enter two fractions. They may be improper. First, enter the numerator of the first fraction. "))
    b = int(raw_input("Next, enter the denominator of the second fraction."))
    c = int(raw_input("Next, enter the numerator of the second fraction."))
    d = int(raw_input("Lastly, enter the denominator of the second fraction."))
    x = fraction.Fraction(a, b)
    y = fraction.Fraction(c, d)
    print str(a) + "/" + str(b) + "+" + str(c) + "/" + str(d) + "=" + str(fraction.add(x,y))


start()
