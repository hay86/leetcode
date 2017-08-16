# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root is not None:
            q = [root]
            while len(q) > 0:
                node = q.pop()
                if node.right is not None:
                    q.append(node.right)
                    node.right = None
                if node.left is None:
                    ret.append(node.val)
                else:
                    tmp = node.left
                    node.left = None
                    q.append(node)
                    q.append(tmp)
        return ret
