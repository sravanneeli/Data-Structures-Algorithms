import sys
from bisect import bisect_right


def binSearch(mat, min_ele, max_ele, upperBound):
    start = min_ele
    end = max_ele
    
    while start < end:
        mid = start + (end-start) // 2
        cnt = 0
        for row in mat:
            cnt += bisect_right(row, mid)
        if cnt > upperBound:
            end = mid
        else:
            start = mid + 1
    return start
            

def findMedian(mat):
    m, n = len(mat), len(mat[0])
    mat_min = sys.maxsize
    mat_max = -sys.maxsize 
    for row in range(m):
        mat_min = min(mat_min, mat[row][0])
        mat_max = max(mat_max, mat[row][-1])
    
    upperBound = (m * n) // 2
    return binSearch(mat, mat_min, mat_max, upperBound)

def main():
    A = [[1, 3, 5],
         [2, 6, 9],
         [3, 6, 9]]
    print(f"Median of matrix A is: {findMedian(A)}")
    
if __name__ == '__main__':
    main()