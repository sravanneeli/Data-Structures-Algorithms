def neg_to_left(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        while arr[i] < 0 : i += 1
        while arr[j] >= 0 : j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr
    
def main():
    arr = [-6, 3, -8, 10, 5, -7, -9, 12, -4, 2]
    print("negatives to left and positives to right:", neg_to_left(arr))

main()