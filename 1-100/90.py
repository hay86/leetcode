class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        self.dfs([False]*len(nums), nums, ret, 0)
        return ret
        
    def dfs(self, arr, nums, ret, i):
        if i == len(arr):
            tmp = []
            for j in range(len(arr)):
                if arr[j]:
                    tmp.append(nums[j])
            ret.append(tmp)
            return
        self.dfs(arr, nums, ret, i+1)
        if i==0 or nums[i] != nums[i-1] or arr[i-1]:
            arr[i] = True
            self.dfs(arr, nums, ret, i+1)
            arr[i] = False
