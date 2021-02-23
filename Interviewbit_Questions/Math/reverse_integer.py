def reverse_int(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return rev


def main():
    num = 1002
    print(f"Reverse of the given integer is: {reverse_int(num)}")


if __name__ == '__main__':
    main()
