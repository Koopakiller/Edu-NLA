import numpy as np
import numpy.linalg
import math


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
    return np.matrix(map(lambda pair: [e**(d * pair[0]), e**(-d * pair[0]), 1, ], data_list))


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
    for d in get_d_list(3):
        a = get_a_from_data_list(data_list, d)
        q, r = np.linalg.qr(a)
        print q
        print r

if __name__ == "__main__":
    main()
