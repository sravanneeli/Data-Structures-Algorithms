def rotate(mat):
    N = len(mat)

    for i in range(N//2):
        for j in range(i, N-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[N-1-j][i]
            mat[N-1-j][i] = mat[N-1-i][N-1-j]
            mat[N-1-i][N-1-j] = mat[j][N-1-i]
            mat[j][N-1-i] = temp
    
    

def main():
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8], 
           [9, 10, 11, 12], 
           [13, 14, 15, 16]]
    
    rotate(mat)
    print("New matrix after rotating 90 degrees")
    for i in range(len(mat)):
        print(f"{mat[i]}")


if __name__ == "__main__":
    main()
