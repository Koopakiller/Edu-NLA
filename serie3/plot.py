import matrix
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy


def plot():
    n = 6
    h = 1.0 / n

    #r = numpy.arange(0, 1, 0.01)
    #plt.plot(r, numpy.sin(r), "-")

    m = matrix.Matrix("saite", n, "float64")
    axis = [float(i) / n for i in range(1, n+1)]
    b = numpy.array([numpy.sin(float(z))/(n**2) for z in axis])
    b[len(b) - 1] = b[len(b) - 1] + numpy.sin(1)
    x = m.solve(b)

    plt.plot(axis, numpy.sin(axis), "-")

    plt.plot(axis, x, "ro-")

    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
