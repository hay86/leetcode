# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, postorder, 0, len(inorder), 0, len(postorder))
        
    def build(self, inorder, postorder, l1, r1, l2, r2):
        if l1 >= r1:
            return None
        root = TreeNode(postorder[r2-1])
        for i in range(l1, r1):
            if inorder[i] == postorder[r2-1]:
                break
        root.left = self.build(inorder, postorder, l1, i, l2, l2+i-l1)
        root.right = self.build(inorder, postorder, i+1, r1, l2+i-l1, r2-1)
        return root
