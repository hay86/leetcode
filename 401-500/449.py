# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self._deserialize(data.split(','), [0])

    def _deserialize(self, data, pos):
        if data[pos[0]] == '#':
            pos[0] += 1
            return None
        root = TreeNode(int(data[pos[0]]))
        pos[0] += 1
        root.left = self._deserialize(data, pos)
        root.right = self._deserialize(data, pos)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))