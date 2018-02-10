from main5 import main


if __name__ == "__main__":
    # Parameter:
    #  First:  "b" or "c" for the Plots in 5.3 b respective 5.3 c
    #  Second: Parameters for the plots. e.g.:
    #    "b": {"omega": 5, "eps": 10**-5, "sor_plot": [10], "exact_plot": []}
    #    "c": {"omega": 5, "n": [3, 4, 5, 6, 7, 8], "eps": [10**-2, 10**-4, 10**-6]}

    #main("c", {"omega": 5, "n": [3, 4, 5, 6, 7, 8], "eps": [(10**-1, "ro"), (10**-2, "go"), (10**-3, "bo")]})
    main("b", {"omega": 1, "eps": 10**-8, "sor_plot": [5, 10], "exact_plot": []})
