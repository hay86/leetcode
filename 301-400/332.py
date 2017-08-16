class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        size = len(tickets)
        if size == 0:
            return [u'JFK']
        g = {}
        e = {}
        d = {}
        for f,t in tickets:
            e[(f,t)] = e[(f,t)]+1 if (f,t) in e else 1
            d[f] = d[f]+1 if f in d else 1
            d[t] = d[t]+1 if t in d else 1
            if f in g:
                g[f].add(t)
            else:
                g[f] = set([t])
        for k,v in g.items():
            g[k] = sorted(v)
        ret = [u'JFK']
        self.dfs(u'JFK', g, e, d, size, ret)
        return ret
    
    def dfs(self, f, g, e, d, n, ret):
        for t in g[f]:
            if e[(f,t)] == 0 or d[t] == 0:
                continue
            if d[t] == 1:
                if n == 1:
                    d[f], d[t], e[(f,t)] = d[f]-1, d[t]-1, e[(f,t)]-1
                    ret.append(t)
                    return True
            else:
                d[f], d[t], e[(f,t)] = d[f]-1, d[t]-1, e[(f,t)]-1
                ret.append(t)
                if self.dfs(t, g, e, d, n-1, ret):
                    return True
                d[f], d[t], e[(f,t)] = d[f]+1, d[t]+1, e[(f,t)]+1
                ret.pop()
        return False
        
