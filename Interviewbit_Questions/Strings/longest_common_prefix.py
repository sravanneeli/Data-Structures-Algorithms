"""
Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
"""


def get_common(s1, s2):
    m, n =len(s1), len(s2)
    i, j = 0, 0
    while i < m and j < n:
        if s1[i] != s2[j]:
            break
        i += 1
        j += 1
    return i

def longestCommonPrefix(A):
    n = len(A)
    
    for i in range(1, n):
        A[i] = A[i][:get_common(A[i-1], A[i])]
    
    return A[-1]

def main():
    A = ["abab", "ab", "abcd"]
    print(f"longest commong prefix:{longestCommonPrefix(A)}")

if __name__ == '__main__':
    main()
    