def reverse(arr):
    i = 0 
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

def main():
    arr = [4, 12, 9, 15, 6, 10, 7, 2, 3]
    print(reverse(arr))

main()