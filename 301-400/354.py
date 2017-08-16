class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        env = set()
        for x,y in envelopes:
            env.add((x,y))
        env = sorted(env, key=lambda x: (x[0],-x[1]))
        ret = []
        
        for i, e in enumerate(env):
            l,r = 0, len(ret)-1
            while l<=r:
                m = (l+r)/2
                if env[ret[m]][1] >= e[1]:
                    r = m-1
                else:
                    l = m+1
            if l >= len(ret):
                ret.append(i)
            else:
                ret[l] = i
            
        return len(ret)
        
            
        
