class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ret = []
        self.dfs(s, [], ret)
        return ret
        
    def dfs(self, s, r, ret):
    	if len(s) == 0:
    		ret.append(list(r))
    	else:
    		for i in range(len(s)):
    			flag = True
    			for j in range(int(i/2)+1):
    				if s[j] != s[i-j]:
    					flag = False
    					break
    			if flag:
    				r.append(s[:i+1])
    				self.dfs(s[i+1:], r, ret)
    				r.pop()
