# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q1 = [] if root is None else [root]
        q2 = []
        ret = 0
        while len(q1) > 0:
            ret += 1
            for x in q1:
                if x.left is None and x.right is None:
                    return ret
                else:
                    if x.left is not None:
                        q2.append(x.left)
                    if x.right is not None:
                        q2.append(x.right)
            q1 = q2
            q2 = []
        return 0
