class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)
        if target%2 == 1:
            return False
        target = target/2
        size = len(nums)
        matrix = [[0]*(size+1) for i in range(target+1)]
        for i in range(1,target+1):
            for j in range(1,size+1):
                matrix[i][j] = matrix[i][j-1]
                if nums[j-1] <= i:
                    matrix[i][j] = max(matrix[i][j], matrix[i-nums[j-1]][j-1]+nums[j-1])
        return matrix[target][size] == target
                
            
