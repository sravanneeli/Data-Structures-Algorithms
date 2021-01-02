# missing elements when unsorted
def get_missing_numbers(arr, n):
    aux = [0] * (n+1)
    for i in range(len(arr)):
        aux[arr[i]] = 1
    missed = []
    for i in range(1, n+1):
        if aux[i] == 0:
            missed.append(i)
    return missed

# finding multiple missing elements when sorted
def multiple_missing_numbers(arr):
    diff = arr[0] - 0
    missed = []
    for i in range(len(arr)):
        if arr[i] - i != diff:
            while diff < arr[i] - i:
                    missed.append(i + diff)
                    diff += 1
    return missed
    
# if array start from any number but in sorted order
def missing_number(arr):
    diff = arr[0] - 0
    for i in range(len(arr)):
        if arr[i] - i != diff:
            return i + diff

# if array is from 1 to n
def missing_number_n(arr, n):
    s = (n * (n+1)) // 2
    return s - sum(arr)

def main():
    arr = [1,2,3,4,5,6,8,9,10,11,12]
    arr2 = [6, 7, 8, 9, 11, 12, 13, 14, 15]
    arr3 = [6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19]
    n = len(arr) + 1
    nmax = 12
    arr4 = [3, 7, 4, 9, 12, 6, 1, 11, 2, 10]

    print("Missing Element in the array is :", missing_number_n(arr, n))
    print("Missing Element in the array is :", missing_number(arr2))
    print("Missing Element in the array is :", *multiple_missing_numbers(arr3))
    print("Missing Element in the array is :", *get_missing_numbers(arr4, nmax))

