"""
Problem Description

Given a positive integer A, return its corresponding column title as appear in an Excel sheet.
"""


def convertToTitle(num):
    temp = ''
    alpha_dict = {i + 1: chr(ord('A') + i) for i in range(26)}

    while num > 0:
        digit = num % 26
        if digit == 0:
            temp += 'Z'
            num = (num // 26) - 1
        else:
            temp += alpha_dict[digit]
            num //= 26

    return temp[::-1]


def main():
    num = 731
    print(f"Column title: {convertToTitle(num)}")


if __name__ == '__main__':
    main()
