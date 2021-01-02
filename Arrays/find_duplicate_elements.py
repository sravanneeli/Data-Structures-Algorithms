def get_duplicates_and_count(arr):
    n = max(arr) + 1
    aux = [0] * n
    for i in range(len(arr)):
        aux[arr[i]] += 1
    dup = {}
    for i in range(n):
        if aux[i] > 1:
            dup[i] = aux[i]
    return dup


def main():
    arr = [8, 3, 6, 5, 6, 8, 2, 7, 7, 7, 7, 7]
    print("Duplicate Elements and there Counts:", get_duplicates_and_count(arr))


