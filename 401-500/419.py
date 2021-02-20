class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        r = len(board)
        if r == 0:
            return 0
        c = len(board[0])
        if c == 0:
            return 0
        ans = 0
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X':
                    if i-1>=0 and board[i-1][j] == 'X':
                        continue
                    if j-1>=0 and board[i][j-1] == 'X':
                        continue
                    ans +=1
        return ans
