# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
    	queue = deque([root])
    	while len(queue) > 0:
    		root = queue.popleft()
    		if root is None or root.left is None and root.right is None:
    			continue
    		if root.left is not None:
    			if root.right is not None:
    				root.left.next = root.right
    				p = root.right
    			else:
    				p = root.left
    		else:
    			p = root.right
    		q = root
    		while q.next is not None:
    			q = q.next
    			if q.left is not None:
    				p.next = q.left
    				break
    			if q.right is not None:
    				p.next = q.right
    				break
    		if root.left is not None:
    			queue.append(root.left)
    		if root.right is not None:
    			queue.append(root.right)
