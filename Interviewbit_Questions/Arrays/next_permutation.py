def next_max_index(start, arr, curr):
    ans = -1
    index = 0
    for i in range(start, len(arr)):
        if arr[i] > curr:
            if ans == -1:
                ans = curr
                index = i
            else:
                ans = min(ans, arr[i])
                index = i
    return index



def next_permutation(A):
    arr = A.copy()
    n = len(arr)
    i = n - 2
    found = False
    while i >= 0 :
        if arr[i] < arr[i+1]:
            found = True
            break
        i -= 1
    if found:
        m = next_max_index(i+1, arr, arr[i])
        arr[i], arr[m] = arr[m], arr[i]
        arr[i+1:] = arr[i+1:][::-1]
        return arr       
    else:
        arr.sort()
        return arr


def main():
    arr = [1, 3, 2]
    print(f"next greater permutation: {next_permutation(arr)}")

if __name__ == "__main__":
    main()