def sorted_pair_k(arr, k):
    i = 0
    j = len(arr) - 1
    pairs = []
    while i < j:
        if arr[i] + arr[j] == k:
            pairs.append((arr[i], arr[j]))
            i += 1
            j -= 1
        elif arr[i] + arr[j] < k:
            i += 1
        else:
            j -= 1

    return pairs


def sum_pair_k(arr, k):
    n = max(arr) + 1
    aux = [0] * n
    pairs = []
    for i in range(len(arr)):
        if aux[k - arr[i]] != 0:
            pairs.append((arr[i], k - arr[i]))
        aux[arr[i]] += 1

    return pairs


def main():
    arr = [6, 3, 8, 10, 16, 7, 5, 2, 9, 14]
    k = 10
    print("Pairs where sum is {} are {}".format(k, sum_pair_k(arr, k)))
    arr.sort()
    print("Pairs when sum is {} and array is sorted: {}".format(k, sorted_pair_k(arr, k)))


if __name__ == '__main__':
    main()
