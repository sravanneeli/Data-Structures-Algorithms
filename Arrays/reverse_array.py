def reverse(arr):
    i = 0 
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

def checksorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def main():
    arr = [4, 12, 9, 15, 6, 10, 7, 2, 3]
    arrsorted = [4, 8, 13, 25, 23,  28, 33]
    print("Reversed array",reverse(arr))
    print("array is sorted or not ?", checksorted(arrsorted))

main()