def r_rank(r):
    counter = 0
    eps = 10**-12
    for i in range(0, r.shape[0]):
        if not (-eps < r[i, i] < eps):
            counter += 1
    return counter
