def max_min_arr(arr):
    max_ele = arr[0]
    min_ele = arr[0]
    for i in range(1, len(arr)):
        if min_ele < arr[i]:
            min_ele = arr[i]
        elif max_ele > arr[i]:
            max_ele = arr[i]

    return max_ele, min_ele

def main():
    arr = [5, 8, 3, 9, 6, 2, 20, 7, -1, 4]
    max_ele, min_ele = max_min_arr(arr)
    print("Max and Min of the array is {}, {}".format(max_ele, min_ele))


if __name__ == "__main__":
    main()