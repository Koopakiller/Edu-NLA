import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy


def plot(parameter_list, data_points_list):
    x = numpy.arange(0, 6, 0.01)
    plt.plot(map(lambda t: t[4], parameter_list), map(lambda t: t[6], parameter_list), "ro")

    plt.legend()

    plt.xlabel("k")
    plt.ylabel("norm(r)")

    plt.show()
