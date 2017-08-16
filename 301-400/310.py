class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if len(edges) == 0:
            return range(n)
        g = {}
        for i,j in edges:
            if i not in g:
                g[i] = set()
            if j not in g:
                g[j] = set()
            g[i].add(j)
            g[j].add(i)
        e1 = self.bfs(g, n, edges[0][0])
        e2, p2 = self.bfs2(g, n, e1)
        a, b = len(p2), int(len(p2)/2)
        return p2[b-1:b+1] if a%2 == 0 else p2[b:b+1]

    def bfs(self, g, n, i):
        q = [i]
        v = [False] * n
        v[i] = True
        while len(q) > 0:
            j = q.pop(0)
            for k in g[j]:
                if not v[k]:
                    v[k] = True
                    q.append(k)
        return j
        
    def bfs2(self, g, n, i):
        q = [(i,[i])]
        v = [False] * n
        v[i] = True
        while len(q) > 0:
            j, p = q.pop(0)
            for k in g[j]:
                if not v[k]:
                    v[k] = True
                    q.append((k, p+[k]))
        return j, p
