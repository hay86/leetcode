# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.ret = -2147483648
        self.dfs(root)
        return self.ret
    
    def dfs(self, root):
        m1, m2 = 0, 0
        if root.left is not None:
            m1 = max(m1, self.dfs(root.left))
        if root.right is not None:
            m2 = max(m2, self.dfs(root.right))
        v = m1 + m2 + root.val
        v1, v2 = m1 + root.val, m2 + root.val
        if v > self.ret:
            self.ret = v
        return v1 if v1 >= v2 else v2
