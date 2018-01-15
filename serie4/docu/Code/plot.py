x = numpy.arange(0, 25, 0.01)
for entry in parameter_list:
    a, b, c, d, k, n = entry
    plt.plot(x, a * (e ** (d * x)) +
                b * (e ** (-d * x)) + c,
             "-", label="...")

plt.plot(map(lambda pair: pair[0], points),
         map(lambda pair: pair[1], points),
         "ro", label="points")

plt.legend()
plt.xlabel("x")
plt.ylabel("y")

plt.show()
