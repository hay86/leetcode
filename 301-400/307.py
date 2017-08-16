class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.size = len(nums)
        self.sums = [0]*(self.size+1)
        for i in range(self.size):
            j = i + 1
            while j <= self.size :
                self.sums[j] += nums[i]
                j += j&(-j)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        add = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i <= self.size:
            self.sums[i] += add
            i += i&(-i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        ret, j = 0, j+1 
        while j > 0:
            ret += self.sums[j]
            j -= j&(-j)
        while i > 0:
            ret -= self.sums[i]
            i -= i&(-i)
        return ret


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
