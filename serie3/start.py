# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import matrix


def main():
    experiment = "3.2B - B"  # allowed are "3.1B", "3.2B - B"

    # The type to use for the experiments
    dtypes = ["float16", "float32", "float64"]

    # Parameters for 3.1A
    mtypes = ["hilbert", "saite"]
    dims = [5, 7, 9]

    # Parameters for 3.2 B
    n = [5, 8]
    i = [1, 2, 3, 4, 5, 6, 7, 8]  # only i <= n will be used

    matrix.main(experiment, mtypes, dims, dtypes, n, i)


if __name__ == "__main__":
    main()
