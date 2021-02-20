class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        ret = []
        t = 0
        for i in range(n):
            t += nums[i]
            ret.append(t)
        for i in range(1,m):
            ret2 = [max(ret[0],nums[i])]
            for j in range(i+1,n):
                post, local = 0, 2147483647
                for k in range(j,-1,-1):
                    post += nums[k]
                    if post > local:
                        break
                    local = min(local, max(post,ret[k-i]))
                ret2.append(local)
            ret = ret2
        return ret[-1]
                
