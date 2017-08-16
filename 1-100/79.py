class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.s = len(word)
        if self.s == 0:
            return True
        self.h = len(board)
        self.w = len(board[0]) if self.h > 0 else 0
        if self.h == 0 or self.w == 0:
            return False
        self.arr = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(self.h):
            for j in range(self.w):
                if self.dfs(board, word, 0, i, j):
                    return True
        return False
        
    def dfs(self, board, word, i, x, y):
        if board[x][y] != word[i]:
            return False
        if i == self.s-1:
            return True
        board[x][y] = '#'
        for dx, dy in self.arr:
            if -1 < x+dx < self.h and -1 < y+dy < self.w and self.dfs(board, word, i+1, x+dx, y+dy):
                return True
        board[x][y] = word[i]
        return False
                    
                
