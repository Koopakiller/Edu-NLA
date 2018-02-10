# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use("TkAgg")

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


import poisson as p


def plot_b(data):
    n = data["n"]
    h = 1.0/n

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(np.arange(0, 1 + h, h), np.arange(0, 1 + h, h))
    ax.set_xlabel('ih')
    ax.set_ylabel('jh')
    ax.set_zlabel('u(ih, jh)')
    ax.plot_surface(x, y, p.exactu(x, y))

    plt.show()


def plot_c(eps):

    iterative = p.Iterative(5)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ns = [3, 4, 5]
    ys = []
    for n in ns:
        matrix, b = p.lgs(p.rhs, n)
        e = iterative.get_error(n, matrix, b)
        ys.append(e)

    ax.plot(ns, ys, "ro")

    plt.show()


def main(plot, data):
    if plot == "b":
        plot_b(data)
    if plot == "c":
        plot_c(data)
