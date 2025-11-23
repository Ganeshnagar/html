N = 4

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col):
   # Check vertical and horizontal  
   for i in range(N):
     if board[row][i] == 1 or board[i][col] == 1:
       return False
   # Check diagonals
   for i,j in zip(range(row,-1,-1), range(col,-1,-1)): 
     if board[i][j] == 1:
       return False
   return True
   
def solveNQueens(board, col):   
  if col >= N:
    return True
  for i in range(N):

    if is_safe(board, i, col):
      board[i][col] = 1
      if solveNQueens(board, col + 1) == True:
        return True

      board[i][col] = 0

  return False

board = [[0] * N for _ in range(N)]

if solveNQueens(board, 0) == False:
  print ("Solution does not exist")
     
print_board(board)
