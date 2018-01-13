import matrix
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy


def plot():
    n = 7
    h = 1.0 / n

    r = numpy.arange(0, 1, 0.01)
    plt.plot(r, numpy.sin(r*2), "-")

    m = matrix.Matrix("saite", n, "float64")
    b = numpy.array([i*h for i in range(0, n)])
    x = m.solve(b)

    plt.plot(b, x / 55, "ro")

    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
