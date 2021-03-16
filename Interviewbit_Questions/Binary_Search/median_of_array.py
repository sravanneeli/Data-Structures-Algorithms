import sys

def findMedianSortedArrays(A, B):
    if len(A) >  len(B):
        A, B = B, A
    x = len(A)
    y = len(B)
    low = 0
    high = x
    while low <= high:
        partitionx = (low + high) // 2
        partitiony = ((x + y + 1) // 2) - partitionx
        maxleftx = None if partitionx == 0 else A[partitionx-1]
        minrightx = sys.maxsize if partitionx == x else A[partitionx]
        
        maxlefty = None if partitiony == 0 else B[partitiony-1]
        minrighty = sys.maxsize if partitiony == y else B[partitiony]
        
        if maxleftx <= minrighty and maxlefty <= minrightx:
            if (x + y) % 2 == 0:
                return (max(maxleftx, maxlefty) + min(minrightx, minrighty)) / 2.0
            else:
                return float(max(maxleftx, maxlefty))
        elif maxleftx > minrighty:
            high = partitionx - 1
        else:
            low = partitionx + 1
    return None

def main():
    A = [1, 4, 5]
    B = [2, 3]
    print(findMedianSortedArrays(A, B))

if __name__ == '__main__':
    main()
    