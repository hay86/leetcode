class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        w = len(matrix)
        if w == 0:
            return 0
        h = len(matrix[0])
        v = [0]*(h+1)
        ret = 0
        for i in range(w):
            for j in range(h):
                if matrix[i][j] == '0':
                    v[j] = 0
                else:
                    v[j] += 1
            stack = []
            val = 0
            for j in range(h+1):
                while len(stack) > 0 and v[stack[-1]] > v[j]:
                    k = stack.pop()
                    l = -1 if len(stack) == 0 else stack[-1]
                    val = max(val, v[k]*(j-l-1))
                stack.append(j)
            if val > ret:
                ret = val
        return ret
