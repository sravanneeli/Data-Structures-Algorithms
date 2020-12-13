def ncr(n, r):
    if r == 0 or r == n:
        return 1
    return ncr(n-1, r-1) + ncr(n-1, r)


def main():
    print(ncr(5, 3))

main()