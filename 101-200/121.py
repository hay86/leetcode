class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        if len(prices) > 0:
            min = prices[0]
            size = len(prices)
            for i in range(1,size):
                if prices[i] < min:
                    min = prices[i]
                if prices[i] - min > ret:
                    ret = prices[i] - min
        return ret
