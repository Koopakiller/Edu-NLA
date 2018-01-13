import matrix
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy


def plot():
    n = 5
    h = 1.0 / n

    r = numpy.arange(0, 3, 0.01)
    plt.plot(r, numpy.sin(r), "-")

    m = matrix.Matrix("saite", n, "float64")
    b = numpy.array([1*h*h, 2*h*h, 3*h*h, 4*h*h, 5*h*h])
    x = m.solve(b)

    plt.plot(b, x, "ro")

    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
