import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy
import math


def plot(parameter_list, data_points_list):

    #plt.title("a={0}; b={1}; c={2}; d={3}".format(a, b, c, d))

    e = math.e

    x = numpy.arange(0, 25, 0.01)
    for entry in parameter_list:
        a, b, c, d = entry
        plt.plot(x, a * (e ** (d*x)) + b * (e ** (-d * x)) + c, "-")

    plt.plot(map(lambda pair: pair[0], data_points_list), map(lambda pair: pair[1], data_points_list), "ro")

    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()
