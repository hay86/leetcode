class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask, answer = 0, 0
        for i in range(31,-1,-1):
            mask = mask | 1<<i
            prefix = {n&mask for n in nums}
            tmp = answer | 1<<i
            for p in prefix:
                if tmp^p in prefix:
                    answer = tmp
                    break
        return answer
