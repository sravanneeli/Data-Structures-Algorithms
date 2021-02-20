def get_bin(a):
    i = 1 << 31
    bits = []
    while i > 0:
        if a & i != 0:
            bits.append(1)
        else:
            bits.append(0)
        i //= 2

    return bits


def hammingDistance(A):
    mod = 1000000007
    n = len(A)
    if n == 1:
        return 0
    new = []
    for i in range(n):
        new.append(get_bin(A[i]))
    dist = 0
    for i in range(31, -1, -1):
        x, y = 0, 0
        for j in range(n):
            if new[j][i]:
                x += 1
            else:
                y += 1

        dist += 2 * x * y
        dist = dist % mod
    return dist


def main():
    A = [2, 4, 6]
    print(hammingDistance(A))


if __name__ == '__main__':
    main()
