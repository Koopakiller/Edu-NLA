import scipy.sparse


def get_matrix(n):
    size = (n-1)*(n-1)
    result = scipy.sparse.dok_matrix((size, size))
    for block in range(0, n - 1):
        for i in range(0, n - 1):
            result[(block * (n-1)) + i, (block * (n-1)) + i] = 4
            if i > 0:
                result[(block * (n-1)) + i, (block * (n-1)) + i - 1] = -1
            if i < n-2:
                result[(block * (n-1)) + i, (block * (n-1)) + i + 1] = -1
            if block > 0:
                result[(block * (n-1)) + i, ((block-1) * (n-1)) + i] = -1
            if block < n-2:
                result[(block * (n-1)) + i, ((block+1) * (n-1)) + i] = -1
    return result


def main():
    matrix = get_matrix(5)
    print(matrix)
    pass


if __name__ == "__main__":
    main()
