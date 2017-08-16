# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, preorder, 0, len(inorder), 0, len(preorder))
        
    def build(self, inorder, preorder, l1, r1, l2, r2):
        if l1 >= r1:
            return None
        root = TreeNode(preorder[l2])
        for i in range(l1, r1):
            if inorder[i] == preorder[l2]:
                break
        root.left = self.build(inorder, preorder, l1, i, l2+1, l2+i-l1+1)
        root.right = self.build(inorder, preorder, i+1, r1, l2+i-l1+1, r2)
        return root      
