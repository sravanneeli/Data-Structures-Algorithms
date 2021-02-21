"""
Problem Description

Given an array A of integers, find the maximum of j - i subjected to the 
constraint of A[i] <= A[j].
"""
import sys


def maxGap(A):
    n = len(A)
    new = []
    for i in range(n):
        new.append([i, A[i]])

    new = sorted(new, key=lambda x: x[1])

    indexMax = [0] * n
    max_val = -sys.maxsize
    for i in range(n - 1, -1, -1):
        max_val = max(max_val, new[i][0])
        indexMax[i] = max_val
    ans = -sys.maxsize
    for i in range(n):
        ans = max(ans, indexMax[i] - new[i][0])

    return ans


def main():
    A = [3, 5, 4, 2]
    print(f"Max Gap is: {maxGap(A)}")


if __name__ == '__main__':
    main()
