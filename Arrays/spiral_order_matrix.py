def spiralOrder(A):
    m, n = len(A), len(A[0])
    output = [0] * (m * n)
    k, l = 0, 0
    pos = 0
    while (k < m and l < n):
        for r in range(l, n):
            output[pos] = A[k][r]
            pos += 1
        k += 1
        for r in range(k, m):
            output[pos] = A[r][n - 1]
            pos += 1
        n -= 1
        if k < m:
            for r in range(n - 1, (l - 1), -1):
                output[pos] = A[m - 1][r]
                pos += 1
            m -= 1
        if l < n:
            for r in range(m - 1, (k - 1), -1):
                output[pos] = A[r][l]
                pos += 1
            l += 1
    return output


def main():
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(spiralOrder(A))


if __name__ == "__main__":
    main()
