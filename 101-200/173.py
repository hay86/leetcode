# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.q = [] if root is None else [root]

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.q) > 0:
            while self.q[-1].left is not None:
                left = self.q[-1].left
                self.q[-1].left = None
                self.q.append(left)
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            root = self.q.pop()
            if root.right is not None:
                self.q.append(root.right)
            return root.val
        return None

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
