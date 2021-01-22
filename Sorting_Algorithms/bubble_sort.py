def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        flag = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if flag:
            break

    return arr


def main():
    arr = [8, 5, 7, 3, 2]
    print(f"sorted array : {bubble_sort(arr)}")


if __name__ == '__main__':
    main()
