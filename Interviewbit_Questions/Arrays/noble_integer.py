'''
Problem Description

Given an integer array A, find if an integer p exists in the array such that the number of 
integers greater than p in the array equals to p.
'''

def noble(arr):
    arr.sort()
    n = len(arr)
    if arr[n-1] == 0:
        return True
    for i in range(n):
        if arr[i] != arr[i-1]:
            if arr[i] == n-i+1:
                return True

    return False


def main():
    arr = [3, 2, 1, 3]
    print(f"Noble Integer present or not: {noble(arr)}")

if __name__ == '__main__':
    main()
