"""
Problem Description

Given a sorted array A and a target value B, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

"""
def bisect_left(arr, val):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # print(mid)
        if arr[mid] == val:
            return mid
        elif val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

def main():
    A = [1, 3, 5, 7]
    B = 100
    print(bisect_left(A, B))


if __name__ == "__main__":
    main()
    