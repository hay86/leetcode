# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None or root.left is None and root.right is None:
            return
        if root.left is not None:
            self.flatten(root.left)
        if root.right is not None:
            self.flatten(root.right)
        if root.left is not None:
            left = root.left
            while left.right is not None:
                left = left.right
            right = root.right
            root.right = root.left
            root.left = None
            left.right = right
        
