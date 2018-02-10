import scipy.sparse
import numpy


def rhs(x_1, x_2):
    return -2*(x_2*(x_2-1)+x_1*(x_1-1))


def lgs(rhs, n):
    result_a = scipy.sparse.dok_matrix(((n-1)**2, (n-1)**2))
    result_b = scipy.sparse.dok_matrix(((n-1)**2, 1))

    for block in range(0, n - 1):
        for i in range(0, n - 1):
            result_a[(block * (n - 1)) + i, (block * (n - 1)) + i] = 4
            if i > 0:
                result_a[(block * (n - 1)) + i, (block * (n - 1)) + i - 1] = -1
            if i < n - 2:
                result_a[(block * (n - 1)) + i, (block * (n - 1)) + i + 1] = -1
            if block > 0:
                result_a[(block * (n - 1)) + i, ((block - 1) * (n - 1)) + i] = -1
            if block < n - 2:
                result_a[(block * (n - 1)) + i, ((block + 1) * (n - 1)) + i] = -1

    z = n - 2.0
    for i in range(0, (n - 1) * (n - 1)):
        z = z + 1
        result_b[i, 0] = (1.0/n) ** 2 * rhs((1.0/n) * (i % (n - 1) + 1), (1.0/n) * z / (n - 1))

    return result_a, result_b


def exactu(x_1, x_2):
    return x_1 * (1 - x_1) * x_2 * (1 - x_2)


class Iterative:

    def __init__(self, omega, error_border):
        self._omega = omega
        self._error_border = error_border

    def diskreteLsgSOR(self, matrix, b, x_0=None):
        """
        :param matrix: The matrix A with the problem to solve
        :param b: The b in Ax-b<eps
        :param x_0: The start vector for the iterative procedure
        """

        if x_0 is None:
            x_0 = [0 for _ in range(0, matrix.shape[1])]

        error = self._error_border
        n = len(x_0)
        while error >= self._error_border:

            for i in range(1, n):
                o = 0
                for j in range(1, n):
                    if i != j:
                        o = o + x_0[j] * matrix[i, j]
                x_1 = x_0[i]
                x_0[i] = (1 - self._omega) * x_0[i] + \
                         (self._omega / matrix[i, i]) * (b[i, 0] - o)

                error = min(error, abs(x_1 - x_0[i]))

        return x_0

    def get_error(self, n, matrix, b):
        max_error = 0
        it = self.diskreteLsgSOR(matrix, b)
        for x in range(0, n - 1):
            for y in range(0, n - 1):
                max_error = max(max_error, abs(it[x * (n - 1) + y][0, 0] - exactu(float(x) / float(n), float(y) / float(n))))
        return max_error
