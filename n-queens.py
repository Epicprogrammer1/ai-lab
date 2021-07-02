"""
1.	Implement the solution for n-queens problem. 
"""
def canBePlaced(board,row,col,n):
    for i in range(col):
        if(board[row][i]==1):
            return False
    for i, j in zip(range(row, -1, -1),range(col, -1, -1)):
        if(board[i][j]==1):
            return False
    for i, j in zip(range(row, n, 1),range(col, -1, -1)):
        if(board[i][j]==1):
            return False
    return True
        


def solveNQueens(board,col,n):
    if(col>=n):
        return True
    for i in range(0,n):
        if canBePlaced(board,i,col,n):
            board[i][col]=1
            if((solveNQueens(board,col+1,n))==True):
                return True
        board[i][col]=0
    return False
    


n=int(input("Enter the value of n"))
board=[]
for i in range(0,n):
    li=[]
    for j in range(0,n):
        li.append(0)
    board.append(li)
#now we have the n*n chess board where no queen is placed;
#now call the function to place the queens;
if((solveNQueens(board,0,n))==False):
    print(n,"Queens combination is not possible\n")
else:
    #need to print the board;
    for i in range(0,n):
        for j in range(0,n):
            print(board[i][j],end=" ")
        print("\n")
"""
Output:
Enter the value of n8
1 0 0 0 0 0 0 0 

0 0 0 0 0 0 1 0 

0 0 0 0 1 0 0 0 

0 0 0 0 0 0 0 1 

0 1 0 0 0 0 0 0 

0 0 0 1 0 0 0 0 

0 0 0 0 0 1 0 0 

0 0 1 0 0 0 0 0
"""
