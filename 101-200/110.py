# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) is not False
    
    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if l is False or r is False:
            return False
        if abs(l-r) > 1:
            return False
        return max(l, r) + 1
