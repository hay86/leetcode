class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = [0] * numCourses
        g = {}
        for arr in prerequisites:
            if arr[1] not in g:
                g[arr[1]] = set()
            if arr[0] not in g[arr[1]]:
                g[arr[1]].add(arr[0])
                d[arr[0]] += 1
        while True:
            i = 0
            while i < numCourses:
                if d[i] == 0:
                    d[i] = -1
                    break
                i += 1
            if i == numCourses:
                break
            if i in g:
                for j in g[i]:
                    d[j] -= 1
        return max(d) <= 0
