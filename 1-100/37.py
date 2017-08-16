class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board, 0)
    
    def dfs(self, board, c):
        i, j = int(c/9), c%9
        while c < 81 and board[i][j] != '.':
            c += 1
            i, j = int(c/9), c%9
        if c >= 81:
            return True
        b = [False]*10
        x, y = int(i/3)*3, int(j/3)*3
        for k in range(9):
            if board[i][k] != '.':
                b[int(board[i][k])] = True
            if board[k][j] != '.':
                b[int(board[k][j])] = True
            xx, yy = int(k/3), k%3
            if board[x+xx][y+yy] != '.':
                b[int(board[x+xx][y+yy])] = True
        for k in range(1,10):
            if not b[k]:
                board[i][j] = str(k)
                if self.dfs(board, c+1):
                    return True
        board[i][j] = '.'
        return False
            
