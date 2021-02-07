def getMaxMin(arr, low, high):
    if low == high:
        arr_max = arr[low]
        arr_min = arr[high]
        return arr_max, arr_min
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
            return arr_max, arr_min
        else:
            arr_max = arr[high]
            arr_min = arr[low]
            return arr_max, arr_min
    else:
        mid = (low + high) // 2
        arr_max1, arr_min1 = getMaxMin(arr, low, mid)
        arr_max2, arr_min2 = getMaxMin(arr, mid + 1, high)

    return max(arr_max1, arr_max2), min(arr_min1, arr_min2)


def main():
    arr = [-79, 63, 6, -82, 62]
    max_val, min_val = getMaxMin(arr, 0, len(arr) - 1)
    print(f"Max and Min value of the array {max_val + min_val}")


if __name__ == '__main__':
    main()
