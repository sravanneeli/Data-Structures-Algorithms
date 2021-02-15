import sys


def perfect_peak(arr):
    n = len(arr)
    left_arr = []
    left_max = -sys.maxsize
    for i in range(1, n - 1):
        left_max = max(left_max, arr[i - 1])
        left_arr.append(left_max)

    # print(left_arr)

    right_arr = []
    right_min = sys.maxsize
    for i in range(n - 2, 0, -1):
        right_min = min(right_min, arr[i + 1])
        right_arr.append(right_min)

    right_arr = right_arr[::-1]
    for i in range(1, n - 1):
        if left_arr[i - 1] < arr[i] < right_arr[i - 1]:
            return True

    return False
    # print(right_arr)


def main():
    A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    print(f"Peak Element Exists or not: {perfect_peak(A)}")


if __name__ == '__main__':
    main()
