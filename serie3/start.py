# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import matrix


def main():
    mtypes = ["hilbert", "saite"]
    dims = [3, 5, 7, 9]
    dtypes = ["float16", "float32", "float64"]
    matrix.main(mtypes, dims, dtypes)


if __name__ == "__main__":
    main()
