# Authors: Tom Lambert (lambertt) and Yuuma Odaka-Falush (odafaluy)


import matrix


def main():
    """Executes the main program with predefined values."""
    experiment = "3.2B - A"         # allowed are "3.1B", "3.2B - B", "3.2B - A"

    # The types to use for the experiments
    dtypes = ["float16", "float32", "float64"]

    # Parameters for 3.1A
    mtypes = ["hilbert", "saite"]   # The matrix types
    dims = [5, 7, 9]                # The dimensions

    # Parameters for 3.2B - A and B
    n = [5, 8, 51, 101]
    # Parameters for 3.2B - B
    i = [1, 2, 3, 4, 5, 6, 7, 8]    # only i <= n will be used

    matrix.main(experiment, mtypes, dims, dtypes, n, i)


if __name__ == "__main__":
    main()
