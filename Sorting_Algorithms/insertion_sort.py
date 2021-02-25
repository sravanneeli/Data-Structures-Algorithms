"""
    Insertion Sort:
    Worst Time Complexity   : O(n^2)
    Best Time Complexity    : O(n)
    Average Time Complexity : O(n^2)
"""


def insertion_sort(a):
    arr = a
    n = len(arr)
    for i in range(1, n):
        x = arr[i]
        j = i - 1
        while j > -1 and arr[j][1] < x[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr


def main():
    arr = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]]
    print("Sorted Array:", insertion_sort(arr))


if __name__ == "__main__":
    main()
