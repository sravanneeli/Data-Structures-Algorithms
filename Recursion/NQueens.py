import copy
global n
n = 4 # Board size

def print_board(board):
    for i in range(n): 
        for j in range(n):
            print(board[i][j], end = " ")
        print("\n")
    print("\n") 

def checksafe(board,row, col):
    # check from left to present column
    for i in range(col):
        if board[row][i]:
            return False
    
    # Check diagonal positions
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        j -= 1
        i -= 1
    
    i = row
    j = col
    while j >= 0 and i < 4:
        if board[i][j]:
            return False
        i += 1
        j -= 1
    return True

def NQueen(board, col, valid_sol):
    if col == n:
        temp = copy.deepcopy(board)
        valid_sol.append(temp)
        return True
    res = False
    for i in range(n):
        # checking row, col and diagonal positions so that we can place without any clashes
        if checksafe(board, i, col): 
            # Place the queen 
            board[i][col] = 1
            # Recursion call for each row position and then recursion for column
            res = NQueen(board, col+1, valid_sol) or res
            # if plaicng queen in board[i][col] doesn't lead
            # to a solution, then remove from that position.
            board[i][col] = 0
    return res


def main():
    board = [[0 for j in range(n)] 
                for i in range(n)]
    valid_sol = []

    if (NQueen(board, 0, valid_sol) == False): 
        print("Solution does not exist")
    else:
        print("Total Number of Solutions: {}".format(len(valid_sol)))
        for i in range(len(valid_sol)):
            print_board(valid_sol[i])

if __name__ == "__main__":
    main()