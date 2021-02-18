def balance(A):
    n = len(A)
    odd = 0
    even = 0
    leftOdd = [0] * n
    rightOdd = [0] * n
    leftEven = [0] * n
    rightEven = [0] * n
    for i in range(n):
        leftOdd[i] = odd
        leftEven[i] = even
        if i % 2 == 0:
            even += A[i]
        else:
            odd += A[i]
    # print(leftOdd, leftEven)

    odd = 0
    even = 0
    for i in range(n - 1, -1, -1):
        rightOdd[i] = odd
        rightEven[i] = even
        if i % 2 == 0:
            even += A[i]
        else:
            odd += A[i]
    ans = 0
    for i in range(n):
        if leftOdd[i] + rightEven[i] == leftEven[i] + rightOdd[i]:
            ans += 1

    return ans


def main():
    A = [5, 5, 2, 5, 8]
    print(f"Possible special numbers are: {balance(A)}")


if __name__ == '__main__':
    main()
