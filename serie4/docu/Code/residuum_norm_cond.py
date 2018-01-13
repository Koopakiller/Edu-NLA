r = np.dot(a, x) - b

norm_r = np.linalg.norm(r)

cond_a = np.linalg.cond(a)
cond_ata = np.linalg.cond(np.dot(a.T, a))
