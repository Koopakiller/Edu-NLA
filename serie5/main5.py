import matplotlib
matplotlib.use("TkAgg")

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


import poisson as p


def plot_b(data):

    for n in data["exact_plot"]:
        h = 1.0/n
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y = np.meshgrid(np.arange(0, 1 + h, h), np.arange(0, 1 + h, h))
        ax.set_xlabel('ih')
        ax.set_ylabel('jh')
        ax.set_zlabel('u(ih, jh)')
        ax.plot_surface(x, y, p.exactu(x, y))

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

    fig = plt.figure()
    ax = fig.gca()

    for eps, style in data["eps"]:

        iterative = p.Iterative(data["omega"], eps)

        ns = data["n"]
        ys = []
        for n in ns:
            matrix, b = p.lgs(p.rhs, n)
            e = iterative.get_error(n, matrix, b)
            ys.append(e)

        ax.loglog(ns, ys, style, basex=10, basey=10)
    plt.grid(True)
    plt.legend()
    plt.show()


def main(plot, data):
    if plot == "b":
        plot_b(data)
    if plot == "c":
        plot_c(data)
