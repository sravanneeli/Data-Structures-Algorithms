def count_trail_zeros(n):
    i = 5
    count = 0
    while (n / i >= 1):
        count += int(n / i)
        i *= 5
    return count


def main():
    n = int(input("Enter a number: "))
    print("Number of trailing zeros of given number factorial: ", count_trail_zeros(n))


if __name__ == "__main__":
    main()
