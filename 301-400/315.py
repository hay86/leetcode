class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        arr = []
        ret = [0]*size
        for i in range(size):
            arr.append((nums[i],i))
        self.mergesort(arr, ret)
        return ret
        
    def mergesort(self, arr, ret):
        s = len(arr)
        if s <= 1:
            return arr
        arr1 = self.mergesort(arr[:int(s/2)], ret)
        arr2 = self.mergesort(arr[int(s/2):], ret)
        s1, s2 = len(arr1), len(arr2)
        i, j, k = 0, 0, 0
        while i < s1 and j < s2:
            if arr1[i] <= arr2[j]:
                arr[k] = arr2[j]
                k += 1
                j += 1
            else:
                ret[arr1[i][1]] += s2-j
                arr[k] = arr1[i]
                k += 1
                i += 1
        if i < s1:
            while i < s1:
                arr[k] = arr1[i]
                k += 1
                i += 1
        elif j < s2:
            while j < s2:
                arr[k] = arr2[j]
                k += 1
                j += 1
        return arr    
