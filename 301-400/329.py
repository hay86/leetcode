class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        w = len(matrix)
        if w == 0:
            return 0
        h = len(matrix[0])
        size = w*h
        degree = [0]*size
        m = {}
        for i in range(w):
            for j in range(h):
                v = matrix[i][j]
                x = i*h+j
                if i-1 >= 0 and matrix[i-1][j] > v:
                    y = x-h
                    degree[y] += 1
                    if x not in m:
                        m[x] = []
                    m[x].append(y)
                if j-1 >= 0 and matrix[i][j-1] > v:
                    y = x-1
                    degree[y] += 1
                    if x not in m:
                        m[x] = []
                    m[x].append(y)
                if i+1 < w and matrix[i+1][j] > v:
                    y = x+h
                    degree[y] += 1
                    if x not in m:
                        m[x] = []
                    m[x].append(y)
                if j+1 < h and matrix[i][j+1] > v:
                    y = x+1
                    degree[y] += 1
                    if x not in m:
                        m[x] = []
                    m[x].append(y)
        dist = [0]*size
        loop = []
        for i in range(size):
            if degree[i] == 0:
                dist[i] = 1
                loop.append(i)
        k = 0
        size = len(loop)
        while k < size:
            i = loop[k]
            if i in m:
                for j in m[i]:
                    degree[j] -= 1
                    if degree[j] == 0:
                        loop.append(j)
                        size += 1
                    if dist[j] < dist[i]+1:
                        dist[j] = dist[i]+1
            k += 1
        return max(dist)
        
