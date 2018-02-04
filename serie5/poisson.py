import scipy
import numpy


class Problem:

    def rhs(self, x_1, x_2):
        return -(2 * x_1 * x_2 * x_2 - 2 * x_1 * x_2 - x_2 * x_2 + x_2) - \
                (2 * x_2 * x_1 * x_1 - 2 * x_2 * x_1 - x_1 * x_1 + x_1)

    def lgs(self, rhs, n):
        result_a = scipy.dok_matrix((n*n, n*n))
        result_b = scipy.dok_matrix((1, n*n))
        # TODO: Fill result_a and result_b
        return result_a, result_b

    def exactu(self, x_1, x_2):
        # TODO: Implement
        pass


class Iterative:

    def __init__(self, omega):
        self._omega = omega

    def diskreteLsgSOR(self, matrix, b, x_0, error_border):
        """
        :param matrix: The matrix A with the problem to solve
        :param b: The b in Ax-b<eps
        :param x_0: The start vector for the iterative procedure
        :param error_border: The algorithm stops when the error is less then this border
        """
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

    def get_error(self):
        pass

