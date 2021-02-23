import math


def isPower(num):
    if num <= 1:
        return 1
    for i in range(2, int(math.sqrt(num))):
        p = math.log(num, i)
        p = float(f"{p:.5f}")
        if p % 2 == 0 or (p + 1) % 2 == 0:
            return 1

    return 0


def main():
    num = 1001
    print(isPower(num))


if __name__ == '__main__':
    main()
