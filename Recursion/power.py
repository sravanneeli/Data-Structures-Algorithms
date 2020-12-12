def power(m, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(m*m, n/2)
    else:
        return power(m*m, (n-1)/2)


def main():
    m, n = 3, 4
    print("{} to the power of {} is: {}".format(m ,n, pow(m, n)))

if __name__ == "__main__":
    main()