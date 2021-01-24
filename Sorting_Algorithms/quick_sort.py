def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


def main():
    arr = [11, 13, 7, 12, 16, 9, 24, 5, 10, 3]
    print(f"Sorted array {quick_sort(arr, 0, len(arr) - 1)}")


if __name__ == '__main__':
    main()
