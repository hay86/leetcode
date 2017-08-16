class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        node = set()
        edge = {}
        for i,v in enumerate(equations):
            edge[(v[0],v[1])] = values[i]
            edge[(v[1],v[0])] = 1/values[i]
            node.add(v[0])
            node.add(v[1])
        for k in node:
            for i in node:
                for j in node:
                    if (i,k) in edge and (k,j) in edge:
                        if (i,j) not in edge:
                            edge[(i,j)] = edge[(i,k)] * edge[(k,j)]
                        else:
                            edge[(i,j)] = min(edge[(i,j)], edge[(i,k)] * edge[(k,j)])
        ret = []
        for q in queries:
            if (q[0], q[1]) in edge:
                ret.append(edge[(q[0],q[1])])
            else:
                ret.append(-1.0)
        return ret
        
