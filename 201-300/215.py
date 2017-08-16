class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            c = nums[l]
            j = l
            for i in range(l+1, r+1):
                if nums[i] >= c:
                    j += 1
                    if i != j:
                        tmp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = tmp
            nums[l] = nums[j]
            nums[j] = c
            if j-l == k-1:
                break
            elif j-l > k-1:
                r = j-1
            else:
                k -= (j-l+1)
                l = j+1
        return nums[j]
