class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [1,2,3,4,5,6,7,8,9]
        size = len(candidates)
        ret = []
        self.dfs(candidates, k, n, ret, [], size, 0)
        return ret
        
    def dfs(self, candidates, k, n, ret, ans, size, i):
        while i < size:
            c = candidates[i]
            if c == n and len(ans) == k-1:
                ret.append(ans+[c])
            elif c < n and len(ans) < k-1:
                ans.append(c)
                self.dfs(candidates, k, n-c, ret, ans, size, i+1)
                ans.pop()
            elif c > n:
                break
            i += 1
