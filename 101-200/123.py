class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        arr = [0]*n
        m = prices[0]
        ret = 0
        for i in range(1, n):
            x = prices[i] - m
            if x < 0:
                m = prices[i]
            elif x > ret:
                ret = x
            arr[i] = ret
        m = prices[-1]
        ret = 0
        for i in range(-2, -n-1, -1):
            x = m - prices[i]
            if x < 0:
                m = prices[i]
            elif x > ret:
                ret = x
            arr[i] += ret
        return max(arr)
