from functools import cmp_to_key


def largestNumber(A):
    if all(A) == 0:
        return '0'
    A = list(map(str, A))
    A.sort(key=cmp_to_key(lambda x, y: 1 if x + y <= y + x else -1))
    return "".join(A)


def main():
    A = [3, 30, 34, 5, 9]
    print(f"Largest Number possible is {largestNumber(A)}")


if __name__ == '__main__':
    main()
