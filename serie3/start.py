# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import matrix


def main():
    mtypes = ["hilbert", "saite"]
    dims = [5, 7, 9]
    dtypes = ["float16", "float32", "float64"]
    experiment = "3.1B"  # allowed are "3.1B"
    matrix.main(mtypes, dims, dtypes, experiment)


if __name__ == "__main__":
    main()
