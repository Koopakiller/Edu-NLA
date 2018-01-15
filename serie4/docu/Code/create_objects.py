# data_list = [(x, y), ...]

b = np.matrix(map(lambda pair:
                  [pair[1]], data_list))
a = np.matrix(map(lambda pair:
                  [e**(d * pair[0]),
                   e**(-d * pair[0]),
                   1], data_list))
