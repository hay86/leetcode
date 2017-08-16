class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        ret = 0
        size = len(prices)
        if k <= 0 or size <= 1:
            return ret
        diff, maxK = [0]*size, 0
        for i in range(1, size):
            diff[i] = prices[i] - prices[i-1]
            if diff[i] > 0:
                ret += diff[i]
                maxK += 1
        if maxK <= k:
            return ret
        prev_global, next_global = [0]*size, [0]*size
        for i in range(k):
            local = 0
            for j in range(i+1,size):
                next_global[j] = max(next_global[j-1], prev_global[j-1]+diff[j], local+diff[j])
                local = max(prev_global[j-1]+diff[j], local+diff[j])
            prev_global, next_global = next_global, [0]*size
        return prev_global[-1]
