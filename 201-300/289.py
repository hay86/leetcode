class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        coord = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                dead = 0
                live = 0
                for x,y in coord:
                    if 0<=i+x<n and 0<=j+y<m:
                        if board[i+x][j+y] % 2 == 0:
                            dead += 1
                        else:
                            live += 1
                if board[i][j] == 0:
                    if live == 3:
                        board[i][j] = 2
                else:
                    if live < 2 or live > 3:
                        board[i][j] = 3
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
