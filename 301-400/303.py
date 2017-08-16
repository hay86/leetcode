class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.size = len(nums)
        self.sums = [0]
        for i in range(self.size):
            self.sums.append(self.sums[i]+nums[i])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0:
            i = 0
        if j >= self.size:
            j = self.size - 1
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
