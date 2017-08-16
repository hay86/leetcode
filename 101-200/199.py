# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q1 = [] if root is None else [root]
        q2 = []
        ret = []
        while len(q1) > 0:
            ret.append(q1[-1].val)
            for x in q1:
                if x.left is not None:
                    q2.append(x.left)
                if x.right is not None:
                    q2.append(x.right)
            q1 = q2
            q2 = []
        return ret
