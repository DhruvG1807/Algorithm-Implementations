#Insert N queens in an NXN board such that no queen attacks the other
import numpy


def issafe(board,row,column):           #check if queen insertion is safe
    
    for i in range(len(board)):
        if board[row][i] == 1:           #check for queen in same row
            #print("ROW")
            return False
            
        if board[i][column] == 1:        #check for queen in same column
            #print("column")
            return False
    
    for i in range(1,len(board)-row):    #check diagonals below specified position
        if (column+i)<len(board) and (row+i)<len(board):
            if board[row+i][column+i] == 1:
                #print("below right diagonals")
                return False
        
        if (column-i)>=0 and (row+i)<len(board):
            if board[row+i][column-i] == 1:
                #print("below left diagonals")
                return False
    
    for i in range(1,row+1):            #check diagonals above specified position
        if (column-i)>=0 and (row-i)>=0:
            if board[row-i][column-i] == 1:
                #print("above left diagonals")
                return False
        
        if (column+i)<len(board) and (row-i)<len(board):        
            if board[row-i][column+i] == 1:
                #print("above right diagonals")
                return False
            
    return True            

def nqueen(board,row):
    #print(board)
    if row == len(board):               # N queens are inserted
        return True
    
    for col in range(len(board)):
        #print(row,col,issafe(board,row,col))
        if issafe(board,row,col):
            board[row][col] = 1
            #print(board)
            
            if nqueen(board,row+1):
                return True
            
            board[row][col] = 0
    
    return False
    
    
if __name__ == '__main__':
    n = int(input())
    board = []
    for i in range(n):
        board.append([0]*n)
    
    nqueen(board,0)
    print(board)
    