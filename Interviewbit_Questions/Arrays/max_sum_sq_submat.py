def valid(i, j, n):
    return 0 <= i < n and 0 <= j < n


def max_submat(A, B):
    n = len(A)
    print(n)
    ans = -10000000
    for i in range(n):
        for j in range(n):
            if valid(i - 1, j, n):
                A[i][j] += A[i - 1][j]
            if valid(i, j - 1, n):
                A[i][j] += A[i][j - 1]
            if valid(i - 1, j - 1, n):
                A[i][j] -= A[i - 1][j - 1]

    print(A)
    for i in range(n):
        for j in range(n):
            if i == B - 1 and j == B - 1:
                print(1)
                ans = max(ans, A[i][j])
            if i == B - 1 and j - B >= 0:
                print(2)
                print(i, j-B)
                curarea = A[i][j] - A[i][j - B]
                ans = max(ans, curarea)
            if j == B - 1 and i - B >= 0:
                print(3)
                print(j, i-B)
                curarea = A[i][j] - A[i - B][j]
                ans = max(ans, curarea)
            if valid(i - B, j - B, n):
                print(4)
                print(i-B, j-B)
                curarea = A[i][j] - A[i - B][j] - A[i][j - B] + A[i - B][j - B]
                ans = max(ans, curarea)
    return ans


def main():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(max_submat(A, 2))


if __name__ == '__main__':
    main()
