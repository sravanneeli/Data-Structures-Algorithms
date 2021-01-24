def merge(arr, start, mid, end):
    temp = [0] * (end - start + 1)
    i, j, k = start, mid + 1, 0

    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(start, end + 1):
        arr[i] = temp[i - start]


def merge_iter(arr):
    n = len(arr)
    p = 2
    while p <= n:
        i = 0
        while i+p-1 < n:
            low = i
            high = i + p - 1
            mid = (low + high) // 2
            merge(arr, low, mid, high)
            i += p
        p *= 2

    if p // 2 < n:
        merge(arr, 0, p//2, n-1)


def mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def main():
    arr = [14, 7, 3, 12, 9, 11, 6, 2, 15]
    # mergesort(arr, 0, len(arr) - 1)
    merge_iter(arr)
    print("Sorted Array:", arr)


if __name__ == "__main__":
    main()
