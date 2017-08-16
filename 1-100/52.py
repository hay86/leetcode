class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        k, ret = 0, 0
        arr = [-1] * n
        while k >= 0:
            while arr[k] < n-1:
                arr[k] += 1
                if self.pease(arr, k):
                    if k == n-1:
                        ret += 1
                        break
                    k += 1
            arr[k] = -1
            k -= 1
        return ret
    
    def pease(self, arr, k):
        for i in range(k):
            if arr[k] == arr[i] or abs(arr[k]-arr[i]) == k-i:
                return False
        return True
            
