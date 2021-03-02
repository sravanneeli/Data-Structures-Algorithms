"""
Problem Description

Given a column title A as appears in an Excel sheet, return its corresponding column number.
"""


def titleToNumber(A):
    alpha_dict = {chr(ord('A') + i): i + 1 for i in range(26)}
    col_num = 0
    n = len(A)
    for i in range(n - 1, -1, -1):
        col_num += alpha_dict[A[i]] * pow(26, n - i - 1)

    return col_num


def main():
    A = 'ABBC'
    print(f"Column Number: {titleToNumber(A)}")


if __name__ == '__main__':
    main()
