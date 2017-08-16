# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q1 = [] if root is None else [root]
        q2 = []
        ret = []
        reverse = False
        while len(q1) > 0:
            if reverse:
                ret.append([q1[i].val for i in range(len(q1)-1, -1, -1)])
                reverse = False
            else:
                ret.append([q1[i].val for i in range(len(q1))])
                reverse = True
            for x in q1:
                if x.left is not None:
                    q2.append(x.left)
                if x.right is not None:
                    q2.append(x.right)
            q1 = q2
            q2 = []
        return ret
