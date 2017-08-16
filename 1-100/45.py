class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            return 0
        if nums[0] >= size-1:
            return 1
        extend = nums[0]
        cur, ret = 0, 0
        while True:
            extend2 = extend
            while cur <= extend:
                if cur + nums[cur] > extend2:
                    extend2 = cur + nums[cur]
                cur += 1
            ret += 1
            if extend == extend2 or extend2 >= size-1:
                break
            extend = extend2
        return ret + 1
            
                
