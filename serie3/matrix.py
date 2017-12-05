# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import numpy
import scipy


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
                for col in xrange(0, self.dim):
                    if row == col:
                        arr.append(2)
                    elif row - 1 == col or col - 1 == row:
                        arr.append(-1)
                    else:
                        arr.append(0)

        if self.mtype == "hilbert":
            arr = scipy.linalg.hilbert(self.dim).tolist()

        self.matrix = numpy.ndarray(shape=(self.dim, self.dim), dtype=self.dtype, buffer=numpy.array(arr))
        self.inv = numpy.linalg.inv(self.matrix)

    def condition(self):
        # TODO: allowed to use numpy?
        return numpy.linalg.cond(self.matrix, p="inf")

    def solve(self, b):
        pass


def main(mtypes, dims, dtypes):
    for mtype in mtypes:
        for dim in dims:
            for dtype in dtypes:
                # TODO: Implement stuff for 3.1 B
                pass
