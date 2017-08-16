# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        q = [root]
        ret = 0
        while len(q) > 0:
            root = q.pop(0)
            if root.left is None and root.right is None:
                ret += root.val
            else:
                if root.left is not None:
                    root.left.val += 10*root.val
                    q.append(root.left)
                if root.right is not None:
                    root.right.val += 10*root.val
                    q.append(root.right)
        return ret
