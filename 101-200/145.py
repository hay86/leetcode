# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root is not None:
            q = [root]
            while len(q) > 0:
                left = q[-1].left
                right = q[-1].right
                q[-1].left = None
                q[-1].right = None
                if left is None and right is None:
                    root = q.pop()
                    ret.append(root.val)
                if right is not None:
                    q.append(right)
                if left is not None:
                    q.append(left)
        return ret
