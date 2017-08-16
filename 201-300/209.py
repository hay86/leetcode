class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ret = 2147483647
        arr = []
        arrsum = 0
        for n in nums:
            arr.append(n)
            arrsum += n
            if arrsum >= s:
                while len(arr) > 0 and arrsum - arr[0] >= s:
                    arrsum -= arr[0]
                    arr.pop(0)
                if ret > len(arr):
                    ret = len(arr)
        return ret if ret != 2147483647 else 0
