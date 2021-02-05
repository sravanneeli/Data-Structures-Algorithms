from bisect import bisect_left


def binary_search(arr, x):
    index = bisect_left(arr, x)
    if index:
        return index - 1
    else:
        return -1


def tripletSum(A):
    n = len(A)
    suffix_max = [0] * n
    suffix_max[n - 1] = A[n - 1]
    ans = 0
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], A[i])
    left = [A[0]]
    for i in range(1, n - 1):
        index = binary_search(left, A[i])
        if index != -1:
            if suffix_max[i + 1] <= A[i]:
                continue
            val = left[index] + A[i] + suffix_max[i + 1]
            ans = max(ans, val)

    return ans


def main():
    A = [2, 5, 3, 1, 4, 9]
    print(f"Max Sum Triplet: {tripletSum(A)}")


if __name__ == '__main__':
    main()
