def square_sort(A):
    n = len(A)
    start = 0
    end = n - 1
    new = []
    while start <= end:
        left = pow(A[start], 2)
        right = pow(A[end], 2)
        if left >= right:
            new.append(left)
            start += 1
        if left < right:
            new.append(right)
            end -= 1

    return new[::-1]


def main():
    arr = [-855, -847, -747, -708, -701, -667, -666, -618, -609, -536, -533, -509, -500, -396, -336, -297, -284, -229,
           -173, -173, -132, -38, -5, 35, 141, 169, 281, 322, 358, 421, 436, 447, 478, 538, 547, 644, 667, 673, 705,
           711, 718, 724, 726, 811, 869, 894, 895, 902, 912, 942, 961]

    print(f"Sorted list of Squared array : {square_sort(arr)}")


if __name__ == '__main__':
    main()
