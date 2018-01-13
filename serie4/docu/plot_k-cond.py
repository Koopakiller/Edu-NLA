import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy
import math


def plot(parameter_list, data_points_list):
    plt.yscale('log', basey=10)

    x = numpy.arange(0, 6, 0.01)
    plt.plot(map(lambda t: t[4], parameter_list), map(lambda t: t[7], parameter_list), "ro", label="cond(A)")
    plt.plot(map(lambda t: t[4], parameter_list), map(lambda t: t[8], parameter_list), "go", label="cond(A^T A)")

    plt.legend()

    plt.xlabel("k")
    plt.ylabel("Kondition")

    plt.show()
