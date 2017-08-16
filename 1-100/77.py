class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            k = n
        arr = range(1,k+1)
        ret = []
        self.dfs(arr, ret, n+1, k-1)
        return ret
        
    def dfs(self, arr, ret, n, k):
        ret.append(list(arr))
        size = n - arr[k]
        for i in range(1, size):
            arr[k] += i
            self.dfs(arr, ret, arr[k], k-1)
            arr[k] -= i
