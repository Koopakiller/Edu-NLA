from main5 import main


if __name__ == "__main__":
    # Parameter:
    #  First:  "b" or "c" for the Plots in 5.3 b respective 5.3 c
    #  Second: Parameters for the plots. e.g.:
    #    "b": {"omega": 5, "eps": 10**-5, "sor_plot": [10], "exact_plot": []}
    #    "c": {"omega": 5, "eps": }

    main("b", {"omega": 5, "eps": 10**-5, "sor_plot": [10], "exact_plot": []})
