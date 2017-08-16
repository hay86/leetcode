# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        h = 1
        r = root
        while r.right is not None:
            r = r.right
            h += 1
        return self.count(root, h)
        
    def count(self, root, h):
        if root is None:
            return 0
        if root.left is None:
            return 1
        h2 = 2
        r = root.left
        while r.right is not None:
            r = r.right
            h2 += 1
        if h2 == h:
            return self.count(root.left, h-1) + 2**(h-1)
        else:
            return 2**h + self.count(root.right, h-1)
