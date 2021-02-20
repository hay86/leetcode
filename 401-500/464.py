class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.cache = {}
        return self._canIWin(tuple(range(1, maxChoosableInteger + 1)), desiredTotal)

    def _canIWin(self, nums, desiredTotal):
        if nums in self.cache:
            return self.cache[nums]
        if nums[-1] >= desiredTotal:
            self.cache[nums] = True
            return True
        for i in range(len(nums)):
            if not self._canIWin(nums[:i] + nums[i + 1:], desiredTotal - nums[i]):
                self.cache[nums] = True
                return True
        self.cache[nums] = False
        return False
