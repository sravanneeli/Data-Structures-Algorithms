def repeatedNumber(A):
    n = len(A)
    checkArr = [0] * (n + 1)

    for i in range(n):
        if checkArr[A[i]] == 0:
            checkArr[A[i]] += 1
        else:
            return A[i]


def main():
    A = [3, 4, 1, 2, 1]
    print(repeatedNumber(A))


if __name__ == '__main__':
    main()
