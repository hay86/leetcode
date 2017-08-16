# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root is not None:
            q = [root]
            while len(q) > 0:
                node = q.pop()
                ret.append(node.val)
                if node.right != None:
                    q.append(node.right)
                if node.left != None:
                    q.append(node.left)
        return ret
