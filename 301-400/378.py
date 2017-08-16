import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        arr = []
        for i in range(n):
            heapq.heappush(arr, (matrix[0][i], 0, i))
        while k > 0:
            v, i, j = heapq.heappop(arr)
            if i+1 < n:
                heapq.heappush(arr, (matrix[i+1][j], i+1, j))
            k -= 1
        return v
