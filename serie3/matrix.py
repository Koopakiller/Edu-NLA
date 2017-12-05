# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import numpy


class Matrix:

    def __init__(self, mtype, dim, dtype):
        if mtype not in ["hilbert", "saite"]:
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

    def create_matrix(self):
        pass

    def create_inv(self):
        pass

    def condition(self):
        pass


def main():
    pass
