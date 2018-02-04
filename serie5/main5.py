from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


from poisson import Problem


def main():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    n = 10
    x = np.arange(0, 1, 1.0/n)
    y = np.arange(0, 1, 1.0/n)

    X, Y = np.meshgrid(x, y)

    zs = np.array([Problem.exactu(x, y) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z,
                    shade=True)

    plt.show()