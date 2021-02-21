def subUnsort(A):
    n = len(A)
    i, j = 0, n - 1
    left = 0
    right = 0
    while i < n - 1:
        if A[i] > A[i + 1]:
            left = i
            break
        i += 1

    if i == n - 1:
        return [-1]

    while j > 0:
        if A[j] < A[j - 1]:
            right = j
            break
        j -= 1

    max_val = A[left]
    min_val = A[left]
    for k in range(left + 1, right + 1):
        if A[k] > max_val:
            max_val = A[k]
        if A[k] < min_val:
            min_val = A[k]

    for k in range(left):
        if A[k] > min_val:
            left = k
            break

    i = n - 1
    while i >= right + 1:
        if A[i] < max_val:
            right = i
            break
        i -= 1

    return [left, right]


def main():
    A = [1, 3, 2, 4, 5]
    print(subUnsort(A))


if __name__ == '__main__':
    main()
