# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        ret, min, max = self.isValid(root)
        return ret
        
    def isValid(self, root):
        lmin, rmax = root.val, root.val
        if root.left is not None:
            ret, lmin, lmax = self.isValid(root.left)
            if not ret or lmax >= root.val:
                return False, None, None
        if root.right is not None:
            ret, rmin, rmax = self.isValid(root.right)
            if not ret or rmin <= root.val:
                return False, None, None
        return True, lmin, rmax
