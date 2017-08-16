class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        arr = [-1]*n
        ans = []
        self.dfs(arr, 0, n, ans)
        return ans
        
    def dfs(self, arr, i, n, ans):
        if i == n:
            ans.append(self.draw(arr, n))
        else:
            for j in range(n):
                arr[i] = j
                if self.valid(arr, i+1):
                    self.dfs(arr, i+1, n, ans)
            arr[i] = -1
    
    def valid(self, arr, n):
        for i in range(1,n):
            for j in range(i):
                if arr[i] == arr[j] or abs(arr[i]-arr[j]) == i-j:
                    return False
        return True
    
    def draw(self, arr, n):
        ret = [['.']*n for i in range(n)]
        for i in range(n):
            ret[i][arr[i]] = 'Q'
            ret[i] = ''.join(ret[i])
        return ret
        
