"""
Problem Description

Given a string A consisting of lowercase characters.

We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.
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
    print(len(pat) - compute_lps(pat[::-1] + '$' + pat)[-1])


if __name__ == '__main__':
    main()
    