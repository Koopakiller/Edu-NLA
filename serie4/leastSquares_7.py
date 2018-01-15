import numpy as np
import math
from plot import plot as plot
import scipy.linalg


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
        result.append((k, 0.1 + 0.4 * k / (n - 1)))
    return result


def r_rank(r):
    if r.shape[0] != r.shape[1]:
        raise Exception("r is not quadratic")

    counter = 0
    eps = 10**-12
    for i in range(0, r.shape[0]):
        if not (-eps < r[i, i] < eps):
            counter += 1
    return counter


def main(file_name="data.txt", n=7):
    data_list = read_data(file_name)
    b = get_b_from_data_list(data_list)
    parameter_list = []
    for k, d in get_d_list(n):
        print("k={0}; n={1}".format(k, n))
        a = get_a_from_data_list(data_list, d)
        q, r = np.linalg.qr(a)
        if r_rank(r) != 3:
            print("Rank of r or q is not 3!")
        else:
            z = np.dot(q.T, b)
            x = scipy.linalg.solve_triangular(r, z)

            r = np.dot(a, x) - b
            print("Residuum r = Ax - b = ")
            print(str(r))

            norm_r = np.linalg.norm(r)
            print("Norm of Residuum: |r| = " + str(norm_r))

            cond_a = np.linalg.cond(a)
            cond_ata = np.linalg.cond(np.dot(a.T, a))
            print("cond(A) = {0}; cond(A^T A) = {1}".format(cond_a, cond_ata))

            parameter_list.append((x.item(0), x.item(1), x.item(2), d, k, n, norm_r, cond_a, cond_ata))

        print("")

    plot(parameter_list, data_list)


if __name__ == "__main__":
    # available files:
    #  - data.txt          - from task sheet
    #  - data_subset.txt   - contains a subset from data.txt
    #  - data_sym.txt      - contains manipulated (symmetric) data from data.txt
    main(file_name="data.txt", n=5)
