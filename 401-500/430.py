"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        head, tail = self.dfs(head)
        return head
        
    def dfs(self, head):
        p = head
        tail = p
        while p:
            if p.child:
                start, end = self.dfs(p.child)
                p.child = None
                q = p.next
                p.next, start.prev, end.next = start, p, q
                if q:
                    q.prev = end
            tail = p
            p = p.next
        return head, tail
