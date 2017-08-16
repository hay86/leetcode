# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return node
        g = {}
        v = set()
        v.add(node.label)
        q = [node]
        l = node.label
        while len(q) > 0:
            node = q.pop(0)
            if node.label not in g:
                g[node.label] = UndirectedGraphNode(node.label)
            for subnode in node.neighbors:
                if subnode.label not in g:
                    g[subnode.label] = UndirectedGraphNode(subnode.label)
                g[node.label].neighbors.append(g[subnode.label])
                if subnode.label not in v:
                    v.add(subnode.label)
                    q.append(subnode)
        return g[l]
                
            
