"""
    Bubble Sort:
    Worst Time Complexity   : O(n^2)
    Best Time Complexity    : O(n)
    Average Time Complexity : O(n^2)
"""


def bubble_sort(a):
    arr = a.copy()
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
    A = [8, 5, 7, 3, 2]
    print(f"sorted array : {bubble_sort(A)}")


if __name__ == '__main__':
    main()
