class Solution(object):

    def __init__(self):
        self.block=[0,0]

    def is_empty(self,board):
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==0:
                    self.block[0]=i
                    self.block[1]=j
                    return True
        return False


    def is_row_safe(self,board,row,val):
        for i in range(0,9):
            if board[row][i]==val:
                return False
        return True

    def is_column_safe(self,board,column,val):
        for i in range(0,9):
            if board[i][column]==val:
                return False
        return True

    def is_block_Safe(self,board,row,column,val):
        for i in range(0,3):
            for j in range(0,3):
                if board[row+i][column+j]==val:
                    return False
        return True



    def is_safe(self, board, row, column, i):
        return self.is_row_safe(board, row, i) \
               and self.is_column_safe(board,column,i ) \
               and self.is_block_Safe(board,row-row%3,column-column%3,i)



    def solveSudokuutil(self, board):

        if self.is_empty(board) is False:
            return True
        row=self.block[0]
        column=self.block[1]

        for i in range(1, 10):
            if self.is_safe(board, row, column, i):
                board[row][column] = i

                if self.solveSudokuutil(board) is True:
                    return True

                board[row][column] = 0

        return False



    def solveSudoku(self, board):
        self.solveSudokuutil(board)



board=[[0,0,9,7,4,8,0,0,0],
       [7,0,0,0,0,0,0,0,0],
       [0,2,0,1,0,9,0,0,0],
       [0,0,7,0,0,0,2,4,0],
       [0,6,4,0,1,0,5,9,0],
       [0,9,8,0,0,0,3,0,0],
       [0,0,0,8,0,3,0,2,0],
       [0,0,0,0,0,0,0,0,6],
       [0,0,0,2,7,5,9,0,0]]
x=Solution()
x.solveSudoku(board)

for i in range(0,9):
    print board[i]