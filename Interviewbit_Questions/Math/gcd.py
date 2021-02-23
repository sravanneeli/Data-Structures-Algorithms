def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(a % b, b)


def main():
    a, b = 54, 190
    print(gcd(a, b))


if __name__ == '__main__':
    main()
