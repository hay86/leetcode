# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        head = TreeNode(2147483649)
        head.left = root
        parent, node = head, head.left
        while node:
            if node.val == key:
                break
            elif node.val > key:
                parent, node = node, node.left
            else:
                parent, node = node, node.right
        if node:
            self.find_and_replace(parent, node)
        return head.left

    def find_and_replace(self, parent, node):
        p, n = parent, node
        if n.right:
            p, n = n, n.right
            while n.left:
                p, n = n, n.left
            node.val = n.val
            self.find_and_replace(p, n)
        elif n.left:
            p, n = n, n.left
            while n.right:
                p, n = n, n.right
            node.val = n.val
            self.find_and_replace(p, n)
        else:
            if p.left == n:
                p.left = None
            else:
                p.right = None


