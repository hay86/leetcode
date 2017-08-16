class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses == 0:
            return []
        ret = []
        m = [[] for i in range(numCourses)]
        d = [0]*numCourses
        for t,f in prerequisites:
            m[f].append(t)
            d[t] += 1
        que = []
        for i in range(numCourses):
            if d[i] == 0:
                que.append(i)
        while que:
            f = que.pop(0)
            ret.append(f)
            for t in m[f]:
                d[t] -= 1
                if d[t] == 0:
                    que.append(t)
        return [[],ret][len(ret) == numCourses]
        
