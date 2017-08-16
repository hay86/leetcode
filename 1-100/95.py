# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return [None]
        q = [TreeNode(1)]
        for i in range(2, n+1):
            p = []
            node = TreeNode(i)
            while len(q) > 0:
                root = q.pop()
                node.left = root
                p.append(self.copy(node))
                node.left = None
                tmp = root
                while tmp is not None:
                    right = tmp.right
                    tmp.right = node
                    node.left = right
                    p.append(self.copy(root))
                    tmp.right = right
                    node.left = None
                    tmp = tmp.right
            q = p
        return q
        
    def copy(self, root):
        if root is None:
            return None
        node = TreeNode(root.val)
        if root.left is not None:
            node.left = self.copy(root.left)
        if root.right is not None:
            node.right = self.copy(root.right)
        return node
