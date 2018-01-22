q, r = np.linalg.qr(a)
if r_rank(r) != 3:
    print("Rank of r or q is not 3!")
else:
    # z = q^T * b; rx = z
    z = np.dot(q.T, b)
    x = scipy.linalg.solve_triangular(r, z)
