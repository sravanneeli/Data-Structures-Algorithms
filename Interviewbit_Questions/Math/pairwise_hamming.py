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
    for i in range(32):
        x = 0
        for num in A:
            if num & (1 << i):
                x += 1
        dist += 2 * x * (n - x)
        dist = dist % mod
    return dist


def main():
    A = [2, 4, 6]
    print(hammingDistance(A))


if __name__ == '__main__':
    main()
