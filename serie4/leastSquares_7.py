import numpy as np
import numpy.linalg
import math
from plot import plot as plot


def read_data(file_name):
    file_object = open(file_name, "r")
    result = []
    for line in file_object.readlines():
        parts = map(lambda part: float(part.strip()), line.split(","))
        if len(parts) != 2:
            raise Exception("illegal line format")
        result.append((parts[0], parts[1]))
    file_object.close()
    return result


def get_b_from_data_list(data_list):
    return np.matrix(map(lambda pair: [pair[1]], data_list))


def get_a_from_data_list(data_list, d):
    e = math.e
    return np.matrix(map(lambda pair: [e**(d * pair[0]), e**(-d * pair[0]), 1], data_list))


def get_d_list(n):
    if n <= 2:
        raise Exception("n is not > 2")

    result = []
    for k in range(0, n):
        result.append(0.1 + 0.4 * k / (n - 1))
    return result


def main():
    data_list = read_data("data.txt")
    b = get_b_from_data_list(data_list)
    parameter_list = []
    for d in get_d_list(3):
        a = get_a_from_data_list(data_list, d)
        q, r = np.linalg.qr(a)
        if np.linalg.matrix_rank(r) != 3 or np.linalg.matrix_rank(q) != 3:
            print("Rank of r or q is not 3!")
        else:
            p = np.dot(q.T, b)
            x = np.dot(np.linalg.inv(r), p)
            parameter_list.append((x.item(0), x.item(1), x.item(2), d))
    plot(parameter_list)


if __name__ == "__main__":
    main()
