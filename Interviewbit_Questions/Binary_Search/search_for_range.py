"""
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
"""

def searchRange(arr, val):
    n = len(arr)
    low = 0
    high = n - 1
    first = -1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            first = last = mid
            while first > 0 and arr[first-1] == arr[mid]:
                first -= 1
            while last < n-1 and arr[last+1] == arr[mid]:
                last += 1
            break
        elif val > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return [first, last]

def main():
    A = [7, 7, 7, 8, 8, 10]
    B = 7
    print(f"Range of the search element: {searchRange(A, B)}")

if __name__ == "__main__":
    main()