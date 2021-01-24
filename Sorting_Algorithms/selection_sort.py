"""
    Selection Sort:
    Worst Time Complexity   : O(n^2)
    Best Time Complexity    : O(n^2)
    Average Time Complexity : O(n^2)
"""


def selection_sort(a):
    arr = a.copy()
    n = len(arr)
    for i in range(n):
        k = i
        for j in range(i, n):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]

    return arr


def main():
    arr = [11, 13, 7, 2, 6, 9, 4, 5, 10, 3]
    print(f"Sorted array : {selection_sort(arr)}")


if __name__ == '__main__':
    main()
