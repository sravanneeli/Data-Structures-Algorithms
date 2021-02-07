import sys


def maxArr(A):
    n = len(A)
    max1 = -sys.maxsize
    min1 = sys.maxsize
    max2 = -sys.maxsize
    min2 = sys.maxsize

    for i in range(n):
        max1 = max(max1, A[i] + i)
        min1 = min(min1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min2 = min(min2, A[i] - i)

    return max(max1 - min1, max2 - min2)


def main():
    print(f"Max sum possible {maxArr([1, 3, -1])}")


if __name__ == '__main__':
    main()
