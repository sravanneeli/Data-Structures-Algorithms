'''
    Insertion Sort:
    Worst Time Complexity   : O(n^2)
    Best Time Complexity    : O(n)
    Average Time Complexity : O(n^2)
'''
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

def main():
    arr = [25, 17, 31, 13, 2]
    print("Sorted Array:", insertion_sort(arr))
    

if __name__ == "__main__":
    main()