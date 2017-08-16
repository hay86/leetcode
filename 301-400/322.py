class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ret = [-1]*(amount+1)
        ret[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0 and ret[i-c] >= 0 and (ret[i] == -1 or ret[i-c]+1 < ret[i]):
                    ret[i] = ret[i-c]+1
        return ret[-1]
