def pow(x, n, d):
    res = 1 % d
    while n > 0:
        if n & 1:
            res = (res * x) % d
        x = x**2 % d
        n >>= 1
    return res

def main():
    x, n, d = 2, 10, 3
    print(pow(x, n, d))

if __name__ == "__main__":
    main()