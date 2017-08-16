# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if root is not None:
            self.dfs(root, [], ret)
        return ret
    
    def dfs(self, root, path, ret):
        path.append(str(root.val))
        if root.left is not None:
            self.dfs(root.left, path, ret)
        if root.right is not None:
            self.dfs(root.right, path, ret)
        if root.left is None and root.right is None:
            ret.append('->'.join(path))
        path.pop()
