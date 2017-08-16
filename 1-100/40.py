class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        size = len(candidates)
        ret = []
        self.dfs(candidates, target, ret, [False]*size, size, 0)
        return ret
        
    def dfs(self, candidates, target, ret, flag, size, k):
        while k < size:
            c = candidates[k]
            if c == target:
                if k == 0 or candidates[k] != candidates[k-1] or flag[k-1]:
                    ans = []
                    for i in range(size):
                        if flag[i]:
                            ans.append(candidates[i])
                    ans.append(c)
                    ret.append(ans)
            elif c < target:
                if k == 0 or candidates[k] != candidates[k-1] or flag[k-1]:
                    flag[k] = True
                    self.dfs(candidates, target-c, ret, flag, size, k+1)
                    flag[k] = False
            else:
                break
            k += 1
