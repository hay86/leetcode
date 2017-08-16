# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        cur, prev, A, B = None, None, None, None
        while root is not None:
            visit = False
            if root.left is None:
                visit = True
                cur, prev = root, cur
                root = root.right
            else:
                left = root.left
                while left.right is not None and left.right != root:
                    left = left.right
                if left.right is None:
                    left.right = root
                    root = root.left
                else:
                    visit = True
                    cur, prev = root, cur
                    root = root.right
                    left.right = None
                    
            if visit and cur is not None and prev is not None and cur.val < prev.val:
                if A is None:
                    A = prev
                B = cur
        
        if A is not None and B is not None:
            tmp = A.val
            A.val = B.val
            B.val = tmp
        
