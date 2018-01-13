import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy
import math


def plot(parameter_list, data_points_list):
    e = math.e

    x = numpy.arange(0, 25, 0.01)
    for entry in parameter_list:
        a, b, c, d, k, n = entry
        plt.plot(x, a * (e ** (d*x)) + b * (e ** (-d * x)) + c, "-", label="k={0}; n={1}".format(k, n))

    plt.plot(map(lambda pair: pair[0], data_points_list),
             map(lambda pair: pair[1], data_points_list),
             "ro", label="points")

    plt.legend()

    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
