class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size == 0:
            return 0
        contain = [0]*size
        not_contain = [0]*size
        for i in range(1, size):
            tmp = prices[i]-prices[i-1]
            not_contain[i] = max(contain[i-1],not_contain[i-1])
            contain[i] = max(contain[i-1]+tmp,contain[i-3]+tmp if i>=3 else tmp,not_contain[i-2]+tmp if i>=2 else tmp,0)
        return max(contain[size-1],not_contain[size-1])
