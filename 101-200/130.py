class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0]) if n > 0 else 0
        for i in range(n):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, n, m)
            if board[i][m-1] == 'O':
                self.dfs(board, i, m-1, n, m)
        for j in range(m):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, n, m)
            if board[n-1][j] == 'O':
                self.dfs(board, n-1, j, n, m)
        for i in range(n):
            for j in range(m):
                if board[i][j] == '0':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
    def dfs(self, board, i, j, n, m):
        q = [(i*100000+j)]
        while q:
            k = q.pop()
            i, j = k/100000, k%100000
            board[i][j] = '0'
            if i+1 < n and board[i+1][j] == 'O':
                q.append((i+1)*100000+j)
            if i-1 >= 0 and board[i-1][j] == 'O':
                q.append((i-1)*100000+j)
            if j+1 < m and board[i][j+1] == 'O':
                q.append(i*100000+j+1)
            if j-1 >= 0 and board[i][j-1] == 'O':
                q.append(i*100000+j-1)
