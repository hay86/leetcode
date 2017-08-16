class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        size = len(candidates)
        unique_candidates = [] if size == 0 else [candidates[0]]
        for i in range(1, size):
            if candidates[i] != candidates[i-1]:
                unique_candidates.append(candidates[i])
        ret = []
        self.dfs(unique_candidates, target, ret, [], len(unique_candidates), 0)
        return ret
        
    def dfs(self, candidates, target, ret, ans, size, k):
        while k < size:
            c = candidates[k]
            if c == target:
                ret.append(ans+[c])
            elif c < target:
                ans.append(c)
                self.dfs(candidates, target-c, ret, ans, size, k)
                ans.pop()
            else:
                break
            k += 1
