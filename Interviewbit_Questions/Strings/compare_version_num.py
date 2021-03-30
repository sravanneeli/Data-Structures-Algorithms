""""
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""



def compare_version(a, b):
    m, n = len(a), len(b)
    i, j, = 0, 0
    zero = ord('0')
    ver1, ver2 = 0, 0
    while i < m or j < n:
        while i < m and a[i] != '.':
            ver1 += ver1*10 + ord(a[i]) - zero 
            i += 1

        while j < n and b[j] != '.':
            ver2 += ver2*10 + ord(b[j]) - zero
            j += 1
        
        if ver1 > ver2: return 1
        elif ver1 < ver2: return -1

        ver1, ver2 = 0, 0

        i += 1
        j += 1        

    return 0


def main():
    a = '1.2.3'
    b = '1.2.4'
    print(compare_version(a, b))

if __name__ == '__main__':
    main()
    


