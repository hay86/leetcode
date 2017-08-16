# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(root, sum, [], ans)
        return ans
    
    def dfs(self, root, sum, path, ans):
        if root is None:
            return
        path.append(root.val)
        if root.left is None and root.right is None and root.val == sum:
            ans.append(list(path))
        if root.left is not None:
            self.dfs(root.left, sum - root.val, path, ans)
        if root.right is not None:
            self.dfs(root.right, sum - root.val, path, ans)
        path.pop()
