"""
You are given a string S, and you have to find all the amazing substrings of S.

Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
"""


def solve(A):
    count = 0
    n = len(A)
    ovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    mod = 10003
    for i in range(n):
        if A[i] in ovels:
            count = (count + (n-i)) % mod

    return count % mod

def main():
    A = 'aEi'
    print(solve(A))

if __name__ == '__main__':
    main()
    