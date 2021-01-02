def merge(A, B):
    m = len(A)
    n = len(B)
    C = []
    i,j = 0, 0
    while i < m and j < n:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    for k in range(i, m):
        C.append(A[k])
    for k in range(j, n):
        C.append(B[k])

    return C

def main():
    A = [3, 8, 16, 20, 23]
    B = [4, 10, 12, 22, 23]
    C = merge(A, B)
    print("Merged Array", C)

