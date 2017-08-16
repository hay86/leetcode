class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.comb(nums, 0, ans)
        return ans
        
    def comb(self, nums, k, ans):
        n = len(nums)
        if k == n-1:
            ans.append(list(nums))
        else:
            for i in range(k,n):
                tmp = nums[k]
                nums[k] = nums[i]
                nums[i] = tmp
                self.comb(nums, k+1, ans)
                nums[i] = nums[k]
                nums[k] = tmp
