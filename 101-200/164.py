class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return 0
        min_n, max_n = min(nums), max(nums)
        dist = max_n - min_n
        if dist == 0:
            return 0
        num = int(dist/(size-1)) if dist%(size-1) == 0 else int(dist/(size-1))+1
        buck = int((dist+1)/num) if (dist+1)%num == 0 else int((dist+1)/num)+1
        min_arr, max_arr = [2147483647]*buck, [-2147483648]*buck
        for n in nums:
            buck_id = int((n-min_n)/num)
            if min_arr[buck_id] > n:
                min_arr[buck_id] = n
            if max_arr[buck_id] < n:
                max_arr[buck_id] = n
        ret, i, j = 0, 0, 1
        while j < buck:
            if min_arr[j] == 2147483647:
                j += 1
            else:
                if min_arr[j] - max_arr[i] > ret:
                    ret = min_arr[j] - max_arr[i]
                i = j
                j += 1
        return ret
