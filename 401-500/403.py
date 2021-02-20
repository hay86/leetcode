class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        s = [set() for i in range(len(stones))]
        s[0].add(0)
        for i in range(1, len(stones)):
            for j in range(i-1,-1,-1):
                step = stones[i]-stones[j]
                if step > j+1:
                    if j == i-1:
                        return False
                    break
                if step in s[j] or step+1 in s[j] or step-1 in s[j]:
                    if i == len(stones)-1:
                        return True
                    s[i].add(step)
        return False
        
