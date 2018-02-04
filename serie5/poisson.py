import scipy.sparse
import numpy


class Problem:

    def rhs(self, x_1, x_2):
        return -(2 * x_1 * x_2 * x_2 - 2 * x_1 * x_2 - x_2 * x_2 + x_2) - \
                (2 * x_2 * x_1 * x_1 - 2 * x_2 * x_1 - x_1 * x_1 + x_1)

    def lgs(self, rhs, n):
        result_a = scipy.sparse.dok_matrix((n, n))
        result_b = scipy.sparse.dok_matrix((1, n))

        for x in range(0, n):
            for y in range(0, n):
                result_a[x, y] = rhs(float(x) / float(n), float(y) / float(n))

        return result_a, result_b

    @staticmethod
    def exactu(x_1, x_2):
        return x_1 * (1 - x_1) * x_2 * (1 - x_2)


class Iterative:

    def __init__(self, omega):
        self._omega = omega

    def diskreteLsgSOR(self, matrix, b, x_0=None, error_border=None):
        """
        :param matrix: The matrix A with the problem to solve
        :param b: The b in Ax-b<eps
        :param x_0: The start vector for the iterative procedure
        :param error_border: The algorithm stops when the error is less then this border
        """

        if x_0 is None:
            x_0 = matrix.shape[1]

        if error_border is None:
            error_border = 10**-12

        result = x_0
        error = error_border
        n = len(x_0)
        while error >= error_border:
            for k in range(0, n):
                sum1 = 0.0
                for i in range(1, k-1):
                    sum1 = sum1 + matrix[k, i] * result[i]
                sum2 = 0.0
                for i in range(k+1, n):
                    sum2 = sum2 + matrix[k, i] * result[i]

                r2 = (1 - self._omega) * result[k] + self._omega / matrix[k, k] * (b[k] - sum1 - sum2)
                error = max(error, abs(r2 - result[k]))
                result[k] = r2

        return result

    def get_error(self, n, matrix, b):
        max_error = 0
        for x in range(0, n):
            for y in range(0, n):
                max_error = max(max_error, abs(self.diskreteLsgSOR(matrix, b) -
                                               Problem.exactu(float(x) / float(n), float(y) / float(n))))
        return max_error
