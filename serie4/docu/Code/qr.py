q, r = np.linalg.qr(a)
if np.linalg.matrix_rank(r) != 3 \
        or np.linalg.matrix_rank(q) != 3:
    print("Rank of r or q is not 3!")
else:
    # z = q^T * b; rx = z
    z = np.dot(q.T, b)
    x = scipy.linalg.solve_triangular(r, z)
