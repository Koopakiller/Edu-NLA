import matrix
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy


r = numpy.arange(0, 3.2, 0.1)
plt.plot(r, numpy.sin(r), "go")
plt.plot(r, numpy.sin(r), "-")

plt.xlabel("x")
plt.ylabel("y")

plt.show()
