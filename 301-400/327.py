class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        arr = [0]
        total = 0
        for n in nums:
            total += n
            arr.append(total)
        arr, cnt = self.mergesort(arr, lower, upper)
        return cnt
        
    def mergesort(self, arr, lower, upper):
        if len(arr) <= 1:
            return arr, 0
        m = int(len(arr)/2)
        arr1, cnt1 = self.mergesort(arr[:m], lower, upper)
        arr2, cnt2 = self.mergesort(arr[m:], lower, upper)
        cnt = cnt1 + cnt2
        arr = []
        p1, p2 = 0, 0
        while p1<len(arr1) and p2<len(arr2):
            tmp = arr2[p2] - arr1[p1]
            if tmp < lower:
                p2 += 1
            elif tmp > upper:
                p1 += 1
            else:
                val = arr1[p1] + upper
                i, j = p2, len(arr2)-1
                while i<=j:
                    k = int(i+j)/2
                    if arr2[k] <= val:
                        i = k+1
                    else:
                        j = k-1
                cnt += j-p2+1
                p1 += 1
        p1, p2 = 0, 0
        while p1<len(arr1) and p2<len(arr2):
            if arr1[p1] <= arr2[p2]:
                arr.append(arr1[p1])
                p1 += 1
            else:
                arr.append(arr2[p2])
                p2 += 1
        while p1<len(arr1):
            arr.append(arr1[p1])
            p1 += 1
        while p2<len(arr2):
            arr.append(arr2[p2])
            p2 += 1
        return arr, cnt
        
