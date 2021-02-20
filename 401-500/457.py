class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            if -1000 <= nums[i] <= 1000:
                if self.walk(nums, i, n):
                    return True
        return False

    def walk(self, nums, i, n):
        visit = 1001 + i
        while True:
            v = nums[i]
            nums[i] = visit
            j = (i + v) % n
            u = nums[j]
            if u == visit:
                return i != j
            if u > 1000:
                return False
            if u * v < 0:
                return False
            i, v = j, u