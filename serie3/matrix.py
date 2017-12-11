# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import numpy
import scipy
import scipy.linalg


class Matrix:

    def __init__(self, mtype, dim, dtype):
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
        self.__init__dtype_constructor()

        self.matrix = None
        self.inv = None

        self.l = self.u = None

        self.create_matrix_and_inv()

    def __init__dtype_constructor(self):
        if self.dtype == "float16":
            self.dtype_constructor = lambda x: numpy.float16(x)
        if self.dtype == "float32":
            self.dtype_constructor = lambda x: numpy.float32(x)
        if self.dtype == "float64":
            self.dtype_constructor = lambda x: numpy.float64(x)

    def create_matrix_and_inv(self):
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
        return numpy.linalg.norm(self.matrix, ord=numpy.inf) * numpy.linalg.norm(self.inv, ord=numpy.inf)

    def lu(self):
        if self.l is None or self.u is None:
            self.l, self.u = scipy.linalg.lu(self.matrix, permute_l=True)
        return self.l, self.u

    def solve(self, b):
        l, u = self.lu()
        x = scipy.linalg.solve_triangular(u, b, lower=False)
        x = scipy.linalg.solve_triangular(l, x, lower=True)
        return x


def main_31b(mtypes, dims, dtypes):
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
                print("||M|| = {1}         || I - M M^(-1) || = {0}".format(condition, matrix.condition()))


def main_32b_hilbert(dtypes, n_iterable, i_iterable):
    for dtype in dtypes:
        for n in n_iterable:
            for i_max in i_iterable:
                if i_max > n:
                    continue
                matrix = Matrix("hilbert", n, dtype)
                print("Hilbert Matrix with n={0} and type {1}".format(n, dtype))
                result = numpy.identity(n, dtype=dtype)
                for i in xrange(1, i_max + 1):
                    result = result * matrix.matrix
                    print("i = {0}, x^{0} = ".format(i))
                    print(result)


def main(experiment, mtypes=None, dims=None, dtypes=None, n=None, i=None):
    if experiment == "3.1B":
        main_31b(mtypes, dims, dtypes)
    if experiment == "3.2B - B":
        main_32b_hilbert(dtypes, n, i)
    else:
        print("Unknown experiment")
