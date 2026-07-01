class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        for i in range(len(board)):
            s = set()
            for j in range(len(board[0])):
                if board[j][i] != '.':
                    if board[j][i] in s:
                        return False
                    s.add(board[j][i])

        for boxRow in range(3):
            for boxCol in range(3):
                s = set()
                
                
                startRow = boxRow * 3
                startCol = boxCol * 3

                for r in range(3):
                    for c in range(3):
                        if board[r+startRow][c + startCol] != ".":
                            if board[r+startRow][c + startCol] in s:
                                return False
                            s.add(board[r+startRow][c + startCol])
        return True


        
