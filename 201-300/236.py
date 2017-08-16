# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ans = []
        self.dfs(root, p, q, [], ans)
        x, y = ans[0], ans[1]
        for i in range(min(len(x), len(y))):
            if x[i] != y[i]:
                break
            root = root.left if x[i] == 0 else root.right
        return root
        
    def dfs(self, root, p, q, i, ans):
        if root == p or root == q:
            ans.append(list(i))
        if len(ans) == 2:
            return
        if root.left is not None:
            i.append(0)
            self.dfs(root.left, p, q, i, ans)
            i.pop()
        if root.right is not None:
            i.append(1)
            self.dfs(root.right, p, q, i, ans)
            i.pop()
