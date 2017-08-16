# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        i = (len(nums)-1)/2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[0:i])
        root.right = self.sortedArrayToBST(nums[i+1:])
        return root
