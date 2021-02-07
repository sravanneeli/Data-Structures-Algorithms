def maxSubArr(arr):
    n = len(arr)
    max_sub = arr[0]
    max_sum = arr[0]
    for i in range(1, n):
        max_sub = max(arr[i], max_sub + arr[i])
        max_sum = max(max_sub, max_sum)

    return max_sum


def main():
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(f"Max sum possible {maxSubArr(arr)}")


if __name__ == '__main__':
    main()
