import sys


def get_leaders(A):
    n = len(A)
    if n == 1:
        return A
    suffixMax = []
    maxVal = -sys.maxsize
    for i in range(n - 1, -1, -1):
        maxVal = max(A[i], maxVal)
        suffixMax.append(maxVal)
    suffixMax = suffixMax[::-1]
    leaders = []
    for i in range(n):
        if A[i] >= suffixMax[i]:
            leaders.append(A[i])

    return leaders


def main():
    A = [16, 17, 4, 3, 5, 2]
    get_leaders(A)


if __name__ == '__main__':
    main()
