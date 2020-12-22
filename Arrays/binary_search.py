import math

# Loop approach
def binary_search(A, key):
    l = 0
    h = len(A)
    while (l <= h):
        mid = math.floor((l + h) / 2)

        if A[mid] == key:
            return mid
        elif key < A[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return -1

# Recursive Approach
def rbinary_search(A, l, h, key):

    if l <= h:
        mid = math.floor((l + h) / 2)

        if A[mid] == key:
            return mid
        elif key < A[mid]:
            return rbinary_search(A, l, mid - 1, key)
        else:
            return rbinary_search(A, mid+1, h, key)

    return -1

def main():
    A = [3, 4, 5, 10, 20, 25, 28, 29]
    index = binary_search(A,29)
    if index == -1:
        print("Key not found")
    else:
        print("Key found at index: {}".format(index))
    index = rbinary_search(A, 0, len(A), 3)
    if index == -1:
        print("Key not found")
    else:
        print("Key found at index: {}".format(index))

main()
