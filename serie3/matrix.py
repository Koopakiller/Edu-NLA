# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import numpy
import scipy
import scipy.linalg


class Matrix:
    """
    Provides Methods for operations with an hilbert- or a special triangular matrix.
    """

    def __init__(self, mtype, dim, dtype):
        """
        Initializes the class instance.

        :param mtype: The matrix type ("hilbert" or "saite" for triangular)
        :param dim: The dimension. Must be > 0.
        :param dtype: The type to use. Can be "float16", "float32" or "flaot64"
        """
        if mtype not in ["saite", "hilbert"]:
            raise Exception("Unknown mtype. Allowed are 'hilbert' and 'saite'.")
        self.mtype = mtype

        if dim <= 0:
            raise Exception("dim must be > 0")
        self.dim = dim

        if dtype not in ["float16", "float32", "float64"]:
            raise Exception("Unknown dtype. Allowed are 'float16', 'float32' and 'float64'.")
        self.dtype = dtype
        self.dtype_constructor = None

        self.matrix = None
        self.inv = None

        self.l = None
        self.u = None

        self.create_matrix_and_inv()

    def create_matrix_and_inv(self):
        """
        Calculates the matrix from the values given to the constructor and its inverse.

        :return: Nothing.
        """
        arr = []
        if self.mtype == "saite":
            for row in xrange(0, self.dim):
                arr.append([])
                for col in xrange(0, self.dim):
                    if row == col:
                        arr[row].append(2)
                    elif row - 1 == col or col - 1 == row:
                        arr[row].append(-1)
                    else:
                        arr[row].append(0)

        if self.mtype == "hilbert":
            arr = scipy.linalg.hilbert(self.dim).tolist()

        self.matrix = numpy.array(arr, dtype=self.dtype)
        self.inv = scipy.linalg.inv(self.matrix)

    def condition(self):
        """
        Calculates the condition of the matrix.

        :return: The condition of the matrix.
        """
        return numpy.linalg.norm(self.matrix, ord=numpy.inf) * numpy.linalg.norm(self.inv, ord=numpy.inf)

    def lu(self):
        """
        Splits the matrix into l (left lower) and u (right upper) matrices. (Matrix A = LU)

        :return: A Tuple l,u of matrices
        """
        if self.l is None or self.u is None:
            self.l, self.u = scipy.linalg.lu(self.matrix, permute_l=True)
        return self.l, self.u

    def solve(self, b):
        """
        Solves the equation Ax=b for x and the matrix A.

        :param b: The vector b to solve the Matrix for.
        :return: The vector x from Ax=b.
        """
        l, u = self.lu()
        x = scipy.linalg.solve_triangular(u, b, lower=False)
        x = scipy.linalg.solve_triangular(l, x, lower=True)
        return x


def main_31b(mtypes, dims, dtypes):
    """
    Executes experiments as described in 3.1B.

    :param mtypes: The mtype-values to use.
    :param dims: The dimensions to use.
    :param dtypes: The dtype-values to use.
    :return: Nothing.
    """
    for mtype in mtypes:
        for dim in dims:
            for dtype in dtypes:
                print("")
                print("Experiment for mtype={0}, dim={1}, dtype={2}".format(mtype, dim, dtype))

                identity = numpy.identity(dim, dtype)
                matrix = Matrix(mtype, dim, dtype)
                m = identity - (matrix.matrix * matrix.inv)

                try:
                    m_inv = scipy.linalg.inv(m)
                except (numpy.linalg.linalg.LinAlgError, ValueError) as ex:
                    print("Cannot calculate inverse of M: " + ex.message)
                    continue

                condition = numpy.linalg.norm(m, ord=numpy.inf) * numpy.linalg.norm(m_inv, ord=numpy.inf)
                print("cond(M) = {1}         || I - M M^(-1) || = {0}".format(condition, matrix.condition()))


def main_32b_saite():
    print("Not Implemented")


def main_32b_hilbert(i_max, dtype, n):
    """
    Executes experiments as described in 3.2B B. (Hilbert)

    :param i_max: The maximum i to use
    :param dtype: the data-type to use (float16, float32 or float64)
    :param n: The dimension to use.
    :return: Nothing.
    """
    matrix = Matrix("hilbert", n, dtype)
    print("Hilbert Matrix with n={0} and type {1}".format(n, dtype))
    result = numpy.identity(n, dtype=dtype)
    for i in xrange(1, i_max + 1):
        result = result * matrix.matrix
        print("i = {0}, x^{0} = ".format(i))
        print(result)


def main_32b(dtypes, n_iterable, i_iterable):
    """
    Executes experiments as described in 3.2B

    :param dtypes: the data-type to use (float16, float32 or float64)
    :param n_iterable: The n-values to use.
    :param i_iterable: The i-values to use. (if i>n it will be ignored).
    :return: Nothing.
    """
    for dtype in dtypes:
        for n in n_iterable:
            for i_max in i_iterable:
                if i_max > n:
                    continue
                main_32b_hilbert(i_max, dtype, n)


def main(experiment, mtypes=None, dims=None, dtypes=None, n_iterable=None, i_iterable=None):
    """
    Executes experiments as described.
    See start.py for more information.

    :return: Nothing.
    """
    if experiment == "3.1B":
        main_31b(mtypes, dims, dtypes)
    elif experiment == "3.2B - A":
        main_32b_saite()
    elif experiment == "3.2B - B":
        main_32b(dtypes, n_iterable, i_iterable)
    else:
        print("Unknown experiment")
