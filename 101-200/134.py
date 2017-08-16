class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ssum = 0
        smin = 2147483647
        spos = -1
        size = len(gas)
        for i in range(size):
            ssum += gas[i] - cost[i]
            if ssum < smin:
                smin = ssum
                spos = i
        return -1 if ssum < 0 else (spos+1)%size
