def findPerm(A, B):
    arr = []
    m = 1
    n = A
    for i in range(len(B)):
        if B[i] == 'D':
            arr.append(max(m, n))
            n -= 1
        if B[i] == 'I':
            arr.append(min(m, n))
            m += 1
    arr.append(m)
    return arr
    
def main():
    A = 4
    B = 'III'
    print(f'{findPerm(A, B)}')


if __name__ == "__main__":
    main()