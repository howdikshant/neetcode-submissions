class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        
        
        box = set()

        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j]) 

        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] != ".": 
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
        
        for boxrow in range(0,9,3):
            for boxcol in range(0,9,3):
                box = set()
                for i in range(3):
                    for j in range(3):

                        val = board[boxrow + i][boxcol + j]
                        if val != ".":
                            if val in box:
                                return False
                            box.add(val)
        return True
