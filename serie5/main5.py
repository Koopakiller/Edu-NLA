import matplotlib
matplotlib.use("TkAgg")

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


import poisson as p


def plot_b(data):
    """Plots the exact- and the SOR solution"""

    for n in data["exact_plot"]:
        h = 1.0/n
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y = np.meshgrid(np.arange(0, 1 + h, h), np.arange(0, 1 + h, h))
        ax.set_xlabel('ih')
        ax.set_ylabel('jh')
        ax.set_zlabel('u(ih, jh)')
        ax.plot_surface(x, y, p.exactu(x, y), color="c")

        plt.title("Exact Plot for n=" + str(n))

        plt.show()

    for n in data["sor_plot"]:
        h = 1.0/n
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y = np.meshgrid(np.arange(0, 1 + h, h), np.arange(0, 1 + h, h))
        ax.set_xlabel('ih')
        ax.set_ylabel('jh')
        ax.set_zlabel('u(ih, jh)')

        a, b = p.lgs(p.rhs, n)
        iterative = p.Iterative(data["omega"], data["eps"])
        l = iterative.diskreteLsgSOR(a, b)

        plot_matrix = np.zeros(((n + 1), (n + 1)))
        for i in range(0, (n - 1)):
            for j in range(0, (n - 1)):
                val = l[i * (n - 1) + j]
                plot_matrix[i + 1, j + 1] = val

        ax.plot_surface(x, y, plot_matrix)

        plt.title("SOR Plot for n=" + str(n))

        plt.show()


def plot_c(data):
    """Plots the maximum error with different epsilons and dimensions."""

    fig = plt.figure()
    ax = fig.gca()

    plt.grid(True)

    ns = data["n"]

    # ax.loglog(ns, map(lambda x: x*x, ns), "-", basex=10, basey=10, label="x^2")

    ax.set_xlabel('n')
    ax.set_ylabel('Error')

    for eps, style in data["eps"]:

        print("Plotting for eps={0}".format(eps))

        iterative = p.Iterative(data["omega"], eps)

        ys = []
        for n in ns:
            matrix, b = p.lgs(p.rhs, n)
            e = iterative.get_error(n, matrix, b)
            ys.append(e)

        ax.loglog(ns, ys, style, basex=10, basey=10, label="eps={0}".format(eps))

    plt.legend()
    plt.show()


def main(plot, data):
    """Plots the given task."""
    if plot == "b":
        plot_b(data)
    if plot == "c":
        plot_c(data)
