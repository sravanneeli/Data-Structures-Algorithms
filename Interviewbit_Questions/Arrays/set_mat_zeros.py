def set_mat_zeros(A):
    m, n = len(A), len(A[0])
    rows = set()
    cols = set()
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        for j in range(n):
            A[row][j] = 0

    for col in cols:
        for i in range(m):
            A[i][col] = 0

    print(A)


def main():
    A = [[1, 0],
         [1, 1],
         [1, 0]]
    set_mat_zeros(A)


if __name__ == '__main__':
    main()
