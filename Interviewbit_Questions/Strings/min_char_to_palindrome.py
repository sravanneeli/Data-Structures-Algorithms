"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.
"""


def compute_lps(pat):
    length = 0
    i = 1 
    n = len(pat)
    lps = [0] * n

    while i < n:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps


def main():
    pat = "aaabaaa"
    print(len(pat) - compute_lps(pat + '$' + pat)[-1])


if __name__ == '__main__':
    main()
    