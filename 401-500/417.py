class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        if r == 0:
            return []
        c = len(matrix[0])
        if c == 0:
            return []
        
        stack = [(0,0)]
        visit1 = set(stack)
        for i in range(1,r):
            stack.append((i,0))
            visit1.add((i,0))
        for i in range(1,c):
            stack.append((0,i))
            visit1.add((0,i))
        self.bfs(stack, visit1, matrix, r, c)
        
        stack = [(r-1,c-1)]
        visit2 = set(stack)
        for i in range(r-1):
            stack.append((i,c-1))
            visit2.add((i,c-1))
        for i in range(c-1):
            stack.append((r-1,i))
            visit2.add((r-1,i))
        self.bfs(stack, visit2, matrix, r, c)
        
        return list(visit1.intersection(visit2))
        
        
    def bfs(self, stack, visit, matrix, r, c):
        while len(stack) > 0:
            i,j = stack.pop()
            h = matrix[i][j]
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                idx, jdy = i+dx, j+dy
                if 0<=idx<r and 0<=jdy<c and (idx, jdy) not in visit and matrix[idx][jdy] >= h:
                    stack.append((idx, jdy))
                    visit.add((idx, jdy))
