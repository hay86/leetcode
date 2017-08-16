class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.comb(nums, 0, ans, len(nums)-1)
        return ans
        
    def comb(self, nums, k, ans, K):
        if k == K:
            ans.append(list(nums))
        else:
            s = set()
            for i in range(k,K+1):
                if nums[i] in s:
                    continue
                else:
                    s.add(nums[i])
                if nums[i] != nums[k]:
                    tmp = nums[k]
                    nums[k] = nums[i]
                    nums[i] = tmp
                self.comb(nums, k+1, ans, K)
                if nums[i] != nums[k]:
                    nums[i] = nums[k]
                    nums[k] = tmp
