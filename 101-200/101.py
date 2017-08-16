# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymmetric2(root.left, root.right)
    
    def isSymmetric2(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            if left.val != right.val:
                return False
            return self.isSymmetric2(left.left, right.right) and self.isSymmetric2(left.right, right.left)
        else:
            return False
            
