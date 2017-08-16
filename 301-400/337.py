# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.dfs(root))
        
    def dfs(self, root):
        li, le, ri, re = 0, 0, 0, 0
        if root.left is not None:
            li, le = self.dfs(root.left)
        if root.right is not None:
            ri, re = self.dfs(root.right)
        return root.val+le+re, max(le+re, le+ri, li+re, li+ri)
