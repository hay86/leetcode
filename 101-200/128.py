class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        size = {}
        for x in nums:
            if x in map:
                continue
            if x+1 in map and x-1 in map:
                root1 = self.root(map, x+1)
                root2 = self.root(map, x-1)
                if root1 != root2:
                    map[x] = root2
                    map[root1] = root2
                    size[root2] += (size[root1] + 1)
            elif x+1 in map:
                map[x] = self.root(map, x+1)
                size[map[x]] += 1
            elif x-1 in map:
                map[x] = self.root(map, x-1)
                size[map[x]] += 1
            else:
                map[x] = x
                size[x] = 1
        return 0 if len(size) == 0 else max(size.values())
    
    def root(self, map, x):
        if map[x] != x:
            tmp = self.root(map, map[x])
            if map[x] != tmp:
                map[x] = tmp
        return map[x]
