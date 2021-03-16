"""
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...
"""

def count(s):
    c = 1
    n = len(s)
    i = 1
    temp = ''
    while i < n:
        if s[i-1] == s[i]:
            c += 1
        else:
            temp += str(c) + s[i-1]
            c = 1
        i += 1
    temp += str(c) + s[i-1]
    return temp


def countAndSay(A):
    if A == 1:
        return '1'
    if A == 2:
        return '11'
    s = '11'
    for i in range(3, A+1):
        s = count(s)
    return s

def main():
    A = 5
    print(f"Sequence :{countAndSay(A)}")

if __name__ == '__main__':
    main()
    