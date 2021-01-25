def shell_short(a):
    arr = a.copy()
    n = len(arr)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i - gap
            while j > -1 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        gap //= 2

    return arr


def main():
    arr = [11, 13, 7, 12, 16, 9, 24, 5, 10, 3]
    print(f"Sorted array {shell_short(arr)}")


if __name__ == '__main__':
    main()
