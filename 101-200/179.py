class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if len(nums) == 0:
            return '0'
        nums = [str(x) for x in nums]
        nums.sort(cmp=self.cmp)
        return ''.join(nums) if nums[0] != '0' else '0'
    
    def cmp(self, a,b):
        if a == b:
            return 0
        for i in range(min(len(a),len(b))):
            if a[i] > b[i]:
                return -1
            elif a[i] < b[i]:
                return 1
        return self.cmp(a[i+1:], b) if len(a) > len(b) else self.cmp(a, b[i+1:])
