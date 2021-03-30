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
    


