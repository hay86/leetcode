import heapq
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        r = len(heightMap)
        if r == 0:
            return 0
        c = len(heightMap[0])
        if c == 0:
            return 0
        q = []
        visit = [[False]*c for i in range(r)]
        for i in range(c):
            heapq.heappush(q, (heightMap[0][i], 0, i))
            heapq.heappush(q, (heightMap[r-1][i], r-1, i))
            visit[0][i], visit[r-1][i] = True, True
        for i in range(1, r-1):
            heapq.heappush(q, (heightMap[i][0], i, 0))
            heapq.heappush(q, (heightMap[i][c-1], i, c-1))
            visit[i][0], visit[i][c-1] = True, True
        ans = 0
        while len(q) > 0:
            h,i,j = heapq.heappop(q)
            stack = [(i,j)]
            while len(stack) > 0:
                i,j = stack.pop()
                ans += h - heightMap[i][j]
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    idx, jdy = i+dx, j+dy
                    if 0<idx<r-1 and 0<jdy<c-1 and not visit[idx][jdy]:
                        visit[idx][jdy] = True
                        if h > heightMap[idx][jdy]:
                            stack.append((idx, jdy))
                        else:
                            heapq.heappush(q, (heightMap[idx][jdy], idx, jdy))
        return ans
        
