from collections import defaultdict
from math import sqrt
import bisect


def getFrequency(arr):
    n = len(arr)
    left = [1] * n
    right = [1] * n
    s = []
    top = -1
    for i in range(n):
        # print(s, left)
        while top >= 0 and arr[s[top]] <= arr[i]:
            s.pop()
            top -= 1
        if top >= 0 :
            left[i] = i - s[top]
        else:
            left[i] = i + 1

        s.append(i)
        top += 1

    S = []
    top = -1
    for i in range(n-1, -1, -1):
        while(top >= 0 and arr[S[top]] < arr[i]):
            S.pop()
            top -= 1
        if (top >= 0):
            right[i] = S[top] - i
        else:
            right[i] = n - i
        S.append(i)
        top += 1
    print(left, right)
    for i in range(n):
        left[i] *= right[i]
    return left

def main():
    arr = [300, 300, 100, 100,200, 200]
    print(getFrequency(arr))

if __name__ == '__main__':
    main()
    