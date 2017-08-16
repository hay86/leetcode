class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            chk = [False]*10
            for j in range(9):
                if board[i][j] != '.':
                    board[i][j] = int(board[i][j])
                    if not chk[board[i][j]]:
                        chk[board[i][j]] = True
                    else:
                        return False
                        
        for i in range(9):
            chk = [False]*10
            for j in range(9):
                if board[j][i] != '.':
                    if not chk[board[j][i]]:
                        chk[board[j][i]] = True
                    else:
                        return False
                        
        for i in range(0,9,3):
            for j in range(0,9,3):
                chk = [False]*10
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] != '.':
                            if not chk[board[i+k][j+l]]:
                                chk[board[i+k][j+l]] = True
                            else:
                                return False
        return True
