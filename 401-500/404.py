# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        if root is not None:
            self.dfs(root, False)
        return self.ret
        
    def dfs(self, root, left):
        if root.left is None and root.right is None:
            if left:
                self.ret += root.val
        else:
            if root.left is not None:
                self.dfs(root.left, True)
            if root.right is not None:
                self.dfs(root.right, False)
