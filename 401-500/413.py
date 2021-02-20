class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        step, count, ans = A[1]-A[0], 1, 0
        for i in range(2,n):
            if A[i] - A[i-1] == step:
                count += 1
            else:
                if count > 1:
                    ans += count*(count-1)/2
                step = A[i]-A[i-1]
                count = 1
        if count > 1:
            ans += count*(count-1)/2
        return ans
