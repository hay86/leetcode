# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        left_total = self.total(root.left) 
        if k == left_total+1:
            return root.val
        elif k <= left_total:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-left_total-1)
        
    def total(self, root):
        if root is None:
            return 0
        return 1 + self.total(root.left) + self.total(root.right)
