from main5 import main


if __name__ == "__main__":
    # Parameter:
    #  First:  "b" or "c" for the Plots in 5.3 b respective 5.3 c
    #  Second: Parameters for the plots.
    # e.g.:

    #main("c", {"omega": 1, "n": [3, 5, 7, 10, 15], "eps": [
    #    (0.1**-2, "ro-"),
    #    (0.1**0, "go-"),
    #    (0.1**2, "bo-"),
    #    (0.1**4, "co-"),
    #    (0.1**6, "mo-")
    #]})

    #main("b", {"omega": 1, "eps": 10**-6, "sor_plot": [4, 15], "exact_plot": [15]})

    main("b", {"omega": 1, "eps": 10 ** -6, "sor_plot": [4, 15], "exact_plot": [15]})
