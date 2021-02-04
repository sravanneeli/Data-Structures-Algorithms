def max_sum(A, b):
    arr = A[:b]
    val = sum(arr)
    ans = val
    for _ in range(b):
        rmv = arr.pop()
        add = A.pop()
        val = val - rmv + add
        ans = max(val, ans)

    return ans


def main():
    A = [5, -2, 3, 1, 2]
    b = 3
    print(f"Max sum possible: {max_sum(A, b)}")


if __name__ == '__main__':
    main()
