"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ret = []
        level = []
        q = deque([root, None])
        while q:
            e = q.popleft()
            if e is None:
                if level:
                    ret.append(level)
                    level = []
                    q.append(None)
            else:
                level.append(e.val)
                q.extend(e.children)
        return ret
