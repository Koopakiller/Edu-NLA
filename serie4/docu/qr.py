q, r = np.linalg.qr(a)
if np.linalg.matrix_rank(r) != 3 \
        or np.linalg.matrix_rank(q) != 3:
    print("Rank of r or q is not 3!")
else:
    # x = inv(r) * q^T * b
    p = np.dot(q.T, b)
    x = np.dot(np.linalg.inv(r), p)
